"""One-off 30k fixed-seed acceptance replay, held on test-only PR #25.

Not part of the #23 shipped synthetic laboratory or source distribution.
"""
import random
import unittest
from datetime import datetime, date, timedelta, timezone

from experiments.intelligence.engine import (
    Observation, ValidationError, InsufficientEvidence,
)
from experiments.intelligence.research_bridge import build_research_execution_fixture
from experiments.intelligence.contract_canary import validate_research_execution
from experiments.intelligence.vocabulary import SOURCE_OUTCOMES
from experiments.intelligence.test_research_bridge import fixture_policy


class IndependentThirtyThousandCaseReplay(unittest.TestCase):
    def test_every_accepted_bridge_envelope_passes_its_canary(self):
        rng = random.Random(20261025)
        zones = (
            "UTC", "Europe/Berlin", "America/Sao_Paulo",
            "Pacific/Kiritimati", "Asia/Kathmandu",
        )
        outcomes = tuple(sorted(SOURCE_OUTCOMES))
        accepted, rejected = 0, 0
        saw_outcomes = set()
        for _ in range(30000):
            base = datetime(2026, 10, 10, tzinfo=timezone.utc)
            moments = [
                base + timedelta(days=rng.randint(0, 14),
                                 hours=rng.randint(0, 23))
                for _ in range(2)
            ]
            rows = []
            for _ in range(rng.randint(0, 6)):
                observed = rng.choice(moments)
                rows.append(Observation(
                    publication_id=rng.choice(
                        ("fixture-a", "fixture-b", "fixture-c")),
                    channel_id=rng.choice(("fixture-ch", "fixture-ch2")),
                    platform=rng.choice(("fixture-p1", "fixture-p2")),
                    content_type=rng.choice(("short", "long")),
                    views=rng.choice((None, 0, 5, 1000)),
                    observed_at=observed,
                    published_at=observed - timedelta(
                        hours=rng.randint(0, 400)),
                    source_kind="SYNTHETIC_FIXTURE",
                ))
            outcome = rng.choice(outcomes)
            saw_outcomes.add(outcome)
            try:
                envelope = build_research_execution_fixture(
                    research_execution_id="fixture-r",
                    research_intent="MARKET_SCAN",
                    primary_entity="synthetic items",
                    market="DE",
                    language="de",
                    range_from=date(2026, 9, 1),
                    range_to=date(2026, 11, 1),
                    observation_rows=rows,
                    source_outcome=outcome,
                    limit=rng.choice((1, 2, 10, 100)),
                    population_coverage_verified=bool(rng.getrandbits(1)),
                    requested_national_top=bool(rng.getrandbits(1)),
                    source_coverage_verified=bool(rng.getrandbits(1)),
                    negative_coverage_satisfies_request=bool(rng.getrandbits(1)),
                    ranking_requested=bool(rng.getrandbits(1)),
                    time_zone=rng.choice(zones),
                    policy_decision=fixture_policy(
                        blocked=bool(rng.getrandbits(1))),
                    generated_at=datetime(
                        2026, 10, 30, tzinfo=timezone.utc),
                )
            except (ValidationError, InsufficientEvidence):
                rejected += 1
                continue
            validate_research_execution(
                envelope, evidence_by_id=envelope["fixture_evidence_index"])
            accepted += 1
        self.assertEqual(set(outcomes), saw_outcomes)
        self.assertGreater(accepted, 1000, "Inadequate accepted fixture coverage")
        self.assertEqual(30000, accepted + rejected)
