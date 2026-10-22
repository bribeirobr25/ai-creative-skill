"""Scoped technical QA for static sites. Browser verification is optional; no claim of WCAG or conversions."""
import datetime,hashlib,json,pathlib,re,subprocess,urllib.parse,shutil
from bs4 import BeautifulSoup
from .validate import build_hash

def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def check(id,requirement,criticality,result,mode,evidence,hash,viewport=None,reason=None):
    c={'check_id':id,'requirement':requirement,'criticality':criticality,'procedure':id.replace('_',' '),'result':result,'evidence_mode':mode,'evidence_ref':evidence,'build_hash':hash,'viewport':viewport,'checked_at':now()}
    if reason:c['reason']=reason
    return c

ABSOLUTE_PATH=re.compile(r'(?<![\w:/.])(?:[A-Za-z]:\\|/)(?:[^\s:\'"()<>]+[/\\])+[^\s:\'"()<>]*')

def redact(text,*roots):
    """Evidence must not carry local directory names: known roots become '.', other absolute paths '<path>'."""
    text=str(text)
    for r in sorted({str(x) for x in roots if x},key=len,reverse=True):text=text.replace(r,'.')
    return ABSOLUTE_PATH.sub('<path>',text)

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
    files=project_files(root,project_root,['index.html']+css_files+js_files)
    return {'source_hash':build_hash(project_root,files),'files':files,'hash_routes':hash_routes,'assets_found':len(local)-len(missing),'missing_assets':missing,'broken_anchors':bad,'js_errors':js_errors,'reduced_motion_css_declared':'prefers-reduced-motion' in css,'form_count':len(soup.find_all('form')),'external_links':[x['href'] for x in soup.find_all('a',href=True) if x['href'].startswith(('http://','https://'))],'primary_link_candidates':[x.get('href') for x in soup.select('a.button,a.primary,a.nav-cta')]}

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
COLLAPSED_IMAGES_JS='''() => [...document.images].filter(i => i.complete && i.naturalWidth >= 64 && i.naturalHeight >= 64
  && i.getClientRects().length > 0 && getComputedStyle(i).visibility !== 'hidden')
  .filter(i => { const r = i.getBoundingClientRect(); return r.width < 16 || r.height < 16; })
  .map(i => i.getAttribute('src') || i.currentSrc)'''
BROKEN_IMAGES_JS='''() => [...document.images].filter(i => (i.currentSrc || i.getAttribute('src')) && i.complete && i.naturalWidth === 0)
  .map(i => i.getAttribute('src') || i.currentSrc)'''

def audit(root,out_dir,base_url=None,project_root=None,open_file=True):
    """QA evidence may live outside the site (so it never ships with it) but must stay inside the project root,
    which is the root later passed to validate.check. Evidence refs are always relative, never absolute."""
    root=pathlib.Path(root).resolve();project_root=pathlib.Path(project_root).resolve() if project_root else root
    out=pathlib.Path(out_dir).resolve()
    if not root.is_relative_to(project_root):raise ValueError('Site root must be inside the project root')
    if not out.is_relative_to(project_root):raise ValueError('QA evidence directory must be under the project root')
    out.mkdir(parents=True,exist_ok=True)
    rel=lambda name: (out/name).relative_to(project_root).as_posix()
    s=static_audit(root,project_root);h=s['source_hash'];(out/'static_audit.json').write_text(json.dumps(s,indent=2,ensure_ascii=False))
    checks=[check('assets_available','Local assets exist','ESSENTIAL','PASS' if not s['missing_assets'] else 'FAIL','STATIC_INSPECTED',rel('static_audit.json'),h),
      check('anchors_static','Local anchors resolve','ADVISORY','PASS' if not s['broken_anchors'] else 'FAIL','STATIC_INSPECTED',rel('static_audit.json'),h,reason=(f"{len(s['hash_routes'])} hash route link(s) not statically checkable" if s['hash_routes'] else None)),
      check('js_syntax','JavaScript syntax','ADVISORY','PASS' if not s['js_errors'] else 'FAIL','STATIC_INSPECTED',rel('static_audit.json'),h),
      check('content_truth','Product facts and rights','CRITICAL','NOT_TESTED','NONE',None,h,reason='Requires authoritative human/project evidence; source inspection alone insufficient')]
    browser_reason=None;opened_via=None
    # Without a preview server the browser opens the built index.html itself (file://); the URI never enters evidence.
    target=base_url or ((root/'index.html').as_uri() if open_file else None)
    if not target:browser_reason='Browser not run: static-only audit requested'
    else:
        try:
            from playwright.sync_api import sync_playwright
            with sync_playwright() as p:
                browser=p.chromium.launch(headless=True,executable_path=shutil.which('chromium') or shutil.which('chromium-browser') or None,args=['--no-sandbox'])
                collapsed=[];image_notes=[];broken=[]
                for width,height,check_id in VIEWPORTS:
                    page=browser.new_page(viewport={'width':width,'height':height},reduced_motion='reduce')
                    try:
                        response=page.goto(target,wait_until='domcontentloaded',timeout=12000)
                        opened=(response is not None and response.status==200) if base_url else (response is None or response.ok)
                    except Exception as e:opened,response=False,None;browser_reason='Page did not open: '+type(e).__name__
                    if opened:
                        opened_via='url' if base_url else 'file'
                        # Scroll once so loading="lazy" images load before the capture.
                        try:pending,settle_error=page.evaluate(SETTLE_JS),None
                        except Exception as e:pending,settle_error=None,type(e).__name__
                        page.wait_for_timeout(200)
                        e=f'viewport_{width}.png';page.screenshot(path=str(out/e),full_page=True,timeout=12000)
                        overflow=page.evaluate('document.documentElement.scrollWidth - window.innerWidth')
                        failed=overflow>1
                        checks.append(check(check_id,f'Page rendered at {width} without horizontal overflow','ESSENTIAL','FAIL' if failed else 'PASS','BROWSER_OBSERVED',rel(e),h,str(width),reason=f'Horizontal overflow of {overflow}px observed' if failed else None))
                        if width in (1440,390):
                            collapsed+=[f'{redact(c,project_root,root)} at {width}' for c in page.evaluate(COLLAPSED_IMAGES_JS)]
                        if width==1440:
                            checks.append(check('browser_render','Actual HTML opened','ESSENTIAL','PASS','BROWSER_OBSERVED',rel(e),h,'1440'))
                            broken=page.evaluate(BROKEN_IMAGES_JS);shot=rel(e)
                            if broken:image_notes.append('Images failed to load: '+', '.join(redact(b,project_root,root) for b in broken[:8]))
                            if pending:image_notes.append(f'{pending} image(s) not loaded after scrolling (hidden or still pending); not verified')
                            if settle_error:image_notes.append('Scroll before capture failed: '+settle_error)
                    elif not browser_reason:browser_reason=f'HTTP status unavailable or {getattr(response,"status",None)}'
                    page.close()
                browser.close()
                if 'browser_render' in {c['check_id'] for c in checks}:
                    if collapsed:image_notes.append('Images collapsed below 16 px: '+', '.join(collapsed[:8]))
                    checks.append(check('images_rendered','Referenced images decoded after scrolling and not collapsed','ESSENTIAL','FAIL' if broken or collapsed else 'PASS','BROWSER_OBSERVED',shot,h,'1440,390',reason='; '.join(image_notes) or None))
        except Exception as e:
            browser_reason=type(e).__name__+': '+redact(e,project_root,root,pathlib.Path.home())[:250]
    present={c['check_id'] for c in checks}
    rendered=('browser_render','desktop_render','mobile_render','narrow_render','images_rendered')
    for k in rendered+('cta_interaction','keyboard_interaction','responsive','reduced_motion','form_behavior'):
        if k not in present:
            checks.append(check(k,k.replace('_',' '),'ESSENTIAL' if k in rendered+('cta_interaction','keyboard_interaction') else 'ADVISORY','NOT_TESTED','NONE',None,h,reason=browser_reason if k in rendered else 'Requires explicit interaction test and appropriate evidence'))
    report={'status':'PARTIAL','build_hash':h,'checks':checks,'opened_via':opened_via,'browser_blocker':browser_reason,'limits':['No real conversion or user study','No WCAG certification','No rights clearance','No human brand approval']}
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
    images=sorted({x.get('src') for x in soup.find_all('img') if x.get('src') and not x.get('src').startswith(('http:','https:','data:'))})
    checks=q['checks'];browser=any(c['check_id']=='browser_render' and c['result']=='PASS' for c in checks)
    verdict='BLOCKED' if any(c['criticality']=='CRITICAL' and c['result']=='FAIL' for c in checks) else 'PARTIAL'
    enum=lambda *v:todo('one of '+' | '.join(v))
    limits=list(q.get('limits',[]))+([ 'Browser not run: '+q['browser_blocker']] if q.get('browser_blocker') else [])
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
        'asset_authority_and_rights':todo('who approved the assets; add images set from CSS or JS, which are not listed here'),
        'generation_required_decision':todo('was generation needed and authorised'),'product_identity_preservation':todo('how product identity was kept'),
        'provisional_vs_approved_labels':todo('which assets are provisional')},
      'WEB_PREVIEW_BUILD':{'preview_status':'AVAILABLE_VERIFIED' if browser else 'AVAILABLE_UNVERIFIED','source_files':s['files'],
        'verified_preview_ref_or_local_open_instructions':f'Open {(prefix/"index.html").as_posix()} in a browser (file://); hash routes work offline.',
        'responsive_strategy':todo('breakpoints and mobile behaviour'),'working_interactions':[todo('each interaction that works')],
        'primary_cta_behavior':enum('REAL_VERIFIED_LINK','SAFE_LOCAL_DEMO','CONTACT_LINK_VERIFIED','WAITLIST_NOT_CONNECTED','MOCK_FORM_LABELED','DISABLED_PENDING_DESTINATION'),
        'real_vs_mock_integrations':todo('what is real and what is local or mocked'),'version_id':h[:12],
        'form_mode':enum('NONE','LOCAL_CALCULATION','EXTERNAL_SUBMISSION','MOCK_INPUT'),'external_link_targets':s['external_links'],
        'prefers_reduced_motion_fallback':todo('describe the reduced-motion fallback') if s['reduced_motion_css_declared'] else None},
      'WEB_QA':{'checks':checks,'known_limitations':limits,'verdict':verdict}}
