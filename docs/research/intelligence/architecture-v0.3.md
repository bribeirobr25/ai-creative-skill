# Intelligence Architecture v0.3 · consolidated candidate · 2026-10-24

**Authority status:** DOCUMENTED CANDIDATE / `GATE_0_NOT_PASSED` / OWNER DECISION PENDING / NO RELEASE. See [STATUS.md](STATUS.md) for the single current status and stages S0–S6. Supersedes v0.1/v0.2 for proposed design; those documents remain evidence of historical drafts.

## Goal and modality

In-house provider-neutral **Content, Product and Advertising Intelligence** for a single operator, supporting both **owner-authorized analytics** and **appropriately licensed external market discovery**. No vidIQ/Orthogonal runtime reliance or unlicensed scraping. No universal viral score, automatic spend, publishing, or compulsory MCP/server/dashboard. Candidate implementation starts offline with Python stdlib, no real data.

## Canonical ownership, one authority per concern

| Concern | Canonical owner | Proposed new scope |
|---|---|---|
| Task intent, project scope, permitted side effects | Stage 0, Research Work Profile, Project Profile, AUTONOMY_ENVELOPE | No second task owner, permission ledger or authorization state |
| Source outcome, plan, Evidence Record, Evidence Cluster and research result | RESEARCH_EVIDENCE_SYNTHESIS | Preserve existing 11 outcomes and `research_execution` output schema; do not invent new status |
| Ad observations, creative variants and L0–L3 evidence strength | AD_FUNNEL_INTELLIGENCE | Domain ad result references `research_execution_ref`; not nested competing ad authority |
| Product/listing/seller identity | PRODUCT_MARKETPLACE_INTELLIGENCE | Link IDs only with provenance, never by visual resemblance alone |
| Creative publication and campaign performance lineage | Execution Contracts §23.1 and Architecture §11.1 | Reuse publication_id / asset_id / post_or_ad_id rather than duplicate them |
| Deterministic performance statistics | **UNRESOLVED METHOD OWNER** | Proposed age cohorts, velocity, outlier, coverage and uncertainty need either a versioned Research Evidence Synthesis amendment (including existing `engagement_observed`) or a newly approved Specialist Method under the Growth Rule; do not invent a third unregistered category |
| Source documentation, field-level policy facts | Execution Contracts §24 Provider Onboarding · LATER | Future adapter registry describes source facts and rights only. Architecture §24.1 DATA-SOURCE CONNECTORS is explicitly NOT CURRENT CAPABILITIES; enable via separate acceptance |
| Paid sources and approvals | Execution Contracts §3–4.1, §26 stop semantics | Approval+Budget Ledger+operation-binding, never `derived_permission` or access-token alone |
| Handoff | Execution Contracts V2.3 HANDOFF_PACKET | `permissions_carried: NONE`, `action_authority_recheck_required: true` |
| Publication safety | ADR-0001, proposed ADR-0003 / PR #20 | Prepublication guard, distinct from Intelligence policy |

## Candidate data flow

User intent → Stage 0/Research Work Profile → canonical research_execution → bounded `intelligence_query` filter → source eligibility/rights **descriptive** preflight → existing authorization gate → observed source outcomes + canonical Evidence Records and Evidence Clusters → deterministic metric helper if operation permitted → domain method synthesizes → report with coverage/unknowns/stop → optional HANDOFF_PACKET; action authority rechecked.

**Evidence Record** (one primary observation) is NOT an **Evidence Cluster** (theme/claim with evidence refs and independence key). `MetricObservation` references research_execution_id, evidence_id and source_outcome_ref without independent provenance or source outcomes. Methods may add namespaced metrics, but not duplicate the research result or change its owner. Consuming Ad/Funnel and Product outputs point back to the research execution.

## Policy and method contracts

- One proposed `SourceCapabilityRecord` **target schema, not the current offline implementation** is pending an owner-controlled §24 amendment; there is currently no accepted live field schema. Candidate descriptive fields: `source_id`, `provider`, `operation`, `source_kind`, `policy_ref`, `fields`, `transformations`, `geography_basis`, `time_basis`, `retention_limit_by_data_class`, `redistribution_rights`, `verification_evidence_ref`, `reviewed_at`, `expires_at`, `revoked`. Project scopes, approval status and execution authority belong to AUTONOMY_ENVELOPE and the Project Profile, NOT this record.
- Separate source factual rights (endpoint, operation, fields, transformation, geo/time meaning, retention/TTL, redistribution, status/expiry) from user/project authorization (Project Profile + AUTONOMY_ENVELOPE) and paid approval/ledger.
- Unknown rights, missing rights evidence or unapproved Analytics & Reporting amendment => no derived real analytics; request can remain PARTIAL/BLOCKED through existing research/stop status owner. No free-form `NOT_PERMITTED` source enum until an explicit owner-controlled spec amendment.
- `viewCount` cumulative isn't delta; creator locale isn't audience locale; active advertisement isn't sale or return on ad spend.
- Historical matched-age outlier needs lawful historical snapshots. Without those it is NOT AVAILABLE, regardless of an elegant synthetic formula.
- Source-specific retrieval and retention must not silently cross over between owner-channel YouTube Analytics and third-party Data API or Meta ad-account data versus Ad Library public datasets.
- `UNKNOWN` is never 0. Missing any ranking-affecting counters prevents claiming complete national ranking.

## Gates before code promotion

**G0-01:** one research owner and canonical vocabulary; Evidence separate from Clusters.
**G0-02:** one typed MetricObservation, stable IDs and provenance.
**G0-03:** no paid call before bound Approval + Budget Ledger.
**G0-04:** field/purpose/operation rights, storage/expiry/revocation with authoritative verification.
**G0-05:** typed country basis, time basis, comparable snapshots and population/coverage.

Existing isolated, synthetic-only experiments remain research evidence, NOT accepted formulas or canonical functionality. Further experiments and production promotion remain under the owner's explicit scope decision. Code under src/ requires inventory/Manifest/validation governance change, coordinated with the independent 2.6 candidate. Importing experiments from src/ is prohibited.

## Decisions not assumed

Owner account-first is an attractive first live path, not an automatic license or final decision. Product/Ads third-party discovery remains a separate research route. API-key possession != Analytics-derived permission; model creativity != evidence confidence. S4 starts after consolidated lab with testable resilience hypotheses.

**No merge, payments, provider calls, source storage, release or changes to PR #17 are authorized by this proposal.** Existing Research Evidence Synthesis §§3, 13 and 17 do not adopt foreign engagement formulas, thresholds or persistent watchlists, so the metric method choice requires an explicit owner-controlled version and Manifest change. Future direct capability invocation must satisfy [ADR-0002](../../decisions/ADR-0002-capability-bounded-invocation.md), T1–T7; see [Issue #1](https://github.com/bribeirobr25/ai-creative-skill/issues/1).
