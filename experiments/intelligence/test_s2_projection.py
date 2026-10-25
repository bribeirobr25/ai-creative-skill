"""Cross-stage S2 -> S3 projection tests, synthetic-only."""
import copy
import unittest

from experiments.intelligence.contract_canary import ContractViolation, validate_query_filter
from experiments.intelligence.s2_projection import project_s2_query
from experiments.intelligence.policy_gate import InvalidContract, evaluate
from experiments.intelligence.test_policy_gate import capability

NOW = "2026-10-23T15:00:00+00:00"


def s2_query():
    return {
        "operation": "PUBLIC_VIDEO_SEARCH",
        "platforms": ["fixture-platform"],
        "geographic_filter": {
            "code": "DE", "meaning": "SEARCH_RESULT_LOCALE",
            "level": "COUNTRY",
        },
        "time_filter": {
            "start_inclusive": "2026-10-01", "end_exclusive": "2026-10-24",
            "meaning": "PUBLISHED_DURING_WINDOW", "timezone": "Europe/Berlin",
        },
        "ranking": {"metric": "PUBLIC_VIEW_COUNT", "limit": 10},
    }


def project(q=None, **kwargs):
    opt = {"project_id": "fixture-project", "purpose": "RESEARCH_ONLY",
           "fields": ["viewCount"], "transformations": ["DISPLAY_NATIVE"]}
    opt.update(kwargs)
    return project_s2_query(q or s2_query(), **opt)


class S2S3CompatibilityTests(unittest.TestCase):
    def test_s2_query_valid_before_mapping(self):
        validate_query_filter(s2_query())

    def test_mapping_preserves_platform_country_geo_time_and_exact_window(self):
        q = s2_query()
        p = project(q)
        self.assertEqual(q["platforms"][0], p["platform"])
        self.assertEqual(q["geographic_filter"]["code"], p["country"])
        self.assertEqual(q["geographic_filter"]["meaning"], p["geography_basis"])
        self.assertEqual(q["time_filter"]["meaning"], p["time_basis"])
        self.assertEqual(q["time_filter"]["start_inclusive"], p["window_start"])
        self.assertEqual(q["time_filter"]["end_exclusive"], p["window_end"])
        self.assertEqual("RESEARCH_ONLY", p["purpose"])

    def test_mapping_does_not_inherit_source_permission(self):
        p = project()
        r = evaluate(p, capability(), now=NOW)
        self.assertEqual("SHAPE_CHECK_PASSED_SYNTHETIC_ONLY", r["decision"])
        self.assertFalse(r["may_access_real_source"])
        self.assertFalse(r["may_spend"])

    def test_multiplatform_requires_separate_permission_evaluation(self):
        q = s2_query()
        q["platforms"].append("another-platform")
        with self.assertRaises(InvalidContract):
            project(q)

    def test_original_s2_invalid_query_cannot_skip_validation(self):
        q = s2_query()
        q["ranking"]["limit"] = True
        with self.assertRaises(ContractViolation):
            project(q)

    def test_audience_geo_cannot_fall_back_to_search_locale(self):
        q = s2_query()
        q["geographic_filter"]["meaning"] = "AUDIENCE_GEO"
        p = project(q)
        r = evaluate(p, capability(), now=NOW)
        self.assertIn("GEOGRAPHY_SEMANTICS_MISMATCH", r["reason_codes"])

    def test_time_meaning_not_silently_substituted(self):
        q = s2_query()
        q["time_filter"]["meaning"] = "ENGAGEMENT_GAINED_DURING_WINDOW"
        p = project(q)
        r = evaluate(p, capability(), now=NOW)
        self.assertIn("TIME_SEMANTICS_MISMATCH", r["reason_codes"])

    def test_date_window_outside_source_scope_is_blocked(self):
        q = s2_query()
        q["time_filter"]["start_inclusive"] = "2025-10-01"
        p = project(q)
        r = evaluate(p, capability(), now=NOW)
        self.assertIn("TIME_WINDOW_OUTSIDE_DECLARED_SCOPE", r["reason_codes"])

    def test_projected_paid_request_cannot_trigger_spend(self):
        p = project(requires_paid=True)
        r = evaluate(p, capability(), now=NOW)
        self.assertIn("PAID_RESEARCH_NOT_ENABLED_IN_S3", r["reason_codes"])
        self.assertFalse(r["may_spend"])

    def test_projected_persistence_denied_beyond_fixture_ttl(self):
        p = project(storage_mode="PERSIST", retention_days=8)
        r = evaluate(p, capability(), now=NOW)
        self.assertIn("FIELD_PERSISTENCE_NOT_GRANTED", r["reason_codes"])

    def test_query_input_remains_unmodified(self):
        q = s2_query()
        before = copy.deepcopy(q)
        project(q)
        self.assertEqual(before, q)


if __name__ == "__main__":
    unittest.main()


class RedistributionIntentTests(unittest.TestCase):
    def test_explicit_redistribution_reaches_preflight(self):
        from experiments.intelligence.policy_gate import evaluate
        from experiments.intelligence.test_policy_gate import capability
        q = s2_query()
        base = dict(project_id="fixture-project", purpose="RESEARCH_ONLY",
                    fields=["viewCount"], transformations=["DISPLAY_NATIVE"])
        private = project_s2_query(q, **base)
        sharing = project_s2_query(q, redistribute_output=True, **base)
        self.assertIs(private["redistribute_output"], False)
        self.assertIs(sharing["redistribute_output"], True)
        c = capability()
        c["field_grants"]["viewCount"]["actions"] = ["READ", "PROCESS"]
        out = evaluate(sharing, c, now="2026-10-23T15:00:00+00:00")
        self.assertEqual("BLOCKED", out["decision"])
        self.assertIn("FIELD_REDISTRIBUTION_NOT_GRANTED", out["reason_codes"])
        out_private = evaluate(private, c, now="2026-10-23T15:00:00+00:00")
        self.assertNotIn("FIELD_REDISTRIBUTION_NOT_GRANTED", out_private["reason_codes"])
