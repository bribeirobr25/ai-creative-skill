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


    def test_forged_policy_pass_with_blocking_reasons_is_not_accepted(self):
        p=fixture_policy()
        p["reason_codes"]=["POLICY_NOT_CURRENT"]
        with self.assertRaises(ValidationError):
            research_request(policy_decision=p)
        p=fixture_policy()
        p["rights_scope"]="REAL_SOURCE_GRANTED"
        with self.assertRaises(ValidationError):
            research_request(policy_decision=p)

    def test_complete_research_without_explicit_policy_decision_rejected(self):
        e=research_request()
        del e["intelligence"]["policy_shape_decision"]
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=e["fixture_evidence_index"])

    def test_official_source_outcome_in_synthetic_execution_rejected(self):
        e=research_request()
        e["source_outcomes"][0]["source_class"]="OFFICIAL_API"
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=e["fixture_evidence_index"])

    def test_invented_stop_code_rejected(self):
        e=research_request()
        e["intelligence"]["stop_code"]="STOP_INVENTED_OK"
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=e["fixture_evidence_index"])

    def test_real_provider_short_urls_cannot_be_evidence(self):
        e=research_request()
        eid=next(iter(e["fixture_evidence_index"]))
        for source in ("//youtube.com/watch?v=x", "https://youtu.be/x",
                       "https://tiktok.com/@creator/video/1"):
            e["fixture_evidence_index"][eid]["source_ref"]=source
            with self.subTest(source=source), self.assertRaises(ContractViolation):
                validate_research_execution(e, evidence_by_id=e["fixture_evidence_index"])

    def test_derived_operation_always_requires_derivation_right(self):
        c=capability(operation="DERIVED_ANALYTICS")
        q=policy_request(operation="DERIVED_ANALYTICS",
                         transformations=["DISPLAY_NATIVE"])
        d=evaluate(q,c,now="2026-10-23T15:00:00+00:00")
        self.assertEqual("BLOCKED",d["decision"])
        self.assertIn("DERIVED_OPERATION_REQUIRES_DERIVATION",d["reason_codes"])

    def test_unauthorized_fields_rejected_in_nested_contracts(self):
        e=research_request()
        e["coverage"]["may_publish"]=True
        with self.assertRaises(ContractViolation):
            validate_research_execution(e,evidence_by_id=e["fixture_evidence_index"])
        c=capability()
        c["allowed_project_ids"]=["fixture-project"]
        with self.assertRaises(InvalidContract):
            validate_capability(c)
        c=capability()
        c["field_grants"]["viewCount"]["approval_ref"]="claimed"
        with self.assertRaises(InvalidContract):
            validate_capability(c)

    def test_metric_claimed_derived_but_not_performed_is_rejected(self):
        e=research_request()
        e["intelligence"]["metric_observations"][0]["metric_name"]="OUTLIER_RATIO"
        with self.assertRaises(ContractViolation):
            validate_research_execution(e,evidence_by_id=e["fixture_evidence_index"])


    def test_local_berlin_publication_window_is_not_utc_window(self):
        from datetime import date, datetime
        from zoneinfo import ZoneInfo
        berlin=ZoneInfo("Europe/Berlin")
        pub=datetime(2026,10,25,0,30,tzinfo=berlin)
        seen=datetime(2026,10,25,3,30,tzinfo=berlin)
        row=Observation(
            publication_id="local-first-hour",channel_id="fixture-creator",
            platform="fixture-synthetic",content_type="long",views=40,
            observed_at=seen,published_at=pub,source_kind="SYNTHETIC_FIXTURE"
        )
        request_args=dict(
            range_from=date(2026,10,25),range_to=date(2026,10,26),
            observation_rows=[row],generated_at=datetime(2026,10,25,5,tzinfo=berlin),
        )
        valid=research_request(**request_args,time_zone="Europe/Berlin")
        self.assertEqual("COMPLETE",valid["status"])
        self.assertEqual("Europe/Berlin",valid["intelligence"]["time_zone"])
        with self.assertRaises(ValidationError):
            research_request(**request_args,time_zone="UTC")

    def test_bridge_rejects_metric_it_does_not_implement(self):
        with self.assertRaises(ValidationError):
            research_request(requested_metric="OUTLIER_RATIO")

    def test_preflight_rejects_unverified_timezone_and_source_result_limit(self):
        c=capability(max_results_per_call=5,
                     supported_time_zones=["UTC"])
        q=policy_request(time_zone="Europe/Berlin",result_limit=20)
        d=evaluate(q,c,now="2026-10-23T15:00:00+00:00")
        self.assertEqual("BLOCKED",d["decision"])
        self.assertIn("SOURCE_TIME_ZONE_UNVERIFIED",d["reason_codes"])
        self.assertIn("SOURCE_RESULT_LIMIT_UNVERIFIED",d["reason_codes"])

    def test_date_overflow_fails_as_contract_violation(self):
        from experiments.intelligence.policy_gate import retention_verdict
        with self.assertRaises(InvalidContract):
            retention_verdict(recorded_at="9999-12-31T00:00:00+00:00",
                              ttl_days=30,now="9999-12-31T00:00:00+00:00")


if __name__=="__main__":
    unittest.main()
