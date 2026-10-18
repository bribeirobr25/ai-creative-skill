> **V2.4 CANDIDATE SCOPE:** Modified version of this method family. Read the final section “V2.4 real-world hardening” for current candidate additions. Historical V2.3 discussion and prior-source pointers below remain provenance, not active version resolution.

# AI Creative Skill · Specialist Method · Talking Persona · Pre-v0.7-V2.4-CANDIDATE

## Status

```text
METHOD ID = TALKING_PERSONA
VERSION = Pre-v0.7-V2.4-CANDIDATE
DATE = 2026-10-16
PARENT_DOCUMENT = AI_Creative_Skill_Specialist_Method_System
LAST_VALIDATED_AGAINST = AI_Creative_Skill_Specialist_Method_System_Pre-v0.10.md
STATUS = DESIGN METHOD · NOT INSTALLED
```

This cross-cutting method is for recurring AI personas speaking on camera. It generalizes validated project lessons without copying project-specific identities or voice locks into the generic method. Validator correction round (operator-agreed window, 2026-10-09): Pre-v0.6 renames the brief fields `identity_authority` → `identity_authority_ref` and `voice_authority` → `voice_authority_ref` (canonical names; the old names are accepted aliases). No other behavior changes. Pre-v0.5 retains the authority-bounded acting-task structure from Pre-v0.4 and deepens cross-modal speech-performance coherence, route-appropriate articulation readiness and speech-beat anchoring without imposing one universal mouth pose or gesture cadence.

---

# 1. Trigger

Use when all are true:

```text
recurring persona
+ visible speaking performance
+ identity / behavioral continuity matters
```

Project Profile remains authority for identity, voice, environment, disclosure and route locks.

---

# 2. Required Layers

Resolve independently:

```text
VISUAL IDENTITY
BEHAVIORAL VOICE
SPOKEN TEXT
VOICE IDENTITY
LIPSYNC
PERFORMANCE
ENVIRONMENT / CONTINUITY
```

A clip may pass one dimension and fail another.

---

# 3. Talking Persona Brief

```yaml
persona_ref:
identity_authority_ref:
voice_authority_ref:
behavioral_voice_ref:
environment_ref:
script_ref:
presentation_mode:
audio_binding_contract:
speech_text_evidence_ref:
acting_task:
  scene_purpose:
  motive_ref_or_supported_motive:
  goal:
  obstacle_or_pressure:
  tactic:
  beat_actions:
signature_behavior_plan:
camera:
start_frame_ref:
continuity_requirements:
text_graphics_mode:
acceptance_criteria:
```

Do not invent a recurring voice when Project Profile authority is missing.

---

# 4. Canonical Exemplars

Use a small curated set of approved persona scripts/media to calibrate:

```text
vocabulary
sentence rhythm
energy
humor / seriousness
facial restraint / expressiveness
audience relationship
```

Exemplars inform style. They do not replace canonical identity or script authority.

---

# 5. Start-Frame Readiness

A talking start frame should support:

```text
recognizable identity
usable face angle
visible mouth / jaw
appropriate crop
clean reference state
route-appropriate articulation readiness
no accidental text/logo contamination when prohibited
```

`route-appropriate articulation readiness` means the visible mouth/jaw/source state should be compatible with the first intended articulation and selected talking/lipsync route. It does **not** impose `lips closed` as universal law. Some routes or tasks may benefit from a neutral/closed start; others may support a mild natural expression. Route evidence and current Project authority decide the executable requirement.

When multipart continuity needs a clean end-state anchor, the requested end pose may deliberately settle into a reusable state. That is a continuity tactic, not a mandatory final facial pose for every talking clip.

A technical derivative remains linked to canonical identity and does not silently become a new hero image.

---

# 6. Speech / Performance Separation

Treat:

```text
WHAT IS SAID
HOW IT SOUNDS
HOW THE FACE / BODY PERFORMS IT
```

as separate controls.

Exact speech does not guarantee voice identity. Correct voice does not guarantee lip-sync. Good lip-sync does not guarantee natural eye/face behavior.

## 6.1 Cross-modal speech-performance coherence

Review the speaking performance as one coordinated result across already-separated authorities:

```text
SPOKEN MEANING / BEAT
↔ VOICE AFFECT / PROSODY
↔ FACIAL AFFECT
↔ EYE / GAZE BEHAVIOR
↔ HEAD / BODY / GESTURE RESPONSE
```

A clip can have technically correct phoneme sync and still fail when the audible delivery and visible performance contradict one another, remain mechanically flat or change emotion at unrelated moments.

Check, when material:

```text
emotion / intent transition occurs at the relevant speech beat
face and gaze support rather than contradict the audible delivery
head / body / gesture response serves meaning rather than filling time
continuous playback is reviewed; isolated frames alone do not establish performance coherence
```

Consume `AUDIO_VOICE_PERFORMANCE` bindings by reference. When a particular audio layer drives articulation, use the owned `lipsync_driver_ref`, `articulating_subject_ref` and applicable segment scope rather than inventing a second mouth-driving schema here.

---

# 7. Acting Discipline

Prefer restrained, motivated actions for direct-to-camera performance unless the persona or script requires more. Observable actions remain reviewable, but for a character-led performance they may be the **channel of an acting task**, not the whole task.

When useful, resolve only the layers supported by current persona/script authority:

```text
SCENE PURPOSE
→ what this shot must accomplish

MOTIVE
→ why the persona is doing it, only when canonically supported

GOAL
→ what the persona is trying to obtain/change in the moment

OBSTACLE / PRESSURE
→ what makes the moment non-neutral, when relevant

TACTIC
→ what the persona is doing toward the viewer/partner to pursue the goal

BEAT ACTIONS
→ observable gaze / hand / posture / pause / interaction choices that express the task
```

Do not invent backstory, motive, desire or relationship merely to make an acting brief sound sophisticated. A simple direct-address clip may need only scene purpose, goal/tactic and a few observable beat actions.

Useful observable directions include:

```text
when to look at camera
when to glance away / at object
small facial reactions
hand use
posture changes
pause points
end pose
```

Avoid constant smiling, random gestures, head bobbing, excessive blinking and movement unrelated to speech meaning.

For audio-led performance, when authoritative timestamped speech evidence exists, important gestures/reactions may be anchored to the relevant word, phrase or speech beat through `speech_text_evidence_ref` rather than an invented wall-clock guess. Use only the beats that materially improve performance control; no fixed gesture interval is generic law.

If the persona has a canonical signature gesture/behavior, use it only when motivated or useful to the beat. Repetition frequency is not identity fidelity. Overusing a signature behavior can turn a recognizable trait into a mechanical tic.

```text
CANONICAL SIGNATURE BEHAVIOR
!=
MANDATORY BEHAVIOR IN EVERY CLIP / LINE
```

---

# 8. Duration and Multipart

Use route/project duration limits.

If splitting is required:

```text
PART 1
→ generate / bind audio / verify / accept
→ derive allowed continuity anchor
→ PART 2
```

Do not generate dependent later parts from an unaccepted earlier state.

---

# 9. Speech Verification

When exact or materially important speech is required:

```text
returned audio / video
→ AUDIO_VOICE_PERFORMANCE creates or resolves canonical `speech_text_evidence_ref`
→ VIDEO_EVIDENCE_INSPECTION only when structured video-specific coverage is needed
→ script comparison against the referenced speech-text evidence
→ human listening or equivalent authoritative review
→ creative acceptance
```

Preserve `speech_text_evidence_ref`; the referenced Audio & Voice record owns transcript source, language status, coverage and missing intervals. A mismatch should point the reviewer to the affected source timestamp instead of triggering a provider/model switch or full regeneration by default.

ASR is diagnostic support, not final truth for naturalness, exact meaning, voice identity or lipsync. Sampled frames plus ASR do not establish lipsync; that dimension requires adequate continuous audio/video review.

---

# 10. Progressive Fidelity

When project/route supports it:

```text
low-cost performance validation
→ acceptance
→ preserve same performance
→ upscale / finish
→ final-resolution review
```

Do not regenerate an accepted performance merely to fix resolution, color or a controlled text layer when those can be repaired downstream.

---

# 11. Scorecard

Typical high-priority dimensions:

```text
identity fidelity
language naturalness
spoken-text fidelity
voice-identity fidelity
lip-sync
mouth / teeth / jaw integrity
eye / face behavior
performance naturalness
cross-modal voice / face / gaze / body coherence
acting motive/goal/tactic does not invent persona canon
signature behavior remains intentional rather than mechanically repeated
reproducibility
```

Cinematic flourish is secondary when it conflicts with identity or speech correctness.

---

# 12. Failure Preflight

Before submission, check applicable experience memory for known issues such as:

```text
duplicate dialogue instructions
reference contamination
wrong-language tendency
voice replacement timing risk
identity drift at specific framing
multipart continuity failure
```

Only use documented/observed route-specific failures as hard mitigations.

---

# 13. Acceptance

A talking-persona output is accepted only when required dimensions are actually reviewed at adequate coverage.

A strong clip that looks like a different persona or speaks with the wrong locked voice is not accepted.


---

## V2.4 real-world hardening — character design vs talking performance

Creation of a complete Character Bible is a pre-production deliverable owned by the requesting Work Profile's identity/script/image composition. This `TALKING_PERSONA` specialist triggers **only** when a recurring character visibly speaks and performance/lipsync matters; it does not seize ownership for a name-only request or static portrait. When active, consume the approved Bible and ensure vocal timbre, PT-BR pronunciation when needed, articulation, facial behavior, performance and continuity have separate acceptance checks. A proposed voice description is not approval of voice audio or lipsync.

