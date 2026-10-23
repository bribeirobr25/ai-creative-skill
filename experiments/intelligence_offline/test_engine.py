"""Offline invariants for the experimental intelligence engine.

Run: python -m unittest discover -s experiments/intelligence_offline -p 'test_*.py' -v
No third-party dependencies or network calls.
"""
import unittest
from datetime import datetime, timedelta, timezone

from engine import (
    Observation, ValidationError, InsufficientEvidence, unique_observations,
    outlier_ratio, view_velocity, rank_sample, simulate_operational_resilience
)

T0 = datetime(2026, 10, 20, tzinfo=timezone.utc)


def obs(video="v0", channel="c1", views=100, hours_old=24, snap=T0,
        fmt="long", platform="synthetic", kind="SYNTHETIC_FIXTURE"):
    return Observation(
        publication_id=video, channel_id=channel, platform=platform,
        content_type=fmt, views=views, observed_at=snap,
        published_at=snap - timedelta(hours=hours_old), source_kind=kind,
    )


class InputAndIdentityTests(unittest.TestCase):
    def test_non_synthetic_rejected(self):
        with self.assertRaises(ValidationError):
            obs(kind="YOUTUBE_DATA_API")

    def test_missing_is_not_zero(self):
        self.assertIsNone(obs(views=None).views)
        with self.assertRaises(InsufficientEvidence):
            rank_sample([obs(views=None)], limit=1)

    def test_boolean_or_negative_views_not_numbers(self):
        for val in (-1, True):
            with self.subTest(val=val), self.assertRaises(ValidationError):
                obs(views=val)

    def test_timezone_aware_required(self):
        with self.assertRaises(ValidationError):
            obs(snap=datetime(2026, 10, 20))

    def test_exact_duplicate_deduplicated(self):
        self.assertEqual(1, len(unique_observations([obs(), obs()])))

    def test_conflicting_duplicate_rejected(self):
        with self.assertRaises(ValidationError):
            unique_observations([obs(views=10), obs(views=50)])

    def test_different_platform_same_id_remains_distinct(self):
        x = [obs(platform="A"), obs(platform="B")]
        self.assertEqual(2, len(unique_observations(x)))


class MetricsTests(unittest.TestCase):
    def setUp(self):
        self.target = obs("target", views=800)
        self.baseline = [obs("one", views=100), obs("two", views=200),
                         obs("three", views=100), obs("four", views=200)]

    def test_outlier_forbidden_by_default(self):
        with self.assertRaises(ValidationError):
            outlier_ratio(self.target, self.baseline)

    def test_outlier_age_matched_and_auditable(self):
        val = outlier_ratio(self.target, self.baseline, derived_permission=True)
        self.assertEqual(4, val["baseline_n"])
        self.assertEqual(150, val["median_comparable_views"])
        self.assertAlmostEqual(800 / 150, val["ratio"])

    def test_exclude_other_channel_format_and_age(self):
        cases = self.baseline + [obs("bad1", channel="other", views=1),
                                 obs("bad2", fmt="short", views=1),
                                 obs("bad3", hours_old=200, views=1)]
        val = outlier_ratio(self.target, cases, derived_permission=True)
        self.assertEqual(4, val["baseline_n"])

    def test_outlier_missing_baseline(self):
        with self.assertRaises(InsufficientEvidence):
            outlier_ratio(self.target, self.baseline[:2], derived_permission=True)

    def test_outlier_zero_median(self):
        x = [obs("a", views=0), obs("b", views=0), obs("c", views=0)]
        with self.assertRaises(InsufficientEvidence):
            outlier_ratio(self.target, x, derived_permission=True)

    def test_multiple_snapshots_one_baseline_publication_do_not_inflate_n(self):
        one = obs("repeat", views=100)
        later = obs("repeat", views=150, snap=T0 + timedelta(minutes=10),
                    hours_old=24 + 10 / 60)
        # One video sampled twice is not two independent comparison videos.
        with self.assertRaises(ValidationError):
            outlier_ratio(self.target, [one, later, obs("b"), obs("c")],
                          derived_permission=True)

    def test_velocity_is_interval_delta_not_total_over_age(self):
        earlier = obs("target", views=120)
        later = obs("target", views=200, snap=T0 + timedelta(hours=4), hours_old=28)
        out = view_velocity(earlier, later, derived_permission=True)
        self.assertEqual(20.0, out["views_per_hour"])

    def test_velocity_rejects_counter_correction(self):
        earlier = obs("target", views=200)
        later = obs("target", views=120, snap=T0 + timedelta(hours=4), hours_old=28)
        with self.assertRaises(InsufficientEvidence):
            view_velocity(earlier, later, derived_permission=True)

    def test_velocity_missing_and_reverse_time(self):
        with self.assertRaises(InsufficientEvidence):
            view_velocity(obs(views=None), obs(views=20, snap=T0 + timedelta(hours=4), hours_old=28),
                          derived_permission=True)
        with self.assertRaises(InsufficientEvidence):
            view_velocity(obs(views=100), obs(views=200), derived_permission=True)

    def test_velocity_no_permission(self):
        with self.assertRaises(ValidationError):
            view_velocity(obs(views=100), obs(views=200))

    def test_ranking_cannot_claim_national_top_without_population(self):
        with self.assertRaises(InsufficientEvidence):
            rank_sample([obs("one", views=1)], limit=10, requested_national_top=True)

    def test_sample_rank_stable_ties_and_missing(self):
        ranked = rank_sample([obs("b", views=10), obs("a", views=10), obs("c", views=None)], limit=5)
        self.assertEqual(["a", "b"], [x["publication_id"] for x in ranked["results"]])
        self.assertEqual(1, ranked["missing_count"])
        self.assertEqual("OBSERVED_SAMPLE_ONLY", ranked["population"])

    def test_cannot_mix_platforms(self):
        with self.assertRaises(ValidationError):
            rank_sample([obs(platform="A"), obs(platform="B")], limit=10)

    def test_cannot_mix_snapshot_times(self):
        with self.assertRaises(ValidationError):
            rank_sample([obs(video="a"), obs(video="b", snap=T0 + timedelta(hours=1))], limit=10)


class MonteCarloTests(unittest.TestCase):
    def test_seeded_reproducible_and_count_conserved(self):
        a = simulate_operational_resilience(trials=500, seed=4567)
        b = simulate_operational_resilience(trials=500, seed=4567)
        self.assertEqual(a, b)
        self.assertEqual(500, sum(a["counts"].values()))

    def test_forced_common_outage(self):
        a = simulate_operational_resilience(trials=100, common_outage_probability=1.0)
        self.assertEqual(100, a["counts"]["BLOCKED"])

    def test_no_outages(self):
        a = simulate_operational_resilience(
            trials=100, common_outage_probability=0.0, independent_failure_probability=0.0
        )
        self.assertEqual(100, a["counts"]["COMPLETE"])

    def test_invalid_probabilities_rejected(self):
        with self.assertRaises(ValidationError):
            simulate_operational_resilience(common_outage_probability=-0.1)


if __name__ == "__main__":
    unittest.main()
