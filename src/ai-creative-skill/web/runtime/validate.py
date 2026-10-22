"""Web Experience MVP v0.2. Contract and evidence validator, not a design-quality scorer."""
import hashlib,json,os,pathlib,sys,datetime
from jsonschema import Draft202012Validator
SCHEMA=pathlib.Path(__file__).resolve().parents[1]/'schemas/web_delivery_v0.2.schema.json'
CANONICAL=json.loads(SCHEMA.read_text())
VALIDATOR=Draft202012Validator(CANONICAL)
VALID_RESULTS={'PASS','FAIL','NOT_TESTED','NOT_APPLICABLE'}
BROWSER_NEEDED={'browser_render','desktop_render','mobile_render','narrow_render','images_rendered','cta_interaction','keyboard_interaction','responsive','reduced_motion','form_behavior'}
REQUIRED_FAST_CHECKS={'browser_render','desktop_render','mobile_render','cta_interaction','keyboard_interaction','content_truth','assets_available'}

def sha256(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
    return h.hexdigest()

def contained_path(root,ref):
    if not ref or '://' in ref: return None
    target=(pathlib.Path(root)/ref).resolve()
    if not target.is_relative_to(pathlib.Path(root).resolve()):return None
    return target

def todo_paths(node,path=''):
    """Strings still starting with TODO, as left by the record draft."""
    if isinstance(node,str):return [path] if node.lstrip().upper().startswith('TODO') else []
    items=node.items() if isinstance(node,dict) else enumerate(node) if isinstance(node,list) else []
    return [p for k,v in items for p in todo_paths(v,f'{path}/{k}' if path else str(k))]

def check(record, project_root, package_installed=False):
    """Returns machine errors; cannot certify browser actions, product truth or rights."""
    errors=[{'code':'UNFILLED_FIELD','path':path,'message':'Placeholder left by creative_web.py record; fill it'} for path in todo_paths(record)]
    todo={e['path'] for e in errors}
    for e in VALIDATOR.iter_errors(record):
        path='/'.join(map(str,e.absolute_path))
        if path not in todo:errors.append({'code':'SCHEMA','path':path,'message':e.message[:210]})
    if errors: return errors
    def fail(code,path,message):errors.append({'code':code,'path':path,'message':message})
    ex=record['execution'];build=record['WEB_PREVIEW_BUILD'];qa=record['WEB_QA'];brief=record['WEB_BRIEF'];asset=record['WEB_ASSET_PLAN']
    if ex['execution_mode']=='WEB_MODULE_EXECUTED' and (not package_installed or not ex.get('activation_evidence')):
        fail('UNVERIFIED_ACTIVATION','execution/execution_mode','Module execution requires independent activation evidence and installed candidate')
    if record['route']=='WEB_PUBLICATION' and not ex['public_deploy_authorized']:
        fail('PUBLICATION_GATE','execution/public_deploy_authorized','Publication needs specific authority')
    if record['state'] in ('PUBLICATION_APPROVED','LIVE_VERIFIED') and not ex['public_deploy_authorized']:
        fail('PUBLICATION_GATE','state','Preview approval does not grant deployment')
    if build['form_mode']=='EXTERNAL_SUBMISSION' and not build.get('form_destination'):
        fail('MISSING_FORM_DESTINATION','WEB_PREVIEW_BUILD/form_destination','Real submission must declare destination')
    if build['form_mode']=='LOCAL_CALCULATION' and build.get('form_destination'):
        fail('FORM_CONTRADICTION','WEB_PREVIEW_BUILD/form_destination','Local calculation cannot claim external destination')
    if build['form_mode']=='MOCK_INPUT' and build['primary_cta_behavior']=='REAL_VERIFIED_LINK':
        fail('MOCK_CTA_CONTRADICTION','WEB_PREVIEW_BUILD/primary_cta_behavior','Mock input cannot be described as a real CTA submission')
    if record['state']=='PREVIEW_ACCEPTED':
        fail('HUMAN_APPROVAL_NOT_AUTOMATABLE','state','Requires separately verified explicit human approval; not accepted in offline validator')
    if record['route']=='WEB_EDIT' and not record['WEB_REVISION'].get('approval_reference'):
        # Can edit unapproved regions, but cannot claim preserve accepted regions.
        if record['WEB_REVISION']['preserve_regions']:
            fail('UNVERIFIED_PRESERVE_APPROVAL','WEB_REVISION/approval_reference','Preserved human-approved region requires approval reference')
    required_files=build['source_files'] if record['route'] in ('WEB_PREVIEW','WEB_EDIT','WEB_PUBLICATION') else []
    for i,p in enumerate(required_files):
        t=contained_path(project_root,p)
        if t is None or not t.is_file():fail('MISSING_SOURCE','WEB_PREVIEW_BUILD/source_files/'+str(i),'Referenced local source must exist under project root')
    for i,item in enumerate(asset['assets_used']):
        path=item['path'];t=contained_path(project_root,path)
        if t is None or not t.is_file():fail('MISSING_ASSET','WEB_ASSET_PLAN/assets_used/'+str(i),'Asset not present or path unsafe')
        if record['route']=='WEB_PUBLICATION' or record['state'] in ('PUBLICATION_PREFLIGHT','PUBLICATION_APPROVED','LIVE_VERIFIED'):
            # A human review record + content binding is a preflight requirement,
            # never legal certification or a replacement for deployment authority.
            clearance=item.get('publication_clearance',{})
            evidence=contained_path(project_root,clearance.get('evidence_ref'))
            compatible=(item['approval']=='APPROVED_FOR_THIS_USE' and item['rights']!='UNKNOWN'
                and item['use_scope'] in clearance.get('allowed_uses',[])
                and clearance.get('conditions_status') in ('SATISFIED','NOT_APPLICABLE')
                and (item['rights']!='RESTRICTED' or clearance.get('conditions_status')=='SATISFIED'))
            bound=(t is not None and t.is_file() and evidence is not None and evidence.is_file()
                and evidence.stat().st_size>0 and evidence!=t
                and clearance.get('asset_sha256')==sha256(t)
                and clearance.get('evidence_sha256')==sha256(evidence))
            if not compatible or not bound:
                fail('RIGHTS_GATE','WEB_ASSET_PLAN/assets_used/'+str(i),
                     'Publication requires scoped approval and a current, asset-bound rights review with satisfied conditions; declarations alone are insufficient')
    for field in ['product_service_truth_refs','known_unknown_boundary']:
        for s in brief[field]:
            if not s.strip():fail('EMPTY_TRUTH','WEB_BRIEF/'+field,'Empty item')
    if brief['business_kind']=='DIGITAL_PRODUCT' and not brief.get('regulated_claim_boundary') and 'finance' in (brief['deliverable_scope']+' '+brief['user_goal']).lower():
        fail('MISSING_REGULATED_BOUNDARY','WEB_BRIEF/regulated_claim_boundary','Financial-facing flow needs claim boundary')
    if brief['business_kind']=='PHYSICAL_PRODUCT' and not brief.get('product_material_scale_truth_state'):
        fail('MISSING_PRODUCT_TRUTH','WEB_BRIEF/product_material_scale_truth_state','Product needs clear facts/unknowns')
    if brief['brand_authority_state'] in ('EXISTING_APPROVED','EXISTING_MIXED') and not brief.get('current_brand_refs'):
        fail('MISSING_BRAND_REF','WEB_BRIEF/current_brand_refs','Existing brand needs pointers')
    if build['primary_cta_behavior'] in ('REAL_VERIFIED_LINK','CONTACT_LINK_VERIFIED') and not build['external_link_targets'] and not build['primary_cta_behavior']=='REAL_VERIFIED_LINK':
        fail('NO_DESTINATION','WEB_PREVIEW_BUILD/external_link_targets','External contact needs destination')
    if record['WEB_DIRECTION'].get('motion_fallback_and_controls') and not build.get('prefers_reduced_motion_fallback'):
        fail('MISSING_REDUCED_MOTION','WEB_PREVIEW_BUILD/prefers_reduced_motion_fallback','Motion requires fallback declaration')
    checks=qa['checks'];seen=set()
    for i,c in enumerate(checks):
        path=f'WEB_QA/checks/{i}'
        if c['check_id'] in seen:fail('DUPLICATE_CHECK',path,'Duplicate check_id')
        seen.add(c['check_id'])
        if c['result'] in ('NOT_TESTED','NOT_APPLICABLE') and not c.get('reason'):
            fail('MISSING_REASON',path+'/reason','Not-tested and N/A require reason')
        if c['result']=='PASS' and c['evidence_mode']=='NONE':fail('FALSE_EVIDENCE_PASS',path,'PASS requires evidence mode')
        if c['result']=='PASS' and c['check_id'] in BROWSER_NEEDED and c['evidence_mode']!='BROWSER_OBSERVED':
            fail('STATIC_AS_BROWSER',path,'Browser runtime requirement not proven by code review')
        if c['result']=='PASS' and not c['evidence_ref']:fail('MISSING_EVIDENCE',path+'/evidence_ref','PASS requires verifiable file')
        if c['evidence_ref']:
            file=contained_path(project_root,c['evidence_ref'])
            if file is None or not file.is_file():fail('EVIDENCE_FILE_MISSING',path+'/evidence_ref','Evidence not in root')
        if c['build_hash']!=build_hash(project_root,required_files):
            fail('STALE_BUILD_EVIDENCE',path+'/build_hash','QA check build hash does not match current source')
    if build['preview_status']=='AVAILABLE_VERIFIED' and not any(c['check_id']=='browser_render' and c['result']=='PASS' and c['evidence_mode']=='BROWSER_OBSERVED' for c in checks):
        fail('FALSE_PREVIEW_VERIFICATION','WEB_PREVIEW_BUILD/preview_status','Verified preview needs actual browser evidence')
    if any(c['criticality']=='CRITICAL' and c['result']=='FAIL' for c in checks) and qa['verdict']!='BLOCKED':
        fail('FALSE_CRITICAL_VERDICT','WEB_QA/verdict','Critical failure requires BLOCKED')
    if record['route'] in ('WEB_PREVIEW','WEB_EDIT') and not REQUIRED_FAST_CHECKS.issubset(seen):
        fail('MISSING_FAST_QA','WEB_QA/checks','Essential FAST checks missing: '+str(sorted(REQUIRED_FAST_CHECKS-seen)))
    if qa['verdict']=='PASS':
        if not REQUIRED_FAST_CHECKS.issubset(seen):fail('MISSING_FAST_QA','WEB_QA/checks',str(sorted(REQUIRED_FAST_CHECKS-seen)))
        bad=[x['check_id'] for x in checks if x['criticality'] in ('CRITICAL','ESSENTIAL') and x['result']!='PASS']
        if bad: fail('FALSE_AGGREGATE_PASS','WEB_QA/verdict','Essential checks not PASS: '+str(bad))
        if build['preview_status']!='AVAILABLE_VERIFIED':fail('PREVIEW_UNVERIFIED','WEB_PREVIEW_BUILD/preview_status','PASS needs verified preview')
    if qa['verdict']!=record['verdict']:fail('VERDICT_MISMATCH','verdict','Aggregate and QA verdict must agree')
    if record['verdict']=='PASS' and record['state'] not in ('PREVIEW_DRAFT','PREVIEW_REVIEWED'):
        fail('PASS_STATE_INVALID','state','PASS means scoped QA passed, not human approval')
    return errors

def build_hash(root,files):
    h=hashlib.sha256()
    for p in sorted(files):
        f=contained_path(root,p)
        if f is None or not f.is_file(): continue
        h.update(p.encode());h.update(sha256(f).encode())
    return h.hexdigest()

def run_cli():
    import argparse
    p=argparse.ArgumentParser();p.add_argument('record');p.add_argument('--root',required=True);p.add_argument('--installed',action='store_true')
    a=p.parse_args();obj=json.loads(pathlib.Path(a.record).read_text());errors=check(obj,a.root,package_installed=a.installed)
    print(json.dumps({'valid':not errors,'errors':errors},indent=2,ensure_ascii=False));sys.exit(1 if errors else 0)
if __name__=='__main__':run_cli()
