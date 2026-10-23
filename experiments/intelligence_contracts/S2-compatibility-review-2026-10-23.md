# S2 · Contract compatibility review · 2026-10-23

**Verdict:** `OFFLINE_CONTRACT_CANDIDATE_PASS / CANONICAL_INTEGRATION_NOT_READY / SOURCE_AUTHORIZATION_NOT_VERIFIED`

**Source-of-truth:** Research Evidence Synthesis Pre-v0.3 §§6–9, 14; Execution Contracts Pre-v0.21 §4.1 and V2.3 HANDOFF_PACKET; ADR-0001, ADR-0002; Architecture proposal v0.2 in PR #18; previous synthetic bridge in PR #19.

**Verified execution:** [GitHub Actions S2 contract test run](https://github.com/bribeirobr25/ai-creative-skill/actions/runs/40019484706): **42/42 PASS** at commit `9c5cff1c1212a3838712b1b64c86042eaf1af192`. This CI result concerns synthetic validation tests only. The PR branch also contains workflow and documentation. No real API calls or external data were authorized.

## 1. Gate 0 compatibility matrix

| Gate 0 | Verified in synthetic canary | Still required before production |
|---|---|---|
| G0-01 Owner of research_execution | Checks required canonical envelope keys, source outcome/research status separation, one intelligence extension | Owner review of concrete schema and host Core integration, no second ResearchResult |
| G0-02 Evidence owner | Separate Evidence Record index from Evidence Cluster; every MetricObservation binds research_execution_id, evidence_id and source_outcome_ref; cluster independence and no orphan metrics/rank refs | Refactor PR #19 research_bridge fixture to this proposed shape and test end-to-end with owner method |
| G0-03 Paid authority | No paid call possible, even when fabricated approval/reservation refs supplied; HANDOFF_PACKET carries NONE | Genuine Approval + Budget Ledger reservation, eligible operation and execution fingerprint under Execution Contracts, when paid source is needed |
| G0-04 Processing, storage and rights | Per-operation/purpose/field/transform candidate; unknown rights DENY; real API, persistence and spend always disabled | S3 policy records backed by official rights evidence, verified scopes, refresh, deletion/TTL/revocation and redistribution rules |
| G0-05 Geo/time/ranking meaning | No silent geographic/time meaning substitution; invalid time window/limit rejected; incomplete national coverage and unknown metrics cannot form COMPLETE national ranking | Validate actual provider data coverage; sampling/missingness; historical series rights; source-specific result and fallback semantics |

**Exact canonical source outcomes preserved (11):** OK, NO_RESULTS, PARTIAL, RATE_LIMITED, AUTH_FAILED, PAYMENT_REQUIRED, UNREACHABLE, TIMEOUT, SCHEMA_DRIFT, SKIPPED_UNCONFIGURED, ERROR. The Research method owns these terms, not this experiment.

## 2. Contract mismatch found in PR #19 (not silently corrected)

The current experimental `research_bridge.py` returns **individual Evidence Records** directly inside `evidence_clusters` rather than grouped Evidence Clusters with `cluster_id`, `supporting_evidence_refs` and `counterevidence_refs`. Its `metric_observations` use `metric` and `value`, not `metric_name`/`metric_value`, and lack the per-row `research_execution_id` and several §4.4 metadata fields.

For S2 the Evidence records are passed by an external mapping `evidence_by_id`, with the research owner retaining provenance. This is a proposed **validation interface**, not a new authoritative database or an amendment to the canonical output shape. The validator deliberately rejects the legacy bridge example to make the mismatch visible. A later, reviewed bridge adapter may convert to this representation **only after** schema ownership and destination are confirmed. Until then, PR #19 remains an isolated synthetic laboratory, not canonically integrated.

## 3. Specific safeguards proven by tests

- An AUTH_FAILED, SCHEMA_DRIFT, PAYMENT_REQUIRED or other non-evidentiary source result cannot be treated as positive Evidence, and NO_RESULTS remains a completed negative attempt rather than fabricated items.
- No metric may use a nonexistent, unrelated or unclustered Evidence Record; an evidence_id/source_outcome_ref mismatch is rejected.
- Duplicate evidence in one cluster and independent_source_count inflated by syndicated copies are rejected using independence_key.
- The canary cannot accept a future measurement timestamp as if it were already observed at report generation.
- UNKNOWN counters remain UNKNOWN rather than silently turning into 0; NaN, infinite, negative and boolean counters fail validation.
- A fake positive source capability does not grant real execution; all of may_call_external_api, may_persist and may_spend remain false.
- HANDOFF_PACKET requires lineage, evidence references and permissions_carried NONE with action_authority_recheck_required true.

**These are 42 checks of synthetic code paths, not a cross-PR integration test against the actual PR #19 runtime, not a policy/license clearance, and not host QA.**

## 4. Stage decision

- S2 **offline candidate implementation and contract review:** TESTED / PASS FOR ITS DECLARED FIXTURE SCOPE.
- S2 **canonical acceptance and migration:** NOT APPROVED, dependency on method owner and bridge design.
- S3 **source permissions:** NOT RUN; start with operation and purpose rights, source policy evidence and retention preflight, still offline until lawful permission is established.
- S4 **resilience, quotas, statistical stress:** NOT RUN.
- S5 **real authorized connector:** NOT RUN.
- Security S0 was previously administratively closed by owner attestation in PR #20. That does not waive checking new publications.
- PR #17 website remains untouched; no merge into PR #18 or main is authorized.
