"""Field test of the PR #17 runtime: run web.runtime.qa.audit on frozen deliveries (coordinator tooling).
usage: python3 field_qa.py <dqb3_root> <label> [<label> ...]"""
import functools,http.server,json,sys,threading,pathlib
ROOT=pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0,str(ROOT/'skill-A/src/ai-creative-skill/web'))
from runtime import qa
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a):pass
for label in sys.argv[2:]:
    site=ROOT/'frozen'/label;out=ROOT/'qa-field'/label
    srv=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Q,directory=str(site)))
    threading.Thread(target=srv.serve_forever,daemon=True).start()
    try:rep=qa.audit(site,out,f'http://127.0.0.1:{srv.server_address[1]}/',project_root=ROOT)
    finally:srv.shutdown();srv.server_close()
    res={c['check_id']:c['result'] for c in rep['checks']}
    bad={c['check_id']:c.get('reason') for c in rep['checks'] if c['result']=='FAIL'}
    print(label,json.dumps(res),'FAIL:',bad)
    leak=[str(p) for p in out.rglob('*.json') if str(ROOT) in p.read_text() or '/home/' in p.read_text()]
    print('  absolute paths in evidence:',leak or 'none')
