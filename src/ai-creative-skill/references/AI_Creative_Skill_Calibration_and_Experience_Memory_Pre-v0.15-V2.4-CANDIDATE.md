> **V2.4 CANDIDATE SCOPE:** Modified version of this method family. Read the final section “V2.4 real-world hardening” for current candidate additions. Historical V2.3 discussion and prior-source pointers below remain provenance, not active version resolution.

# AI Creative Skill · Calibration and Experience Memory · Pre-v0.15-V2.4-CANDIDATE

## Status

```text
DOCUMENT TYPE
=
CALIBRATION / EXPERIENCE MEMORY DESIGN

VERSION
=
Pre-v0.15-V2.4-CANDIDATE

DATE
=
2026-10-16

PARENT_DOCUMENT
=
AI_Creative_Skill_Architecture_Spec

LAST_VALIDATED_AGAINST
=
AI_Creative_Skill_Architecture_Spec_Pre-v0.15-V2-CANDIDATE.md

STATUS
=
DESIGN DOCUMENT
NOT INSTALLED
```

GPT validation hardening branch (2026-10-10): Pre-v0.13-V2-CANDIDATE adds `SIMULATION_ONLY` as an explicit observation origin, preventing model-based test outcomes from becoming project-empirical provider facts; it also tightens provider/model/version scope and expiry/revalidation of empirical lessons.

Z4/Z4.1 creative-balance hardening branch (2026-10-11): Pre-v0.14-V2.2-CANDIDATE adds canon-promotion boundaries for expressive choices, longitudinal canon anchoring, creative-divergence/mode-collapse calibration and pairwise review guidance that treats compliance as a gate rather than the whole creative ranking.


This document defines how the skill should turn real execution history into reusable competence without converting one anecdote into a universal rule.

Validator correction round (operator-agreed window, 2026-10-09): Pre-v0.12 gives each initial third-party visual/video failure class in §14.1 its own `signal_origin_class`, `hypothesis_status` and `source_ref`, separating what the G1 source posts state from analyst extensions (`analyst_extension` field in the §14.1 schema); identifies each quoted Higgsfield post by the sha256 of its summarized note and of the validator's raw capture that holds the quote (§14.1, §17.1, §19); adds §17.1 with the four G2 third-party talking-performance hypotheses that Ledger §22 had routed here without recording them; adds `source_ref` with short literal quotes to the §18 and §19 external cases and corrects the §19 declared-count case (total count × per-row count: the documented failure gave only a total, in a one-sentence prose prompt; prompt N5, also one prose sentence, gave per-row counts 7/6/7 and matched; the numbered-list prompt N11 was not counted); adds `signal_origin_class = THIRD_PARTY_TOOL_DIAGNOSTIC` and uses it for predictive scores in §18.1; and states in §8.1 that `variant_family_id` and Execution Contracts `variation_batch_id` are different concepts. Canonical names follow Execution Contracts Pre-v0.16 §1.1. No calibration rule is promoted.

Pre-v0.11 adds scoped third-party information-dense-image counterexamples: declared counts can still fail in output, readable mathematical/technical content can still be wrong or invented, structured prompts can contain internal collisions, and reference text can leak into derived imagery. These remain external anti-examples rather than provider laws. Pre-v0.10 commercial-generation counterexamples and predictive-score handling remain in force.

---

# 1. Experience Is Scoped Evidence

```text
ONE FAILURE
≠
UNIVERSAL MODEL LAW
```

Every reusable lesson must retain scope:

```text
model / route / provider
operation
input/reference conditions
prompt/spec version
observed output
date
confidence
```

Repeated evidence may increase confidence. Contradictory evidence must remain visible.

---

## 1.1 End-of-Run Learning Capture and Promotion

After a materially relevant execution, the system may perform a quiet internal learning check before final state persistence. It is not a required user-facing step and does not authorize adjacent work.

Useful prompts are:

```text
DID A STEP FAIL OR REQUIRE A WORKAROUND?
DID THE OPERATOR / REVIEWER CORRECT OR REJECT SOMETHING MATERIAL?
DID THE RUN REVEAL A SCOPED FACT OR FAILURE MODE A FUTURE RUN MAY NEED?
```

If all answers are immaterial, record nothing. Do not manufacture a lesson merely because a run ended.

When a material observation exists:

```text
OBSERVATION
→ SCOPED EVIDENCE / FAILURE / PREFERENCE RECORD
→ CONFIDENCE + COUNTEREVIDENCE PRESERVED
→ OPTIONAL CHANGE PROPOSAL
→ REVIEW / OPERATOR APPROVAL
→ VALIDATION
→ VERSIONED CANONICAL PROMOTION
```

A proposal may be justified by repeated evidence **or** by one clearly objective/deterministic defect, safety/governance issue or otherwise high-confidence correction whose scope is explicit. One aesthetic rejection still does not become universal preference law.

```text
LEARNING CAPTURE
!=
AUTOMATIC SKILL EDIT

SELF-REVIEW
!=
CANONICAL AUTHORITY
```

Do not append a routine "I learned X / should I update the skill?" message to the requested deliverable. Surface the proposal only when operator governance requires a decision or when the user explicitly asks about learned changes.

For packaged runtime rules, canonical changes must occur in the authoritative package/design source and follow its version/promotion discipline; an installed runtime copy must not silently rewrite itself.

---

## 1.2 Observation Origin and Promotion Barrier

Every reusable observation declares an origin class when promotion risk exists:

```text
SIMULATION_ONLY
CONTROLLED_TEST
PROJECT_EMPIRICAL
THIRD_PARTY
THIRD_PARTY_TOOL_DIAGNOSTIC
USER_PREFERENCE
```

`SIMULATION_ONLY` can validate logic, invariants or hypotheses but cannot automatically promote into `PROJECT_EMPIRICAL`, provider reliability, quality ranking or measured-performance evidence. Promotion requires new evidence from the target empirical class.

Provider/model lessons additionally retain the applicable provider, route, model/version, operation and configuration scope. A materially new model/version makes the old lesson historical until revalidated; it does not erase history or silently transfer current confidence.

---

# 2. Causal Before / After Case

A high-value learning case records:

```yaml
case_id:
request_class:
route:
input_refs:
spec_before:
output_before:
defect:
probable_cause:
primary_change:
spec_after:
output_after:
improved:
regressed:
transferable_principle:
confidence:
```

The point is to preserve cause-and-effect hypotheses, not only before/after screenshots.

---

# 3. Known-Failure Preflight

Before a paid submission, compare the compiled request against applicable known failures.

```text
COMPILED REQUEST
→ KNOWN FAILURE CHECK
→ MITIGATE / ACCEPT RISK / BLOCK
→ SUBMIT
```

Example pattern:

```text
known defect:
spoken phrase repeated when the same dialogue appears in multiple prompt roles

current request:
phrase appears in speech + scene description

preflight:
remove duplicate speech content before submission
```

Failure memory should prevent repeated known mistakes, not merely explain them afterward.

---

# 4. Regression Risk Before Repair

Before a retry or regeneration:

```yaml
repair_target:
accepted_state:
weakly_anchored_state:
regression_risk:
mitigation:
primary_change:
```

The system must know what is currently correct and may be lost.

```text
FIX ONE DEFECT
≠
AUTHORIZE RANDOM CHANGE ELSEWHERE
```

---

# 5. Controlled Repair Learning

When diagnosing a defect, prefer one main causal intervention per retry when practical.

Multiple changes are allowed when technically inseparable, but the record should say so.

Changing model, prompt, reference, duration, framing and lighting at once may improve the output but produces poor learning.

---

# 6. Creative Preference Memory

Keep three categories separate:

```text
OBJECTIVE DEFECT
PROJECT / PERSONA RULE
OPERATOR CREATIVE PREFERENCE
```

A preference record may include:

```yaml
preference_id:
scope:
statement:
evidence_examples:
explicit_operator_statement:
repeated_approval_rejection_pattern:
confidence:
last_confirmed:
```

One rejection does not automatically become a permanent preference.

Preferences help rank technically valid options. They do not redefine physics, truth or policy.

---

## 6.1 Expressive Choice → Canon Promotion Boundary

A generated or operator-selected expressive choice does not become project/persona canon merely because it appears repeatedly.

```text
REPEATED GENERATED CHOICE
!=
CANON

ACCEPTED EXPRESSIVE CHOICE
!=
PERMANENT LOCK
```

Promotion to identity/continuity authority requires an applicable governance path, such as explicit Project/Profile authority, explicit operator decision, or another already-authorized canonical-promotion mechanism.

When promotion occurs, retain enough evidence to know:

```yaml
canon_promotion_ref:
source_dimension:
prior_latitude:  # BOUNDED_VARIATION | OPEN_EXPLORATION
promoted_scope:
authority_ref:
effective_from:
affected_future_work:
```

Promotion is scoped. A jacket accepted as recurring wardrobe does not automatically freeze lighting, camera, gesture or every other dimension of the scene.

---


# 7. Canonical Exemplars

For recurring voice/style/persona work, curate a small representative set rather than loading the entire archive.

Possible exemplar classes:

```text
casual explanation
story / anecdote
reaction / commentary
commercial-adjacent mention
high-energy / low-energy variants when canonical
```

Each exemplar should say what it teaches and what must not be copied mechanically.

Anti-exemplars are equally valuable when they show language that is superficially similar but not canonical.

---

# 8. Canonical Benchmark Pack

Route/model/provider comparisons should use fixed cases where possible.

Initial design pack:

```text
BENCH-STATIC-01
product identity + exact text + hierarchy

BENCH-REF-01
recurring character + environment/reference preservation

BENCH-ACTION-01
single controlled physical interaction

BENCH-TALK-01
short PT-BR talking clip + exact script + voice requirement

BENCH-CONTINUITY-01
two linked shots with explicit end/start state
```

Every benchmark preserves:

```text
same requirements
same source assets
same acceptance rubric
same review procedure
```

Provider/model differences should not be inferred from unrelated prompts.

---

## 8.1 Controlled Variant Families

When the purpose is a controlled comparison or a deliberately coherent campaign/series family, declare what stays invariant and what is intentionally changed instead of treating every repeated specification as accidental sameness.

```yaml
variant_family_id:
purpose:  # CONTROLLED_COMPARISON | DELIBERATE_SERIES_FAMILY | OTHER
preserved_dimensions:
varied_dimensions:
shared_spec_refs:
variant_input_refs:
review_scope:
```

Typical preserved dimensions may include camera behavior, timing structure, shot function, layout grammar or another deliberately fixed factor. Typical varied dimensions may include subject, product, environment, hook or another explicitly selected variable.

```text
CONTROLLED VARIANT FAMILY
=
DECLARED PRESERVE SET
+
DECLARED VARY SET

PRESERVED SPECIFICATION
!=
AUTOMATIC ACCEPTANCE OF EVERY OUTPUT
```

Each generated/output variant remains independently reviewable. A fixed camera/motion specification may be useful precisely because it isolates the changed variable across separate outputs; that does not override `VIDEO_DIRECTION` rules against accidental repeated-loop feel inside one sequence.

Use this record only when invariance serves comparison, learning or deliberate family continuity. Do not freeze creative dimensions merely to make variants easier to label.

`variant_family_id` is not the Execution Contracts `variation_batch_id`. A variation batch is one bounded execution of N accepted variants with its own approval, budget and attempt state; a variant family is the comparison/series grouping whose preserve/vary sets serve learning or deliberate continuity. A family may be produced by one or more batches, and a batch need not form a family. When family outputs are produced through a variation batch, reference its `variation_batch_id` instead of duplicating approval/budget/attempt state here (Execution Contracts §1.1).

---

## 8.2 Creative Balance / Longitudinal Drift Calibration

Creative calibration should distinguish at least four outcomes:

```text
CONSISTENT + EXPRESSIVE
→ stable identity/continuity with useful variation

CONSISTENT + REPETITIVE
→ stable identity but unnecessary mode collapse in open dimensions

NOVEL + GROUNDED
→ materially new expression that still satisfies authority/objective

NOVEL + RANDOM
→ difference without sufficient relevance, continuity or purpose
```

For longitudinal work, compare new outputs to current canonical / approved identity-bearing authority rather than relying only on the immediately previous derivative. A previous derivative may be a useful scoped continuity reference, but it is not a substitute for canon unless promoted.

Pairwise creative review may compare technically valid candidates on objective fit, relevance, specificity, distinctiveness and supported surprise. Do not create universal numerical novelty thresholds from model-based simulations. Project/operator preference and real performance evidence may later calibrate ranking at their valid scope.

For concept families where distinctness is requested, record whether candidates differ materially across declared `OPEN_EXPLORATION` dimensions. For controlled-comparison families, repetition in deliberately preserved dimensions is not a defect.

A diagnostic `creative_latitude_utilization` record may be used to detect over-control, but it is not a universal maximize-everything score:

```yaml
creative_latitude_utilization:
  declared_open_dimensions:
  actually_varied_dimensions:
  intentionally_held_dimensions:
  nonvariation_reason:
  review_state:  # HEALTHY | REVIEW_OVERCONTROL | NOT_APPLICABLE
```

Not every open dimension must vary in every asset. The diagnostic asks whether the chosen concept meaningfully used the legitimate space it needed, not whether it changed everything it was allowed to change.

---


# 9. Uncertainty-First Canary

Before scaling a costly task, identify the highest-risk unknown.

```text
HIGHEST-RISK UNKNOWN
→ LOWEST-COST VALID TEST
→ REVIEW
→ ONLY THEN SCALE
```

Examples:

- test one talking clip before generating ten variants;
- test one exact-text static before a full campaign family;
- test one physical interaction before a multi-shot sequence depends on it.

A canary is task-specific validation, not a generic provider benchmark.

---

## 9.1 Draft → Final Evidence Transfer

A low-cost draft/canary proves only the properties actually exercised by that draft **and** preserved by the final lineage. Do not silently promote a draft verdict into final-artifact acceptance.

```yaml
draft_evidence_ref:
final_lineage_relation:  # SAME_ACCEPTED_MEDIA_TRANSFORM | DETERMINISTIC_RERENDER | STOCHASTIC_REGENERATION | UNKNOWN
transferable_checks:
nontransferable_checks:
final_review_required:
lineage_evidence_ref:
```

Interpretation:

```text
SAME_ACCEPTED_MEDIA_TRANSFORM
→ unaffected accepted properties may carry forward
→ transformed/final-resolution properties still require applicable review

DETERMINISTIC_RERENDER
→ transfer only properties that the verified rerender semantics actually preserve
→ final output still receives applicable review

STOCHASTIC_REGENERATION
→ new artifact / new take
→ draft may validate prompt, scene logic, feasibility or route behavior
→ identity / performance / artifact acceptance does not carry automatically

UNKNOWN
→ do not assume artifact-level acceptance transfers
```

A concrete route may later record verified draft/final behavior in its Registry/Route Recipe evidence. This calibration document does **not** invent a route fact merely because a third-party tutorial uses a draft-first workflow.

---

# 10. Performance Instrumentation Before Publication

When publication/performance learning is in scope, define creative identifiers before distribution.

At minimum where applicable:

```text
concept_id
variant_id
asset_id
hook_id
opening_type
format
persona
platform
publication_id
campaign / audience context
```

Then attach observed metrics to the publication instance, not vaguely to the asset.

Metrics without creative lineage produce anecdotes, not learning.

---

# 11. Pairwise Review

When several candidates are technically acceptable, pairwise comparison can be more discriminating than giving all of them similar numerical scores.

```text
A vs B
→ which better satisfies the stated objective and why?

winner vs C
→ repeat with the same rubric
```

Where possible, hide provider/model identity from creative reviewers to reduce brand bias.

---

# 12. Real-Use Context Tests

Calibration examples should include use-context checks where relevant:

```text
thumbnail test
first-frame test
1-second comprehension
muted test
phone-size test
crop / safe-area test
audio-on intelligibility test
```

An artifact that works only when enlarged in an editor is not necessarily fit for social delivery.

---

# 13. Edge-Case Library

Build cases around recurring difficult surfaces, for example:

```text
transparent packaging
mirrors / glasses / reflections
jewelry
small objects in hands
liquids
food deformation
readable labels
multiple people
hair across face
fast speech
numbers / prices
screens / UI
before-after claims
very small products
```

Each edge case should record common failure, specification strategy, inspection method and repair strategy.

---

# 14. Failure → Repair Cookbook

Examples:

| Defect | Likely surface | Preferred first repair |
|---|---|---|
| wrong CTA text | controlled text layer | replace text layer |
| subtitle timing | timing/finishing | retime captions |
| voice identity wrong | audio binding | voice replacement / regenerate audio stage |
| lipsync wrong with correct audio | sync stage | repair lipsync, preserve audio |
| one broken hand | localized visual defect | targeted edit if capable |
| product geometry wrong | reference/model execution | product-preserving edit or affected-shot regeneration |
| pacing weak | edit/timing | recut before regenerating performance |
| unsupported claim | strategy/evidence | return to evidence gate |
| chatbot/drafting residue in final copy | text/copy surface | remove wrapper after protected-text check |
| unsupported borrowed authority | evidence/copy | resolve source or narrow/remove authority wording |

The cookbook is a starting heuristic, not a guarantee of root cause.

## 14.1 Third-party visual / video failure hypotheses

External tutorials, provider failure tables and before/after examples may seed **diagnostic hypotheses**, but they do not become project-empirical root-cause rules merely because the example looks convincing. Preserve source interest, scope and counterevidence.

```yaml
visual_failure_case_id:
source_ref:
analyst_extension:     # wording not stated by the source (or none); that part is ANALYST_HYPOTHESIS, UNVALIDATED
signal_origin_class:  # THIRD_PARTY_METHOD_REFERENCE | THIRD_PARTY_TOOL_DIAGNOSTIC | ANALYST_HYPOTHESIS | PROJECT_EMPIRICAL
hypothesis_status:     # UNVALIDATED | SUPPORTED | NARROWED | REJECTED
symptom_pattern:
hypothesized_surface:
prevention_candidate:
detection_check:
first_repair_candidate:
false_positive_context:
operator_or_reviewer_verdict:
confidence:
```

Initial third-party classes, from the G1 Higgsfield blog source group (Ledger §21). Each `source_ref` names the post slug, the sha256 of the captured note `higgsfield-blog_<slug>.md` in `/Google Drive/ai/influencer/utils/higgsfield-blog/` (`note sha256`), the sha256 of the validator's raw text capture `hblog/raw/<slug>.txt` (`raw sha256`) and a quote from the post (`https://higgsfield.ai/blog/<slug>`), as captured by the validator on 2026-10-08. The literal quote comes from the raw capture; the notes are summarized captures and do not contain the quoted wording. `analyst_extension` marks wording that the posts do not state; that part is `ANALYST_HYPOTHESIS`, `UNVALIDATED`.

```yaml
- visual_failure_case_id: EXT-VID-LIGHT-01
  symptom_pattern: unmotivated / duplicated / flickering light
  signal_origin_class: THIRD_PARTY_METHOD_REFERENCE
  hypothesis_status: UNVALIDATED
  source_ref:
    - "why-ai-video-generations-fail · note sha256 f1d46850f1290e2df590bd0094da72593ca5361937850e977fd1139c37bd44b5 · raw sha256 61fda88c3ceb6bdb877189e8efc629e8b9b1a4714b11c2214e81030cd3a3dcc5 · \"Lighting flickers in a way no real light source would.\""
    - "ai-video-prompt-mistakes · note sha256 52ca080c1133a6177db8ca3c1a5e5a71e461a855b6938da84abe5ea6b570f950 · raw sha256 eb6355053206b49f682d47e6c78567fbdc1e7459e4c655af635725a8b390ec71 · \"what came back showed two suns\""
    - "ai-video-look-real-2026 · note sha256 d64bfade5c8cf3636dc0fa43309c205435fbc002a9018fc71efa9e795b578c00 · raw sha256 2e3be57d6ce1760f63d334d79c09a2fb54dee0211fa5df32b640b0fd0cdde33f · \"The light has an obvious source.\""
  analyst_extension: none

- visual_failure_case_id: EXT-VID-RIGID-GEOMETRY-01
  symptom_pattern: rigid geometry that warps or changes scale under motion
  signal_origin_class: THIRD_PARTY_METHOD_REFERENCE
  hypothesis_status: UNVALIDATED
  source_ref:
    - "ai-video-prompt-mistakes · note sha256 52ca080c1133a6177db8ca3c1a5e5a71e461a855b6938da84abe5ea6b570f950 · raw sha256 eb6355053206b49f682d47e6c78567fbdc1e7459e4c655af635725a8b390ec71 · \"a rigid aircraft ends up flexing mid-turn like it's made of rubber\""
    - "how-to-avoid-distortions-ai-videos · note sha256 dc50850e4b71717e51aa44032f701209496b7e3c450ac862498f2982b3159e91 · raw sha256 0bb7b2726a3ed86cd319ac3a71ddc52b7c1ff4d043b0ce64ef459fb85fc17de6 · \"backgrounds that warp mid-sequence\""
  analyst_extension: "changes scale under motion"

- visual_failure_case_id: EXT-VID-WEIGHT-SUPPORT-01
  symptom_pattern: body motion without support / footfall / weight transfer
  signal_origin_class: THIRD_PARTY_METHOD_REFERENCE
  hypothesis_status: UNVALIDATED
  source_ref:
    - "ai-video-look-real-2026 · note sha256 d64bfade5c8cf3636dc0fa43309c205435fbc002a9018fc71efa9e795b578c00 · raw sha256 2e3be57d6ce1760f63d334d79c09a2fb54dee0211fa5df32b640b0fd0cdde33f · \"A body gliding with no weight transfer is one of the fastest tells\""
    - "why-ai-video-generations-fail · note sha256 f1d46850f1290e2df590bd0094da72593ca5361937850e977fd1139c37bd44b5 · raw sha256 61fda88c3ceb6bdb877189e8efc629e8b9b1a4714b11c2214e81030cd3a3dcc5 · \"A character floats slightly above the ground.\""
  analyst_extension: none

- visual_failure_case_id: EXT-VID-BACKGROUND-STATE-01
  symptom_pattern: background state that appears, disappears or melts without scene cause
  signal_origin_class: THIRD_PARTY_METHOD_REFERENCE
  hypothesis_status: UNVALIDATED
  source_ref:
    - "why-ai-video-generations-fail · note sha256 f1d46850f1290e2df590bd0094da72593ca5361937850e977fd1139c37bd44b5 · raw sha256 61fda88c3ceb6bdb877189e8efc629e8b9b1a4714b11c2214e81030cd3a3dcc5 · \"A background detail, a piece of furniture, a second character, changes slightly or disappears between frames.\""
    - "how-to-avoid-distortions-ai-videos · note sha256 dc50850e4b71717e51aa44032f701209496b7e3c450ac862498f2982b3159e91 · raw sha256 0bb7b2726a3ed86cd319ac3a71ddc52b7c1ff4d043b0ce64ef459fb85fc17de6 · \"backgrounds that warp mid-sequence\""
  analyst_extension: "appears; the posts name change, disappearance and warping between frames"

- visual_failure_case_id: EXT-VID-HAND-CONTACT-01
  symptom_pattern: hand / object contact that fuses, penetrates or loses support
  signal_origin_class: THIRD_PARTY_METHOD_REFERENCE
  hypothesis_status: UNVALIDATED
  source_ref:
    - "ai-video-prompt-mistakes · note sha256 52ca080c1133a6177db8ca3c1a5e5a71e461a855b6938da84abe5ea6b570f950 · raw sha256 eb6355053206b49f682d47e6c78567fbdc1e7459e4c655af635725a8b390ec71 · \"Extra fingers, fused hands, AI slop\" / \"Points of contact were never specified\""
  analyst_extension: "penetrates or loses support"

- visual_failure_case_id: EXT-VID-CAMERA-APPARATUS-01
  symptom_pattern: camera behavior inconsistent with the intended capture apparatus
  signal_origin_class: ANALYST_HYPOTHESIS
  hypothesis_status: UNVALIDATED
  source_ref:
    - "ai-video-look-real-2026 · note sha256 d64bfade5c8cf3636dc0fa43309c205435fbc002a9018fc71efa9e795b578c00 · raw sha256 2e3be57d6ce1760f63d334d79c09a2fb54dee0211fa5df32b640b0fd0cdde33f · \"A camera that's too stable and too smooth is one of the clearest signs that a shot was generated\""
  analyst_extension: "the whole class; the post states only the narrower too-stable/too-smooth signal, which Ledger §21.4 does not adopt as a universal defect"
```

These classes may point QA toward an observable defect and Repair toward a likely surface. They do **not** prove the generating cause, provider weakness or best fix. The canonical acceptance criteria remain in the owning QA/method documents.

### Repeatability as a diagnostic hypothesis

When prior attempts already exist, variation across them may contribute evidence to root-cause diagnosis:

```text
DEFECT VARIES MATERIALLY ACROSS OTHERWISE COMPARABLE ATTEMPTS
→ may suggest underconstraint / stochastic route behavior / unstable reference binding

DEFECT REPEATS IN THE SAME WAY ACROSS OTHERWISE COMPARABLE ATTEMPTS
→ may suggest deterministic parameter / reference / compilation / route behavior
```

Source split:

```yaml
source_backed_part:
  statement: a defect that changes on every run points to an underspecified prompt; a defect that is wrong the same way every time points to settings
  signal_origin_class: THIRD_PARTY_METHOD_REFERENCE
  hypothesis_status: UNVALIDATED
  source_ref: "ai-video-prompt-mistakes · note sha256 52ca080c1133a6177db8ca3c1a5e5a71e461a855b6938da84abe5ea6b570f950 · raw sha256 eb6355053206b49f682d47e6c78567fbdc1e7459e4c655af635725a8b390ec71 · \"A prompt problem changes on every run. A settings problem is wrong the same way every time\""
analyst_extension:
  statement: the causal candidates beyond prompt vs settings (stochastic route behavior, unstable reference binding, reference / compilation / route behavior)
  signal_origin_class: ANALYST_HYPOTHESIS
  hypothesis_status: UNVALIDATED
```

Both parts remain unvalidated unless project evidence supports them. Do not spend or create extra attempts solely to classify the pattern; use executions that already exist or a separately justified canary.

---

# 15. Stop Criterion for Quality Iteration

Do not regenerate an accepted result only because a hypothetical better result might exist.

A new attempt requires a reason such as:

```text
unmet acceptance criterion
material objective defect
approved experiment
known high-value uncertainty
operator-requested alternative
```

```text
ACCEPTED
≠
PERFECT IN THE ABSTRACT
```

The purpose is consistent excellent work within scope, not infinite aesthetic search.

---

# 16. Text / Copy Calibration Cases

External writing-pattern checklists are calibration hypotheses, not project law. Before promoting a style signal into a reusable rule, preserve language, content type and voice authority. `SCRIPT_PERFORMANCE` owns the canonical text-finding schema; calibration stores `text_finding_ref` for concrete findings and adds only calibration-specific hypothesis/history fields.

```yaml
text_case_id:
language:
content_mode:
source_ref:
signal_origin_class:  # THIRD_PARTY_METHOD_REFERENCE | THIRD_PARTY_TOOL_DIAGNOSTIC | ANALYST_HYPOTHESIS | PROJECT_EMPIRICAL
hypothesis_status:    # UNVALIDATED | SUPPORTED | NARROWED | REJECTED
voice_authority_ref:
text_finding_ref:  # canonical Script finding when a concrete observed instance exists
hypothesis_pattern_description:  # allowed for hypothesis-only calibration with no concrete finding yet
false_positive_context:
protected_text_refs:
calibration_recommendation:
change_delta_summary:
semantic_fidelity_check:
operator_or_reviewer_verdict:
transferable_principle:
confidence:
```

Examples borrowed from an external source remain `THIRD_PARTY_METHOD_REFERENCE` until a project case confirms, narrows or rejects the lesson. Integration-review suggestions that are not present in the source and have not been observed in project evidence remain `ANALYST_HYPOTHESIS` with `hypothesis_status = UNVALIDATED`.

For the current Humanizer integration, PT-BR prompts such as `não é só X, é Y`, `A verdade é que...`, `Vamos lá...` and `E isso muda tudo.` are analyst hypotheses only. They must not be promoted into PT-BR audience rules without empirical calibration.

For recurring personas:

```text
CANONICAL VOICE EXAMPLE
>
GENERIC “AI WRITING” HEURISTIC
```

The calibration objective is not to make every text stylistically irregular. It is to distinguish intentional voice from generic model defaults without changing truth, approved wording or required disclosure.
---

# 17. Media / Transcript Calibration Hypotheses

External implementation reports may contribute scoped media-inspection hypotheses without becoming project law. Current third-party hypothesis:

```yaml
media_case_id: EXT-ASR-PTBR-01
signal_origin_class: THIRD_PARTY_METHOD_REFERENCE
hypothesis_status: UNVALIDATED
scope: PT-BR speech verification
observation_hypothesis: English-only ASR/transcription models may translate, distort or otherwise fail to preserve PT-BR speech faithfully.
operational_guardrail: declare the known target language/locale when supported; treat an ASR model that does not support the target language as ineligible for material verification.
authoritative_check: human or otherwise authoritative listening remains required where exact speech/voice verification is mandatory.
```

This entry is a calibration hypothesis derived from reviewed external tooling behavior. It may be promoted, narrowed or rejected only through scoped project evidence.

## 17.1 Third-party talking-performance hypotheses (G2)

Ledger §22 (G2 persona / voice) routed four third-party hypotheses here. All four come from one captured post, `make-ai-lipsync-videos` (note `higgsfield-blog_make-ai-lipsync-videos.md`, sha256 `11dfb5c49429371fb48d6fa84b8f3ce351592e6dff5506d07d02c686972300e5`; raw text capture `hblog/raw/make-ai-lipsync-videos.txt`, sha256 `ed70d98ac731e7be345b6c09d9ddca819428f42a78474b5c451d5131e5655cb7`; post `https://higgsfield.ai/blog/make-ai-lipsync-videos`, captured by the validator on 2026-10-08). The quotes in `source_ref` come from the raw capture; the note is a summarized capture and does not contain them. They are diagnostic hypotheses for Talking Persona / Audio review, not route facts or project rules.

```yaml
- media_case_id: EXT-TALK-FROZEN-FACE-01
  signal_origin_class: THIRD_PARTY_METHOD_REFERENCE
  hypothesis_status: UNVALIDATED
  scope: talking-head / lipsync performance
  observation_hypothesis: a flat source expression or flat (monotone) audio may contribute to a frozen face outside the mouth
  source_ref: "make-ai-lipsync-videos · \"The cause is usually a source image with a neutral, flat expression.\" / \"A flat audio track produces a flat face regardless of which model you use.\""

- media_case_id: EXT-TALK-GESTURE-REPEAT-01
  signal_origin_class: THIRD_PARTY_METHOD_REFERENCE
  hypothesis_status: UNVALIDATED
  scope: talking-head / lipsync performance
  observation_hypothesis: longer single generations may accumulate repeated gestures / head movements
  source_ref: "make-ai-lipsync-videos · \"Gesture repetition accumulates in longer generations but resets on each new clip.\""

- media_case_id: EXT-TALK-FIXED-GAZE-01
  signal_origin_class: THIRD_PARTY_METHOD_REFERENCE
  hypothesis_status: UNVALIDATED
  scope: talking-head / lipsync performance
  observation_hypothesis: fixed gaze / mechanical blink may be a route or tool limit rather than a prompt defect
  source_ref: "make-ai-lipsync-videos · \"Most tools default to a fixed blink interval and minimal gaze variation. The fix depends on the tool.\""

- media_case_id: EXT-TALK-SUBTLE-EMOTION-01
  signal_origin_class: THIRD_PARTY_METHOD_REFERENCE
  hypothesis_status: UNVALIDATED
  scope: voice-to-face emotional transfer
  observation_hypothesis: subtle emotions may not transfer reliably from voice to face on some routes
  source_ref: "make-ai-lipsync-videos · \"Subtle emotions like skepticism, distraction, or irony don't transfer reliably from voice to face on any current tool.\""
```

The source's clip-length thresholds and tool comparisons are not imported. The post's "any current tool" is a provider claim; record it only as a hypothesis scoped to the route actually used. Recurring-persona clip length remains owned by the Project Profile and Talking Persona.

---

# 18. External commercial-generation anti-examples

A third-party workflow execution may be useful precisely because it fails commercial truth boundaries. Record such cases as **counterexamples**, not as audience truth and not as proof that every route will fail in the same way.

Current G5 external cases from the inspected `content-factory` run. `source_ref` quotes the transcript `content-factory.txt` (sha256 `d780b15fbb3d2b62228d72868f32d57b5e05616a1442774e5514aca8c607a36c`, 16,801 bytes); the quoted lines are spoken by generated presenters in the demonstrated outputs or by the tutorial narrator about them.

```yaml
- media_case_id: EXT-COM-GEN-SPEECH-01
  signal_origin_class: THIRD_PARTY_METHOD_REFERENCE
  hypothesis_status: UNVALIDATED
  observed_pattern: generated speech introduces an unsupported product-composition claim
  source_ref: "content-factory.txt · \"100% natural orange juice\" / \"No sugar, no nonsense, just orange.\""
  transferable_check: compare actual generated speech with product/claim authority before commercial acceptance

- media_case_id: EXT-COM-SYNTH-PROOF-01
  signal_origin_class: THIRD_PARTY_METHOD_REFERENCE
  hypothesis_status: UNVALIDATED
  observed_pattern: generated presenter supplies rating / duration-of-use / status-based social proof without underlying customer evidence
  source_ref: "content-factory.txt · \"Honestly, 9 out of 10.\" / \"Higs Kiwi has been my 3PM thing for 2 weeks straight.\" / \"if he buys this product, why shouldn't you?\""
  transferable_check: synthetic performance does not create testimonial/review evidence

- media_case_id: EXT-COM-PACKAGING-01
  signal_origin_class: THIRD_PARTY_METHOD_REFERENCE
  hypothesis_status: UNVALIDATED
  observed_pattern: route invents packaging and then repeats it consistently across outputs
  source_ref: "content-factory.txt · \"Also invented the box for us.\" / \"Same box. It's consistent with the previous video, which is very important.\""
  transferable_check: consistency of a generated detail does not make that detail product truth
```

These cases reinforce existing Evidence & Rights and Ads Profile rules. They do not require spending credits to reproduce them. Promote a narrower causal rule only if project evidence later supports it.

## 18.1 Predictive creative scores

A third-party virality/hook/retention/engagement score may be stored as a diagnostic observation with its tool/model/version and asset reference. Its `signal_origin_class` is `THIRD_PARTY_TOOL_DIAGNOSTIC`: an output of an external scoring/diagnostic tool about our asset, as distinct from `THIRD_PARTY_METHOD_REFERENCE` (a method or example borrowed from an external source). This is the same class that Work Profile Ads §17.1 calls "third-party diagnostic evidence". It remains diagnostic unless independently validated for the decision being made.

```text
PREDICTIVE SCORE
→ candidate ranking / test hypothesis
!= acceptance verdict
!= measured campaign performance
```



---

# 19. External information-dense image anti-examples

The G6 Nano Banana Pro source group provides useful external **counterexamples** because the source's own published results can fail dimensions that the accompanying marketing text presents as reliable. Preserve these as `THIRD_PARTY_METHOD_REFERENCE`, not as universal failure claims about one provider/model. `source_ref` names the captured note `higgsfield-blog_Nano-Banana-Pro-Expert-Use-Cases.md` (sha256 `c3aa54d069e5f6b78d312974e6844de196cc62fe081c392f5a10ac143388ef1a`; post `https://higgsfield.ai/blog/Nano-Banana-Pro-Expert-Use-Cases`) with the post section, prompt ID (N1–N12) and published image; literal quotes come from the validator's raw text capture `hblog/raw/Nano-Banana-Pro-Expert-Use-Cases.txt` (sha256 `7bf248cd0d698bb11dff4ada6d96fc8a38dd52dee3e62db6a954e8695390beb7`); the note is a summarized capture and holds only some of them (the prompt texts); `observed_instance` records what the published image shows, as inspected in the saved validator report `ANALISE_higgsfield-blog_nano-banana-pro.md` §7.

```yaml
- media_case_id: EXT-IMG-DECLARED-COUNT-01
  signal_origin_class: THIRD_PARTY_METHOD_REFERENCE
  hypothesis_status: UNVALIDATED
  observed_pattern: a declared repeated-item count can render with missing/extra items; in the documented failure the prompt gave the count only as a total, in one prose sentence (seven requested, six rendered)
  source_ref: "Nano-Banana-Pro-Expert-Use-Cases · section 10, prompt N12 · \"A high-resolution food photograph shows seven cuts of steak, sliced and arranged in a row\""
  observed_instance: the published image shows six cuts with six doneness labels, not seven
  counter_observation: section 4, prompt N5, also one prose sentence, states the count per row ("7 in the front row, 6 in the middle row, 7 in the back row"); the published image matches 7/6/7. One failure and one match establish no causal rule. The numbered-list prompt N11 (section 9, 50 artifacts in five numbered groups) was not counted in the saved report and is neither a match nor a failure here
  transferable_check: acceptance compares the actual output against the declared count/list rather than trusting prompt presence

- media_case_id: EXT-IMG-INFORMATION-AUTHORITY-01
  signal_origin_class: THIRD_PARTY_METHOD_REFERENCE
  hypothesis_status: UNVALIDATED
  observed_pattern: generated mathematical/technical/diagram text can look organized and readable while containing a wrong sign, duplicated/misspelled label, wrong dimension or invented source/credit
  source_ref: "Nano-Banana-Pro-Expert-Use-Cases · sections 5, 6, 6.1 and 8, prompts N6, N7, N8, N10 · \"It first computes the mathematical result internally.\" / \"perfect typographical fidelity\""
  observed_instance: boxed integral answer "−(4/3)x sin(2−3x) − (4/9)cos(2−3x) + C" (the correct cosine term is +(4/9)cos(2−3x)); F-117 labels "V-TAIL RUTTERS" and a duplicated "INTEGRATED AVIONICS BAY"; floor plan "Badroom 2" next to "Bedroom 2" and a "143m" dimension (the area rendered as a length); poster footer "© 2025 Human Systems Lab" that the prompt did not request
  transferable_check: verify informational content against authority; legibility is not factual correctness

- media_case_id: EXT-IMG-STRUCTURED-COLLISION-01
  signal_origin_class: THIRD_PARTY_METHOD_REFERENCE
  hypothesis_status: UNVALIDATED
  observed_pattern: a structured prompt can contain mutually incompatible instructions and the route resolves the collision arbitrarily
  source_ref: "Nano-Banana-Pro-Expert-Use-Cases · section 2, prompt N2 (JSON) · \"Make up a name for each characer\" vs \"empty for later name entry\""
  observed_instance: the published character-select image shows named plaques (KENJI, SARA, …)
  transferable_check: structured JSON/blocks do not replace Route Compilation collision review

- media_case_id: EXT-IMG-REFERENCE-TEXT-LEAK-01
  signal_origin_class: THIRD_PARTY_METHOD_REFERENCE
  hypothesis_status: UNVALIDATED
  observed_pattern: text visible on a source identity/reference image can leak into the generated derivative
  source_ref: "Nano-Banana-Pro-Expert-Use-Cases · section 2, prompt N2 with 10 input photos"
  observed_instance: one generated fighter carries the phrase printed on the T-shirt of its input photo (the saved report records the observation but does not quote the phrase)
  transferable_check: reference readiness includes unwanted inherited text/marks where they could contaminate the target
```

These cases do not require dedicated paid reproduction. A project execution that independently exhibits one of the patterns may support, narrow or reject the relevant hypothesis.


---

## V2.4 real-world hardening — natural trials and first-pass completeness learning

Keep a provenance-linked `first_pass_completion_rate`, `human_intervention_count`, `cost_per_approved_asset`, `critical_continuity_violation_rate`, `unexpected_reference_inheritance`, `creative_acceptance`, and `delivered_vs_promised_method_coverage` per experiment. Separate model, host, skill package, prompt and provider causes. Approved improvisation informs expressive-latitude calibration but never silently promotes source facts or canon. Historical Paris outcomes must not contaminate Berlin location authority. An unverified claimed skill load is not empirical proof of JIT read.

Treat Della and AI influencer tests as natural-user observations; P0/P1/P2 labels, rejection/approval statements and job billing evidence should each retain provenance. Do not attribute changes causally to removal of timestamps when duration/model/voice language and other factors also changed.

