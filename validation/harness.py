"""Execute probes against canonical helpers; no production orchestration or paid adapter."""
from __future__ import annotations
import argparse, copy, datetime, hashlib, importlib.util, io, json, platform, random
import shutil, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor
from dataclasses import replace
from pathlib import Path
from unittest.mock import patch
from urllib.request import urlopen
from urllib.error import HTTPError
from importlib.metadata import version
ROOT=Path(__file__).resolve().parents[1]
SKILL=ROOT/'src/ai-creative-skill'
sys.path.insert(0,str(SKILL/'web'));sys.path.insert(0,str(SKILL/'media/runtime'))
from runtime import router, validate, revision, preview, migrate, qa
import media_upscale_v02 as media
import media_upscale_v03 as neural
from validation.generators.pairwise import generate, coverage
from validation.simulations.economics import sensitivity
from validation import invariants

def module_from(path,name):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec)
    sys.modules[name]=m;spec.loader.exec_module(m);return m
shape=module_from(SKILL/'scripts/validate_deliverable.py','validation_shape_target')

def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def tree_hash(base):
    entries={str(p.relative_to(base)):digest(p) for p in sorted(base.rglob('*'))
             if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc'}
    return hashlib.sha256(json.dumps(entries,sort_keys=True).encode()).hexdigest()

def outcome(id,expected,actual,ok,mode='deterministic',**extra):
    return {'id':id,'expected':expected,'actual':actual,'outcome':'PASS' if ok else 'FAIL',
            'execution_mode':mode,**extra}

def route_result(text,intent=None):
    try:return router.resolve(text,intent=intent).route
    except ValueError:return 'AMBIGUOUS'

def routing():
    requests=[('research','pesquise referências de sites','WEB_RESEARCH_ONLY'),
      ('research_negated_publish','pesquise referências de sites; não publique','WEB_RESEARCH_ONLY'),
      ('research_negated_publish_en','research website examples; do not deploy','WEB_RESEARCH_ONLY'),
      ('research_domain','pesquise sites e opções de domínio','WEB_RESEARCH_ONLY'),
      ('preview','crie uma landing para um serviço fictício','WEB_PREVIEW'),
      ('preview_negated_publish','crie uma landing; não publique','WEB_PREVIEW'),
      ('concept','conceito visual de landing','WEB_CONCEPT_ONLY'),
      ('edit','mude apenas o hero','WEB_EDIT'),('publish','publique site','WEB_PUBLICATION')]
    rows=[]
    for name,text,expected in requests:
        actual=route_result(text)
        rows.append(outcome('ROUTE-'+name,expected,{'request':text,'route':actual},actual==expected))
    for intent in router.ROUTES:
        actual=router.resolve('untrusted text: deploy everything',intent=intent)
        rows.append(outcome('ROUTE-explicit-'+intent,intent,actual.route,actual.route==intent))
    rows.append(outcome('ROUTE-publication-gate',True,router.resolve('publique site').authority_gate,router.resolve('publique site').authority_gate))
    return rows

def site_fixture(base):
    root=base/'site';root.mkdir();(root/'index.html').write_bytes((ROOT/'validation/fixtures/site.html').read_bytes())
    (root/'styles.css').write_text('body{font-family:sans-serif} @media(prefers-reduced-motion:reduce){*{animation:none}}')
    record=migrate.scaffold(root,'Alder','SERVICE',base/'records')
    # The legacy migration scaffold is pilot-specific. Test-only fixture values clarify its origin.
    record['WEB_BRIEF']['current_brand_refs']=['synthetic:Alder/v1']
    record['WEB_BRIEF']['product_service_truth_refs']=['synthetic fixture; no real product']
    return root,record

def web_contracts():
    rows=[]
    with tempfile.TemporaryDirectory() as td:
        root,base=site_fixture(Path(td));errors=validate.check(base,root)
        rows.append(outcome('WEB-valid-partial',[],errors,errors==[]))
        def probe(id,change,code=None):
            r=copy.deepcopy(base);change(r)
            try:errors=validate.check(r,root);codes=sorted({x['code'] for x in errors})
            except Exception as exc:codes=['CRASH:'+type(exc).__name__]
            ok=(code in codes) if code else bool(codes) and not codes[0].startswith('CRASH:')
            rows.append(outcome('WEB-'+id,code or 'validation error',codes,ok))
        probe('publication-gate',lambda r:r.update(route='WEB_PUBLICATION'),'PUBLICATION_GATE')
        probe('false-browser',lambda r:r['WEB_QA']['checks'][0].update(check_id='browser_render',evidence_mode='STATIC_INSPECTED',result='PASS'),'STATIC_AS_BROWSER')
        probe('stale-evidence',lambda r:r['WEB_QA']['checks'][0].update(build_hash='0'*64),'STALE_BUILD_EVIDENCE')
        probe('missing-evidence',lambda r:r['WEB_QA']['checks'][0].update(evidence_ref='missing.txt'),'EVIDENCE_FILE_MISSING')
        probe('human-acceptance',lambda r:r.update(state='PREVIEW_ACCEPTED'),'HUMAN_APPROVAL_NOT_AUTOMATABLE')
        probe('critical-failure',lambda r:r['WEB_QA']['checks'][3].update(result='FAIL'),'FALSE_CRITICAL_VERDICT')
        for value in ('false',1,None):
            probe('typed-approval-'+repr(value),lambda r,v=value:r['execution'].update(paid_authorized=v),'SCHEMA')
        for ref in ('../outside.txt','https://example.invalid/source','/synthetic-does-not-exist'):
            probe('unsafe-source-'+str(len(rows)),lambda r,v=ref:r['WEB_PREVIEW_BUILD']['source_files'].append(v),'MISSING_SOURCE')
        (root/'asset.txt').write_text('synthetic asset')
        for rights,approval in [('UNKNOWN','PROVISIONAL'),('RESTRICTED','APPROVED_FOR_THIS_USE'),('UNKNOWN','APPROVED_FOR_THIS_USE')]:
            def change(r):
                r['route']='WEB_PUBLICATION';r['execution']['public_deploy_authorized']=True
                r['WEB_ASSET_PLAN']['assets_used']=[{'path':'asset.txt','origin':'synthetic','approval':approval,'rights':rights,'use_scope':'private_preview_only'}]
            probe('rights-'+rights+'-'+approval,change,'RIGHTS_GATE')
        r=copy.deepcopy(base);r['WEB_PREVIEW_BUILD'].update(primary_cta_behavior='REAL_VERIFIED_LINK',external_link_targets=[])
        errors=validate.check(r,root)
        rows.append(outcome('WEB-internal-cta-no-external-target','valid internal anchor needs no external target',errors,not errors))
        probe('missing-revision',lambda r:r.update(route='WEB_EDIT'),'SCHEMA')
        # Identical paths but changed asset content should stale browser evidence too.
        r=copy.deepcopy(base);r['WEB_PREVIEW_BUILD']['source_files'].append('asset.txt')
        for c in r['WEB_QA']['checks']:c['build_hash']=validate.build_hash(root,r['WEB_PREVIEW_BUILD']['source_files'])
        (root/'asset.txt').write_text('altered synthetic brand')
        rows.append(outcome('WEB-content-change','STALE_BUILD_EVIDENCE',[e['code'] for e in validate.check(r,root)],any(e['code']=='STALE_BUILD_EVIDENCE' for e in validate.check(r,root))))
    return rows

def preserve():
    rows=[]
    with tempfile.TemporaryDirectory() as td:
        root,record=site_fixture(Path(td))
        for name,change_protected,change_css,new_js in [('allowed',False,False,False),('protected',True,False,False),('protected-plus-css',True,True,False),('new-script',False,False,True)]:
            after=Path(td)/name;shutil.copytree(root,after)
            s=(after/'index.html').read_text().replace('Alder Studio — fictional workshop','New fictional hero')
            if change_protected:s=s.replace('No commercial claims or submissions.','Fabricated claim')
            (after/'index.html').write_text(s)
            if change_css:(after/'styles.css').write_text('body{color:red}')
            if new_js:
                (after/'app.js').write_text('document.body.style.display="none"')
                (after/'index.html').write_text(s.replace('</body>','<script src="app.js"></script></body>'))
            actual=revision.compare(root,after,['facts'],['hero'])
            ok=actual['status']=='FAIL' if change_protected else (actual['browser_retest_required'] if new_js else actual['status']=='SOURCE_PRESERVATION_PASS')
            rows.append(outcome('PRESERVE-'+name,'FAIL dominates' if change_protected else ('browser retest' if new_js else 'source pass'),actual,ok))
    return rows

def structural():
    catalog=json.loads(shape.CATALOG.read_text())['types'];rows=[]
    for typ,spec in catalog.items():
        valid={k:'Synthetic substantive fixture' for k in spec['required']}
        r=shape.inspect(typ,valid);rows.append(outcome('SHAPE-valid-'+typ,'PASS_STRUCTURAL; semantic false',r,r['result']=='PASS_STRUCTURAL' and r['semantic_verified'] is False))
        for k in spec['required']:
            bad=dict(valid);bad.pop(k);r=shape.inspect(typ,bad)
            rows.append(outcome('SHAPE-missing-'+typ+'-'+k,'FAIL_STRUCTURAL',r,r['result']=='FAIL_STRUCTURAL'))
        for trigger,fields in spec['conditional'].items():
            r=shape.inspect(typ,valid,[trigger]);rows.append(outcome('SHAPE-conditional-'+typ+'-'+trigger,'FAIL_STRUCTURAL',r,r['result']=='FAIL_STRUCTURAL'))
        bad={k:' \t\n ' for k in spec['required']};r=shape.inspect(typ,bad)
        rows.append(outcome('SHAPE-whitespace-'+typ,'FAIL_STRUCTURAL',r,r['result']=='FAIL_STRUCTURAL'))
    r=shape.inspect('CONTENT_IDEA',{},scope='BOUNDED');rows.append(outcome('SHAPE-independent-bounded','BOUNDED_SCOPE',r,r['result']=='BOUNDED_SCOPE'))
    return rows

def image_fixture(base,mode='RGBA'):
    from PIL import Image,ImageDraw
    p=base/'source.png';im=Image.new(mode,(64,48),(30,90,140,120) if mode=='RGBA' else (30,90,140))
    ImageDraw.Draw(im).rectangle((8,8,35,30),fill=(220,20,90,255) if mode=='RGBA' else (220,20,90));im.save(p)
    return media.MediaRequest(str(p),128,96)

def media_properties():
    rows=[];rng=random.Random(20261020)
    with tempfile.TemporaryDirectory() as td:
        base=Path(td);req=image_fixture(base);original=media.sha(req.source)
        for n,scale in enumerate(rng.sample(range(2,7),5)):
            r=replace(req,target_width=64*scale,target_height=48*scale)
            q=media.quote(r);copy_path=base/f'copy{n}.png';shutil.copyfile(req.source,copy_path)
            q2=media.quote(replace(r,source=str(copy_path)))
            rows.append(outcome(f'MEDIA-path-invariant-{n}','equal content fingerprints',q['fingerprint']==q2['fingerprint'],q['fingerprint']==q2['fingerprint']))
        controls=[('paid',{'allow_paid_submission':True}),('upload',{'allow_external_transfer':True}),
          ('mock',{'route_id':'mock.bfl.direct.video.v0.2','media_kind':'VIDEO'}),('fake-provider',{'route_id':'invented.free.all-capabilities'}),
          ('kind',{'media_kind':'VIDEO'}),('budget-nan',{'max_additional_cash_usd':'NaN'}),('budget-negative',{'max_additional_cash_usd':'-1'}),
          ('budget-infinity',{'max_additional_cash_usd':'Infinity'}),('bool-width',{'target_width':True}),('float-width',{'target_width':128.0}),('aspect',{'target_width':129,'target_height':300})]
        for name,kwargs in controls:
            try:media.quote(replace(req,**kwargs));actual='ACCEPTED'
            except media.MediaError as e:actual=str(e)
            rows.append(outcome('MEDIA-reject-'+name,'MediaError',actual,actual!='ACCEPTED'))
        result=media.run_image(req,base/'output');again=media.run_image(req,base/'output')
        rows.append(outcome('MEDIA-real-local-image','technical only, source intact, alpha retained, idempotent',
            {'state':result['state'],'reuse':again['state'],'fidelity':result['qa']['fidelity_verdict'],'source_intact':media.sha(req.source)==original,'checks':result['qa']['checks']},
            result['qa']['fidelity_verdict']=='UNVERIFIED' and again['state']=='IDEMPOTENT_REUSE' and media.sha(req.source)==original and all(result['qa']['checks'].values())))
        Path(result['output']).write_bytes(b'corrupt synthetic result')
        try:media.run_image(req,base/'output');actual='REPEATED'
        except media.MediaError as e:actual=str(e)
        rows.append(outcome('MEDIA-corrupt-output','RECOVERY_REQUIRED',actual,'RECOVERY_REQUIRED' in actual))
        # Content changes must invalidate quotes, independent of path.
        from PIL import Image
        Image.new('RGBA',(64,48),(1,2,3,255)).save(req.source)
        rows.append(outcome('MEDIA-content-fingerprint','different source fingerprint',media.quote(req)['fingerprint']!=result['quote']['fingerprint'],media.quote(req)['fingerprint']!=result['quote']['fingerprint']))
    return rows

def faults():
    rows=[]
    with tempfile.TemporaryDirectory() as td:
        base=Path(td);req=image_fixture(base);q=media.quote(req)
        with patch.object(media.shutil,'which',return_value=None), patch.object(media,'video_probe',side_effect=AssertionError('Dependency gate bypassed')):
            try:media.quote(replace(req,route_id=media.VIDEO_CONV,media_kind='VIDEO'));actual='ACCEPTED'
            except media.MediaError as exc:actual=str(exc)
        rows.append(outcome('FAULT-missing-ffmpeg','ROUTE_UNAVAILABLE_ON_HOST',actual,actual=='ROUTE_UNAVAILABLE_ON_HOST',mode='mocked'))
        for state in ['SUBMITTING','UNKNOWN','QA_FAILED','COMPLETE','CANCELLED']:
            out=base/state;out.mkdir();(out/'image_execution_ledger.json').write_text(json.dumps({q['fingerprint']:{'state':state,'output_file':'missing.png'}}))
            try:media.run_image(req,out);actual='REPEATED'
            except Exception as e:actual=str(e)
            rows.append(outcome('FAULT-resume-'+state,'RECOVERY_REQUIRED',actual,'RECOVERY_REQUIRED' in actual))
        for name,exception in [('timeout',TimeoutError('synthetic timeout')),('storage',OSError('synthetic disk failure'))]:
            out=base/name
            with patch.object(media.Image.Image,'save',side_effect=exception):
                try:media.run_image(req,out)
                except type(exception):pass
            ledger=json.loads((out/'image_execution_ledger.json').read_text())
            try:media.run_image(req,out);actual='REPEATED'
            except media.MediaError as e:actual=str(e)
            rows.append(outcome('FAULT-'+name,'UNKNOWN then no retry',{'ledger':ledger[q['fingerprint']]['state'],'resume':actual},ledger[q['fingerprint']]['state']=='UNKNOWN' and 'RECOVERY_REQUIRED' in actual,mode='mocked'))
        out=base/'commit-failure';real=media.save_atomic;calls=[]
        def fail_final(path,data):
            calls.append(1)
            if len(calls)==2:raise OSError('synthetic failure after output promotion')
            return real(path,data)
        with patch.object(media,'save_atomic',side_effect=fail_final):
            try:media.run_image(req,out)
            except OSError:pass
        try:media.run_image(req,out);actual='REPEATED'
        except media.MediaError as e:actual=str(e)
        rows.append(outcome('FAULT-final-ledger-commit','no duplicate after interrupted commit',actual,'RECOVERY_REQUIRED' in actual,mode='mocked'))
        raw=io.BytesIO(b'12345')
        try:neural._read_exact(raw,6);actual='ACCEPTED'
        except media.MediaError as e:actual=str(e)
        rows.append(outcome('FAULT-truncated-frame','TRUNCATED_RAW_VIDEO_FRAME',actual,actual=='TRUNCATED_RAW_VIDEO_FRAME'))
        out=base/'concurrent'
        with ThreadPoolExecutor(max_workers=4) as pool:states=[r['state'] for r in pool.map(lambda _:media.run_image(req,out),range(4))]
        rows.append(outcome('FAULT-concurrent-local','one execution, three reuses',sorted(states),states.count('EXECUTED_TECHNICAL_QA_PASS')==1 and states.count('IDEMPOTENT_REUSE')==3))
    return rows

def pairwise():
    domains={'paid':[False,True],'upload':[False,True],'budget':['0.00','NaN'],
             'route':['known','unknown'],'dimensions':['valid','invalid'],'source':['valid','corrupt']}
    combos=generate(domains);rows=[]
    with tempfile.TemporaryDirectory() as td:
        base=Path(td);req=image_fixture(base);bad=base/'bad.png';bad.write_text('not an image')
        for i,c in enumerate(combos):
            r=replace(req,source=str(bad) if c['source']=='corrupt' else req.source,
                allow_paid_submission=c['paid'],allow_external_transfer=c['upload'],max_additional_cash_usd=c['budget'],
                route_id=media.IMAGE_CONV if c['route']=='known' else 'invented',target_width=128 if c['dimensions']=='valid' else 0)
            allowed=not c['paid'] and not c['upload'] and c['budget']=='0.00' and c['route']=='known' and c['dimensions']=='valid' and c['source']=='valid'
            try:media.quote(r);actual=True
            except (media.MediaError,OSError):actual=False
            rows.append(outcome(f'PAIR-{i:02}','accept' if allowed else 'reject',{'input':c,'accepted':actual},actual==allowed))
    stats=coverage(domains,combos);rows.append(outcome('PAIR-coverage','all pair interactions',stats,stats['missing_pairs']==0))
    return rows

def preview_checks():
    rows=[]
    with tempfile.TemporaryDirectory() as td:
        base=Path(td);root,record=site_fixture(base);(root/'.synthetic-hidden').write_text('SYNTHETIC_NOT_A_SECRET')
        outside=base/'outside-fixture.txt';outside.write_text('SYNTHETIC_OUTSIDE_ROOT');(root/'linked.txt').symlink_to(outside)
        result=preview.start(root)
        try:
            for id,path in [('plain-hidden','.synthetic-hidden'),('encoded-hidden','%2esynthetic-hidden'),('symlink-escape','linked.txt')]:
                try:
                    with urlopen(result['url']+path,timeout=3) as response:status=response.status;body=response.read().decode()
                except HTTPError as e:status=e.code;body='denied'
                rows.append(outcome('PREVIEW-'+id,'403 or 404',{'http_status':status,'synthetic_fixture_returned':body.startswith('SYNTHETIC')},status in (403,404)))
            a=preview.start(root);rows.append(outcome('PREVIEW-reuse','REUSED_RUNNING',a['state'],a['state']=='REUSED_RUNNING'))
        finally:preview.stop(root)
        rows.append(outcome('PREVIEW-stopped','STALE_OR_UNVERIFIED',preview.status(root)['state'],preview.status(root)['state']=='STALE_OR_UNVERIFIED'))
    return rows

def video_checks():
    if not shutil.which('ffmpeg') or not shutil.which('ffprobe'):
        return [{'id':'VIDEO-synthetic','expected':'local FFmpeg technical pass','actual':'FFmpeg unavailable','outcome':'BLOCKED','execution_mode':'deterministic'}]
    rows=[]
    with tempfile.TemporaryDirectory() as td:
        base=Path(td);src=base/'synthetic.mp4'
        subprocess.run(['ffmpeg','-v','error','-f','lavfi','-i','testsrc2=size=64x48:rate=12:duration=1','-f','lavfi','-i','sine=frequency=440:duration=1','-c:v','libx264','-pix_fmt','yuv420p','-c:a','aac','-shortest','-y',str(src)],check=True,capture_output=True,timeout=30)
        req=media.MediaRequest(str(src),128,96,route_id=media.VIDEO_CONV,media_kind='VIDEO')
        result=media.run_video(req,base/'out');again=media.run_video(req,base/'out')
        rows.append(outcome('VIDEO-synthetic','actual local encode, technical pass and idempotent',{'status':result['status'],'qa_kind':result['qa']['kind'],'checks':result['qa']['checks'],'reuse':again['status']},result['qa']['status']=='PASS' and again['status']=='IDEMPOTENT_REUSE' and result['qa']['kind']=='TECHNICAL_QA_ONLY'))
    return rows

def mutations():
    rows=[]
    specs=[('router-authority',SKILL/'web/runtime/router.py','build,auth=ROUTES[r]','build,auth=(True,False)'),
           ('media-paid',SKILL/'media/runtime/media_upscale_v02.py','if not isinstance(self.allow_paid_submission,bool) or self.allow_paid_submission:','if False:'),
           ('shape-missing',SKILL/'scripts/validate_deliverable.py',"missing=[k for k in needed if k not in item or item[k] is None or (isinstance(item[k],str) and not item[k].strip()) or item[k]==[] or item[k]=={}]",'missing=[]')]
    with tempfile.TemporaryDirectory() as td:
        base=Path(td);req=image_fixture(base)
        for name,source,old,new in specs:
            text=source.read_text();assert text.count(old)==1,'Mutation anchor drift'
            # Isolated full package preserves relative contract paths; canonical tree untouched.
            target=base/name/'skill';shutil.copytree(SKILL,target,ignore=shutil.ignore_patterns('__pycache__'))
            p=target/source.relative_to(SKILL);p.write_text(text.replace(old,new))
            m=module_from(p,'mutant_'+name.replace('-','_'))
            check,canonical = {'router-authority':(invariants.publication_requires_authority,router),
                'media-paid':(lambda module:invariants.paid_request_is_rejected(module,req.source),media),
                'shape-missing':(invariants.missing_fields_are_rejected,shape)}[name]
            check(canonical)  # baseline control must pass before accepting a kill
            try:check(m);killed=False
            except AssertionError:killed=True
            evidence={'detected':killed,'baseline_control':'PASS','mutation':old+' -> '+new,
                      'oracle':'validation/invariants.py; also called by tests/test_validation_harness.py'}
            if name=='router-authority':
                proc=subprocess.run([sys.executable,'-m','unittest','test_web_runtime.WebTests.test_04_route_publication_gate'],
                    cwd=target/'web/tests',capture_output=True,text=True,timeout=30)
                evidence['preexisting_test_detected']=proc.returncode==1 and 'FAILED (failures=1)' in proc.stderr
                killed=killed and evidence['preexisting_test_detected']
            rows.append(outcome('MUTATION-'+name,'regression oracle detects injected defect',evidence,killed))
    return rows

GROUPS={'routing':routing,'web_contracts':web_contracts,'preserve':preserve,'structural':structural,
        'media':media_properties,'faults':faults,'pairwise':pairwise,'mutations':mutations}

def run(include_host=False):
    before=tree_hash(SKILL);records=[]
    for group,fn in {**GROUPS,**({'preview':preview_checks,'video':video_checks} if include_host else {})}.items():
        try:rr=fn()
        except Exception as exc:rr=[{'id':'HARNESS-'+group,'expected':'group executes','actual':type(exc).__name__+': '+str(exc)[:180],'outcome':'FAIL','execution_mode':'deterministic','classification':'HARNESS_OR_ENVIRONMENT_ERROR'}]
        for row in rr:row['group']=group
        records.extend(rr)
    assert tree_hash(SKILL)==before,'Canonical source mutation detected'
    return records

def harness_hash():
    entries={str(p.relative_to(ROOT)):digest(p) for p in sorted((ROOT/'validation').rglob('*'))
             if p.is_file() and '__pycache__' not in p.parts and 'reports' not in p.parts and p.suffix in ('.py','.json','.txt','.html')}
    return hashlib.sha256(json.dumps(entries,sort_keys=True).encode()).hexdigest()

def tool_version(tool):
    if not shutil.which(tool):return 'UNAVAILABLE'
    return subprocess.check_output([tool,'--version' if tool=='node' else '-version'],text=True).splitlines()[0]

def environment():
    def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT,text=True).strip()
    complete_history=git('rev-parse','--is-shallow-repository')=='false'
    return {'python':platform.python_version(),'os':platform.system(),'release':platform.release(),'machine':platform.machine(),
      'packages':{name:version(name) for name in ['Pillow','numpy','jsonschema','beautifulsoup4']},
      'git_head':git('rev-parse','HEAD'),'source_commit':git('log','-1','--format=%H','--','src/ai-creative-skill') if complete_history else None,
      'source_commit_history_complete':complete_history,
      'dirty':bool(git('status','--porcelain')),'canonical_tree_sha256':tree_hash(SKILL),
      'harness_sha256':harness_hash(),
      'executed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'tools':{tool:tool_version(tool) for tool in ('ffmpeg','ffprobe','node')},
      'seed':20261020,'provider_calls':0,'paid_calls':0,'private_assets_used':False}

def expectation_errors(records,known,signatures=None,expected_ids=None):
    failures={r['id'] for r in records if r['outcome']=='FAIL'}
    relevant={r['id'] for r in records};expected=set(known)&relevant
    return {'unexpected_failures':sorted(failures-expected),'resolved_findings_need_review':sorted(expected-failures),
            'blocked':sorted(r['id'] for r in records if r['outcome']=='BLOCKED'),
            'missing_records':sorted(set(expected_ids or [])-relevant),
            'changed_failure_evidence':sorted(r['id'] for r in records if r['id'] in (signatures or {}) and
                r['outcome']=='FAIL' and r['actual']!=signatures[r['id']])}

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',default='validation/reports/current.json');p.add_argument('--host',action='store_true');p.add_argument('--check',action='store_true');a=p.parse_args()
    records=run(a.host);catalog=json.loads((ROOT/'validation/scenarios/register.json').read_text())
    for row in records:
        group=catalog['groups'][row['group']]
        for key in ('capability','contract','risk','fixture_refs','severity','recommended_correction','regression_coverage'):row[key]=group[key]
        row['reproducibility']='python -m validation.harness'+(' --host' if a.host else '')
        row['evidence_ref']='records/'+row['id']
        row['execution_performed']=True
        row['environment_ref']='environment'
        row['inputs_ref']='validation/harness.py:'+row['group']
    for gap in catalog['unexecuted']:records.append(gap)
    known=json.loads((ROOT/'validation/known_findings.json').read_text())
    expected_ids=[id for id,group in known.get('expected_record_groups',{}).items() if a.host or group not in ('preview','video')]
    review=expectation_errors(records,known['expected_failures'],known.get('actual_signatures'),expected_ids)
    result={'schema_version':'1.0','harness_version':'0.1.0','environment':environment(),'records':records,
            'summary':{s:sum(r['outcome']==s for r in records) for s in ('PASS','FAIL','BLOCKED','NOT_RUN','UNVERIFIED')},
            'regression_gate':review,'production_approval':'UNVERIFIED',
            'warning':'Known FAILs remain failures. A green regression check means no unreviewed delta, not production readiness.'}
    out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    economics=out.with_name(out.stem+'-economics.json');economics.write_text(json.dumps(sensitivity(),indent=2)+'\n')
    print(json.dumps({'summary':result['summary'],'regression_gate':review,'report':str(out)},indent=2))
    if a.check and any(review.values()):return 1
    return 0
if __name__=='__main__':sys.exit(main())
