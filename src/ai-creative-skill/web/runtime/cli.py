"""Entry point for an isolated host-neutral web preview helper, NOT installed in V2.4."""
import argparse,json,sys,pathlib,importlib.util
from .router import resolve

def main():
    p=argparse.ArgumentParser();sub=p.add_subparsers(dest='cmd',required=True)
    r=sub.add_parser('route');r.add_argument('request');r.add_argument('--intent');r.add_argument('--deep',action='store_true')
    a=sub.add_parser('audit');a.add_argument('site_dir');a.add_argument('--output',required=True);a.add_argument('--url')
    a.add_argument('--project-root',help='Root later passed to validate; QA evidence may live here outside the site')
    v=sub.add_parser('validate');v.add_argument('record');v.add_argument('--site-dir',required=True)
    h=sub.add_parser('preview');h.add_argument('operation',choices=['start','status','stop','restart']);h.add_argument('site_dir')
    args=p.parse_args()
    if args.cmd=='route':print(json.dumps(resolve(args.request,args.intent,args.deep).__dict__,ensure_ascii=False,indent=2))
    elif args.cmd=='audit':
        from . import qa
        print(json.dumps(qa.audit(args.site_dir,args.output,args.url,args.project_root),ensure_ascii=False,indent=2))
    elif args.cmd=='validate':
        from .validate import check
        errors=check(json.loads(pathlib.Path(args.record).read_text()),args.site_dir)
        print(json.dumps({'ok':not errors,'errors':errors},ensure_ascii=False,indent=2));sys.exit(bool(errors))
    elif args.cmd=='preview':
        from . import preview
        fn={'start':preview.start,'stop':preview.stop,'status':preview.status,'restart':lambda root:(preview.stop(root),preview.start(root))[1]}[args.operation]
        print(json.dumps(fn(args.site_dir),ensure_ascii=False,indent=2))
if __name__=='__main__':main()
