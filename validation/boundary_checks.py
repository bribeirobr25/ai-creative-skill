"""Adjacent positive/negative controls for the six remediation families. Synthetic only."""
import copy,http.client,json,os,shutil,tempfile
from pathlib import Path
from urllib.parse import urlsplit

def non_http(h):
    rows=[]
    def add(id,expected,actual,ok):rows.append(h.outcome('BOUNDARY-'+id,expected,actual,ok))
    routes=[
      ('research-negated','não publique o site; pesquise referências','WEB_RESEARCH_ONLY'),
      ('research-en',"research website examples; don't deploy",'WEB_RESEARCH_ONLY'),
      ('preview-en',"build a website; don't publish",'WEB_PREVIEW'),
      ('preview-accent','CRIE UM SITE; NAO PUBLIQUE','WEB_PREVIEW'),
      ('edit-negated','mude apenas o hero; não publique o site','WEB_EDIT'),
      ('negative-only','não publique o site','AMBIGUOUS'),
      ('negative-en-only',"don't deploy the website",'AMBIGUOUS'),
      ('not-research','não pesquise; publique o site','WEB_PUBLICATION'),
      ('mixed','pesquise e publique o site','AMBIGUOUS'),
      ('contradiction','não publique o site; publique o site','AMBIGUOUS'),
      ('research-build-how','research how to build a website','WEB_RESEARCH_ONLY'),
      ('research-and-build','research the website and build a website','AMBIGUOUS'),
      ('research-how','pesquise como publicar um site','WEB_RESEARCH_ONLY'),
      ('advertising-word','pesquise publicidade para sites','WEB_RESEARCH_ONLY'),
      ('publish-en','publish the website','WEB_PUBLICATION'),
      ('publish-pt','publique o site','WEB_PUBLICATION'),
      ('unknown','seria legal ter algo bonito','AMBIGUOUS')]
    for name,text,expected in routes:
        try:actual=h.router.resolve(text).route
        except ValueError:actual='AMBIGUOUS'
        add('route-'+name,expected,actual,actual==expected)
    try:h.router.resolve('não publique o site',intent='WEB_PUBLICATION');actual='ACCEPTED'
    except ValueError:actual='AMBIGUOUS'
    add('route-explicit-conflict','AMBIGUOUS',actual,actual=='AMBIGUOUS')
    typ='PROJECT_NEXT_ACTION';required=json.loads(h.shape.CATALOG.read_text())['types'][typ]['required']
    for name,value,expected in [('zero',0,'PASS_STRUCTURAL'),('false',False,'PASS_STRUCTURAL'),('text','0','PASS_STRUCTURAL'),('unicode-space','\u2003\u00a0\t','FAIL_STRUCTURAL'),('empty-list',[],'FAIL_STRUCTURAL'),('empty-object',{},'FAIL_STRUCTURAL')]:
        actual=h.shape.inspect(typ,{key:value for key in required})
        add('shape-'+name,expected,actual['result'],actual['result']==expected and actual['semantic_verified'] is False)
    with tempfile.TemporaryDirectory() as td:
        base=Path(td);root,record=h.site_fixture(base)
        asset=root/'asset.txt';asset.write_text('SYNTHETIC_ASSET')
        evidence=root/'license-review.txt';evidence.write_text('FICTIONAL review fixture, not a legal license. Conditions fulfilled for the stated use.')
        good={'path':'asset.txt','origin':'synthetic','approval':'APPROVED_FOR_THIS_USE','rights':'RESTRICTED','use_scope':'commercial_publication','publication_clearance':{
          'allowed_uses':['commercial_publication'],'conditions_status':'SATISFIED','evidence_ref':'license-review.txt','evidence_sha256':h.digest(evidence),'asset_sha256':h.digest(asset),'reviewed_by':'Fictional reviewer'}}
        cases=[('restricted-permitted',lambda r,a:None,True),
          ('cleared-permitted',lambda r,a:a.update(rights='CLEARED'),True),
          ('noncommercial-permitted',lambda r,a:(a.update(use_scope='public_website'),a['publication_clearance'].update(allowed_uses=['public_website'])),True),
          ('legacy-version-new-field',lambda r,a:r.update(schema_version='0.2.0'),False),
          ('no-review',lambda r,a:a.pop('publication_clearance'),False),
          ('not-approved',lambda r,a:a.update(approval='PROVISIONAL'),False),
          ('unknown-rights',lambda r,a:a.update(rights='UNKNOWN'),False),
          ('wrong-purpose',lambda r,a:a['publication_clearance'].update(allowed_uses=['public_website']),False),
          ('private-scope',lambda r,a:a.update(use_scope='private_preview_only'),False),
          ('pending-conditions',lambda r,a:a['publication_clearance'].update(conditions_status='PENDING'),False),
          ('restricted-na',lambda r,a:a['publication_clearance'].update(conditions_status='NOT_APPLICABLE'),False),
          ('missing-evidence',lambda r,a:a['publication_clearance'].update(evidence_ref='missing.txt'),False),
          ('outside-evidence',lambda r,a:a['publication_clearance'].update(evidence_ref='../license-review.txt'),False),
          ('remote-evidence',lambda r,a:a['publication_clearance'].update(evidence_ref='https://example.invalid/license'),False),
          ('stale-evidence',lambda r,a:a['publication_clearance'].update(evidence_sha256='0'*64),False),
          ('stale-asset',lambda r,a:a['publication_clearance'].update(asset_sha256='0'*64),False),
          ('blank-reviewer',lambda r,a:a['publication_clearance'].update(reviewed_by='  '),False),
          ('preview-legacy',lambda r,a:(r.update(route='WEB_PREVIEW',schema_version='0.2.0'),a.pop('publication_clearance'),a.update(rights='UNKNOWN',approval='PROVISIONAL',use_scope='private_preview_only')),True),
          ('state-route-bypass',lambda r,a:(r.update(route='WEB_PREVIEW',state='PUBLICATION_PREFLIGHT'),a.pop('publication_clearance')),False)]
        for name,change,allowed in cases:
            r=copy.deepcopy(record);a=copy.deepcopy(good);r['route']='WEB_PUBLICATION';r['schema_version']='0.2.1-candidate';r['execution']['public_deploy_authorized']=True
            change(r,a);r['WEB_ASSET_PLAN']['assets_used']=[a];errors=h.validate.check(r,root)
            codes=sorted({e['code'] for e in errors});add('rights-'+name,'accepted preflight' if allowed else 'RIGHTS_GATE or SCHEMA',codes,not codes if allowed else bool({'RIGHTS_GATE','SCHEMA'}&set(codes)))
        # Dependency graph positive and negative controls; all revise the authorized hero.
        (root/'app.js').write_text('import "./nested.js";')
        (root/'nested.js').write_text('const label="Alder";')
        (root/'deep.css').write_text('body{color:black}')
        (root/'theme').write_text('@import "deeper.css";')
        (root/'deeper.css').write_text('h1{color:black}')
        (root/'styles.css').write_text('@import "deep.css"; @import url(theme); .hero{background:url("texture.png")}')
        (root/'texture.png').write_bytes(b'synthetic texture bytes')
        (root/'index.html').write_text((root/'index.html').read_text().replace('</body>','<script src="app.js?v=1"></script></body>'))
        cases=[('protected-and-css',lambda p:((p/'index.html').write_text((p/'index.html').read_text().replace('No commercial claims or submissions.','Wrong claim')),(p/'deep.css').write_text('body{color:red}')),'FAIL',True),
          ('protected-removed',lambda p:(p/'index.html').write_text((p/'index.html').read_text().replace('id="facts"','id="removed"')),'FAIL',True),
          ('new-script',lambda p:((p/'new.js').write_text('const v=1;'),(p/'index.html').write_text((p/'index.html').read_text().replace('</body>','<script src="new.js"></script></body>'))),'PARTIAL',True),
          ('new-style',lambda p:((p/'new.css').write_text('body{color:blue}'),(p/'index.html').write_text((p/'index.html').read_text().replace('</body>','<link rel="stylesheet" href="new.css"></body>'))),'PARTIAL',True),
          ('nested-js',lambda p:(p/'nested.js').write_text('const label="Changed";'),'PARTIAL',True),
          ('extensionless-import',lambda p:(p/'deeper.css').write_text('h1{color:red}'),'PARTIAL',True),
          ('outside-region-ui',lambda p:(p/'index.html').write_text((p/'index.html').read_text().replace('<body>','<body hidden>')),'PARTIAL',True),
          ('nested-css',lambda p:(p/'deep.css').write_text('body{color:purple}'),'PARTIAL',True),
          ('css-asset',lambda p:(p/'texture.png').write_bytes(b'changed synthetic texture'),'PARTIAL',True),
          ('query-version',lambda p:(p/'index.html').write_text((p/'index.html').read_text().replace('?v=1','?v=2')),'PARTIAL',True),
          ('inline-js',lambda p:(p/'index.html').write_text((p/'index.html').read_text().replace('</body>','<script>document.body.hidden=true</script></body>')),'PARTIAL',True),
          ('script-attribute',lambda p:(p/'index.html').write_text((p/'index.html').read_text().replace('<script src=','<script async src=')),'PARTIAL',True),
          ('removed-dependency',lambda p:(p/'nested.js').unlink(),'PARTIAL',True),
          ('unreferenced-file',lambda p:(p/'unreferenced.js').write_text('unused'),'SOURCE_PRESERVATION_PASS',False),
          ('unused-css',lambda p:(p/'unused.css').write_text('unused'),'SOURCE_PRESERVATION_PASS',False),
          ('hero-only',lambda p:None,'SOURCE_PRESERVATION_PASS',False),
          ('dynamic-import',lambda p:(p/'nested.js').write_text('import(location.hash.slice(1));'),'PARTIAL',True)]
        for name,change,status,retest in cases:
            after=base/name;shutil.copytree(root,after)
            (after/'index.html').write_text((after/'index.html').read_text().replace('Alder Studio — fictional workshop','Updated fictional hero'))
            change(after);actual=h.revision.compare(root,after,['facts'],['hero'])
            add('revision-'+name,{'status':status,'browser_retest_required':retest},actual,actual['status']==status and actual['browser_retest_required']==retest)
    return rows


def http_checks(h):
    rows=[]
    with tempfile.TemporaryDirectory() as td:
        base=Path(td);root,_=h.site_fixture(base)
        (root/'app.js').write_text('const synthetic=true;')
        (root/'asset one.txt').write_text('LEGITIMATE_SYNTHETIC')
        (root/'.secret').write_text('SYNTHETIC_HIDDEN')
        (root/'.hidden').mkdir();(root/'.hidden'/'plain.txt').write_text('SYNTHETIC_HIDDEN_DIRECTORY')
        (root/'nested').mkdir();(root/'nested'/'index.html').write_text('LEGITIMATE_DIRECTORY_INDEX')
        (root/'listing').mkdir();(root/'listing'/'.secret').write_text('SYNTHETIC_LISTING_HIDDEN')
        outside=base/'outside.txt';outside.write_text('SYNTHETIC_OUTSIDE')
        (root/'linked.txt').symlink_to(outside);(root/'linked-dir').symlink_to(base,target_is_directory=True)
        (root/'internal-link.txt').symlink_to(root/'asset one.txt')
        (root/'index-link').mkdir();(root/'index-link'/'index.html').symlink_to(outside)
        os.mkfifo(root/'synthetic.fifo')
        (root/'__web_preview_health__').write_text('HEALTH_SHADOW_FILE')
        server=h.preview.start(root);url=urlsplit(server['url']);meta=h.preview.metadata(root)
        def request(path,method='GET',token=None):
            connection=http.client.HTTPConnection(url.hostname,url.port,timeout=3)
            headers={} if token is None else {'X-Web-Preview-Token':token}
            try:
                connection.request(method,path,headers=headers)
                response=connection.getresponse();return response.status,response.read(),dict(response.getheaders())
            finally:connection.close()
        try:
            denied=['/.secret','/%2esecret','/%252esecret','/%25252esecret','/.hidden/plain.txt','/%2ehidden/plain.txt','/nested/../.secret','/nested/%2e%2e/.secret','/nested/%252e%252e/.secret','/linked.txt','/linked-dir/outside.txt','/internal-link.txt','/index-link/','/listing/','/%00x','/%5c..%5coutside.txt','/%FF','/%25252525252525252esecret','/synthetic.fifo']
            for method in ('GET','HEAD'):
                for i,path in enumerate(denied):
                    status,body,headers=request(path,method)
                    rows.append(h.outcome(f'BOUNDARY-http-deny-{method}-{i}','403 or 404 with no synthetic secret',{'path':path,'status':status,'secret_returned':b'SYNTHETIC_' in body},status in (403,404) and b'SYNTHETIC_' not in body and (method!='HEAD' or body==b'')))
                for i,path in enumerate(['/','/index.html','/styles.css','/app.js','/asset%20one.txt','/nested/','/styles.css?v=1']):
                    status,body,headers=request(path,method)
                    rows.append(h.outcome(f'BOUNDARY-http-allow-{method}-{i}','200 and correct body/length',{'path':path,'status':status},status==200 and int(headers['Content-Length'])>0 and (bool(body) if method=='GET' else body==b'')))
                for i,path in enumerate(['/__web_preview_health__','/%5f_web_preview_health__','/__web_preview_health__?probe=1','/__web_preview_health__/']):
                    for label,token in [('absent',None),('wrong','wrong'),('non-ascii','é')]:
                        status,body,headers=request(path,method,token)
                        rows.append(h.outcome(f'BOUNDARY-health-deny-{method}-{i}-{label}','404; no ownership metadata or shadow file',status,status==404 and meta['token'].encode() not in body and b'HEALTH_SHADOW' not in body))
                    status,body,headers=request(path,method,meta['token'])
                    valid=status==200 and headers.get('Cache-Control')=='no-store'
                    if method=='GET':valid=valid and json.loads(body)['token']==meta['token'] and json.loads(body)['root']==str(root.resolve())
                    else:valid=valid and body==b''
                    rows.append(h.outcome(f'BOUNDARY-health-owner-{method}-{i}','authenticated response',{'status':status,'valid':valid},valid))
            status,body,headers=request('/nested')
            rows.append(h.outcome('BOUNDARY-http-directory-redirect','local directory redirect',{'status':status,'location':headers.get('Location')},status==301 and headers.get('Location')=='/nested/'))
            rows.append(h.outcome('BOUNDARY-health-lifecycle','owner health and reuse work',h.preview.status(root)['state'],h.preview.health(meta) and h.preview.start(root)['state']=='REUSED_RUNNING'))
        finally:h.preview.stop(root)
    return rows


def mutations(h,include_http=False):
    """Reintroduce each boundary defect in disposable copies; reuse executed probes."""
    from types import SimpleNamespace
    specs=[
      ('rights-proof','web/runtime/validate.py','if not compatible or not bound:','if not compatible:','validate','BOUNDARY-rights-missing-evidence'),
      ('preserve-verdict','web/runtime/revision.py',"'status':'FAIL' if preserved_diffs or changed_missing else", "'status':'FAIL' if False else",'revision','BOUNDARY-revision-protected-and-css'),
      ('dependencies','web/runtime/revision.py',"globals_changed=[f for f in sorted(set(b['global_files'])|set(a['global_files'])) if b['global_files'].get(f)!=a['global_files'].get(f)]",'globals_changed=[]','revision','BOUNDARY-revision-nested-js'),
      ('negation','web/runtime/router.py','negative|=denied;positive|=not denied','negative=False;positive=True','router','BOUNDARY-route-research-negated'),
      ('blank-fields','scripts/validate_deliverable.py',"(isinstance(item[k],str) and not item[k].strip())","item[k]==''",'shape','BOUNDARY-shape-unicode-space')]
    if include_http:
        specs.extend([
          ('nofollow','web/runtime/preview.py','child=os.open(part,os.O_RDONLY|os.O_NOFOLLOW|os.O_NONBLOCK,dir_fd=fd)','child=os.open(part,os.O_RDONLY|os.O_NONBLOCK,dir_fd=fd)','preview','BOUNDARY-http-deny-GET-9'),
          ('health-auth','web/runtime/preview.py',"if not hmac.compare_digest(supplied,token.encode('ascii')):",'if False:','preview','BOUNDARY-health-deny-GET-0-absent')])
    rows=[]
    controls={r['id']:r for r in non_http(h)}
    if include_http:controls.update({r['id']:r for r in http_checks(h)})
    with tempfile.TemporaryDirectory() as td:
        for name,relative,old,new,attribute,oracle in specs:
            target=Path(td)/name/'skill';shutil.copytree(h.SKILL,target,ignore=shutil.ignore_patterns('__pycache__'))
            path=target/relative;text=path.read_text()
            if text.count(old)!=1:raise AssertionError('Boundary mutation anchor drift: '+name)
            path.write_text(text.replace(old,new));mutant=h.module_from(path,'boundary_mutant_'+name.replace('-','_'))
            context=SimpleNamespace(**{key:getattr(h,key) for key in ('SKILL','router','shape','validate','revision','preview','site_fixture','digest','outcome')})
            setattr(context,attribute,mutant)
            mutated={r['id']:r for r in (http_checks(context) if attribute=='preview' else non_http(context))}
            detected=controls[oracle]['outcome']=='PASS' and mutated[oracle]['outcome']=='FAIL'
            rows.append(h.outcome('BOUNDARY-MUTATION-'+name,'baseline passes, specified mutant fails',{'baseline':controls[oracle]['outcome'],'mutant':mutated[oracle]['outcome'],'oracle':oracle},detected))
    return rows
