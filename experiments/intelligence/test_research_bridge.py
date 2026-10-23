"""Synthetic bridge tests; canonical method compatibility is only a fixture claim."""
import unittest
from dataclasses import replace
from datetime import date, datetime, timedelta, timezone

from intelligence.engine import Observation, ValidationError
from intelligence.research_bridge import build_research_execution_fixture, SOURCE_OUTCOMES, _REQUIRED_ENVELOPE_KEYS

T = datetime(2026, 10, 23, 10, 0, tzinfo=timezone.utc)


def synthetic_row(id="a", views=200, obs_at=T, pub_at=None, platform="synthetic"):
    return Observation(
        publication_id=id, channel_id="creator",
        platform=platform, content_type="long", views=views,
        observed_at=obs_at,
        published_at=pub_at or T - timedelta(days=2), source_kind="SYNTHETIC_FIXTURE",
    )


def request(**overrides):
    base = {
        "research_execution_id": "research:synthetic:001",
        "research_intent": "MARKET_SCAN",
        "primary_entity": "fictional makeup bags",
        "market": "DE",
        "language": "de",
        "range_from": date(2026, 10, 1),
        "range_to": date(2026, 10, 24),
        "generated_at": T + timedelta(seconds=5),
        "observation_rows": [synthetic_row("a"), synthetic_row("b", 100)],
        "source_outcome": "OK",
    }
    base.update(overrides)
    return build_research_execution_fixture(**base)


class SyntheticBridgeTests(unittest.TestCase):
    def test_envelope_mirrors_all_existing_method_fields(self):
        x = request()
        self.assertTrue(_REQUIRED_ENVELOPE_KEYS <= x.keys())
        self.assertEqual("COMPLETE", x["status"])
        self.assertFalse(x["intelligence"]["external_calls_performed"])
        self.assertFalse(x["intelligence"]["derived_metrics_performed"])
        self.assertEqual("SYNTHETIC_FIXTURE_ONLY", x["coverage"]["actual_scope"])

    def test_metrics_resolve_only_to_existing_evidence(self):
        x = request()
        evid = set(x["fixture_evidence_index"])
        self.assertEqual(2, len(evid))
        for m in x["intelligence"]["metric_observations"]:
            self.assertIn(m["evidence_id"], evid)
        for ref in x["intelligence"]["ranked_evidence_refs"]:
            self.assertIn(ref, evid)

    def test_composite_evidence_ids_cannot_collide_when_source_ids_have_colons(self):
        x = request(observation_rows=[
            synthetic_row("c", platform="a:b"),
            synthetic_row("b:c", platform="a"),
        ])
        ids = [e["evidence_id"] for e in x["evidence_clusters"]]
        self.assertEqual(2, len(set(ids)))
        subjects = [m["subject_id"] for m in x["intelligence"]["metric_observations"]]
        self.assertEqual(2, len(set(subjects)))
        self.assertTrue(any("%3A" in v for v in ids))
        self.assertEqual("PARTIAL", x["status"])  # mixed platforms, no mixed rank

    def test_unknown_metric_not_zero(self):
        x = request(observation_rows=[synthetic_row(views=None)])
        self.assertEqual("UNKNOWN", x["intelligence"]["metric_observations"][0]["value"])
        self.assertEqual([], x["intelligence"]["ranked_evidence_refs"])

    def test_ok_source_without_any_ranking_metrics_is_not_complete(self):
        x = request(observation_rows=[synthetic_row(views=None)])
        self.assertEqual("INSUFFICIENT_EVIDENCE", x["status"])

    def test_ok_source_with_some_missing_metrics_is_partial(self):
        x = request(observation_rows=[synthetic_row("a", views=100), synthetic_row("b", views=None)])
        self.assertEqual("PARTIAL", x["status"])

    def test_ok_source_with_incompatible_platforms_is_partial(self):
        x = request(observation_rows=[
            synthetic_row("a", platform="A"),
            synthetic_row("b", platform="B")
        ])
        self.assertEqual("PARTIAL", x["status"])
        self.assertEqual("NOT_COMPARABLE", x["intelligence"]["ranking_scope"])

    def test_source_outcomes_are_exactly_original_vocab(self):
        self.assertEqual(11, len(SOURCE_OUTCOMES))
        x = request(source_outcome="RATE_LIMITED")
        self.assertEqual("PARTIAL", x["status"])
        self.assertEqual("RATE_LIMITED", x["source_outcomes"][0]["outcome"])

    def test_auth_failure_not_a_negative_search(self):
        x = request(source_outcome="AUTH_FAILED", observation_rows=[])
        self.assertEqual("BLOCKED", x["status"])
        self.assertEqual("AUTH_FAILED", x["source_outcomes"][0]["outcome"])

    def test_exhaustive_negative_search_can_complete_absence_question(self):
        x = request(
            source_outcome="NO_RESULTS", observation_rows=[],
            negative_coverage_satisfies_request=True,
            source_coverage_verified=True,
        )
        self.assertEqual("COMPLETE", x["status"])
        self.assertTrue(x["coverage"]["source_coverage_verified"])

    def test_negative_search_without_complete_scope_remains_insufficient(self):
        x = request(
            source_outcome="NO_RESULTS", observation_rows=[],
            negative_coverage_satisfies_request=True,
            source_coverage_verified=False,
        )
        self.assertEqual("INSUFFICIENT_EVIDENCE", x["status"])

    def test_national_rank_flag_propagates_and_prevents_sample_substitution(self):
        x = request(requested_national_top=True, population_coverage_verified=False)
        self.assertEqual("INSUFFICIENT_EVIDENCE", x["status"])
        self.assertEqual("NATIONAL_COVERAGE_UNVERIFIED", x["intelligence"]["ranking_scope"])
        self.assertEqual([], x["intelligence"]["ranked_evidence_refs"])
        self.assertTrue(x["coverage"]["requested_national_top"])

    def test_national_top_needs_both_population_and_source_coverage(self):
        x = request(requested_national_top=True,
                    population_coverage_verified=True,
                    source_coverage_verified=False)
        self.assertEqual("INSUFFICIENT_EVIDENCE", x["status"])
        self.assertEqual("NATIONAL_COVERAGE_UNVERIFIED",
                         x["intelligence"]["ranking_scope"])
        self.assertEqual([], x["intelligence"]["ranked_evidence_refs"])
        self.assertFalse(x["coverage"]["population_verified"])

    def test_rate_limited_source_cannot_qualify_as_exhaustive_national_rank(self):
        x = request(requested_national_top=True,
                    population_coverage_verified=True,
                    source_coverage_verified=True, source_outcome="RATE_LIMITED")
        self.assertEqual("INSUFFICIENT_EVIDENCE", x["status"])
        self.assertEqual("RATE_LIMITED", x["source_outcomes"][0]["outcome"])
        self.assertEqual([], x["intelligence"]["ranked_evidence_refs"])

    def test_national_top_with_missing_counts_is_not_definitive(self):
        x = request(requested_national_top=True,
                    population_coverage_verified=True,
                    source_coverage_verified=True,
                    observation_rows=[
                        synthetic_row("known", views=20),
                        synthetic_row("unknown", views=None),
                    ])
        self.assertEqual("INSUFFICIENT_EVIDENCE", x["status"])
        self.assertEqual("NATIONAL_RANKING_UNDETERMINED",
                         x["intelligence"]["ranking_scope"])
        self.assertEqual([], x["intelligence"]["ranked_evidence_refs"])

    def test_fully_verified_synthetic_national_rank_keeps_auditable_refs(self):
        x = request(requested_national_top=True,
                    population_coverage_verified=True,
                    source_coverage_verified=True)
        self.assertEqual("COMPLETE", x["status"])
        evid = {e["evidence_id"] for e in x["evidence_clusters"]}
        self.assertTrue(x["intelligence"]["ranked_evidence_refs"])
        self.assertTrue(set(x["intelligence"]["ranked_evidence_refs"]) <= evid)

    def test_synthetic_complete_scope_remains_explicitly_not_real_market(self):
        x = request(requested_national_top=True, population_coverage_verified=True,
                    source_coverage_verified=True)
        self.assertEqual("COMPLETE", x["status"])
        self.assertFalse(x["coverage"]["report_is_real_market_research"])
        self.assertEqual("COMPLETE", x["intelligence"]["ranking_scope"])

    def test_national_rank_and_absence_rule_cannot_combine(self):
        with self.assertRaises(ValidationError):
            request(
                source_outcome="NO_RESULTS", observation_rows=[],
                requested_national_top=True, negative_coverage_satisfies_request=True,
                source_coverage_verified=True,
            )

    def test_limit_rejected_before_rank_try_handler(self):
        for x in [0, True, -1, 101]:
            with self.subTest(limit=x), self.assertRaises(ValidationError):
                request(limit=x, observation_rows=[
                    synthetic_row("a", platform="A"), synthetic_row("b", platform="B")
                ])

    def test_reject_unhashable_source_outcome_cleanly(self):
        with self.assertRaises(ValidationError):
            request(source_outcome=[])

    def test_successful_no_results_distinct_from_auth_failure(self):
        x = request(source_outcome="NO_RESULTS", observation_rows=[])
        self.assertEqual("INSUFFICIENT_EVIDENCE", x["status"])
        self.assertEqual("NO_RESULTS", x["source_outcomes"][0]["outcome"])

    def test_no_results_with_data_is_conflict(self):
        with self.assertRaises(ValidationError):
            request(source_outcome="NO_RESULTS")

    def test_success_without_data_must_be_explicit_no_results(self):
        with self.assertRaises(ValidationError):
            request(observation_rows=[])

    def test_no_third_party_observations(self):
        with self.assertRaises(ValidationError):
            Observation(
                publication_id="x", channel_id="c", platform="youtube",
                content_type="long", views=30, observed_at=T,
                published_at=T-timedelta(days=1), source_kind="YOUTUBE_DATA_API"
            )

    def test_off_window_publication_blocked(self):
        with self.assertRaises(ValidationError):
            request(observation_rows=[synthetic_row(pub_at=T-timedelta(days=90))])

    def test_future_observation_blocked(self):
        with self.assertRaises(ValidationError):
            request(observation_rows=[synthetic_row(obs_at=T + timedelta(hours=1))])

    def test_source_kind_is_synthetic_not_claim_of_market_evidence(self):
        x = request()
        self.assertTrue(all(i["source_class"]=="SYNTHETIC_FIXTURE" for i in x["fixture_evidence_index"].values()))
        self.assertTrue(all(i["evidence_strength"]=="INDETERMINATE" for i in x["fixture_evidence_index"].values()))
        self.assertFalse(x["coverage"]["report_is_real_market_research"])

    def test_reject_incompatible_or_unknown_outcomes(self):
        for source in ("SUCCESS", "DENIED", "none"):
            with self.subTest(source=source), self.assertRaises(ValidationError):
                request(source_outcome=source)

    def test_different_platform_rank_ref_not_unjustified(self):
        x = request(observation_rows=[synthetic_row("a", platform="A"),synthetic_row("b", platform="B")])
        self.assertEqual("NOT_COMPARABLE", x["intelligence"]["ranking_scope"])
        self.assertEqual([], x["intelligence"]["ranked_evidence_refs"])

    def test_stable_view_ranking_has_evidence_links(self):
        x = request()
        values = x["intelligence"]["ranked_evidence_refs"]
        self.assertEqual(2, len(values))
        self.assertIn("synthetic:a", values[0])

    def test_non_string_identity_rejected(self):
        with self.assertRaises(ValidationError):
            request(research_execution_id="")

    def test_equal_window_rejected(self):
        with self.assertRaises(ValidationError):
            request(range_to=date(2026, 10, 1))

    def test_limit_bounds_rejected(self):
        with self.assertRaises(ValidationError):
            request(limit=0)


if __name__ == "__main__":
    unittest.main()
