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
FINDING_STATUS = {'OPEN', 'FIXED', 'ACCEPTED-RISK', 'UNKNOWN', 'WITHDRAWN'}
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


def problems(rows, root=ROOT, allow_private=False):
    errs, ids = [], {}
    classes = {'public', 'private'} if allow_private else {'public'}
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
        if r.get('privacy_class') not in classes:
            errs.append('%s: privacy_class must be %s; private records belong outside this repository' % (where, ' or '.join('"%s"' % c for c in sorted(classes))))
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
        if f == 'findings.jsonl':
            t = str(r.get('test_ref') or '')
            if not t:
                errs.append('%s: a finding needs test_ref (a test path, or "paper" until one exists)' % where)
            elif t != 'paper' and not (root / t.split('::')[0]).exists():
                errs.append('%s: test_ref file does not exist: %s' % (where, t))
            if r.get('finding_status') not in FINDING_STATUS:
                errs.append('%s: finding_status must be one of %s' % (where, ', '.join(sorted(FINDING_STATUS))))
            if r.get('kind') != 'OBSERVED':
                errs.append('%s: a finding is an OBSERVED record' % where)
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


REQUIRED_CHECKS = {'Immutable V2.5 integrity', 'Boundary hardening candidate', 'scan-publication-diff', 'brain-records'}


def settings_problems(rulesets, repo):
    """Findings ISS24-1/2/3/7/9/10: the protections Issue #24 asked for are still in place.

    rulesets: list of ruleset details (GET /repos/{owner}/{repo}/rulesets/{id}); repo: GET /repos/{owner}/{repo},
    plus 'actions_permissions' from GET /repos/{owner}/{repo}/actions/permissions."""
    errs = []

    def find(include):
        return [r for r in rulesets if r.get('enforcement') == 'active' and include in r['conditions']['ref_name']['include']]

    def rules(r):
        return {x['type']: x.get('parameters') or {} for x in r.get('rules', [])}

    main = find('~DEFAULT_BRANCH')
    if not main:
        errs.append('no active ruleset on the default branch')
    for r in main[:1]:
        got = rules(r)
        for t in ('deletion', 'non_fast_forward', 'required_linear_history', 'pull_request', 'required_status_checks'):
            if t not in got:
                errs.append('default-branch ruleset lacks %s' % t)
        checks = {c['context'] for c in got.get('required_status_checks', {}).get('required_status_checks', [])}
        if not REQUIRED_CHECKS <= checks:
            errs.append('required checks missing: %s' % ', '.join(sorted(REQUIRED_CHECKS - checks)))
        if 'required_status_checks' in got and not got['required_status_checks'].get('strict_required_status_checks_policy'):
            errs.append('required checks do not require up-to-date branches')
        if 'pull_request' in got and got['pull_request'].get('allowed_merge_methods') != ['squash']:
            errs.append('default branch is not squash-only')
        if r.get('bypass_actors'):
            errs.append('default-branch ruleset has bypass actors')
    for include, need, label in (('~ALL', ('deletion', 'non_fast_forward'), 'evidence-branch'),
                                 ('refs/tags/v*', ('deletion', 'update', 'non_fast_forward'), 'release-tag')):
        rs = find(include)
        if not rs or any(t not in rules(rs[0]) for t in need):
            errs.append('%s ruleset missing or incomplete' % label)
    sa = repo.get('security_and_analysis') or {}
    for k in ('secret_scanning', 'secret_scanning_push_protection'):
        if (sa.get(k) or {}).get('status') != 'enabled':
            errs.append('%s is not enabled' % k)
    if not (repo.get('actions_permissions') or {}).get('sha_pinning_required'):
        errs.append('Actions SHA pinning is not required in repository settings')
    return errs


def fetch_settings():
    listed = gh('api', 'repos/{owner}/{repo}/rulesets')
    repo = gh('api', 'repos/{owner}/{repo}')
    actions = gh('api', 'repos/{owner}/{repo}/actions/permissions')
    if listed is None or repo is None or actions is None:
        return None
    repo['actions_permissions'] = actions
    details = [gh('api', 'repos/{owner}/{repo}/rulesets/%d' % r['id']) for r in listed]
    return None if None in details else (details, repo)


# Finding SNAP-1: living docs (not dated records) must not describe merged PRs as open or proposed.
LIVING_DOCS = ('README.md', 'AGENTS.md', 'brain/README.md', 'docs/benchmarks/benchmark-log.md', 'docs/migration/README.md',
               'docs/research/intelligence/STATUS.md', 'docs/research/intelligence/README.md',
               'experiments/intelligence/README.md', 'security/README.md', 'validation/README.md')
PR_REF = re.compile(r'(?i)(?:\bPRs?\s*#|/pull/)(\d+)')
STALE_WORD = re.compile(r'(?i)\b(?:open|draft|pending|before merging|antes do merge|proposed|unmerged|not merged|to review|aberto|pendente|propost[oa]|'
                        r'em revis[aã]o|a revisar|n[aã]o integrad[oa])\b')
MERGED_WORD = re.compile(r'(?i)\b(?:merged|integrad[oa]s?|closed|fechado)\b')


def stale_doc_lines(merged, root=ROOT, docs=LIVING_DOCS):
    """Lines that call a merged PR open/proposed. merged: set of merged PR numbers."""
    out = []
    for rel in docs:
        path = Path(root) / rel
        if not path.exists():
            continue
        for n, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            if MERGED_WORD.search(line):
                continue
            for m in PR_REF.finditer(line):
                near = line[max(0, m.start() - 40):m.end() + 40]
                if int(m.group(1)) in merged and STALE_WORD.search(near):
                    out.append('%s:%d: PR #%s is merged but described as %r' % (rel, n, m.group(1), STALE_WORD.search(near).group(0)))
    return out


def merged_prs():
    rows = gh('pr', 'list', '--state', 'merged', '--limit', '500', '--json', 'number')
    return None if rows is None else {r['number'] for r in rows}


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
    obs = [r for r in cur if r.get('kind') != 'DECISION_RECORDED' and not r.get('finding_status')]
    if obs:
        L += ['', '## Observations and requests (not decisions)', '']
        L += ['- %s `%s`: %s%s' % (r['kind'].lower(), r['subject'], r['statement'],
                                   ' [scope: %s]' % r['scope'] if r.get('scope') else '') for r in obs]
    finds = [r for r in cur if r.get('finding_status')]
    if finds:
        paper = [r for r in finds if r.get('finding_status') in ('OPEN', 'UNKNOWN') and r.get('test_ref') == 'paper']
        L += ['', '## Findings (brain/records/findings.jsonl)', '',
              '- %d carried: %s' % (len(finds), ', '.join('%d %s' % (sum(r['finding_status'] == k for r in finds), k)
                                                       for k in sorted(FINDING_STATUS) if any(r['finding_status'] == k for r in finds))),
              '- not fixed and no test yet (paper): ' + (', '.join(r['id'] for r in paper) or 'none')]
    due = [r for r in cur if r.get('review_by') and r['review_by'] <= today]
    L += ['', '## Due for review', '']
    L += ['- %s (review_by %s)' % (r['id'], r['review_by']) for r in due] or ['- none']
    gates = json.loads(GATES.read_text(encoding='utf-8'))['gates'] if GATES.exists() else []
    L += ['', '## Gates', '']
    for g in gates:
        L.append('- %s %s: %s. Enforced by: %s' % ({'live': '[live]', 'waived': '[waived]'}.get(g['status'], '[PAPER]'), g['id'], g['principle'], g['enforced_by']))
    checks = benchmark_checks()
    if checks:
        L += ['', '## Benchmark checks (docs/benchmarks/benchmark-log.md)', '']
        L += ['- %s: %s (%s)' % (c['id'], c['check'], c['status']) for c in checks]
    fetched = fetch_settings() if online else None
    L += ['', '## Repository settings (Issue #24)', '']
    if fetched is None:
        L.append('- not checked (GitHub not reachable)')
    else:
        L += ['- PROBLEM: ' + e for e in settings_problems(*fetched)] or ['- protections in place (rulesets, required checks, secret scanning, Actions SHA pinning)']
    merged = merged_prs() if online else None
    L += ['', '## Stale living docs (merged PRs described as open)', '']
    if merged is None:
        L.append('- not checked (GitHub not reachable)')
    else:
        L += ['- ' + x for x in stale_doc_lines(merged)] or ['- none']
    L += ['', '## Open on GitHub', '']
    prs = gh('pr', 'list', '--state', 'open', '--json', 'number,title') if online else None
    issues = gh('issue', 'list', '--state', 'open', '--json', 'number,title') if online else None
    if prs is None and issues is None:
        L.append('- GitHub not reachable (gh missing, offline or not signed in); open work not listed.')
    else:
        L += ['- PR #%d %s' % (p['number'], p['title']) for p in prs or []] or ['- no open PRs']
        L += ['- Issue #%d %s' % (i['number'], i['title']) for i in issues or []]
    return '\n'.join(L) + '\n'
