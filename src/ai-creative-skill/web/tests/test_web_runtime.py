import copy,json,pathlib,shutil,tempfile,unittest,sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from runtime.router import resolve
from runtime.validate import check, build_hash
from runtime.qa import static_audit
from runtime.revision import compare
from runtime.preview import start,stop,status
from runtime.migrate import scaffold

class WebTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
    cls.tmp=tempfile.TemporaryDirectory();cls.base=pathlib.Path(cls.tmp.name)
    cls.root=cls.base/'site';cls.root.mkdir();(cls.root/'index.html').write_text('''<!doctype html><title>Test</title><section class="hero" id="hero"><h1>Sample</h1></section><section id="faq">Facts</section><a href="#faq">FAQ</a><script src="app.js"></script><link rel="stylesheet" href="styles.css">''');(cls.root/'styles.css').write_text('@media (prefers-reduced-motion: reduce) { * { animation: none; }}');(cls.root/'app.js').write_text('console.log("ok");')
    cls.record=scaffold(cls.root,'Fixture','SERVICE',cls.base)
 @classmethod
 def tearDownClass(cls):cls.tmp.cleanup()
 def valid(self):return copy.deepcopy(self.record)
 def test_01_route_preview(self):self.assertEqual(resolve('crie uma landing para meu serviço').route,'WEB_PREVIEW')
 def test_02_route_research(self):self.assertEqual(resolve('pesquise referências de sites').route,'WEB_RESEARCH_ONLY')
 def test_03_route_edit(self):self.assertEqual(resolve('mude apenas o hero').route,'WEB_EDIT')
 def test_04_route_publication_gate(self):self.assertTrue(resolve('publique site').authority_gate)
 def test_05_ambiguous_no_build(self):
    with self.assertRaises(ValueError):resolve('seria legal ter algo bonito')
 def test_06_valid_candidate_scaffold(self):self.assertEqual(check(self.valid(),self.root),[])
 def test_07_reject_unknown_state(self):
    r=self.valid();r['state']='READY_TO_DEPLOY';self.assertTrue(check(r,self.root))
 def test_08_reject_missing_family(self):
    r=self.valid();r.pop('WEB_ASSET_PLAN');self.assertTrue(check(r,self.root))
 def test_09_reject_wrong_type(self):
    r=self.valid();r['execution']['paid_authorized']='false';self.assertTrue(check(r,self.root))
 def test_10_valid_bool_and_number(self):
    r=self.valid();self.assertFalse(check(r,self.root));self.assertIsInstance(r['execution']['paid_authorized'],bool)
 def test_11_reject_legacy_alias(self):
    r=self.valid();r['web_brief']=r.pop('WEB_BRIEF');self.assertTrue(check(r,self.root))
 def test_12_reject_fake_QA_pass(self):
    r=self.valid();r['verdict']=r['WEB_QA']['verdict']='PASS';self.assertTrue(check(r,self.root))
 def test_13_reject_browser_static(self):
    r=self.valid();c=r['WEB_QA']['checks'][0].copy();c.update(check_id='browser_render',result='PASS',evidence_mode='STATIC_INSPECTED');r['WEB_QA']['checks'].append(c);self.assertTrue(any(x['code']=='STATIC_AS_BROWSER' for x in check(r,self.root)))
 def test_14_reject_missing_evidence(self):
    r=self.valid();r['WEB_QA']['checks'][0]['evidence_ref']='missing.png';self.assertTrue(check(r,self.root))
 def test_15_reject_stale_source_hash(self):
    r=self.valid();r['WEB_QA']['checks'][0]['build_hash']='0'*64;self.assertTrue(check(r,self.root))
 def test_16_reject_unverified_activation(self):
    r=self.valid();r['execution']['execution_mode']='WEB_MODULE_EXECUTED';self.assertTrue(check(r,self.root))
 def test_17_reject_publication_without_approval(self):
    r=self.valid();r['route']='WEB_PUBLICATION';self.assertTrue(check(r,self.root))
 def test_18_reject_paid_fake_form(self):
    r=self.valid();r['WEB_PREVIEW_BUILD']['form_mode']='EXTERNAL_SUBMISSION';self.assertTrue(check(r,self.root))
 def test_19_reject_local_form_external(self):
    r=self.valid();r['WEB_PREVIEW_BUILD']['form_mode']='LOCAL_CALCULATION';r['WEB_PREVIEW_BUILD']['form_destination']='https://third-party.example';self.assertTrue(check(r,self.root))
 def test_20_reject_auto_user_acceptance(self):
    r=self.valid();r['state']='PREVIEW_ACCEPTED';self.assertTrue(check(r,self.root))
 def test_21_missing_file(self):
    r=self.valid();r['WEB_PREVIEW_BUILD']['source_files'].append('absent.css');self.assertTrue(check(r,self.root))
 def test_22_path_escape(self):
    r=self.valid();r['WEB_PREVIEW_BUILD']['source_files'].append('../evil.txt');self.assertTrue(check(r,self.root))
 def test_23_static_audit_clean(self):
    r=static_audit(self.root);self.assertEqual(r['missing_assets'],[]);self.assertTrue(r['reduced_motion_css_declared'])
 def test_24_revision_hero_only(self):
    after=self.base/'after';shutil.copytree(self.root,after,ignore=shutil.ignore_patterns('.web*'))
    html=(after/'index.html').read_text().replace('Sample','Updated');(after/'index.html').write_text(html)
    r=compare(self.root,after,['faq'],['hero']);self.assertTrue(r['protected_regions_unchanged']);self.assertFalse(r['target_regions_unchanged']);self.assertFalse(r['browser_retest_required'])
 def test_25_revision_shared_css_needs_browser_qa(self):
    after=self.base/'after2';shutil.copytree(self.root,after,ignore=shutil.ignore_patterns('.web*'))
    html=(after/'index.html').read_text().replace('Sample','Updated');(after/'index.html').write_text(html)
    (after/'styles.css').write_text('body{color:red}')
    r=compare(self.root,after,['faq'],['hero']);self.assertTrue(r['browser_retest_required'])
 def test_26_preview_lifecycle(self):
    a=start(self.root);self.assertEqual(a['state'],'STARTED');self.assertEqual(status(self.root)['state'],'HEALTHY_OWNED')
    b=start(self.root);self.assertEqual(b['state'],'REUSED_RUNNING');self.assertEqual(stop(self.root)['state'],'STOPPED')
 def test_27_preview_restart_from_stale(self):
    a=start(self.root);self.assertEqual(a['state'],'STARTED');self.assertEqual(stop(self.root)['state'],'STOPPED');self.assertEqual(start(self.root)['state'],'STARTED');self.assertEqual(stop(self.root)['state'],'STOPPED')
 def test_28_wrong_verdict_mismatch(self):
    r=self.valid();r['verdict']='UNVERIFIED';self.assertTrue(check(r,self.root))
 def test_29_browser_missing_marked_not_tested(self):
    checks={c['check_id']:c for c in self.valid()['WEB_QA']['checks']};self.assertEqual(checks['browser_render']['result'],'NOT_TESTED')
 def test_30_no_images_external_required(self):self.assertFalse(check(self.valid(),self.root))
 def test_31_preview_claim_needs_browser_evidence(self):
    r=self.valid();r['WEB_PREVIEW_BUILD']['preview_status']='AVAILABLE_VERIFIED';self.assertTrue(any(e['code']=='FALSE_PREVIEW_VERIFICATION' for e in check(r,self.root)))
 def test_32_critical_fail_requires_blocked(self):
    r=self.valid();r['WEB_QA']['checks'][3]['result']='FAIL';self.assertTrue(any(e['code']=='FALSE_CRITICAL_VERDICT' for e in check(r,self.root)))
 def test_33_missing_fast_test_fails(self):
    r=self.valid();r['WEB_QA']['checks']=[c for c in r['WEB_QA']['checks'] if c['check_id']!='browser_render'];self.assertTrue(any(e['code']=='MISSING_FAST_QA' for e in check(r,self.root)))
 def test_34_preview_blocks_hidden_metadata(self):
    from urllib.request import urlopen
    from urllib.error import HTTPError
    result=start(self.root)
    try:
        with self.assertRaises(HTTPError) as ctx:urlopen(result['url']+'.web-preview-owner.json')
        self.assertEqual(ctx.exception.code,403)
    finally:stop(self.root)
 def test_35_non_local_path_rejected(self):
    r=self.valid();r['WEB_PREVIEW_BUILD']['source_files'].append('/etc/passwd');self.assertTrue(check(r,self.root))

if __name__=='__main__':unittest.main(verbosity=2)
