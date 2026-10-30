import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from brain import core  # noqa: E402


def rec(**kw):
    r = {'id': 'DEC-x', 'kind': 'DECISION_RECORDED', 'subject': 's', 'statement': 'x', 'authority_ref': 'pr:#1',
         'evidence_refs': [], 'occurred_at': '2026-10-30', 'recorded_at': '2026-10-30', 'privacy_class': 'public'}
    r.update(kw)
    return r


def rows(*records, file='decisions.jsonl'):
    return [(file, n, r) for n, r in enumerate(records, 1)]


class Contract(unittest.TestCase):
    def test_repository_records_pass(self):
        self.assertEqual(core.problems(core.load()), [])

    def test_decision_needs_owner_pr(self):
        errs = core.problems(rows(rec(authority_ref='owner said so in chat')))
        self.assertTrue(any('authority_ref' in e for e in errs))

    def test_private_record_rejected(self):
        errs = core.problems(rows(rec(privacy_class='private')))
        self.assertTrue(any('privacy_class' in e for e in errs))

    def test_contradiction_fails_closed(self):
        errs = core.problems(rows(rec(id='A'), rec(id='B')))
        self.assertTrue(any('contradiction' in e for e in errs))

    def test_superseded_is_not_current(self):
        rs = rows(rec(id='A'), rec(id='B', supersedes='A'))
        self.assertEqual(core.problems(rs), [])
        self.assertEqual([r['id'] for r in core.current(rs)], ['B'])

    def test_unknown_supersedes_and_duplicate_id(self):
        errs = core.problems(rows(rec(id='A', supersedes='Z'), rec(id='A', subject='t')))
        self.assertTrue(any('unknown id' in e for e in errs))
        self.assertTrue(any('duplicate id' in e for e in errs))

    def test_observation_never_counts_as_decision(self):
        rs = rows(rec(id='O', kind='OBSERVED', authority_ref=None), rec(id='D'))
        self.assertEqual(core.problems(rs), [])

    def test_missing_evidence_path_and_bad_date(self):
        errs = core.problems(rows(rec(evidence_refs=['docs/no-such-file.md'], review_by='soon')))
        self.assertTrue(any('does not exist' in e for e in errs))
        self.assertTrue(any('review_by' in e for e in errs))

    def test_finding_needs_test_ref(self):
        errs = core.problems(rows(rec(kind='OBSERVED', authority_ref=None), file='findings.jsonl'))
        self.assertTrue(any('test_ref' in e for e in errs))

    def test_finding_status_and_test_file_checked(self):
        bad = rec(kind='OBSERVED', authority_ref=None, finding_status='DONE', test_ref='tests/no_such_test.py::X')
        errs = core.problems(rows(bad, file='findings.jsonl'))
        self.assertTrue(any('finding_status' in e for e in errs))
        self.assertTrue(any('test_ref file does not exist' in e for e in errs))

    def test_malformed_line_reported(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / 'decisions.jsonl').write_text('{"id": \n')
            self.assertTrue(any('not valid JSON' in e for e in core.problems(core.load(d))))


class Authority(unittest.TestCase):
    def pr(self, merged=True, by='owner', owner='owner'):
        return {'merged': merged, 'merged_by': {'login': by} if by else None, 'base': {'repo': {'owner': {'login': owner}}}}

    def test_owner_merge_verifies(self):
        self.assertEqual(core.verify_authority(rows(rec()), fetch=lambda n: self.pr()), [])

    def test_unmerged_or_other_merger_fails(self):
        self.assertTrue(core.verify_authority(rows(rec()), fetch=lambda n: self.pr(merged=False)))
        self.assertTrue(core.verify_authority(rows(rec()), fetch=lambda n: self.pr(by='someone-else')))

    def test_unreachable_github_fails(self):
        self.assertTrue(core.verify_authority(rows(rec()), fetch=lambda n: None))


class Status(unittest.TestCase):
    def test_status_offline_lists_decisions_and_due_reviews(self):
        out = core.status(rows(rec(review_by='2026-01-01')), today='2026-10-30', online=False)
        self.assertIn('## Current decisions', out)
        self.assertIn('DEC-x (review_by 2026-01-01)', out)
        self.assertIn('GitHub not reachable', out)

    def test_benchmark_checks_parsed(self):
        self.assertTrue(any(c['id'] == 'C1' for c in core.benchmark_checks()))

    def test_gates_file_shape(self):
        gates = json.loads(core.GATES.read_text())['gates']
        self.assertTrue(all(g['status'] in ('live', 'paper') for g in gates))
        self.assertEqual(len({g['id'] for g in gates}), len(gates))

    def test_private_class_only_outside_repository(self):
        self.assertEqual(core.problems(rows(rec(privacy_class='private')), allow_private=True), [])
        out = subprocess.run([sys.executable, '-m', 'brain', 'validate', '--records', 'brain/records', '--allow-private'],
                             cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(out.returncode, 1)
        self.assertIn('outside this repository', out.stdout)

    def test_cli_validate(self):
        out = subprocess.run([sys.executable, '-m', 'brain', 'validate'], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(out.returncode, 0, out.stdout + out.stderr)
        self.assertIn('PASS', out.stdout)


if __name__ == '__main__':
    unittest.main()
