# AI Creative Skill · Work Profile · Ads · Pre-v0.8

## Status

```text
DOCUMENT TYPE
=
ADS WORK PROFILE

VERSION
=
Pre-v0.8

DATE
=
2026-10-09

PARENT_DOCUMENT
=
AI_Creative_Skill_Architecture_Spec

LAST_VALIDATED_AGAINST
=
AI_Creative_Skill_Architecture_Spec_Pre-v0.14.md

STATUS
=
DESIGN PROFILE
NOT INSTALLED
```

This profile contains commercial/ad-specific reasoning that was intentionally removed from the generic Creative Core.

This document supersedes `AI_Creative_Skill_Work_Profile_Ads_Pre-v0.7.md` for design purposes. Pre-v0.8 adds commercial claim/evidence revalidation for material variants, explicit review of route-generated speech, and a boundary that treats third-party predictive creative scores as diagnostics rather than measured performance or acceptance authority. Pre-v0.7 research/video-inspection routing remains in force.

---

# 1. Scope

Use this Work Profile when the requested output is a paid ad, ad creative, commercial landing/funnel creative, or performance-oriented commercial variation.

It adds:

```text
buyer / purchase-situation research
offer semantics
ad / funnel research
evidence / claim discipline
persuasion strategy
PROOF / QUEST where useful
concept-family / variant logic
commercial copy / CTA
campaign-result learning
```

It does not own Project Profile identity, voice, environment or route locks.

## 1.1 Default Specialist Method Stack

Depending on the bounded request, this Work Profile may activate:

```text
RESEARCH_EVIDENCE_SYNTHESIS, when external/current evidence retrieval is active
BUYER_RESEARCH
AD_FUNNEL_INTELLIGENCE
VIDEO_EVIDENCE_INSPECTION, when material competitor/reference-video claims require structured inspection
ADS_STRATEGY
SCRIPT_PERFORMANCE
IMAGE_DIRECTION
VIDEO_DIRECTION
TALKING_PERSONA, when applicable
TYPOGRAPHY_LAYOUT
AUDIO_VOICE_PERFORMANCE, when applicable
PLATFORM_META, when applicable
ROUTE_COMPILATION
QA_EVIDENCE_RIGHTS
QA_REALISM_PERFORMANCE
LOCALIZED_REPAIR, when needed
```

These methods are loaded only when needed. Their professional procedure lives in the current Specialist Method documents as resolved by the Specialist Method System and Provenance Map; this Work Profile remains authority for ad-specific commercial logic.

---

# 2. Ads Intake Map

The reviewed `meta-ads-client-brief.pdf` is treated as an intake source, not as the full ads method.

Mapping:

```text
BRIEF §1 · Business / goals / market
→ business context + objective + market + language

BRIEF §2 · Product / service / offer
→ OFFER entity

BRIEF §3 · Buyers / desired customers / competitors
→ client-declared hypotheses + research seeds

BRIEF §4 · Click destination / customer-data context
→ funnel context + first-party context

BRIEF §5 · Past ads / results
→ performance/improve context

BRIEF §6 · Media budget / dates / contribution
→ campaign context

BRIEF §7 · Photos / materials
→ candidate reference assets

BRIEF §8 · launch/account/readiness
→ planning metadata
```

Client-declared audience information is not treated as independent research.

```text
CLIENT SAYS WHO BUYS
≠
BUYER RESEARCH COMPLETE
```

---

# 3. Production Supplement

Commercial intake is not a production spec.

When relevant, Ads additionally requires:

```text
persona / presenter
deliverable count
static / video / mixed
placements
aspect ratios
durations
brand voice / visual rules
project/canon authority
rights / consent
production budget
script / creative / final-media approval gates
master vs draft quality
AI disclosure requirements
advertising disclosure requirements
```

Keep campaign/media budget separate from production-generation budget.

---

# 4. Offer as a First-Class Entity

Each priority offer receives a stable ID.

Example:

```yaml
offer_id:
name:
priority:
problem:
desired_outcome:
inclusions:
exclusions:
delivery:
price:
terms:
aov:
benefits:
differentiators:
evidence:
promotion:
guarantee:
subscription:
limitations:
unsuitable_users:
forbidden_claims:
```

Lineage:

```text
OFFER
→ BUYER RESEARCH
→ CLAIMS
→ PERSUASION HYPOTHESIS
→ CONCEPT FAMILY
→ ASSETS
→ PERFORMANCE
```

One offer should not silently inherit price, guarantee or proof from another offer.

---

# 5. Buyer Research

Research should begin with the purchase situation, not demographic decoration.

Useful fields:

```text
situation / trigger
desired progress
current alternatives
objections / hesitation
positive experiences
negative experiences
poor-fit users
actual buyer language
required proof
```

Separate evidence classes where practical:

```text
exact SKU / offer
comparable offer
category-level evidence
```

For a new ad creative, a grounded audience basis is required:

```text
FRESH INSPECTED BUYER RESEARCH
OR
STILL-VALID REUSED BUYER RESEARCH
OR
AUTHORITATIVE SUPPLIED EVIDENCE
```

If none is adequate, `BUYER_RESEARCH` becomes required before strategy. When external retrieval is needed, `RESEARCH_EVIDENCE_SYNTHESIS` provides the shared query/source/coverage/freshness layer and Buyer Research interprets the result for purchase situations. A bounded edit or repair may reuse existing valid research when the requested change does not depend on new buyer facts.

Research completeness is a gate for strategy when fresh research is required. Deep research may use proportional coverage targets from the Buyer Research Method, including source diversity, counterevidence and explicit coverage reporting.

---

# 6. Ad and Funnel Research

After buyer synthesis, inspect relevant current ads and destinations when the task calls for live research.
Use `RESEARCH_EVIDENCE_SYNTHESIS` for generic multi-source planning/outcomes when the research extends beyond a single directly inspected ad/funnel surface.

Capture:

```text
hook / promise
proof / visible support
offer
objection handling
CTA
format
concept family
destination
funnel continuity
```

When live ad/funnel research is active, also preserve where accessible:

```text
advertiser / page identity
ad or creative ID
market / country
status / dates
inspection date
variant-family relationship
actual inspection coverage
```

Cluster repeated/localized variants so twenty translations are not treated as twenty independent concept confirmations. When a material observation depends on an ad/reference video, use `VIDEO_EVIDENCE_INSPECTION` when structured evidence is needed and retain its inspection reference/coverage rather than recreating video-inspection fields here. For a deep run, the Ad/Funnel Intelligence Method may use approximate coverage targets such as several relevant advertisers and roughly twenty distinct observations when accessible; actual coverage must be reported.

Do not promote ad longevity, reach or organic popularity into conversion proof.

Evidence ladder:

```text
L0 OBSERVED
existence / format / copy / dates / visible reach

L1 INFERRED
possible relevance / continued spend

L2 MEASURED
hook rate / CTR / CPL / CPA / conversion

L3 ECONOMIC
revenue / CAC / margin / ROAS / LTV
```

Never promote L1 into L2 or L3.

---

# 7. Claim Registry

Ads claims require explicit support status.

Suggested record:

```yaml
claim_id:
proposition:
source_refs:
scope:
status:
  # OBSERVED | USER_PROVIDED | VERIFIED_EXTERNAL | INFERRED | PROPOSED | UNSUPPORTED
confidence_notes:
contradictions:
allowed_wording:
forbidden_wording:
```

No invented:

```text
customer
verified buyer
review
rating
commercial result
before/after result
stress-test proof
```

An AI persona can explain or demonstrate but cannot impersonate a real customer experience that did not occur.

---

# 8. Commercial Authenticity

```text
GENERATED ACTOR
≠
REAL CUSTOMER
```

```text
GENERATED WATER / FIRE / IMPACT SCENE
≠
REAL PRODUCT TEST
```

```text
AI DISCLOSURE
≠
ADVERTISING DISCLOSURE
```

Project Profiles may impose stricter commercial-authenticity rules.

---

# 9. Persuasion Strategy

Before final copy, resolve six material decisions:

```text
1. purchase situation / job
2. desired outcome + relevant obstacle
3. product/service mechanism + one supported difference that matters
4. main objection + evidence / truthful explanation
5. real offer: price / inclusions / conditions / destination / next action
6. measurable hypothesis: what should change, for whom, and what result would support or reject it
```

If a decision is materially unknown, narrow the concept rather than inventing it.

The core commercial chain is:

```text
BUYER SITUATION
→ BUYING MOTIVE
→ OBJECTION / HESITATION
→ PERSUASION HYPOTHESIS
→ CONCEPT FAMILY
→ VARIANTS
```

A different wrapper is not automatically a new concept.

A materially different reason-to-believe or commercial mechanism is a new concept.

---

# 10. PROOF and QUEST

Use only when they fit the task.

## Product / E-commerce · PROOF

```text
Promise
Receipts
Offer
Objection
First step
```

## Service · QUEST

```text
Qualify
Understand
Educate
Stimulate
Transition
```

These are reasoning frameworks, not mandatory visual templates.

The skill may select another appropriate framework when evidence and offer structure demand it.

---

# 11. Static Ad Families

Common product-oriented families learned from the reviewed source workflow:

```text
CALLOUT / DIAGRAM
REVIEW-LED
OFFER-LED
```

Common service-oriented families:

```text
QUIZ
CASE STORY
DIRECT OFFER
```

These are reusable format families, not a requirement to generate all of them.

Format choice carries an evidence obligation:

```text
CALLOUT / DIAGRAM
→ verified visible feature + supported benefit

REVIEW-LED
→ traceable authentic review/testimonial and permitted attribution

OFFER-LED
→ current product / price / inclusions / material terms

QUIZ
→ truthful self-assessment + real next step; no fake diagnosis

CASE STORY
→ documented starting point / intervention / supported result

DIRECT OFFER
→ real scope / terms / CTA
```

Quantity comes from the task/experiment plan.

---

# 12. Review-Led Creative Rule

If an authentic review is unavailable:

```text
REVIEW CARD
=
UNFINISHED BLUEPRINT
```

Do not synthesize:

```text
fake name
fake quote
fake star count
"verified buyer"
fake case result
```

A design can reserve a review area for later evidence, but it must not manufacture the evidence.

## 12.1 Packaging / Unboxing Truth

Unboxing or offer-reveal creative must match verified packaging, included items and item count. Without evidence, do not invent a gift box, accessory, warranty card, hidden compartment, capacity, compliance badge or other product detail. Use an honest product/offer reveal instead.

## 12.2 Localization

Localization is not literal translation. Recheck for every market where relevant:

```text
buyer context
spelling
units
currency
offer eligibility
cultural meaning
voice timing
line breaks
claims
typography
pacing
destination
```

A concept may transfer while execution changes materially.

---

# 13. Concept vs Variant

```text
concept_id
=
commercial hypothesis / mechanism

variant_id
=
controlled change around the same concept
```

Variant dimensions may include:

```text
hook
opening visual
actor/presenter
execution style
audio/music
placement/aspect
offer emphasis
CTA wording
```

For controlled optimization, vary one main factor when practical.

For creative exploration, deliberate diversity is allowed but should not be confused with a controlled model/creative benchmark.

---

## 13.1 Commercial claim/evidence revalidation across variants

A variant may inherit structure, timing, presenter or other declared preserved attributes from an accepted source. It does **not** automatically inherit commercial claim acceptance when the varied surface changes what the audience is being asked to believe.

```text
APPROVED SOURCE ASSET
!=
AUTOMATIC CLAIM ACCEPTANCE FOR EVERY VARIANT
```

Re-resolve affected claims/evidence when a variant materially changes:

```text
product / SKU / packaging state
offer / price / terms
market / language when claim scope can change
presenter / testimonial framing
visible proof / demonstration / before-after
spoken or on-screen wording
comparison target
other claim-bearing surface
```

A pure wrapper change may reuse unchanged claim references only when lineage proves that the claim-bearing surfaces and their scope were preserved. `preserve` may keep camera, timing, presenter or composition; it must not silently preserve a claim whose underlying product/offer/evidence changed.

---

# 14. Internal Ads Production Brief

Before compiling provider prompts, build a compact internal brief:

```text
business goal
market / language / placement
buyer situation / motive / objection
persuasion hypothesis
concept family / variant ID
exact hook / support / offer / CTA
proof / missing evidence
visual progression / reference authorities
destination
primary metric / failure hypothesis
active specialist method refs
product truth / packaging refs when relevant
```

This is the handshake between commercial intelligence and the generic execution layer.

The execution layer should not need the entire raw client brief.

---

# 15. Commercial Pre-Generation QA

Before paid generation check:

```text
price / terms / quantity exactness
claim support
review / testimonial authenticity
offer-destination consistency
reference authority
exact copy
rights / disclosure
technical executability
known route failure preflight
need for a task-specific canary before scale
budget / approval
```

Commercial pre-generation QA must pass before paid generation. Prompt quality does not compensate for an incorrect offer, unsupported claim, invalid authority or missing approval.

---

## 15.1 Route-generated / improvised commercial speech

A route may generate native speech, dialogue or a monologue even when the operator supplied only a concept. That wording is **new claim-bearing output**, not pre-approved copy authority.

For a public/commercial asset:

```text
ROUTE-GENERATED SPEECH
→ capture / eligible transcription or exact route evidence
→ compare with script + claim authority
→ review new/changed claims
→ only then accept for delivery/publication
```

If exact speech is required, constrain the route to approved wording. If the selected route cannot reliably accept the required exact material claim, it is not eligible for that execution merely because its visual/voice result is attractive.

Post-generation review must inspect what was actually said, not only what the prompt asked the route to say.

---

# 16. Commercial Post-Generation QA

Check separately:

```text
exact offer / price / terms
claim-to-visual support
generated/native speech vs approved script + claim registry
customer/review authenticity
product geometry / packaging
copy accuracy
CTA
mobile readability / intended-size review
first-frame / muted / crop checks where relevant
commercial disclosure where required
```

A requirement in the prompt is not evidence that the output complied.

---

# 17. Improve Route

When real performance data exists, connect it to the exact concept/variant and comparable conditions.

When learning is intended, define creative lineage before publication where possible:

```text
concept_id
variant_id
asset_id
hook_id
opening_type
format / placement
publication_id
```

Useful performance context:

```text
campaign / ad ID
market / audience
period
spend
impressions
clicks
leads
qualified leads
purchases
revenue
CPA / CAC
ROAS
refunds where relevant
attribution window / source
```

Separate:

```text
attention
intent
commercial outcome
```

Do not simply label assets winner/loser. Diagnose where persuasion failed.

---

## 17.1 Third-party predictive scores are diagnostic signals

A provider/tool score for virality, hook strength, retention risk, predicted engagement or similar pre-launch performance is third-party diagnostic evidence.

```text
PREDICTIVE / SELF-SCORE
!=
MEASURED MARKET PERFORMANCE
!=
CREATIVE ACCEPTANCE AUTHORITY
```

Store the tool/model/version and input asset when material, and use the score to rank a shortlist or form a test hypothesis. Do not promote it to L2 `MEASURED` or L3 `ECONOMIC`, and do not let it override evidence/rights/claim failures. Actual performance remains tied to published variant + comparable placement/spend conditions.

Sending an asset to an external scorer also follows the selected provider's data/privacy boundary.

---

# 18. Output of Ads Profile

The Ads profile hands the generic Core/Execution layer a provider-neutral object containing:

```text
commercial objective
offer / claim refs
concept / variant
variant_claim_revalidation_ref when applicable
generated_speech_review_ref when applicable
third_party_predictive_score_ref when used
exact copy
reference authority
static or scene production spec
acceptance criteria
performance hypothesis
active method outputs / refs
localization requirements where relevant
```

From that point, the generic execution contracts decide model, route, provider mechanics, cost, submission and retrieval. Applicable execution/QA Specialist Methods decide how the provider-neutral spec is compiled and how the resulting artifact is inspected without changing the commercial authority defined here.
