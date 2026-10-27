"""2.6.0-dev regressions for defects observed in DQB-02/DQB-03 and the style test (router, QA evidence, hash routes, 320 px,
lazy and collapsed images, file:// audit, delivery record draft) and candidate governance."""
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

BUILD=('Crie o website descrito no briefing, com as páginas pedidas','faça um site para minha padaria','build me a landing page for my sauna',
 'Quero um site novo para a loja','desenvolva a homepage da Tábua','gere uma página de vendas','Create the website described in the brief','make me a website',
 'Faz um site pra mim','Me faz uma landing page','Crie uma loja virtual','Elabore um site institucional','I want a website for my bakery',
 'Put together a landing page','Crie, por favor, um site','crie um site sem publicar','crie uma landing; não publique','preciso de um site',
 'we need a new website','Crie o e-commerce da marca')
# Requests found in review that must not start a build (edits, bugs, other media, social pages, questions, negations).
NOT_BUILD=('make the page faster','make my page faster','make our website responsive','faça o site mais rápido',
 'faça a página carregar mais rápido','quero que o site carregue mais rápido','melhore o design do site','Revise o design da landing page',
 'crie um botão no site','crie uma nova seção na página inicial','create a button on the page','o build do site quebrou',
 'the build of the site is broken','preciso de ajuda com o site','gere imagens para o site','create an image for my website',
 'generate copy for the landing page','crie o texto da landing page','crie o logo do site','crie um vídeo para a landing page',
 'crie um moodboard para o site','crie um mockup do site','crie uma página no Instagram','create a LinkedIn page for my company',
 'crie um post para a página do Instagram','quero ver exemplos de sites','quero saber como funciona um site','gere um relatório sobre o site',
 'faça uma avaliação do site','create a report about the website','como criar um site?','Quanto custa criar um site?',
 'how to make a landing page','Você consegue criar um site?','faça tudo menos o site','faca o app nao o site',
 'create everything except the website','crie qualquer coisa exceto uma landing page','crie um site e publique','não crie o site',
 'research the website and build a website','seria legal ter algo bonito')

class RouterNaturalRequests(unittest.TestCase):
    def test_natural_build_requests_route_to_preview(self):
        for text in BUILD:self.assertEqual(route(text),'WEB_PREVIEW',text)

    def test_non_build_requests_never_route_to_preview(self):
        for text in NOT_BUILD:self.assertNotEqual(route(text),'WEB_PREVIEW',text)
        for text in NOT_BUILD[:4]+('crie um botão no site','como criar um site?','faça tudo menos o site'):
            self.assertEqual(route(text),'AMBIGUOUS',text)

    def test_other_operations_keep_their_route(self):
        cases={'crie um wireframe do site':'WEB_CONCEPT_ONLY','crie o conceito visual do site':'WEB_CONCEPT_ONLY',
               'quero analisar sites':'WEB_RESEARCH_ONLY','research how to build a website':'WEB_RESEARCH_ONLY',
               'não crie um site, só pesquise sites':'WEB_RESEARCH_ONLY','mude apenas o hero do site':'WEB_EDIT',
               'quero publicar o site':'WEB_PUBLICATION'}
        for text,expected in cases.items():self.assertEqual(route(text),expected,text)

    def test_long_inputs_stay_fast(self):
        import time
        for phrase in ('faça o site ','quero um site ','crie um site '):
            start=time.monotonic();route(phrase*2000)
            self.assertLess(time.monotonic()-start,2.0,phrase)

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

    def test_js_error_detail_and_paths_outside_site(self):
        if not shutil.which('node'):self.skipTest('node not installed')
        with tempfile.TemporaryDirectory() as td:
            project=Path(td);site=make_site(project);(project/'shared').mkdir()
            (project/'shared/ErrorReporter.js').write_text("if (x) { throw new Error('boom' }")
            (site/'index.html').write_text((site/'index.html').read_text().replace('<script src="app.js">','<script src="../shared/ErrorReporter.js">'))
            r=qa.static_audit(site,project)
            self.assertEqual(len(r['js_errors']),1)
            self.assertIn('SyntaxError',r['js_errors'][0])
            self.assertNotIn(str(project.resolve()),json.dumps(r))

    def test_redact_handles_file_uris(self):
        root='/srv/Área de/proj'
        self.assertEqual(qa.redact('file:///srv/%C3%81rea%20de/proj/site/a.png',root),'./site/a.png')
        self.assertEqual(qa.redact('file:///C:/Users/x%20y/a.png'),'<path>')
        self.assertEqual(qa.redact('at file:///home/u/p/x.js:3 failed'),'at <path> failed')
        self.assertEqual(qa.redact('C:/Users/someone/a.js'),'<path>')

    def test_static_only_is_honoured_with_url(self):
        with tempfile.TemporaryDirectory() as td:
            project=Path(td);site=make_site(project)
            report=qa.audit(site,project/'qa','http://127.0.0.1:9/',project_root=project,browser=False,skip_reason='Legacy migration: browser checks not re-run')
            self.assertIsNone(report['opened_via'])
            self.assertFalse(any(c['evidence_mode']=='BROWSER_OBSERVED' for c in report['checks']))
            self.assertEqual({c['check_id']:c for c in report['checks']}['browser_render']['reason'],'Legacy migration: browser checks not re-run')
            rec=qa.draft_record(site,project/'qa/qa_matrix.json',project)
            self.assertEqual(rec['WEB_QA']['known_limitations'][-1],'Browser checks not completed: Legacy migration: browser checks not re-run')

    def test_todo_marker_only(self):
        from runtime.validate import todo_paths
        for text in ('Todos os tamanhos são feitos à mão','Todo visitante vê o preço','site/todo-app/index.html','to do: later','TODOS: x'):
            self.assertEqual(todo_paths({'a':text}),[],text)
        for text in ('TODO: fill','  todo : fill','\u200bTODO: x','\ufeffTODO:x'):
            self.assertEqual(todo_paths({'a':[text]}),['a/0'],text)

    def test_record_lists_srcset_and_root_relative_images(self):
        with tempfile.TemporaryDirectory() as td:
            project=Path(td);site=make_site(project)
            (site/'index.html').write_text((site/'index.html').read_text().replace('<script','<img srcset="assets/a.png 1x, assets/b.png 2x" alt="a"><picture><source srcset="/assets/c.webp"><img src="/assets/d.png" alt="d"></picture><script'))
            qa.audit(site,project/'qa',project_root=project,browser=False)
            paths={a['path'] for a in qa.draft_record(site,project/'qa/qa_matrix.json',project)['WEB_ASSET_PLAN']['assets_used']}
            self.assertTrue({'site/assets/a.png','site/assets/b.png','site/assets/c.webp','site/assets/d.png','site/assets/foto.png'}<=paths,paths)

    def test_redact_keeps_urls_and_relative_paths(self):
        self.assertEqual(qa.redact("Executable doesn't exist at /home/someone/.cache/ms-playwright/x/shell"),"Executable doesn't exist at <path>")
        self.assertEqual(qa.redact('C:\\Users\\someone\\a.js:3'),'<path>:3')
        for text in ('https://example.com/a/b.png','assets/foto.png','../shared/x.js',"SyntaxError: Unexpected token ';'"):
            self.assertEqual(qa.redact(text),text)
        self.assertEqual(qa.redact('/srv/proj/site/app.js','/srv/proj/site'),'./app.js')

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
            # With a browser available the page is opened via file:// and captures join the evidence.
            self.assertIn('qa-evidence/static_audit.json',refs)
            self.assertTrue(all(ref.startswith('qa-evidence/') for ref in refs),refs)
            self.assertFalse((site/'qa-evidence').exists())
            self.assertTrue(all(not ref.startswith('/') for ref in refs))
            with self.assertRaisesRegex(ValueError,'project root'):qa.audit(site,Path(td).parent/'elsewhere',project_root=project)
            with self.assertRaisesRegex(ValueError,'project root'):qa.audit(site,project/'qa-evidence')
            from runtime.validate import contained_path
            self.assertTrue(all(contained_path(project,ref).is_file() for ref in refs))
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

    def test_infinite_scroll_page_terminates(self):
        td=tempfile.TemporaryDirectory();self.addCleanup(td.cleanup)
        project=Path(td.name);root=make_site(project)
        (root/'app.js').write_text("addEventListener('scroll',()=>{const d=document.createElement('div');d.style.height='3000px';document.body.append(d)});")
        import time;start=time.monotonic()
        report=qa.audit(root,project/'qa',self.serve(root),project_root=project)
        self.assertLess(time.monotonic()-start,90)
        self.assertEqual({c['check_id']:c for c in report['checks']}['browser_render']['result'],'PASS')

    def test_collapsed_image_fails_but_hidden_image_does_not(self):
        td=tempfile.TemporaryDirectory();self.addCleanup(td.cleanup)
        project=Path(td.name);root=make_site(project);png(root/'assets/big.png',80,80)
        html=(root/'index.html').read_text()
        (root/'index.html').write_text(html.replace('<script','<div style="display:none"><img src="assets/big.png" alt="menu"></div><script'))
        checks={c['check_id']:c for c in qa.audit(root,project/'qa',self.serve(root),project_root=project)['checks']}
        self.assertEqual(checks['images_rendered']['result'],'PASS',checks['images_rendered'].get('reason'))
        (root/'index.html').write_text(html.replace('<script','<div style="height:0;overflow:hidden"><img src="assets/big.png" alt="card" style="width:100%;height:100%;object-fit:cover"></div><script'))
        checks={c['check_id']:c for c in qa.audit(root,project/'qa',self.serve(root),project_root=project)['checks']}
        self.assertEqual(checks['images_rendered']['result'],'FAIL')
        self.assertIn('assets/big.png at 1440',checks['images_rendered']['reason'])

    def test_audit_without_url_opens_the_file(self):
        td=tempfile.TemporaryDirectory();self.addCleanup(td.cleanup)
        project=Path(td.name);root=make_site(project)
        report=qa.audit(root,project/'qa',project_root=project)
        checks={c['check_id']:c for c in report['checks']}
        self.assertEqual(report['opened_via'],'file')
        for k in ('browser_render','desktop_render','mobile_render','narrow_render','images_rendered'):
            self.assertEqual(checks[k]['result'],'PASS',(k,checks[k].get('reason')))
        for f in (project/'qa').glob('*.json'):
            text=f.read_text();self.assertNotIn(str(project.resolve()),text);self.assertNotIn('file:',text)

    def test_record_draft_must_be_filled_then_validates(self):
        from runtime import validate
        td=tempfile.TemporaryDirectory();self.addCleanup(td.cleanup)
        project=Path(td.name);root=make_site(project)
        qa.audit(root,project/'qa',project_root=project)
        rec=qa.draft_record(root,project/'qa/qa_matrix.json',project,'test')
        self.assertEqual(rec['WEB_PREVIEW_BUILD']['preview_status'],'AVAILABLE_VERIFIED')
        errors=validate.check(rec,project)
        self.assertTrue(errors and {e['code'] for e in errors}=={'UNFILLED_FIELD'},errors)
        self.assertIn('WEB_BRIEF/business_kind',{e['path'] for e in errors})
        enums={'business_kind':'PHYSICAL_PRODUCT','brand_authority_state':'PROVISIONAL','approval':'PROVISIONAL','rights':'UNKNOWN',
               'primary_cta_behavior':'SAFE_LOCAL_DEMO','form_mode':'NONE'}
        def fill(node,key=None):
            if isinstance(node,dict):return {k:fill(v,k) for k,v in node.items()}
            if isinstance(node,list):return [fill(v,key) for v in node]
            return enums.get(key,'filled') if isinstance(node,str) and node.startswith('TODO') else node
        self.assertEqual(validate.check(fill(rec),project),[])
        (root/'styles.css').write_text('body{color:red}')
        with self.assertRaisesRegex(ValueError,'another build'):qa.draft_record(root,project/'qa/qa_matrix.json',project)

    def audit_variant(self,snippet,via='url',base=None,js=None):
        td=tempfile.TemporaryDirectory();self.addCleanup(td.cleanup)
        project=Path(td.name) if base is None else Path(td.name)/base;project.mkdir(parents=True,exist_ok=True)
        root=make_site(project);png(root/'assets/big.png',128,128)
        (root/'assets/icon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512"><circle cx="256" cy="256" r="200"/></svg>')
        (root/'index.html').write_text((root/'index.html').read_text().replace('<script',snippet+'<script'))
        if js is not None:(root/'app.js').write_text(js)
        report=qa.audit(root,project/'qa',self.serve(root) if via=='url' else None,project_root=project)
        return report,{c['check_id']:c for c in report['checks']},project

    def test_small_icons_inactive_slides_and_sr_only_are_not_collapsed(self):
        for snippet in ('<footer><img src="assets/big.png" width="14" height="14" alt="icon"></footer>',
                        '<img src="assets/icon.svg" style="width:14px;height:14px" alt="icon">',
                        '<div style="display:flex"><img src="assets/big.png" style="width:300px" alt="a"><img src="assets/big.png" style="width:0;opacity:0" alt="b"></div>',
                        '<span style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0,0,0)"><img src="assets/big.png" style="width:100%;height:100%" alt="sr"></span>',
                        '<div style="display:flex;overflow:hidden;width:300px"><img src="assets/big.png" style="width:300px;flex-shrink:0" alt="1"><img src="assets/big.png" style="width:300px;flex-shrink:0" alt="2"></div>'):
            _,checks,_=self.audit_variant(snippet)
            self.assertEqual(checks['images_rendered']['result'],'PASS',(snippet,checks['images_rendered'].get('reason')))

    def test_sized_image_inside_collapsed_container_fails(self):
        _,checks,_=self.audit_variant('<div style="height:0;overflow:hidden"><img src="assets/big.png" style="width:300px;height:200px" alt="card"></div>')
        self.assertEqual(checks['images_rendered']['result'],'FAIL')

    def test_file_mode_evidence_has_no_local_path(self):
        # A space and a non-ASCII letter in the project path; srcset-only images report their authored URL.
        report,checks,project=self.audit_variant('<div style="height:0"><img srcset="assets/big.png 1x" style="width:100%;height:100%" alt="x"></div>'
                                                  '<img srcset="assets/nope.png 1x" alt="missing">',via='file',base='Área de Trabalho/meu projeto')
        self.assertEqual(report['opened_via'],'file')
        self.assertEqual(checks['images_rendered']['result'],'FAIL')
        self.assertIn('assets/big.png at 1440',checks['images_rendered']['reason'])
        self.assertIn('assets/nope.png',checks['images_rendered']['reason'])
        for f in (project/'qa').glob('*.json'):
            text=f.read_text()
            for marker in ('Trabalho','projeto','%C3','file:',str(project)):self.assertNotIn(marker,text,(f.name,marker))

    def test_file_mode_needs_http_for_modules_and_fetch(self):
        for snippet,js,why in (('<main id="app"></main><script type="module" src="mod.js"></script>',None,'ES module'),
                               ('<main id="app"></main>',"fetch('data.json').then(r=>r.json()).then(d=>{document.getElementById('app').textContent=d.t})",'fetch()')):
            report,checks,project=self.audit_variant(snippet,via='file',js=js)
            for k in ('browser_render','desktop_render','images_rendered'):
                self.assertEqual(checks[k]['result'],'NOT_TESTED',k);self.assertIn('--url',checks[k]['reason'])
            self.assertIn(why,report['browser_blocker'])
            rec=qa.draft_record(project/'site',project/'qa/qa_matrix.json',project)
            self.assertEqual(rec['WEB_PREVIEW_BUILD']['preview_status'],'AVAILABLE_UNVERIFIED')
            self.assertIn('preview start',rec['WEB_PREVIEW_BUILD']['verified_preview_ref_or_local_open_instructions'])

    def test_blank_page_fails_render(self):
        td=tempfile.TemporaryDirectory();self.addCleanup(td.cleanup)
        project=Path(td.name);root=project/'site';root.mkdir()
        (root/'index.html').write_text('<!doctype html><title>x</title><main id="app"></main>')
        checks={c['check_id']:c for c in qa.audit(root,project/'qa',self.serve(root),project_root=project)['checks']}
        self.assertEqual(checks['browser_render']['result'],'FAIL')

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
        self.assertEqual(self.ci.CANDIDATE_ID,'web-runtime-2.6-v2')
        parent,scope=self.ci.CANDIDATE_SCOPES[self.ci.CANDIDATE_ID]
        self.assertEqual(parent,'web-runtime-2.6-v1')
        self.assertTrue(self.ci.CANDIDATE_SCOPES[parent][1]<scope)
        self.assertTrue(self.ci.BOUNDARY_SCOPE<scope)
        self.assertTrue(self.ci.lineage_valid())

    def test_manifest_cannot_widen_reviewed_scope(self):
        manifest=json.loads((self.ci.CANDIDATE/'source-manifest.json').read_text())
        manifest['changed_from_release']=sorted(manifest['changed_from_release']+['SKILL.md'])
        with self.assertRaisesRegex(ValueError,'scope'):self.ci.check(manifest=manifest)
        manifest=json.loads((self.ci.CANDIDATE/'source-manifest.json').read_text())
        manifest['parent_candidate']=None
        with self.assertRaisesRegex(ValueError,'lineage'):self.ci.check(manifest=manifest)

    def test_pointer_cannot_roll_back_to_superseded_candidate(self):
        with self.assertRaisesRegex(ValueError,'newest'):self.ci.lineage_valid('boundary-hardening-v1')
        with self.assertRaisesRegex(ValueError,'newest'):self.ci.lineage_valid('web-runtime-2.6-v1')

    def test_superseded_candidate_records_are_byte_preserved(self):
        self.assertTrue(self.ci.preserved_history())
        for cid,name in (('boundary-hardening-v1','source-manifest.json'),('boundary-hardening-v1','remediation.json'),
                         ('web-runtime-2.6-v1','README.md'),('web-runtime-2.6-v1','source-manifest.json')):
            path=f'validation/candidates/{cid}/{name}'
            self.assertEqual((self.ci.ROOT/path).read_bytes(),self.ci.git_bytes(self.ci.SUPERSEDED[cid],path))

    def test_record_todo_is_reported_even_with_schema_errors(self):
        from runtime import validate
        errors=validate.check({'schema_version':'0.2.0','route':'TODO: pick','WEB_BRIEF':{'user_goal':'TODO: goal'}},'.')
        codes={(e['code'],e['path']) for e in errors}
        self.assertIn(('UNFILLED_FIELD','route'),codes)
        self.assertIn(('UNFILLED_FIELD','WEB_BRIEF/user_goal'),codes)
        self.assertNotIn(('SCHEMA','route'),codes)
        self.assertIn('SCHEMA',{c for c,_ in codes})

if __name__=='__main__':unittest.main()
