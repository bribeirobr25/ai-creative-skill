"""CC adversarial regressions, not provider permission or production API tests."""
import copy
import unittest
from dataclasses import replace
from experiments.intelligence.engine import Observation, ValidationError, rank_sample
from experiments.intelligence.policy_gate import evaluate, validate_capability, InvalidContract
from experiments.intelligence.research_bridge import build_research_execution_fixture
from experiments.intelligence.contract_canary import validate_research_execution, ContractViolation
from experiments.intelligence.test_policy_gate import request as policy_request, capability
from experiments.intelligence.test_research_bridge import request as research_request, synthetic_row, fixture_policy


def synthetic_grant():
    return fixture_policy()


class AdversarialFixes(unittest.TestCase):
    def test_real_source_names_and_unicode_confusables_never_become_fixtures(self):
        for name in ("youtube", "YouTube Shorts", "yt", "yоutube", "ＹｏｕＴｕｂｅ", "meta", "facebook"):
            with self.subTest(value=name):
                with self.assertRaises(ValidationError):
                    synthetic_row(platform=name)
                c=capability()
                c["platform"]=name
                with self.assertRaises(InvalidContract):
                    validate_capability(c)

    def test_provider_documentation_cannot_be_relabelled_to_fake_fixture(self):
        from experiments.intelligence.provider_templates import unverified_capability_template
        c=unverified_capability_template("YOUTUBE_DERIVED_ANALYTICS")
        c.update(source_id="fixture-youtube-data-api", platform="fixture-provider",
                 source_kind="SYNTHETIC_FIXTURE",
                 authorization_state="SIMULATED_VERIFIED")
        with self.assertRaises(InvalidContract):
            validate_capability(c)

    def test_derived_metric_synonyms_not_display_native(self):
        for name in ("ENGAGEMENT_RATE", "outlier_ratio", "VIEW_VELOCITY", "DERIVED_OUTLIER_SCORE"):
            c=capability()
            c["documented_metric_support"].append(name)
            q=policy_request(requested_metric=name, transformations=["DISPLAY_NATIVE"])
            out=evaluate(q,c,now="2026-10-23T15:00:00+00:00")
            self.assertEqual("BLOCKED",out["decision"])
            self.assertIn("DERIVED_METRIC_REQUIRES_EXPLICIT_TRANSFORM",out["reason_codes"])

    def test_unverified_century_retention_of_titles_and_comments_is_rejected(self):
        for kind in ("TITLE", "COMMENT", "DESCRIPTION", "STATISTICS"):
            c=capability()
            c["field_grants"]["viewCount"]["data_class"]=kind
            c["field_grants"]["viewCount"]["max_retention_days"]=36500
            with self.subTest(kind=kind), self.assertRaises(InvalidContract):
                validate_capability(c)

    def test_blocked_policy_cannot_become_successful_research(self):
        p=synthetic_grant()
        p=fixture_policy(blocked=True)
        result=research_request(policy_decision=p, observation_rows=[],
                                source_outcome="OK")
        self.assertEqual("BLOCKED",result["status"])
        self.assertEqual("SKIPPED_UNCONFIGURED",result["source_outcomes"][0]["outcome"])
        self.assertEqual("STOP_POLICY_REJECTION",result["intelligence"]["stop_code"])
        validate_research_execution(result,evidence_by_id=result["fixture_evidence_index"])

    def test_blocked_policy_cannot_use_old_source_observations(self):
        p=synthetic_grant()
        p=fixture_policy(blocked=True)
        with self.assertRaises(ValidationError):
            research_request(policy_decision=p)

    def test_non_national_partial_source_must_never_claim_complete_ranking(self):
        for outcome in ("PARTIAL", "RATE_LIMITED", "TIMEOUT"):
            result=research_request(source_outcome=outcome,
                                     population_coverage_verified=True,
                                     source_coverage_verified=True)
            self.assertNotEqual("COMPLETE", result["intelligence"]["ranking_scope"])
            self.assertEqual("PARTIAL", result["status"])
            validate_research_execution(result,evidence_by_id=result["fixture_evidence_index"])

    def test_complete_result_without_clusters_or_metrics_is_rejected(self):
        result=research_request()
        result["evidence_clusters"]=[]
        result["intelligence"]["metric_observations"]=[]
        result["intelligence"]["ranked_evidence_refs"]=[]
        with self.assertRaises(ContractViolation):
            validate_research_execution(result,evidence_by_id=result["fixture_evidence_index"])

    def test_blocked_research_with_successful_evidence_rejected(self):
        result=research_request()
        result["status"]="BLOCKED"
        with self.assertRaises(ContractViolation):
            validate_research_execution(result,evidence_by_id=result["fixture_evidence_index"])

    def test_real_provider_urls_not_allowed_as_fixture_evidence(self):
        result=research_request()
        eid=next(iter(result["fixture_evidence_index"]))
        result["fixture_evidence_index"][eid]["source_ref"]="https://www.youtube.com/watch?v=some-id"
        with self.assertRaises(ContractViolation):
            validate_research_execution(result,evidence_by_id=result["fixture_evidence_index"])

    def test_ranking_coverage_flags_are_exact_bools(self):
        with self.assertRaises(ValidationError):
            rank_sample([synthetic_row()],limit=1,population_coverage_verified="no")
        with self.assertRaises(ValidationError):
            rank_sample([synthetic_row()],limit=1,requested_national_top=1)


if __name__=="__main__":
    unittest.main()
