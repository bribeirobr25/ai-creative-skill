"""Pure adapter from the S2 query proposal to an S3 permission request.

This does NOT execute a query or inherit authority from the Research envelope.
It intentionally requires an explicit single platform and fresh task purpose.
S2 remains owner of the query contract; S3 only checks candidate rights.
"""
from __future__ import annotations

from typing import Mapping
from contract_canary import validate_query_filter
from policy_gate import InvalidContract, validate_request


def project_s2_query(
    query: Mapping, *,
    project_id: str, purpose: str, fields: list[str],
    transformations: list[str], storage_mode: str = "TRANSIENT_ONLY",
    retention_days: int = 0, estimated_calls: int = 1,
    requires_paid: bool = False, requests_raw_media: bool = False,
    background_collection: bool = False,
) -> dict:
    validate_query_filter(query)
    platforms = query["platforms"]
    if len(platforms) != 1:
        raise InvalidContract("MULTI_PLATFORM_QUERY_REQUIRES_SEPARATE_PREFLIGHTS")
    geo, window = query["geographic_filter"], query["time_filter"]
    # No conversion of country, audience basis, temporal basis or limits.
    projected = {
        "operation": query["operation"], "platform": platforms[0],
        "project_id": project_id, "purpose": purpose,
        "country": geo["code"], "geography_basis": geo["meaning"],
        "time_basis": window["meaning"],
        "window_start": window["start_inclusive"],
        "window_end": window["end_exclusive"],
        "fields": list(fields), "transformations": list(transformations),
        "storage_mode": storage_mode, "retention_days": retention_days,
        "requires_paid": requires_paid,
        "requests_raw_media": requests_raw_media,
        "background_collection": background_collection,
        "estimated_calls": estimated_calls,
    }
    validate_request(projected)
    return projected
