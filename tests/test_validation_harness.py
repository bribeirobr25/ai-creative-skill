"""Regressions against actual helpers and sanity controls for the test machinery."""
import json
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
from validation import harness as h, invariants
from validation.generators.pairwise import generate, coverage
from validation.simulations.economics import Assumptions, simulate, STRATEGIES

class HarnessTests(unittest.TestCase):
    def test_canonical_helper_regression_baseline(self):
        known=h.expectations('candidate')
        records=h.run()
        expected=[id for id,g in known['expected_record_groups'].items() if g not in (*h.HOST_GROUPS,'journey')]
        review=h.expectation_errors(records,known['expected_failures'],known['actual_signatures'],expected)
        self.assertFalse(any(review.values()),review)
        self.assertTrue(all(r['outcome']=='PASS' for r in records),'Candidate regressions must pass; historical FAILs remain in immutable reports')

    def test_publication_oracle(self):
        invariants.publication_requires_authority(h.router)

    def test_payment_oracle(self):
        with tempfile.TemporaryDirectory() as td:
            req=h.image_fixture(Path(td))
            invariants.paid_request_is_rejected(h.media,req.source)

    def test_shape_oracle(self):
        invariants.missing_fields_are_rejected(h.shape)

    def test_pairwise_is_complete_deterministic_and_smaller(self):
        domains={c:[False,True] for c in 'abcdef'}
        rows=generate(domains)
        self.assertEqual(rows,generate(domains))
        self.assertEqual(coverage(domains,rows)['missing_pairs'],0)
        self.assertLess(len(rows),64)

    def test_new_failure_is_not_waived(self):
        r=[{'id':'new','actual':[],'outcome':'FAIL'}]
        self.assertEqual(h.expectation_errors(r,['known'])['unexpected_failures'],['new'])

    def test_fixed_failure_requires_baseline_review(self):
        r=[{'id':'known','outcome':'PASS'}]
        self.assertEqual(h.expectation_errors(r,['known'])['resolved_findings_need_review'],['known'])

    def test_changed_symptom_and_missing_probe_are_not_waived(self):
        r=[{'id':'known','outcome':'FAIL','actual':'different'}]
        review=h.expectation_errors(r,['known'],{'known':'original'},['known','missing'])
        self.assertEqual(review['changed_failure_evidence'],['known'])
        self.assertEqual(review['missing_records'],['missing'])

    def test_blocked_environment_never_passes_ci(self):
        review=h.expectation_errors([{'id':'ffmpeg','outcome':'BLOCKED'}],[])
        self.assertEqual(review['blocked'],['ffmpeg'])

    def test_simulation_reproducible_and_budget_bounded(self):
        a=Assumptions(trials=100,budget_cents=180)
        for strategy in STRATEGIES:
            first=simulate(a,strategy)
            self.assertEqual(first,simulate(a,strategy))
            self.assertEqual(first['budget_overrun_count'],0)
            self.assertLessEqual(first['cash_quantiles_usd']['0.95'],1.8)

    def test_zero_budget_blocks_commercial_attempts(self):
        r=simulate(Assumptions(trials=100,budget_cents=0),'commercial_only')
        self.assertEqual(r['accepted'],0)
        self.assertEqual(r['mean_reserved_cash_usd'],0)
        self.assertIsNone(r['cash_per_accepted_asset_including_failed_jobs_usd'])

    def test_unknown_stops_before_any_retry(self):
        a=Assumptions(trials=100,availability=1,uncertain_outcome=1)
        r=simulate(a,'commercial_only')
        self.assertEqual(r['stops']['UNKNOWN_RECONCILE'],100)
        self.assertEqual(r['mean_attempts'],1)
        self.assertEqual(r['accepted'],0)

    def test_perfect_acceptance_and_complete_rejection(self):
        a=Assumptions(trials=100,availability=1,technical_success=1,uncertain_outcome=0,local_acceptance=1,human_intervention=0)
        r=simulate(a,'local_only')
        self.assertEqual(r['accepted'],100)
        self.assertEqual(r['time_to_acceptance_minutes_conditional_on_acceptance']['0.5'],4)
        r=simulate(replace(a,local_acceptance=0),'local_only')
        self.assertEqual(r['accepted'],0)
        self.assertIsNone(r['time_to_acceptance_minutes_conditional_on_acceptance']['0.5'])

    def test_invalid_probability_rejected(self):
        with self.assertRaises(ValueError):simulate(Assumptions(availability=float('nan')),'local_only')

if __name__=='__main__':unittest.main()
