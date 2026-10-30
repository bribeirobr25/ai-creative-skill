"""Guards for findings carried into brain/records/findings.jsonl. Each test names the finding it keeps fixed."""
import copy
import re
import subprocess
import sys
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
        self.assertIn('git archive "origin/$GITHUB_BASE_REF" security', wf)
        self.assertIn('"$RUNNER_TEMP/base-guard/security/publication_guard.py"', wf)


def good_settings():
    def rs(include, rules):
        return {'enforcement': 'active', 'bypass_actors': [], 'conditions': {'ref_name': {'include': [include]}},
                'rules': [{'type': t, 'parameters': p} for t, p in rules]}
    main = rs('~DEFAULT_BRANCH', [('deletion', None), ('non_fast_forward', None), ('required_linear_history', None),
                                  ('pull_request', {'allowed_merge_methods': ['squash']}),
                                  ('required_status_checks', {'strict_required_status_checks_policy': True,
                                                              'required_status_checks': [{'context': c} for c in core.REQUIRED_CHECKS]})])
    branches = rs('~ALL', [('deletion', None), ('non_fast_forward', None)])
    tags = rs('refs/tags/v*', [('deletion', None), ('update', None), ('non_fast_forward', None)])
    repo = {'security_and_analysis': {'secret_scanning': {'status': 'enabled'}, 'secret_scanning_push_protection': {'status': 'enabled'}}}
    return [main, branches, tags], repo


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
        }
        for want, mutate in cases.items():
            rs, repo = copy.deepcopy(good_settings())
            mutate(rs, repo)
            errs = core.settings_problems(rs, repo)
            self.assertTrue(any(want.split()[-1] in e for e in errs), (want, errs))


if __name__ == '__main__':
    unittest.main()
