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
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
import re
from unicodedata import normalize

from .vocabulary import (SOURCE_OUTCOMES, RESEARCH_STATUSES, DATE_CONFIDENCE,
                         RELEVANCE, EVIDENCE_STRENGTH, GEO_MEANINGS, TIME_MEANINGS,
                         RESEARCH_REQUIRED)


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
    _require(bool(re.fullmatch(r"[A-Z]{2}", geo["code"])), "Invalid ISO country code")
    _require(geo.get("meaning") in GEO_MEANINGS, "unrecognized geo meaning")
    tf = _obj(q.get("time_filter"), "time_filter")
    _require(tf.get("meaning") in TIME_MEANINGS, "unrecognized temporal meaning")
    _id(tf.get("timezone"), "time_filter.timezone")
    try:
        ZoneInfo(tf["timezone"])
    except (ZoneInfoNotFoundError, ValueError, KeyError) as exc:
        raise ContractViolation("Invalid IANA time zone") from exc
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
    for flag in ("requested_national_top", "source_coverage_verified"):
        _require(type(coverage.get(flag)) is bool, "Coverage flag must be boolean")

    attempts: dict[str, Mapping] = {}
    for raw in _list(data["source_outcomes"], "source_outcomes"):
        s = _obj(raw, "source_outcome")
        ref = _id(s.get("source_ref"), "source_ref")
        _require(ref not in attempts, "duplicate source attempt")
        _require(type(s.get("outcome")) is str and s["outcome"] in SOURCE_OUTCOMES,
                 "source outcome is not canonical")
        attempts[ref] = s
    _require(bool(attempts), "at least one source attempt required")
    if data["status"] == "COMPLETE":
        _require(all(v["outcome"] in ("OK", "NO_RESULTS") for v in attempts.values()),
                 "COMPLETE cannot conceal failed or incomplete source attempts")
        _require(any(v["outcome"] == "OK" for v in attempts.values()) or
                 (coverage.get("source_coverage_verified") is True and
                  coverage.get("negative_coverage_satisfies_request") is True),
                 "COMPLETE empty research requires verified negative intent")

    registry = _obj(evidence_by_id, "evidence_by_id")
    if data["status"] == "COMPLETE" and any(
        v["outcome"] == "OK" for v in attempts.values()
    ):
        _require(bool(registry), "OK with COMPLETE requires Evidence")
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
        independent = {normalize("NFC", registry[ref]["independence_key"].strip())
                       for ref in refs}
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
    _require(not ({"may_spend", "may_publish", "may_access_real_source",
                   "approval_ref", "api_key", "authorization"} & set(intelligence)),
             "intelligence extension cannot define action authority")



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
