# Intelligence · Acceptance Matrix v0.3 · 2026-10-24

**State:** PROPOSED / OWNER_ACCEPTANCE_PENDING / NO_RELEASE / NO_REAL_SOURCE. This is the **single active candidate acceptance matrix**. Earlier matrices are historical. See [STATUS.md](STATUS.md) and [architecture-v0.3.md](architecture-v0.3.md).

| ID | Required behavior / evidence | Current verification | Merge acceptance |
|---|---|---|---|
| INT-C01 | Research Work Profile and Research Evidence Synthesis own `research_execution` and outcome/status vocabulary | Unified PR #23 tests synthetic shape and canonical Markdown parity | Owner method review; no second ResearchResult |
| INT-C02 | Evidence Records separate from Evidence Clusters with correct independent refs | PR #23 synthetic integration and evidence validation | Test actual bridge→validator and mixed sources |
| INT-C03 | MetricObservation IDs and timestamps provenance and derived rights | PR #23 synthetic checks; DST UTC normalization | No real source use until per-operation approval |
| INT-C04 | `AUTH_FAILED` / RATE_LIMITED / PAYMENT_REQUIRED may not become `NO_RESULTS` / COMPLETE | PR #23 synthetic status validation | Negative tests and canonical stop-code mapping |
| INT-C05 | S2→S3 preserves geo/time basis, window, requested metric and project-purpose context | PR #23 synthetic projection | Cross-stage coverage tests, no silent fallback |
| INT-C06 | Real provider disguised as SYNTHETIC_FIXTURE rejected | PR #23 spoofing test / fixture-prefix gating | No runtime client until authenticated evidence from Core |
| INT-C07 | Existing Project Profile/AUTONOMY_ENVELOPE owns project action authority | PR #23 removes project grants from SourceCapabilityRecord | Owner acceptance and host integration |
| INT-C08 | Existing §3–4.1 Approval+Budget Ledger owns paid research | Synthetic candidate has `may_spend=false` | Live paid gate NOT IMPLEMENTED and NOT AUTHORIZED |
| INT-C09 | Storage TTL, data class, field rights, deletion and revocation | PR #23 fixture-only checks | Real policy proof + durable purge integration NOT RUN |
| INT-C10 | Owner-channel and external market discovery have distinct data rights | Documented, not implemented | Decide initial route; verify YouTube/Meta scopes |
| INT-C11 | No implicit creative production, handoff carries no permission | Synthetic HANDOFF_PACKET checks only | [ADR-0002](../../decisions/ADR-0002-capability-bounded-invocation.md) T1–T7 and [Issue #1](https://github.com/bribeirobr25/ai-creative-skill/issues/1): host conformance NOT RUN |
| INT-C12 | Independent security scan and publication safety | PR #20 synthetic and Git regression tests | Independent reviewer validation, accepted ADR-0003 and prepush controls, owner acceptance NOT RUN |
| INT-C13 | No conflict with PR #17 Web/2.6 candidate and immutable V2.5 | CI baseline tests; no src changes | Independent combined-worktree comparison, CC/owner acceptance |
| INT-C14 | Resilience: correlated failures, quota, retries, TTL 29/30/31, cost | S4 NOT RUN | Hypotheses and deterministic oracles first |
| INT-C15 | Real external provider read-only collection and documented costs/coverage | S5 NOT RUN (no calls) | Distinguish documented account access from field-level legal rights, policy, cost and owner authorization before use |

**Scope of green CI:** offline fixture correctness only. This matrix never certifies real analytics rights, platform rate limits, national rankings, market coverage, GDPR compliance, real persistence, approval or release.

**Governance:** Independent review and owner acceptance are separate prerequisites for promotion. Historical #19/#21/#22 experiments are superseded by the consolidated #23 candidate and are not production modules.
