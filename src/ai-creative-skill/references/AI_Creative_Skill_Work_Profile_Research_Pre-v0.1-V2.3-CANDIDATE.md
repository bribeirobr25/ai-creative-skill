# AI Creative Skill · Work Profile · Research · Pre-v0.1-V2.3-CANDIDATE

## Status

```text
DOCUMENT TYPE = WORK PROFILE
PROFILE ID = RESEARCH_ONLY
VERSION = Pre-v0.1-V2.3-CANDIDATE
DATE = 2026-10-11
STATUS = ARCHITECTURE-REACTIVATION CANDIDATE · NOT PROMOTED TO 00_ACTIVE
```

Parent architecture: `AI_Creative_Skill_Architecture_Spec_Pre-v0.16-V2.3-CANDIDATE.md`

## 1. Purpose

`RESEARCH_ONLY` owns bounded research, comparison, verification and evidence-synthesis deliverables that have independent user value and may complete without creative generation.

It is an ownership surface, not a second research engine.

## 2. Positive Ownership

Typical examples:

```text
market / trend scan as final deliverable
competitor / product comparison as final deliverable
buyer/review evidence synthesis as final deliverable
product / marketplace lookup
exact product/listing matching
social/video evidence inspection for a research conclusion
fact / claim verification
research-only recommendation or shortlist
```

## 3. Non-Ownership

Do not own merely because research appears inside a different final deliverable.

```text
research competitors and create ads
→ ADS final owner
→ RESEARCH_ONLY bounded subtask

research TikTok trends and create a post
→ ORGANIC_CONTENT final owner
→ RESEARCH_ONLY bounded subtask
```

Do not own ordinary conversation, pure utility arithmetic/currency conversion, generic writing, image/video generation, publication/deployment, purchase/order/contract authority or unrelated tool debugging.

## 4. Default JIT Specialist Stack

Load only what the task needs:

```text
RESEARCH_EVIDENCE_SYNTHESIS
BUYER_RESEARCH
VIDEO_EVIDENCE_INSPECTION
AD_FUNNEL_INTELLIGENCE
PRODUCT_MARKETPLACE_INTELLIGENCE
```

`RESEARCH_EVIDENCE_SYNTHESIS` remains the canonical owner of generic query/evidence/freshness semantics.

`BUYER_RESEARCH` remains the canonical owner of buyer/review interpretation.

`PRODUCT_MARKETPLACE_INTELLIGENCE` owns only product/listing/seller/variant marketplace-specific interpretation.

## 5. Inputs / Outputs

Inputs may include user question, current Project Profile/scoped state, user-provided links/files/media, authorized web/connector evidence, prior accepted evidence packages and project constraints.

Outputs may include observations, source refs, evidence class/confidence/freshness, explicit unknowns, counterevidence, decision/comparison/shortlist when requested and a completion boundary.

When the next task belongs to another Work Profile, produce a `HANDOFF_PACKET`.

## 6. Evidence Discipline

Inherited without duplication:

```text
OBSERVED
USER_PROVIDED
VERIFIED
INFERRED
UNKNOWN

PARTIAL != NO_RESULTS
ENGAGEMENT != SALES
SELLER CLAIM != INDEPENDENT PERFORMANCE EVIDENCE
UNKNOWN REMAINS UNKNOWN
```

## 7. Product / Marketplace Use

Load `PRODUCT_MARKETPLACE_INTELLIGENCE` only when product/listing/seller/variant identity or exact-match semantics materially matter.

## 8. Supplier Boundary

Current V2.3 does not create a Supplier Sourcing specialist.

Supplier/listing discovery, MOQ/price/freight quote interpretation and confirmed-vs-unconfirmed state may be handled through Research Evidence + Product Marketplace for the tested scope.

Automatic contact, negotiation, purchase, order placement or due-diligence guarantee is outside this profile by default.

## 9. Completion Boundary

```text
RESEARCH COMPLETE
!= GENERATE
!= PUBLISH
!= PURCHASE
```

## 10. U1/U2 Basis

U1 demonstrates independent research value, false-positive Creative resistance and later delayed positive Creative activation.

U2 demonstrates research as one bounded phase inside a persistent multi-owner project.

## 11. Packaging Boundary

Logical Work Profile adoption does not decide physical packaging. Validate behavior first; host/runtime packaging may later place Research Only inside one skill or a sibling package.
