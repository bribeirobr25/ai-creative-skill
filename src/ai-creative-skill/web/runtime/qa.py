"""Scoped technical QA for static sites. Browser verification is optional; no claim of WCAG or conversions."""
import datetime,hashlib,json,pathlib,subprocess,urllib.parse,shutil
from bs4 import BeautifulSoup
from .validate import build_hash

def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def check(id,requirement,criticality,result,mode,evidence,hash,viewport=None,reason=None):
    c={'check_id':id,'requirement':requirement,'criticality':criticality,'procedure':id.replace('_',' '),'result':result,'evidence_mode':mode,'evidence_ref':evidence,'build_hash':hash,'viewport':viewport,'checked_at':now()}
    if reason:c['reason']=reason
    return c

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
                detail=next((l for l in (e.stderr or '').splitlines() if 'Error' in l),'syntax check failed')
                js_errors.append(js+': '+detail.replace(str(root),'.')[:160])
            except (OSError,subprocess.TimeoutExpired) as e:js_errors.append(js+': '+type(e).__name__)
    css='\n'.join((root/p).read_text(errors='replace') for p in css_files if (root/p).exists())
    files=project_files(root,project_root,['index.html']+css_files+js_files)
    return {'source_hash':build_hash(project_root,files),'files':files,'hash_routes':hash_routes,'assets_found':len(local)-len(missing),'missing_assets':missing,'broken_anchors':bad,'js_errors':js_errors,'reduced_motion_css_declared':'prefers-reduced-motion' in css,'form_count':len(soup.find_all('form')),'external_links':[x['href'] for x in soup.find_all('a',href=True) if x['href'].startswith(('http://','https://'))],'primary_link_candidates':[x.get('href') for x in soup.select('a.button,a.primary,a.nav-cta')]}

VIEWPORTS=[(1440,900,'desktop_render'),(390,844,'mobile_render'),(320,640,'narrow_render')]
SETTLE_JS='''async () => {
  const step = Math.max(200, Math.floor(window.innerHeight * 0.8));
  for (let y = 0; y < document.documentElement.scrollHeight; y += step) {
    window.scrollTo(0, y); await new Promise(r => setTimeout(r, 60));
  }
  window.scrollTo(0, 0);
  await Promise.all([...document.images].filter(i => !i.complete).map(i => new Promise(r => {
    i.addEventListener('load', r, {once: true}); i.addEventListener('error', r, {once: true}); setTimeout(r, 3000);
  })));
}'''
BROKEN_IMAGES_JS='''() => [...document.images].filter(i => (i.currentSrc || i.getAttribute('src')) && i.complete && i.naturalWidth === 0)
  .map(i => i.getAttribute('src') || i.currentSrc)'''

def audit(root,out_dir,base_url=None,project_root=None):
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
    browser_reason=None
    if base_url:
        try:
            from playwright.sync_api import sync_playwright
            with sync_playwright() as p:
                browser=p.chromium.launch(headless=True,executable_path=shutil.which('chromium') or shutil.which('chromium-browser') or None,args=['--no-sandbox'])
                for width,height,check_id in VIEWPORTS:
                    page=browser.new_page(viewport={'width':width,'height':height},reduced_motion='reduce')
                    response=page.goto(base_url,wait_until='domcontentloaded',timeout=12000)
                    if response and response.status==200:
                        # Scroll once so loading="lazy" images load before the full-page capture.
                        try:page.evaluate(SETTLE_JS)
                        except Exception:pass
                        page.wait_for_timeout(200)
                        e=f'viewport_{width}.png';page.screenshot(path=str(out/e),full_page=True,timeout=12000)
                        overflow=page.evaluate('document.documentElement.scrollWidth - window.innerWidth')
                        failed=overflow>1
                        checks.append(check(check_id,f'Page rendered at {width} without horizontal overflow','ESSENTIAL','FAIL' if failed else 'PASS','BROWSER_OBSERVED',rel(e),h,str(width),reason=f'Horizontal overflow of {overflow}px observed' if failed else None))
                        if width==1440:
                            checks.append(check('browser_render','Actual HTML opened','ESSENTIAL','PASS','BROWSER_OBSERVED',rel(e),h,'1440'))
                            broken=page.evaluate(BROKEN_IMAGES_JS)
                            checks.append(check('images_rendered','Referenced images decoded after scrolling','ESSENTIAL','FAIL' if broken else 'PASS','BROWSER_OBSERVED',rel(e),h,'1440',reason=('Images failed to load: '+', '.join(broken[:8])) if broken else None))
                    else:browser_reason=f'HTTP status unavailable or {getattr(response,"status",None)}'
                    page.close()
                browser.close()
        except Exception as e:
            browser_reason=type(e).__name__+': '+str(e)[:250]
    else:browser_reason='No accessible preview URL supplied'
    present={c['check_id'] for c in checks}
    rendered=('browser_render','desktop_render','mobile_render','narrow_render','images_rendered')
    for k in rendered+('cta_interaction','keyboard_interaction','responsive','reduced_motion','form_behavior'):
        if k not in present:
            checks.append(check(k,k.replace('_',' '),'ESSENTIAL' if k in rendered+('cta_interaction','keyboard_interaction') else 'ADVISORY','NOT_TESTED','NONE',None,h,reason=browser_reason if k in rendered else 'Requires explicit interaction test and appropriate evidence'))
    report={'status':'PARTIAL','build_hash':h,'checks':checks,'browser_blocker':browser_reason,'limits':['No real conversion or user study','No WCAG certification','No rights clearance','No human brand approval']}
    (out/'qa_matrix.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    return report
