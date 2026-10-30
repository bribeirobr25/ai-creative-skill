"""python3 -m brain {status,validate} [--verify-authority] [--offline]"""
import argparse
import sys

from brain import core


def main(argv=None):
    p = argparse.ArgumentParser(prog='python3 -m brain', description='Project Brain (brain/README.md)')
    sub = p.add_subparsers(dest='cmd', required=True)
    v = sub.add_parser('validate', help='check records against brain/CONTRACT.md')
    v.add_argument('--verify-authority', action='store_true', help='also check on GitHub that each decision PR was merged by the owner')
    s = sub.add_parser('status', help='print the current state, derived on read')
    s.add_argument('--offline', action='store_true', help='skip GitHub')
    a = p.parse_args(argv)
    rows = core.load()
    if a.cmd == 'status':
        sys.stdout.write(core.status(rows, online=not a.offline))
        return 0
    errs = core.problems(rows) + (core.verify_authority(rows) if a.verify_authority else [])
    for e in errs:
        print('FAIL ' + e)
    print('%s: %d record(s), %d problem(s)' % ('PASS' if not errs else 'FAIL', len(rows), len(errs)))
    return 1 if errs else 0


if __name__ == '__main__':
    sys.exit(main())
