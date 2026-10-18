# AI Creative Skill · Specialist Method · QA · Evidence & Rights · Pre-v0.9-V2-CANDIDATE

## Status

```text
METHOD ID = QA_EVIDENCE_RIGHTS
VERSION = Pre-v0.9-V2-CANDIDATE
DATE = 2026-10-10
PARENT_DOCUMENT = AI_Creative_Skill_Specialist_Method_System
LAST_VALIDATED_AGAINST = AI_Creative_Skill_Specialist_Method_System_Pre-v0.11-V2-CANDIDATE.md
STATUS = DESIGN METHOD · NOT INSTALLED
```

GPT validation hardening branch (2026-10-10): Pre-v0.9-V2-CANDIDATE separates visible text, display authority and claim-evidence authority; makes localization a claim-equivalence decision rather than a cosmetic rewrite; and explicitly separates input language, output language, market scope and jurisdiction scope where they affect evidence or disclosure.


This method reviews factual/commercial support, asset provenance, public-facing wording and required disclosure. It is not automatic legal clearance. Validator correction round (operator-agreed window, 2026-10-09): Pre-v0.8 adds real persons named in a prompt/brief or depicted by requested likeness to the §1 trigger and gives them the consent/provenance rule in §5.2; separates a deliberately requested real brand/mark (owned here: authority/rights, provenance, implied-endorsement check) from an accidental brand/mark in generated output (owned by `IMAGE_DIRECTION`); and adds `video_inspection_evidence_ref` to the §9 output so the full-interval video evidence required by §5.1 is recorded. Pre-v0.7 strengthens the delivered-pixel check added in Pre-v0.6: when screen-derived material appears in video, the sensitive-data review must cover the entire screen-containing interval through `VIDEO_EVIDENCE_INSPECTION`; sampled frames alone are not release evidence. Existing freshness/claim namespaces and shared QA verdict/severity vocabularies are preserved.

---

# 1. Trigger

Use when deliverables contain material:

```text
commercial claims
offers / price / terms
reviews / testimonials
product demonstrations
third-party assets
real brands / marks
real persons named or depicted by likeness
regulated/sensitive claims
disclosure obligations
```

Real brands / marks have two owners:

```text
REAL BRAND / MARK REQUESTED ON PURPOSE
(named in the brief/prompt, supplied as reference, or kept deliberately after review)
→ QA_EVIDENCE_RIGHTS
→ supplied authority or rights/permission for the intended use
→ provenance under §5
→ no implied endorsement, sponsorship or unsupported claim

REAL BRAND / MARK APPEARING ACCIDENTALLY IN GENERATED OUTPUT
→ IMAGE_DIRECTION (accidental brand / text prevention and output review)
→ remove or repair there; if it is kept deliberately, it becomes a requested brand under this method
```

Real persons include anyone named in a prompt, brief or reference label (for example as a cast or crew member), any requested resemblance to a real person, and real-person photos/footage used as source or reference media. They trigger §5.2.

---

# 2. Evidence Before Style

A beautiful asset cannot rescue an unsupported claim.

Check:

```text
proposition
source
scope
status
contradictions
allowed wording
visual implication
```

Pictures can make claims even when copy avoids them.

Generated fire, water, impact, packing or stress-test footage does not prove real product performance.

---

## 2.1 Visible Text / Display Authority / Claim Evidence

A reference or delivered pixel can contain readable wording without proving the proposition. Keep three independent questions:

```yaml
visible_text:        # what pixels literally show
display_authority:   # whether that wording may be preserved/rendered in this bounded asset
claim_evidence:      # whether the proposition may be asserted as a factual/commercial claim
```

`VISIBLE_TEXT` does not upgrade to `CLAIM_EVIDENCE`. Official packaging may justify exact visual preservation while a new ad headline using the same proposition still requires applicable claim support.

---

# 3. Testimonials / Reviews

Require genuine traceable evidence for:

```text
customer quote
name / identity
rating
verified buyer label
case result
before/after
commercial outcome
```

A generated actor or fictional persona may explain or demonstrate. It must not impersonate a real customer experience that did not occur.

---

# 3.1 Borrowed-authority wording

Treat wording such as the following as an evidence trigger when it materially supports a claim:

```text
“especialistas dizem”
“estudos mostram”
“segundo especialistas”
“relatórios do setor indicam”
“amplamente reconhecido”
prestige-publication lists used as proof by association
```

The phrase itself is not automatically false. Resolve the source and what it actually supports. If the source cannot be established, narrow or remove the authority claim rather than replacing it with another vague authority.

---

# 4. Offer Truth

Verify where relevant:

```text
price
reference price / savings
quantity / inclusions
shipping
guarantee
subscription
stock / deadline
eligibility
geography
CTA destination
```

Do not inherit material terms from another offer or competitor example.

---

# 5. Asset Provenance

For used assets, retain enough information to answer:

```text
origin
owner / supplied authority
intended use
attribution / disclosure requirement
material uncertainty
```

Do not export credentials, signed URLs, private customer records or source-system secrets into reusable packages.

## 5.1 Screen-derived sensitive-data inspection

When a public/shareable deliverable contains **real screen-derived pixels** such as screenshots, UI captures, terminal/log output, dashboards, forms or documents, inspect the actual included frame/crop before delivery. Source metadata or an upstream “safe” label is not enough if the rendered pixels can expose material information.

Check at the applicable scope for unauthorized exposure such as:

```text
credentials / API keys / access tokens
signed or private-access URLs
private customer / employee / account records
material personal identifiers or contact data
internal IDs, secrets or environment details that should not be public
other task/project-defined sensitive fields
```

This list is illustrative, not a universal privacy taxonomy. Whether a field may appear depends on Project/task authority, consent, disclosure needs and applicable privacy/security rules.

For **video that contains screen-derived material**, sampled screenshots are not sufficient for this privacy/security check. Require a `video_inspection_evidence_ref` to `VIDEO_EVIDENCE_INSPECTION` covering the **entire interval in which the screen-derived material is visible**:

```text
coverage.visual_continuity = FULL
```

When the possible exposure is carried by readable on-screen text, require as well:

```text
coverage.on_screen_text = FULL
```

`SAMPLED` coverage may help localize a suspected issue, but it does not establish that no credential/private-data exposure occurs elsewhere in the screen-containing interval. If FULL coverage required for a material release decision is unavailable, the privacy/security proposition remains `UNVERIFIED` and must be narrowed, re-inspected or blocked according to the normal QA contract.

If a material exposure is found:

```text
PRESERVE the accepted unaffected asset
→ CROP / REDACT / MASK / BLUR only the smallest reliable surface when authorized
→ RE-INSPECT the delivered frame/crop
```

Do not assume blur is always sufficient, and do not upload a private asset to a third-party detector merely to perform this check unless external processing is authorized. If the sensitive region cannot be reliably removed while preserving the deliverable, mark the issue under the normal QA verdict/severity contract rather than publishing it anyway.

## 5.2 Real persons: identity, likeness and consent

Before generating, transforming or publishing material that names a real person, depicts a real person, or asks for a real person's resemblance:

```text
REAL PERSON NAMED / DEPICTED / RESEMBLED
→ CONSENT OR RIGHTS AUTHORITY FOR THE INTENDED USE RESOLVED
→ SOURCE MEDIA PROVENANCE RECORDED (§5)
→ NO IMPERSONATION OF SPEECH, ENDORSEMENT OR EXPERIENCE THAT DID NOT OCCUR
→ ONLY THEN PROCEED
```

A public or famous person is not exempt. A route that accepts a real-person photo or name does not create permission. If consent/rights authority cannot be established, remove the real-person element, replace it with a non-identifiable or authorized subject, or block. Voice cloning and real-person voice reuse follow the same rule through `AUDIO_VOICE_PERFORMANCE`. Project Profiles may be stricter.

---

# 6. Originality Boundary

Competitor research may inform:

```text
buyer problem
hierarchy
proof mechanism
pacing
concept family
```

Do not trace distinctive layouts, reuse footage, copy scripts, lift mascots/characters or import customer proof.

---

# 6.1 Volatile Claim Currentness

For a material external claim whose truth can change quickly, check whether the support is current enough for the decision boundary. Examples may include current availability, price, platform status, live counts, active policy/rule state or other time-sensitive facts.

When `RESEARCH_EVIDENCE_SYNTHESIS` provides a freshness verdict, preserve it:

```text
CURRENT
STALE
CONTRADICTED
UNSUPPORTED
UNVERIFIED
```

These are **research freshness verdicts**, not claim-registry statuses. `CURRENT` can preserve existing claim support only when the verification source actually covers the same proposition/scope. `STALE`, `CONTRADICTED` and research-freshness `UNSUPPORTED` do not support publication of the original claim as current; `UNVERIFIED` remains unknown and must be narrowed, qualified, rechecked or blocked according to materiality.

If a non-current freshness verdict invalidates or fails to re-establish the **only** material support for a claim, re-evaluate the claim record under the claim registry vocabulary (`OBSERVED | USER_PROVIDED | VERIFIED_EXTERNAL | INFERRED | PROPOSED | UNSUPPORTED`) rather than copying the freshness word into the claim field. Research `STALE` is also unrelated to Execution Route `STALE`; the owning field/schema controls meaning.

Do not rerun an entire research corpus merely to verify one refetchable volatile datum. Prefer bounded point verification when it can establish the claim.

---

# 7. Current Rules / Market

When legal/platform requirements matter, inspect current authoritative rules for the actual market and placement.

Do not hard-code one country's advertising guidance as universal.

The method reports what was checked and what remains outside review.

---

## 7.1 Language, Market, Jurisdiction and Claim Translation

Keep distinct when material:

```text
INPUT_LANGUAGE
OUTPUT_LANGUAGE
MARKET_SCOPE
JURISDICTION_SCOPE
```

Language does not determine market or jurisdiction. Translating a claim is a semantic transformation: compare proposition strength/scope before and after translation and confirm that the same evidence applies in the target market/jurisdiction. A stronger translated statement is not accepted merely because the source sentence was supported.

Brand names, product names, shade names, legal phrases, required disclosures and other protected strings may carry `DO_NOT_TRANSLATE` authority.

---

# 8. Disclosure

Keep distinct:

```text
AI / synthetic-media disclosure
advertising / sponsorship disclosure
affiliate disclosure
other market/platform disclosure
```

One does not silently replace another.

Naturalness, shortening or style editing must treat required disclosure and safety wording as protected content. A line that sounds formulaic is not removable merely because an external style checklist calls similar language “residue”. Change required wording only when the governing authority allows it.

---

# 9. Output

```yaml
review_id:
asset_or_spec_ref:
claims_reviewed:
offer_reviewed:
asset_rights_reviewed:
screen_sensitive_data_review_if_applicable:
video_inspection_evidence_ref:  # required when §5.1 applies to video; canonical reference to VIDEO_EVIDENCE_INSPECTION
disclosure_reviewed:
visual_claim_reviewed:
textual_evidence_flags:
visible_text_review:
display_authority_refs:
claim_evidence_refs:
input_language:
output_language:
market_scope:
jurisdiction_scope:
claim_translation_equivalence:
volatile_claim_freshness:
protected_disclosure_refs:
verdict:
  # ACCEPTED | REPAIR | BLOCKED | UNVERIFIED
issues:
  - issue_id:
    issue:
    consequence:
    severity:  # BLOCKER | REPAIR_REQUIRED | NOTE · semantics owned by QA_REALISM_PERFORMANCE
    required_fix:
inspection_scope:
```


`QA_REALISM_PERFORMANCE` owns the canonical review-issue severity vocabulary. This method consumes `BLOCKER | REPAIR_REQUIRED | NOTE` by reference and does not redefine their meaning. The overall review verdict uses the Execution Contracts vocabulary `ACCEPTED | REPAIR | BLOCKED | UNVERIFIED`.

---

# 10. Acceptance Rubric

Pass only when material claims and offer terms are supported at the correct scope, asset use has no known unresolved material rights issue, applicable screen-derived public/shareable pixels have no unresolved material sensitive-data exposure, and required disclosure is present or correctly planned.

Do not label an asset "fully compliant", "IP-safe" or "guaranteed platform-approved" merely because this review passed.
