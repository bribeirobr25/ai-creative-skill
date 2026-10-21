"""2.6.0-dev regressions for defects observed in DQB-02 (router, QA evidence, hash routes, 320 px, lazy images)."""
import functools,http.server,importlib.util,json,shutil,struct,sys,tempfile,threading,unittest,zlib
from pathlib import Path

WEB=Path(__file__).resolve().parents[1]/'src/ai-creative-skill/web'
sys.path.insert(0,str(WEB))
from runtime.router import resolve  # noqa: E402
from runtime import qa  # noqa: E402
from runtime.validate import build_hash  # noqa: E402

def route(text):
    try:return resolve(text).route
    except ValueError:return 'AMBIGUOUS'

def png(path,w=4,h=3):
    raw=b''.join(b'\x00'+b'\x80\x40\x20'*w for _ in range(h))
    def chunk(t,d):return struct.pack('>I',len(d))+t+d+struct.pack('>I',zlib.crc32(t+d)&0xffffffff)
    path.write_bytes(b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',w,h,8,2,0,0,0))+chunk(b'IDAT',zlib.compress(raw))+chunk(b'IEND',b''))

SITE='''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="styles.css"></head><body>
<nav><a href="#/menu">Menu</a> <a href="#sobre">Sobre</a> <a href="#!/agenda">Agenda</a></nav>
<section id="sobre" class="hero"><h1>Teste</h1><div class="wide">{wide}</div></section>
<div style="height:2400px"></div>
<img src="assets/foto.png" alt="foto" loading="lazy" width="40" height="30">
{broken}<script src="app.js"></script></body></html>'''

def make_site(base,wide=False,broken=False):
    site=base/'site';(site/'assets').mkdir(parents=True)
    (site/'index.html').write_text(SITE.format(wide='x' if wide else '',broken='<img src="assets/missing.png" alt="falta">' if broken else ''))
    (site/'styles.css').write_text('body{margin:0;font-family:sans-serif}@media (prefers-reduced-motion:reduce){*{animation:none}}'
        +('.wide{width:340px;height:4px;background:#000}' if wide else ''))
    (site/'app.js').write_text('document.documentElement.dataset.ready="1";')
    png(site/'assets/foto.png')
    return site

class RouterNaturalRequests(unittest.TestCase):
    def test_natural_build_requests_route_to_preview(self):
        for text in ('Crie o website descrito no briefing, com as páginas pedidas','faça um site para minha padaria',
                     'build me a landing page for my sauna','Create the website described in the brief',
                     'Quero um site novo para a loja','desenvolva a homepage da Tábua','gere uma página de vendas'):
            self.assertEqual(route(text),'WEB_PREVIEW',text)

    def test_other_operations_keep_their_route(self):
        cases={'crie um wireframe do site':'WEB_CONCEPT_ONLY','crie o conceito visual do site':'WEB_CONCEPT_ONLY',
               'quero analisar sites':'WEB_RESEARCH_ONLY','research how to build a website':'WEB_RESEARCH_ONLY',
               'mude apenas o hero do site':'WEB_EDIT','quero publicar o site':'WEB_PUBLICATION',
               'não crie um site, só pesquise sites':'WEB_RESEARCH_ONLY','crie um site sem publicar':'WEB_PREVIEW'}
        for text,expected in cases.items():self.assertEqual(route(text),expected,text)

    def test_unsafe_or_multi_operation_requests_stay_ambiguous(self):
        for text in ('make the page faster','crie um site e publique','não crie o site',
                     'research the website and build a website','seria legal ter algo bonito'):
            self.assertEqual(route(text),'AMBIGUOUS',text)

class StaticAudit(unittest.TestCase):
    def test_hash_routes_are_not_broken_anchors(self):
        with tempfile.TemporaryDirectory() as td:
            site=make_site(Path(td));r=qa.static_audit(site)
            self.assertEqual(r['broken_anchors'],[])
            self.assertEqual(r['hash_routes'],['/menu','!/agenda'])
            (site/'index.html').write_text((site/'index.html').read_text().replace('#sobre','#nao-existe'))
            self.assertEqual(qa.static_audit(site)['broken_anchors'],['nao-existe'])

    def test_js_errors_do_not_record_absolute_paths(self):
        if not shutil.which('node'):self.skipTest('node not installed')
        with tempfile.TemporaryDirectory() as td:
            site=make_site(Path(td));(site/'app.js').write_text('let = ;')
            r=qa.static_audit(site)
            self.assertEqual(len(r['js_errors']),1)
            self.assertTrue(r['js_errors'][0].startswith('app.js: '))
            self.assertNotIn(str(Path(td).resolve()),json.dumps(r))

    def test_files_and_hash_are_relative_to_project_root(self):
        with tempfile.TemporaryDirectory() as td:
            project=Path(td);site=make_site(project)
            alone=qa.static_audit(site);nested=qa.static_audit(site,project)
            self.assertEqual(alone['files'],['index.html','styles.css','app.js'])
            self.assertEqual(nested['files'],['site/index.html','site/styles.css','site/app.js'])
            self.assertEqual(nested['source_hash'],build_hash(project,nested['files']))
            with self.assertRaises(ValueError):qa.static_audit(project,site)

    def test_evidence_outside_site_but_inside_project(self):
        with tempfile.TemporaryDirectory() as td:
            project=Path(td);site=make_site(project)
            report=qa.audit(site,project/'qa-evidence',project_root=project)
            refs={c['evidence_ref'] for c in report['checks'] if c['evidence_ref']}
            self.assertEqual(refs,{'qa-evidence/static_audit.json'})
            self.assertFalse((site/'qa-evidence').exists())
            self.assertTrue(all(not ref.startswith('/') for ref in refs))
            with self.assertRaisesRegex(ValueError,'project root'):qa.audit(site,Path(td).parent/'elsewhere',project_root=project)
            with self.assertRaisesRegex(ValueError,'project root'):qa.audit(site,project/'qa-evidence')
            names={c['check_id'] for c in report['checks']}
            self.assertTrue({'narrow_render','images_rendered'}<=names)

def browser_available():
    if importlib.util.find_spec('playwright') is None:return False
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            p.chromium.launch(headless=True,executable_path=shutil.which('chromium') or shutil.which('chromium-browser') or None,args=['--no-sandbox']).close()
        return True
    except Exception:return False

@unittest.skipUnless(browser_available(),'Playwright and Chromium not installed')
class BrowserAudit(unittest.TestCase):
    def serve(self,root):
        class Quiet(http.server.SimpleHTTPRequestHandler):
            def log_message(self,*a):pass
        server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(root)))
        threading.Thread(target=server.serve_forever,daemon=True).start()
        self.addCleanup(server.server_close);self.addCleanup(server.shutdown)
        return f'http://127.0.0.1:{server.server_address[1]}/'

    def run_audit(self,**site):
        td=tempfile.TemporaryDirectory();self.addCleanup(td.cleanup)
        project=Path(td.name);root=make_site(project,**site)
        report=qa.audit(root,project/'qa',self.serve(root),project_root=project)
        return {c['check_id']:c for c in report['checks']},project

    def test_clean_site_passes_three_widths_and_lazy_image(self):
        checks,project=self.run_audit()
        for k in ('browser_render','desktop_render','mobile_render','narrow_render','images_rendered'):
            self.assertEqual(checks[k]['result'],'PASS',(k,checks[k].get('reason')))
        self.assertEqual(checks['narrow_render']['viewport'],'320')
        self.assertTrue((project/'qa/viewport_320.png').is_file())

    def test_overflow_only_at_320_is_caught(self):
        checks,_=self.run_audit(wide=True)
        self.assertEqual(checks['mobile_render']['result'],'PASS')
        self.assertEqual(checks['narrow_render']['result'],'FAIL')
        self.assertIn('overflow',checks['narrow_render']['reason'])

    def test_broken_image_is_reported(self):
        checks,_=self.run_audit(broken=True)
        self.assertEqual(checks['images_rendered']['result'],'FAIL')
        self.assertIn('assets/missing.png',checks['images_rendered']['reason'])

class CandidateGovernance(unittest.TestCase):
    def setUp(self):
        sys.path.insert(0,str(WEB.parents[2]))
        from validation import candidate_integrity
        self.ci=candidate_integrity

    def test_active_candidate_is_cumulative_over_parent(self):
        self.assertEqual(self.ci.CANDIDATE_ID,'web-runtime-2.6-v1')
        parent,scope=self.ci.CANDIDATE_SCOPES[self.ci.CANDIDATE_ID]
        self.assertEqual(parent,'boundary-hardening-v1')
        self.assertTrue(self.ci.BOUNDARY_SCOPE<scope)
        self.assertTrue(self.ci.lineage_valid())

    def test_manifest_cannot_widen_reviewed_scope(self):
        manifest=json.loads((self.ci.CANDIDATE/'source-manifest.json').read_text())
        manifest['changed_from_release']=sorted(manifest['changed_from_release']+['SKILL.md'])
        with self.assertRaisesRegex(ValueError,'scope'):self.ci.check(manifest=manifest)
        manifest=json.loads((self.ci.CANDIDATE/'source-manifest.json').read_text())
        manifest['parent_candidate']=None
        with self.assertRaisesRegex(ValueError,'lineage'):self.ci.check(manifest=manifest)

    def test_superseded_candidate_records_are_byte_preserved(self):
        self.assertTrue(self.ci.preserved_history())
        path='validation/candidates/boundary-hardening-v1/source-manifest.json'
        self.assertEqual((self.ci.ROOT/path).read_bytes(),self.ci.git_bytes(self.ci.SUPERSEDED['boundary-hardening-v1'],path))

if __name__=='__main__':unittest.main()
