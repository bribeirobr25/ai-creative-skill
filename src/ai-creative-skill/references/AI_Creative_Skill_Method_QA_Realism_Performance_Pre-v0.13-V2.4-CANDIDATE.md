> **V2.4 CANDIDATE SCOPE:** Modified version of this method family. Read the final section “V2.4 real-world hardening” for current candidate additions. Historical V2.3 discussion and prior-source pointers below remain provenance, not active version resolution.

# AI Creative Skill · Specialist Method · QA · Realism & Performance · Pre-v0.13-V2.4-CANDIDATE

## Status

```text
METHOD ID = QA_REALISM_PERFORMANCE
VERSION = Pre-v0.13-V2.4-CANDIDATE
DATE = 2026-10-16
PARENT_DOCUMENT = AI_Creative_Skill_Specialist_Method_System
LAST_VALIDATED_AGAINST = AI_Creative_Skill_Specialist_Method_System_Pre-v0.10.md
STATUS = DESIGN METHOD · NOT INSTALLED
```

This method performs artifact-level review of commercial clarity, realism, identity, physical behavior, typography, audio and motion. Pre-v0.12 adds provider-neutral physical-realism checks for grounded body support/weight transfer, motivated scene-light coherence and rigid environment/parallax stability. Pre-v0.11 preflight-vs-final-acceptance ownership, caption/layout checks and canonical review-issue severity remain in force.

---

# 1. Review Independence

Final creative review should be separate from the author/operator when practical and follows the canonical independence semantics in the Specialist Method System.

An `INDEPENDENT` reviewer:

```text
is not the producer / sole author of the reviewed artifact
starts from a fresh bounded review context rather than the producer's reasoning trail
receives the actual artifact + acceptance criteria + authoritative references
is not primed with a desired verdict
does not modify the artifact while forming the verdict; read-only enforcement is preferred when the runtime supports it
```

If those conditions are only partly satisfied, record `MIXED`; producer-only review is `SELF_REVIEW`; unknown provenance remains `UNKNOWN`.

---

# 2. Still Inspection Coverage

Inspect:

```text
full-resolution artifact
intended display size
important crops / placements
```

Do not pass typography or fine product details only from a thumbnail.

---

# 3. Video Inspection Coverage

Preferred acceptance coverage remains:

```text
entire final video at normal speed with audio
+
important contacts / transitions / text frame-by-frame where needed
```

When direct adequate playback is unavailable, or when a structured evidence package is useful, consume `VIDEO_EVIDENCE_INSPECTION`. Record the resulting `video_inspection_evidence_ref` and evaluate only dimensions supported by that package's canonical `coverage` object. Do not copy, rename or partially re-enumerate the video coverage fields in this method.

The instrument-capability boundary, sampled-frame limitations, transcript limitations and broad-pass → targeted-drill procedure are owned by `VIDEO_EVIDENCE_INSPECTION`. QA uses those declared limits to decide whether each quality dimension is reviewable, `UNVERIFIED`, or blocked by the applicable acceptance requirement.

A model observation may contribute evidence only with the reviewer/evidence provenance declared by the inspection package. It does not silently become independent human review or override Project/Profile requirements for authoritative listening or direct review.

## 3.1 Diagnostic Preflight vs Final Acceptance

`QA_REALISM_PERFORMANCE` owns the system-level distinction between cheap/partial preflight and final artifact acceptance.

```text
PREFLIGHT / REPRESENTATIVE PREVIEW / STATIC CHECK
= diagnostic or preventive evidence

FINAL ACCEPTANCE
= verdict on the delivered artifact under the required coverage and acceptance rubric
```

A preflight may prevent an obviously bad full render or localize a likely defect. It cannot by itself issue the final creative verdict unless the applicable acceptance contract explicitly defines that preflight artifact as the deliverable being accepted.

---

# 4. Commercial / Narrative Clarity

Check:

```text
primary message is understandable
product / subject priority is appropriate
proof is visible
motion reveals useful information
CTA / payoff is present when required
copy is specific rather than interchangeable
```

A pretty asset with weak meaning can fail.

---

# 5. People / Identity

Check:

```text
identity / age / defining features
face / eyes
hands / fingers
body proportions
posture / balance
gaze
wardrobe continuity
performance behavior
```

Common failure signals include dead eyes, constant smile, random eyebrow motion, unmotivated gestures, head bobbing and posture changes unrelated to the action.

## 5.1 Grounded body mechanics

When locomotion, standing, landing, lifting or another body-weight event is material, inspect the visible support chain rather than accepting motion merely because each frame looks plausible.

```text
support / footfall / grip is physically established
→ center-of-mass / weight transfer follows the action
→ limbs / body respond to force, terrain and contact
→ recovery / settle follows acceleration, impact or landing where applicable
```

Do not require exaggerated body mechanics. The criterion is physical coherence relative to the intended action. Sliding feet, floating support, weight that never transfers or a landing with no corresponding body response are observable defects when the scene calls for grounded motion.

---

# 6. Product / Object / Physics

Check:

```text
product geometry
labels / hardware / seams
materials
object support
contact shadow
hand-object contact
weight / force response
liquid / fabric / reflection behavior
spatial consistency
```

Objects should not float, teleport or respond before contact.

## 6.1 Scene / environment physical coherence

When the acceptance target includes physically plausible scene lighting or rigid environment behavior, check:

```text
motivated scene-light logic
light direction / relative intensity / shadow / occlusion / falloff coherence
no unexplained duplicate source, flicker or time-of-day jump when continuity is required
rigid environment geometry / parallax stability
background-state stability through camera or subject motion
```

A light source does not need to be visible in frame. It may be off-camera, environmental or otherwise inferable from the declared scene. The requirement is that illumination behaves coherently with the authorized lighting logic. Stylized or intentionally nonphysical lighting is valid when that is the declared creative target.

Rigid architecture, furniture, vehicles, hardware or similar structures should show plausible parallax and occlusion under motion rather than unexplained warping, melting, scale drift, sliding or topology changes.

These checks name observable defects. They do not infer which model, prompt or setting caused them.

---

# 7. Design / Text

Check:

```text
hierarchy
mobile readability
exact copy
line breaks
price / quantity
contrast
safe areas
accidental text / logo
false UI
```

## 7.1 Caption / subtitle layout checks

When timed captions/subtitles are present, consume the applicable `TYPOGRAPHY_LAYOUT` spec rather than defining a second caption schema. Check the rendered result for:

```text
clipping / overflow
face / mouth occlusion
product / proof occlusion
text-on-text or graphic collision
reading order / hierarchy
platform overlay / crop risk
contrast at intended display size
caption timing / hold long enough to read under the resolved spec
```

A cheap representative-frame preview may catch deterministic text/layout errors before full render. Apply the canonical preflight-vs-final-acceptance rule in §3.1; final acceptance still requires the delivered artifact and adequate motion/audio/text coverage for the dimensions being judged.

---

## 7.2 Text / copy naturalness diagnostic

When delivered copy, subtitles, captions or visible text are in scope, a reviewer may flag generic model-writing behavior only with an observable description.

When a material text issue is found, create or reference the canonical text finding owned by `SCRIPT_PERFORMANCE`:

```yaml
text_finding_ref:
```

Do not re-declare the text-finding fields here. The referenced finding carries issue class, quoted span, evidence strength, reader/canon context, consequence and smallest repair.

Examples of useful diagnoses:

```text
chatbot offer remains in the final caption
closer repeats the previous sentence without adding information
reply spends three sentences restating context supplied by the audience
“experts say” is used without traceable support
```

Do not fail an asset because a single `CONTEXTUAL_SIGNAL` appears. Canonical persona voice, deliberate rhetoric and the content objective can justify patterns that a generic checklist would otherwise flag. Full text-naturalness procedure lives in `Script & Performance`.

Text-pattern evidence may support a writing-quality finding. It may **not** support a claim that AI authored the text. This is a rule, not a defect-record field. If provenance/authorship matters, use actual provenance evidence; do not substitute stylistic detection.

For a bounded text audit, prefer a named finding + exact quoted span + consequence + smallest fix over a score or global label.

---

# 8. Motion / Audio

Check:

```text
opening pays off
action completes
camera serves the action
continuity
speech intelligibility
spoken-text fidelity
voice identity
lipsync
caption sync
music / SFX balance
CTA hold
```

---

# 9. Defect Record

For every material issue record:

```yaml
artifact:
video_inspection_evidence_ref:
region_or_timestamp:
defect:
consequence:
severity:  # BLOCKER | REPAIR_REQUIRED | NOTE
likely_surface:
smallest_repair:
text_finding_ref:
```

"Looks AI" is not a sufficient diagnosis.


Canonical review-issue severity:

```text
BLOCKER
=
the artifact cannot be accepted/delivered in the current state because a required criterion, authority, verification or safety/evidence condition is materially violated

REPAIR_REQUIRED
=
an acceptance criterion fails, but a bounded repair is available or can be planned within authority

NOTE
=
a non-blocking observation that does not by itself require repair, regeneration or rejection
```

Severity describes consequence for the current acceptance decision, not aesthetic intensity. A `NOTE` must not silently become authorization to spend on another attempt.

---

# 10. Verdict

```text
ACCEPTED
REPAIR
BLOCKED
UNVERIFIED
```

No dimension passes because the prompt requested it.

---

# 11. Real-Use Tests

Where relevant perform:

```text
thumbnail test
first-frame test
1-second comprehension
muted test
phone-size test
crop/safe-area test
audio-on test
```

---

# 12. Pairwise Selection

When several outputs pass basic QA, pairwise comparison may be used to select the strongest objective fit under the same rubric.

Prefer concrete comparative reasons over undifferentiated numerical beauty scores.


---

## V2.4 real-world hardening — two-level QA and scene evidence

Run P0 hard/factual/physical invariants separately from P1 craft/continuity and P2 human editorial preferences. Review actual output at appropriate temporal and audio coverage; an ASR transcript proves words only to its accuracy, not human timbre, lip-sync or audio preservation. Object hidden behind a person/out of view is `OFFSCREEN_UNVERIFIED` rather than `CONFIRMED_ABSENT`. Inspect causal hand/phone/zipper/bag/plate transfers and continuity of beverage/food counts. Do not confuse user-approved, provider-COMPLETED, QA-PASS, master HD and PUBLISHED.

A P2 imperfection must not trigger automatic regeneration of a user-approved film. Preservation failures in localized edit are hard failures. Scope findings with timestamp/evidence and avoid treating camera-improvisation differences as defects absent protected authority.

