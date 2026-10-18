# AI Creative Skill · Method · Product / Marketplace Intelligence · Pre-v0.1-V2.3-CANDIDATE

## Status

```text
METHOD ID = PRODUCT_MARKETPLACE_INTELLIGENCE
VERSION = Pre-v0.1-V2.3-CANDIDATE
DATE = 2026-10-11
STATUS = SPECIALIST METHOD CANDIDATE · NOT PROMOTED TO 00_ACTIVE
```

Parent: `AI_Creative_Skill_Specialist_Method_System_Pre-v0.13-V2.3-CANDIDATE.md`

## 1. Purpose

Provide narrow domain interpretation for product / marketplace research where generic evidence synthesis cannot cleanly express entity identity and marketplace equivalence.

This method is not a crawler, Buyer Research clone, supplier-negotiation agent or creative-production method.

## 2. Growth Rule Justification

Generic Research Evidence + Buyer Research already handle query planning, source quality, freshness, comparison, review semantics, counterevidence, PARTIAL vs NO_RESULTS and engagement-vs-sales discipline.

They do not cleanly own:
- exact product vs substitute;
- product vs listing vs seller vs variant;
- cross-market listing equivalence confidence;
- stable product identity through longitudinal research;
- stable entity handoff into downstream creative work.

## 3. Entity Model

Minimum entity types:

```text
PRODUCT_FAMILY
PRODUCT_VARIANT
LISTING
SELLER
BRAND
SOURCE_PRODUCT_REF
```

A listing is not automatically a product identity.
A seller is not automatically a manufacturer.
Visual similarity is not proof of common source/manufacturer.

Stable entity fields:

```yaml
entity_id: string
entity_type: enum
canonical_label: string | UNKNOWN
source_refs: [string]
observed_identifiers: [string]
match_confidence: HIGH | MEDIUM | LOW | UNKNOWN
notes: string | UNKNOWN
```

## 4. Exact vs Similar Matching

Task policy may be:

```text
EXACT_MATCH_REQUIRED
SIMILAR_ALLOWED
SIMILAR_AS_FALLBACK_ONLY
```

User corrections revise the scoped policy and persist until explicitly changed.

## 5. Listing Equivalence

Evaluate observable dimensions such as form, dimensions/capacity, material, design/illustration, packaging, variant naming, identifiable marks, product photos and seller-provided specs.

Verdicts:

```text
EXACT_OR_HIGH_CONFIDENCE_MATCH
LIKELY_SAME_FAMILY_OR_VARIANT
SIMILAR_ONLY
NOT_A_MATCH
INSUFFICIENT_EVIDENCE
```

Resemblance never becomes manufacturer/source certainty.

## 6. Marketplace Evidence

Reuse canonical Research Evidence / Buyer Research semantics.

```text
seller bestseller badge → seller claim / merchandising signal
review showing owned item → ownership/use evidence
like/view → weak interest
save → stronger interest, not purchase
"where can I buy?" → purchase-intent signal
"I ordered X" → stronger purchase evidence

none alone → bestseller rank / conversion / market size
```

## 7. Price / MOQ / Quote State

Preserve observed distinctions.

```text
regular MOQ stated by supplier → CONFIRMED
shipping quote for 10-unit scenario → CONFIRMED QUOTE SCENARIO
10-unit order acceptance → UNKNOWN unless explicitly confirmed
```

Quote arithmetic is not final landed cost unless material cost components are actually accounted for.

## 8. Supplier Boundary

May support supplier/listing discovery as part of marketplace research.

Does not own full supplier due diligence or guarantee manufacturer/trader status, legal entity legitimacy, certification, food-contact compliance, factory capability, delivery performance or product quality.

`SUPPLIER_SOURCING_DUE_DILIGENCE` remains dormant until separate craft depth is demonstrated.

## 9. Handoff to Creative

When exact identity matters downstream:

```text
RESEARCH PRODUCT ENTITY
→ stable_entity_id + source refs
→ HANDOFF_PACKET
→ ORGANIC / ADS / PRODUCT_CONTENT
```

Creative presentation labels may not erase the source/canonical entity.
No procurement/purchase authority transfers.

## 10. Completion / Non-Duplication

Outputs may include exact/similar match result, entity map, shortlist, marketplace comparison, demand-signal interpretation, explicit uncertainty and source refs.

If generic Research Evidence or Buyer Research can answer the question without marketplace-specific entity interpretation, do not load this method.
