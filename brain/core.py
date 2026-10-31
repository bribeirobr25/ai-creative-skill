"""Project Brain: record validation and status derived on read (contract: brain/CONTRACT.md)."""
import datetime
import json
import posixpath
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
STR_FIELDS = ('id', 'kind', 'subject', 'statement', 'authority_ref', 'supersedes', 'occurred_at', 'recorded_at',
              'review_by', 'privacy_class', 'finding_status', 'test_ref', 'source', 'scope')
SQUASH_PR = re.compile(r'\(#(\d+)\)\s*$')


def load(records=RECORDS):
    """Return [(file, line_no, record)]; a malformed line is reported, never skipped."""
    out = []
    for path in sorted(Path(records).glob('*.jsonl')):
        for n, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            if line.strip():
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError as e:
                    obj = {'_error': str(e)}
                out.append((path.name, n, obj if isinstance(obj, dict) else {'_error': 'not a JSON object'}))
    return out


def _typed(r):
    """A loaded object whose contract fields are strings (malformed lines are reported by problems())."""
    return '_error' not in r and isinstance(r.get('id'), str) and all(isinstance(r[k], str) for k in STR_FIELDS if r.get(k) is not None)


def _subject(r):
    return r.get('subject', '').strip().lower()


def problems(rows, root=ROOT, allow_private=False):
    errs, ids = [], {}
    classes = {'public', 'private'} if allow_private else {'public'}
    for f, n, r in rows:
        where = '%s:%d' % (f, n)
        if '_error' in r:
            errs.append('%s: not valid JSON (%s)' % (where, r['_error']))
            continue
        wrong = [k for k in STR_FIELDS if r.get(k) is not None and not isinstance(r[k], str)]
        if wrong:
            errs.append('%s: %s must be text' % (where, ', '.join(wrong)))
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
                elif not ref.startswith(('pr:', 'issue:', 'commit:')):
                    part = ref.split('#')[0]
                    if part != posixpath.normpath(part) or part.startswith(('./', '/')):
                        errs.append('%s: write evidence paths repo-relative without ./, // or a trailing /: %s' % (where, ref))
                    elif not (root / part).exists():
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
    typed = [(f, n, r) for f, n, r in rows if _typed(r)]
    known = {r['id']: r for _, _, r in typed}
    for f, n, r in typed:
        if r.get('supersedes') == r['id']:
            errs.append('%s:%d: %s supersedes itself' % (f, n, r['id']))
        elif r.get('supersedes') and r['supersedes'] not in known:
            errs.append('%s:%d: supersedes unknown id %s' % (f, n, r['supersedes']))
        elif r.get('supersedes') and r.get('kind') != 'DECISION_RECORDED' and \
                known[r['supersedes']].get('kind') == 'DECISION_RECORDED':
            errs.append('%s:%d: %s cannot supersede decision %s; only a decision can replace a decision' % (f, n, r.get('kind'), r['supersedes']))
    cycles = set()
    for _, _, r in typed:
        chain, nxt = [r['id']], r.get('supersedes')
        while nxt in known and nxt not in chain:
            chain.append(nxt)
            nxt = known[nxt].get('supersedes')
        if nxt in chain and nxt != r['id'] or (nxt == r['id'] and len(chain) > 1):
            loop = frozenset(chain[chain.index(nxt):])
            if loop not in cycles:
                cycles.add(loop)
                errs.append('supersession cycle: %s; history must end in one record' % ' -> '.join(chain[chain.index(nxt):] + [nxt]))
    errs += contradictions(current(rows))
    return errs


def contradictions(records):
    """Two or more decisions in force on one subject (compared without case or surrounding spaces)."""
    by_subject = {}
    for r in records:
        if r.get('kind') == 'DECISION_RECORDED':
            by_subject.setdefault(_subject(r), []).append(r['id'])
    return ['contradiction: %d current decisions on subject %r (%s); supersede one' % (len(rs), s, ', '.join(rs))
            for s, rs in sorted(by_subject.items()) if len(rs) > 1]


def current(rows, accepted=None):
    """Records in force. With `accepted` (ids of decisions whose PR the owner merged), any other decision
    neither counts nor supersedes: a pending replacement leaves the accepted decision current.
    Only a decision can supersede a decision; an observation or change request never revokes one.
    In the accepted view, a decision in force that supersedes one that is not (a pending or invalid middle link)
    also retires what that link superseded, so a chain never brings an older decision back."""
    recs = [r for _, _, r in rows if _typed(r)]
    by_id = {}
    for r in recs:
        by_id.setdefault(r['id'], r)
    decision = {i for i, r in by_id.items() if r.get('kind') == 'DECISION_RECORDED'}

    def counts(r):
        return accepted is None or r.get('kind') != 'DECISION_RECORDED' or r['id'] in accepted

    live = [r for r in recs if counts(r)]
    gone = set()
    for r in live:
        target, seen = r.get('supersedes'), {r['id']}
        if r.get('kind') != 'DECISION_RECORDED' and target in decision:
            continue
        while target and target not in seen:
            gone.add(target)
            seen.add(target)
            link = by_id.get(target)
            if link is None or counts(link):
                break
            target = link.get('supersedes')
    return [r for r in live if r['id'] not in gone]


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


def pr_files(n):
    """Paths changed by PR n, or None when GitHub is not reachable."""
    if not shutil.which('gh'):
        return None
    try:
        out = subprocess.run(['gh', 'api', '--paginate', 'repos/{owner}/{repo}/pulls/%d/files?per_page=100' % n, '--jq', '.[].filename'],
                             cwd=ROOT, capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return set(out.stdout.split('\n')) - {''} if out.returncode == 0 else None


def added_in(record_id):
    """The PR whose squash merge added this record on origin/main: its number, 'branch' when the record is not on
    origin/main (this branch only, or not fetched yet), 'unknown' when it arrived outside a squash-merged PR, or
    None when git cannot tell."""
    try:
        if subprocess.run(['git', 'rev-parse', '--verify', '-q', 'origin/main'], cwd=ROOT, capture_output=True).returncode:
            return None
        for needle in ('"id": "%s"' % record_id, '"id":"%s"' % record_id):
            out = subprocess.run(['git', 'log', 'origin/main', '--reverse', '--format=%s', '-S' + needle, '--', 'brain/records'],
                                 cwd=ROOT, capture_output=True, text=True, timeout=60)
            if out.returncode:
                return None
            first = out.stdout.splitlines()[:1]
            if first:
                m = SQUASH_PR.search(first[0])
                return int(m.group(1)) if m else 'unknown'
    except (OSError, subprocess.TimeoutExpired):
        return None
    return 'branch'


def authority(rows, fetch=None, files=None, added=None):
    """Classify every decision by its authority PR: {id: (state, reason)}.

    accepted: merged by the repository owner; the record itself was added to main by a PR the owner merged
              (from git history), so a branch cannot borrow an old merge; and the authority PR changed at least one
              of the record's evidence files (or brain/records when it cites none). The file match is a provenance
              consistency check that catches a wrong PR number; it is not proof of authorization, which is the
              owner's merge and review itself;
    pending: the PR is still open, or the record exists only on this branch; unverified: GitHub or git history
    not reachable; invalid: anything else, including a duplicate id or a malformed authority_ref."""
    fetch = fetch or (lambda n: gh('api', 'repos/{owner}/{repo}/pulls/%d' % n))
    files = files or pr_files
    added = added or added_in
    prs, changed, out = {}, {}, {}

    def pr_of(n):
        if n not in prs:
            prs[n] = fetch(n)
        return prs[n]

    def owner_merged(pr):
        return bool(pr.get('merged')) and (pr.get('merged_by') or {}).get('login') == pr['base']['repo']['owner']['login']

    decisions = [r for _, _, r in rows if _typed(r) and r.get('kind') == 'DECISION_RECORDED']
    seen = {}
    for r in decisions:
        seen[r['id']] = seen.get(r['id'], 0) + 1
    for r in decisions:
        rid = r['id']
        m = AUTHORITY.match(r.get('authority_ref', ''))
        if seen[rid] > 1:
            out[rid] = ('invalid', 'duplicate id %s; no copy counts until one is renamed' % rid)
            continue
        if not m:
            out[rid] = ('invalid', 'authority_ref must be "pr:#N"')
            continue
        n = int(m.group(1))
        pr = pr_of(n)
        if pr is None:
            out[rid] = ('unverified', 'cannot reach GitHub to verify pr:#%d' % n)
            continue
        if not pr.get('merged'):
            out[rid] = ('pending', 'pr:#%d is open, not merged yet' % n) if pr.get('state') == 'open' else \
                ('invalid', 'pr:#%d was closed without merge, so it is not the owner\'s decision' % n)
            continue
        if not owner_merged(pr):
            out[rid] = ('invalid', 'pr:#%d was not merged by the repository owner' % n)
            continue
        source = added(rid)
        if source is None:
            out[rid] = ('unverified', 'cannot tell from git history which PR added the record (fetch origin/main)')
            continue
        if source == 'branch':
            out[rid] = ('pending', 'the record exists only on this branch; it counts once its PR is merged (or run git fetch)')
            continue
        if source == 'unknown':
            out[rid] = ('invalid', 'the record reached main outside a squash-merged PR')
            continue
        if source != n:
            adder = pr_of(source)
            if adder is None:
                out[rid] = ('unverified', 'cannot reach GitHub to verify pr:#%d, which added the record' % source)
                continue
            if not owner_merged(adder):
                out[rid] = ('invalid', 'the record was added by pr:#%d, which the owner did not merge' % source)
                continue
        if n not in changed:
            changed[n] = files(n)
        if changed[n] is None:
            out[rid] = ('unverified', 'cannot reach GitHub to list the files of pr:#%d' % n)
            continue
        paths = {e.split('#')[0] for e in r.get('evidence_refs', []) if not str(e).startswith(('pr:', 'issue:', 'commit:'))}
        hit = {p for p in paths if p in changed[n] or any(f.startswith(p.rstrip('/') + '/') for f in changed[n])} if paths \
            else {f for f in changed[n] if f.startswith('brain/records/')}
        out[rid] = ('accepted', '') if hit else \
            ('invalid', 'pr:#%d changed none of the record\'s evidence files (provenance check); is the PR number right?' % n)
    return out


def verify_authority(rows, fetch=None, files=None, added=None):
    """Every decision, current or history, must be the owner's: merged by the owner, added by an owner-merged PR,
    and consistent with its evidence. A chain is only as good as each link."""
    states = authority(rows, fetch, files, added)
    errs = []
    for rid, (state, reason) in sorted(states.items()):
        if state != 'accepted':
            errs.append('%s: %s%s' % (rid, reason, ', so the decision is not yet the owner\'s' if state == 'pending' else ''))
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
               'experiments/intelligence/README.md', 'security/README.md', 'validation/README.md', 'docs/vision/README.md',
               'brain/gates.json')
PR_REF = re.compile(r'(?i)(?:\bPRs?\s*#|/pull/)(\d+)')
STALE_WORD = re.compile(r'(?i)\b(?:open|draft|pending|before merging|antes do merge|proposed|unmerged|not merged|to review|aberto|pendente|propost[oa]|'
                        r'em revis[aã]o|a revisar|n[aã]o integrad[oa])\b')
MERGED_WORD = re.compile(r'(?i)\b(?:merged|integrad[oa]s?|closed|fechado)\b')


ADR_STATUS = re.compile(r'^\*\*Status:\*\*\s*ACCEPTED', re.M)
PROPOSED_WORD = r'(?:PROPOSED|proposed|propost[oa]|continua PROPOSED)'
ADR_FILENAME = re.compile(r'ADR-\d{4}-PROPOSED-[\w.-]*')


def accepted_adrs(root=ROOT):
    """ADR ids whose own Status line says ACCEPTED."""
    return {p.name[:8] for p in sorted((Path(root) / 'docs' / 'decisions').glob('ADR-[0-9][0-9][0-9][0-9]-*.md'))
            if ADR_STATUS.search(p.read_text(encoding='utf-8'))}


def stale_doc_lines(merged, root=ROOT, docs=LIVING_DOCS):
    """Lines that call a merged PR open/proposed, or an accepted ADR proposed (2026-10-30 audit).
    merged: set of merged PR numbers."""
    out = []
    adrs = accepted_adrs(root)
    adr_rx = [(a, re.compile(r'%s(?!-PROPOSED-)(?:(?!ADR-)[^.\n]){0,40}?\b%s\b|\b%s\s+(?:a\s+)?%s' % (a, PROPOSED_WORD, PROPOSED_WORD, a)))
              for a in sorted(adrs)]
    for rel in docs:
        path = Path(root) / rel
        if not path.exists():
            continue
        for n, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            bare = ADR_FILENAME.sub('', line)
            for a, rx in adr_rx:
                if rx.search(bare) and not re.search(r'(?i)\baccept', bare):
                    out.append('%s:%d: %s is ACCEPTED but described as proposed' % (rel, n, a))
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


def status(rows, today=None, online=True, fetch=None, files=None, added=None):
    today = today or datetime.date.today().isoformat()
    L = ['# Project Brain status (derived %s; not committed)' % today, '']
    errs = problems(rows)
    if errs:
        L += ['**Records have %d problem(s); run `python3 -m brain validate`.**' % len(errs), '']

    def line(r, note=''):
        return '- **%s** (%s, %s): %s%s' % (r.get('subject', '?'), r.get('occurred_at', '?'), r.get('authority_ref', '?'),
                                             r.get('statement', '?'), note)

    def decisions(rs):
        return sorted((r for r in rs if r.get('kind') == 'DECISION_RECORDED'), key=lambda r: r.get('subject', ''))

    states = authority(rows, fetch, files, added) if (online or fetch) else None
    if states is None:
        cur = current(rows)
        L += ['## Decisions (not verified: GitHub not reachable; none is confirmed as the owner\'s)', '']
        L += [line(r) for r in decisions(cur)]
    else:
        accepted = {i for i, (st, _) in states.items() if st == 'accepted'}
        cur = current(rows, accepted)
        typed = [r for _, _, r in rows if _typed(r)]
        by_id = {}
        for r in typed:
            by_id.setdefault(r['id'], r)
        # A decision whose replacement cannot be checked may already be replaced: not shown as confirmed.
        unsure = {r['supersedes']: r['id'] for r in typed
                  if r.get('kind') == 'DECISION_RECORDED' and r.get('supersedes') and states.get(r['id'], ('',))[0] == 'unverified'}
        L += ['## Current decisions', '']
        L += [line(r) for r in decisions(cur) if r['id'] not in unsure] or ['- none confirmed']
        superseded_by = {}
        for r in typed:
            if r.get('kind') == 'DECISION_RECORDED' and r.get('supersedes'):
                superseded_by.setdefault(r['supersedes'], []).append(r['id'])
        extra = {'invalid': ['- ' + c for c in contradictions(cur)],
                 'unverified': [line(r, ' (may be superseded by %s, which cannot be checked)' % unsure[r['id']])
                                for r in decisions(cur) if r['id'] in unsure]}
        for state, title in (('pending', 'Pending decisions (their PR is not merged yet; not in force)'),
                             ('unverified', 'Decisions not verified (GitHub or git history not reachable)'),
                             ('invalid', 'Decision problems (not in force)')):
            rs = [by_id[i] for i, (st, _) in states.items() if st == state and i in by_id]
            items = []
            for r in decisions(rs):
                note = ' (would replace %s)' % r['supersedes'] if r.get('supersedes') and state == 'pending' else ''
                held = [i for i in superseded_by.get(r['id'], []) if i in accepted]
                if held:
                    note += ' (superseded by %s, which is in force, although this link is not)' % ', '.join(held)
                items.append(line(r, note + ' [%s]' % states[r['id']][1]))
            items += extra.get(state, [])
            if items:
                L += ['', '## ' + title, ''] + items
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
              '- not fixed and no test yet (paper): ' + (', '.join(r['id'] for r in paper) or 'none'),
              '- fixed or accepted, verified by review only (no automated guard): ' +
              (', '.join(r['id'] for r in finds if r.get('finding_status') in ('FIXED', 'ACCEPTED-RISK') and r.get('test_ref') == 'paper') or 'none')]
    # Due reviews are listed whatever GitHub says; a decision that is not confirmed is tagged with its state.
    pool = {r['id']: r for r in current(rows) + cur}
    due = sorted((r for r in pool.values() if r.get('review_by') and r['review_by'] <= today), key=lambda r: r['id'])
    tag = lambda r: '' if states is None or r.get('kind') != 'DECISION_RECORDED' or r['id'] in accepted \
        else ' [%s]' % states.get(r['id'], ('not checked',))[0]  # noqa: E731
    L += ['', '## Due for review', '']
    L += ['- %s (review_by %s)%s' % (r['id'], r['review_by'], tag(r)) for r in due] or ['- none']
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
