"""Project Brain: record validation and status derived on read (contract: brain/CONTRACT.md)."""
import datetime
import json
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECORDS = ROOT / 'brain' / 'records'
GATES = ROOT / 'brain' / 'gates.json'
BENCHMARK_LOG = ROOT / 'docs' / 'benchmarks' / 'benchmark-log.md'
KINDS = {'OBSERVED', 'CHANGE_REQUESTED', 'DECISION_RECORDED'}
REQUIRED = ('id', 'kind', 'subject', 'statement', 'evidence_refs', 'occurred_at', 'recorded_at', 'privacy_class')
DATE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
AUTHORITY = re.compile(r'^pr:#(\d+)$')
REF = re.compile(r'^(pr:#\d+|issue:#\d+|commit:[0-9a-f]{7,40}|[\w./-]+(#[\w-]+)?)$')


def load(records=RECORDS):
    """Return [(file, line_no, record)]; a malformed line is reported, never skipped."""
    out = []
    for path in sorted(Path(records).glob('*.jsonl')):
        for n, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            if line.strip():
                try:
                    out.append((path.name, n, json.loads(line)))
                except json.JSONDecodeError as e:
                    out.append((path.name, n, {'_error': str(e)}))
    return out


def problems(rows, root=ROOT):
    errs, ids = [], {}
    for f, n, r in rows:
        where = '%s:%d' % (f, n)
        if '_error' in r:
            errs.append('%s: not valid JSON (%s)' % (where, r['_error']))
            continue
        for k in REQUIRED:
            if k not in r or r[k] in ('', None):
                errs.append('%s: missing %s' % (where, k))
        if r.get('id') in ids:
            errs.append('%s: duplicate id %s (first at %s)' % (where, r['id'], ids[r['id']]))
        ids.setdefault(r.get('id'), where)
        if r.get('kind') not in KINDS:
            errs.append('%s: kind must be one of %s' % (where, ', '.join(sorted(KINDS))))
        if r.get('kind') == 'DECISION_RECORDED' and not AUTHORITY.match(str(r.get('authority_ref', ''))):
            errs.append('%s: a decision needs authority_ref "pr:#N" (the PR whose merge was the owner act)' % where)
        if r.get('privacy_class') != 'public':
            errs.append('%s: privacy_class must be "public"; private records belong outside this repository' % where)
        for k in ('occurred_at', 'recorded_at', 'review_by'):
            if k in r and not DATE.match(str(r[k])):
                errs.append('%s: %s must be YYYY-MM-DD' % (where, k))
        if not isinstance(r.get('evidence_refs', []), list):
            errs.append('%s: evidence_refs must be a list' % where)
        else:
            for ref in r.get('evidence_refs', []):
                if not REF.match(str(ref)):
                    errs.append('%s: unrecognised evidence ref %r' % (where, ref))
                elif not ref.startswith(('pr:', 'issue:', 'commit:')) and not (root / ref.split('#')[0]).exists():
                    errs.append('%s: evidence path does not exist: %s' % (where, ref))
        if f == 'findings.jsonl' and not r.get('test_ref'):
            errs.append('%s: a finding needs test_ref (a test path, or "paper" until one exists)' % where)
    known = {r.get('id') for _, _, r in rows}
    for f, n, r in rows:
        if r.get('supersedes') and r['supersedes'] not in known:
            errs.append('%s:%d: supersedes unknown id %s' % (f, n, r['supersedes']))
    by_subject = {}
    for r in current(rows):
        if r.get('kind') == 'DECISION_RECORDED':
            by_subject.setdefault(r.get('subject'), []).append(r['id'])
    for s, rs in sorted(by_subject.items()):
        if len(rs) > 1:
            errs.append('contradiction: %d current decisions on subject %r (%s); supersede one' % (len(rs), s, ', '.join(rs)))
    return errs


def current(rows):
    gone = {r.get('supersedes') for _, _, r in rows if r.get('supersedes')}
    return [r for _, _, r in rows if '_error' not in r and r.get('id') not in gone]


def gh(*args):
    """Run gh and return parsed JSON, or None when gh is missing, offline or unauthenticated."""
    if not shutil.which('gh'):
        return None
    try:
        out = subprocess.run(['gh', *args], cwd=ROOT, capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.TimeoutExpired):
        return None
    if out.returncode:
        return None
    try:
        return json.loads(out.stdout)
    except json.JSONDecodeError:
        return None


def verify_authority(rows, fetch=None):
    """A decision counts only if its PR was merged by the repository owner."""
    fetch = fetch or (lambda n: gh('api', 'repos/{owner}/{repo}/pulls/%d' % n))
    errs, cache = [], {}
    for r in current(rows):
        m = AUTHORITY.match(str(r.get('authority_ref', '')))
        if r.get('kind') != 'DECISION_RECORDED' or not m:
            continue
        n = int(m.group(1))
        if n not in cache:
            cache[n] = fetch(n)
        pr = cache[n]
        if pr is None:
            errs.append('%s: cannot reach GitHub to verify pr:#%d' % (r['id'], n))
        elif not pr.get('merged'):
            errs.append('%s: pr:#%d is not merged, so the decision is not yet the owner\'s' % (r['id'], n))
        elif (pr.get('merged_by') or {}).get('login') != pr['base']['repo']['owner']['login']:
            errs.append('%s: pr:#%d was not merged by the repository owner' % (r['id'], n))
    return errs


def benchmark_checks(path=BENCHMARK_LOG):
    if not Path(path).exists():
        return []
    rows = []
    for line in Path(path).read_text(encoding='utf-8').splitlines():
        m = re.match(r'^\| (C\d+) \| (.*?) \| (.*?) \| (.*?) \|$', line)
        if m:
            rows.append({'id': m.group(1), 'check': m.group(2), 'status': m.group(4)})
    return rows


def status(rows, today=None, online=True):
    today = today or datetime.date.today().isoformat()
    cur = current(rows)
    L = ['# Project Brain status (derived %s; not committed)' % today, '']
    errs = problems(rows)
    if errs:
        L += ['**Records have %d problem(s); run `python3 -m brain validate`.**' % len(errs), '']
    L += ['## Current decisions', '']
    for r in sorted((r for r in cur if r.get('kind') == 'DECISION_RECORDED'), key=lambda r: r.get('subject', '')):
        L.append('- **%s** (%s, %s): %s' % (r['subject'], r['occurred_at'], r.get('authority_ref', '?'), r['statement']))
    obs = [r for r in cur if r.get('kind') != 'DECISION_RECORDED']
    if obs:
        L += ['', '## Observations and requests (not decisions)', '']
        L += ['- %s `%s`: %s%s' % (r['kind'].lower(), r['subject'], r['statement'],
                                   ' [scope: %s]' % r['scope'] if r.get('scope') else '') for r in obs]
    due = [r for r in cur if r.get('review_by') and r['review_by'] <= today]
    L += ['', '## Due for review', '']
    L += ['- %s (review_by %s)' % (r['id'], r['review_by']) for r in due] or ['- none']
    gates = json.loads(GATES.read_text(encoding='utf-8'))['gates'] if GATES.exists() else []
    L += ['', '## Gates', '']
    for g in gates:
        L.append('- %s %s: %s. Enforced by: %s' % ('[live]' if g['status'] == 'live' else '[PAPER]', g['id'], g['principle'], g['enforced_by']))
    checks = benchmark_checks()
    if checks:
        L += ['', '## Benchmark checks (docs/benchmarks/benchmark-log.md)', '']
        L += ['- %s: %s (%s)' % (c['id'], c['check'], c['status']) for c in checks]
    L += ['', '## Open on GitHub', '']
    prs = gh('pr', 'list', '--state', 'open', '--json', 'number,title') if online else None
    issues = gh('issue', 'list', '--state', 'open', '--json', 'number,title') if online else None
    if prs is None and issues is None:
        L.append('- GitHub not reachable (gh missing, offline or not signed in); open work not listed.')
    else:
        L += ['- PR #%d %s' % (p['number'], p['title']) for p in prs or []] or ['- no open PRs']
        L += ['- Issue #%d %s' % (i['number'], i['title']) for i in issues or []]
    return '\n'.join(L) + '\n'
