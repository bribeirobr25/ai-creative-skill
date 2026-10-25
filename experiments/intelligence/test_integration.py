"""Cross-module regression: metric engine → research envelope → S2 → S3."""
import copy
import unittest
from datetime import datetime, date, timedelta, timezone
from zoneinfo import ZoneInfo

from experiments.intelligence.engine import Observation, ValidationError, view_velocity
from experiments.intelligence.research_bridge import build_research_execution_fixture
from experiments.intelligence.contract_canary import validate_research_execution
from experiments.intelligence.s2_projection import project_s2_query
from experiments.intelligence.policy_gate import evaluate
from experiments.intelligence.test_policy_gate import capability
from experiments.intelligence.test_research_bridge import fixture_policy
from experiments.intelligence.test_s2_projection import s2_query

UTC = timezone.utc
AT = datetime(2026, 10, 24, 11, tzinfo=UTC)


def row(name="one", count=100):
    return Observation(
        publication_id=("fixture-" + name if not name.startswith("fixture-") else name),
        channel_id="fixture-channel",
        platform="fixture-platform", content_type="long",
        views=count, observed_at=AT,
        published_at=AT-timedelta(days=2), source_kind="SYNTHETIC_FIXTURE",
    )


def envelope(outcome="OK", rows=None, **kwargs):
    return build_research_execution_fixture(
        research_execution_id="fixture-research-01",
        research_intent="MARKET_SCAN", primary_entity="fictional-thing",
        market="DE", language="de", range_from=date(2026,10,1),
        range_to=date(2026,10,26), generated_at=AT+timedelta(seconds=1),
        observation_rows=rows if rows is not None else [row()],
        source_outcome=outcome,
        policy_decision=kwargs.pop("policy_decision", fixture_policy()),
        time_zone=kwargs.pop("time_zone", "UTC"),
        ranking_requested=kwargs.pop("ranking_requested", True), **kwargs,
    )


class CrossModuleTests(unittest.TestCase):
    def test_actual_bridge_shape_validated_by_s2(self):
        result=envelope()
        validate_research_execution(result, evidence_by_id=result["fixture_evidence_index"])
        self.assertEqual("COMPLETE",result["status"])
        self.assertEqual(1,len(result["evidence_clusters"]))
        self.assertNotIn("evidence_id", result["evidence_clusters"][0])

    def test_negative_absence_and_auth_failure_through_s2(self):
        for result in (
            envelope("NO_RESULTS", [], negative_coverage_satisfies_request=True, source_coverage_verified=True),
            envelope("AUTH_FAILED", [])
        ):
            with self.subTest(status=result["status"]):
                validate_research_execution(result, evidence_by_id=result["fixture_evidence_index"])

    def test_metric_and_source_ref_equal_the_canonical_evidence(self):
        e=envelope()
        ref=next(iter(e["fixture_evidence_index"]))
        metric=e["intelligence"]["metric_observations"][0]
        self.assertEqual(ref,metric["evidence_id"])
        self.assertEqual(e["fixture_evidence_index"][ref]["source_outcome_ref"],metric["source_outcome_ref"])

    def test_dst_fall_back_actual_elapsed_and_velocity(self):
        local=ZoneInfo("Europe/Berlin")
        # Noon on consecutive local dates around the 2026 autumn transition.
        first=datetime(2026,10,24,12,tzinfo=local)
        second=datetime(2026,10,25,12,tzinfo=local)
        self.assertEqual(25,(second.astimezone(UTC)-first.astimezone(UTC)).total_seconds()/3600)
        old=Observation("fixture-v","fixture-c","fixture-platform","long",100,first,first-timedelta(days=1),"SYNTHETIC_FIXTURE")
        new=Observation("v","fixture-c","fixture-platform","long",150,second,first-timedelta(days=1),"SYNTHETIC_FIXTURE")
        self.assertEqual(25,(new.observed_at-old.observed_at).total_seconds()/3600)
        self.assertAlmostEqual(2,view_velocity(old,new,derived_permission=True)["views_per_hour"])

    def test_spoofed_real_source_cannot_be_eligible(self):
        c=capability()
        c["source_id"]="YOUTUBE_DATA_API"
        c["source_kind"]="SYNTHETIC_FIXTURE"
        from experiments.intelligence.policy_gate import InvalidContract
        with self.assertRaises(InvalidContract):
            evaluate({
            "operation":"PUBLIC_VIDEO_SEARCH","platform":"fixture-platform",
            "project_id":"fixture-project","purpose":"RESEARCH_ONLY","country":"DE",
            "geography_basis":"SEARCH_RESULT_LOCALE","time_basis":"PUBLISHED_DURING_WINDOW",
            "window_start":"2026-10-01","window_end":"2026-10-24",
            "requested_metric":"PUBLIC_VIEW_COUNT","fields":["viewCount"],
            "transformations":["DISPLAY_NATIVE"],"storage_mode":"TRANSIENT_ONLY",
            "retention_days":0,"requires_paid":False,"requests_raw_media":False,
            "background_collection":False,"estimated_calls":1,
            },c,now="2026-10-23T15:00:00Z")

    def test_derived_metric_cannot_be_hidden_by_native_display_transform(self):
        q=s2_query()
        q["ranking"]["metric"]="DERIVED_OUTLIER_SCORE"
        req=project_s2_query(q,project_id="fixture-project",purpose="RESEARCH_ONLY",
                             fields=["viewCount"],transformations=["DISPLAY_NATIVE"])
        out=evaluate(req,capability(),now="2026-10-23T15:00:00Z")
        self.assertEqual("BLOCKED",out["decision"])
        self.assertIn("DERIVED_METRIC_REQUIRES_EXPLICIT_TRANSFORM",out["reason_codes"])

    def test_no_source_permission_propagated_via_intelligence(self):
        env=envelope()
        env["intelligence"]["may_spend"]=True
        from experiments.intelligence.contract_canary import ContractViolation
        with self.assertRaises(ContractViolation):
            validate_research_execution(env,evidence_by_id=env["fixture_evidence_index"])


if __name__=="__main__":
    unittest.main()
