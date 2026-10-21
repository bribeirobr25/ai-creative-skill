"""Bounded local preview lifecycle. No public deployment, no killing unrelated processes."""
import argparse,hmac,http.server,io,json,os,pathlib,signal,socket,stat,subprocess,sys,time,urllib.request,uuid
from urllib.parse import urlsplit, unquote, quote

META='.web-preview-owner.json'
_HANDLES={}

def owned_process(pid, token):
    if not pid or not token:return False
    try:
        out=subprocess.check_output(['ps','-p',str(pid),'-o','args='],text=True,stderr=subprocess.DEVNULL).strip()
        return ('preview.py serve' in out or 'preview.py' in out and 'serve' in out) and token in out
    except (OSError,subprocess.CalledProcessError):return False

def request_parts(target):
    """Decode once for both validation and serving; reject ambiguous encodings."""
    parsed=urlsplit(target)
    if parsed.scheme or parsed.netloc:raise ValueError('Absolute request target')
    decoded=unquote(parsed.path,errors='strict')
    if '%' in decoded or '\\' in decoded or any(ord(c)<32 or ord(c)==127 for c in decoded):
        raise ValueError('Ambiguous or invalid path')
    parts=tuple(p for p in decoded.split('/') if p)
    if any(p.startswith('.') for p in parts):raise ValueError('Hidden or dot path')
    return parts,decoded.endswith('/')


def open_bounded(root_fd,parts):
    """Walk directory descriptors, never symlinks; avoid check/open races."""
    fd=os.dup(root_fd)
    try:
        for part in parts:
            child=os.open(part,os.O_RDONLY|os.O_NOFOLLOW|os.O_NONBLOCK,dir_fd=fd)
            os.close(fd);fd=child
        return fd
    except Exception:
        os.close(fd);raise


def server(root,port,token):
    root=pathlib.Path(root).resolve()
    # The preview lifecycle already requires Unix. Fail explicitly on unsupported hosts.
    if not hasattr(os,'O_NOFOLLOW') or os.open not in os.supports_dir_fd:
        raise RuntimeError('Bounded preview requires no-follow directory descriptors')
    root_fd=os.open(root,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW)
    class H(http.server.SimpleHTTPRequestHandler):
        def __init__(self,*a,**k):super().__init__(*a,directory=str(root),**k)
        def send_head(self):
            try:parts,trailing=request_parts(self.path)
            except (ValueError,UnicodeError):
                self.send_error(403,'Path outside preview scope');return None
            # GET and HEAD share this path. Encoded aliases cannot bypass authentication
            # or fall through to a file with the reserved health endpoint's name.
            if parts==('__web_preview_health__',):
                supplied=self.headers.get('X-Web-Preview-Token','').encode('utf-8')
                if not hmac.compare_digest(supplied,token.encode('ascii')):
                    self.send_error(404);return None
                payload=json.dumps({'token':token,'root':str(root),'pid':os.getpid()}).encode()
                self.send_response(200);self.send_header('Content-Type','application/json')
                self.send_header('Content-Length',str(len(payload)));self.send_header('Cache-Control','no-store')
                self.end_headers();return io.BytesIO(payload)
            fd=None
            try:
                fd=open_bounded(root_fd,parts)
                if stat.S_ISDIR(os.fstat(fd).st_mode):
                    if not trailing:
                        self.send_response(301)
                        self.send_header('Location','/'+ '/'.join(quote(p,safe='') for p in parts)+'/')
                        self.send_header('Content-Length','0');self.end_headers();return None
                    index_fd=None
                    for index in ('index.html','index.htm'):
                        try:index_fd=os.open(index,os.O_RDONLY|os.O_NOFOLLOW|os.O_NONBLOCK,dir_fd=fd);break
                        except FileNotFoundError:continue
                    if index_fd is None:
                        self.send_error(403,'Directory listing disabled');return None
                    os.close(fd);fd=index_fd;parts=parts+(index,)
                info=os.fstat(fd)
                if not stat.S_ISREG(info.st_mode):
                    self.send_error(403,'Only regular preview files are served');return None
                file=os.fdopen(fd,'rb');fd=None
                self.send_response(200);self.send_header('Content-Type',self.guess_type(parts[-1]))
                self.send_header('Content-Length',str(info.st_size));self.send_header('X-Content-Type-Options','nosniff')
                self.end_headers();return file
            except FileNotFoundError:self.send_error(404)
            except OSError:self.send_error(403,'Path outside preview scope')
            finally:
                if fd is not None:os.close(fd)
            return None
        def log_message(self,*a):pass
    try:
        with http.server.ThreadingHTTPServer(('127.0.0.1',port),H) as httpd:httpd.serve_forever()
    finally:os.close(root_fd)

def health(meta):
    try:
        request=urllib.request.Request(meta['url']+'__web_preview_health__',headers={'X-Web-Preview-Token':meta['token']})
        with urllib.request.urlopen(request,timeout=1.0) as r:
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
