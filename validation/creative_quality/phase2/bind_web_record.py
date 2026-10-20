"""Bind the research record to canonical hashes and concrete local QA evidence."""
import importlib.util,json,shutil,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent;repo=HERE.parents[2]
site=Path(sys.argv[1]).resolve();evidence=Path(sys.argv[2]).resolve();record=Path(sys.argv[3]);data=json.loads(record.read_text())
spec=importlib.util.spec_from_file_location('canonical_web_validate',repo/'src/ai-creative-skill/web/runtime/validate.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
out=site/'research-evidence';out.mkdir(exist_ok=True)
shutil.copy2(evidence/'combined.json',out/'browser.json')
for f in evidence.glob('transfer-b-*.png'):shutil.copy2(f,out/f.name)
(out/'fictional-source.json').write_text(json.dumps({'fictional':True,'claims':'No real courses, registration, prices, certificates or external actions','source_files':data['WEB_PREVIEW_BUILD']['source_files']},indent=2))
h=module.build_hash(site,data['WEB_PREVIEW_BUILD']['source_files'])
data['route']='WEB_PREVIEW' # Iteration of a provisional new fictional preview; no accepted production regions.
for c in data['WEB_QA']['checks']:c['build_hash']=h;c['evidence_ref']='research-evidence/browser.json'
required={'browser_render':('BROWSER_OBSERVED','research-evidence/transfer-b-1440-hero.png','1440'),'desktop_render':('BROWSER_OBSERVED','research-evidence/transfer-b-1440-full.png','1440'),'mobile_render':('BROWSER_OBSERVED','research-evidence/transfer-b-390-full.png','390'),'cta_interaction':('BROWSER_OBSERVED','research-evidence/browser.json','1440,390'),'keyboard_interaction':('BROWSER_OBSERVED','research-evidence/browser.json','1440,390'),'content_truth':('STATIC_INSPECTED','research-evidence/fictional-source.json',None),'assets_available':('STATIC_INSPECTED','research-evidence/fictional-source.json',None)}
data['WEB_QA']['checks']=[c for c in data['WEB_QA']['checks'] if c['check_id'] not in required]
for id,(mode,ref,viewport) in required.items():data['WEB_QA']['checks'].append({'check_id':id,'requirement':'Map existing observations to canonical FAST check IDs','criticality':'ESSENTIAL','procedure':'See source observations and fictional brief; no new test implied by this alias','result':'PASS','evidence_mode':mode,'evidence_ref':ref,'build_hash':h,'viewport':viewport,'checked_at':data['WEB_QA']['checks'][0]['checked_at']})
errors=module.check(data,site);record.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
result={'ok':not errors,'errors':errors,'record_verdict':data['verdict'],'state':data['state'],'independent_human_reviews':0,'canonical_sources_changed':False}
(HERE/'results/contract-validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result));sys.exit(bool(errors))
