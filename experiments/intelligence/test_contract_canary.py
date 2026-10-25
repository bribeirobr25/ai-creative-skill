"""S2 adversarial tests: all records are SYNTHETIC_FIXTURE, no APIs."""
import copy
import json
import unittest

from experiments.intelligence.contract_canary import (
    ContractViolation, SOURCE_OUTCOMES, RESEARCH_STATUSES,
    validate_research_execution, validate_query_filter,
    validate_handoff,
)


def fixture():
    stamp = "2026-10-23T09:00:00+00:00"
    evidence = {
        "fixture:e-1": {
            "evidence_id": "fixture:e-1", "source_ref": "fixture:publication:one",
            "source_class": "SYNTHETIC_FIXTURE", "retrieved_at": stamp,
            "published_at": "2026-10-20T09:00:00+00:00",
            "date_confidence": "HIGH", "entity_scope": "synthetic:one",
            "claim_or_observation": "Synthetic counter", "exact_quote_ref": None,
            "relevance": "DIRECT", "evidence_strength": "INDETERMINATE",
            "engagement_observed": False, "independence_key": "synthetic:one",
            "source_outcome_ref": "fixture:attempt-1", "notes": "made-up data",
        },
    }
    envelope = {
        "research_execution_id": "research-1", "research_intent": "MARKET_SCAN",
        "primary_entity": "fictional topic", "market": "DE", "language": "de",
        "range_from": "2026-10-01", "range_to": "2026-10-24",
        "generated_at": stamp, "query_plan": [], "source_outcomes": [{
            "source_ref": "fixture:attempt-1", "source_class": "SYNTHETIC_FIXTURE",
            "outcome": "OK", "checked_at": stamp,
        }],
        "coverage": {
            "actual_scope": "SYNTHETIC_FIXTURE_ONLY",
            "report_is_real_market_research": False,
            "requested_national_top": False, "source_coverage_verified": False,
            "population_verified": False,
        },
        "evidence_clusters": [{
            "cluster_id": "fixture:cluster-1", "question_or_theme": "fictional views",
            "supporting_evidence_refs": ["fixture:e-1"], "counterevidence_refs": [],
            "independent_source_count": 1, "uncertainty": "synthetic-only",
            "what_is_observed": "Synthetic count", "what_is_inferred": "UNKNOWN",
            "creative_or_decision_implication": "UNKNOWN",
        }],
        "counterevidence": [], "freshness_verdicts": [], "status": "PARTIAL",
        "unknowns": ["All market facts UNKNOWN"], "reuse_notes": [],
        "intelligence": {
            "schema_family": "INTELLIGENCE_SYNTHETIC_EXTENSION",
            "schema_version": "s2-contract-canary-0.1",
            "metric_observations": [{
                "observation_id": "obs-1",
                "research_execution_id": "research-1",
                "evidence_id": "fixture:e-1", "source_outcome_ref": "fixture:attempt-1",
                "subject_id": "synthetic:one", "metric_name": "PUBLIC_VIEW_COUNT",
                "metric_value": 200, "observed_at": stamp,
                "observation_basis": "PLATFORM_REPORTED_CUMULATIVE",
                "measurement_window": "UNKNOWN", "geography_meaning": "UNKNOWN",
                "population_coverage": "UNKNOWN", "license_policy_ref": "fixture-only",
                "provenance": "SYNTHETIC_FIXTURE",
                "storage_disposition": "IN_MEMORY_EXPERIMENT_ONLY",
            }],
            "ranked_evidence_refs": ["fixture:e-1"], "ranking_scope": "OBSERVED_SAMPLE_ONLY",
            "external_calls_performed": False, "derived_metrics_performed": False,
            "policy_shape_decision": "SHAPE_CHECK_PASSED_SYNTHETIC_ONLY",
            "stop_code": None,
        },
    }
    return envelope, evidence


def query():
    return {
        "operation": "PUBLIC_VIDEO_SEARCH",
        "platforms": ["SYNTHETIC_FIXTURE"],
        "geographic_filter": {
            "code": "DE", "level": "COUNTRY", "meaning": "SEARCH_RESULT_LOCALE",
        },
        "time_filter": {
            "start_inclusive": "2026-10-01", "end_exclusive": "2026-10-24",
            "meaning": "PUBLISHED_DURING_WINDOW", "timezone": "Europe/Berlin",
        },
        "ranking": {"metric": "PUBLIC_VIEW_COUNT", "limit": 10},
    }


def source():
    return {
        "source_kind": "SYNTHETIC_FIXTURE",
        "source_id": "SYNTHETIC_FIXTURE",
        "operation": "PUBLIC_VIDEO_SEARCH", "adapter_version": "test-only-0.1",
        "access_authorization": "VERIFIED_SYNTHETIC",
        "processing_rights": "VERIFIED_SYNTHETIC",
        "allowed_purposes": ["RESEARCH_ONLY"],
        "documented_geo_semantics": ["SEARCH_RESULT_LOCALE"],
        "documented_time_semantics": ["PUBLISHED_DURING_WINDOW"],
        "documented_metric_support": ["PUBLIC_VIEW_COUNT"],
        "field_rights": {"viewCount": "VERIFIED_SYNTHETIC"},
        "allowed_transformations": ["DISPLAY_NATIVE_METRIC"],
    }


def policy(q=None, rec=None, **kwargs):
    base = {"purpose": "RESEARCH_ONLY", "requested_fields": ["viewCount"],
            "transformation": "DISPLAY_NATIVE_METRIC"}
    base.update(kwargs)
    return evaluate_source_candidate(q or query(), rec or source(), **base)


class CanonicalVocabularyTests(unittest.TestCase):
    def test_source_outcomes_are_full_canonical_set(self):
        self.assertEqual(11, len(SOURCE_OUTCOMES))
        self.assertTrue({"PAYMENT_REQUIRED", "SCHEMA_DRIFT", "SKIPPED_UNCONFIGURED"} <= SOURCE_OUTCOMES)

    def test_statuses_not_source_outcomes(self):
        self.assertEqual({"COMPLETE", "PARTIAL", "INSUFFICIENT_EVIDENCE", "BLOCKED"},
                         set(RESEARCH_STATUSES))

    def test_roundtrip_preserves_research_and_unknowns(self):
        e, refs = fixture()
        wire = json.loads(json.dumps(e))
        validate_research_execution(wire, evidence_by_id=refs)
        self.assertEqual(e, wire)
        self.assertEqual(["All market facts UNKNOWN"], wire["unknowns"])

    def test_complete_cannot_claim_success_from_auth_failure(self):
        e, refs = fixture()
        e["status"] = "COMPLETE"
        e["source_outcomes"][0]["outcome"] = "AUTH_FAILED"
        e["evidence_clusters"] = []
        e["intelligence"]["metric_observations"] = []
        e["intelligence"]["ranked_evidence_refs"] = []
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id={})

    def test_complete_ok_without_evidence_fails(self):
        e, _ = fixture()
        e["status"] = "COMPLETE"
        e["evidence_clusters"] = []
        e["intelligence"]["metric_observations"] = []
        e["intelligence"]["ranked_evidence_refs"] = []
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id={})

    def test_national_top_requires_boolean_flag(self):
        e, refs = fixture()
        e["coverage"]["requested_national_top"] = 1
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)

    def test_unknown_authority_fields_fail(self):
        e, refs = fixture()
        e["intelligence"]["may_spend"] = True
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)

    def test_missing_canonical_research_field_rejected(self):
        e, refs = fixture()
        del e["query_plan"]
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)

    def test_source_outcome_vocabulary_cannot_be_shortened(self):
        for outcome in ("RATE_LIMITED", "AUTH_FAILED", "SCHEMA_DRIFT",
                        "PAYMENT_REQUIRED", "SKIPPED_UNCONFIGURED"):
            with self.subTest(outcome=outcome):
                e, _ = fixture()
                e["source_outcomes"][0]["outcome"] = outcome
                e["status"] = "BLOCKED"
                e["intelligence"]["stop_code"] = (
                    "STOP_REQUIRED_AUTHORITY_MISSING"
                    if outcome in ("AUTH_FAILED", "PAYMENT_REQUIRED")
                    else "STOP_REQUIRED_VERIFICATION_UNAVAILABLE"
                )
                e["evidence_clusters"] = []
                e["intelligence"]["metric_observations"] = []
                e["intelligence"]["ranked_evidence_refs"] = []
                validate_research_execution(e, evidence_by_id={})

    def test_failed_source_cannot_support_claims_or_metrics(self):
        for outcome in ("AUTH_FAILED", "SCHEMA_DRIFT", "PAYMENT_REQUIRED",
                        "SKIPPED_UNCONFIGURED", "UNREACHABLE", "ERROR"):
            with self.subTest(outcome=outcome):
                e, refs = fixture()
                e["source_outcomes"][0]["outcome"] = outcome
                with self.assertRaises(ContractViolation):
                    validate_research_execution(e, evidence_by_id=refs)


    def test_invalid_source_outcome_rejected(self):
        e, refs = fixture()
        e["source_outcomes"][0]["outcome"] = "NO_DATA"
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)

    def test_duplicate_source_attempt_rejected(self):
        e, refs = fixture()
        e["source_outcomes"].append(copy.deepcopy(e["source_outcomes"][0]))
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)

    def test_non_utc_offset_timestamp_supported(self):
        e, refs = fixture()
        e["generated_at"] = "2026-10-23T11:00:00+02:00"
        validate_research_execution(e, evidence_by_id=refs)

    def test_timezone_naive_timestamp_rejected(self):
        e, refs = fixture()
        e["generated_at"] = "2026-10-23T09:00:00"
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)


class EvidenceOwnershipTests(unittest.TestCase):
    def test_evidence_records_and_clusters_are_separate(self):
        e, refs = fixture()
        validate_research_execution(e, evidence_by_id=refs)
        self.assertEqual("fixture:cluster-1", e["evidence_clusters"][0]["cluster_id"])
        self.assertNotIn("evidence_id", e["evidence_clusters"][0])

    def test_legacy_bridge_shape_is_not_a_cluster(self):
        e, refs = fixture()
        e["evidence_clusters"] = [copy.deepcopy(refs["fixture:e-1"])]
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)

    def test_future_metric_and_evidence_timestamps_are_rejected(self):
        e, refs = fixture()
        e["intelligence"]["metric_observations"][0]["observed_at"] = "2026-10-24T00:00:00+00:00"
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)
        e, refs = fixture()
        refs["fixture:e-1"]["retrieved_at"] = "2026-10-24T00:00:00+00:00"
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)

    def test_invalid_source_state_type_does_not_crash_with_typeerror(self):
        e, refs = fixture()
        e["source_outcomes"][0]["outcome"] = []
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)
        e, refs = fixture()
        e["status"] = []
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)

    def test_metric_has_to_reference_canonical_evidence(self):
        e, refs = fixture()
        e["intelligence"]["metric_observations"][0]["evidence_id"] = "missing"
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)

    def test_metric_source_attempt_must_match_evidence(self):
        e, refs = fixture()
        e["intelligence"]["metric_observations"][0]["source_outcome_ref"] = "attempt-other"
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)

    def test_metric_cannot_rebind_research_execution(self):
        e, refs = fixture()
        e["intelligence"]["metric_observations"][0]["research_execution_id"] = "other"
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)

    def test_cluster_cannot_refer_to_absent_or_duplicate_evidence(self):
        e, refs = fixture()
        e["evidence_clusters"][0]["supporting_evidence_refs"].append("missing")
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)
        e, refs = fixture()
        e["evidence_clusters"][0]["supporting_evidence_refs"].append("fixture:e-1")
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)

    def test_independence_count_cannot_treat_copies_as_corroboration(self):
        e, refs = fixture()
        second = copy.deepcopy(refs["fixture:e-1"])
        second["evidence_id"] = "fixture:e-2"
        second["source_ref"] = "fixture:copy"
        refs["fixture:e-2"] = second
        e["evidence_clusters"][0]["supporting_evidence_refs"].append("fixture:e-2")
        e["evidence_clusters"][0]["independent_source_count"] = 2
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)
        e["evidence_clusters"][0]["independent_source_count"] = 1
        validate_research_execution(e, evidence_by_id=refs)

    def test_metric_or_ranking_cannot_use_evidence_omitted_from_clusters(self):
        e, refs = fixture()
        e["evidence_clusters"] = []
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)
        e, refs = fixture()
        e["intelligence"]["metric_observations"] = []
        e["evidence_clusters"] = []
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)

    def test_no_results_source_cannot_claim_evidence(self):
        e, refs = fixture()
        e["source_outcomes"][0]["outcome"] = "NO_RESULTS"
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)

    def test_metric_duplicate_id_and_unknown_evidence_rejected(self):
        e, refs = fixture()
        e["intelligence"]["metric_observations"].append(
            copy.deepcopy(e["intelligence"]["metric_observations"][0]))
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)
        e, refs = fixture()
        e["intelligence"]["ranked_evidence_refs"].append("missing")
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)

    def test_missing_metric_is_UNKNOWN_not_zero(self):
        e, refs = fixture()
        e["intelligence"]["metric_observations"][0]["metric_value"] = "UNKNOWN"
        validate_research_execution(e, evidence_by_id=refs)
        e["intelligence"]["metric_observations"][0]["metric_value"] = None
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)

    def test_invalid_float_nan_inf_bool_rejected(self):
        for value in (float("nan"), float("inf"), True, -1):
            e, refs = fixture()
            e["intelligence"]["metric_observations"][0]["metric_value"] = value
            with self.subTest(value=str(value)), self.assertRaises(ContractViolation):
                validate_research_execution(e, evidence_by_id=refs)

    def test_real_source_and_storage_never_accepted(self):
        e, refs = fixture()
        refs["fixture:e-1"]["source_class"] = "YOUTUBE_DATA_API"
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)
        e, refs = fixture()
        e["intelligence"]["metric_observations"][0]["storage_disposition"] = "PERSIST"
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)


class CoverageAndHandoffTests(unittest.TestCase):
    def test_national_complete_requires_evidence_and_source_coverage(self):
        e, refs = fixture()
        e["status"] = "COMPLETE"
        e["coverage"]["requested_national_top"] = True
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)
        e["coverage"]["source_coverage_verified"] = True
        e["coverage"]["population_verified"] = "SYNTHETIC_FIXTURE_ONLY"
        validate_research_execution(e, evidence_by_id=refs)

    def test_national_complete_unknown_count_rejected(self):
        e, refs = fixture()
        e["status"] = "COMPLETE"
        e["coverage"].update(requested_national_top=True,
                             source_coverage_verified=True,
                             population_verified="SYNTHETIC_FIXTURE_ONLY")
        e["intelligence"]["metric_observations"][0]["metric_value"] = "UNKNOWN"
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)

    def test_no_execution_authority_through_extension(self):
        e, refs = fixture()
        e["intelligence"]["permissions_carried"] = "PUBLISH"
        with self.assertRaises(ContractViolation):
            validate_research_execution(e, evidence_by_id=refs)

    def test_handoff_requires_lineage_and_evidence_provenance(self):
        base = {
            "project_id": "synthetic", "from_task_id": "r1",
            "to_task_id": "t1", "from_profile": "Research",
            "to_profile": "Ads", "task_outcome": {},
            "accepted_constraints": [], "stable_entities": [{
                "entity_id": "e1", "entity_type": "CONTENT_PUBLICATION",
                "canonical_label": "UNKNOWN", "source_refs": ["ev-1"],
            }], "evidence_items": [{
                "evidence_ref": "ev-1", "evidence_class": "OBSERVED",
                "confidence": "LOW", "freshness": "UNKNOWN",
            }],
            "explicit_unknowns": [], "accepted_outputs": [],
            "protected_state": [], "invalidated_state": [],
            "permissions_carried": "NONE", "action_authority_recheck_required": True,
        }
        validate_handoff(base)
        missing = copy.deepcopy(base)
        del missing["evidence_items"][0]["evidence_ref"]
        with self.assertRaises(ContractViolation):
            validate_handoff(missing)
        missing = copy.deepcopy(base)
        del missing["to_task_id"]
        with self.assertRaises(ContractViolation):
            validate_handoff(missing)

    def test_handoff_refuses_authority_transfer(self):
        h = {
            "project_id": "synthetic", "from_task_id": "r1", "to_task_id": "t1",
            "from_profile": "Research", "to_profile": "Ads", "task_outcome": {},
            "accepted_constraints": [], "stable_entities": [], "evidence_items": [],
            "explicit_unknowns": [], "accepted_outputs": [],
            "protected_state": [], "invalidated_state": [],
            "permissions_carried": "NONE", "action_authority_recheck_required": True,
        }
        validate_handoff(h)
        h["permissions_carried"] = "SPEND"
        with self.assertRaises(ContractViolation):
            validate_handoff(h)
        h["permissions_carried"] = "NONE"
        h["action_authority_recheck_required"] = False
        with self.assertRaises(ContractViolation):
            validate_handoff(h)



if __name__ == "__main__":
    unittest.main()
