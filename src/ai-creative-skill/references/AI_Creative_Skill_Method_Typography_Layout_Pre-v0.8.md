# AI Creative Skill · Specialist Method · Typography & Layout · Pre-v0.8

## Status

```text
METHOD ID = TYPOGRAPHY_LAYOUT
VERSION = Pre-v0.8
DATE = 2026-10-09
PARENT_DOCUMENT = AI_Creative_Skill_Specialist_Method_System
LAST_VALIDATED_AGAINST = AI_Creative_Skill_Specialist_Method_System_Pre-v0.10.md
STATUS = DESIGN METHOD · NOT INSTALLED
```

This method controls exact text, hierarchy, spacing, UI truth and mobile readability. Speech-derived caption timing is bound to evidence: authoritative/timestamped speech evidence supplies timing, while approved visible copy remains the text authority. Validator correction round (operator-agreed window, 2026-10-09): Pre-v0.8 returns the Remotion implementation-example sentence to the end of §4.1, where it stood in Pre-v0.6 (the Pre-v0.7 insertion of §4.2 had left it, undeclared, at the end of §4.2); adds infographic / annotated diagram / technical or data visual to the trigger; and states in §4.2 who owns label-to-target binding (this method for rendered text; Image Direction for `COMPOSITION` map labels). No other behavior changes. Pre-v0.7 adds explicit authority for factual/informational text and semantic annotation binding: a readable label, arrow or callout must map to the intended visual entity, and generated technical/mathematical/factual content does not become authority merely because it renders plausibly. Pre-v0.6 deterministic text-fit preflight and earlier authority corrections remain in force.

---

# 1. Trigger

Use when visible text or graphic hierarchy materially affects the deliverable:

```text
static ads
captions / subtitles
headlines
callouts
end cards
price / offer cards
UI-like creative
infographic / annotated diagram / technical or data visual
controlled finishing
```

---

# 2. Text Authority

Resolve:

```text
exact copy
allowed edits
required line breaks if any
language / locale
price / number formatting
physical text vs overlay text
```

Do not let generated text become authority merely because the model rendered something plausible.

`TYPOGRAPHY_LAYOUT` resolves and carries the visible/display text authority for the creative surface as `display_text_authority_ref`. The wording itself comes from the approved copy / script and Project authority; this method does not originate it. For spoken media, Audio/Voice consumes `display_text_authority_ref`; pronunciation/TTS hints may affect speech execution but do not replace visible-copy authority.


## 2.1 Informational-content authority

For information-dense graphics, visible text can carry factual content beyond ordinary copy. Examples include:

```text
formula / equation / worked step
technical specification
dimension / measurement
table cell
diagram label
footnote / source line
historical or scientific fact
product / performance datum
```

The content authority must be resolved **before** the model is asked to render the information.

```text
MODEL-RENDERED PLAUSIBLE INFORMATION
!=
FACTUAL / MATHEMATICAL / TECHNICAL AUTHORITY
```

If a visual region is reserved for dense informational text but no approved content exists, keep it empty, use clearly marked placeholder/filler that cannot be mistaken for factual authority, or supply approved content through controlled finishing. Do not invite a generative image route to invent sources, credits, calculations, specifications or institutional-looking labels merely to fill the composition.

When the informational content is materially factual, `QA_EVIDENCE_RIGHTS` remains owner of evidence/support review.

---

# 3. Hierarchy

A viewer should understand the intended order.

Typical hierarchy:

```text
PRIMARY HOOK / MESSAGE
→ PROOF / PRODUCT
→ SUPPORTING DETAIL
→ OFFER
→ CTA
```

Not every asset needs every layer.

The dominant element should match the objective rather than decorative preference.

---

# 4. Composition and Spacing

Specify:

```text
alignment
margins
safe areas
copy block width
line length
spacing between hierarchy levels
relationship to face/product/action
platform crop risk
```

Do not place copy over the evidence it is supposed to explain.

Safe areas are **resolved constraints**, not universal pixel constants. When material, resolve them from the applicable Project/Work Profile, platform/placement rules and route/output geometry. Check actual collision risk against:

```text
face / mouth
product / proof
required action
other text / graphics
platform UI / controls
known crop / placement boundaries
```

A source tool's numeric margins may be used as scoped reference/calibration only when that source/route is actually in use; they do not become generic defaults.


## 4.1 Deterministic text-fit measurement

When the selected controlled-finishing route can measure text/layout deterministically, use that capability before an expensive/full render for material copy blocks.

```text
RENDER-EQUIVALENT FONT / FONT STATE READY
→ MEASURE WITH THE SAME MATERIAL FONT PROPERTIES USED FOR RENDERING
→ COMPARE AGAINST THE RESOLVED TEXT REGION / LINE CONSTRAINTS
→ FLAG OVERFLOW / CLIPPING / UNREADABLE FIT
→ REPAIR THE SMALLEST AUTHORIZED LAYOUT SURFACE
```

Measurement should use the actual or render-equivalent font family, weight, size, letter spacing and other material properties rather than a convenient substitute. If font readiness is uncertain, the measurement is not accepted as deterministic layout evidence.

A failed fit check does **not** authorize changing exact copy. Prefer the smallest authorized adjustment among line breaks, region size/position, spacing, hierarchy-preserving type size or another controlled layout parameter. Do not auto-shrink text below the resolved readability/hierarchy requirement merely to make a box pass.

```text
TEXT-FIT MEASUREMENT
= PREFLIGHT / DIAGNOSTIC EVIDENCE
≠ FINAL ARTIFACT ACCEPTANCE
```

Route-specific APIs such as Remotion `measureText()` / `fitText()` / `fillTextBox()` are implementation examples, not provider-neutral method law.


## 4.2 Semantic annotation binding

For an annotated diagram, infographic, map-like visual, labeled product breakdown or other explanatory layout, typography quality includes **what each annotation points to**, not only whether the words are readable.

Where material, bind:

```yaml
annotation_bindings:
  - annotation_text_ref:
    target_visual_entity_ref:
    relationship:  # LABEL | CALLOUT | ARROW | LEGEND | DIMENSION | STEP | OTHER
    placement_intent:
    factual_support_ref_if_material:
```

Check that:

```text
label / callout text
→ resolves to the intended depicted entity

arrow / connector endpoint
→ lands on the intended target or target region

legend / numbered step / dimension
→ corresponds to the correct object, region or sequence
```

Readable text attached to the wrong target is a semantic layout failure. The annotation text remains subordinate to its approved text/factual authority; visually coherent generative output does not create truth.

This method owns the binding of rendered text (labels, callouts, arrows, legends) to its intended target; `IMAGE_DIRECTION` owns the labels of a `COMPOSITION` map (Image Direction §10) and region occupancy.

---

# 5. Phone-Size Readability

Review the asset at intended mobile size.

Check:

```text
headline readable without zoom
CTA distinguishable
price/terms not visually buried
subtitles do not cover mouth/product proof
contrast survives actual background
platform overlays do not destroy key copy
```

Large-editor readability is insufficient.

---

# 6. Controlled Finishing

When exact text matters and generative text fidelity is not validated:

```text
clean visual generation
→ deterministic / controlled text layer
```

Preserve accepted photography or footage when correcting copy.

---

# 7. UI Truth

A creative may use UI-like treatment only when it does not falsely imply:

```text
private message
platform notification
official alert
real dashboard state
verified account interaction
interactive button that does not exist
```

Avoid fake screenshots or false interface affordances used as proof.

---

# 8. Video Typography

For timed text:

```text
on-screen duration
entry/exit timing
speech alignment
reading speed
safe area
contrast
motion stability
```

## 8.1 Caption carrier vs emphasis

When subtitles/captions carry materially required speech, distinguish:

```text
CARRIER
= readability-first continuous/required caption surface

EMPHASIS
= optional promoted words/phrases used selectively for hierarchy or punch
```

Do not force every spoken word through a high-emphasis treatment. Required speech should remain legible even when no word is being visually promoted. Emphasis is scarce and subordinate to comprehension.

### Speech-derived caption timing evidence

When captions/subtitles materially track speech, do not estimate their final timing from word count once timestamped/authoritative speech evidence exists. Record the timing source in `caption_timing_evidence_ref`: it points to the `speech_text_evidence_ref` owned by `AUDIO_VOICE_PERFORMANCE` when the timing comes from transcript/ASR evidence, or to another explicit Project/task timing authority when it does not. This method does not define a timing schema of its own.

```text
APPROVED DISPLAY TEXT
→ owns what the viewer should read

TIMESTAMPED SPEECH EVIDENCE
→ owns when speech-derived caption windows occur
```

The transcript/timing instrument does not silently rewrite exact approved visible copy. ASR uncertainty remains governed by `AUDIO_VOICE_PERFORMANCE`; use authoritative listening where exact speech requires it.

When the route/placement requires explicit caption constraints, resolve and record only the values supported by current authority:

```yaml
caption_role:  # CARRIER | EMPHASIS
caption_timing_evidence_ref:
safe_area_ref:
max_lines_if_resolved:
line_length_target_if_resolved:
minimum_display_duration_if_resolved:
timing_tolerance_if_resolved:
collision_avoidance_targets:
line_break_policy:
```

Do not import fixed character counts, frame tolerances, pixel margins or caption gaps from an external tool as universal law.

A final CTA should have a stable hold when readability is required.

## 8.2 Cheap deterministic preflight

When a controlled finishing route can preview representative frames cheaply, inspect high-risk caption/text moments before an expensive full render. Prioritize:

```text
longest lines
line-break transitions
face / mouth / product overlap
platform-overlay regions
first / last caption
CTA hold
```

This preflight catches deterministic layout defects early. Final-artifact acceptance semantics and required review coverage are owned by `QA_REALISM_PERFORMANCE`; this section defines only the Typography-side diagnostic preflight.

---

# 9. Output

```yaml
typography_spec_id:
exact_copy:
hierarchy:
layout_regions:
safe_areas:
font_style_constraints:
text_fit_measurement_ref_if_applicable:
contrast_requirements:
physical_vs_overlay:
display_text_authority_ref:
informational_content_refs_if_applicable:
annotation_bindings_if_applicable:
pronunciation_or_tts_hint_ref:
timing_if_video:
caption_constraints_if_applicable:  # includes caption_timing_evidence_ref (§8.1)
platform_crop_notes:
acceptance_criteria:
```

---

# 10. Acceptance Rubric

Pass only if copy is exact where required, hierarchy is obvious, important text works at target size, required factual/informational content traces to the appropriate authority, material labels/callouts/arrows bind to the intended visual entities, required caption carrier text remains readable, any applicable deterministic text-fit preflight uses render-equivalent font/layout properties and resolves material overflow without unauthorized copy changes, speech-derived caption timing is bound to applicable timestamp evidence rather than word-count estimation, emphasis does not obstruct comprehension, collision/crop risks are resolved at the applicable scope, and no deceptive UI/text artifact remains.
