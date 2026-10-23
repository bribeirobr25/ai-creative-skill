# S2 · Contract compatibility canary (synthetic only) · 2026-10-23

**Status:** PROPOSED / OFFLINE / NO_CANON / NO_REAL_SOURCE / NO_MERGE / NO_RELEASE.

This folder is a *candidate*, not a second research execution runtime. It lives in a branch stacked on [PR #18](https://github.com/bribeirobr25/ai-creative-skill/pull/18), independently of [PR #19](https://github.com/bribeirobr25/ai-creative-skill/pull/19). It changes no source skill, SKILL.md, V2.5, release, real API access, persistence or canonical task authority. Python standard library only.

Run: python -m unittest discover -s experiments/intelligence_contracts -p 'test_*.py' -v

**Evidência de execução:** [42/42 testes PASS no commit 9c5cff1c](https://github.com/bribeirobr25/ai-creative-skill/actions/runs/40019484706), incluindo validações de cópias não independentes, evidência órfã, timestamps, fonte com falha e limites de autoridade. [Relatório S2 com gates e pendências](S2-compatibility-review-2026-10-23.md). O CI testa o candidato offline, não valida direitos reais.

## Verified source-of-truth mapping

| Authoritative document | Protected owner / vocabulary | What candidate checks |
|---|---|---|
| Research Evidence Synthesis Pre-v0.3, §6 | 11 Source Outcomes including NO_RESULTS, PAYMENT_REQUIRED, SCHEMA_DRIFT, SKIPPED_UNCONFIGURED | Exact vocabulary; distinct research statuses; no positive evidence from NO_RESULTS |
| Same, §§7–9 | Evidence Record is source observation; Evidence Cluster has cluster_id and evidence references | Evidence supplied through a separate index owned by research; clusters reference evidence by ID; never reinterpret individual Evidence Record as a Cluster |
| Same, §14 | research_execution envelope, COMPLETE/PARTIAL/INSUFFICIENT_EVIDENCE/BLOCKED | Required envelope keys, dates and extension, preserving owner |
| Execution Contracts Pre-v0.21, §4.1 | Paid Research requires applicable Approval **plus** Budget Ledger reservation bound to operation | No paid execution possible here, even if a fake boolean or refs are supplied |
| Same, V2.3 HANDOFF_PACKET | Lineage transfers, not authority: permissions_carried NONE and action_authority_recheck_required true | Rechecks in synthetic candidate |
| Architecture PR #18 v0.2 §4 | intelligence_query, operation-scoped SourceCapabilityRecord, MetricObservation with Evidence reference | Explicit geo/time/metric semantics; source-purpose-field-transformation checks; observation tied to evidence/attempt/execution |

**Important reconciliation with PR #19:** the existing research_bridge.py records per-publication Evidence directly as elements of evidence_clusters. The Research Evidence Synthesis method defines these as separate layers. Its current metric_observations also use short fields such as metric/value rather than the v0.2 candidate's metric_name/metric_value, and lack research_execution_id on each metric. Therefore PR #19's experimental bridge **must NOT be called canonical or assumed compatible**. It needs an explicit, reviewed adapter/migration after S2. The S2 tests deliberately reject the legacy Evidence-as-Cluster shape.

## Candidate contracts, not new canonical authority

- **validate_query_filter:** validates operation, declared geo basis, time-window meaning/zone and numeric limit. It makes no query and never substitutes creator country for audience country or a cumulative counter for period gains.
- **validate_research_execution(envelope, evidence_by_id=...):** validates a synthetic research_execution and an **external index** of canonical Evidence Records, without adding a second source truth inside intelligence. Metrics must link to the original research_execution_id, evidence_id and source_outcome_ref. A national ranking cannot be complete when source/population coverage or counters are unknown.
- **evaluate_source_candidate:** simulates the proposed SourceCapabilityRecord. Checks operation, explicit purpose, geo/time meaning, metric, field, processing/transformation and paid-binding shapes. The return flags may_call_external_api, may_persist and may_spend are **always false**. An eligible fixture means **only that fake inputs satisfy this synthetic shape**, not platform approval.
- **validate_handoff:** checks V2.3 handoff authority boundary. Downstream creative work requires new permission before generating, publishing or spending.

No validator evaluates actual YouTube/Meta legal terms, freshness of provider policy, real credentials, data sovereignty/GDPR, source authorizations, field-level redistribution, pricing or provider quotas. S3 must build and verify the **real** Source Permission Gate before access.

## Stage gates and unmet prerequisites

- **S2 contract canary:** automated fixtures and adversarial tests. Green CI shows code behavior only. Method owner acceptance and adapter mapping remain review items.
- **S3 permission source gate:** authoritative versioned policy records, validated exact endpoint/operation and purpose, token scope, data field, transformation, collection, retention/TTL, revocation, audit and paid Approval+Ledger binding. Fail closed on unavailable evidence.
- **S4:** stress tests, fault injection, permission expiry and realistic Monte Carlo (offline).
- **S5/S6:** only authorized read-only provider canaries, integration into Core and host QA after explicit owner approval.

**No authorization to merge:** stacked PR targets architecture proposal, not main. No upstream PR is promoted. PR #17 stays untouched.
