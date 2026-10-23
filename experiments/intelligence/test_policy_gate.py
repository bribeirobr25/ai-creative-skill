"""S3 offline policy canary regression tests. No external data or credentials."""
import copy
import unittest
from datetime import datetime, timedelta, timezone

from intelligence.policy_gate import (
    InvalidContract, evaluate, retention_verdict, validate_capability,
    validate_request,
)

NOW = "2026-10-23T15:00:00+00:00"


def request(**changes):
    data = {
        "operation": "PUBLIC_VIDEO_SEARCH", "platform": "fixture-platform",
        "project_id": "fixture-project", "purpose": "RESEARCH_ONLY",
        "country": "DE", "geography_basis": "SEARCH_RESULT_LOCALE",
        "time_basis": "PUBLISHED_DURING_WINDOW",
        "requested_metric": "PUBLIC_VIEW_COUNT",
        "window_start": "2026-10-01", "window_end": "2026-10-24",
        "fields": ["viewCount"], "transformations": ["DISPLAY_NATIVE"],
        "storage_mode": "TRANSIENT_ONLY", "retention_days": 0,
        "requires_paid": False, "requests_raw_media": False,
        "background_collection": False, "estimated_calls": 2,
    }
    data.update(changes)
    return data


def capability(**changes):
    data = {
        "source_id": "fixture-source-01", "source_kind": "SYNTHETIC_FIXTURE",
        "platform": "fixture-platform", "operation": "PUBLIC_VIDEO_SEARCH",
        "adapter_version": "canary-0.1", "policy_ref": "synthetic-policy-01",
        "authorization_state": "SIMULATED_VERIFIED",
        "purposes": ["RESEARCH_ONLY"],
        "countries": ["DE"], "geography_bases": ["SEARCH_RESULT_LOCALE"],
        "time_bases": ["PUBLISHED_DURING_WINDOW"],
        "transformations": ["DISPLAY_NATIVE", "DERIVE_RATIO", "SUMMARIZE"],
        "documented_metric_support": ["PUBLIC_VIEW_COUNT", "OUTLIER_RATIO"],
        "field_grants": {
            "viewCount": {
                "actions": ["READ", "PROCESS", "DERIVE", "PERSIST", "REDISTRIBUTE"],
                "max_retention_days": 7,
                "data_class": "STATISTICS",
                "retention_policy_ref": "fixture-policy",
            },
        },
        "available_from": "2026-01-01", "available_to": "2027-01-01",
        "reviewed_at": "2026-10-01T00:00:00+00:00",
        "expires_at": "2026-11-01T00:00:00+00:00",
        "revoked": False, "max_calls_per_day": 20,
    }
    data.update(changes)
    return data


def verdict(query=None, source=None, **changes):
    return evaluate(query or request(), source or capability(),
                    now=changes.get("now", NOW))


class PositiveFixtures(unittest.TestCase):
    def test_positive_simulation_is_not_real_permission(self):
        d = verdict()
        self.assertEqual("SHAPE_CHECK_PASSED_SYNTHETIC_ONLY", d["decision"])
        self.assertEqual([], d["reason_codes"])
        for field in ("may_access_real_source", "may_spend",
                      "may_store_real_data", "may_publish"):
            self.assertIs(d[field], False)
        self.assertEqual("SYNTHETIC_FIXTURE_ONLY", d["rights_scope"])

    def test_candidate_allows_synthetic_derived_ratio_only_with_field_rights(self):
        q = request(transformations=["DISPLAY_NATIVE", "DERIVE_RATIO"])
        self.assertEqual("SHAPE_CHECK_PASSED_SYNTHETIC_ONLY", verdict(query=q)["decision"])

    def test_fake_persistent_permission_never_enables_real_storage(self):
        q = request(storage_mode="PERSIST", retention_days=7)
        d = verdict(query=q)
        self.assertEqual("SHAPE_CHECK_PASSED_SYNTHETIC_ONLY", d["decision"])
        self.assertEqual(7, d["simulated_retention_days"])
        self.assertFalse(d["may_store_real_data"])

    def test_default_transient_has_no_simulated_retention(self):
        self.assertEqual(0, verdict()["simulated_retention_days"])

    def test_repeated_evaluation_has_identical_result(self):
        self.assertEqual(verdict(), verdict())
        self.assertEqual(verdict(), verdict())

    def test_json_roundtrip_preserves_meaning(self):
        import json
        self.assertEqual(verdict(), evaluate(json.loads(json.dumps(request())),
                                             json.loads(json.dumps(capability())), now=NOW))


class AuthorizationBoundary(unittest.TestCase):
    def test_official_youtube_source_never_gains_access_from_fake_grants(self):
        d = verdict(source=capability(source_kind="OFFICIAL_API"))
        self.assertEqual("BLOCKED", d["decision"])
        self.assertIn("REAL_SOURCE_NOT_AUTHORIZED", d["reason_codes"])
        self.assertFalse(d["may_access_real_source"])

    def test_licensed_provider_claim_also_denied_in_s3(self):
        d = verdict(source=capability(source_kind="LICENSED_THIRD_PARTY"))
        self.assertEqual("BLOCKED", d["decision"])

    def test_unknown_access_authorization_denied(self):
        d = verdict(source=capability(authorization_state="NOT_VERIFIED"))
        self.assertIn("ACCESS_NOT_GRANTED_FOR_FIXTURE", d["reason_codes"])

    def test_permission_claim_in_request_cannot_elevate_source(self):
        q = request()
        q["permission_granted"] = True
        d = verdict(query=q, source=capability(source_kind="OFFICIAL_API"))
        self.assertFalse(d["may_access_real_source"])

    def test_project_authority_not_decided_by_provider_descriptor(self):
        # This only validates a hypothetical source-rights shape.
        # Project Profile and AUTONOMY_ENVELOPE still must authorize usage.
        d = verdict(query=request(project_id="different"))
        self.assertEqual("SHAPE_CHECK_PASSED_SYNTHETIC_ONLY", d["decision"])
        self.assertFalse(d["may_access_real_source"])

    def test_source_descriptor_cannot_define_project_authority(self):
        c = capability()
        c["projects"] = ["fixture-project"]
        with self.assertRaises(InvalidContract):
            verdict(source=c)

    def test_purpose_not_in_scope_is_blocked(self):
        d = verdict(query=request(purpose="CREATIVE_GENERATION"))
        self.assertIn("PURPOSE_NOT_IN_SCOPE", d["reason_codes"])

    def test_operation_or_platform_mismatch(self):
        for rec in (
            capability(operation="ANOTHER_OPERATION"),
            capability(platform="different-platform"),
        ):
            with self.subTest(rec=rec["operation"]):
                self.assertIn("OPERATION_MISMATCH", verdict(source=rec)["reason_codes"])

    def test_country_and_geo_basis_cannot_substitute(self):
        d = verdict(query=request(country="BR", geography_basis="AUDIENCE_GEO"))
        self.assertIn("COUNTRY_NOT_IN_SCOPE", d["reason_codes"])
        self.assertIn("GEOGRAPHY_SEMANTICS_MISMATCH", d["reason_codes"])

    def test_time_meaning_cannot_substitute(self):
        d = verdict(query=request(time_basis="ENGAGEMENT_GAINED_DURING_WINDOW"))
        self.assertIn("TIME_SEMANTICS_MISMATCH", d["reason_codes"])

    def test_fields_must_be_explicitly_granted(self):
        d = verdict(query=request(fields=["viewCount", "ownerEmail"]))
        self.assertIn("FIELD_RIGHTS_NOT_ESTABLISHED", d["reason_codes"])

    def test_read_and_processing_required(self):
        r = capability()
        r["field_grants"]["viewCount"]["actions"] = ["READ"]
        self.assertIn("FIELD_READ_OR_PROCESS_NOT_GRANTED", verdict(source=r)["reason_codes"])

    def test_derived_transform_requires_per_field_right(self):
        r = capability()
        r["field_grants"]["viewCount"]["actions"].remove("DERIVE")
        d = verdict(query=request(transformations=["DERIVE_RATIO"]), source=r)
        self.assertIn("FIELD_DERIVATION_NOT_GRANTED", d["reason_codes"])

    def test_transform_cannot_be_invented_by_caller(self):
        r = capability(transformations=["DISPLAY_NATIVE"])
        d = verdict(query=request(transformations=["DERIVE_RATIO"]), source=r)
        self.assertIn("TRANSFORMATION_NOT_GRANTED", d["reason_codes"])

    def test_private_summary_does_not_require_external_redistribution(self):
        r = capability()
        r["field_grants"]["viewCount"]["actions"].remove("REDISTRIBUTE")
        d = verdict(query=request(transformations=["SUMMARIZE"]), source=r)
        self.assertEqual("SHAPE_CHECK_PASSED_SYNTHETIC_ONLY", d["decision"])

    def test_grants_require_data_class_and_policy_provenance(self):
        r = capability()
        del r["field_grants"]["viewCount"]["data_class"]
        with self.assertRaises(InvalidContract):
            verdict(source=r)

    def test_summary_output_requires_redistribution_right_in_fixture(self):
        r = capability()
        r["field_grants"]["viewCount"]["actions"].remove("REDISTRIBUTE")
        d = verdict(query=request(transformations=["SUMMARIZE"], redistribute_output=True), source=r)
        self.assertIn("FIELD_REDISTRIBUTION_NOT_GRANTED", d["reason_codes"])

    def test_paid_stays_blocked_even_if_approval_refs_are_supplied(self):
        q = request(requires_paid=True)
        q["approval_ref"] = "simulated-approval"
        q["reservation_ref"] = "simulated-ledger-entry"
        d = verdict(query=q)
        self.assertIn("PAID_RESEARCH_NOT_ENABLED_IN_S3", d["reason_codes"])
        self.assertFalse(d["may_spend"])

    def test_raw_media_is_not_authorized_by_data_metadata(self):
        d = verdict(query=request(requests_raw_media=True))
        self.assertIn("RAW_MEDIA_NOT_AUTHORIZED_IN_S3", d["reason_codes"])

    def test_background_collection_must_be_separately_authorized(self):
        d = verdict(query=request(background_collection=True))
        self.assertIn("BACKGROUND_COLLECTION_NOT_AUTHORIZED", d["reason_codes"])

    def test_quota_exceedance_denied(self):
        d = verdict(query=request(estimated_calls=21))
        self.assertIn("QUOTA_BUDGET_EXCEEDED", d["reason_codes"])

    def test_revocation_immediately_blocks_simulation(self):
        d = verdict(source=capability(revoked=True))
        self.assertIn("SOURCE_REVOKED", d["reason_codes"])

    def test_policy_expiry_blocks_at_boundary(self):
        r = capability(expires_at=NOW)
        self.assertIn("POLICY_NOT_CURRENT", verdict(source=r)["reason_codes"])

    def test_future_policy_review_blocks(self):
        r = capability(reviewed_at="2026-10-24T00:00:00+00:00")
        self.assertIn("POLICY_NOT_CURRENT", verdict(source=r)["reason_codes"])

    def test_malformed_policy_interval_blocks(self):
        r = capability(expires_at="2026-09-30T00:00:00+00:00")
        self.assertIn("POLICY_NOT_CURRENT", verdict(source=r)["reason_codes"])

    def test_retention_greater_than_allowed_ttl_blocked(self):
        d = verdict(query=request(storage_mode="PERSIST", retention_days=8))
        self.assertIn("FIELD_PERSISTENCE_NOT_GRANTED", d["reason_codes"])

    def test_field_without_persistence_right_fails(self):
        r = capability()
        r["field_grants"]["viewCount"]["actions"].remove("PERSIST")
        d = verdict(query=request(storage_mode="PERSIST", retention_days=1), source=r)
        self.assertIn("FIELD_PERSISTENCE_NOT_GRANTED", d["reason_codes"])


class InvalidShapes(unittest.TestCase):
    def test_missing_operation(self):
        q = request()
        del q["operation"]
        with self.assertRaises(InvalidContract):
            verdict(query=q)

    def test_extreme_retention_request_and_grant_rejected(self):
        with self.assertRaises(InvalidContract):
            verdict(query=request(storage_mode="PERSIST", retention_days=10 ** 18))
        c = capability()
        c["field_grants"]["viewCount"]["max_retention_days"] = 10 ** 18
        with self.assertRaises(InvalidContract):
            verdict(source=c)

    def test_unknown_storage_mode(self):
        with self.assertRaises(InvalidContract):
            verdict(query=request(storage_mode="UNBOUNDED"))

    def test_true_as_retention_int_or_call_count_is_rejected(self):
        for change in ({"retention_days": True}, {"estimated_calls": True}):
            with self.subTest(change=change), self.assertRaises(InvalidContract):
                verdict(query=request(**change))

    def test_bool_not_allowed_as_permission_flag_string(self):
        with self.assertRaises(InvalidContract):
            verdict(query=request(requires_paid="false"))

    def test_duplicate_requested_fields(self):
        with self.assertRaises(InvalidContract):
            verdict(query=request(fields=["viewCount", "viewCount"]))

    def test_unknown_transform_rejected_as_invalid_request(self):
        with self.assertRaises(InvalidContract):
            verdict(query=request(transformations=["AUTO_PUBLISH"]))

    def test_norecord_persistent_ttl_mismatch(self):
        for changes in (
            {"storage_mode": "NONE", "retention_days": 1},
            {"storage_mode": "PERSIST", "retention_days": 0},
            {"storage_mode": "TRANSIENT_ONLY", "retention_days": 5},
        ):
            with self.subTest(changes=changes), self.assertRaises(InvalidContract):
                verdict(query=request(**changes))

    def test_non_numeric_quota_is_rejected(self):
        with self.assertRaises(InvalidContract):
            verdict(source=capability(max_calls_per_day="100"))

    def test_invalid_field_grants_are_rejected(self):
        r = capability()
        r["field_grants"]["viewCount"]["actions"] = ["READ", "RUN_SHELL"]
        with self.assertRaises(InvalidContract):
            verdict(source=r)

    def test_persistence_requires_explicit_ttl(self):
        r = capability()
        r["field_grants"]["viewCount"]["max_retention_days"] = 0
        with self.assertRaises(InvalidContract):
            verdict(source=r)

    def test_expiry_must_have_timezone(self):
        with self.assertRaises(InvalidContract):
            verdict(source=capability(expires_at="2026-11-01T00:00:00"))

    def test_unknown_source_kind_is_not_assumed_public(self):
        with self.assertRaises(InvalidContract):
            verdict(source=capability(source_kind="PUBLIC"))

    def test_no_echo_of_unverified_policy_reference(self):
        r = capability(source_kind="OFFICIAL_API", policy_ref="potential_private_string")
        d = verdict(source=r)
        self.assertNotIn("potential_private_string", str(d))


class RetentionTests(unittest.TestCase):
    def test_before_expiry_remains_simulated(self):
        d = retention_verdict(recorded_at=NOW, ttl_days=7,
                              now="2026-10-29T14:59:59+00:00")
        self.assertEqual("SIMULATED_VALID", d["decision"])
        self.assertFalse(d["actual_deletion_performed"])

    def test_exact_expiry_requires_purge(self):
        d = retention_verdict(recorded_at=NOW, ttl_days=7,
                              now="2026-10-30T15:00:00+00:00")
        self.assertEqual("PURGE_REQUIRED", d["decision"])
        self.assertTrue(d["must_invalidate_derivatives"])
        self.assertFalse(d["actual_deletion_performed"])

    def test_revocation_requires_purge_before_ttl(self):
        d = retention_verdict(recorded_at=NOW, ttl_days=7,
                              now=NOW, revoked=True)
        self.assertEqual("PURGE_REQUIRED", d["decision"])

    def test_zero_ttl_never_grants_period_of_storage(self):
        d = retention_verdict(recorded_at=NOW, ttl_days=0, now=NOW)
        self.assertEqual("PURGE_REQUIRED", d["decision"])

    def test_time_travel_and_naive_rejected(self):
        with self.assertRaises(InvalidContract):
            retention_verdict(recorded_at=NOW, ttl_days=1,
                              now="2026-10-22T15:00:00+00:00")
        with self.assertRaises(InvalidContract):
            retention_verdict(recorded_at=NOW, ttl_days=1,
                              now="2026-10-23T15:00:00")

    def test_extreme_ttl_fails_before_timedelta_overflow(self):
        with self.assertRaises(InvalidContract):
            retention_verdict(recorded_at=NOW, ttl_days=10 ** 18, now=NOW)

    def test_bool_ttl_and_revocation_rejected(self):
        with self.assertRaises(InvalidContract):
            retention_verdict(recorded_at=NOW, ttl_days=True, now=NOW)
        with self.assertRaises(InvalidContract):
            retention_verdict(recorded_at=NOW, ttl_days=1, now=NOW,
                              revoked="false")


if __name__ == "__main__":
    unittest.main()
