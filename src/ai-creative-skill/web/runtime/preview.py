"""Bounded local preview lifecycle. No public deployment, no killing unrelated processes."""
import argparse,functools,hashlib,http.server,json,os,pathlib,signal,socket,subprocess,sys,time,urllib.request,uuid

META='.web-preview-owner.json'
_HANDLES={}

def owned_process(pid, token):
    if not pid or not token:return False
    try:
        out=subprocess.check_output(['ps','-p',str(pid),'-o','args='],text=True,stderr=subprocess.DEVNULL).strip()
        return ('preview.py serve' in out or 'preview.py' in out and 'serve' in out) and token in out
    except (OSError,subprocess.CalledProcessError):return False

def server(root,port,token):
    root=pathlib.Path(root).resolve()
    class H(http.server.SimpleHTTPRequestHandler):
        def __init__(self,*a,**k):super().__init__(*a,directory=str(root),**k)
        def do_GET(self):
            if self.path=='/__web_preview_health__':
                payload=json.dumps({'token':token,'root':str(root),'pid':os.getpid()}).encode()
                self.send_response(200);self.send_header('Content-Type','application/json');self.send_header('Content-Length',str(len(payload)));self.end_headers();self.wfile.write(payload)
            elif any(part.startswith('.') for part in self.path.split('?',1)[0].split('/') if part):
                self.send_error(403,'Hidden files are not served')
            else:super().do_GET()
        def log_message(self,*a):pass
    with http.server.ThreadingHTTPServer(('127.0.0.1',port),H) as httpd:httpd.serve_forever()

def health(meta):
    try:
        with urllib.request.urlopen(meta['url']+'__web_preview_health__',timeout=1.0) as r:
            obj=json.loads(r.read());return r.status==200 and obj.get('token')==meta['token'] and obj.get('root')==meta['root']
    except Exception:return False

def metadata(root):
    f=pathlib.Path(root).resolve()/META
    return json.loads(f.read_text()) if f.exists() else None

def start(root):
    root=pathlib.Path(root).resolve()
    if not (root/'index.html').is_file():raise RuntimeError('index.html missing')
    old=metadata(root)
    if old and health(old) and owned_process(old.get('pid'),old.get('token')):return {'state':'REUSED_RUNNING','url':old['url'],'pid':old['pid']}
    if old and health(old):raise RuntimeError('Existing healthy server lacks verifiable ownership; refusing to replace')
    sock=socket.socket();sock.bind(('127.0.0.1',0));port=sock.getsockname()[1];sock.close()
    token=uuid.uuid4().hex
    log=open(root/'.web-preview.log','ab')
    proc=subprocess.Popen([sys.executable,str(pathlib.Path(__file__).resolve()),'serve','--root',str(root),'--port',str(port),'--token',token],stdin=subprocess.DEVNULL,stdout=log,stderr=log,start_new_session=True,close_fds=True);log.close()
    _HANDLES[proc.pid]=proc
    result={'token':token,'url':f'http://127.0.0.1:{port}/','root':str(root),'pid':proc.pid,'scope':'LOCAL_LOOPBACK_ONLY','persistence':'NOT_GUARANTEED_ACROSS_HOST_SESSION','started_at':time.time()}
    (root/META).write_text(json.dumps(result,indent=2))
    for _ in range(50):
        if health(result):return {'state':'STARTED','url':result['url'],'pid':proc.pid}
        if proc.poll() is not None:break
        time.sleep(.1)
    if owned_process(proc.pid,token):os.kill(proc.pid,signal.SIGTERM)
    raise RuntimeError('Preview failed healthcheck')

def status(root):
    m=metadata(root)
    if not m:return {'state':'NOT_STARTED'}
    return {'state':'HEALTHY_OWNED' if health(m) and owned_process(m.get('pid'),m.get('token')) else 'STALE_OR_UNVERIFIED','url':m['url'],'pid':m['pid']}

def stop(root):
    m=metadata(root)
    if not m:return {'state':'NOT_RUNNING'}
    if not owned_process(m.get('pid'),m.get('token')):return {'state':'UNKNOWN_NOT_OWNED_NO_SIGNAL'}
    os.kill(m['pid'],signal.SIGTERM)
    if m['pid'] in _HANDLES:
        try:_HANDLES.pop(m['pid']).wait(timeout=2.0)
        except subprocess.TimeoutExpired:pass
    for _ in range(20):
        if not owned_process(m['pid'],m['token']):return {'state':'STOPPED'}
        time.sleep(.1)
    return {'state':'STOP_REQUESTED_UNCONFIRMED'}

def cli():
    a=argparse.ArgumentParser();sub=a.add_subparsers(dest='op',required=True)
    for name in ['start','status','restart','stop','serve']:
        q=sub.add_parser(name);q.add_argument('--root',required=True)
        if name=='serve':q.add_argument('--port',type=int,required=True);q.add_argument('--token',required=True)
    o=a.parse_args()
    if o.op=='serve':server(o.root,o.port,o.token);return
    if o.op=='start':r=start(o.root)
    elif o.op=='status':r=status(o.root)
    elif o.op=='stop':r=stop(o.root)
    else:
        s=status(o.root)
        if s['state']=='HEALTHY_OWNED':stop(o.root)
        elif s['state']=='STALE_OR_UNVERIFIED' and health(metadata(o.root)):raise RuntimeError('Not owned; no restart')
        r=start(o.root)
    print(json.dumps(r,ensure_ascii=False))
if __name__=='__main__':cli()
