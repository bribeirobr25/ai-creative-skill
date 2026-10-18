> **V2.4 CANDIDATE SCOPE:** Modified version of this method family. Read the final section “V2.4 real-world hardening” for current candidate additions. Historical V2.3 discussion and prior-source pointers below remain provenance, not active version resolution.

# AI Creative Skill · Specialist Method · Video Direction · Pre-v0.13-V2.4-CANDIDATE

## Status

```text
METHOD ID = VIDEO_DIRECTION
VERSION = Pre-v0.13-V2.4-CANDIDATE
DATE = 2026-10-16
PARENT_DOCUMENT = AI_Creative_Skill_Specialist_Method_System
LAST_VALIDATED_AGAINST = AI_Creative_Skill_Specialist_Method_System_Pre-v0.12-V2.2-CANDIDATE.md
STATUS = DESIGN METHOD · NOT INSTALLED
```

Z4/Z4.1 creative-balance hardening branch (2026-10-11): Pre-v0.11-V2.2-CANDIDATE consumes task-relative creative latitude, canon anchoring and user-scoped preserve/explore directives so continuity can remain stable without collapsing multi-shot work into repeated camera/performance patterns.

E4 empirical-hardening branch (2026-10-11): Pre-v0.12-V2.2.1-CANDIDATE adds one narrow observability-by-design rule for material temporal state. If a state/invariant must later be verified, the shot/beat plan provides enough observable evidence at the relevant review window; hidden state is not silently treated as preserved. Existing creative-latitude, camera and expression/identity semantics are unchanged.

This method turns creative intent into physically credible, reviewable motion units before route compilation. Validator correction round (operator-agreed window, 2026-10-09): Pre-v0.10 renames the temporal-invariant type `BOUNDED_WINDOW` to `WINDOW_SCOPED_EXISTENCE` so it no longer collides with the `BOUNDED_WINDOWS` timing-precision level; merges the former `authoritative_dimensions` into `protected_dimensions` and declares the preserve/change correspondence with Localized Repair §6 and the transition seam; routes source media containing a real person through QA Evidence & Rights §5 / §5.2 before transformation; and renames `blocking_plan_ref` to the canonical `composition_ref` (`COMPOSITION` reference role, Image Direction §10). No other behavior changes. Pre-v0.9 adds explicit temporal-invariant semantics for one-way state, single-occurrence events and bounded windows, plus a source-media authority contract for source-led transformation or performance-transfer work. Pre-v0.8 shot planning, task-relative timing precision, world-space blocking, per-angle background continuity, transition seams and physical-camera-versus-optical-change distinctions remain in force.

---

# 1. Trigger

Use for generated or materially edited motion:

```text
video ads
organic short-form
B-roll
product demonstrations
story scenes
talking performance where body/camera action matters
multi-shot continuity
```

---

# 2. Choose the Right Motion Problem

Before writing a motion prompt, classify the job:

```text
simple text-to-video
reference-led motion
talking / lipsync
exact performance transfer
first/last-frame control
localized edit
reframe / relight / grade
```

A generic video model should not be forced to imitate a specialized workflow when a validated specialized route exists.

---

# 3. Useful Change

Every motion unit should create useful change:

```text
new information
physical demonstration
emotional/performance progression
revealed evidence
narrative consequence
```

A drifting camera over an unchanged idea is not automatically meaningful motion.

## 3.1 Previsualization and shot-plan bridge

For multi-shot, spatially complex or expensive motion work, resolve the visual plan before final motion generation:

```text
SCRIPT / BEAT INTENT
→ WRITTEN SHOT PLAN
→ OPTIONAL STORYBOARD / CONTROL FRAME
→ REVIEW / LOCK
→ MOTION SPEC
```

The shot plan is a decision surface, not a second creative authority. It should make each material beat recoverable through fields such as:

```text
shot / beat purpose
viewer information gained
framing / camera intent
subject action
blocking / spatial relationship
reference needs
continuity in / continuity out
transition intent
timing precision needed
```

A storyboard or control frame is optional. Use it when static review can cheaply resolve composition, geography, reference readiness or continuity before motion spend. A planning/control frame may be omitted from the final edit; its value can be purely diagnostic or spatial.

An accepted storyboard/control frame becomes a motion reference only when Project/reference authority permits it. It supplements, rather than silently replacing, canonical identity/product/environment authorities.

Do not require a storyboard for a simple one-shot job whose composition and continuity are already unambiguous.

---

## 3.2 Motion Continuity vs Expressive Variation

Use the cross-method `creative_latitude_ref` to decide what must remain stable and what can change across shots/scenes/episodes.

```text
CONTINUITY
→ preserves dimensions that carry the current identity, world, action history or seam contract

EXPRESSION
→ may vary camera, blocking, performance, focus, lighting, transition or concept only when those dimensions remain open
```

Do not hardcode a modality-wide rule that camera or lighting must always vary. An intentional locked shot or stable lighting state can be correct. Conversely, repeated framing/movement/performance across open dimensions can be mode collapse rather than stronger continuity.

For longitudinal sequences, resolve stable character/world state from canonical/approved authority plus the accepted continuity state that actually changed during the story. Do not let derivative-to-derivative drift redefine identity, environment geometry or persona merely because each preceding shot was accepted for another purpose.

An explicit user instruction such as `keep the environment and character exactly consistent but make the camera language much more inventive` should preserve the first dimensions and open the second. The instruction does not authorize unrelated changes.

---


# 4. Complexity Budget

Count independent actions **and** other independently tracked burdens that materially compete for temporal/spatial consistency. Relevant burdens may include:

```text
independent actions / beats
independently tracked people or identities
speakers whose mouth state must remain attributable
simultaneous contacts / handoffs / collisions
background actions that must remain controlled
material camera-side / spatial relationship changes
```

Do not convert this into a universal maximum-person rule. The purpose is to identify when one generation has too many coupled states to review and preserve reliably.

If a short clip asks one generation to:

```text
walk
open bag
remove item
turn to camera
speak
change camera side
hand item to another person
```

consider splitting it.

Default principle:

```text
ONE CONTROLLABLE UNIT
→ REVIEW
→ NEXT DEPENDENT UNIT
```

Combine actions only when the route has evidence it can perform them reliably and the timing is physically plausible.

---

# 5. Timed Beat Table

For each beat define:

```text
time range / event-time budget
commercial / narrative job
framing
start state
acting task
action
hand / contact state when interaction-critical
contact / cause
physical consequence
lighting source / state when material to the beat
camera behavior
screen direction / relationship axis when material
background action when material
transition / cut intent when material
viewer information gained
end state
copy / audio
```

The last state of one dependent shot must provide the required start state of the next.

For generative motion, a prompt/stage time range is normally an **event-time budget**, not a promise that the visible event will land on a frame-accurate edit boundary. Use tighter timing only when the task/route has an authoritative timing constraint. Deterministic edit points must come from measured/project/route authority, not from the mere presence of a timestamp in a generative prompt.

For audio-led work, when Audio/Voice supplies an accepted/authoritative timing reference, reconcile the beat table to that real timing rather than preserving an earlier word-count or script estimate. Record the timing authority used in `timing_authority_ref`: for audio-led work it points to the references owned by `AUDIO_VOICE_PERFORMANCE` (`measured_duration_ref` for total duration, `speech_text_evidence_ref` when segment-level timing is needed); otherwise it points to the project/task authority that governs timing.

Choose the **least timing precision that still protects the job**:

```text
CONTINUOUS_UNIT
→ one continuous action/performance; no internal edit points required

ORDERED_BEATS
→ order matters; exact timestamps do not

BOUNDED_WINDOWS
→ each beat/speech event has an authoritative or production-useful time window

DETERMINISTIC_EDIT_POINTS
→ exact cut/sync points are required and supported by measured/project/route authority
```

Do not escalate to exact-timestamp syntax merely because a provider accepts timestamps. Precision is justified by the edit/performance contract, not by vendor prompt fashion.

For a material transition between dependent beats/shots, define a **transition seam contract**:

```text
outgoing trigger / state
→ dimensions that must persist across the seam
→ dimensions explicitly allowed to change
→ incoming start state
→ audio relationship when material
```

The seam uses the same preserve/change correspondence as source-media authority (§9.2): dimensions that must persist = `protected_dimensions` (PRESERVE); dimensions explicitly allowed to change = `allowed_changes` (VARY / FIX); any other change = FORBIDDEN CHANGE (Localized Repair §6).

Hard cut, match-on-action, full-occlusion cut and foreground wipe are optional tactics that may realize this contract. They are not mandatory styles, and route-specific reliability claims remain calibration/recipe evidence.

---

# 6. Cause → Contact → Consequence

Physical interaction should read as:

```text
APPROACH / CAUSE
→ CONTACT
→ FORCE / WEIGHT / RESPONSE
→ CONSEQUENCE
→ RECOVERY / END STATE
```

Do not skip contact and then show the result magically.

For an interaction-critical hand, specify only the state needed to make the physical relationship reviewable:

```text
which hand / limb
→ what it supports, holds or touches
→ grip / contact / separation state that matters
→ start state
→ end state
```

Do not inventory every finger merely for verbosity. Finger-level placement is warranted only when the shot, product interaction, proof requirement or known failure actually depends on it. An irrelevant hand may be kept still, occluded or outside the critical action rather than over-specified.

---

# 7. Acting Tasks

Avoid vague instructions such as:

```text
look confident
act natural
be charismatic
```

Use observable tasks:

```text
glance at product
return gaze to camera
half-smile
raise one eyebrow slightly
lift product after grip is established
pause before final line
```

For recurring persona work, `TALKING_PERSONA` may supply a structured acting task (scene purpose, canonically supported motive, goal, obstacle/pressure, tactic and beat actions). Video Direction consumes that task and turns it into visible timing/action; it does not invent persona motive or backstory. Observable micro-actions are channels for the task, not compulsory emotion-result tricks.

Maintain persona-specific behavior from Project Profile/canon.

---

# 8. Camera Discipline

Camera movement must serve a communication or physical purpose.

```text
CAMERA MOVEMENT
→ reveal / follow / clarify / create intended energy
```

A named camera technique is not sufficient by itself. When a term could be ambiguous, resolve it into the observable behavior that matters:

```text
NAMED TECHNIQUE
→ subject / target
→ observable movement, focus or framing change
→ start state / end state where material
→ speed / energy where material
```

For example, the useful part of a focus-shift instruction is which plane/subject begins in focus and which one ends in focus, not merely the technique label. A controlled vocabulary may be used as a repertoire, but it is not an obligation to add camera movement.

When the distinction is material to the intended shot, separate **camera-body movement** from **optical change**:

```text
camera translates / changes world position
≠
camera rotates from a fixed world position
≠
lens / focal / focus state changes while camera position remains fixed
```

A dolly/truck/orbit-like instruction therefore should not silently compile into an optical zoom, and an optical zoom should not imply world-space camera travel. Describe the observable start/end relationship that matters; do not import fixed FOV tables, lens brands or provider-specific movement presets as generic law.

If movement hides proof, breaks continuity or competes with the action, simplify it.

For short controlled scenes, one purposeful movement is often stronger than multiple decorative moves.

For multi-subject or spatially dependent sequences, preserve screen direction and a relationship/action axis when they are needed for viewer orientation or contact continuity. Crossing an axis is allowed when deliberate and legible; the method does not impose a universal 180-degree rule on every scene.

## 8.1 Intentional adjacent-shot variation

In multi-shot short-form, review consecutive motion units for accidental visual repetition. If two adjacent units have effectively the same framing, scale, camera side, motion pattern, environment treatment and information density without a deliberate reason, the sequence can read like a repeated generation loop rather than progression.

Variation can come from framing, scale, camera side, subject/action, environment, information density or motion pattern. It is subordinate to the communication job and continuity:

```text
INTENTIONAL STABLE FRAMING
≠
DEFECT

ACCIDENTAL REPETITION WITH NO NEW FUNCTION
→ REVISE / MERGE / RE-DIRECT
```

Do not force a new camera mode merely to create novelty.

For intentionally rapid cuts, a stable **visual anchor** may be preserved across adjacent units when it helps the viewer keep spatial/gaze orientation. This was promoted during the Seedance report cross-check from the independently inspected companion transcript; it is an optional continuity aid, not a fixed editing style.

## 8.2 Capture apparatus / native-camera realism

When the content/presentation mode intentionally imitates self-shot, casual or social-native capture, define a plausible capture apparatus before adding camera imperfections:

```yaml
capture_apparatus_plan:
  device_or_capture_class:
  operator_or_support:
  intended_stability:
  motivated_physical_behavior:
  forbidden_artifacts_if_material:
```

Examples of motivated behavior may include a brief placement settle, restrained handheld micro-sway or vehicle vibration **only when the chosen apparatus/context would physically produce it**. Stable support or tripod-like framing is valid when the creative actually calls for it.

```text
NATIVE / CASUAL CAPTURE
!=
ALWAYS SHAKE THE CAMERA
```

Do not add random shake, blur, grain, focus pumping or exposure breathing merely as an “AI realism” filter. The capture behavior should be bounded, physically motivated and subordinate to readability, identity and action.

---

## 8.3 Controlled Variant Family Consumption

When `CALIBRATION_AND_EXPERIENCE_MEMORY` supplies a `variant_family_ref`, consume its declared preserve/vary sets rather than improvising a different camera or motion plan for every variant.

```text
DECLARED CONTROLLED FAMILY
→ preserve the specified invariant motion / camera / structure
→ vary only the declared dimensions unless a material feasibility issue requires replanning
→ review every output independently
```

A repeated camera/motion specification across **separate variants** can be intentional because it isolates subject/product/environment or another changed variable. This is distinct from accidental repetition **inside one sequence**, which remains governed by §8.1.

If the supposedly invariant motion becomes unsuitable for a changed subject, geometry, action or proof requirement, do not force the invariant blindly. Record the divergence and preserve the comparison meaning where possible.

---

# 9. Continuity State

Track where relevant:

```text
character position
physical/world-space station or seat when material
screen-space position when material
fixed environment landmark relationship
visible background for the current camera angle
body orientation
gaze
hand occupancy
product position / orientation
prop state
wardrobe state
lighting direction
lighting_state_within_unit
motivated_light_source_state when material
camera side
screen direction / relationship-axis side when material
background state / background action when material
```

For multi-subject scenes, distinguish **physical placement in the world** from **where the subject appears in the frame**. A person can remain in the same physical seat/station while moving from screen-left to screen-right after the camera changes sides.

When geography matters:

```text
WORLD / SET GEOMETRY
→ fixed seats/stations + fixed landmarks + movement paths
→ current camera position/side
→ visible background for this shot
→ resulting screen-space composition
```

Do not move doors, windows, furniture or other fixed architecture merely to keep the same landmark behind the same person through a reverse angle. Describe the background visible from the current camera angle while preserving world geometry.

Possessing a prop or performing an action does not, by itself, define the subject's spatial station. If exact placement matters, specify it or bind an approved `COMPOSITION` reference (`composition_ref`).

A prop/object that will be manipulated should already exist in a coherent start state unless its appearance/disappearance is itself an explicit scene event. Preserve its identity/geometry through the interaction rather than letting it pop in, vanish or redesign itself between beats.

For reference-led character motion, identity-reference lighting is not scene-lighting authority by default. Resolve the subject's lighting from the target environment / Project authority when those contexts differ, including physically plausible contact/shadow/local-color response. When the shot is supposed to occur under stable lighting, treat unintended light/time-of-day drift inside the motion unit as a continuity failure rather than a cinematic flourish.

When a material light source moves or changes within a unit, the illumination state should change **because of that source event**: the lit side, shadow placement, relative intensity and falloff should respond coherently. When the source is stable, do not invent flicker, duplicate sources or unmotivated lighting changes. This is scene-physics direction, not a requirement that every light source appear on camera.

```text
END STATE N
=
REQUIRED START STATE N+1
```

A clean anchor/reference may be derived from an accepted prior state when the Project Profile permits it.

## 9.1 Temporal invariants when state/event direction matters

Some continuity requirements are not merely “keep this state.” They constrain **how state is allowed to evolve over time**.

Use a temporal invariant only when the production actually needs one:

```yaml
temporal_invariants:
  - subject_or_state_ref:
    invariant_type: IRREVERSIBLE_OR_MONOTONIC | SINGLE_OCCURRENCE | WINDOW_SCOPED_EXISTENCE
    starts_at_or_after:
    ends_at_or_before:
    allowed_progression:
    forbidden_reset_or_repeat:
```

Interpretation:

```text
IRREVERSIBLE_OR_MONOTONIC
→ a material state moves in one declared direction once activated
→ examples: wetness accumulates; damage remains; an object that is consumed does not regrow

SINGLE_OCCURRENCE
→ a material event occurs once in its authorized beat/window
→ it does not spontaneously repeat elsewhere

WINDOW_SCOPED_EXISTENCE
→ a material state/event may exist only inside its declared window
→ outside the window, it is absent unless a later authority explicitly reactivates it
```

`WINDOW_SCOPED_EXISTENCE` is an invariant type. It is distinct from `BOUNDED_WINDOWS` in §5, which is a timing-precision level.

Do not manufacture temporal locks for decorative details that do not matter. The purpose is to prevent silent resets, repetitions or state resurrection when those would break the intended action/history.

Temporal invariants remain subject to the normal authority hierarchy. A generated take that accidentally changes state does not redefine the contract.

## 9.2 Source-media authority for source-led work

When the job transforms, extends or transfers from an existing source clip, resolve **which dimensions of that source are authoritative** before directing the change.

If the source media contains a real person, resolve consent, origin and intended-use authority under QA Evidence & Rights §5 / §5.2 before directing any transformation, extension or performance transfer.

```yaml
source_media_authority:
  source_ref:
  protected_dimensions:
  allowed_changes:
  required_new_interactions:
  end_state_requirements:
```

`protected_dimensions` are the source dimensions that are authoritative for this job and must remain source-faithful; the former `authoritative_dimensions` field is merged into it and is read as an alias. Correspondence with Localized Repair §6: `protected_dimensions` = PRESERVE; `allowed_changes` = VARY / FIX; any change not declared in `allowed_changes` = FORBIDDEN CHANGE.

Possible protected dimensions include, only when actually required:

```text
camera path / framing
subject motion or performance timing
scene geometry
focus behavior
lighting / color relationship
background
duration / editorial timing
accepted physical contact or motion state
```

This is **not** a universal freeze of the source clip. Preserve only the dimensions the task/project actually authorizes as source truth, and state the permitted change separately.

If the requested addition changes physical contact, occlusion, shadows, reflections or scene occupancy, the new interaction must be coherent with the protected source dimensions rather than pasted over them as an unrelated layer.

The route-specific mechanics for expressing source-media authority belong to Route Compilation / Route Recipe.

---

## 9.3 Observability of material temporal state

When a material temporal state or invariant must later be verified, the shot/beat plan should provide sufficient visual evidence at the review window where that assertion matters.

```text
VERIFIABLE MATERIAL STATE REQUIREMENT
→ PLAN SUFFICIENT OBSERVABLE EVIDENCE
```

This does not require every protected object to remain visible continuously. It requires enough visibility to inspect the state being claimed. If the selected framing, occlusion or action makes the material state unobservable, review must leave that assertion `UNVERIFIED / REVIEW` rather than infer preservation from silence.

Examples include a phone required to remain face down, a package required to remain sealed, or a prop whose material state is supposed to persist across a beat.

---

# 10. First Frame and CTA Hold

The first frame should already support the intended opening when the route permits.

For commercial CTA/end-card moments, provide a stable readable hold where required rather than forcing important copy through unstable motion.

---

# 11. Audio and Speech

Speech, music, SFX and voice identity are separate contracts.

The Video Direction method specifies visible performance and timing; Audio/Voice Method owns detailed voice and mix requirements.

Do not duplicate exact speech across prompt sections unless route behavior requires it.

---

# 12. Feasibility Gate Before Spend

Before paid generation, check:

```text
action count fits duration
references support the required identity / state
route can perform required motion/audio
script fits naturally
applicable timing authority is resolved
adjacent-shot repetition is intentional or corrected
first/last frame constraints are expressible
material world-space blocking and per-angle background are recoverable
the chosen timing precision is no stricter than required and is actually supportable
material transition seams have explicit preserve/change intent
material temporal invariants are explicit when state/event direction matters
source-led work declares what source dimensions are protected versus allowed to change
known failure memory has been checked
```

If not, decompose or select another route before spending.

---

# 13. Output

```yaml
video_spec_id:
objective:
creative_latitude_ref:
creative_risk_level:
canon_anchor_refs:
previsualization_or_shot_plan_ref:
timing_authority_ref:
timing_precision_mode:
shot_type:
references:
composition_ref:
beats:
  - time:
    job:
    framing:
    start_state:
    acting_task:
    action:
    hand_contact_state_if_material:
    contact_consequence:
    lighting_source_or_state_if_material:
    camera:
    physical_or_screen_space_blocking_if_material:
    visible_background_if_material:
    screen_direction_or_relationship_axis_if_material:
    transition_or_cut_intent:
    transition_seam_if_material:
    viewer_gain:
    end_state:
    audio_copy:
continuity_state:
temporal_invariants:
source_media_authority:
variant_family_ref:
adjacent_shot_variation_plan:
capture_apparatus_plan:
acceptance_criteria:
```

---

# 14. Acceptance Rubric

Review the entire clip at normal speed with audio, then inspect important contacts/transitions frame-by-frame.

Check:

```text
opening communicates
motion adds useful change
action completes
contact/weight are credible
interaction-critical hands maintain the declared support/contact state
material lighting changes are physically motivated by the declared scene/source state
camera supports action and matches the intended capture apparatus/presentation mode
physical camera travel and optical change are not conflated when the distinction is material
world-space geometry remains coherent as screen-space composition changes across camera angles
material transitions preserve/change only the dimensions authorized by the seam contract
temporal invariants do not reset, repeat or escape their declared window without authority
material temporal-state assertions have sufficient observable evidence for the claimed review scope; insufficiently observed state remains UNVERIFIED / REVIEW rather than PASS
source-led transformations preserve only the declared protected dimensions while integrating allowed changes coherently
adjacent shots vary only where variation serves progression; accidental repeated-loop feel is absent
identity/world continuity is preserved without freezing dimensions explicitly open to expression
declared cross-variant invariants remain stable where feasible, while every output is independently reviewed
reference-led subjects inherit scene lighting only when authorized and are physically grounded in the target environment
manipulated props maintain a coherent start/action/end state
identity remains stable
performance is natural for persona
continuity is intact
speech/audio are intelligible
CTA/payoff is visible long enough
```

Sampled frames cannot certify pacing, motion or sound.


---

## V2.4 real-world hardening — format selection, visual iteration and narrative-first compiler input

Before costly video generation classify the **communication treatment** as narrative/cinematic, physical/digital product demo, editorial showcase, motion graphics, tutorial/explainer, creator-style/UGC, or authorized hybrid. Treatment is a craft decision, not a new Work Profile or provider promise. Ask only material missing questions.

`STORYBOARD_DECISION` must be evaluated before motion spend: default to propose visual previsualization for multi-beat, multi-location, physical transfer/reveal, multiple characters or multi-chapter scenes. New storyboard is skipped for accepted storyboard reuse, genuinely unambiguous one-shot or user-declined boards, with scope recorded. Storyboard is reviewable in both directions with concept/script, not a fixed frame/timestamp demand. It may be an optional tool artifact, not an input to the generator by default.

**Narrative-first mode** for PCN/character stories: use `Text on Screen` only if meaningful, `Setting & Atmosphere` (place/season/light/world/sound), `Script & Creative Direction` (continuous director's prose with natural dialogue, overlapping speech/actions, reactions, motivated camera), `Creative Invariants` (identity, products, chronology, objects, rights/claims), `Creative Open Zones` (acting, camera, improvisation), and global technical constraints. Prefer `CONTINUOUS_UNIT` or `ORDERED_BEATS` over second-by-second syntax. Use `BOUNDED_WINDOWS` or `DETERMINISTIC_EDIT_POINTS` only when actual route/measured audio/edit authority needs precision; avoid forcing arbitrary cuts.

**Physical continuity ledger** only for interaction-critical scenes: object stable identity, count, current holder/location, origin/destination, hand/support contact, action/reveal order, visibility and causal transitions. Object briefly out of frame is `OFFSCREEN_UNVERIFIED`, not deleted. Protect sequence across chapters using approved end-state + actual validated media frame, not an unapproved generated guess; no automatic frame promotes facial canon.

Use the smallest set of visual references: canonical faces, real product, scene architecture, optional per-shot frame only if materially needed. Provider may improvise on creative-open zones but must not invent a second persona, turn a croissant-printed pouch into pastry, or create extra drinks, hands, props or third-party labels. Test feasibility and quote before spend. Evaluate full audiovisual output and preserve user-approved creative choices.

