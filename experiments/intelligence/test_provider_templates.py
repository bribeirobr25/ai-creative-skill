"""Every real-platform planning template is denied until verified outside S3."""
import unittest

from experiments.intelligence.provider_templates import planning_templates, unverified_capability_template
from experiments.intelligence.policy_gate import evaluate, validate_capability


def fake_request(cap):
    return {
        "operation": cap["operation"], "platform": cap["platform"],
        "project_id": "fixture-only", "purpose": "RESEARCH_ONLY",
        "country": "DE", "geography_basis": "SEARCH_RESULT_LOCALE",
        "time_basis": "PUBLISHED_DURING_WINDOW",
        "requested_metric": "PUBLIC_VIEW_COUNT",
        "window_start": "2026-10-01", "window_end": "2026-10-24",
        "fields": ["viewCount"], "transformations": ["DISPLAY_NATIVE"],
        "storage_mode": "TRANSIENT_ONLY", "retention_days": 0,
        "requires_paid": False, "requests_raw_media": False,
        "background_collection": False, "estimated_calls": 1,
    }


class TemplateSafetyTests(unittest.TestCase):
    def test_catalog_has_three_distinct_operation_hypotheses(self):
        catalog = planning_templates()
        self.assertEqual(3, len(catalog))
        self.assertIn("YOUTUBE_PUBLIC_VIDEO_SEARCH", catalog)
        self.assertIn("YOUTUBE_DERIVED_ANALYTICS", catalog)
        self.assertIn("META_AD_LIBRARY_DISCOVERY", catalog)

    def test_documentation_urls_are_not_credentials_or_access_grants(self):
        for key, row in planning_templates().items():
            with self.subTest(key=key):
                self.assertTrue(row["policy_documentation"])
                self.assertTrue(all(u.startswith("https://") for u in row["policy_documentation"]))
                self.assertNotIn("credentials", str(row).lower())

    def test_every_provider_capability_denied(self):
        for key in planning_templates():
            with self.subTest(key=key):
                c = unverified_capability_template(key)
                validate_capability(c)
                d = evaluate(fake_request(c), c, now="2026-10-23T15:00:00+00:00")
                self.assertEqual("BLOCKED", d["decision"])
                self.assertIn("REAL_SOURCE_NOT_AUTHORIZED", d["reason_codes"])
                self.assertFalse(d["may_access_real_source"])
                self.assertFalse(d["may_spend"])

    def test_forged_verified_synthetic_access_state_not_enough(self):
        c = unverified_capability_template("YOUTUBE_DERIVED_ANALYTICS")
        c["authorization_state"] = "SIMULATED_VERIFIED"
        d = evaluate(fake_request(c), c, now="2026-10-23T15:00:00+00:00")
        self.assertEqual("BLOCKED", d["decision"])
        self.assertFalse(d["may_access_real_source"])

    def test_catalog_returns_independent_copies(self):
        a = planning_templates()
        a["YOUTUBE_DERIVED_ANALYTICS"]["policy_documentation"].append("fake")
        b = planning_templates()
        self.assertNotIn("fake", b["YOUTUBE_DERIVED_ANALYTICS"]["policy_documentation"])

    def test_unknown_template_fails_closed(self):
        with self.assertRaises(KeyError):
            unverified_capability_template("UNLISTED_PLATFORM")


if __name__ == "__main__":
    unittest.main()
