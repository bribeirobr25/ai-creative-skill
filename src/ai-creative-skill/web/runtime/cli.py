"""Entry point for an isolated host-neutral web preview helper, NOT installed in V2.4."""
import argparse,json,sys,pathlib,importlib.util
from .router import resolve

def main():
    p=argparse.ArgumentParser();sub=p.add_subparsers(dest='cmd',required=True)
    r=sub.add_parser('route');r.add_argument('request');r.add_argument('--intent');r.add_argument('--deep',action='store_true')
    a=sub.add_parser('audit');a.add_argument('site_dir');a.add_argument('--output',required=True);a.add_argument('--url')
    a.add_argument('--static-only',action='store_true',help='Skip the browser, even with --url; otherwise without --url the browser opens index.html via file://')
    a.add_argument('--project-root',help='Root later passed to validate --project-root; QA evidence may live here outside the site')
    v=sub.add_parser('validate');v.add_argument('record');v.add_argument('--site-dir',required=True)
    v.add_argument('--project-root',help='Use when audit ran with --project-root; defaults to --site-dir')
    d=sub.add_parser('record',help='Write a delivery record draft from a QA run; fill every TODO, then validate')
    d.add_argument('site_dir');d.add_argument('--qa',required=True,help='qa_matrix.json written by audit');d.add_argument('--output',required=True)
    d.add_argument('--project-root');d.add_argument('--project')
    h=sub.add_parser('preview');h.add_argument('operation',choices=['start','status','stop','restart']);h.add_argument('site_dir')
    args=p.parse_args()
    if args.cmd=='route':print(json.dumps(resolve(args.request,args.intent,args.deep).__dict__,ensure_ascii=False,indent=2))
    elif args.cmd=='audit':
        from . import qa
        print(json.dumps(qa.audit(args.site_dir,args.output,args.url,args.project_root,browser=not args.static_only),ensure_ascii=False,indent=2))
    elif args.cmd=='validate':
        from .validate import check
        errors=check(json.loads(pathlib.Path(args.record).read_text()),args.project_root or args.site_dir)
        print(json.dumps({'ok':not errors,'errors':errors},ensure_ascii=False,indent=2));sys.exit(bool(errors))
    elif args.cmd=='record':
        from . import qa
        rec=qa.draft_record(args.site_dir,args.qa,args.project_root,args.project)
        pathlib.Path(args.output).write_text(json.dumps(rec,ensure_ascii=False,indent=2))
        from .validate import todo_paths
        print(json.dumps({'written':pathlib.Path(args.output).name,'todo_fields':len(todo_paths(rec))},indent=2))
    elif args.cmd=='preview':
        from . import preview
        fn={'start':preview.start,'stop':preview.stop,'status':preview.status,'restart':lambda root:(preview.stop(root),preview.start(root))[1]}[args.operation]
        print(json.dumps(fn(args.site_dir),ensure_ascii=False,indent=2))
if __name__=='__main__':main()
