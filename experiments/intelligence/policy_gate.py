"""S3 policy preflight laboratory. PURE FUNCTIONS, SYNTHETIC FIXTURES ONLY.

Never calls an API, stores data, spends money, opens a network client, or
considers a real-source capability to be authorized. This is deliberately
not an implementation of provider access or a legal/contractual grant.
"""
from __future__ import annotations

from datetime import date, datetime, timedelta, timezone
from typing import Mapping
from .vocabulary import GEO_MEANINGS, TIME_MEANINGS

TRANSFORMATIONS = frozenset({"DISPLAY_NATIVE", "DERIVE_RATIO", "SUMMARIZE"})
ACTIONS = frozenset({"READ", "PROCESS", "DERIVE", "PERSIST", "REDISTRIBUTE"})
STORAGE_MODES = frozenset({"NONE", "TRANSIENT_ONLY", "PERSIST"})
SOURCE_KINDS = frozenset({"SYNTHETIC_FIXTURE", "OFFICIAL_API", "LICENSED_THIRD_PARTY"})

class InvalidContract(ValueError):
    """Invalid configuration cannot quietly become authorization."""


def require(condition: bool, label: str) -> None:
    if not condition:
        raise InvalidContract(label)


def text_field(data: Mapping, key: str) -> str:
    value = data.get(key)
    require(type(value) is str and bool(value.strip()), "INVALID_" + key.upper())
    return value


def mapping(value: object, label: str) -> Mapping:
    require(isinstance(value, Mapping), "INVALID_" + label)
    return value


def string_list(value: object, label: str) -> list[str]:
    require(type(value) is list and all(type(x) is str and bool(x.strip()) for x in value),
            "INVALID_" + label)
    require(len(value) == len(set(value)), "DUPLICATE_" + label)
    return value


def aware_instant(value: object, label: str) -> datetime:
    require(type(value) is str, "INVALID_" + label)
    try:
        instant = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError) as exc:
        raise InvalidContract("INVALID_" + label) from exc
    require(instant.tzinfo is not None and instant.utcoffset() is not None,
            "NAIVE_" + label)
    return instant.astimezone(timezone.utc)


def date_field(value: object, label: str) -> date:
    require(type(value) is str, "INVALID_" + label)
    try:
        result = date.fromisoformat(value)
    except ValueError as exc:
        raise InvalidContract("INVALID_" + label) from exc
    require(result.isoformat() == value, "INVALID_" + label)
    return result


def validate_request(raw: Mapping) -> Mapping:
    q = mapping(raw, "REQUEST")
    for key in ("operation", "platform", "project_id", "purpose", "country",
                "geography_basis", "time_basis"):
        text_field(q, key)
    start = date_field(q.get("window_start"), "WINDOW_START")
    end = date_field(q.get("window_end"), "WINDOW_END")
    require(start < end, "INVALID_REQUEST_WINDOW")
    require(q["geography_basis"] in GEO_MEANINGS, "UNRECOGNIZED_GEO_BASIS")
    require(q["time_basis"] in TIME_MEANINGS, "UNRECOGNIZED_TIME_BASIS")
    text_field(q, "requested_metric")
    fields = string_list(q.get("fields"), "FIELDS")
    require(bool(fields), "EMPTY_FIELDS")
    changes = string_list(q.get("transformations"), "TRANSFORMATIONS")
    require(bool(changes) and set(changes) <= TRANSFORMATIONS,
            "UNKNOWN_TRANSFORMATION")
    storage = q.get("storage_mode")
    require(type(storage) is str and storage in STORAGE_MODES, "INVALID_STORAGE_MODE")
    retention = q.get("retention_days")
    require(type(retention) is int and 0 <= retention <= 36500,
            "INVALID_RETENTION_DAYS")
    if storage == "NONE":
        require(retention == 0, "NONE_CANNOT_RETAIN")
    if storage == "TRANSIENT_ONLY":
        require(retention == 0, "TRANSIENT_CANNOT_RETAIN")
    if storage == "PERSIST":
        require(retention > 0, "PERSIST_REQUIRES_TTL")
    if "redistribute_output" in q:
        require(type(q["redistribute_output"]) is bool, "INVALID_REDISTRIBUTION_FLAG")
    for key in ("requires_paid", "requests_raw_media", "background_collection"):
        require(type(q.get(key)) is bool, "INVALID_" + key.upper())
    calls = q.get("estimated_calls")
    require(type(calls) is int and 1 <= calls <= 10000, "INVALID_ESTIMATED_CALLS")
    return q


def validate_capability(raw: Mapping) -> Mapping:
    c = mapping(raw, "SOURCE_CAPABILITY")
    for key in ("source_id", "source_kind", "platform", "operation",
                "adapter_version", "policy_ref", "authorization_state"):
        text_field(c, key)
    require(c["source_kind"] in SOURCE_KINDS, "UNKNOWN_SOURCE_KIND")
    require("projects" not in c, "SOURCE_CAPABILITY_MUST_NOT_OWN_PROJECT_AUTHORITY")
    for key in ("purposes", "countries", "geography_bases",
                "time_bases", "transformations", "documented_metric_support"):
        string_list(c.get(key), key.upper())
    require(set(c["transformations"]) <= TRANSFORMATIONS,
            "UNKNOWN_CAPABILITY_TRANSFORMATION")
    require(set(c["geography_bases"]) <= GEO_MEANINGS, "INVALID_SOURCE_GEO_BASIS")
    require(set(c["time_bases"]) <= TIME_MEANINGS, "INVALID_SOURCE_TIME_BASIS")
    grants = mapping(c.get("field_grants"), "FIELD_GRANTS")
    for field, grant in grants.items():
        require(type(field) is str and bool(field.strip()), "INVALID_GRANTED_FIELD")
        g = mapping(grant, "GRANT")
        text_field(g, "data_class")
        text_field(g, "retention_policy_ref")
        actions = string_list(g.get("actions"), "GRANT_ACTIONS")
        require(set(actions) <= ACTIONS, "INVALID_GRANT_ACTION")
        ttl = g.get("max_retention_days")
        require(type(ttl) is int and 0 <= ttl <= 36500, "INVALID_GRANT_TTL")
        if "PERSIST" in actions:
            require(ttl > 0, "PERSIST_GRANT_REQUIRES_TTL")
    available_start = date_field(c.get("available_from"), "AVAILABLE_FROM")
    available_end = date_field(c.get("available_to"), "AVAILABLE_TO")
    require(available_start < available_end, "INVALID_SOURCE_WINDOW")
    for key in ("reviewed_at", "expires_at"):
        aware_instant(c.get(key), key.upper())
    require(type(c.get("revoked")) is bool, "INVALID_REVOKED")
    quota = c.get("max_calls_per_day")
    require(type(quota) is int and quota >= 0, "INVALID_QUOTA")
    return c


def evaluate(request: Mapping, capability: Mapping, *, now: str) -> dict:
    """Policy-shape evaluation. No result can authorize real execution."""
    q = validate_request(request)
    c = validate_capability(capability)
    instant = aware_instant(now, "NOW")
    reviewed = aware_instant(c["reviewed_at"], "REVIEWED_AT")
    expires = aware_instant(c["expires_at"], "EXPIRES_AT")
    reasons: list[str] = []

    def reject(reason: str, failed: bool) -> None:
        if failed and reason not in reasons:
            reasons.append(reason)

    reject("REAL_SOURCE_NOT_AUTHORIZED", c["source_kind"] != "SYNTHETIC_FIXTURE")
    reject("SYNTHETIC_IDENTITY_FORGED", not c["source_id"].startswith("fixture-") or
           c["platform"].strip().casefold() in
           ("youtube", "meta", "facebook", "instagram", "tiktok") or
           c["source_id"].strip().upper() in
           ("YOUTUBE_DATA_API", "META_AD_LIBRARY", "META_ADS", "TIKTOK"))
    reject("ACCESS_NOT_GRANTED_FOR_FIXTURE",
           c["authorization_state"] != "SIMULATED_VERIFIED")
    reject("OPERATION_MISMATCH", (c["operation"], c["platform"]) !=
           (q["operation"], q["platform"]))
    # Project-specific authority belongs to Project Profile/AUTONOMY_ENVELOPE,
    # never to a provider rights descriptor. This lab does not grant authority.
    reject("PURPOSE_NOT_IN_SCOPE", q["purpose"] not in c["purposes"])
    reject("COUNTRY_NOT_IN_SCOPE", q["country"] not in c["countries"])
    reject("GEOGRAPHY_SEMANTICS_MISMATCH",
           q["geography_basis"] not in c["geography_bases"])
    reject("TIME_SEMANTICS_MISMATCH", q["time_basis"] not in c["time_bases"])
    reject("TIME_WINDOW_OUTSIDE_DECLARED_SCOPE",
           date_field(q["window_start"], "WINDOW_START") <
           date_field(c["available_from"], "AVAILABLE_FROM") or
           date_field(q["window_end"], "WINDOW_END") >
           date_field(c["available_to"], "AVAILABLE_TO"))
    reject("TRANSFORMATION_NOT_GRANTED",
           not set(q["transformations"]) <= set(c["transformations"]))
    reject("METRIC_NOT_SUPPORTED",
           q["requested_metric"] not in c["documented_metric_support"])
    reject("DERIVED_METRIC_REQUIRES_EXPLICIT_TRANSFORM",
           q["requested_metric"] in
           ("OUTLIER_RATIO", "VIEW_VELOCITY", "DERIVED_OUTLIER_SCORE") and
           "DERIVE_RATIO" not in q["transformations"])
    reject("POLICY_NOT_CURRENT", reviewed > instant or expires <= reviewed or
           instant >= expires)
    reject("SOURCE_REVOKED", c["revoked"])
    reject("QUOTA_BUDGET_EXCEEDED", q["estimated_calls"] > c["max_calls_per_day"])

    grants = c["field_grants"]
    for field in q["fields"]:
        grant = grants.get(field)
        if grant is None:
            reject("FIELD_RIGHTS_NOT_ESTABLISHED", True)
            continue
        allowed = set(grant["actions"])
        reject("FIELD_READ_OR_PROCESS_NOT_GRANTED",
               not {"READ", "PROCESS"} <= allowed)
        reject("FIELD_DERIVATION_NOT_GRANTED",
               "DERIVE_RATIO" in q["transformations"] and "DERIVE" not in allowed)
        reject("FIELD_PERSISTENCE_NOT_GRANTED",
               q["storage_mode"] == "PERSIST" and
               ("PERSIST" not in allowed or
                q["retention_days"] > grant["max_retention_days"]))
        reject("FIELD_REDISTRIBUTION_NOT_GRANTED",
               q.get("redistribute_output", False) is True and
               "REDISTRIBUTE" not in allowed)

    reject("PAID_RESEARCH_NOT_ENABLED_IN_S3", q["requires_paid"])
    reject("RAW_MEDIA_NOT_AUTHORIZED_IN_S3", q["requests_raw_media"])
    reject("BACKGROUND_COLLECTION_NOT_AUTHORIZED", q["background_collection"])

    # Even a permitted-looking fixture is NOT a real-world grant. This result
    # deliberately contains no token, external URL, source payload or secret.
    return {
        "decision": "SHAPE_CHECK_PASSED_SYNTHETIC_ONLY" if not reasons else "BLOCKED",
        "reason_codes": reasons,
        "rights_scope": "SYNTHETIC_FIXTURE_ONLY",
        "may_access_real_source": False,
        "may_spend": False,
        "may_store_real_data": False,
        "may_publish": False,
        "simulated_transient_processing": not reasons,
        "simulated_retention_days": (q["retention_days"] if not reasons and
                                     q["storage_mode"] == "PERSIST" else 0),
        "policy_ref_class": "SYNTHETIC_POLICY_TEST_ONLY" if
                            c["source_kind"] == "SYNTHETIC_FIXTURE" else
                            "UNVERIFIED_EXTERNAL_POLICY",
    }


def retention_verdict(*, recorded_at: str, ttl_days: int, now: str,
                      revoked: bool = False) -> dict:
    """Compute a fixture cleanup decision; no data is actually stored/deleted."""
    created = aware_instant(recorded_at, "RECORDED_AT")
    current = aware_instant(now, "NOW")
    require(current >= created, "TIME_TRAVEL_NOT_ALLOWED")
    require(type(ttl_days) is int and 0 <= ttl_days <= 36500, "INVALID_TTL")
    require(type(revoked) is bool, "INVALID_REVOKED")
    expired = (current >= created + timedelta(days=ttl_days))
    outcome = "PURGE_REQUIRED" if revoked or expired else "SIMULATED_VALID"
    return {
        "decision": outcome, "simulated_only": True,
        "actual_deletion_performed": False, "must_invalidate_derivatives": outcome == "PURGE_REQUIRED",
    }
