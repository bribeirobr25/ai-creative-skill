# Intelligence · STATUS / Decision Ledger · 2026-10-24

**SINGLE ACTIVE STATUS:** `GATE_0_CONDITIONAL / NO_CANONICAL_INTEGRATION / SOURCE_AUTHORIZATION_PENDING / NO_RELEASE`.
**Authority:** existing SKILL.md, Current Design Manifest, Research Work Profile, Research Evidence Synthesis, Ad/Funnel Intelligence, Product/Marketplace, Execution Contracts and ADR-0001/0002. This document is a **candidate**, not an approval.

**Current candidate documents:** [architecture-v0.3.md](architecture-v0.3.md) and [acceptance-v0.3.md](acceptance-v0.3.md), with this STATUS as the single current stage/authority verdict. Historical v0.1/v0.2, older audits, stages and the PR descriptions are preserved as **historical research**, not parallel current governance. In particular, obsolete claims in older documents such as “S0 open” and “YouTube categorically prohibited” do **not** override this status.

## Single sequence

| Phase | Meaning | State |
|---|---|---|
| S0 | Historic repository safety triage | **CLOSED_BY_OWNER_ATTESTATION_WITH_LIMITS**. New incidents are separate |
| S1 | Synthetic metric invariants PR #19 | TESTED (68 cases) / architecture integration BLOCKED |
| S2 | Contract shapes PR #21 | TESTED (42 cases) / canonical acceptance BLOCKED |
| S3 | Source-policy shape PR #22 | TESTED (71 cases) / real authorization NOT VERIFIED |
| S4 | Fault injection and resilience | NOT STARTED; pause until reconciled lab |
| S5 | Authenticated read-only canary | NOT APPROVED; no tokens/provider calls |
| S6 | Canonical skill integration and release | NOT APPROVED |

**CI GREEN != MERGE READY.** The CC independent review found defects including status/evidence inconsistencies, DST, derived-metric loss across S2→S3, self-declared synthetic source identities, and security scanning blind spots. The PR #19/#21/#22 lab should be replaced by one dedicated, unstacked lab PR based on `main`. No branch is merged simply to reach a green check.

## Owner decisions pending

1. First live data scope: owner-authorized accounts versus third-party public discoveries. Preserve both as distinct future routes, not as interchangeable rights.
2. Host: local private adapter and credentials vs public distributable skill. Default to **private credentials outside Git**, no built-in runtime secrets.
3. Canonical method ownership for deterministic performance metrics and watchlists. Do not silently mutate Research Evidence Synthesis or Ad/Funnel outputs.
4. Alias and provider onboarding amendments: explicit version through Execution Contracts, Design Manifest and appropriate validation gate.
5. Formal acceptance of minimal publication-safety ADR-0003 (#20), after independent review.

## Hard boundaries

- Don't touch PR #17's branch.
- Keep V2.5 immutable and main untouched until explicit, separately reviewed merge.
- No data from YouTube/Meta or other third-party sources in synthetic lab.
- Never interpret `SIMULATION_ELIGIBLE` or `derived_permission=True` as real rights, authorization, spend or storage.
- Do not infer national audience ranking, revenue, conversion or performance from partial counters.
- S0 closed does not resolve licensing of media elements, current Drive links in `src/`, forks or metadata.

**Review requirement:** CC independently evaluates corrected PR heads, integration effects and the final merge plan. All PRs remain Draft until owner acceptance.
