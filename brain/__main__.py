"""python3 -m brain {status,validate} [--verify-authority] [--offline]"""
import argparse
import sys

from brain import core


def main(argv=None):
    p = argparse.ArgumentParser(prog='python3 -m brain', description='Project Brain (brain/README.md)')
    sub = p.add_subparsers(dest='cmd', required=True)
    v = sub.add_parser('validate', help='check records against brain/CONTRACT.md')
    v.add_argument('--verify-authority', action='store_true', help='also check on GitHub that each decision PR was merged by the owner')
    v.add_argument('--records', help='validate another records folder, e.g. the private half (evidence paths resolve from its parent)')
    v.add_argument('--allow-private', action='store_true', help='accept privacy_class "private" (only for a folder outside this repository)')
    sub.add_parser('lint-docs', help='fail if a living doc calls a merged PR open or proposed (needs GitHub)')
    s = sub.add_parser('status', help='print the current state, derived on read')
    s.add_argument('--offline', action='store_true', help='skip GitHub')
    a = p.parse_args(argv)
    rows = core.load(a.records) if getattr(a, 'records', None) else core.load()
    if a.cmd == 'lint-docs':
        merged = core.merged_prs()
        if merged is None:
            print('FAIL cannot reach GitHub to list merged PRs')
            return 1
        stale = core.stale_doc_lines(merged)
        for x in stale:
            print('FAIL ' + x)
        print('%s: %d stale line(s) in %d living docs' % ('PASS' if not stale else 'FAIL', len(stale), len(core.LIVING_DOCS)))
        return 1 if stale else 0
    if a.cmd == 'status':
        sys.stdout.write(core.status(rows, online=not a.offline))
        return 0
    if a.allow_private and (not a.records or core.Path(a.records).resolve().is_relative_to(core.ROOT)):
        print('FAIL --allow-private needs --records outside this repository')
        return 1
    root = core.Path(a.records).resolve().parent if a.records else core.ROOT
    errs = core.problems(rows, root, a.allow_private) + (core.verify_authority(rows) if a.verify_authority else [])
    for e in errs:
        print('FAIL ' + e)
    print('%s: %d record(s), %d problem(s)' % ('PASS' if not errs else 'FAIL', len(rows), len(errs)))
    return 1 if errs else 0


if __name__ == '__main__':
    sys.exit(main())
