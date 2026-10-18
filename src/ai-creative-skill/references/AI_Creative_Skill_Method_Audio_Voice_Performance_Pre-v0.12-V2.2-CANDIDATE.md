# AI Creative Skill · Specialist Method · Audio & Voice Performance · Pre-v0.12-V2.2-CANDIDATE

## Status

```text
METHOD ID = AUDIO_VOICE_PERFORMANCE
VERSION = Pre-v0.12-V2.2-CANDIDATE
DATE = 2026-10-11
PARENT_DOCUMENT = AI_Creative_Skill_Specialist_Method_System
LAST_VALIDATED_AGAINST = AI_Creative_Skill_Specialist_Method_System_Pre-v0.12-V2.2-CANDIDATE.md
STATUS = DESIGN METHOD · NOT INSTALLED
```

Z4/Z4.1 creative-balance hardening branch (2026-10-11): Pre-v0.12-V2.2-CANDIDATE consumes task-relative creative latitude so recurring voice identity/accent/timbre can remain stable while scene-level emotion, pace, pauses, breathing, emphasis and delivery vary inside approved performance envelopes.

This method deepens the Core audio model for speech, voice identity, timing, music and SFX. It preserves canonical speech-text evidence, measured loudness discipline, measured/approved audio timing as a downstream authority for audio-led work, and music-energy alignment without fixed BPM or mix presets. Pre-v0.10 retains the articulation-driver distinction from Pre-v0.9 and adds a provider-neutral recurring-voice reproducibility profile. A locked voice is no longer represented only by a semantic authority label: material source/model/configuration state can be retained for reproducibility, while scene-level performance variation remains bounded by Project/Profile authority rather than frozen universally.

Validator correction round (operator-agreed window, 2026-10-09): Pre-v0.11 renames the §10 output field `voice_authority` to the canonical `voice_authority_ref` (same field) and declares `scene_adjustment_envelope_ref` as the canonical name of the approved contextual-variation range ("approved envelope" in prose; aliases are declared in Execution Contracts Pre-v0.16 §1.1). No audio behavior changes.

---

# 1. Trigger

Use when a deliverable contains:

```text
on-camera speech
voiceover
locked / recurring voice
exact approved audio
TTS
voice replacement
music
SFX
lipsync
```

---

# 2. Resolve Presentation and Binding Separately

Core presentation:

```text
ON_CAMERA_SPEECH
VOICEOVER
NO_SPEECH
```

Core binding:

```text
NATIVE_SPEECH
VOICE_REFERENCE
EXACT_APPROVED_AUDIO
SEPARATE_TTS
NATIVE_SPEECH_THEN_VOICE_REPLACEMENT
```

Do not collapse these into one overloaded label.

---

# 3. Voice Performance Brief

Where speech exists, define:

```text
language / locale
voice authority
tone / energy
pace
pause structure
pronunciation
emphasis
emotion / acting
speech density
duration target
exact wording requirement
```

A voice reference controls permitted voice characteristics. It does not authorize rewriting exact approved audio.

## 3.1 Actual audio timing as downstream authority

For audio-led work such as `VOICEOVER` or an approved separate TTS track, planning duration is provisional until the actual audio exists. Once the current audio/performance is accepted or otherwise authoritative, retain its measured duration and timing reference for downstream scene/edit timing.

```text
SCRIPT / WORD-COUNT ESTIMATE
= PLANNING AID

APPROVED / AUTHORITATIVE AUDIO TIMING
= DOWNSTREAM TIMING AUTHORITY FOR AUDIO-LED WORK
```

This method owns the audio timing references. It exports exactly two, and no third timing object:

```text
measured_duration_ref
= total measured duration of the accepted / authoritative audio

speech_text_evidence_ref
= the canonical speech-text evidence of §9, whose preserved time offsets supply segment-level timing
```

Where only total duration is needed, `measured_duration_ref` is sufficient. Where timestamped speech segments are needed, use `speech_text_evidence_ref`. Do not infer exact caption or cut timing from word count after authoritative audio timing exists.

Consumer methods reference these objects under their own field names and do not define a timing schema of their own:

```text
SCRIPT_PERFORMANCE / VIDEO_DIRECTION · timing_authority_ref
→ for audio-led work: measured_duration_ref and/or speech_text_evidence_ref
→ otherwise: the project/task authority that governs timing

TYPOGRAPHY_LAYOUT · caption_timing_evidence_ref
→ for speech-derived captions: speech_text_evidence_ref
```

This rule does not force every video into an audio-first workflow. Native on-camera performance, music-led edits and exact performance-transfer tasks may resolve timing differently under Project/Work/Profile authority.

---

# 4. Pronunciation and Language

Preflight:

```text
names
brands
foreign words
numbers
prices
acronyms
ambiguous spelling
regional pronunciation
```

Use pronunciation hints only in a route-appropriate form and only when they do not contaminate exact spoken wording.

Visible/display text authority is resolved and carried by `TYPOGRAPHY_LAYOUT` as `display_text_authority_ref`; the wording itself comes from the approved copy / script and Project authority. When spoken media also has visible text, consume `display_text_authority_ref`; pronunciation/TTS representation remains an audio execution aid and must not override that referenced display authority.

---

# 5. Naturalness

Review for:

```text
breathability
unnatural speed
robotic pause cadence
wrong emphasis
flat affect
excessive performance
word substitutions
language drift
```

Naturalness is contextual to persona and content type.

---

# 6. Voice Identity

For recurring/locked voice:

```text
voice identity
prosody consistency
age / perceived character fit
accent / locale
stability across parts
```

Correct speech with the wrong voice is a fail when voice is locked.

## 6.1 Recurring-voice reproducibility profile

For a recurring or locked voice, preserve enough execution state to reproduce and revalidate the approved identity without treating a provider preset name as complete authority.

```yaml
voice_reproducibility_profile_ref:
  voice_source_ref:                 # approved preset / clone / source voice / approved voice asset
  voice_route_or_model_ref:         # only when materially relevant to reproducibility
  identity_critical_settings_ref:   # settings whose change may alter perceived voice identity
  scene_adjustment_envelope_ref:    # optional approved range for contextual delivery variation; canonical name for the "approved performance envelope"
  voice_config_persistence_ref:     # saved preset/config/snapshot when available
  voice_authority_ref:
  verification_ref:
```

Rules:

```text
PROJECT / PERSONA AUTHORITY
→ decides what is locked

PROVIDER PRESET NAME
!=
SUFFICIENT REPRODUCIBILITY RECORD WHEN MATERIAL SETTINGS ALSO SHAPE THE VOICE

LOCKED VOICE
!=
FREEZE EVERY PERFORMANCE CONTROL FOR EVERY SCENE
```

Retain only settings material to the approved recurring identity/performance. Contextual pace, emphasis or affect may vary inside the approved envelope (`scene_adjustment_envelope_ref`) when that variation does not change the locked identity. A material switch of voice source, route/model or identity-critical configuration requires revalidation against `voice_authority_ref`; equivalence by provider label alone is not enough.

A cloned or real-person voice remains subject to applicable consent/rights authority; reproducibility metadata does not create permission to clone or reuse a voice. Provider-specific control names, preset counts, prices and model rankings remain Registry/Route Recipe facts, not generic method law.

---

## 6.2 Locked Voice Does Not Mean Flat Performance

Resolve voice identity and performance expression separately through the task's `creative_latitude_ref` and, when applicable, `scene_adjustment_envelope_ref`.

Typical examples, not universal locks:

```text
VOICE IDENTITY MAY PRESERVE
→ approved voice source / identity-critical configuration
→ accent / locale when canonical
→ timbre / age impression inside the approved identity band
→ protected pronunciation

PERFORMANCE MAY VARY INSIDE AUTHORITY
→ emotion / affect
→ pace
→ pause shape
→ breathing / hesitation
→ emphasis
→ sentence attack / release
→ dynamic energy
```

A recurring character should remain recognizably the same speaker without delivering every scene with identical prosody. Conversely, `be more emotional` does not authorize a different voice identity, accent or unsupported wording.

When a performance dimension is `BOUNDED_VARIATION`, respect the approved envelope. When it is `OPEN_EXPLORATION`, explore only after voice identity and script/claim authority remain satisfied. Longitudinal voice consistency should anchor to `voice_authority_ref` / the reproducibility profile, not merely to the immediately previous generated take.

---


# 7. Lipsync

Review separately:

```text
phoneme timing
mouth closure/opening
jaw integrity
teeth artifacts
speech start/end alignment
visible lag / lead
facial behavior during speech
```

Do not infer lipsync from audio correctness alone.

## 7.1 Lipsync-driving audio vs final mix

When a route uses an audio reference to drive articulation, resolve which audio component is actually authorized to control the visible mouth motion.

```text
FULL / MASTER MIX
!=
LIPSYNC-DRIVING AUDIO
```

If a composite track contains backing vocals, ad-libs, multiple speakers or other vocal layers that must **not** drive the visible subject's mouth, create or resolve a scoped `lipsync_driver_ref` containing only the intended articulating voice for that subject/segment where practical. Preserve the approved/full mix separately as `full_mix_ref` (or the current project-equivalent) for finishing/delivery.

```yaml
lipsync_driver_ref:
full_mix_ref:
articulating_subject_ref:
segment_scope_if_applicable:
```

This method owns the distinction. `TALKING_PERSONA`, `VIDEO_DIRECTION` and `ROUTE_COMPILATION` may consume these references by reference; they do not define competing lipsync-audio schemas.

The transport/container trick used by one provider workflow (for example wrapping audio inside a black video) is **not** generic method law. It belongs only in a verified Route Recipe if a selected route actually requires it.

---

# 8. Music and SFX

Music/SFX should support rather than mask:

```text
speech intelligibility
proof/action timing
brand/persona tone
platform behavior
```

Also check **energy alignment** between soundtrack and the visual/performance plan. Cut cadence, action intensity and narrative mood should not be accidentally fought by the chosen track. Do not turn source-specific BPM bands into universal law; resolve pace/energy from the creative, an approved reference or project authority.

When music choice materially affects acceptance and alternatives are cheap relative to full downstream assembly, a scoped audition/selection gate may be useful before the expensive final bake. The number of alternatives and whether human approval is required come from task/project approval policy, not from a universal three-track rule.

Important physical actions may need audible consequence when realism requires it.

## 8.1 Measured loudness / mix normalization

When loudness consistency is material, resolve the target from the applicable project/route/delivery authority or an approved reference. Do not invent one universal target.

Preferred discipline:

```text
1. RESOLVE TARGET OR REFERENCE
2. MEASURE CURRENT OUTPUT
3. COMPARE AGAINST TARGET / REFERENCE
4. APPLY THE SMALLEST NEEDED GAIN / MIX / LIMITING CHANGE
5. RE-MEASURE
6. AUTHORITATIVELY LISTEN FOR SPEECH MASKING / DISTORTION / PUMPING
7. RECORD RESULT
```

A two-pass measurement/normalization implementation may be appropriate for a deterministic audio route, but the implementation and numeric target remain route/project parameters rather than generic method law. A target already validated by current Project Profile authority is authoritative at that project scope; it is not converted into a cross-project default.

Where available, retain relevant measurements such as integrated loudness and peak/headroom indicators together with the measurement method. Relative matching to an approved reference is valid when the task does not specify an absolute delivery target.

---

# 9. Verification

Where exact speech matters:

```text
TIMESTAMPED SPEECH-TEXT EVIDENCE
+
SCRIPT COMPARISON
+
HUMAN OR AUTHORITATIVE LISTENING
```

This method is the canonical owner of `speech_text_evidence`. Create or reference the same object for audio-only sources, TTS outputs and video-derived speech. A video inspection may carry `speech_text_evidence_ref`, but video coverage and transcript provenance are not the same schema.

Canonical record:

```yaml
speech_text_evidence_id:
source_media_ref:
source_type:  # AUDIO_ONLY | VIDEO_AUDIO | TTS_OUTPUT | NATIVE_CAPTION_TRACK | OTHER
transcript_source:  # HUMAN_TRANSCRIPT | NATIVE_CAPTION | ASR
transcription_route_or_instrument:
model_or_backend_ref:
language_hint:
language_status:  # DECLARED | DETECTED_UNVERIFIED | UNKNOWN
language_eligibility:  # ELIGIBLE | INELIGIBLE | UNKNOWN
source_time_offsets_preserved:
coverage:  # FULL | PARTIAL | NONE
missing_or_failed_intervals:
transcript_or_segment_ref:
authoritative_listening_ref:
notes:
```

For any ASR used in material speech verification, use the known spoken language/locale as an explicit hint when supported and verify that the selected model/instrument supports that target language. A recognizer restricted to another language, including an English-only model used for PT-BR, is `INELIGIBLE` for material verification. Do not promote automatic language detection or silent translation into verified locale evidence.

```text
TARGET LANGUAGE UNSUPPORTED BY TRANSCRIPTION INSTRUMENT
→ INSTRUMENT INELIGIBLE
→ AUTHORIZED ELIGIBLE ROUTE
OR
STOP_REQUIRED_VERIFICATION_UNAVAILABLE
```

```text
ASR MISMATCH
→ TIMESTAMPED DIAGNOSTIC
→ FOCUSED AUTHORITATIVE LISTENING
```

ASR mismatch is diagnostic, not automatic rejection when recognition is uncertain. ASR agreement is also not proof of voice identity, naturalness or lipsync. Human/authoritative listening can reveal substitutions or pronunciation defects ASR misses.

Do not silently switch transcription provider after failure when the alternative changes privacy, cost or processing behavior.

---

# 10. Output

```yaml
audio_spec_id:
presentation_mode:
binding_contract:
voice_authority_ref:
voice_reproducibility_profile_ref:
creative_latitude_ref:
creative_risk_level:
canon_anchor_refs:
script_ref:
language:
performance_direction:
measured_duration_ref:
pronunciation_notes:
display_text_authority_ref:
music_plan:
music_energy_alignment:
sfx_plan:
loudness_target_or_reference_ref:
loudness_measurement_ref:
loudness_adjustment_plan:
post_adjustment_measurement_ref:
lipsync_requirements:
lipsync_driver_ref:
full_mix_ref:
verification_plan:
speech_text_evidence_ref:
acceptance_criteria:
```

---

# 11. Acceptance Rubric

Evaluate separately:

```text
spoken-text fidelity
voice identity
language naturalness
pronunciation
prosody / performance
performance has appropriate expressive variation without voice-identity drift or mechanical sameness when variation is authorized
intelligibility
music/SFX balance
loudness target/reference resolved and measured when material
lipsync
technical audio integrity
```
