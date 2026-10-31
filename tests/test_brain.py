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


def pr(merged=True, by='owner', owner='owner', state=None):
    return {'merged': merged, 'state': state or ('closed' if merged else 'open'),
            'merged_by': {'login': by} if by and merged else None, 'base': {'repo': {'owner': {'login': owner}}}}


EVIDENCE = 'brain/CONTRACT.md'
CHANGED = lambda n: {EVIDENCE}  # noqa: E731  the authority PR changed the record's evidence file


def own_pr(*records):
    """Stub for git history: each record was added to main by its own authority PR."""
    m = {r['id']: int(r['authority_ref'][4:]) for r in records if str(r.get('authority_ref', '')).startswith('pr:#')}
    return lambda rid: m.get(rid, 'branch')


class Authority(unittest.TestCase):
    def verify(self, record, fetch, files=CHANGED, added=None):
        return core.verify_authority(rows(record), fetch=fetch, files=files, added=added or own_pr(record))

    def test_owner_merge_verifies(self):
        self.assertEqual(self.verify(rec(evidence_refs=[EVIDENCE]), lambda n: pr()), [])

    def test_unmerged_or_other_merger_fails(self):
        self.assertTrue(self.verify(rec(evidence_refs=[EVIDENCE]), lambda n: pr(merged=False)))
        self.assertTrue(self.verify(rec(evidence_refs=[EVIDENCE]), lambda n: pr(by='someone-else')))

    def test_unreachable_github_fails(self):
        self.assertTrue(self.verify(rec(evidence_refs=[EVIDENCE]), lambda n: None))
        self.assertTrue(self.verify(rec(evidence_refs=[EVIDENCE]), lambda n: pr(), files=lambda n: None))

    def test_wrong_pr_number_cannot_borrow_another_merge(self):
        # A record citing a PR that the owner merged but that carries none of its evidence (e.g. a Dependabot PR).
        errs = self.verify(rec(evidence_refs=[EVIDENCE]), lambda n: pr(), files=lambda n: {'.github/workflows/brain.yml'})
        self.assertTrue(errs and 'is the PR number right' in errs[0], errs)

    def test_record_without_evidence_files_needs_a_records_change(self):
        self.assertTrue(self.verify(rec(), lambda n: pr(), files=lambda n: {'README.md'}))
        self.assertEqual(self.verify(rec(), lambda n: pr(), files=lambda n: {'brain/records/decisions.jsonl'}), [])

    def test_states(self):
        cases = {'accepted': pr(), 'pending': pr(merged=False), 'unverified': None,
                 'invalid': pr(merged=False, state='closed')}
        for want, answer in cases.items():
            r = rec(evidence_refs=[EVIDENCE])
            got = core.authority(rows(r), fetch=lambda n: answer, files=CHANGED, added=own_pr(r))['DEC-x'][0]
            self.assertEqual(got, want)


class PendingDecisions(unittest.TestCase):
    """A decision whose PR is not merged is shown as pending and changes nothing until the owner merges it."""

    OLD = rec(id='DEC-old', authority_ref='pr:#1', statement='old rule', evidence_refs=[EVIDENCE])
    NEW = rec(id='DEC-new', authority_ref='pr:#2', statement='new rule', supersedes='DEC-old', evidence_refs=[EVIDENCE])

    def status(self, *records, answers, added=None):
        return core.status(rows(*records), today='2026-10-30', online=False, fetch=lambda n: answers.get(n), files=CHANGED,
                           added=added or own_pr(*records))

    @staticmethod
    def section(out, title):
        return out.split('## ' + title, 1)[1].split('\n## ', 1)[0] if '## ' + title in out else ''

    def test_pending_is_not_current(self):
        out = self.status(rec(id='DEC-p', authority_ref='pr:#2', evidence_refs=[EVIDENCE]), answers={2: pr(merged=False)})
        self.assertNotIn('DEC', self.section(out, 'Current decisions'))
        self.assertIn('pr:#2', self.section(out, 'Pending decisions'))

    def test_pending_replacement_keeps_accepted_decision_current(self):
        out = self.status(self.OLD, self.NEW, answers={1: pr(), 2: pr(merged=False)})
        self.assertIn('old rule', self.section(out, 'Current decisions'))
        self.assertNotIn('new rule', self.section(out, 'Current decisions'))
        self.assertIn('new rule (would replace DEC-old)', self.section(out, 'Pending decisions'))

    def test_merged_replacement_takes_over(self):
        out = self.status(self.OLD, self.NEW, answers={1: pr(), 2: pr()})
        self.assertIn('new rule', self.section(out, 'Current decisions'))
        self.assertNotIn('old rule', out)

    def test_closed_or_foreign_merge_is_a_problem_not_a_decision(self):
        for answer in (pr(merged=False, state='closed'), pr(by='someone-else')):
            out = self.status(self.OLD, answers={1: answer})
            self.assertNotIn('old rule', self.section(out, 'Current decisions'))
            self.assertIn('old rule', self.section(out, 'Decision problems'))

    def test_unreachable_github_confirms_nothing(self):
        out = self.status(self.OLD, answers={})
        self.assertNotIn('old rule', self.section(out, 'Current decisions'))
        self.assertIn('old rule', self.section(out, 'Decisions not verified'))
        offline = core.status(rows(self.OLD), today='2026-10-30', online=False)
        self.assertIn('none is confirmed as the owner', offline)

    def test_observation_or_request_cannot_revoke_a_decision(self):
        for kind in ('OBSERVED', 'CHANGE_REQUESTED'):
            other = rec(id='OBS-x', kind=kind, statement='a note', supersedes='DEC-old')
            del other['authority_ref']
            out = self.status(self.OLD, other, answers={1: pr()})
            self.assertIn('old rule', self.section(out, 'Current decisions'), kind)
            self.assertIn('DEC-old', [r['id'] for r in core.current(rows(self.OLD, other))], kind)
            self.assertTrue(any('only a decision can replace a decision' in e for e in core.problems(rows(self.OLD, other))), kind)

    def test_observation_may_still_supersede_an_observation(self):
        first = rec(id='FND-a', kind='OBSERVED', statement='first')
        second = rec(id='FND-b', kind='OBSERVED', statement='second', supersedes='FND-a')
        for r in (first, second):
            del r['authority_ref']
        self.assertEqual([r['id'] for r in core.current(rows(first, second))], ['FND-b'])
        self.assertEqual(core.problems(rows(first, second)), [])

    def test_validate_without_authority_still_accepts_own_pending_records(self):
        # The PR check runs `validate` without --verify-authority, so a decision PR can pass before its own merge.
        self.assertEqual(core.problems(rows(self.OLD, self.NEW)), [])


class Hardening(unittest.TestCase):
    """2026-10-30 audit: attacks reproduced against PR #51, each pinned by a test."""

    A = rec(id='A', authority_ref='pr:#1', statement='rule A', evidence_refs=[EVIDENCE])
    B = rec(id='B', authority_ref='pr:#2', statement='rule B', supersedes='A', evidence_refs=[EVIDENCE])
    C = rec(id='C', authority_ref='pr:#3', statement='rule C', supersedes='B', evidence_refs=[EVIDENCE])
    section = staticmethod(PendingDecisions.section)

    def status(self, *records, answers, added=None, files=CHANGED, today='2026-10-30'):
        return core.status(rows(*records), today=today, online=False, fetch=lambda n: answers.get(n), files=files,
                           added=added or own_pr(*records))

    def test_branch_record_cannot_borrow_an_old_merge(self):
        # A record added on a branch that cites an old, owner-merged PR whose files match its evidence.
        fake = rec(id='DEC-fake', authority_ref='pr:#50', statement='agents may spend freely', evidence_refs=[EVIDENCE])
        out = self.status(fake, answers={50: pr()}, added=lambda rid: 'branch')
        self.assertNotIn('spend freely', self.section(out, 'Current decisions'))
        self.assertIn('exists only on this branch', self.section(out, 'Pending decisions'))
        self.assertTrue(core.verify_authority(rows(fake), fetch=lambda n: pr(), files=CHANGED, added=lambda rid: 'branch'))

    def test_record_added_by_a_later_owner_merged_pr_counts(self):
        # Backfilled records (decided in #31, recorded in #36) stay valid; a non-owner or unknown adder does not.
        r = rec(id='DEC-l', authority_ref='pr:#31', evidence_refs=[EVIDENCE])
        ok = core.authority(rows(r), fetch=lambda n: pr(), files=CHANGED, added=lambda rid: 36)
        self.assertEqual(ok['DEC-l'][0], 'accepted')
        foreign = core.authority(rows(r), fetch=lambda n: pr(by='someone-else') if n == 36 else pr(), files=CHANGED, added=lambda rid: 36)
        self.assertEqual(foreign['DEC-l'][0], 'invalid')
        self.assertEqual(core.authority(rows(r), fetch=lambda n: pr(), files=CHANGED, added=lambda rid: 'unknown')['DEC-l'][0], 'invalid')
        self.assertEqual(core.authority(rows(r), fetch=lambda n: pr(), files=CHANGED, added=lambda rid: None)['DEC-l'][0], 'unverified')

    def test_chain_with_a_middle_link_not_in_force_does_not_revive_the_oldest(self):
        for middle in (pr(merged=False), pr(merged=False, state='closed')):
            out = self.status(self.A, self.B, self.C, answers={1: pr(), 2: middle, 3: pr()})
            current = self.section(out, 'Current decisions')
            self.assertIn('rule C', current)
            self.assertNotIn('rule A', current)
            self.assertIn('superseded by C, which is in force', out)
        errs = core.verify_authority(rows(self.A, self.B, self.C), fetch=lambda n: pr(merged=n != 2), files=CHANGED,
                                     added=own_pr(self.A, self.B, self.C))
        self.assertTrue(any(e.startswith('B:') for e in errs), errs)

    def test_cycles_and_self_supersession_fail(self):
        x = rec(id='X', supersedes='Y')
        y = rec(id='Y', supersedes='X', subject='t')
        self.assertTrue(any('cycle' in e for e in core.problems(rows(x, y))))
        self.assertTrue(any('supersedes itself' in e for e in core.problems(rows(rec(id='S', supersedes='S')))))

    def test_unverified_replacement_does_not_leave_the_old_decision_confirmed(self):
        new = rec(id='NEW', authority_ref='pr:#2', statement='rule new', supersedes='A', evidence_refs=[EVIDENCE])
        out = self.status(self.A, new, answers={1: pr()})
        self.assertNotIn('rule A', self.section(out, 'Current decisions'))
        self.assertIn('may be superseded by NEW', self.section(out, 'Decisions not verified'))

    def test_duplicate_id_counts_for_neither_copy(self):
        first = rec(id='X', authority_ref='pr:#2', statement='PENDING rule', subject='other', evidence_refs=[EVIDENCE])
        second = rec(id='X', authority_ref='pr:#1', statement='merged rule', evidence_refs=[EVIDENCE])
        out = self.status(first, second, answers={1: pr(), 2: pr(merged=False)}, added=lambda rid: 1)
        self.assertNotIn('rule', self.section(out, 'Current decisions'))
        self.assertIn('duplicate id', self.section(out, 'Decision problems'))

    def test_malformed_lines_are_reported_not_crashing(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / 'decisions.jsonl').write_text('[]\n"text"\nnull\n5\n', encoding='utf-8')
            loaded = core.load(d)
        self.assertEqual(len(loaded), 4)
        self.assertEqual(len([e for e in core.problems(loaded) if 'not valid JSON' in e]), 4)
        listed = rows(rec(id=['x']), rec(id='Q', supersedes=['A']))
        self.assertEqual(len([e for e in core.problems(listed) if 'must be text' in e]), 2)
        bare = rec(id='N')
        del bare['statement']
        core.status(rows(bare), today='2026-10-30', online=False)
        core.status(rows(bare), today='2026-10-30', online=False, fetch=lambda n: pr(), files=CHANGED, added=own_pr(bare))

    def test_due_reviews_listed_when_github_is_unreachable(self):
        r = rec(id='R', review_by='2026-01-01', evidence_refs=[EVIDENCE])
        out = self.status(r, answers={})
        self.assertIn('R (review_by 2026-01-01) [unverified]', self.section(out, 'Due for review'))

    def test_malformed_authority_is_a_problem(self):
        r = rec(id='M', authority_ref='PR #5', statement='odd rule', evidence_refs=[EVIDENCE])
        out = self.status(r, answers={})
        self.assertIn('odd rule', self.section(out, 'Decision problems'))
        self.assertTrue(core.verify_authority(rows(r), fetch=lambda n: pr(), files=CHANGED, added=lambda rid: 1))

    def test_subjects_compare_without_case(self):
        errs = core.problems(rows(rec(id='U1', subject='Container'), rec(id='U2', subject='container ')))
        self.assertTrue(any('contradiction' in e for e in errs), errs)

    def test_evidence_paths_normalized_and_directories_match(self):
        self.assertTrue(any('repo-relative' in e for e in core.problems(rows(rec(evidence_refs=['./brain/CONTRACT.md'])))))
        r = rec(id='D', evidence_refs=['brain'])
        got = core.authority(rows(r), fetch=lambda n: pr(), files=lambda n: {'brain/CONTRACT.md'}, added=own_pr(r))
        self.assertEqual(got['D'][0], 'accepted')

    def test_cli_rejects_a_missing_records_folder(self):
        out = subprocess.run([sys.executable, '-m', 'brain', 'validate', '--records', '/nonexistent-brain-records'],
                             cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(out.returncode, 1)
        self.assertIn('is not a folder', out.stdout)


class Status(unittest.TestCase):
    def test_status_offline_lists_decisions_and_due_reviews(self):
        out = core.status(rows(rec(review_by='2026-01-01')), today='2026-10-30', online=False)
        self.assertIn('## Decisions (not verified', out)
        self.assertIn('DEC-x (review_by 2026-01-01)', out)
        self.assertIn('GitHub not reachable', out)

    def test_review_only_fixes_are_listed_apart(self):
        # A fix checked by document review only must not read as guarded by a test.
        f = dict(rec(id='FND-r', kind='OBSERVED', subject='finding.r', finding_status='FIXED', test_ref='paper'))
        del f['authority_ref']
        out = core.status(rows(f, file='findings.jsonl'), today='2026-10-30', online=False)
        self.assertIn('verified by review only (no automated guard): FND-r', out)

    def test_benchmark_checks_parsed(self):
        self.assertTrue(any(c['id'] == 'C1' for c in core.benchmark_checks()))

    def test_gates_file_shape(self):
        gates = json.loads(core.GATES.read_text())['gates']
        self.assertTrue(all(g['status'] in ('live', 'paper', 'waived') for g in gates))
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
