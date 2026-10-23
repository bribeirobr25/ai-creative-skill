"""Experimental bridge into the existing Research Evidence Synthesis *method* contract.

This mirrors the research_execution OUTPUT described in references, NOT a live
schema, canonical runtime or plugin installation. Only synthetic fixtures:
there is NO network, API client, source storage, publication or billing.
"""
from __future__ import annotations

from datetime import date, datetime, timezone
from typing import Iterable

from engine import Observation, ValidationError, InsufficientEvidence, unique_observations, rank_sample


SOURCE_OUTCOMES = frozenset({
    "OK", "NO_RESULTS", "PARTIAL", "RATE_LIMITED", "AUTH_FAILED",
    "PAYMENT_REQUIRED", "UNREACHABLE", "TIMEOUT", "SCHEMA_DRIFT",
    "SKIPPED_UNCONFIGURED", "ERROR",
})
RESEARCH_STATUSES = frozenset({"COMPLETE", "PARTIAL", "INSUFFICIENT_EVIDENCE", "BLOCKED"})
_ALLOWED_WITH_ROWS = frozenset({"OK", "PARTIAL", "RATE_LIMITED", "TIMEOUT"})
_REQUIRED_ENVELOPE_KEYS = frozenset({
    "research_execution_id", "research_intent", "primary_entity", "market",
    "language", "range_from", "range_to", "generated_at", "query_plan",
    "source_outcomes", "coverage", "evidence_clusters", "counterevidence",
    "freshness_verdicts", "status", "unknowns", "reuse_notes"
})


def _nonempty(value: str, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValidationError(f"{name}: nonempty string required")
    return value.strip()


def build_research_execution_fixture(
    *,
    research_execution_id: str,
    research_intent: str,
    primary_entity: str,
    market: str,
    language: str,
    range_from: date,
    range_to: date,
    observation_rows: Iterable[Observation],
    source_outcome: str = "OK",
    limit: int = 10,
    population_coverage_verified: bool = False,
    generated_at: datetime,
) -> dict:
    """Make a synthetic-only contract fixture for a bounded Research result.

    The publication observed view-count and result ID live under 'intelligence'
    as an EXTENSION, while source outcomes/coverage/evidence are in the already
    documented research_execution envelope. No new source owner is introduced.

    No paid authorization or real rights are accepted. This builder is NOT
    allowed to interpret or persist third-party data.
    """
    for name, value in (
        ("research_execution_id", research_execution_id),
        ("research_intent", research_intent),
        ("primary_entity", primary_entity),
        ("market", market),
        ("language", language),
    ):
        _nonempty(value, name)
    if not isinstance(range_from, date) or not isinstance(range_to, date):
        raise ValidationError("Date window requires date objects")
    if range_from >= range_to:
        raise ValidationError("End exclusive must follow start")
    if not isinstance(generated_at, datetime) or generated_at.tzinfo is None or generated_at.utcoffset() is None:
        raise ValidationError("Generated-at timestamp must be timezone-aware")
    if source_outcome not in SOURCE_OUTCOMES:
        raise ValidationError("Invalid source outcome")
    rows = unique_observations(observation_rows)

    # To be explicit: "OK with no rows" is NOT a valid full negative scan.
    # NO_RESULTS requires a successful negative coverage evaluation.
    if source_outcome == "NO_RESULTS" and rows:
        raise ValidationError("NO_RESULTS cannot carry observations")
    if source_outcome == "OK" and not rows:
        raise ValidationError("Use NO_RESULTS for a completed empty result")
    if rows and source_outcome not in _ALLOWED_WITH_ROWS:
        raise ValidationError("Source status incompatible with observations")

    for x in rows:
        # Defense in depth, even though Observation itself validates.
        if x.source_kind != "SYNTHETIC_FIXTURE":
            raise ValidationError("Real data is forbidden")
        if x.observed_at > generated_at:
            raise ValidationError("Cannot cite future observations")
        # Time window is a publication window for this narrowly-scoped fixture.
        pub_date = x.published_at.astimezone(timezone.utc).date()
        if not (range_from <= pub_date < range_to):
            raise ValidationError("Publication outside declared UTC window")

    if source_outcome == "OK":
        status = "COMPLETE"
    elif rows:
        status = "PARTIAL"
    elif source_outcome == "NO_RESULTS":
        status = "INSUFFICIENT_EVIDENCE"
    else:
        status = "BLOCKED"

    evidence = []
    metrics = []
    for row in rows:
        iso = row.observed_at.astimezone(timezone.utc).isoformat()
        reference = f"fixture:{row.platform}:{row.publication_id}:{iso}"
        source_attempt = "synthetic-source-attempt:001"
        evidence.append({
            "evidence_id": reference,
            "source_ref": reference,
            "source_class": "SYNTHETIC_FIXTURE",
            "retrieved_at": iso,
            "published_at": row.published_at.astimezone(timezone.utc).isoformat(),
            "date_confidence": "HIGH",
            "entity_scope": f"{row.platform}:{row.publication_id}",
            "claim_or_observation": "Synthetic view-count observation",
            "exact_quote_ref": None,
            "relevance": "DIRECT",
            "evidence_strength": "INDETERMINATE",
            "engagement_observed": False,
            "independence_key": f"{row.platform}:{row.publication_id}",
            "source_outcome_ref": source_attempt,
            "notes": "SYNTHETIC FIXTURE; not third-party evidence",
        })
        metrics.append({
            "observation_id": reference,
            "evidence_id": reference,
            "source_outcome_ref": source_attempt,
            "subject_id": f"{row.platform}:{row.publication_id}",
            "metric": "PUBLIC_VIEW_COUNT_FIXTURE",
            "value": row.views if row.views is not None else "UNKNOWN",
            "unit": "views",
            "observed_at": iso,
            "provenance": "SYNTHETIC_FIXTURE",
            "storage_disposition": "IN_MEMORY_EXPERIMENT_ONLY",
        })

    # Sample sorting reuses the synthetic-only helper. It is NOT a derived
    # YouTube metric, creator comparison or ranking of a country.
    ranked_refs: list[str] = []
    ranking_note = "NO_OBSERVATIONS"
    if rows and any(row.views is not None for row in rows):
        try:
            ranked = rank_sample(rows, limit=limit, population_coverage_verified=population_coverage_verified)
            ranked_refs = [
                next(e["evidence_id"] for e in evidence if e["entity_scope"] == f"{rows[0].platform}:{result['publication_id']}")
                for result in ranked["results"]
            ]
            ranking_note = ranked["population"]
        except (InsufficientEvidence, ValidationError):
            ranking_note = "NOT_COMPARABLE"
    if limit < 1 or limit > 100:
        raise ValidationError("Invalid limit")

    result = {
        "research_execution_id": research_execution_id,
        "research_intent": research_intent,
        "primary_entity": primary_entity,
        "market": market,
        "language": language,
        "range_from": range_from.isoformat(),
        "range_to": range_to.isoformat(),
        "generated_at": generated_at.astimezone(timezone.utc).isoformat(),
        "query_plan": [{
            "question": "Fixture-only search, no platform API",
            "source_classes": ["SYNTHETIC_FIXTURE"],
            "source_constraints": "OFFLINE_NO_NETWORK",
        }],
        "source_outcomes": [{
            "source_ref": "synthetic-source-attempt:001",
            "source_class": "SYNTHETIC_FIXTURE",
            "outcome": source_outcome,
            "checked_at": generated_at.astimezone(timezone.utc).isoformat(),
        }],
        "coverage": {
            "actual_scope": "SYNTHETIC_FIXTURE_ONLY",
            "source_attempts": 1,
            "observed_publication_count": len(rows),
            "geography_basis": "UNKNOWN",
            "population_verified": False if not population_coverage_verified else "SYNTHETIC_FIXTURE_ONLY",
            "report_is_real_market_research": False,
        },
        "evidence_clusters": evidence,
        "counterevidence": [],
        "freshness_verdicts": [],
        "status": status,
        "unknowns": [
            "No real platform coverage, license, audience geography, or data acquisition verified",
        ],
        "reuse_notes": ["Synthetic experiment only, in-memory result"],
        "intelligence": {
            "schema_family": "INTELLIGENCE_SYNTHETIC_EXTENSION",
            "schema_version": "offline-exp-0.1",
            "metric_observations": metrics,
            "ranked_evidence_refs": ranked_refs,
            "ranking_scope": ranking_note,
            "metric_definition": "RAW_VIEW_COUNT_FIXTURE",
            "derived_metrics_performed": False,
            "external_calls_performed": False,
        },
    }
    if not _REQUIRED_ENVELOPE_KEYS.issubset(result):
        raise ValidationError("Missing research envelope field")
    if result["status"] not in RESEARCH_STATUSES:
        raise ValidationError("Invalid report status")
    return result
