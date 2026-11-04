"""Guards for findings carried into brain/records/findings.jsonl. Each test names the finding it keeps fixed."""
import copy
import json
import os
import re
import shutil
import tempfile
import subprocess
import sys
import textwrap
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from brain import core  # noqa: E402


def tracked(prefix):
    out = subprocess.run(['git', 'ls-files', prefix], cwd=ROOT, capture_output=True, text=True, check=True).stdout
    return [ROOT / p for p in out.split()]


class SrcExposure(unittest.TestCase):
    """S0-1 and P1b: no private storage locator or operator-account statement in the shipped skill."""
    PATTERNS = [re.compile(p) for p in (r'drive\.google\.com', r'/Google Drive/', r"operator's account", r'\bin the account\b')]

    def test_no_private_locators_under_src(self):
        hits = []
        for path in tracked('src'):
            if path.suffix.lower() in ('.md', '.json', '.py', '.txt', '.yml', '.yaml', '.html', '.js', '.css'):
                text = path.read_text(encoding='utf-8', errors='replace')
                hits += ['%s: %s' % (path.relative_to(ROOT), p.pattern) for p in self.PATTERNS if p.search(text)]
        self.assertEqual(hits, [])


class ActionsPinning(unittest.TestCase):
    """PR20-P2-7: every third-party Action is pinned by a full commit SHA."""
    KNOWN_UNPINNED = set()

    def test_no_new_unpinned_actions(self):
        refs = set()
        for wf in tracked('.github/workflows'):
            refs |= set(re.findall(r'uses:\s*([^\s#]+)', wf.read_text()))
        unpinned = {r for r in refs if not re.search(r'@[0-9a-f]{40}$', r) and not r.startswith('./')}
        self.assertLessEqual(unpinned, self.KNOWN_UNPINNED, 'pin new Actions by commit SHA')

    def test_guard_enforces_with_base_branch_copy(self):
        # PR20-P1-4: the enforcing scan must run the base branch's scanner, not the PR's.
        wf = (ROOT / '.github/workflows/publication-guard.yml').read_text()
        self.assertIn('git archive "$BASE_SHA" security', wf)
        self.assertIn('BASE_SHA: ${{ github.event.pull_request.base.sha }}', wf)
        self.assertIn('"$RUNNER_TEMP/base-guard/security/publication_guard.py"', wf)

    @staticmethod
    def steps(name):
        text = (ROOT / '.github/workflows' / name).read_text()
        return re.split(r'\n      - ', text)[1:]

    def test_piped_steps_keep_the_exit_status(self):
        # 2026-10-30 audit: under the default `bash -e`, `scan | tee out` returns tee's status and hides a BLOCK.
        # Any step that pipes into tee must run with `shell: bash` (which sets pipefail).
        for wf in tracked('.github/workflows'):
            for step in re.split(r'\n      - ', wf.read_text())[1:]:
                if re.search(r'\|\s*tee\b', step):
                    self.assertRegex(step, r'\n\s+shell: bash\n', '%s: %s' % (wf.name, step.splitlines()[0]))

    def test_required_checks_run_only_on_pull_requests(self):
        # 2026-11-03 audit: a manual run reported the required check names using only the branch's own code, and
        # retargeting a PR did not re-run brain-records.
        for name in ('brain.yml', 'publication-guard.yml'):
            head = (ROOT / '.github/workflows' / name).read_text().split('\njobs:')[0]
            self.assertNotIn('workflow_dispatch', head, name)
            self.assertIn('types: [opened, synchronize, reopened, edited]', head, name)
        self.assertIn('history-audit:', (ROOT / '.github/workflows/history-audit.yml').read_text())

    def test_base_brain_step_cannot_be_shadowed(self):
        # 2026-11-03 audit: `python -m` puts the working folder first on sys.path, so a top-level module in the PR
        # could replace the standard library inside the base-copy step.
        step = next(st for st in self.steps('brain.yml') if 'git archive "$BASE_SHA" brain' in st)
        self.assertIn('python -P -m brain validate', step)
        self.assertIn('PYTHONPATH="$RUNNER_TEMP/brain-path"', step)

    def test_enforcing_checks_run_before_pr_code(self):
        # 2026-10-30 audit: the base-copy checks run before any step that executes the PR's own code.
        guard = self.steps('publication-guard.yml')
        base = next(i for i, st in enumerate(guard) if 'base-guard' in st)
        self.assertLess(base, next(i for i, st in enumerate(guard) if 'unittest discover -s security' in st))
        brain = self.steps('brain.yml')
        base = next(i for i, st in enumerate(brain) if 'git archive "$BASE_SHA" brain' in st)
        self.assertLess(base, next(i for i, st in enumerate(brain) if st.startswith('name: Records follow')))
        self.assertIn('fetch-depth: 0', brain[0])

    def test_media_needs_recorded_review(self):
        # OWN-A2: a REVIEW for media fails the required check unless the PR body records the human review.
        wf = (ROOT / '.github/workflows/publication-guard.yml').read_text()
        self.assertIn('tee "$RUNNER_TEMP/guard.out"', wf)
        self.assertIn("grep -q -i -E '^Media reviewed: *[^ ]'", wf)
        self.assertIn('types: [opened, synchronize, reopened, edited]', wf)


def good_settings():
    def rs(include, rules, target='branch', exclude=()):
        return {'enforcement': 'active', 'target': target, 'bypass_actors': [],
                'conditions': {'ref_name': {'include': [include], 'exclude': list(exclude)}},
                'rules': [{'type': t, 'parameters': p} for t, p in rules]}
    main = rs('~DEFAULT_BRANCH', [('deletion', None), ('non_fast_forward', None), ('required_linear_history', None),
                                  ('pull_request', {'allowed_merge_methods': ['squash']}),
                                  ('required_status_checks', {'strict_required_status_checks_policy': True,
                                                              'required_status_checks': [{'context': c, 'integration_id': 15368} for c in core.REQUIRED_CHECKS]})])
    branches = rs('~ALL', [('non_fast_forward', None)], exclude=('~DEFAULT_BRANCH', 'refs/heads/dependabot/**'))
    tags = rs('refs/tags/v*', [('deletion', None), ('update', None), ('non_fast_forward', None)], target='tag')
    archive = rs('refs/tags/archive/**', [('deletion', None), ('update', None), ('non_fast_forward', None)], target='tag')
    repo = {'delete_branch_on_merge': True, 'security_and_analysis': {'secret_scanning': {'status': 'enabled'}, 'secret_scanning_push_protection': {'status': 'enabled'}},
            'actions_permissions': {'sha_pinning_required': True}}
    repo.update(branches=['main', 'feature-x'], open_pr_heads=['feature-x'], default_branch='main')
    return [main, branches, tags, archive], repo


class RepoSettings(unittest.TestCase):
    """ISS24-1/2/3/7/9/10: `python3 -m brain status` re-checks the live settings on read; these tests pin the checker."""

    def test_good_settings_pass(self):
        self.assertEqual(core.settings_problems(*good_settings()), [])

    def test_each_weakening_is_reported(self):
        cases = {
            'required checks missing': lambda rs, repo: rs[0]['rules'][4]['parameters']['required_status_checks'].pop(),
            'up-to-date': lambda rs, repo: rs[0]['rules'][4]['parameters'].update(strict_required_status_checks_policy=False),
            'squash-only': lambda rs, repo: rs[0]['rules'][3]['parameters'].update(allowed_merge_methods=['squash', 'merge']),
            'bypass actors': lambda rs, repo: rs[0].update(bypass_actors=[{'actor_id': 1}]),
            'release-tag': lambda rs, repo: rs.pop(2),
            'evidence-branch': lambda rs, repo: rs[1].update(enforcement='disabled'),
            'push_protection': lambda rs, repo: repo['security_and_analysis']['secret_scanning_push_protection'].update(status='disabled'),
            'lacks deletion': lambda rs, repo: rs[0]['rules'].pop(0),
            'SHA pinning': lambda rs, repo: repo['actions_permissions'].update(sha_pinning_required=False),
            'deleted automatically': lambda rs, repo: repo.update(delete_branch_on_merge=False),
            'evidence-branch ruleset missing': lambda rs, repo: rs[1]['rules'].pop(),
            'evidence-branch ruleset excludes': lambda rs, repo: rs[1]['conditions']['ref_name']['exclude'].append('refs/heads/**'),
            'release-tag ruleset has bypass actors': lambda rs, repo: rs[2].update(bypass_actors=[{'actor_id': 1}]),
            'evidence-branch ruleset targets': lambda rs, repo: rs[1].update(target='tag'),
            'not pinned to GitHub Actions': lambda rs, repo: rs[0]['rules'][4]['parameters']['required_status_checks'][0].pop('integration_id'),
            'archive-tag ruleset missing': lambda rs, repo: rs.pop(3),
            'branches without an open PR': lambda rs, repo: repo['branches'].append('stale-branch'),
        }
        for want, mutate in cases.items():
            rs, repo = copy.deepcopy(good_settings())
            mutate(rs, repo)
            errs = core.settings_problems(rs, repo)
            self.assertTrue(any(want.split()[-1] in e for e in errs), (want, errs))


class StaleDocs(unittest.TestCase):
    """SNAP-1: living docs must not call a merged PR open or proposed (`python3 -m brain lint-docs` in CI)."""

    def lint(self, text, merged=frozenset({23})):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / 'README.md').write_text(text, encoding='utf-8')
            return core.stale_doc_lines(set(merged), root=d, docs=('README.md',))

    def test_merged_pr_called_proposed_or_open_is_flagged(self):
        self.assertTrue(self.lint('S1: substituição proposta no PR #23'))
        self.assertTrue(self.lint('See PR #23, still open for review'))

    def test_accepted_adr_called_proposed_is_flagged(self):
        # 2026-10-30 audit: five living lines still called ADR-0003 PROPOSED and the lint did not see them.
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / 'docs' / 'decisions').mkdir(parents=True)
            (Path(d) / 'docs' / 'decisions' / 'ADR-0003-PROPOSED-x.md').write_text('# x\n\n**Status:** ACCEPTED by the owner.\n')
            (Path(d) / 'docs' / 'decisions' / 'ADR-0004-PROPOSED-y.md').write_text('# y\n\n**Status:** PROPOSED.\n')
            (Path(d) / 'README.md').write_text('ADR-0003 is PROPOSED\n"source": "ADR-0003 (PROPOSED)"\nproposed ADR-0003 here\n'
                                               'ADR-0004 is PROPOSED\nsee ADR-0003-PROPOSED-x.md\nADR-0003 was proposed, then accepted\n'
                                               '[ADR-0003](docs/decisions/ADR-0003-PROPOSED-x.md) and ADR-0005; ADR-0004 is PROPOSED\n')
            got = core.stale_doc_lines(set(), root=d, docs=('README.md',))
        self.assertEqual([g.split(':')[1] for g in got], ['1', '2', '3'])

    def test_proposed_status_in_any_case_but_not_history(self):
        # 2026-11-03 audit: "status: Proposed" was missed, an unrelated "accepted" on the line exempted it, and a
        # true historical sentence ("ADR-0005 D2 proposed withdrawing M4") was flagged.
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / 'docs' / 'decisions').mkdir(parents=True)
            for n in ('0003', '0005', '0006'):
                (Path(d) / 'docs' / 'decisions' / ('ADR-%s-x.md' % n)).write_text('# x\n\n**Status:** ACCEPTED.\n')
            (Path(d) / 'README.md').write_text('ADR-0003 status: Proposed.\nADR-0003 is PROPOSED; ADR-0006 is accepted.\n'
                                               'ADR-0005 D2 proposed withdrawing M4\nADR-0003 is still proposed\n'
                                               'ADR-0006 was proposed and accepted\n')
            got = core.stale_doc_lines(set(), root=d, docs=('README.md',))
        self.assertEqual([g.split(':')[1] for g in got], ['1', '2', '4'])

    def test_acknowledged_or_unmerged_is_not_flagged(self):
        self.assertEqual(self.lint('PR #23 was merged on 2026-10-26; it had been proposed earlier'), [])
        self.assertEqual(self.lint('PR #99 is open', merged={23}), [])
        self.assertEqual(self.lint('PR #23 added the lab'), [])

    def test_living_docs_list_exists(self):
        self.assertTrue(all((ROOT / p).exists() for p in core.LIVING_DOCS))


class BaseRecordsFailClosed(unittest.TestCase):
    def test_a_base_with_no_records_cannot_be_read(self):
        # FND-AUDIT2-RECORD-REWRITE (2026-11-04 review): an empty listing means a wrong path or git context, and
        # reading it as "no merged records" would pass every rewrite.
        self.assertIsNone(core.main_records('4b825dc642cb6eb9a060e54bf8d69288fbee4904'))  # git's empty tree
        self.assertIsNone(core.main_records('no-such-ref'))
        self.assertTrue(core.main_records('HEAD'))


class TrustedRuleFive(unittest.TestCase):
    """FND-AUDIT2-RECORD-REWRITE: the base-code step in brain.yml judges rule 5 itself, so a PR that rewrites a merged
    record and edits its own validator to hide it still fails (2026-11-04 review). Runs the step's own script in a
    throwaway repository. It covers the validator path only: a PR that edits the workflow is FND-AUDIT-WORKFLOW-EDIT."""

    @classmethod
    def setUpClass(cls):
        if sys.version_info < (3, 11):
            raise unittest.SkipTest('the step runs python -P (3.11+)')
        text = (ROOT / '.github/workflows/brain.yml').read_text()
        step = next(st for st in re.split(r'\n      - ', text)[1:] if 'git archive "$BASE_SHA" brain' in st)
        cls.script = textwrap.dedent(step.split('run: |\n', 1)[1])

    def git(self, ws, *args):
        return subprocess.run(['git', '-c', 'user.name=t', '-c', 'user.email=t@example.invalid', *args], cwd=ws,
                              capture_output=True, text=True, check=True).stdout.strip()

    def run_step(self, base_edit=None, rewrite=True, blind=True):
        d = Path(self.enterContext(tempfile.TemporaryDirectory(ignore_cleanup_errors=True)))
        ws = d / 'ws'
        for rel in subprocess.run(['git', 'ls-files', '-z'], cwd=ROOT, capture_output=True, text=True,
                                  check=True).stdout.split('\0'):
            if rel and (ROOT / rel).is_file():
                (ws / rel).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / rel, ws / rel)
        if base_edit:
            base_edit(ws)
        self.git(ws, 'init', '-q')
        self.git(ws, 'add', '-A')
        self.git(ws, 'commit', '-q', '-m', 'base')
        base = self.git(ws, 'rev-parse', 'HEAD')
        if rewrite:
            path = ws / 'brain/records/decisions.jsonl'
            lines = path.read_text().splitlines()
            i = next(n for n, line in enumerate(lines) if '"DECISION_RECORDED"' in line)
            r = json.loads(lines[i])
            r['statement'] += ' (rewritten)'
            lines[i] = json.dumps(r)
            path.write_text('\n'.join(lines) + '\n')
        if blind:
            core_py = ws / 'brain/core.py'
            core_py.write_text(core_py.read_text().replace('def append_only_problems(base, rows):\n',
                                                           'def append_only_problems(base, rows):\n    return []\n', 1))
        self.git(ws, 'commit', '-q', '-am', 'head')
        shim = d / 'bin'
        shim.mkdir()
        (shim / 'python').symlink_to(sys.executable)
        if sys.platform == 'darwin':
            # macOS bsdtar stops reading at the end-of-archive marker, so `git archive | tar` can end in SIGPIPE
            # under pipefail; the CI runner's GNU tar reads to the end. Buffer the stream for local runs.
            (shim / 'tar').write_text('#!/bin/bash\nf=$(mktemp); cat > "$f"; /usr/bin/tar "$@" -f "$f"; s=$?; rm -f "$f"; exit $s\n')
            (shim / 'tar').chmod(0o755)
        (d / 'runner').mkdir()
        env = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}
        env.update(BASE_SHA=base, GITHUB_WORKSPACE=str(ws), RUNNER_TEMP=str(d / 'runner'),
                   PATH='%s%s%s' % (shim, os.pathsep, env.get('PATH', '')))
        step = subprocess.run(['bash', '-eo', 'pipefail', '-c', self.script], cwd=ws, env=env, capture_output=True, text=True)
        own = subprocess.run(['python', '-m', 'brain', 'validate', '--base-ref', base], cwd=ws, env=env,
                             capture_output=True, text=True)
        return step, own

    def test_rewrite_with_blinded_validator_fails_the_base_step(self):
        step, own = self.run_step()
        self.assertEqual(own.returncode, 0, own.stdout)  # the PR's own validator no longer sees the rewrite
        self.assertNotEqual(step.returncode, 0, step.stdout + step.stderr)
        self.assertIn('was changed after its merge', step.stdout)

    def test_clean_pr_passes_the_base_step(self):
        step, _ = self.run_step(rewrite=False)
        self.assertEqual(step.returncode, 0, step.stdout + step.stderr)

    def test_bootstrap_base_without_the_flag_cannot_judge_rule_5(self):
        # Documented limit: a base validator that predates --base-ref (main before PR #58) leaves rule 5 to the PR's code.
        def old_base(ws):
            m = ws / 'brain/__main__.py'
            m.write_text(m.read_text().replace("'--base-ref'", "'--base-git-ref'"))
        step, _ = self.run_step(base_edit=old_base)
        self.assertEqual(step.returncode, 0, step.stdout + step.stderr)
        self.assertIn('::warning::bootstrap', step.stdout)

    def test_current_validator_keeps_the_flag(self):
        # Once this is on main, the base step requires rule 5; renaming the flag would silently fall back to bootstrap.
        self.assertIn('--base-ref', (ROOT / 'brain/__main__.py').read_text())

if __name__ == '__main__':
    unittest.main()
