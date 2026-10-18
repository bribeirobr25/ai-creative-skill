"""Scoped technical QA for static sites. Browser verification is optional; no claim of WCAG or conversions."""
import datetime,hashlib,json,pathlib,subprocess,urllib.parse,shutil
from bs4 import BeautifulSoup
from .validate import build_hash

def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def check(id,requirement,criticality,result,mode,evidence,hash,viewport=None,reason=None):
    c={'check_id':id,'requirement':requirement,'criticality':criticality,'procedure':id.replace('_',' '),'result':result,'evidence_mode':mode,'evidence_ref':evidence,'build_hash':hash,'viewport':viewport,'checked_at':now()}
    if reason:c['reason']=reason
    return c

def static_audit(root):
    root=pathlib.Path(root).resolve();html=root/'index.html'
    if not html.exists():raise ValueError('No index.html')
    code=html.read_text();soup=BeautifulSoup(code,'html.parser')
    js_files=[x.get('src') for x in soup.find_all('script') if x.get('src') and not x.get('src').startswith('http')]
    css_files=[x.get('href') for x in soup.find_all('link') if x.get('rel')==['stylesheet'] and x.get('href')]
    local=[x.get('src') for x in soup.find_all('img') if x.get('src')]+js_files+css_files
    missing=[p for p in local if not p.startswith(('http:','https:','data:')) and not (root/p).is_file()]
    anchors=[x['href'][1:] for x in soup.find_all('a',href=True) if x['href'].startswith('#') and len(x['href'])>1]
    ids={n.get('id') for n in soup.find_all(id=True)}
    bad=[a for a in anchors if a not in ids]
    js_errors=[]
    for js in js_files:
        if (root/js).exists():
            try:subprocess.run(['node','--check',str(root/js)],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=12)
            except (OSError,subprocess.CalledProcessError,subprocess.TimeoutExpired) as e:js_errors.append(js+': '+str(e)[:120])
    css='\n'.join((root/p).read_text(errors='replace') for p in css_files if (root/p).exists())
    return {'source_hash':build_hash(root,['index.html']+css_files+js_files),'files':['index.html']+css_files+js_files,'assets_found':len(local)-len(missing),'missing_assets':missing,'broken_anchors':bad,'js_errors':js_errors,'reduced_motion_css_declared':'prefers-reduced-motion' in css,'form_count':len(soup.find_all('form')),'external_links':[x['href'] for x in soup.find_all('a',href=True) if x['href'].startswith(('http://','https://'))],'primary_link_candidates':[x.get('href') for x in soup.select('a.button,a.primary,a.nav-cta')]}

def audit(root,out_dir,base_url=None):
    root=pathlib.Path(root).resolve();out=pathlib.Path(out_dir).resolve();out.mkdir(parents=True,exist_ok=True)
    if not out.is_relative_to(root):raise ValueError('QA evidence directory must be under site root')
    rel=lambda name: str((out/name).relative_to(root))
    s=static_audit(root);h=s['source_hash'];(out/'static_audit.json').write_text(json.dumps(s,indent=2,ensure_ascii=False))
    checks=[check('assets_available','Local assets exist','ESSENTIAL','PASS' if not s['missing_assets'] else 'FAIL','STATIC_INSPECTED',rel('static_audit.json'),h),
      check('anchors_static','Local anchors resolve','ADVISORY','PASS' if not s['broken_anchors'] else 'FAIL','STATIC_INSPECTED',rel('static_audit.json'),h),
      check('js_syntax','JavaScript syntax','ADVISORY','PASS' if not s['js_errors'] else 'FAIL','STATIC_INSPECTED',rel('static_audit.json'),h),
      check('content_truth','Product facts and rights','CRITICAL','NOT_TESTED','NONE',None,h,reason='Requires authoritative human/project evidence; source inspection alone insufficient')]
    browser_reason=None
    if base_url:
        try:
            from playwright.sync_api import sync_playwright
            with sync_playwright() as p:
                browser=p.chromium.launch(headless=True,executable_path=shutil.which('chromium') or shutil.which('chromium-browser') or None,args=['--no-sandbox'])
                for width,height in [(1440,900),(390,844)]:
                    page=browser.new_page(viewport={'width':width,'height':height},reduced_motion='reduce')
                    response=page.goto(base_url,wait_until='domcontentloaded',timeout=12000)
                    page.wait_for_timeout(200)
                    if response and response.status==200:
                        e=f'viewport_{width}.png';page.screenshot(path=str(out/e),full_page=True,timeout=12000)
                        overflow=page.evaluate('document.documentElement.scrollWidth > window.innerWidth + 1')
                        check_id='desktop_render' if width==1440 else 'mobile_render'
                        checks.append(check(check_id,f'Page rendered at {width}','ESSENTIAL','FAIL' if overflow else 'PASS','BROWSER_OBSERVED',rel(e),h,str(width),reason='Horizontal overflow observed' if overflow else None))
                        if width==1440:checks.append(check('browser_render','Actual HTML opened','ESSENTIAL','PASS','BROWSER_OBSERVED',rel(e),h,'1440'))
                    else:browser_reason=f'HTTP status unavailable or {getattr(response,"status",None)}'
                    page.close()
                browser.close()
        except Exception as e:
            browser_reason=type(e).__name__+': '+str(e)[:250]
    else:browser_reason='No accessible preview URL supplied'
    present={c['check_id'] for c in checks}
    for k in ('browser_render','desktop_render','mobile_render','cta_interaction','keyboard_interaction','responsive','reduced_motion','form_behavior'):
        if k not in present:
            checks.append(check(k,k.replace('_',' '),'ESSENTIAL' if k in ('browser_render','desktop_render','mobile_render','cta_interaction','keyboard_interaction') else 'ADVISORY','NOT_TESTED','NONE',None,h,reason=browser_reason if k in ('browser_render','desktop_render','mobile_render') else 'Requires explicit interaction test and appropriate evidence'))
    report={'status':'PARTIAL','build_hash':h,'checks':checks,'browser_blocker':browser_reason,'limits':['No real conversion or user study','No WCAG certification','No rights clearance','No human brand approval']}
    (out/'qa_matrix.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    return report
