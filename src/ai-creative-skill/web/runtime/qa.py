"""Scoped technical QA for static sites. Browser verification is optional; no claim of WCAG or conversions."""
import datetime,hashlib,json,pathlib,re,subprocess,urllib.parse,shutil
from bs4 import BeautifulSoup
from .validate import build_hash

def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def check(id,requirement,criticality,result,mode,evidence,hash,viewport=None,reason=None):
    c={'check_id':id,'requirement':requirement,'criticality':criticality,'procedure':id.replace('_',' '),'result':result,'evidence_mode':mode,'evidence_ref':evidence,'build_hash':hash,'viewport':viewport,'checked_at':now()}
    if reason:c['reason']=reason
    return c

ABSOLUTE_PATH=re.compile(r'(?<![\w:/.])(?:[A-Za-z]:[\\/]|/)(?:[^\s:\'"()<>]+[/\\])+[^\s:\'"()<>]*')
FILE_URI=re.compile(r'(?<![\w-])file:(?://)?[^\s\'"<>()]*',re.I)

def redact(text,*roots):
    """Evidence must not carry local directory names: known roots become '.', other absolute paths and file: URIs '<path>'."""
    text=str(text)
    names=sorted({str(x) for x in roots if x}|{pathlib.PurePath(str(x)).as_posix() for x in roots if x},key=len,reverse=True)
    def strip(t):  # a root counts only as a whole absolute-path prefix, never inside a relative path or URL
        for r in names:t=re.sub(r'(?<![\w/.:-])'+re.escape(r)+r'(?=[/\\\s\'"<>()]|$)','.',t)
        return t
    def uri(m):  # file:///C:/x%20y/a.png -> C:/x y/a.png; inside a known root -> ./a.png, otherwise <path>
        path=urllib.parse.unquote(urllib.parse.urlsplit(m.group(0)).path)
        path=path[1:] if re.match(r'/[A-Za-z]:/',path) else path
        out=strip(path);return out if out!=path else '<path>'
    return ABSOLUTE_PATH.sub('<path>',strip(FILE_URI.sub(uri,text)))

JS_COMMENT=re.compile(r'/\*.*?\*/|(?:^|(?<=[\s;{}(),]))//[^\n]*',re.S|re.M)
def strip_js_comments(text):
    """Remove /* */ and // comments (a // right after ':' as in a URL is kept); approximate, enough to ignore mentions."""
    return JS_COMMENT.sub(' ',text)

def srcset_urls(value):
    """URLs of a srcset; data: URLs may contain commas, so a candidate ends at whitespace or at a comma that ends the URL."""
    out=[]
    for m in re.finditer(r'\s*([^\s]+)(?:\s+[^,]*)?(?:,|$)',value or ''):
        url=m.group(1)
        if url.startswith('data:'):continue
        out+=[u for u in url.split(',') if u] if not re.search(r'\s',url) and ',' in url and not url.startswith('data:') else [url]
    return [u for u in out if u]

def project_files(root,project_root,files):
    """Express site files relative to the project root used by validate.check."""
    prefix=root.relative_to(project_root)
    return [(prefix/f).as_posix() for f in files]

def static_audit(root,project_root=None):
    root=pathlib.Path(root).resolve();html=root/'index.html'
    project_root=pathlib.Path(project_root).resolve() if project_root else root
    if not root.is_relative_to(project_root):raise ValueError('Site root must be inside the project root')
    if not html.exists():raise ValueError('No index.html')
    code=html.read_text();soup=BeautifulSoup(code,'html.parser')
    js_files=[x.get('src') for x in soup.find_all('script') if x.get('src') and not x.get('src').startswith('http')]
    css_files=[x.get('href') for x in soup.find_all('link') if x.get('rel')==['stylesheet'] and x.get('href')]
    local=[x.get('src') for x in soup.find_all('img') if x.get('src')]+js_files+css_files
    missing=[p for p in local if not p.startswith(('http:','https:','data:')) and not (root/p).is_file()]
    fragments=[x['href'][1:] for x in soup.find_all('a',href=True) if x['href'].startswith('#') and len(x['href'])>1]
    # "#/route" and "#!/route" are client-side routes, not element ids; they need a browser check.
    hash_routes=[f for f in fragments if f.startswith(('/','!'))]
    anchors=[urllib.parse.unquote(f) for f in fragments if not f.startswith(('/','!'))]
    ids={n.get('id') for n in soup.find_all(id=True)}
    bad=[a for a in anchors if a not in ids]
    js_errors=[]
    for js in js_files:
        if (root/js).exists():
            # Relative path and cwd keep absolute local directories out of the evidence file.
            try:subprocess.run(['node','--check',js],cwd=root,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=12,text=True)
            except subprocess.CalledProcessError as e:
                detail=next((l for l in (e.stderr or '').splitlines() if re.match(r'\w*Error\b',l)),'syntax check failed')
                js_errors.append(js+': '+redact(detail,project_root,root)[:160])
            except (OSError,subprocess.TimeoutExpired) as e:js_errors.append(js+': '+type(e).__name__)
    css='\n'.join((root/p).read_text(errors='replace') for p in css_files if (root/p).exists())
    # ES modules, fetch/XHR and dynamic import do not work from file://: such pages need an HTTP preview to be judged.
    # Executable scripts only (no type, a JavaScript type or module; JSON-LD and templates are data), comments removed.
    runnable=lambda x:(x.get('type') or 'text/javascript').strip().lower() in ('text/javascript','application/javascript','module','')
    scripts=[strip_js_comments(t) for t in [x.get_text() for x in soup.find_all('script') if not x.get('src') and runnable(x)]
        +[(root/j).read_text(errors='replace') for j in js_files if (root/j).is_file() and j.lower().endswith(('.js','.mjs'))]]
    needs_http=sorted({'ES module script' for x in soup.find_all('script') if (x.get('type') or '').strip().lower()=='module'}
        |{name for name,rx in (('fetch()',r'\bfetch\s*\('),('XMLHttpRequest',r'\bXMLHttpRequest\b'),('dynamic import()',r'\bimport\s*\(')) if any(re.search(rx,t) for t in scripts)})
    files=project_files(root,project_root,['index.html']+css_files+js_files)
    return {'source_hash':build_hash(project_root,files),'files':files,'hash_routes':hash_routes,'assets_found':len(local)-len(missing),'missing_assets':missing,'broken_anchors':bad,'js_errors':js_errors,'needs_http':needs_http,'reduced_motion_css_declared':'prefers-reduced-motion' in css,'form_count':len(soup.find_all('form')),'external_links':[x['href'] for x in soup.find_all('a',href=True) if x['href'].startswith(('http://','https://'))],'primary_link_candidates':[x.get('href') for x in soup.select('a.button,a.primary,a.nav-cta')]}

VIEWPORTS=[(1440,900,'desktop_render'),(390,844,'mobile_render'),(320,640,'narrow_render')]
SETTLE_JS='''async () => {
  // Bounded: infinite-scroll pages grow while scrolling, so cap steps and time.
  const step = Math.max(200, Math.floor(window.innerHeight * 0.8)), t0 = performance.now();
  for (let i = 0, y = 0; i < 60 && y < document.documentElement.scrollHeight && performance.now() - t0 < 8000; i++, y += step) {
    window.scrollTo(0, y); await new Promise(r => setTimeout(r, 60));
  }
  window.scrollTo(0, 0);
  await Promise.all([...document.images].filter(i => !i.complete).map(i => new Promise(r => {
    i.addEventListener('load', r, {once: true}); i.addEventListener('error', r, {once: true}); setTimeout(r, 3000);
  })));
  return [...document.images].filter(i => !i.complete).length;
}'''
# Laid out (has client rects, so not display:none), visible, decoded at a real size, yet drawn under 16 px: a collapsed box.
# Image source as authored (src or first srcset URL); currentSrc only as a last resort, made relative to the page.
# Name of the image as the page loads it: over HTTP the resolved currentSrc (relative to the page when same-origin, so the
# srcset candidate that actually loaded or failed is named); under file:// the authored src or first srcset URL, so no
# local path is ever produced.
IMG_SRC_JS=r'''const srcOf = i => { const authored = i.getAttribute('src') || ((i.getAttribute('srcset') || '').trim().split(/\s+/)[0] || '').replace(/,$/, '');
  try { const u = new URL(i.currentSrc || authored, location.href), b = new URL('.', location.href);
    if (u.protocol !== 'file:' && i.currentSrc) return u.origin === b.origin && u.href.startsWith(b.href) ? decodeURIComponent(u.href.slice(b.href.length)) : u.href;
  } catch (e) {}
  return authored || '<path>'; };'''
# Real collapse only: a drawn side under 2 px, or a side under 16 px with the aspect distorted more than 2x, or a sized image
# clipped by a collapsed overflow container. Not collapsed: images hidden by display/visibility/opacity, by sr-only style
# zero-area clipping, inside panels the page declares closed (hidden, inert, aria-hidden="true", role="tabpanel", or the
# target of aria-controls on an element with aria-expanded="false"), and small icons drawn at their own aspect.
COLLAPSED_IMAGES_JS='''() => { '''+IMG_SRC_JS+r'''
  const nums = t => (t.match(/-?[\d.]+/g) || []).map(Number);
  const srOnlyClip = cs => { if (cs.clip && cs.clip.startsWith('rect(')) { const [t, r, b, l] = nums(cs.clip); if (b - t <= 1 || r - l <= 1) return true; }
    const cp = cs.clipPath || 'none'; return /inset\(\s*(50|100)%/.test(cp) || /circle\(\s*0(px|%)?\s/.test(cp + ' '); };
  const closedPanel = e => e.hidden || e.inert || e.getAttribute('aria-hidden') === 'true' || e.getAttribute('role') === 'tabpanel'
    || (e.id && document.querySelector('[aria-expanded="false"][aria-controls~="' + CSS.escape(e.id) + '"]'));
  const exempt = i => { if (i.checkVisibility && !i.checkVisibility({opacityProperty: true, visibilityProperty: true})) return true;
    for (let e = i; e && e !== document.body; e = e.parentElement) { if (closedPanel(e) || srOnlyClip(getComputedStyle(e))) return true; } return false; };
  const collapsedParent = i => { for (let e = i.parentElement; e && e !== document.body; e = e.parentElement) {
      const cs = getComputedStyle(e), r = e.getBoundingClientRect();
      if ((cs.overflowX !== 'visible' && r.width < 2) || (cs.overflowY !== 'visible' && r.height < 2)) return true; } return false; };
  return [...document.images].filter(i => i.complete && i.naturalWidth >= 64 && i.naturalHeight >= 64 && i.getClientRects().length > 0 && !exempt(i))
    .filter(i => { const r = i.getBoundingClientRect(), w = r.width, h = r.height;
      if (Math.min(w, h) < 2) return true;
      const distortion = Math.max((w / h) / (i.naturalWidth / i.naturalHeight), (i.naturalWidth / i.naturalHeight) / (w / h));
      return (Math.min(w, h) < 16 && distortion > 2) || (Math.min(w, h) >= 16 && collapsedParent(i)); })
    .map(srcOf); }'''
BROKEN_IMAGES_JS='''() => { '''+IMG_SRC_JS+'''
  return [...document.images].filter(i => (i.currentSrc || i.getAttribute('src')) && i.complete && i.naturalWidth === 0).map(srcOf); }'''
# Visible content: text, decoded images, or drawn canvas, svg and video (WebGL, illustration or video-only pages).
CONTENT_JS='''() => { const shown = e => { const r = e.getBoundingClientRect(); return r.width >= 2 && r.height >= 2 && (!e.checkVisibility || e.checkVisibility({opacityProperty: true, visibilityProperty: true})); };
  return {text: (document.body && document.body.innerText || '').trim().length,
    images: [...document.images].filter(i => i.naturalWidth > 0 && i.getClientRects().length).length
      + [...document.querySelectorAll('canvas, svg, video')].filter(shown).length}; }'''
FILE_BLOCK=re.compile(r'CORS|cross[- ]origin|origin .null.|module|Failed to fetch|XMLHttpRequest',re.I)
FONT_CORS=re.compile(r'\bfont\b|woff2?\b|\.ttf\b|\.otf\b',re.I)
CAPTURE_MAX=16000  # px; a capture of an endlessly growing page must not exhaust the time budget
RENDER_CHECKS=('browser_render','desktop_render','mobile_render','narrow_render','images_rendered')

def browser_pass(root,out,rel,h,target,file_mode,static,redact_):
    """Open the page at each viewport. Returns (checks, blocker, page_errors). One failing viewport does not discard the others."""
    from playwright.sync_api import sync_playwright
    checks=[];errors=[];collapsed=[];broken=[];notes=[];shots={};observed=[]
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True,executable_path=shutil.which('chromium') or shutil.which('chromium-browser') or None,args=['--no-sandbox'])
        try:
            for width,height,check_id in VIEWPORTS:
                page=browser.new_page(viewport={'width':width,'height':height},reduced_motion='reduce')
                page.on('pageerror',lambda e:errors.append('pageerror: '+str(e)[:160]))
                page.on('console',lambda m:errors.append('console: '+m.text[:160]) if m.type=='error' else None)
                page.on('requestfailed',lambda r:errors.append('requestfailed: '+r.url[:160]))
                try:
                    response=page.goto(target,wait_until='load',timeout=12000)
                    if not file_mode and (response is None or response.status!=200):
                        checks.append(check(check_id,f'Page rendered at {width} without horizontal overflow','ESSENTIAL','NOT_TESTED','NONE',None,h,str(width),reason=f'HTTP status unavailable or {getattr(response,"status",None)}'));continue
                    try:pending=page.evaluate(SETTLE_JS)
                    except Exception as e:pending=None;notes.append(f'Scroll before capture failed at {width}: {type(e).__name__}')
                    page.wait_for_timeout(200)
                    full=page.evaluate('document.documentElement.scrollHeight')
                    e=f'viewport_{width}.png'
                    page.screenshot(path=str(out/e),full_page=True,clip={'x':0,'y':0,'width':width,'height':max(height,min(full,CAPTURE_MAX))},timeout=12000)
                    overflow=page.evaluate('document.documentElement.scrollWidth - window.innerWidth');content=page.evaluate(CONTENT_JS)
                    shots[width]=rel(e);failed=overflow>1
                    checks.append(check(check_id,f'Page rendered at {width} without horizontal overflow','ESSENTIAL','FAIL' if failed else 'PASS','BROWSER_OBSERVED',rel(e),h,str(width),reason=f'Horizontal overflow of {overflow}px observed' if failed else None))
                    if width in (1440,390):
                        collapsed+=[f'{redact_(c)[:120]} at {width}' for c in page.evaluate(COLLAPSED_IMAGES_JS)];observed.append(str(width))
                    if width==1440:
                        blank=content['text']<20 and content['images']==0
                        checks.append(check('browser_render','Actual HTML opened with visible content','ESSENTIAL','FAIL' if blank else 'PASS','BROWSER_OBSERVED',rel(e),h,'1440',reason='Page rendered no visible text or images' if blank else None))
                        broken=page.evaluate(BROKEN_IMAGES_JS)
                        if pending:notes.append(f'{pending} image(s) not loaded after scrolling (hidden or still pending); not verified')
                        if full>CAPTURE_MAX:notes.append(f'Capture limited to the first {CAPTURE_MAX}px of a {full}px page')
                except Exception as ex:
                    checks.append(check(check_id,f'Page rendered at {width} without horizontal overflow','ESSENTIAL','NOT_TESTED','NONE',None,h,str(width),reason=f'Viewport {width} not completed: {type(ex).__name__}'))
                finally:page.close()
        finally:browser.close()
    if observed:
        if broken:notes.insert(0,'Images failed to load: '+', '.join(redact_(b)[:120] for b in broken[:8]))
        if collapsed:notes.insert(0,'Images collapsed: '+', '.join(collapsed[:8]))
        checks.append(check('images_rendered','Referenced images decoded after scrolling and not collapsed','ESSENTIAL','FAIL' if broken or collapsed else 'PASS','BROWSER_OBSERVED',shots.get(1440) or shots.get(390),h,','.join(observed),reason='; '.join(notes) or None))
    page_errors=[redact_(x) for x in dict.fromkeys(errors)][:8]
    # Errors that mean the page cannot work from file:// (a font preload CORS message is harmless: the font still loads).
    file_blocked=[x for x in page_errors if x.startswith('pageerror') or (x.startswith('console') and FILE_BLOCK.search(x) and not FONT_CORS.search(x))]
    if file_mode and (static['needs_http'] or file_blocked):
        why=', '.join(static['needs_http']) or 'errors reported by the page'
        reason=f'Opened via file:// but the page uses {why}; needs an HTTP preview (--url)' if static['needs_http'] else f'Page reported errors under file://; needs an HTTP preview (--url) to confirm'
        checks=[check(c['check_id'],c['requirement'],c['criticality'],'NOT_TESTED','NONE',None,h,c['viewport'],reason=reason) if c['check_id'] in RENDER_CHECKS else c for c in checks]
        return checks,reason,page_errors
    return checks,None,page_errors

def audit(root,out_dir,base_url=None,project_root=None,open_file=True,browser=True,skip_reason=None):
    """QA evidence may live outside the site (so it never ships with it) but must stay inside the project root,
    which is the root later passed to validate.check. Evidence refs are always relative, never absolute.
    Without base_url the browser opens index.html via file://; browser=False keeps the audit static."""
    root=pathlib.Path(root).resolve();project_root=pathlib.Path(project_root).resolve() if project_root else root
    out=pathlib.Path(out_dir).resolve()
    if not root.is_relative_to(project_root):raise ValueError('Site root must be inside the project root')
    if not out.is_relative_to(project_root):raise ValueError('QA evidence directory must be under the project root')
    out.mkdir(parents=True,exist_ok=True)
    rel=lambda name: (out/name).relative_to(project_root).as_posix()
    redact_=lambda x:redact(x,project_root,root,pathlib.Path.home())
    s=static_audit(root,project_root);h=s['source_hash'];(out/'static_audit.json').write_text(json.dumps(s,indent=2,ensure_ascii=False))
    checks=[check('assets_available','Local assets exist','ESSENTIAL','PASS' if not s['missing_assets'] else 'FAIL','STATIC_INSPECTED',rel('static_audit.json'),h),
      check('anchors_static','Local anchors resolve','ADVISORY','PASS' if not s['broken_anchors'] else 'FAIL','STATIC_INSPECTED',rel('static_audit.json'),h,reason=(f"{len(s['hash_routes'])} hash route link(s) not statically checkable" if s['hash_routes'] else None)),
      check('js_syntax','JavaScript syntax','ADVISORY','PASS' if not s['js_errors'] else 'FAIL','STATIC_INSPECTED',rel('static_audit.json'),h),
      check('content_truth','Product facts and rights','CRITICAL','NOT_TESTED','NONE',None,h,reason='Requires authoritative human/project evidence; source inspection alone insufficient')]
    opened_via=None;page_errors=[]
    target=base_url or ((root/'index.html').as_uri() if open_file else None)
    if not browser or not target:browser_reason=skip_reason or ('Static-only audit requested' if not browser else 'No preview URL and file:// opening disabled')
    else:
        try:
            found,browser_reason,page_errors=browser_pass(root,out,rel,h,target,not base_url,s,redact_)
            checks+=found
            if any(c['evidence_mode']=='BROWSER_OBSERVED' for c in found):opened_via='url' if base_url else 'file'
        except Exception as e:browser_reason=type(e).__name__+': '+redact_(e)[:250]
    present={c['check_id'] for c in checks}
    for k in RENDER_CHECKS+('cta_interaction','keyboard_interaction','responsive','reduced_motion','form_behavior'):
        if k not in present:
            checks.append(check(k,k.replace('_',' '),'ESSENTIAL' if k in RENDER_CHECKS+('cta_interaction','keyboard_interaction') else 'ADVISORY','NOT_TESTED','NONE',None,h,reason=browser_reason or 'Not completed' if k in RENDER_CHECKS else 'Requires explicit interaction test and appropriate evidence'))
    report={'status':'PARTIAL','build_hash':h,'checks':checks,'opened_via':opened_via,'needs_http':s['needs_http'],'page_errors':page_errors,'browser_blocker':browser_reason,'limits':['No real conversion or user study','No WCAG certification','No rights clearance','No human brand approval']}
    (out/'qa_matrix.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    return report

def todo(hint):return 'TODO: '+hint

def draft_record(root,qa_matrix,project_root=None,project=None):
    """Record draft from one QA run. Derivable fields are filled; judgement fields say TODO, so validate fails until filled."""
    root=pathlib.Path(root).resolve();project_root=pathlib.Path(project_root).resolve() if project_root else root
    q=json.loads(pathlib.Path(qa_matrix).read_text()) if not isinstance(qa_matrix,dict) else qa_matrix
    s=static_audit(root,project_root);h=s['source_hash']
    if q.get('build_hash')!=h:raise ValueError('QA matrix was produced from another build; run audit again')
    prefix=root.relative_to(project_root)
    soup=BeautifulSoup((root/'index.html').read_text(),'html.parser')
    # <img src>, every srcset URL and <source srcset>; root-relative URLs ('/assets/x') resolve against the site root.
    urls=[x.get('src') for x in soup.find_all('img')]+[u for x in soup.find_all(['img','source']) for u in srcset_urls(x.get('srcset'))]
    images=sorted({u.lstrip('/') for u in urls if u and not u.startswith(('http:','https:','data:','//'))})
    checks=q['checks'];browser=any(c['check_id']=='browser_render' and c['result']=='PASS' for c in checks)
    verdict='BLOCKED' if any(c['criticality']=='CRITICAL' and c['result']=='FAIL' for c in checks) else 'PARTIAL'
    enum=lambda *v:todo('one of '+' | '.join(v))
    limits=list(q.get('limits',[]))+(['Browser checks not completed: '+q['browser_blocker']] if q.get('browser_blocker') else [])
    index=(prefix/'index.html').as_posix()
    if q.get('needs_http') or q.get('opened_via')=='url':
        opening=f'Serve the site over HTTP (python scripts/creative_web.py preview start {prefix.as_posix() or "."}) and open the URL'+(f"; file:// is not enough because the page uses {', '.join(q['needs_http'])}" if q.get('needs_http') else '')
    else:opening=f'Open {index} in a browser (file://); hash routes work offline.'
    return {'schema_version':'0.2.0','route':'WEB_PREVIEW','mode':'FAST','project':project or root.name,'build_version':h[:12],
      'state':'PREVIEW_DRAFT','verdict':verdict,
      'execution':{'execution_mode':'MANUAL_SPEC_GUIDED','skill_package_version':todo('skill package version used'),
        'methods':[{'name':'WEB_EXPERIENCE Work Profile v0.2 FAST flow','state':'DOCUMENTED'}],
        'tools':['creative_web.py audit','creative_web.py record'],'paid_authorized':False,'public_deploy_authorized':False,'activation_evidence':None},
      'WEB_BRIEF':{'deliverable_scope':todo('what was built'),'business_kind':enum('PHYSICAL_PRODUCT','SERVICE','DIGITAL_PRODUCT','CREATOR','IDEA'),
        'user_goal':todo('visitor goal'),'audience_basis':todo('audience and its source'),'product_service_truth_refs':[todo('source of each product/service fact')],
        'known_unknown_boundary':[todo('what is unknown and was not claimed')],'brand_authority_state':enum('EXISTING_APPROVED','EXISTING_MIXED','PROVISIONAL','UNKNOWN'),
        'primary_action_intent':todo('single primary action'),'task_completion_condition':todo('what counts as done'),
        'product_material_scale_truth_state':todo('product facts vs unknowns (material, scale); required for PHYSICAL_PRODUCT, delete otherwise')},
      'WEB_DIRECTION':{'value_proposition':todo('one sentence'),'primary_cta_intent':todo('primary CTA and where it leads'),
        'sections_and_purpose':[{'id':todo('section id'),'purpose':todo('why the section exists')}],'visual_direction':todo('style, type, palette, imagery'),
        'creative_open_zones':[todo('what was left open')],'brand_alignment':todo('how the brand authority was respected'),
        'claim_and_offer_boundaries':todo('claims and offers not made')},
      'WEB_ASSET_PLAN':{'assets_used':[{'path':(prefix/i).as_posix(),'origin':todo('origin'),'approval':enum('APPROVED_FOR_THIS_USE','PROVISIONAL','LEGACY','UNKNOWN'),
          'rights':enum('CLEARED','UNKNOWN','RESTRICTED'),'use_scope':todo('approved use')} for i in images],
        'asset_authority_and_rights':todo('who approved the assets; add images set from CSS backgrounds or JS and remote images, which are not listed here'),
        'generation_required_decision':todo('was generation needed and authorised'),'product_identity_preservation':todo('how product identity was kept'),
        'provisional_vs_approved_labels':todo('which assets are provisional')},
      'WEB_PREVIEW_BUILD':{'preview_status':'AVAILABLE_VERIFIED' if browser else 'AVAILABLE_UNVERIFIED','source_files':s['files'],
        'verified_preview_ref_or_local_open_instructions':opening,
        'responsive_strategy':todo('breakpoints and mobile behaviour'),'working_interactions':[todo('each interaction that works')],
        'primary_cta_behavior':enum('REAL_VERIFIED_LINK','SAFE_LOCAL_DEMO','CONTACT_LINK_VERIFIED','WAITLIST_NOT_CONNECTED','MOCK_FORM_LABELED','DISABLED_PENDING_DESTINATION'),
        'real_vs_mock_integrations':todo('what is real and what is local or mocked'),'version_id':h[:12],
        'form_mode':enum('NONE','LOCAL_CALCULATION','EXTERNAL_SUBMISSION','MOCK_INPUT'),'external_link_targets':s['external_links'],
        'prefers_reduced_motion_fallback':todo('describe the reduced-motion fallback') if s['reduced_motion_css_declared'] else None},
      'WEB_QA':{'checks':checks,'known_limitations':limits,'verdict':verdict}}
