"""Experimental bridge into the existing Research Evidence Synthesis *method* contract.

This mirrors the research_execution OUTPUT described in references, NOT a live
schema, canonical runtime or plugin installation. Only synthetic fixtures:
there is NO network, API client, source storage, publication or billing.
"""
from __future__ import annotations

from datetime import date, datetime, timezone
from typing import Iterable
from urllib.parse import quote

from .engine import Observation, ValidationError, InsufficientEvidence, unique_observations, rank_sample
from .policy_gate import validate_fixture_verdict, InvalidContract


from .vocabulary import SOURCE_OUTCOMES, RESEARCH_STATUSES, RESEARCH_REQUIRED
_ALLOWED_WITH_ROWS = frozenset({"OK", "PARTIAL", "RATE_LIMITED", "TIMEOUT"})
_REQUIRED_ENVELOPE_KEYS = RESEARCH_REQUIRED


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
    requested_national_top: bool = False,
    source_coverage_verified: bool = False,
    negative_coverage_satisfies_request: bool = False,
    policy_decision: dict,
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
    if type(range_from) is not date or type(range_to) is not date:
        raise ValidationError("Date window requires plain date objects")
    if range_from >= range_to:
        raise ValidationError("End exclusive must follow start")
    if not isinstance(generated_at, datetime) or generated_at.tzinfo is None or generated_at.utcoffset() is None:
        raise ValidationError("Generated-at timestamp must be timezone-aware")
    if type(source_outcome) is not str or source_outcome not in SOURCE_OUTCOMES:
        raise ValidationError("Invalid source outcome")
    if type(limit) is not int or not 1 <= limit <= 100:
        raise ValidationError("Invalid limit")
    if any(type(x) is not bool for x in (
        population_coverage_verified, requested_national_top,
        source_coverage_verified, negative_coverage_satisfies_request,
    )):
        raise ValidationError("Coverage and intent flags must be booleans")
    if requested_national_top and negative_coverage_satisfies_request:
        raise ValidationError("A ranking request cannot be answered by an absence-only completion rule")
    if negative_coverage_satisfies_request and source_outcome != "NO_RESULTS":
        raise ValidationError("Negative completion intent requires NO_RESULTS outcome")
    try:
        policy_decision = validate_fixture_verdict(policy_decision)
    except (InvalidContract, TypeError, ValueError) as exc:
        raise ValidationError("Explicit complete synthetic policy verdict required") from exc
    is_policy_blocked = policy_decision["decision"] == "BLOCKED"
    if is_policy_blocked:
        source_outcome = "SKIPPED_UNCONFIGURED"
        # A blocked operation must never consume data or report source success.
        if list(observation_rows):
            raise ValidationError("Blocked source may not yield observations")
        observation_rows = []
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

    if is_policy_blocked:
        status = "BLOCKED"
    elif source_outcome == "OK":
        status = "COMPLETE"
    elif rows:
        status = "PARTIAL"
    elif source_outcome == "NO_RESULTS":
        # A fully completed empty search may answer an ABSENCE question, but
        # it does not answer a request for a Top N of existing videos.
        status = (
            "COMPLETE"
            if negative_coverage_satisfies_request and source_coverage_verified
            else "INSUFFICIENT_EVIDENCE"
        )
    else:
        status = "BLOCKED"

    evidence = []
    metrics = []
    evidence_by_publication: dict[tuple[str, str], str] = {}
    for row in rows:
        iso = row.observed_at.astimezone(timezone.utc).isoformat()
        # Encode each identifier independently. Raw ':' within either field
        # must not collide with the ':' field delimiter in an evidence ID.
        subject = f"{quote(row.platform, safe='')}:{quote(row.publication_id, safe='')}"
        reference = f"fixture:{subject}:{iso}"
        evidence_by_publication[(row.platform, row.publication_id)] = reference
        source_attempt = "fixture:source-attempt:001"
        evidence.append({
            "evidence_id": reference,
            "source_ref": reference,
            "source_class": "SYNTHETIC_FIXTURE",
            "retrieved_at": iso,
            "published_at": row.published_at.astimezone(timezone.utc).isoformat(),
            "date_confidence": "HIGH",
            "entity_scope": subject,
            "claim_or_observation": "Synthetic view-count observation",
            "exact_quote_ref": None,
            "relevance": "DIRECT",
            "evidence_strength": "INDETERMINATE",
            "engagement_observed": False,
            "independence_key": subject,
            "source_outcome_ref": source_attempt,
            "notes": "SYNTHETIC FIXTURE; not third-party evidence",
        })
        metrics.append({
            "observation_id": reference,
            "research_execution_id": research_execution_id,
            "evidence_id": reference,
            "source_outcome_ref": source_attempt,
            "subject_id": subject,
            "metric_name": "PUBLIC_VIEW_COUNT_FIXTURE",
            "metric_value": row.views if row.views is not None else "UNKNOWN",
            "observation_basis": "PLATFORM_REPORTED_CUMULATIVE",
            "measurement_window": "UNKNOWN",
            "geography_meaning": "UNKNOWN",
            "population_coverage": "UNKNOWN",
            "license_policy_ref": "fixture-only",
            "unit": "views",
            "observed_at": iso,
            "provenance": "SYNTHETIC_FIXTURE",
            "storage_disposition": "IN_MEMORY_EXPERIMENT_ONLY",
        })

    # Sample sorting reuses the synthetic-only helper. It is NOT a derived
    # YouTube metric, creator comparison or ranking of a country.
    ranked_refs: list[str] = []
    ranking_note = "NO_OBSERVATIONS"
    verified_scope = (
        population_coverage_verified and source_coverage_verified
        and source_outcome == "OK"
    )
    if rows and any(row.views is not None for row in rows):
        try:
            ranked = rank_sample(
                rows, limit=limit, requested_national_top=requested_national_top,
                population_coverage_verified=verified_scope,
            )
            ranked_refs = [
                evidence_by_publication[(rows[0].platform, result["publication_id"])]
                for result in ranked["results"]
            ]
            ranking_note = ranked["population"]
        except (InsufficientEvidence, ValidationError):
            ranking_note = "NOT_COMPARABLE"
    # A source attempt can be OK yet the research conclusion insufficient.
    # Separate source retrieval outcome from the ranking deliverable status.
    if requested_national_top and rows:
        if not verified_scope:
            status = "INSUFFICIENT_EVIDENCE"
            ranking_note = "NATIONAL_COVERAGE_UNVERIFIED"
            ranked_refs = []
        elif ranking_note in ("NOT_COMPARABLE", "NO_OBSERVATIONS"):
            status = "INSUFFICIENT_EVIDENCE"
            ranking_note = "NATIONAL_RANKING_UNDETERMINED"
            ranked_refs = []
    elif source_outcome != "OK" and ranking_note == "COMPLETE":
        ranking_note = "OBSERVED_SAMPLE_ONLY"
    elif source_outcome == "OK" and rows:
        if all(r.views is None for r in rows):
            status = "INSUFFICIENT_EVIDENCE"
        elif ranking_note == "NOT_COMPARABLE" or any(r.views is None for r in rows):
            status = "PARTIAL"

    clusters = [{
        "cluster_id": "cluster:" + e["entity_scope"],
        "question_or_theme": "Synthetic publication metric",
        "supporting_evidence_refs": [e["evidence_id"]],
        "counterevidence_refs": [],
        "independent_source_count": 1,
        "uncertainty": "SYNTHETIC_FIXTURE_ONLY",
    } for e in evidence]
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
            "source_ref": "fixture:source-attempt:001",
            "source_class": "SYNTHETIC_FIXTURE",
            "outcome": source_outcome,
            "checked_at": generated_at.astimezone(timezone.utc).isoformat(),
        }],
        "coverage": {
            "actual_scope": "SYNTHETIC_FIXTURE_ONLY",
            "source_attempts": 1,
            "observed_publication_count": len(rows),
            "geography_basis": "UNKNOWN",
            "population_verified": "SYNTHETIC_FIXTURE_ONLY" if verified_scope else False,
            "report_is_real_market_research": False,
            "source_coverage_verified": source_coverage_verified,
            "requested_national_top": requested_national_top,
            "negative_coverage_satisfies_request": negative_coverage_satisfies_request,
        },
        "evidence_clusters": clusters,
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
            "policy_shape_decision": policy_decision["decision"],
            "stop_code": (
                "STOP_POLICY_REJECTION" if is_policy_blocked
                else ("STOP_REQUIRED_AUTHORITY_MISSING" if status == "BLOCKED"
                      and source_outcome in ("AUTH_FAILED", "PAYMENT_REQUIRED")
                      else ("STOP_REQUIRED_VERIFICATION_UNAVAILABLE"
                            if status == "BLOCKED" else None))
            ),
            "metric_definition": "RAW_VIEW_COUNT_FIXTURE",
            "derived_metrics_performed": False,
            "external_calls_performed": False,
        },
    }
    if not _REQUIRED_ENVELOPE_KEYS.issubset(result):
        raise ValidationError("Missing research envelope field")
    if result["status"] not in RESEARCH_STATUSES:
        raise ValidationError("Invalid report status")
    # This index is a synthetic test harness convenience, not a second
    # canonical owner. The Research Evidence method owns real Evidence Records.
    result["fixture_evidence_index"] = {e["evidence_id"]: e for e in evidence}
    return result
