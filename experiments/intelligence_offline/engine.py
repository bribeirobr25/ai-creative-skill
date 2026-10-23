"""Offline, synthetic-data-only intelligence experiment.

NO network, API calls, credentials, third-party data, source media or billing.
NO integration with the canonical skill runtime. No YouTube data is permitted here.
Python stdlib only; all observations must carry SYNTHETIC_FIXTURE provenance.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from math import isfinite
from statistics import median
from typing import Iterable
import json
import random


class ValidationError(ValueError):
    """Input breaks an invariant: fail closed rather than invent a metric."""


class InsufficientEvidence(ValueError):
    """No mathematically defensible result for the supplied synthetic sample."""


@dataclass(frozen=True)
class Observation:
    publication_id: str
    channel_id: str
    platform: str
    content_type: str  # 'short' or 'long'
    views: int | None
    observed_at: datetime
    published_at: datetime
    source_kind: str = "SYNTHETIC_FIXTURE"
    geographic_basis: str = "UNKNOWN"

    def __post_init__(self) -> None:
        if self.source_kind != "SYNTHETIC_FIXTURE":
            raise ValidationError("Only synthetic fixtures are allowed in this experiment")
        if not self.publication_id or not self.channel_id or not self.platform:
            raise ValidationError("Stable source identities must be nonempty")
        if self.content_type not in ("short", "long"):
            raise ValidationError("Unknown content type")
        for d in (self.observed_at, self.published_at):
            if d.tzinfo is None or d.utcoffset() is None:
                raise ValidationError("Timezones are required")
        if self.observed_at < self.published_at:
            raise ValidationError("Observation cannot predate publication")
        if self.views is not None and (isinstance(self.views, bool) or not isinstance(self.views, int) or self.views < 0):
            raise ValidationError("Views must be a nonnegative integer or None")

    @property
    def age_hours(self) -> float:
        return (self.observed_at - self.published_at).total_seconds() / 3600


def unique_observations(rows: Iterable[Observation]) -> list[Observation]:
    """Deduplicate an exact observation, never conflate reposted publications.

    Same platform/publication/time with inconsistent metadata or views is a
    conflict, not an invitation to choose the more flattering number.
    """
    index: dict[tuple[str, str, datetime], Observation] = {}
    for item in rows:
        key = (item.platform, item.publication_id, item.observed_at)
        old = index.get(key)
        if old is not None and old != item:
            raise ValidationError("Conflicting duplicate for same publication and time")
        index[key] = item
    return sorted(index.values(), key=lambda v: (v.platform, v.publication_id, v.observed_at))


def _require_derived_permission(allowed: bool) -> None:
    if allowed is not True:
        raise ValidationError("Derived metric permission not established; synthetic algorithms are gated")


def outlier_ratio(
    video: Observation,
    baseline: Iterable[Observation],
    *,
    derived_permission: bool = False,
    min_baseline: int = 3,
    age_tolerance: float = 0.20,
) -> dict:
    """Age-matched creator baseline; all data MUST be synthetic.

    No YouTube- or vidIQ-specific scoring is implemented or reverse-engineered.
    Video and baseline must have the same channel, platform, format and similar
    age. The median is undefined for zero-only baselines.
    """
    _require_derived_permission(derived_permission)
    if min_baseline < 2 or not 0 <= age_tolerance <= 1:
        raise ValidationError("Invalid comparator configuration")
    if video.views is None or video.age_hours <= 0:
        raise InsufficientEvidence("Missing target views or invalid video age")
    dedup = unique_observations(baseline)
    selected = [
        obs.views for obs in dedup
        if obs.publication_id != video.publication_id
        and obs.platform == video.platform
        and obs.channel_id == video.channel_id
        and obs.content_type == video.content_type
        and obs.age_hours > 0
        and abs(obs.age_hours - video.age_hours) / video.age_hours <= age_tolerance
        and obs.views is not None
    ]
    if len(selected) < min_baseline:
        raise InsufficientEvidence("Insufficient comparable baseline sample")
    typical = median(selected)
    if typical <= 0:
        raise InsufficientEvidence("Zero baseline median; ratio undefined")
    ratio = video.views / typical
    if not isfinite(ratio):
        raise ValidationError("Nonfinite ratio")
    return {
        "metric": "OUTLIER_RATIO",
        "metric_version": "offline-exp-0.1",
        "ratio": ratio,
        "median_comparable_views": typical,
        "baseline_n": len(selected),
        "age_hours": video.age_hours,
        "population": "SYNTHETIC_AGE_MATCHED_CHANNEL_BASELINE",
        "scope": "FIXTURE_ONLY_NOT_PLATFORM_RANKING",
    }


def view_velocity(earlier: Observation, later: Observation, *, derived_permission: bool = False) -> dict:
    _require_derived_permission(derived_permission)
    if (earlier.platform, earlier.publication_id, earlier.channel_id, earlier.published_at) != (
        later.platform, later.publication_id, later.channel_id, later.published_at
    ):
        raise ValidationError("Incompatible publication observations")
    if earlier.views is None or later.views is None:
        raise InsufficientEvidence("A view counter is missing")
    elapsed = (later.observed_at - earlier.observed_at).total_seconds() / 3600
    if elapsed <= 0:
        raise InsufficientEvidence("Need observations at strictly increasing times")
    delta = later.views - earlier.views
    if delta < 0:
        raise InsufficientEvidence("Decreasing counter; correction cannot represent growth")
    return {
        "metric": "VIEW_VELOCITY",
        "metric_version": "offline-exp-0.1",
        "views_delta": delta,
        "hours": elapsed,
        "views_per_hour": delta / elapsed,
        "scope": "SYNTHETIC_OBSERVED_INTERVAL_ONLY",
    }


def rank_sample(
    observations: Iterable[Observation], *,
    limit: int,
    requested_national_top: bool = False,
    population_coverage_verified: bool = False,
) -> dict:
    """Sort reported counters, not a derived cross-platform viral score."""
    if limit < 1 or limit > 100:
        raise ValidationError("Limit must be from 1 to 100")
    rows = unique_observations(observations)
    if requested_national_top and not population_coverage_verified:
        raise InsufficientEvidence("National Top N cannot be inferred from an observed sample")
    if not rows:
        raise InsufficientEvidence("No verified synthetic sample")
    platforms = {r.platform for r in rows}
    if len(platforms) != 1:
        raise ValidationError("Different platforms require separate rankings")
    with_count = [r for r in rows if r.views is not None]
    if not with_count:
        raise InsufficientEvidence("No available counters")
    if len({r.observed_at for r in with_count}) != 1:
        raise ValidationError("Mixed observation moments: choose a comparable snapshot")
    ranked = sorted(with_count, key=lambda v: (-v.views, v.publication_id))
    return {
        "metric": "RAW_VIEW_COUNT",
        "population": "COMPLETE" if population_coverage_verified else "OBSERVED_SAMPLE_ONLY",
        "missing_count": len(rows) - len(with_count),
        "results": [{"publication_id": x.publication_id, "views": x.views} for x in ranked[:limit]],
    }


def simulate_operational_resilience(
    *, trials: int = 2000, seed: int = 20261023,
    common_outage_probability: float = 0.10,
    independent_failure_probability: float = 0.15,
) -> dict:
    """Assumption-driven simulation; NOT a forecast of real provider reliability.

    Two hypothetical sources with correlated common-mode outages.
    No input/output links to real APIs. Simple fixed-seed Monte Carlo.
    """
    if not 1 <= trials <= 100000:
        raise ValidationError("Trial count out of bounds")
    for p in (common_outage_probability, independent_failure_probability):
        if not isfinite(p) or not 0 <= p <= 1:
            raise ValidationError("Probability outside [0,1]")
    rng = random.Random(seed)
    complete = partial = blocked = 0
    for _ in range(trials):
        common_down = rng.random() < common_outage_probability
        if common_down:
            working = 0
        else:
            working = sum(rng.random() >= independent_failure_probability for _ in range(2))
        if working == 2:
            complete += 1
        elif working == 1:
            partial += 1
        else:
            blocked += 1
    return {
        "status": "SYNTHETIC_SCENARIO_ONLY",
        "seed": seed, "trials": trials,
        "assumptions": {
            "common_outage_probability": common_outage_probability,
            "independent_failure_probability": independent_failure_probability,
            "sources": 2
        },
        "counts": {"COMPLETE": complete, "PARTIAL": partial, "BLOCKED": blocked}
    }


if __name__ == "__main__":
    print(json.dumps(simulate_operational_resilience(), sort_keys=True))
