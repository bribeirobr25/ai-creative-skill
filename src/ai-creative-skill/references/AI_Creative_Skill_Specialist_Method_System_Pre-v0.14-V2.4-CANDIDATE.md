> **V2.4 CANDIDATE SCOPE:** Modified version of this method family. Read the final section “V2.4 real-world hardening” for current candidate additions. Historical V2.3 discussion and prior-source pointers below remain provenance, not active version resolution.

# AI Creative Skill · Specialist Method System · Pre-v0.14-V2.4-CANDIDATE

## Status

```text
DOCUMENT TYPE
=
SPECIALIST METHOD SYSTEM

VERSION
=
Pre-v0.14-V2.4-CANDIDATE

DATE
=
2026-10-16

PARENT_DOCUMENT
=
AI_Creative_Skill_Architecture_Spec

LAST_VALIDATED_AGAINST
=
AI_Creative_Skill_Architecture_Spec_Pre-v0.16-V2.3-CANDIDATE.md

STATUS
=
DESIGN METHOD SYSTEM
NOT INSTALLED
```

GPT validation hardening branch (2026-10-10): Pre-v0.11-V2-CANDIDATE formalizes cross-method constraint/provenance propagation and a compact decision-trace discipline. Specialist handoff may transform representation but may not silently strengthen claim/evidence/rights/authority state or drop protected constraints.

Z4/Z4.1 creative-balance hardening branch (2026-10-11): Pre-v0.12-V2.2-CANDIDATE adds task-relative creative-latitude semantics, an optional creative-risk ladder, conditional divergence-before-convergence, narrow user preserve/explore overrides, and explicit separation of consistency from repetition and creativity from randomness. These controls never relax factual, rights, identity, product, exact-text, approval, policy or safety authority.


This document defines how a broad creative orchestrator acquires specialist depth without turning the generic Core into one enormous all-purpose instruction file. Pre-v0.10 tightens canonical schema ownership after the third coherence cleanup: text findings are directly referenceable, speech-text coverage belongs to Audio & Voice rather than video coverage, and the shared QA severity vocabulary is explicitly cross-QA.

This version preserves the bounded self-check and version-resolution policies introduced earlier. Existing specialist methods do not require a version bump solely because the Architecture, Method System or manifest advances. Their current versions are resolved by the Current Design Manifest; revalidation/versioning is required only when consumed behavior or the method itself materially changes.

```text
CORE
=
ROUTING + AUTHORITY + STATE + EXECUTION CONTROL

SPECIALIST METHOD
=
DOMAIN CRAFT + DECISION RULES + CALIBRATION + ACCEPTANCE
```

A method is loaded only when the current request requires it.

---

# 1. Specialist Method Principle

The skill should not rely on one generic instruction such as “research well”, “make it natural” or “review quality”. Those phrases describe an intention, not a professional method.

Every specialist method must answer:

```text
WHAT TO LOOK FOR
HOW TO DECIDE
HOW TO EXECUTE
WHAT GOOD LOOKS LIKE
WHAT FAILURE LOOKS LIKE
WHEN TO STOP
WHAT TO HAND OFF
```

Specialist methods do not override law, operator governance, project canon, Project Profiles or Work Profiles.

---

# 2. Common Specialist Contract

Every specialist method should define at least:

```yaml
method_id:
trigger:
inputs:
authority:
boundaries:
method:
decision_rules:
output:
acceptance_rubric:
reuse_and_freshness:
failure_and_stop:
calibration_pack:
```

Interpretation:

- `trigger`: when the method is required, optional or unnecessary;
- `inputs`: minimum useful context;
- `authority`: what decisions the method may make;
- `boundaries`: what remains owned elsewhere;
- `method`: actual professional procedure;
- `decision_rules`: how competing options are resolved;
- `output`: structured handoff to the next stage;
- `acceptance_rubric`: observable pass/fail criteria; where practical, express them as explicit questions or checks that can be evaluated one by one rather than as vague quality adjectives;
- `reuse_and_freshness`: when prior work can be reused;
- `failure_and_stop`: when the method must narrow, block or return unknown;
- `calibration_pack`: examples, anti-examples, edge cases and known failures.

---

# 3. Method Stack Resolution

A request may require several specialists.

Example:

```text
"Create three Meta video ads for this product"

Project Profile
+ Ads Work Profile
+ Research Evidence Synthesis, when external/current evidence retrieval is active
+ Buyer Research, if no valid audience basis exists
+ Ad/Funnel Intelligence
+ Video Evidence Inspection, when material competitor/reference-video claims require structured inspection
+ Ads Strategy
+ Platform Meta
+ Script / Performance
+ Video Direction
+ Audio / Voice, if speech exists
+ Route Compilation
+ Evidence / Rights QA
+ Realism / Performance QA
```

A bounded edit may require only:

```text
"Fix the CTA on this image"

Project Profile
+ applicable Work Profile
+ Typography / Layout
+ Localized Repair
+ QA
→ DELIVER
→ END
```

Do not load specialists merely because they exist.

---

# 4. Method Precedence

When methods overlap:

```text
PROJECT / WORK AUTHORITY
>
NARROWER APPLICABLE SPECIALIST METHOD
>
BROADER SPECIALIST METHOD
>
GENERIC CRAFT DEFAULT
```

A Platform Method may modify execution grammar but may not rewrite a Project Profile identity rule or invent commercial evidence.

A Route Compilation Method may adapt syntax and decomposition but may not change creative intent silently.

---

# 5. Abstract Intent Must Become Observable Direction

Specialist methods should translate vague adjectives into observable choices.

Bad:

```text
premium
cinematic
natural
authentic
dynamic
viral
```

Better:

```text
restricted composition
one dominant subject
controlled negative space
motivated directional light
accurate material reflections
purposeful movement
observable acting task
stable readable CTA
```

The specialist should preserve the user’s intent while replacing ambiguous craft language with instructions that can be produced and reviewed.

---

# 6. Constraint Priority

When a production request contains many requirements, classify them:

```text
HARD INVARIANT
REQUIRED
PREFERRED
FLEXIBLE
FORBIDDEN
```

A route or model must not be expected to infer which of twenty instructions matters most.

Hard invariants and forbidden elements must be explicit in the production spec and review rubric.

---

## 6.1 Cross-Method Constraint Propagation

At each specialist handoff, preserve or explicitly resolve material constraints that remain applicable, including:

```text
claim / evidence status
rights status
authority scope
protected_dimensions
excluded_inheritance
exact approved text
do_not_translate refs
cost / attempt / approval constraints
review state
```

A summary, paraphrase or specialist handoff does not upgrade provenance or authority. If an upstream field is intentionally narrowed, removed or superseded, record the authority/reason rather than silently dropping it.

---

## 6.2 Task-Relative Creative Latitude

Constraint priority and creative latitude are separate axes.

```text
PRIORITY / AUTHORITY
=
HARD INVARIANT | REQUIRED | PREFERRED | FLEXIBLE | FORBIDDEN

CREATIVE LATITUDE
=
PRESERVE | BOUNDED_VARIATION | OPEN_EXPLORATION
```

`FORBIDDEN` remains a permission/priority state. It is not duplicated as a creative-latitude value.

Use a task-relative dimension policy when the distinction is material:

```yaml
dimension_policy:
  dimension:
  priority:  # HARD INVARIANT | REQUIRED | PREFERRED | FLEXIBLE | FORBIDDEN
  creative_latitude:  # PRESERVE | BOUNDED_VARIATION | OPEN_EXPLORATION
  authority_ref:
  envelope_ref:       # required when BOUNDED_VARIATION needs an explicit range
  canon_promotion_ref:
  task_scope:
  rationale:
```

Interpretation:

```text
PRESERVE
→ keep the applicable identity / continuity / authority-bearing state stable

BOUNDED_VARIATION
→ vary expression only inside the resolved envelope

OPEN_EXPLORATION
→ explore materially different valid expressions inside all higher-priority authority
```

`identity-bearing` and `expression-bearing` are task-relative roles, not universal modality lists. Lighting, wardrobe, gesture, phrasing, pacing, camera behavior or another dimension may be expressive in one task and continuity/canon in another. Resolve from Project/Work authority, accepted continuity state, explicit user instruction and the applicable specialist method.

```text
CONSISTENCY != REPETITION
CREATIVITY != RANDOMNESS

PRESERVE WHAT MAKES THE CURRENT WORK / PERSONA / WORLD THE SAME THING
EXPLORE WHAT LEGITIMATELY ALLOWS IT TO EXPRESS SOMETHING NEW
```

Do not invent locks merely because a dimension appeared before. Conversely, do not open a dimension that current authority or continuity requires to remain stable.

A user instruction such as `preserve lighting`, `keep the same voice`, `be creative with camera` or `vary the emotional delivery` changes only the named legitimate dimension(s). It does not silently weaken unrelated hard constraints, rights, claims, identity, product truth, exact text, approval, policy or safety.

For longitudinal work, stable identity-bearing state should resolve from current canon / approved authority rather than from the immediately previous generated derivative alone. An accepted derivative may supply scoped continuity evidence when authorized, but derivative-to-derivative drift does not become authority by accumulation.

---

## 6.3 Creative Risk Is Orthogonal to Factual / Authority Risk

When useful for concept or expression work, record an optional `creative_risk_level`:

```yaml
creative_risk_level:  # SAFE | BALANCED | BOLD | EXPERIMENTAL
```

```text
SAFE
BALANCED
BOLD
EXPERIMENTAL
```

The ladder changes how aggressively the system explores dimensions already marked `BOUNDED_VARIATION` or `OPEN_EXPLORATION`. It never changes what is true, permitted, approved, owned or identity-critical.

```text
CREATIVE RISK
!=
FACTUAL RISK
!=
RIGHTS RISK
!=
AUTHORITY RISK
!=
SAFETY RISK
```

A higher creative-risk level may justify less literal framing, a less familiar narrative structure, stronger contrast, unusual camera/composition choices or a more surprising but relevant concept. It may not authorize unsupported claims, identity drift, product redesign, rights violations or policy bypass.

---

## 6.4 Conditional Divergence Before Convergence

For tasks whose objective materially benefits from **distinct concepts** rather than mechanical variants, use a bounded exploration path:

```text
EXPLORE
→ CLUSTER / COMPARE
→ SELECT
→ DEVELOP
→ HAND OFF FOR EXECUTION
```

Do not require this path for bounded edits, deterministic repairs, exact transformations, controlled experiments whose point is to preserve most dimensions, or jobs with only one materially valid execution.

When multiple distinct concepts are requested, review for mode collapse across the dimensions actually open to exploration. Ten cosmetically different outputs built from one unchanged underlying idea do not satisfy a request for ten distinct concepts.

Record the conditional diversity verdict without inventing a universal novelty score:

```yaml
concept_diversity_acceptance:
  distinctness_required:
  declared_open_dimensions:
  materially_separated_dimensions:
  mode_collapse_state:  # PASS | REVIEW | NOT_APPLICABLE
  rationale:
```

`NOT_APPLICABLE` is correct for controlled variants or tightly preserved families whose purpose is not conceptual divergence.

Compliance and fidelity are gates. Among candidates that already pass those gates, selection may compare:

```text
objective fit
relevance
specificity
conceptual distinctiveness
supported surprise / non-obviousness
craft feasibility
```

Do not reward novelty that weakens relevance, and do not select the safest generic concept merely because compliance is easier to score.

---


# 7. Reference Readiness

A reference having authority does not mean it is technically suitable.

Before binding a reference, check where relevant:

```text
resolution
visibility
occlusion
distortion
wrong text / logo contamination
lighting that hides defining geometry
wrong product version
crop loss
conflicting references
```

A reference must specify what it controls and what it must not contribute. Conflicting references should be scoped or rejected rather than dumped into one prompt.

---

# 8. Calibration Pack Standard

Each specialist should gradually accumulate:

```text
GOOD EXAMPLES
EXCELLENT EXAMPLES
ANTI-EXAMPLES
EDGE CASES
CAUSAL BEFORE / AFTER CASES
FAILURE LIBRARY
REPAIR EXAMPLES
ACCEPTANCE RUBRICS
```

Examples must teach decisions, not only provide prompts.

A complete example should record:

```text
REQUEST
OBJECTIVE
AUTHORITIES
OPTIONS
TRADE-OFF
DECISION
WHAT WAS PRESERVED
WHAT WAS SACRIFICED
PRODUCTION SPEC
EXECUTION RESULT
QA FINDINGS
REPAIR, IF ANY
FINAL ACCEPTANCE
APPLIES WHEN
DOES NOT APPLY WHEN
TRANSFERABLE PRINCIPLE
```

---

# 9. Quality Calibration by Contrast

Where useful, show three levels:

```text
WEAK
=
technically possible but generic / poorly grounded

ACCEPTABLE
=
meets the request and requirements

EXCELLENT
=
strong objective fit, craft, fidelity and review evidence
```

A visually attractive output can still be rejected for wrong product geometry, unsupported proof, broken persona behavior, hidden physical action or missing commercial meaning.

---

# 10. Trade-Off Discipline

Specialists must be able to choose when objectives conflict.

Example:

```text
more camera movement
vs
clearer product demonstration
```

If the commercial job is demonstration, preserve visibility of the mechanism even if the shot becomes less dramatic.

The decision record should identify:

```text
competing objectives
chosen priority
sacrificed quality
why the trade-off is valid
```

---

# 10.1 Method Self-Check

Before handoff, a producer/specialist may run its own acceptance rubric item by item. If a check fails and the current scope permits repair, fix the smallest causal surface and rerun the affected checks.

An iterative self-check must be **bounded**. The applicable specialist should define its retry/pass limit or explicit stopping condition when repeated repair is possible. If the bound is reached with material failures remaining, preserve those failures in the handoff instead of continuing an unbounded quality loop.

```text
SELF-CHECK
=
USEFUL PRE-HANDOFF VALIDATION

SELF-CHECK
!=
INDEPENDENT REVIEW
```

Record a self-check as self-check, including iteration count and remaining failures where relevant. Never describe it as independent verification merely because the same rubric was executed.

---

# 11. Review Independence

When practical, the final specialist reviewer should not be the sole author/operator of the asset.

```text
PRODUCER
≠
SOLE FINAL REVIEWER
```

Canonical `reviewer_independence` semantics:

```text
INDEPENDENT
=
different reviewer from the producer / sole author
+ fresh bounded review context, not the producer's reasoning trail
+ actual artifact + acceptance criteria + authoritative references
+ no desired verdict
+ reviewer does not modify the artifact while forming the verdict
  (read-only enforcement preferred when runtime permissions can express it)

SELF_REVIEW
=
producer/author reviews own work

MIXED
=
some but not all independence conditions are satisfied

UNKNOWN
=
review provenance is insufficient to classify
```

If independent review is unavailable, direct review remains useful but must not be labeled independent. Text instructions alone do not guarantee read-only behavior; when a selected runtime can enforce critical permissions mechanically, use that enforcement in addition to the method instruction.

---

# 12. Positive Specification and Negative Constraints

Default prompt construction should describe the desired result positively.

Negative constraints are appropriate when:

```text
a known route/model failure is documented
OR
a forbidden element must be explicit
OR
a repeated observed defect requires a concise mitigation
```

Do not create long lists of undesirable imagery merely to appear thorough. Route-specific evidence may justify concise negatives.

---

# 13. Role Contract

A specialist role is a bounded responsibility, not necessarily a permanent agent or separate skill.

Each role should define:

```text
RECEIVES
DECIDES
DELIVERS
MAY NOT DECIDE
```

Delegation may run in parallel inside a stage when dependencies allow. Dependent stages remain sequential.

---

# 13.1 Canonical Schema Ownership

When one specialist explicitly owns a reusable structured vocabulary or evidence schema, consumer methods should reference that owner rather than copy a partial local enum or rename equivalent fields.

```text
SCHEMA OWNER
→ defines fields / allowed values / semantics

CONSUMER
→ stores reference + domain interpretation
→ does not create a competing truth
```

Current examples:

```text
RESEARCH_EVIDENCE_SYNTHESIS
→ canonical research source outcomes + research freshness verdicts

VIDEO_EVIDENCE_INSPECTION
→ canonical structured video-inspection coverage

AUDIO_VOICE_PERFORMANCE
→ canonical speech-text / transcription evidence

SCRIPT_PERFORMANCE
→ canonical text-finding schema

QA_REALISM_PERFORMANCE
→ canonical review-issue severity vocabulary used across QA methods
```

Avoiding duplication is a maintenance benefit, not by itself a reason to create a specialist. Specialist creation still requires the Growth Rule below.

---

## 13.2 Decision Trace Discipline

Methods should emit stable references to the authoritative inputs they consumed and the output record they produced. The Execution Contracts decision-trace index may link those references for debugging/audit, but it does not become a competing source of truth.

---

# 14. User-Facing Communication

Expose substantive findings and decisions, not internal plumbing.

Useful:

```text
"The research points to this buyer situation because..."
"The route cannot preserve exact audio, so it is not eligible."
"This clip passed identity but failed lip-sync at 00:07."
```

Normally omit internal worker IDs, validation command names, state-machine implementation details and runtime chatter unless the user asks.

Ask only for missing information that would materially change the result.

---

# 14.1 Current-version resolution

The table below defines the specialist **families and responsibilities**, not their current filenames. Current method versions are resolved exclusively through `AI_Creative_Skill_Current_Design_Manifest`.

```text
METHOD INDEX HERE
=
WHAT SPECIALISTS EXIST / WHAT THEY OWN

CURRENT DESIGN MANIFEST
=
WHICH VERSION OF EACH SPECIALIST IS CURRENT
```

This avoids duplicating version truth in both the Method System and the manifest.

---

# 15. Current Specialist Index

| Method | Primary trigger | Primary output |
|---|---|---|
| Research Evidence Synthesis | Stage-2 external/current evidence retrieval is active | provider-neutral research plan + evidence/freshness handoff |
| Product / Marketplace Intelligence | product/listing/seller/variant identity or marketplace-specific comparison requires domain interpretation | stable product entities + exact/similar match confidence + marketplace decision handoff |
| Buyer Research | grounded buyer basis required | buyer evidence synthesis |
| Ad & Funnel Intelligence | current market/ad/funnel evidence required | observed competitor/funnel mechanisms |
| Ads Strategy | commercial concept or ad copy required | persuasion hypothesis + concept brief |
| Script & Performance | spoken/scripted content required | executable script / beat plan |
| Image Direction | still or image-reference asset required | image production spec |
| Video Direction | generated/edited motion required | timed scene spec |
| Video Evidence Inspection | material claims about a video require structured visual/audio coverage | timestamped inspection evidence package |
| Talking Persona | recurring speaking persona | persona talking production brief |
| Typography & Layout | visible text / graphic hierarchy | controlled text/layout spec |
| Audio & Voice Performance | speech/music/SFX/voice identity | audio performance spec |
| Organic Content Craft | non-paid social/editorial content | social-native content brief |
| Platform Meta | Meta placement materially changes execution | Meta execution guidance |
| Route Compilation | provider/model execution required | route-native execution spec |
| QA · Evidence & Rights | claims/offer/rights/disclosure | factual/commercial verdict |
| QA · Realism & Performance | visual/audio/media acceptance | media-quality verdict |
| Localized Repair | accepted work contains localized defect | minimum causal repair plan |

---

# 16. Growth Rule

Do not add a new specialist because a label sounds useful.

Create or split a method only when at least one is true:

```text
existing method cannot express the craft depth needed
repeated failures show a distinct decision discipline
a platform/medium imposes materially different execution grammar
independent calibration examples justify separate treatment
```

The goal is expert depth with controlled loading, not a decorative taxonomy.

For the currently adopted cross-cutting methods, the formal Growth Rule justification is **existing method cannot express the craft depth needed**: generic buyer/ad/organic methods did not own provider-neutral cross-domain research execution, and generic QA/audio/video-direction methods did not own provenance-aware video evidence preparation. “Avoid duplication” may support the design but is not an independent Growth Rule criterion.


---

# 17. V2.3 Product / Marketplace Intelligence Candidate

Method ID:

```text
PRODUCT_MARKETPLACE_INTELLIGENCE
```

It exists because the U1 ablation showed a recurring domain decision discipline not cleanly owned by generic Research Evidence or Buyer Research:

- exact product vs substitute;
- stable product/listing/seller/variant entities;
- cross-market listing equivalence confidence;
- product-family vs variant identity;
- marketplace-specific product comparison;
- bounded product-level demand signal meaning;
- stable entity transfer into downstream creative work.

It must consume canonical schemas from:

```text
RESEARCH_EVIDENCE_SYNTHESIS
→ source outcomes / freshness / corroboration / PARTIAL vs NO_RESULTS

BUYER_RESEARCH
→ buyer/review semantics when applicable
```

It may not redefine those schemas.

Role contract:

```text
RECEIVES
=
research evidence + product/listing refs + current project constraints

DECIDES
=
entity identity / equivalence / exact-vs-similar confidence / product-level marketplace interpretation

DELIVERS
=
stable entities + decision evidence + explicit uncertainty + source refs

MAY NOT DECIDE
=
generic source truth outside evidence
creative production
supplier purchase/contact authority
contracts
customs/legal compliance
supplier due-diligence guarantees
```

Growth Rule result:

```text
existing method cannot express the craft depth needed
=
PASS

separate supplier specialist required by current U1/U2 corpus
=
NO
```

`SUPPLIER_SOURCING_DUE_DILIGENCE` remains a dormant extension hook. It is created only if real tasks demonstrate deeper supplier-risk/certification/legal-entity/manufacturer-vs-trader semantics that overload Product/Marketplace Intelligence.


---

## V2.4 real-world hardening — substantive completeness and creative permission

Select the requested deliverable's canonical completeness contract **before production** from `AI_Creative_Skill_Deliverable_Completeness_Catalog_Pre-v0.1-V2.4-CANDIDATE.md`. Narrower methods own meaning, the Catalog owns the cross-method minimum field declaration, runtime/Contracts own validation evidence. Resolve required/conditional/optional/open based on the **bounded requested deliverable**, not a universal 20-field template. A name-only request must not trigger an entire Character Bible. All `FULL` items receive a bounded per-item self-check against substantive content and canonical sources. Empty headings, generic fillers, ungrounded source claims and unspecified omissions fail relevant checks. Unknown facts stay unknown; do not invent to satisfy the schema.

The producer is invited to add valuable optional creative elements, richer backstories, gestures, surprising payoffs and narrative detail if authority permits. This is `CREATIVE_OPEN`, not license to violate exact copy, product truth, rights, identity, approved scope or claim boundaries.

To form a complete new `CHARACTER_BIBLE` within Organic/Ads, combine content/persona positioning with Script/Performance behavior and Image Direction identity; Talking Persona is added when visible recurring speech applies. Do not introduce a standalone `CHARACTER_IDENTITY_DESIGN` method without composition/ablation proof of recurring deficiency. Per-method rubric passing must be recorded as self-check, not declared independently validated unless the independent reviewer actually inspected the output.

