#!/usr/bin/env python3
"""Install the local pre-push publication check (finding S0-3; ADR-0003 §1: check before every public write).

    python3 security/install_hooks.py            # install .git/hooks/pre-push
    python3 security/install_hooks.py --check    # exit 0 if installed and current

The hook scans every commit about to be pushed with security/publication_guard.py and stops the push on BLOCK.
GitHub API or connector writes do not run local hooks; for those, the required CI check is the barrier.
An existing pre-push hook that this script did not write is never overwritten.
"""
import argparse
import os
import stat
import subprocess
import sys
from pathlib import Path

MARKER = '# ai-creative-skill publication guard hook v1'
HOOK = MARKER + r'''
# Installed by security/install_hooks.py. Reads "<local ref> <local sha> <remote ref> <remote sha>" lines from git.
set -u
top=$(git rev-parse --show-toplevel)
zero=0000000000000000000000000000000000000000
status=0
while read -r local_ref local_sha remote_ref remote_sha; do
  [ "$local_sha" = "$zero" ] && continue            # deleting a remote ref adds no content
  if [ "$remote_sha" = "$zero" ]; then
    base=$(git merge-base "$local_sha" origin/main 2>/dev/null || git rev-list --max-parents=0 "$local_sha" | tail -n 1)
  else
    base=$remote_sha
  fi
  [ "$base" = "$local_sha" ] && continue
  python3 "$top/security/publication_guard.py" --range "$base...$local_sha" --history-range "$base..$local_sha" || status=1
done
if [ "$status" -ne 0 ]; then
  echo "pre-push: publication guard found a BLOCK; push stopped. Fix it, or ask the owner before using --no-verify." >&2
fi
exit $status
'''


def hook_path(repo):
    out = subprocess.run(['git', 'rev-parse', '--git-path', 'hooks/pre-push'], cwd=repo, capture_output=True, text=True, check=True)
    return (Path(repo) / out.stdout.strip()).resolve()


def install(repo='.'):
    path = hook_path(repo)
    if path.exists() and MARKER not in path.read_text(errors='replace'):
        raise SystemExit('A different pre-push hook exists at %s; not overwriting it. Merge it by hand.' % path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('#!/bin/sh\n' + HOOK)
    path.chmod(path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    return path


def installed(repo='.'):
    path = hook_path(repo)
    return path.exists() and path.read_text(errors='replace') == '#!/bin/sh\n' + HOOK and os.access(path, os.X_OK)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args(argv)
    if a.check:
        ok = installed()
        print('pre-push hook: %s' % ('installed' if ok else 'NOT installed (run python3 security/install_hooks.py)'))
        return 0 if ok else 1
    print('installed: %s' % install())
    return 0


if __name__ == '__main__':
    sys.exit(main())
