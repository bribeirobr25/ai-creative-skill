"""Public planning templates only. No permissions, credentials or live API behavior.

Documentation links are identifiers for HUMAN policy review, not grants.
Every record is deliberately UNVERIFIED and has zero quota/field rights.
"""
from __future__ import annotations

from copy import deepcopy

_TEMPLATES = {
    "YOUTUBE_PUBLIC_VIDEO_SEARCH": {
        "source_id": "YOUTUBE_DATA_API",
        "platform": "YOUTUBE", "operation": "PUBLIC_VIDEO_SEARCH",
        "policy_documentation": [
            "https://developers.google.com/youtube/terms/developer-policies-guide",
            "https://developers.google.com/youtube/data/determine_quota_cost",
            "https://developers.google.com/youtube/v3/docs/search/list",
        ],
        "documentation_note": "PUBLIC_API_CATALOG_ONLY_NOT_OPERATIONAL_ACCESS",
    },
    "YOUTUBE_DERIVED_ANALYTICS": {
        "source_id": "YOUTUBE_DATA_API",
        "platform": "YOUTUBE", "operation": "DERIVED_ANALYTICS",
        "policy_documentation": [
            "https://developers.google.com/youtube/terms/derived-metrics-policy",
            "https://developers.google.com/youtube/terms/developer-policies-guide",
        ],
        "documentation_note": "REQUIRES_EXPRESS_ANALYTICS_AND_REPORTING_APPROVAL",
    },
    "META_AD_LIBRARY_DISCOVERY": {
        "source_id": "META_AD_LIBRARY",
        "platform": "META", "operation": "AD_LIBRARY_DISCOVERY",
        "policy_documentation": [
            "https://www.facebook.com/ads/library/api/",
            "https://developers.facebook.com/docs/graph-api/reference/ads_archive/",
        ],
        "documentation_note": "COUNTRY_CATEGORY_FIELD_AND_ACCESS_COVERAGE_NOT_VERIFIED",
    },
}


def planning_templates() -> dict:
    """Copies of operation *hypotheses*, never an approved SourceCapabilityRecord."""
    return deepcopy(_TEMPLATES)


def unverified_capability_template(key: str) -> dict:
    """Shape-compatible candidate. evaluate() MUST block this record."""
    if key not in _TEMPLATES:
        raise KeyError("Unknown planning template")
    row = _TEMPLATES[key]
    return {
        "source_id": row["source_id"], "platform": row["platform"],
        "operation": row["operation"], "source_kind": "OFFICIAL_API",
        "adapter_version": "NOT_IMPLEMENTED",
        "policy_ref": "POLICY_EVIDENCE_NOT_VERIFIED",
        "authorization_state": "NOT_VERIFIED",
        "purposes": [], "projects": [], "countries": [],
        "geography_bases": [], "time_bases": [],
        "transformations": [], "field_grants": {},
        "reviewed_at": "2026-10-23T00:00:00+00:00",
        "expires_at": "2026-10-23T00:00:00+00:00",
        "revoked": False, "max_calls_per_day": 0,
        "documentation_note": row["documentation_note"],
        "documentation_links": list(row["policy_documentation"]),
    }
