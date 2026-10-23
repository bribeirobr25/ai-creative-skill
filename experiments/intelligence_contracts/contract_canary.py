"""S2 contract canary: strict, synthetic-only validation of PROPOSED interfaces.

Derived from the current RESEARCH_EVIDENCE_SYNTHESIS output/method and
Execution Contracts HANDOFF_PACKET. Not a canonical runtime, provider
connector, rights approval, persistence engine, or API client.
Python standard library only. No network, filesystem, secrets or billing.
"""
from __future__ import annotations

from datetime import date, datetime
from math import isfinite
from typing import Mapping

SOURCE_OUTCOMES = frozenset({
    "OK", "NO_RESULTS", "PARTIAL", "RATE_LIMITED", "AUTH_FAILED",
    "PAYMENT_REQUIRED", "UNREACHABLE", "TIMEOUT", "SCHEMA_DRIFT",
    "SKIPPED_UNCONFIGURED", "ERROR",
})
RESEARCH_STATUSES = frozenset({
    "COMPLETE", "PARTIAL", "INSUFFICIENT_EVIDENCE", "BLOCKED",
})
DATE_CONFIDENCE = frozenset({"HIGH", "MED", "LOW", "UNKNOWN"})
RELEVANCE = frozenset({"DIRECT", "SUPPORTING", "CONTEXTUAL", "TANGENTIAL"})
EVIDENCE_STRENGTH = frozenset({"STRONG", "MODERATE", "WEAK", "INDETERMINATE"})
GEO_MEANINGS = frozenset({
    "AD_DELIVERY_GEO", "CREATOR_REGISTERED_GEO", "AUDIENCE_GEO",
    "SEARCH_RESULT_LOCALE", "SELLER_GEO", "SHIPPING_DESTINATION",
})
TIME_MEANINGS = frozenset({
    "PUBLISHED_DURING_WINDOW", "ACTIVE_DURING_WINDOW",
    "ENGAGEMENT_GAINED_DURING_WINDOW", "OBSERVED_AS_OF",
})
RESEARCH_REQUIRED = frozenset({
    "research_execution_id", "research_intent", "primary_entity",
    "market", "language", "range_from", "range_to", "generated_at",
    "query_plan", "source_outcomes", "coverage", "evidence_clusters",
    "counterevidence", "freshness_verdicts", "status", "unknowns",
    "reuse_notes",
})


class ContractViolation(ValueError):
    """Failed S2 candidate check, never an implied permission decision."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ContractViolation(message)


def _obj(value: object, name: str) -> Mapping:
    _require(isinstance(value, Mapping), name + " must be a mapping")
    return value


def _list(value: object, name: str) -> list:
    _require(type(value) is list, name + " must be a list")
    return value


def _id(value: object, name: str) -> str:
    _require(type(value) is str and bool(value.strip()), name + " must be a nonempty string")
    return value


def _time(value: object, name: str) -> datetime:
    _require(type(value) is str, name + " must be an ISO timestamp")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ContractViolation(name + " must be an ISO timestamp") from exc
    _require(parsed.tzinfo is not None and parsed.utcoffset() is not None,
             name + " requires an offset")
    return parsed


def _date(value: object, name: str) -> date:
    _require(type(value) is str, name + " must be YYYY-MM-DD")
    try:
        parsed = date.fromisoformat(value)
    except ValueError as exc:
        raise ContractViolation(name + " must be YYYY-MM-DD") from exc
    _require(parsed.isoformat() == value, name + " must be YYYY-MM-DD")
    return parsed


def validate_query_filter(query: Mapping) -> None:
    """Candidate typed semantics; no geo/time meaning may be auto-substituted."""
    q = _obj(query, "intelligence_query")
    _id(q.get("operation"), "operation")
    platforms = _list(q.get("platforms"), "platforms")
    _require(bool(platforms) and all(type(p) is str and p.strip() for p in platforms),
             "platforms must contain identifiers")
    geo = _obj(q.get("geographic_filter"), "geographic_filter")
    _id(geo.get("code"), "geographic_filter.code")
    _require(geo.get("meaning") in GEO_MEANINGS, "unrecognized geo meaning")
    tf = _obj(q.get("time_filter"), "time_filter")
    _require(tf.get("meaning") in TIME_MEANINGS, "unrecognized temporal meaning")
    _id(tf.get("timezone"), "time_filter.timezone")
    _require(_date(tf.get("start_inclusive"), "start_inclusive")
             < _date(tf.get("end_exclusive"), "end_exclusive"),
             "query time window must be increasing and end-exclusive")
    ranking = _obj(q.get("ranking"), "ranking")
    _id(ranking.get("metric"), "ranking.metric")
    n = ranking.get("limit")
    _require(type(n) is int and 1 <= n <= 100, "ranking.limit must be an integer 1..100")


def validate_research_execution(
    envelope: Mapping, *, evidence_by_id: Mapping
) -> None:
    """Validate a SYNTHETIC research_execution and an external Evidence index.

    Evidence Records are supplied by the research owner, NOT nested in
    evidence_clusters and NOT duplicated inside the intelligence extension.
    This intentionally rejects PR #19's older bridge fixture shape.
    """
    data = _obj(envelope, "research_execution")
    _require(RESEARCH_REQUIRED <= data.keys(), "missing canonical research envelope keys")
    rid = _id(data["research_execution_id"], "research_execution_id")
    _require(type(data["status"]) is str and data["status"] in RESEARCH_STATUSES,
             "unknown research completion status")
    _require(_date(data["range_from"], "range_from") < _date(data["range_to"], "range_to"),
             "invalid research date window")
    _time(data["generated_at"], "generated_at")
    for key in ("research_intent", "primary_entity", "market", "language"):
        _id(data[key], key)
    for key in ("query_plan", "counterevidence", "freshness_verdicts", "unknowns", "reuse_notes"):
        _list(data[key], key)
    coverage = _obj(data["coverage"], "coverage")
    _require(coverage.get("report_is_real_market_research") is False,
             "S2 cannot validate or approve a real market report")

    attempts: dict[str, Mapping] = {}
    for raw in _list(data["source_outcomes"], "source_outcomes"):
        s = _obj(raw, "source_outcome")
        ref = _id(s.get("source_ref"), "source_ref")
        _require(ref not in attempts, "duplicate source attempt")
        _require(type(s.get("outcome")) is str and s["outcome"] in SOURCE_OUTCOMES,
                 "source outcome is not canonical")
        attempts[ref] = s
    _require(bool(attempts), "at least one source attempt required")

    registry = _obj(evidence_by_id, "evidence_by_id")
    for eid, raw in registry.items():
        ev = _obj(raw, "Evidence Record")
        _require(_id(eid, "Evidence index ID") == ev.get("evidence_id"),
                 "Evidence index mismatch")
        attempt = _id(ev.get("source_outcome_ref"), "Evidence source_outcome_ref")
        _require(attempt in attempts, "Evidence points to nonexistent source attempt")
        _require(attempts[attempt]["outcome"] in ("OK", "PARTIAL", "RATE_LIMITED", "TIMEOUT"),
                 "failed/empty/untrusted source cannot support an Evidence Record")
        _require(ev.get("source_class") == "SYNTHETIC_FIXTURE",
                 "external evidence prohibited in S2")
        _require(attempts[attempt].get("source_class") == ev.get("source_class"),
                 "Evidence source class mismatch")
        for key in ("source_ref", "independence_key", "claim_or_observation"):
            _id(ev.get(key), "Evidence." + key)
        observed = _time(ev.get("retrieved_at"), "Evidence.retrieved_at")
        _require(observed <= _time(data["generated_at"], "generated_at"),
                 "Evidence retrieved after report generation")
        _require(ev.get("date_confidence") in DATE_CONFIDENCE,
                 "invalid Evidence date confidence")
        _require(ev.get("relevance") in RELEVANCE, "invalid Evidence relevance")
        _require(ev.get("evidence_strength") in EVIDENCE_STRENGTH,
                 "invalid Evidence strength")

    used_clusters: set[str] = set()
    clustered_evidence: set[str] = set()
    for raw in _list(data["evidence_clusters"], "evidence_clusters"):
        cluster = _obj(raw, "Evidence Cluster")
        cluster_id = _id(cluster.get("cluster_id"), "cluster_id")
        _require(cluster_id not in used_clusters, "duplicate cluster_id")
        used_clusters.add(cluster_id)
        refs = _list(cluster.get("supporting_evidence_refs"), "supporting_evidence_refs")
        counters = _list(cluster.get("counterevidence_refs"), "counterevidence_refs")
        _require(bool(refs), "cluster without supporting evidence")
        _require(all(type(r) is str and r in registry for r in refs + counters),
                 "cluster points to unknown Evidence")
        _require(len(refs + counters) == len(set(refs + counters)),
                 "repeated/contradictory Evidence in cluster")
        independent = {registry[ref]["independence_key"] for ref in refs}
        _require(type(cluster.get("independent_source_count")) is int and
                 cluster["independent_source_count"] == len(independent),
                 "cluster independent source count does not match provenance")
        clustered_evidence.update(refs + counters)

    intelligence = _obj(data.get("intelligence"), "intelligence extension")
    _require(intelligence.get("external_calls_performed") is False,
             "S2 cannot verify an external API execution")
    _require(intelligence.get("derived_metrics_performed") is False,
             "S2 forbids derived metrics on external data")
    _require(intelligence.get("schema_family") == "INTELLIGENCE_SYNTHETIC_EXTENSION",
             "unexpected intelligence extension type")
    observation_ids: set[str] = set()
    for raw in _list(intelligence.get("metric_observations"), "metric_observations"):
        m = _obj(raw, "MetricObservation")
        mid = _id(m.get("observation_id"), "observation_id")
        _require(mid not in observation_ids, "duplicate observation_id")
        observation_ids.add(mid)
        _require(m.get("research_execution_id") == rid,
                 "metric research_execution_id does not match envelope")
        ev_id = _id(m.get("evidence_id"), "metric.evidence_id")
        _require(ev_id in registry, "metric refers to nonexistent Evidence")
        _require(ev_id in clustered_evidence,
                 "metric Evidence is not included in a canonical cluster")
        _require(m.get("source_outcome_ref") == registry[ev_id]["source_outcome_ref"],
                 "metric source attempt disagrees with Evidence")
        _id(m.get("subject_id"), "metric.subject_id")
        _id(m.get("metric_name"), "metric.metric_name")
        _id(m.get("observation_basis"), "metric.observation_basis")
        _id(m.get("measurement_window"), "metric.measurement_window")
        _id(m.get("geography_meaning"), "metric.geography_meaning")
        _id(m.get("population_coverage"), "metric.population_coverage")
        _id(m.get("license_policy_ref"), "metric.license_policy_ref")
        moment = _time(m.get("observed_at"), "metric.observed_at")
        _require(moment <= _time(data["generated_at"], "generated_at"),
                 "Metric observation after report generation")
        _require(m.get("provenance") == "SYNTHETIC_FIXTURE",
                 "metric is not a synthetic fixture")
        _require(m.get("storage_disposition") == "IN_MEMORY_EXPERIMENT_ONLY",
                 "S2 cannot approve persistence")
        value = m.get("metric_value")
        _require(value == "UNKNOWN" or
                 (type(value) in (int, float) and isfinite(value) and value >= 0),
                 "metric value must be finite nonnegative or UNKNOWN")
    ranked = _list(intelligence.get("ranked_evidence_refs"), "ranked_evidence_refs")
    _require(all(type(ref) is str and ref in clustered_evidence for ref in ranked),
             "ranking uses unclustered or unverified Evidence")
    _require(len(ranked) == len(set(ranked)),
             "ranking repeats Evidence")
    if coverage.get("requested_national_top") is True and data["status"] == "COMPLETE":
        _require(coverage.get("source_coverage_verified") is True and
                 coverage.get("population_verified") == "SYNTHETIC_FIXTURE_ONLY" and
                 all(s.get("outcome") == "OK" for s in attempts.values()),
                 "national top cannot be COMPLETE without full synthetic coverage")
        _require(bool(ranked) and
                 all(m["metric_value"] != "UNKNOWN" for m in intelligence["metric_observations"]),
                 "national top cannot be COMPLETE with unknown metrics")
    _require(intelligence.get("permissions_carried", "NONE") == "NONE",
             "intelligence cannot carry execution authority")


def evaluate_source_candidate(
    query: Mapping, capability: Mapping, *, purpose: str,
    requested_fields: list[str], transformation: str, storage: str = "TRANSIENT_ONLY",
    requires_paid: bool = False, approval_ref: str | None = None,
    reservation_ref: str | None = None
) -> dict:
    """Synthetic policy-shape canary. NEVER returns permission to access a real API.

    The S3 source-policy authority does not yet exist. Even a complete fixture
    returns SYNTHETIC_ELIGIBLE, not an API-execution approval.
    """
    validate_query_filter(query)
    rec = _obj(capability, "SourceCapabilityRecord")
    reasons: list[str] = []
    _require(type(requires_paid) is bool, "requires_paid must be a boolean")
    _require(storage in ("TRANSIENT_ONLY", "PERSIST"), "unknown storage disposition")
    _id(transformation, "transformation")
    _id(purpose, "purpose")
    _require(type(requested_fields) is list and all(type(x) is str and x for x in requested_fields),
             "requested_fields must be names")
    if rec.get("source_kind") != "SYNTHETIC_FIXTURE":
        reasons.append("REAL_SOURCE_NOT_AUTHORIZED_IN_S2")
    if rec.get("operation") != query["operation"] or not rec.get("adapter_version"):
        reasons.append("OPERATION_OR_ADAPTER_UNVERIFIED")
    if rec.get("access_authorization") != "VERIFIED_SYNTHETIC":
        reasons.append("ACCESS_NOT_VERIFIED")
    if rec.get("processing_rights") != "VERIFIED_SYNTHETIC":
        reasons.append("PROCESSING_RIGHTS_UNVERIFIED")
    if purpose not in rec.get("allowed_purposes", []):
        reasons.append("PURPOSE_NOT_AUTHORIZED")
    if query["geographic_filter"]["meaning"] not in rec.get("documented_geo_semantics", []):
        reasons.append("GEO_SEMANTICS_MISMATCH")
    if query["time_filter"]["meaning"] not in rec.get("documented_time_semantics", []):
        reasons.append("TIME_SEMANTICS_MISMATCH")
    if query["ranking"]["metric"] not in rec.get("documented_metric_support", []):
        reasons.append("METRIC_NOT_SUPPORTED")
    field_rights = _obj(rec.get("field_rights", {}), "field_rights")
    if not requested_fields or any(field_rights.get(key) != "VERIFIED_SYNTHETIC"
                                   for key in requested_fields):
        reasons.append("FIELD_RIGHTS_UNVERIFIED")
    if transformation not in rec.get("allowed_transformations", []):
        reasons.append("TRANSFORMATION_NOT_AUTHORIZED")
    if storage != "TRANSIENT_ONLY":
        reasons.append("S2_STORAGE_NEVER_AUTHORIZED")
    if requires_paid:
        if not approval_ref or not reservation_ref:
            reasons.append("PAID_RESEARCH_APPROVAL_LEDGER_NOT_BOUND")
        # Even a claimed binding is not a real Approval+Budget Ledger.
        reasons.append("S2_PAID_CALL_NEVER_AUTHORIZED")
    return {
        "outcome": "SYNTHETIC_ELIGIBLE" if not reasons else "BLOCKED",
        "reasons": reasons,
        "may_call_external_api": False,
        "may_persist": False,
        "may_spend": False,
        "rights_scope": "SYNTHETIC_FIXTURE_ONLY",
    }


def validate_handoff(packet: Mapping) -> None:
    """V2.3 HANDOFF_PACKET authority boundary; never transfer permissions."""
    h = _obj(packet, "handoff_packet")
    required = ("project_id", "from_task_id", "to_task_id", "from_profile", "to_profile",
                "task_outcome", "accepted_constraints", "stable_entities",
                "evidence_items", "explicit_unknowns", "accepted_outputs",
                "protected_state", "invalidated_state")
    for name in required:
        _require(name in h, "missing HANDOFF_PACKET field: " + name)
    for name in ("project_id", "from_task_id", "to_task_id", "from_profile", "to_profile"):
        _id(h[name], "handoff." + name)
    _require(h.get("permissions_carried") == "NONE",
             "HANDOFF_PACKET cannot carry authority")
    _require(h.get("action_authority_recheck_required") is True,
             "downstream authorization must be re-evaluated")
    for name in ("accepted_constraints", "stable_entities", "evidence_items",
                 "explicit_unknowns", "accepted_outputs", "protected_state",
                 "invalidated_state"):
        _list(h[name], name)
    _obj(h["task_outcome"], "handoff.task_outcome")
    for item in h["stable_entities"]:
        entity = _obj(item, "stable_entity")
        _id(entity.get("entity_id"), "stable_entity.entity_id")
        _id(entity.get("entity_type"), "stable_entity.entity_type")
        _list(entity.get("source_refs"), "stable_entity.source_refs")
    for item in h["evidence_items"]:
        ev = _obj(item, "handoff evidence item")
        _id(ev.get("evidence_ref"), "handoff.evidence_ref")
        _require(ev.get("evidence_class") in
                 ("OBSERVED", "USER_PROVIDED", "VERIFIED", "INFERRED", "UNKNOWN"),
                 "invalid evidence class")
        _require(ev.get("confidence") in ("HIGH", "MEDIUM", "LOW", "UNKNOWN"),
                 "invalid evidence confidence")
        _require("freshness" in ev, "handoff evidence freshness missing")
