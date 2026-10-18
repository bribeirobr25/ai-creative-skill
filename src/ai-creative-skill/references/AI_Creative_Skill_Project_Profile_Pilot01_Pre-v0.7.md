# AI Creative Skill · Project Profile · Pilot 01 · Pre-v0.7

## Status

```text
DOCUMENT TYPE
=
PROJECT PROFILE FOR THE NEW CREATIVE SKILL

VERSION
=
Pre-v0.7

DATE
=
2026-10-09

PARENT
=
AI_Creative_Skill_Architecture_Spec_Pre-v0.14.md

STATUS
=
DESIGN PROFILE
NOT PILOT CANON
NOT INSTALLED
```

This profile internalizes the operational rules the new skill needs when working on Pilot 01.

It does not depend on another execution/governance skill.

It points to current Pilot canonical sources for identity, environment, scripts and approved assets instead of copying the entire canon into this file.

Pre-v0.6 preserves the current Pilot rules and adds an explicit authority category for finalization / delivery / export requirements so finishing parameters can be resolved from current Pilot authority without copying numeric presets into this profile. It also refreshes companion authority pointers while leaving Pilot canon unchanged.

Validator correction round (operator-agreed window, 2026-10-09): Pre-v0.7 records the operator decision of 2026-10-09 that the `higgsfield-content-factory` skill installed in the operator's account stays disabled while Pilot work is active and that no broad-trigger third-party skill orchestrates Pilot work (§3.1), and makes a working Pilot authority binding a precondition of installing the skill package in any host that could receive Pilot work (§2.1). Pilot canon, locks, gates and stop rules are unchanged.

---

# 1. Purpose

Pilot 01 is a recurring-persona project. Its production rules are stricter than a generic content-generation project because identity, voice, recurring environments and accepted media must survive across many outputs.

```text
PROJECT PROFILE
=
OPERATIONAL RULES
+
AUTHORITY POINTERS
+
PROJECT-SPECIFIC GATES
```

not:

```text
PROJECT PROFILE
=
SECOND COPY OF THE CANON
```

---

# 2. Authority Pointers

At runtime the profile must resolve the currently active Pilot authorities for:

```text
character identity
voice lock
recurring environment
approved start frames / technical derivatives
script / content plan
prompt construction rules
approved final media
finalization / delivery / export specification
commercial / disclosure rules
```

Current project evidence reviewed in this design includes the active v1.2 delivery notes and Phase 10 execution records.

The `finalization / delivery / export specification` category resolves project-scoped requirements such as output geometry, frame rate, container/codec, audio delivery/loudness target, controlled text placement and final assembly/export constraints **when current Pilot authority actually specifies them**. This profile does not duplicate those numbers or promote them into cross-project defaults.

## 2.1 Runtime Authority Binding Requirement

The categories above are semantic requirements, not yet concrete runtime addresses. Before live Pilot execution, the runtime must resolve a current authority binding for every category materially required by the task. A binding may be implemented as a manifest, resolver or equivalent lookup, but it must retain at least:

```yaml
authority_category:
canonical_source_ref:
version_or_currentness_ref:
resolver_or_location:
verified_at:
status:
  # RESOLVED | MISSING | STALE | CONFLICT
```

Do not hard-code fragile paths into this profile merely to make the pointer look concrete. If a required binding is missing, stale beyond safe resolution, or materially conflicting:

```text
→ STOP_REQUIRED_AUTHORITY_MISSING
   or STOP_UNRESOLVED_AUTHORITY_CONFLICT
```

The binding mechanism is runtime infrastructure; it does not become a second copy of Pilot canon.

A working binding mechanism for these categories is a precondition of installing the skill package in any host where it could receive Pilot work, and that host must be able to enforce the §13 human gates. Until both exist, the package is not installed for Pilot use, and a Pilot request reaching an installed copy stops with `STOP_REQUIRED_AUTHORITY_MISSING`. Pilot canon remains outside the package.

If a pointer cannot be resolved to a current authority, the skill must not improvise a replacement.

```text
MISSING REQUIRED AUTHORITY
→ STOP_REQUIRED_AUTHORITY_MISSING
```

## 2.2 Specialist Method Authority Boundary

Pilot tasks may invoke generic specialist methods, but those methods remain subordinate to current Pilot authority. In particular:

```text
PROJECT CANON / LOCKS
>
PILOT PROJECT PROFILE
>
APPLICABLE SPECIALIST METHOD DEFAULTS
```

Generic craft guidance may improve execution, but it may not invent a voice, change a recurring environment, promote a generated derivative into canon, relax a human gate or reinterpret a frozen project rule.

## 2.3 Finalization / Delivery Authority

When a Pilot task reaches controlled finishing, assembly or export, resolve the current project authority for finalization / delivery / export before compiling the final execution route.

```text
PROJECT-VALIDATED FINALIZATION PARAMETER
=
PILOT-SCOPED AUTHORITY

PROJECT-VALIDATED FINALIZATION PARAMETER
!=
GENERIC METHOD DEFAULT
```

Current Phase 10 validated production-method and run-record authorities may satisfy this category when the runtime binding confirms they are current and applicable to the asset/task. Numeric values remain in those project authorities; this profile carries the category and resolution rule, not a copied preset table.

If no current authority resolves a material finishing/export parameter required by the task, the skill must not silently inherit a vendor default. Resolve it through applicable project/operator authority or stop under the normal missing-authority rule.

---

# 3. Operator Governance Decision for the New Skill

Current design decision dated 2026-10-06:

```text
THE NEW CREATIVE SKILL
MUST OWN ITS OWN
AUTHORITY / STATE / BUDGET / RECOVERY / QA CONTROLS
```

No external governance skill is a runtime dependency.

The current Pilot canon-edit freeze remains in force for the active Pilot package until its own authority lifts it.

This new skill-design work may continue because it is an external design track explicitly requested by the operator. It does not silently modify the frozen Pilot canon.

```text
PILOT CANON EDIT FREEZE
=
ACTIVE UNDER PILOT AUTHORITY

NEW SKILL DESIGN WORK
=
ALLOWED

NEW SKILL DESIGN
≠
PILOT CANON CHANGE
```

## 3.1 Third-party skill activation during Pilot work

Operator decision dated 2026-10-09:

```text
higgsfield-content-factory
(installed in the operator's account)
=
DISABLED WHILE PILOT WORK IS ACTIVE

BROAD-TRIGGER THIRD-PARTY SKILL
≠
ORCHESTRATOR OF PILOT WORK
```

The operator disables the installed skill in the account; this profile records the decision and does not perform it. While Pilot work is active, no broad-trigger third-party skill may take orchestration of a Pilot task, select its route, voice, persona or environment, or trigger generation, spend or publication. Re-enabling the skill, or calling a third-party skill by name for an explicitly bounded subtask, is an operator decision. This is the Pilot-specific application of the overlapping third-party activation canary in Runtime Activation and Packaging §13.1; that canary remains the generic package test.

---

# 4. Recurring Persona Identity

For Pilot personas:

```text
RECURRING PERSONA IDENTITY
>
RANDOM / ROTATING GENERIC AVATAR
```

Production must use the currently approved identity authority or a technical derivative explicitly linked to it.

A generated technical derivative does not silently become a new hero/canonical identity.

Every downstream asset must retain lineage to the identity authority used.

---

# 5. Voice Authority by Persona

Current project authority state:

| Persona | Voice authority for talking production |
|---|---|
| Dona Vera | LOCKED: Mabel via voice replacement |
| Maya Valença | NOT YET ESTABLISHED |
| Luna Vex | NOT YET ESTABLISHED |
| Valentina Salles | NOT YET ESTABLISHED |
| Seu Arlindo | NOT YET ESTABLISHED |

When a task requires a recurring persona voice and no current voice authority exists:

```text
→ STOP_REQUIRED_AUTHORITY_MISSING
```

The skill must not cast or invent a recurring voice as an execution convenience.

---

# 6. Dona Vera · Current Voice Lock

Current active project decision:

```text
DONA VERA VOICE
=
VOICE_LOCKED
=
Mabel
via voice replacement
```

The active v1.2 delivery notes specify Mabel by voice replacement and state that the older Direction-B audio direction does not reach the video through this route.

Therefore, for the current accepted production path:

```text
NATIVE TALKING PERFORMANCE
→ MABEL VOICE REPLACEMENT
```

corresponds to:

```text
presentation_mode = ON_CAMERA_SPEECH
audio_binding_contract = NATIVE_SPEECH_THEN_VOICE_REPLACEMENT
```

for the current accepted path.

A route that emits a different native voice does not satisfy the voice lock merely because the spoken Portuguese is good.

Changing the locked voice or the voice-replacement requirement is an operator governance change, not an ordinary execution choice.

---

# 7. Dona Vera · Current Validated Talking Production Sequence

For the current validated talking-video method:

```text
SCRIPT
→ if > 15 s, split into sequential parts
→ PART 1 low-res talking generation
→ MABEL VOICE REPLACEMENT
→ mandatory speech/script verification
→ operator low-res acceptance of PART 1
→ if PART 2 is required:
     derive a clean end-frame anchor from accepted PART 1
     exclude visible brand, logo and readable text
     generate PART 2 only after PART 1 acceptance
     apply Mabel voice replacement
     mandatory speech/script verification
     operator low-res acceptance
→ assemble complete 480p preview with controlled on-screen text
→ operator approves complete low-res preview
→ upscale the accepted clip(s)
→ final-resolution review on target mobile display
→ final controlled assembly / export
```

This is a project method baseline, not a permanent vendor lock.

A future non-Higgsfield route may replace individual stages only after it satisfies the same project acceptance requirements.

For the current Higgsfield voice-replacement route, the applied voice identifier must be recorded at submission because the provider result does not preserve sufficient voice-selection provenance by itself.

## 7.1 Talking Persona Specialist Interface

Recurring visible speech should load:

```text
TALKING_PERSONA
+ SCRIPT_PERFORMANCE
+ AUDIO_VOICE_PERFORMANCE
+ VIDEO_DIRECTION
+ QA_REALISM_PERFORMANCE
```

The generic Talking Persona method owns craft procedure. This Project Profile supplies the strict Pilot authority for identity, voice, duration, start-frame discipline, multipart dependencies, human gates and final-resolution review.

A route that is excellent for generic talking avatars is not Pilot-approved until it passes the applicable Pilot scorecard.

---

# 8. Speech Verification

For generated spoken content in the current validated Pilot talking method, speech verification is mandatory **before the clip is presented to the operator for creative acceptance**.

```text
RETURNED AUDIO
→ TRANSCRIPT / SCRIPT COMPARISON
→ HUMAN LISTENING / REVIEW
→ OPERATOR CREATIVE ACCEPTANCE
```

ASR/transcription is diagnostic support, not final truth. Recognition normalization or omission can produce a transcript mismatch without proving a spoken-content defect.

Human listening remains the acceptance authority for naturalness, exact meaning, voice identity and lip-sync.

If the required speech-verification path cannot be performed:

```text
→ STOP_REQUIRED_VERIFICATION_UNAVAILABLE
```

Do not silently downgrade the verification gate to optional.

---

# 9. Resolution / Progressive Fidelity

The current validated method requires approval of performance/content before the expensive final-resolution step.

```text
accepted low-res clip
→ upscale same accepted clip
→ review again at final resolution
```

Direct regeneration at final resolution is not a substitute for preserving an accepted low-resolution performance.

If an upscale fails final-resolution review:

```text
RETRY / REPAIR THE UPSCALE
OF THE SAME ACCEPTED SOURCE CLIP
```

Do not generate a new talking performance merely because the upscale failed.

The project records a failed direct-1080p path in which scene/reference contamination changed the result. Accepted state must therefore be preserved across resolution changes.

---

# 10. Duration / Multipart Rule

For the current validated Dona Vera talking method:

```text
MAX SINGLE PART
=
15 s
```

If the approved script cannot fit within one part:

```text
SCRIPT > 15 s
→ split into sequential parts
```

Multipart dependency rule:

```text
PART 1
→ generate
→ voice replace
→ verify speech
→ operator accept

ONLY THEN

PART 2
→ use a clean end-frame continuity anchor from accepted PART 1
→ generate
```

A validated approximately 12-second canary remains an empirical example, not a universal minimum.

Other future routes may use different duration limits only after the applicable Pilot project rule is explicitly changed or a route-specific project rule is approved.

---

# 11. Reference Restrictions

For the current Pilot persona-generation method:

```text
VISIBLE BRAND
LOGO
READABLE TEXT
IN GENERATION REFERENCE IMAGE
=
NOT ALLOWED
```

This is an operational rule, not a preference.

If branded/textual content is required in the deliverable, add it through controlled finishing/compositing unless the operator explicitly changes the project rule.

Reference authority remains explicit:

```text
character reference
→ identity only unless more is declared

environment reference
→ geometry / spatial identity only unless more is declared

style reference
→ style only
```

Wardrobe is described in words for the current method; do not add a wardrobe-only image reference.

On-screen text is **never requested from the generative image/video model** in the current method. It is added as a controlled finishing layer.

A clean continuity/start-frame derivative does not become a new identity authority.

---

# 12. Start-Frame Discipline

Where a talking/lipsync route benefits from a dedicated start frame:

- use an approved identity source or approved technical derivative;
- prefer route-appropriate framing, face visibility and mouth state;
- do not silently promote a generated start frame into a new identity authority;
- preserve the binding from start frame back to the canonical identity.

The active package specifically added the initial frame as an anchor in the production method. This is treated as a project-specific continuity control.

---

# 13. Human Gates

For the current Dona Vera talking method, required gates include:

```text
per-part speech verification
→ per-part low-res operator acceptance
→ complete 480p preview with controlled text
→ operator preview approval
→ upscale accepted source clip(s)
→ final-resolution review on target mobile display
→ final assembly / export
```

Final-resolution review is mandatory.

Human review may evaluate:

```text
identity
age / recognizability
visual naturalness
mouth / teeth / jaw integrity
lip-sync
PT-BR naturalness
voice identity
spoken-content fidelity
social-native presence
text placement / legibility
final-resolution artifacts
```

The skill cannot mark these passed merely because the request asked for them.

## 13.1 Canonical Exemplars and Creative Preferences

Approved scripts/media may be curated into a small calibration set for recurring persona voice and performance. A calibration exemplar remains an example, not a second canon.

Keep separate:

```text
OBJECTIVE DEFECT
PROJECT / PERSONA RULE
OPERATOR CREATIVE PREFERENCE
```

An explicit operator preference or repeated approval/rejection pattern may inform ranking among technically valid outputs, but one rejection does not silently become permanent project law. Governance changes still require explicit authority.

When the project archive contains useful before/after execution cases, preserve the defect, probable cause, primary change, improvement and regression as scoped experience memory.

---

# 14. Commercial Authenticity and Disclosure

Pilot personas are fictional/AI personas.

```text
FICTIONAL PERSONA
≠
REAL-WORLD CUSTOMER TESTIMONIAL
```

A persona must not convert fiction into a fake first-person claim of real product/service experience.

```text
AI DISCLOSURE
≠
ADVERTISING DISCLOSURE
```

When commercial disclosure is required, identifying the persona as AI does not replace advertising disclosure.

No generated stress-test, review, rating, buyer identity or commercial result is treated as real-world proof without real evidence.

---

# 15. Budget / Spend Behavior

Every paid Pilot action must be inside an operator-approved scope.

Canonical budget arithmetic and reservation semantics are inherited from:

```text
AI_Creative_Skill_Execution_Contracts_Pre-v0.13.md
```

For the current multipart talking-production planning method, the budget plan must include capacity for **two repeat attempts per part** unless the operator approves a different reserve.

A reserve is planning authority, not permission for blind retries. Each retry still follows diagnosis, route state and retry limits.

Reaching the approved cap triggers the canonical cost stop.

Do not repeat authorization questions already covered by a still-valid approval scope.

---

# 16. Retry / Stop Rules

Project-specific triggers:

- before a paid retry, check applicable Pilot/route failure memory and declare accepted state that could regress;
- prefer one primary causal intervention per diagnostic retry when practical;
- before scaling a new high-risk talking route, run the smallest valid canary that exercises the uncertain capability;
- never resubmit a job/batch whose submission outcome is unknown;
- reconcile by provider job/prediction ID first;
- creative rejection is not a technical retry;
- repeated wrong-language behavior can invalidate the model/route for the current task class;
- policy refusal is not bypassed by changing providers;
- operator rejection returns to diagnosis/replanning, not automatic regeneration;
- final-resolution upscale failure returns to the same accepted source clip, not to new talking generation.

The canonical stop labels, job/retrieval states and retry/failover semantics are defined in:

```text
AI_Creative_Skill_Execution_Contracts_Pre-v0.13.md
```

This Project Profile invokes those canonical stops rather than redefining them.

---

# 17. Provider / Route Policy

Pilot 01 is not vendor-locked by architecture.

However:

```text
DOCUMENTED CAPABILITY
≠
PROJECT-APPROVED ROUTE
```

A new route must pass the relevant project benchmark before production approval.

For talking personas, the scorecard should prioritize:

```text
identity fidelity
PT-BR naturalness
spoken-text fidelity
voice-identity fidelity
lip-sync
mouth / teeth / jaw integrity
natural eye / face behavior
cost
reproducibility
```

Cinematic flourish is secondary to identity and speech correctness for a direct-to-camera talking clip.

Route comparison should reuse fixed benchmark cases where practical, and task-specific scale should wait for a small canary when the current request depends on an unvalidated capability.

---

# 18. Route Evidence / Approval Vocabulary

The Project Profile uses the canonical route evidence and production approval vocabularies defined in:

```text
AI_Creative_Skill_Execution_Contracts_Pre-v0.13.md
```

Every empirical pass/fail retains its test scope. A short-duration pass is not evidence of full-length capability.

---

# 19. Current Empirical Baselines to Preserve

Current provider/model empirical baselines and measured cost/test records are stored in:

```text
AI_Media_Provider_Registry_v0.9.md
```

This Project Profile owns operational method and acceptance constraints, not provider-price or benchmark-instance duplication.

The accepted current talking-method baseline remains:

```text
native talking performance
→ Mabel voice replacement
→ mandatory speech verification
→ low-res operator acceptance
→ complete low-res preview
→ upscale accepted source
→ final-resolution mobile review
→ final assembly
```

Provider/model alternatives must be compared against the applicable project acceptance requirements.

---

# 20. Organic vs Ads

Pilot 01 can use different Work Profiles.

```text
PROJECT PROFILE = Pilot 01
WORK PROFILE = ORGANIC
```

must not inherit Ads-only offer/PROOF/QUEST logic.

Likewise:

```text
PROJECT PROFILE = Pilot 01
WORK PROFILE = ADS
```

adds commercial evidence, claims, offer and disclosure requirements without changing the identity/voice locks owned here.

Both Work Profiles may load the same Talking Persona / Script / Audio / Video craft methods, but the Project Profile remains the source of Pilot-specific identity, voice and human-gate constraints.

---

# 21. Project Profile Principle

```text
PILOT PROFILE
=
STRICTER OPERATIONAL CONSTRAINTS
ON TOP OF THE GENERIC CORE
```

A provider capability does not override project truth.

A new route earns permission by passing the project requirement, not by appearing in a model catalog.

Pilot-specific lessons should feed scoped calibration/experience memory so known defects are checked before spend and accepted state is protected during repair.
