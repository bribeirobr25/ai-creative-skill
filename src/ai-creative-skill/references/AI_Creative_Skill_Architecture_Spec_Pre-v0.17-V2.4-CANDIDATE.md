> **V2.4 CANDIDATE SCOPE:** Modified version of this method family. Read the final section “V2.4 real-world hardening” for current candidate additions. Historical V2.3 discussion and prior-source pointers below remain provenance, not active version resolution.

# AI Creative Skill Architecture Spec · Pre-v0.17-V2.4-CANDIDATE

## Status

```text
DOCUMENT TYPE
=
CURRENT DESIGN SPECIFICATION FOR THE NEW CREATIVE SKILL

VERSION
=
Pre-v0.17-V2.4-CANDIDATE

DATE
=
2026-10-16

STATUS
=
V2.3 ARCHITECTURE-REACTIVATION DESIGN CANDIDATE
NOT PROMOTED TO 00_ACTIVE
NOT INSTALLED
ZERO-COST CONTRACT-MODEL VALIDATED
NOT HOST / PROVIDER VALIDATED
NO AUTOMATIC SPEND AUTHORITY
NO CAMPAIGN-LAUNCH AUTHORITY
```

GPT validation hardening branch (2026-10-10): Pre-v0.15-V2-CANDIDATE incorporates only gaps that survived the reproducible zero-cost audit. It adds architectural requirements for canonical execution snapshots, exact approval binding, mutable-state revision control, persisted schema migration, scoped composite-reference locators, cancellation races, state-integrity checks and cross-project reuse boundaries. It also records P1 audit-trace/localization/variant hardening while preserving the existing provider-neutral creative architecture.


This document supersedes `AI_Creative_Skill_Architecture_Spec_Pre-v0.13.md` for design purposes.

Pre-v0.14 stabilizes document-version resolution. It preserves the Pre-v0.13 creative architecture while making the Current Design Manifest the single authority for current companion/method versions, separating parent-document identity from last-validated-against snapshots, and preventing pointer-only changes from causing version cascades.

Historical architecture documents remain research/history only. `AI_Ads_Creative_Intelligence_Working_Notes_v0.4.md` remains a frozen research archive.

The new skill is self-contained. It does not require another governance skill. Authority resolution, authorization, budget control, job state, cost state, retry/recovery, provider routing, asset lineage, QA, stop conditions and learning belong inside this system.

---

# 1. What We Are Building

A provider-agnostic creative operating skill that can turn a request into validated media while preserving project truth, evidence, state, cost and learning.

```text
USER / CLIENT INPUT
        ↓
AUTHORITY + REQUEST ROUTING
        ↓
STATE RECOVERY
        ↓
RESOLVE SPECIALIST METHOD STACK
        ↓
OPTIONAL RESEARCH / EVIDENCE
        ↓
CREATIVE INTENT
        ↓
PRODUCTION SPECIFICATION
        ↓
CAPABILITY ROUTING
        ↓
MODEL SELECTION
        ↓
EXECUTION ROUTE SELECTION
(model × provider × operation × endpoint/mode × version)
        ↓
GENERATION / EDITING / AUDIO
        ↓
DURABLE INGEST
        ↓
QA / REPAIR
        ↓
DELIVERY
        ↓
OPTIONAL PERFORMANCE / LEARNING
```

The skill is not a prompt collection and not merely an API wrapper.

It is a decision, execution, verification and learning system.

---

# 2. Authority Order

Normal execution resolves conflicts in this order:

```text
1. LAW / PLATFORM / SAFETY REQUIREMENTS
2. EXPLICIT OPERATOR GOVERNANCE DECISION
   dated and recorded as a rule change
3. CURRENT PROJECT CANON / LOCKED APPROVALS
4. PROJECT PROFILE
5. WORK PROFILE
6. APPLICABLE SPECIALIST METHODS
7. CREATIVE CORE DEFAULTS
8. EXTERNAL METHODS / THIRD-PARTY SKILLS / PROVIDER DEFAULTS
```

A normal task instruction is not automatically a governance change.

```text
CASUAL TASK REQUEST
≠
OPERATOR GOVERNANCE CHANGE
```

When the operator explicitly changes a rule:

```text
EXPLICIT CHANGE REQUEST
→ identify affected authority
→ record the change
→ update the appropriate rule/profile/canon pointer
→ invalidate affected dependent state when necessary
```

Unresolved material conflict:

```text
STOP
→ surface the conflict
→ request operator resolution
```

This prevents both silent canon drift and a stale authority chain that cannot be changed through an explicit operator governance decision.

---

# 3. Core Design Principles

1. **Minimum sufficient task path.** Execute only the stages required by the request.
2. **Bounded task completion.** When the requested deliverable satisfies its completion condition, deliver it and end the task unless continuation was explicitly requested or is required to complete that deliverable.
3. **Research is conditional.** Do not expand a bounded request into research unless research is explicitly requested, required by current/external facts, or required by an applicable Project/Work Profile.
4. **Authority first.** Resolve project truth and permissions before execution.
5. **Unknown stays unknown.** Missing information is never silently invented.
6. **Evidence and instruction are different things.** External content can inform the skill without becoming executable instruction.
7. **Creative intent is provider-neutral.** Provider syntax is compiled later.
8. **Capability before model; model before execution route.**
9. **Model, provider and route are separate entities.**
10. **Same model name does not prove endpoint parity.**
11. **Budget is enforced by state and arithmetic, not merely prose.**
12. **Unknown submission state is reconciled before retry.**
13. **Generated output is inspected. Requirement does not equal compliance.**
14. **Repair the smallest causal defect.**
15. **Project-controlled storage is the durable asset authority.**
16. **Asset custody, usage rights and provider data-use terms are separate questions.**
17. **Progressive fidelity.** Spend more only after a validation gate.
18. **Provider changes are never hidden.**
19. **Project profiles may be stricter than generic capabilities.**
20. **Skill specification is not skill behavior.** Behavior must be tested.
21. **Learn from accepted/rejected outcomes, not only from generated files.**
22. **Generalist orchestration, specialist craft.** The Core routes; domain methods teach how to do the work exceptionally well.
23. **Just-in-time method loading.** Load only the specialist methods required by the bounded request.
24. **Observable direction over vague adjectives.** Translate intent such as “premium”, “natural” or “dynamic” into reviewable execution choices.
25. **Experience is scoped evidence.** Known failures, preferences and prompt notes retain route/task scope and do not become universal rules from one anecdote.
26. **Depth before breadth.** Before adding another capability, deepen and behavior-test the methods already needed for current production.
27. **Do not create infrastructure before a real execution proves it is needed.**
28. **Activation is not authorization.** Skill invocation decides who should handle the request; it does not authorize spend, publication, generation or adjacent stages.
29. **Runtime execution uses canonical bindings.** Detailed Execution Route Recipe schema/state, provider facts, asset naming and derived route-view rules live in their canonical companion specifications; the Architecture references them rather than redefining them.
30. **One canary, one question.** Separate basic execution, async recovery and craft validation so a pass or failure has interpretable meaning.

---

# 4. Architecture Layers

## A · Governance and State

Owns:

- authority resolution;
- operator governance changes;
- project/profile selection;
- task/run state;
- approval scope;
- production budgets and caps;
- cost reservation/reconciliation;
- job state and retrieval state;
- retry/failover rules;
- stop conditions;
- asset/run lineage;
- route freshness;
- version/dependency invalidation.

## B · Creative Core

Owns generic creative reasoning:

- request classification;
- research interface when needed;
- evidence state;
- creative objective;
- concept/variant distinction;
- copy/script interface;
- static/video/audio production-spec interface;
- reference authority;
- continuity;
- acceptance criteria;
- specialist-method resolution interface;
- calibration / experience-memory interface.

The Core does **not** own Ads-specific buyer/offer frameworks or detailed craft manuals. Those belong in Work Profiles and Specialist Methods.

## C · Production Specification

Owns the provider-neutral executable intent:

- deliverables;
- exact text where applicable;
- reference bindings and authority;
- immutable vs variable attributes;
- presentation mode;
- audio binding contract;
- auxiliary audio requirements;
- continuity;
- layout or scene timing;
- technical requirements;
- acceptance criteria;
- specialist-method outputs required to make the spec observable and reviewable.

## D · Replaceable Execution

Owns:

- capability discovery;
- model selection;
- execution-route selection;
- provider execution binding: Execution Route Recipe for current minimal implementation; reusable Provider Adapter when implemented;
- upload/reference binding;
- quote;
- submission;
- polling/reconciliation;
- retrieval;
- deterministic editing;
- export;
- durable ingest.

## E · QA, Delivery and Learning

Owns:

- technical inspection;
- factual/project/creative QA;
- repair;
- review verdict;
- delivery package;
- performance ingestion where relevant;
- benchmark and regression learning;
- specialist QA rubrics and inspection-coverage discipline;
- causal failure / repair learning.

These are responsibility layers, not five mandatory sequential passes.

## 4.1 Responsibility Layers vs Operational Stages

The architecture has two complementary views:

```text
RESPONSIBILITY LAYERS
=
who owns each kind of decision / state / output

OPERATIONAL STAGES
=
when that work may occur in an end-to-end request
```

A stage can invoke more than one layer, and the same layer can reappear later in the workflow. The table below assigns a **primary** responsibility owner for clarity; it does not prohibit cross-layer checks.

| Stage | Operational stage | Primary responsibility layer |
|---|---|---|
| 0 | Authority + Request Routing | A · Governance and State |
| 1 | State Recovery / Intake | A · Governance and State |
| 2 | Research / Evidence when required | B · Creative Core |
| 3 | Creative Intent / Concept | B · Creative Core |
| 4 | Production Requirements / References | C · Production Specification |
| 5 | Copy / Script / Static / Scene Spec | C · Production Specification |
| 6 | Capability + Model + Route Planning | D · Replaceable Execution |
| 7 | Cost / Approval Preflight | A · Governance and State |
| 8 | Execution + Durable Ingest | D · Replaceable Execution |
| 9 | Editing / Finishing | D · Replaceable Execution |
| 10 | QA + Repair | E · QA, Delivery and Learning |
| 11 | Delivery / Preservation | E · QA, Delivery and Learning |
| 12 | Optional Performance Learning | E · QA, Delivery and Learning |

The operational workflow is therefore not equivalent to a one-pass A → B → C → D → E pipeline.

---

# 4.2 Canonical Path / Route Vocabulary

To avoid using `route` for both task orchestration and technical execution:

```text
TASK PATH
=
the logical stages selected to satisfy the user's bounded request

MINIMUM SUFFICIENT TASK PATH
=
the smallest valid task path that reaches the requested completion boundary

EXECUTION ROUTE
=
model × provider × operation × endpoint/mode × version

EXECUTION ROUTE CONTRACT
=
the canonical technical/state contract for that execution route

EXECUTION ROUTE RECIPE
=
the versioned runtime binding used to invoke that execution route
```

Machine fields may keep compact names such as `route_id` and `route_recipe_ref`; prose should use the canonical terms above when ambiguity is possible.

---

# 5. Task Configuration Elements

The skill combines **two profile types**, a **just-in-time Specialist Method Stack**, and an **execution route**. Project Profile and Work Profile are authority/profile objects; Specialist Methods provide domain craft; Execution Route is a technical execution object. Each task loads only the project/work/method/route information that materially applies.

## 5.1 Project Profile

Contains **runtime project rules** and points to canonical evidence.

It may define:

- canon/authority pointers;
- identity/persona locks;
- environment locks;
- voice/audio locks;
- reference restrictions;
- disclosure/authenticity rules;
- rights constraints;
- human review gates;
- production limits;
- spend/retry/stop overrides;
- route approval constraints.

A Project Profile does not duplicate the entire canon.

```text
PROJECT PROFILE
contains operational rules
and
points to canonical evidence
```

### 5.1.1 V2.3 Project Continuity Candidate

A persistent project may outlive any one bounded task or Work Profile.

```text
PROJECT
!=
TASK

TASK COMPLETE
does not imply
PROJECT COMPLETE
```

Project-scoped state may persist across task boundaries only when it is durable and relevant, including:

- project objective;
- explicit constraints / negative authority;
- resource and budget envelope;
- accepted decisions;
- stable entity identities;
- accepted outputs;
- evidence/source references;
- explicit unknowns and gates;
- experiment state;
- next-action register.

Task-local wording, tone or temporary preferences do not become project canon unless explicitly promoted.

When ownership changes, the previous task closes or delegates through the cross-profile handoff contract defined by Execution Contracts. State/evidence may transfer; authority never transfers by implication.

### 5.1.2 V2.3 Autonomy Envelope Candidate

Broad delegation such as “you decide” is represented as project governance over existing authorization primitives, not as unlimited authority.

```text
AUTO_ALLOWED
ASK_BEFORE
FORBIDDEN_OR_OUTSIDE_AUTHORITY
```

The envelope is evaluated by action class and may be revised by the user. Explicit negative scopes remain binding until revised. Tool connection or capability availability does not alter the envelope by itself.


## 5.2 Work Profile

Defines the type of creative work.

Candidate profiles in this V2.3 reactivation branch:

```text
ADS
ORGANIC_CONTENT
RESEARCH_ONLY
```

Future / still-deferred profiles may include:

```text
PRODUCT_CONTENT
CLIENT_PRODUCTION
```

`RESEARCH_ONLY` is reactivated here as a **logical Work Profile candidate** because U1/U2 demonstrate independent bounded research value. It owns research/synthesis deliverables, not every task that happens to contain research. Supporting research inside an Ads/Organic final deliverable remains a bounded subtask and does not seize final-deliverable ownership.

## 5.3 Specialist Method Stack

A task-specific set of craft methods loaded only when needed.

```text
PROJECT / WORK CONTEXT
+
TASK PATH
+
CURRENT STATE / REUSABLE EVIDENCE
→
SPECIALIST METHOD STACK
```

Examples may include buyer research, ads strategy, image direction, video direction, talking-persona production, typography/layout, audio/voice, platform-specific execution, route compilation, QA and localized repair.

A Specialist Method:

- does not override Project or Work authority;
- owns professional procedure, decision rules, examples and acceptance rubrics for its domain;
- may be skipped when its output already exists and is still valid;
- is loaded just in time rather than copied into the Core.

Canonical method-system semantics are defined in:

```text
AI_Creative_Skill_Specialist_Method_System_Pre-v0.2.md
```

## 5.4 Execution Route

One technically executable combination:

```text
MODEL
+
PROVIDER
+
OPERATION
+
ENDPOINT / MODE
+
VERSION
```

## 5.5 Execution Route Recipe

An Execution Route Recipe is the versioned runtime binding for one concrete Execution Route. It does not own creative intent, pricing truth, route approval or project authority.

Canonical schema, recipe-state semantics and the Slice-1 minimum profile live in:

```text
AI_Creative_Skill_Route_Recipe_Spec_Pre-v0.3.md
AI_Creative_Skill_Execution_Contracts (current version resolved by the Current Design Manifest)
```

The Architecture intentionally does not redeclare recipe fields.

---

# 6. Operating Modes

```text
DEMO
LIVE
EDIT_RESUME
REVIEW_ONLY
BENCHMARK
```

### DEMO
No paid external execution unless separately authorized.

### LIVE
Real research/generation/editing under current authorization.

### EDIT_RESUME
Recover valid state and alter only what is necessary.

### REVIEW_ONLY
Inspect without generating unless a new action is separately authorized.

### BENCHMARK
Controlled comparison with explicit test intent, rubric and budget.

Benchmark subtypes:

```text
CREATIVE_EXPLORATION
MODEL_BENCHMARK
PROVIDER_PARITY_BENCHMARK
PRODUCTION_BENCHMARK
```

---

## 6.1 Skill Activation Boundary

Host/runtime activation occurs before Stage 0. The future runtime package must define:

```text
positive triggers
negative boundaries
overlap / precedence behavior
ownership vs delegation
```

Activation answers:

```text
SHOULD THIS SKILL HANDLE / ORCHESTRATE THIS REQUEST?
```

It does **not** answer:

```text
IS GENERATION AUTHORIZED?
IS SPEND AUTHORIZED?
IS RESEARCH REQUIRED?
SHOULD LATER STAGES RUN?
```

Those remain Stage-0/Stage-1 and profile/approval decisions. If multiple installed capabilities appear relevant, the runtime should prefer the narrowest current authority that actually owns the requested deliverable, or explicitly delegate a bounded subtask. It must not create a hidden dependency on another governance skill.

Detailed packaging/activation guidance lives in `AI_Creative_Skill_Runtime_Activation_and_Packaging_Pre-v0.3.md`.

---

# 7. Task Paths

```text
RESEARCH
NEW_CREATIVE
VARIATE
EDIT
ADAPT
IMPROVE
REVIEW_ONLY
BENCHMARK
RESUME_INTERRUPTED
```

Examples:

| Request | Minimum sufficient task path |
|---|---|
| Explain system | authority/read only |
| Research topic/audience | profile → research → synthesis |
| Script only | state/context → creative intent → script QA → deliver → end |
| New static | applicable profile → creative spec → execute → QA |
| New video | applicable profile → scene/audio spec → execute → QA |
| Variate accepted asset | accepted asset/concept → variation plan → authorized batch execution → per-variant QA → deliver accepted set |
| Fix CTA | accepted asset → controlled edit → QA |
| Resize/reframe | accepted asset → adaptation → QA |
| Resume job | recover → reconcile → continue |
| Analyze results | learning task path; no generation unless requested |
| Compare models | model benchmark |
| Compare providers for same model | parity benchmark |

## 7.1 Task Completion Boundary

Every request must resolve a requested deliverable and a completion condition before entering work beyond intake.

```text
REQUEST
→ resolve requested deliverable
→ determine minimum sufficient task path
→ define completion condition / exit point
→ execute only required stages

WHEN COMPLETION CONDITION IS SATISFIED:
→ deliver the requested result
→ persist only the state required by the applicable contracts
→ END TASK
```

Completion does **not** authorize continuation into adjacent stages. Unless the user explicitly requests continuation or the next step is required to complete the requested deliverable, the skill must not automatically:

- enter provider/model/route planning;
- generate additional assets or variants;
- spend money;
- publish, launch or distribute;
- create adjacent deliverables;
- append unsolicited next-step offers merely because later stages exist.

A material blocker, limitation, safety issue, missing required authority or required handoff may still be surfaced when necessary to explain why the requested deliverable cannot be completed as asked.

A new user request after delivery starts a new routing decision; it is not assumed to be pre-authorized continuation of the previous task.

## 7.2 Research Activation Rule

Research is activated only when at least one of the following is true:

```text
A. USER_EXPLICITLY_REQUESTS_RESEARCH
OR
B. CURRENT / EXTERNAL FACTS ARE NECESSARY
   TO SATISFY THE REQUESTED DELIVERABLE
OR
C. APPLICABLE PROJECT / WORK PROFILE
   REQUIRES SPECIFIC EVIDENCE BEFORE COMPLETION
```

Otherwise:

```text
USE AVAILABLE AUTHORITATIVE CONTEXT
→ DO NOT EXPAND THE TASK INTO RESEARCH
```

If required evidence is missing and cannot be established within the request's allowed task path, preserve the unknown or stop according to the applicable authority/verification rule. Do not silently replace missing evidence with inference.

## 7.3 Variant / Replication Task Path

`VARIATE` is used when the request starts from an accepted asset or accepted concept and asks for multiple controlled executions of the same underlying concept.

The task path must resolve, before paid execution:

```text
SOURCE ASSET / CONCEPT
+
TARGET ACCEPTED VARIANT COUNT
+
PRESERVE SET
+
VARY SET
+
ACCEPTANCE CRITERIA
+
APPROVAL / BUDGET / MAX ATTEMPTS
```

Core distinction:

```text
TARGET_ACCEPTED_VARIANTS
≠
GENERATION_ATTEMPTS
```

A request for `N` accepted variants does not mean exactly `N` provider submissions. Each candidate must be reviewed independently. The batch may require additional attempts within the authorized attempt and budget limits. It must not continue indefinitely to satisfy the accepted-count target.

Declared preserved attributes remain binding across the batch. Declared variation dimensions may change only within the task/profile authority and the selected Execution Route capability. A provider output is not considered compliant merely because the prompt requested the invariant.

The canonical optional batch record and conformance behavior live in `AI_Creative_Skill_Execution_Contracts (current version resolved by the Current Design Manifest)`.

---

# 8. Generic Workflow

```text
0. AUTHORITY + REQUEST ROUTING
1. STATE RECOVERY / INTAKE
2. RESEARCH / EVIDENCE WHEN REQUIRED
3. CREATIVE INTENT / CONCEPT
4. PRODUCTION REQUIREMENTS / REFERENCES
5. COPY / SCRIPT / STATIC / SCENE SPEC
6. CAPABILITY + MODEL + ROUTE PLANNING
7. COST / APPROVAL PREFLIGHT
8. EXECUTION + DURABLE INGEST
9. EDITING / FINISHING
10. QA + REPAIR
11. DELIVERY / PRESERVATION
12. OPTIONAL PERFORMANCE LEARNING
```

Stages are skipped when a valid output already exists. Stages after the resolved exit point are not entered merely because they exist in the generic workflow.

The Work Profile decides what “research”, “concept” and “performance” mean for that work class, while §7.2 decides whether research is activated for the bounded request. Applicable Specialist Methods deepen the active stages without creating new mandatory stages.

---

# 9. Detailed Workflow Start · Stages 0 and 1

The generic workflow lists Stage 0 and Stage 1 separately. They remain separate here because they answer different questions.

## 9.1 Stage 0 · Authority + Request Routing

Purpose:

```text
WHAT IS THIS REQUEST?
WHO / WHAT HAS AUTHORITY?
WHICH PROJECT + WORK RULES APPLY?
```

Before state recovery:

- resolve the authority chain;
- resolve the Project Profile;
- resolve the Work Profile;
- identify the candidate Specialist Method Stack;
- classify the task path;
- classify the operating mode;
- identify any immediate authority or policy conflict that requires a stop;
- establish the initial routing context for the task.

Stage-0 output:

```text
ROUTING CONTEXT
=
resolved authority
+ project profile
+ work profile
+ candidate specialist methods
+ task path
+ operating mode
```

## 9.2 Stage 1 · State Recovery / Intake

Purpose:

```text
WHAT ALREADY EXISTS?
WHAT IS STILL OPEN?
WHAT MAY BE REUSED?
WHAT IS CURRENTLY AUTHORIZED?
```

Recover or establish:

- current Work Card / execution snapshot when applicable;
- open jobs and unknown submissions;
- accepted assets and dependent versions;
- current approval scope;
- confirmed spend, open reservations and remaining budget;
- requested deliverables and missing inputs;
- resolved exit point and completion condition for the bounded request;
- blockers and stop points;
- reusable assets vs required new work;
- reusable research/method outputs vs specialist work that must run now;
- final Specialist Method Stack for the bounded request.

Then choose the minimum sufficient task path using the recovered state, the resolved completion boundary and the final method stack.

Stage-1 output:

```text
WORK CARD / CURRENT EXECUTION SNAPSHOT
```

The Work Card is an execution snapshot, never a second canon. Slice 1 may implement only the six minimum persistent contracts defined in the Execution Contracts rather than a full Work Card.

---

# 10. Evidence State

Generic evidence vocabulary:

```text
OBSERVED
USER_PROVIDED
VERIFIED_EXTERNAL
PROJECT_EMPIRICAL
INFERRED
PROPOSED
UNSUPPORTED
```

Work Profiles may add domain-specific evidence structures.

Do not promote inference into measurement.

---

# 11. Concept and Variant Model

Generic lineage:

```text
OBJECTIVE
→ CREATIVE HYPOTHESIS / INTENT
→ CONCEPT FAMILY
   ├── VARIANT A
   ├── VARIANT B
   └── VARIANT C
```

A materially different communication mechanism is a new concept.

A wrapper change around the same mechanism is usually a variant.

## 11.1 Publication / Performance Lineage · FUTURE INTERFACE

When performance learning is connected to real distribution later, preserve the distinction between the creative asset and each distribution instance:

```text
CONCEPT
→ VARIANT
→ ASSET
→ PUBLICATION INSTANCE
→ PERFORMANCE RECORD
```

The same asset may be published on different platforms, accounts, campaigns, dates or audiences and therefore accumulate different performance records. Performance must attach to the relevant publication context rather than being silently attributed to the underlying asset in the abstract.

This lineage is a future learning/data interface. It does **not** grant publication or campaign-launch authority.

---

# 12. Reference System

## Reference Modes

```text
CREATE
PRESERVE
TRANSFORM
STYLE_ONLY
```

## Reference Authorities

Examples:

```text
CHARACTER_IDENTITY
PRODUCT_IDENTITY
ENVIRONMENT_GEOMETRY
PROP_STATE
START_FRAME_COMPOSITION
VOICE_CHARACTERISTICS
EXACT_AUDIO
STYLE
TEXT_CONTENT
```

Every reference must specify what it controls and what it must not silently contribute.

Example:

```yaml
reference_id: STYLE-017
mode: STYLE_ONLY
authority:
  - lighting
  - palette
  - material_feel
excluded_inheritance:
  - people
  - logo
  - text
  - product_geometry
```

A Project Profile can prohibit a reference class even if a route technically supports it.

---

### 12.1 Scoped / Composite References

A reference role may apply to the whole asset or to a smaller authoritative surface:

```text
WHOLE_ASSET
SEMANTIC_REGION
SPATIAL_REGION
SUBJECT
PANEL
```

The binding carries a stable locator appropriate to the scope. Authority, `allowed_inheritance` and `excluded_inheritance` apply only to that scope. A moodboard panel used for style does not make every person, logo, product, color, text string or environment in the board authoritative.

Cross-project references are ineligible as current authority by default unless an explicit import/reuse authority binds the source asset to the current project and role.

---

# 13. Audio Model

Audio is represented on independent dimensions instead of one overloaded enum.

## 13.1 Presentation Mode

```text
ON_CAMERA_SPEECH
VOICEOVER
NO_SPEECH
```

This describes how speech is presented in the creative.

## 13.2 Audio Binding Contract

```text
NATIVE_SPEECH
VOICE_REFERENCE
EXACT_APPROVED_AUDIO
SEPARATE_TTS
NATIVE_SPEECH_THEN_VOICE_REPLACEMENT
```

This describes how spoken audio is created, bound or preserved.

## 13.3 Auxiliary Audio

```text
SFX
MUSIC
```

Important distinctions:

- presentation mode and binding contract are separate;
- voice reference is not exact audio;
- exact approved audio is not freely reinterpreted;
- native speech followed by voice replacement is a valid pipeline;
- talking video, lipsync and voice replacement are separate capabilities;
- audio quality, voice identity, spoken-content fidelity and lipsync require direct review.

Project Profiles may lock a presentation mode, an audio binding contract, or both for a persona or deliverable.

---

# 14. Provider-Neutral Production Specs

## Static

May contain:

```text
purpose / concept ID
format / aspect
primary visual
reference authorities
reading order
exact text
physical vs overlay text
layout constraints
acceptance checks
```

## Video

May contain:

```text
purpose / concept ID
active references
first frame
identity / physical invariants
acting task
camera / framing
timed stages
start state
action
contact / consequence
end state
presentation mode
audio binding contract
text / graphics plan
acceptance checks
```

Continuity uses:

```text
START STATE
→ ACTION / CONTACT / CAUSE
→ CONSEQUENCE
→ END STATE
→ NEXT START
```

---

# 15. Capability → Model → Route

Never jump directly from task to vendor.

```text
PRODUCTION REQUIREMENT
↓
CAPABILITY REQUIREMENTS
↓
ELIGIBLE MODEL FAMILIES
↓
MODEL SELECTION
↓
ELIGIBLE EXECUTION ROUTES
↓
ROUTE SELECTION
↓
PROVIDER EXECUTION BINDING
(Execution Route Recipe now; reusable Provider Adapter later)
```

Route eligibility is evaluated before price.

Typical filters:

```text
project permission
required inputs
reference behavior
resolution / duration
voice / audio behavior
privacy / rights constraints
benchmark state
route freshness
reliability
```

Only then:

```text
cost
latency
convenience
```

The objective is not “cheapest provider”. It is:

```text
CHEAPEST / BEST-VALUE ELIGIBLE VALIDATED ROUTE
```

---

## 15.1 Derived Approved Route Index

A compact approved-route lookup may exist, but it is a derived view, never an independent authority. Its canonical derivation rule lives in `AI_Media_Provider_Registry (current version resolved by the Current Design Manifest)`; approval/state semantics remain in `AI_Creative_Skill_Execution_Contracts (current version resolved by the Current Design Manifest)`.

---

# 16. Budget and Approval

Every paid action must be inside an explicit approval scope.

Approval can cover a single job, a batch or an authorized budget envelope.

```text
QUOTE
≠
APPROVAL
```

The canonical budget arithmetic, reservation lifecycle and spend-stop semantics are defined in:

```text
AI_Creative_Skill_Execution_Contracts (current version resolved by the Current Design Manifest)
```

The Core requires deterministic enforcement before submission. A Project Profile may impose stricter approval cadence or reserve requirements.

---

### 16.1 Approval Must Bind to What Will Execute

A budget or operation envelope is necessary but not sufficient to prove that a particular plan was authorized. Immediately before paid submission, the Core resolves an immutable canonical execution snapshot and verifies that the applicable approval binds to that exact fingerprint or to a batch template that explicitly permits the child variation.

```text
APPROVED SNAPSHOT / TEMPLATE
≠ CURRENT SNAPSHOT
→ APPROVAL_STALE
→ NO SUBMISSION
```

A monetary cap may remain valid while a concrete execution plan becomes stale.

---

# 17. Job State, Retrieval State and Failover

Provider execution state and asset retrieval state are separate.

The canonical state vocabularies and failover transitions are defined in:

```text
AI_Creative_Skill_Execution_Contracts (current version resolved by the Current Design Manifest)
```

Core invariants:

- an unknown post-submission state must be reconciled before retry;
- a completed provider job with a retrieval failure is retrieved again, not regenerated;
- a provider/policy refusal is not silently bypassed by changing vendors;
- a bad completed output goes to QA/repair diagnosis rather than blind resubmission;
- every route/provider change is recorded and surfaced.

---

### 17.1 Persistence, Concurrency and Cancellation

Persistent state must preserve schema identity/version and reject ambiguous migration rather than reconstructing missing meaning. Mutable current-state writes require revision-aware concurrency control or an implementation-equivalent guarantee against stale overwrite.

Cancellation is asynchronous when the provider cannot prove an immediate stop. `CANCEL_REQUESTED` remains distinct from `CANCELED`; a provider result that completes after cancellation is a late result, not automatic acceptance/delivery.

A state-integrity check runs before resume/execute/deliver when persisted relations may be corrupt or incomplete.

---

# 18. Stop Conditions

The canonical stop vocabulary is defined once in:

```text
AI_Creative_Skill_Execution_Contracts (current version resolved by the Current Design Manifest)
```

The Core requires a stop whenever continuation would violate cost authority, unresolved execution state, policy, project authority, route validity, repair limits, verification requirements or unresolved governance conflict.

A stop must preserve resumable state and expose the blocking condition. Project Profiles may add stricter project-specific triggers without redefining the canonical stop vocabulary.

---

# 19. Progressive Fidelity / Progressive Spend

```text
LOW-COST EXPLORATION
↓
VALIDATION GATE
↓
ACCEPTED INTENT / ASSET
↓
HIGHER-COST MASTER STEP ONLY IF NEEDED
```

The master step can be:

- higher-quality model/route;
- same route at higher quality;
- upscale of the accepted asset;
- deterministic finishing;
- targeted edit.

```text
SAME CREATIVE INTENT
≠
IDENTICAL PROMPT STRING
```

The spec should be recompiled for the chosen master route.

---

# 20. Durable Ingest

Provider result URLs are transport, not archive.

```text
RESULT READY
→ RETRIEVE
→ VERIFY MEDIA READABILITY / TYPE
→ WRITE PROJECT-CONTROLLED COPY
→ HASH / STABLE ID
→ WRITE SIDECAR / INDEX
→ MARK RETRIEVAL VERIFIED
```

A job is not operationally closed merely because a temporary URL exists.

---

## 20.1 Human-Readable Asset Naming

Human-readable physical filenames are convenience metadata, never asset authority. Canonical runtime naming guidance lives in `AI_Creative_Skill_Runtime_Activation_and_Packaging_Pre-v0.3.md`; stable asset identity, hash, lineage and sidecar semantics live in `AI_Creative_Skill_Execution_Contracts (current version resolved by the Current Design Manifest)`.

---

# 21. QA and Repair

QA dimensions depend on media/work profile and the applicable specialist QA methods. Generic dimensions may include:

```text
factual / evidence
authority / identity
product / object fidelity
anatomy / physics
continuity
audio quality
voice identity
spoken-text fidelity
lipsync
performance
typography / legibility
technical file properties
claim-to-visual support
```

Review verdict:

```text
ACCEPTED
REPAIR
BLOCKED
UNVERIFIED
```

Repair principle:

```text
LOCAL DEFECT
→ LOCAL REPAIR
```

Do not regenerate an accepted visual because a controlled text layer is wrong.

Acceptance also depends on inspection coverage. Sampled frames cannot certify motion, pacing, audio or lipsync. When practical, the final creative reviewer should be independent from the sole author/operator. If independent review is unavailable, the review remains useful but must not pretend independence.

Before a retry, record the accepted state at risk and the likely regression surface. The repair route should preserve accepted upstream work and prefer one main causal intervention per diagnostic retry when practical.

---

# 22. Skill Specification ≠ Skill Behavior

A written rule is not evidence that the skill behaves correctly.

Validation ladder:

```text
DESIGN REVIEW
→ STATIC CONTRACT VALIDATION
→ DRY RUN
→ LOW-COST LIVE CANARY
→ OUTPUT QA
→ FAILURE / RECOVERY TESTS
→ REGRESSION
```

## 22.1 Critical Conformance Cases

The detailed test definitions live in the Execution Contracts. The Core requires coverage for at least:

1. batch cost would exceed the authorized cap;
2. provider submission outcome becomes unknown after a possible send;
3. completed job result download fails;
4. provider returns a policy refusal;
5. required project authority/reference is missing;
6. route loses a mandatory capability after planning;
7. wrong-language or systematic output failure repeats;
8. generated output contains unsupported testimonial/review language;
9. offer price or commercial fact conflicts with authority;
10. exact approved text/audio must be preserved;
11. provider swap occurs and must be surfaced/logged;
12. accepted asset has a localized defect that should be repaired without full regeneration;
13. final-resolution review fails after an accepted low-resolution performance;
14. bounded request reaches its requested deliverable and must terminate without adjacent work;
15. a variant batch requests `N` accepted outputs and must distinguish accepted-count target from attempt count while preserving declared invariants and budget limits;
16. a compiled request matches a known failure pattern and must be mitigated or explicitly risk-accepted before paid submission;
17. a costly batch depends on an unvalidated high-risk capability and should run the smallest valid canary before scale;
18. a repair may correct one defect while regressing accepted state and must declare/mitigate that risk;
19. media cannot receive an unconditional acceptance on dimensions that were not actually inspected;
20. an upstream model/version/endpoint/schema disappears or no longer matches a verified execution recipe and must be refreshed/revalidated rather than treated as a creative failure;
21. an async job survives local interruption by recovering the stored provider job identity and retrieving the same result without duplicate paid submission.

The numbered CT matrix and required behavior are canonical only in `AI_Creative_Skill_Execution_Contracts (current version resolved by the Current Design Manifest)`. This Architecture list is a coverage summary, not a second test authority.

Every material real-world failure should become a regression case when it reveals a reusable failure mode.

---

# 23. Runtime Contract

The final runtime is intentionally undecided.

The architecture requires a runtime that can provide, directly or through connected services:

```text
persistent file/state access
secure secret access
HTTP/API/MCP/provider invocation
binary media retrieval
provider job recovery
canonical serialization / hashing
record schema migration
revision-aware mutable-state writes or equivalent concurrency control
state-integrity validation
and either:
  deterministic code execution
or
  an external deterministic state/budget service
```

Possible runtimes may include ChatGPT/Work, Claude/Claude Code, a local/desktop runtime, or a standalone service. Provider execution bindings must not assume one host until implementation chooses it. Concrete Execution Route Recipes are host/runtime-bound only as needed; reusable Provider Adapters remain a later abstraction.

---

# 24. Intended Package Structure

Illustrative target structure, not a requirement to create every file before the first canary:

```text
creative-skill/
├── SKILL.md
├── rules/
│   ├── authority.md
│   ├── budget.md
│   ├── jobs-recovery.md
│   ├── references.md
│   └── authenticity-rights.md
├── projects/
│   └── pilot01.md
├── work/
│   ├── ads.md
│   └── organic.md
├── methods/
│   ├── research/
│   ├── strategy/
│   ├── writing/
│   ├── image/
│   ├── video/
│   ├── audio/
│   ├── design/
│   ├── organic/
│   ├── platforms/
│   ├── execution/
│   ├── qa/
│   └── repair/
├── calibration/
│   ├── exemplars/
│   ├── failures/
│   └── benchmarks/
├── models/
├── providers/
├── routes/                 # concrete Route Recipes created on demand
├── scripts/
│   ├── state
│   ├── budget
│   ├── reconcile
│   └── ingest
└── tests/
    ├── conformance/
    ├── scenarios/
    └── examples/
```

Model/provider/route files are created on demand when implementation or execution requires them. `SKILL.md` remains a thin runtime router; specialist methods and route/provider details are loaded just in time rather than copied into the router.

## 24.1 Future Extension Hooks · NOT CURRENT CAPABILITIES

The current architecture leaves explicit extension points for domains that may later justify dedicated profiles, adapters or registries. Naming an extension hook does not mean the capability is implemented, installed or behavior-validated.

```text
ANALYTICS / DATA-SOURCE CONNECTORS
→ fetch or ingest authorized performance, platform-intelligence, trend or ad-library data
→ separate from media-generation provider adapters

PRODUCT / MARKETPLACE INTELLIGENCE
→ V2.3 reactivation candidate Specialist Method under RESEARCH_ONLY
→ structured interpretation of stable product/listing/seller/variant identity, exact-vs-similar matching, marketplace equivalence confidence and bounded product-demand evidence
→ must reuse generic Research Evidence / Buyer Research semantics rather than duplicate them
→ does not gain contact, negotiation, purchase or supplier-due-diligence authority by implication

SUPPLIER SOURCING / DUE DILIGENCE
→ structured supplier discovery and evidence-based risk/confidence assessment
→ separate domain extension; no quality guarantee and no automatic contact, negotiation or purchase authority
```

If implemented later, these domains must reuse the Core evidence discipline: observed/verified/inferred/unknown states remain distinct, and confidence must not be promoted into guarantee. New registries or profiles are created only when a real execution/control requirement demonstrates the need.

---

# 25. First Implementation Strategy

Implementation starts with evidence, not with building the whole platform. Each canary has one primary question.

## Slice 1A · Basic Execution Canary

Question:

```text
CAN THE SYSTEM SAFELY EXECUTE, INGEST AND ACCOUNT FOR ONE REAL ASSET?
```

Use one external non-Higgsfield static-image route. A synchronous route is acceptable.

Minimum persistent run/state records (**six**):

```text
approval
budget / reservation
Execution Route
attempt / job
asset sidecar / durable ingest
review verdict
```

Required reusable runtime configuration:

```text
Execution Route Recipe
```

The recipe is not a seventh per-run record. It is reusable configuration for the selected Execution Route.

Flow:

```text
ONE SIMPLE PRODUCTION REQUEST
→ ROUTE + FRESHNESS CHECK
→ QUOTE
→ APPROVAL
→ RESERVE
→ SUBMIT
→ RETRIEVE / RECEIVE RESULT
→ DURABLE INGEST
→ LOG / SIDECAR
→ REVIEW
→ COST RECONCILIATION
```

Passing proves basic infrastructure only. It does not prove async recovery, specialist craft, provider parity or complex reference/audio behavior.

## Slice 1B · Async / Recovery Canary

Question:

```text
CAN THE SYSTEM SURVIVE AN INTERRUPTED ASYNC JOB WITHOUT DUPLICATE SPEND?
```

Use one route with a real provider job ID and asynchronous status/retrieval semantics. Validate:

```text
submit
→ provider job identity
→ PENDING
→ poll / resume
→ reconcile after interruption
→ retrieve same job
→ durable ingest
```

The test must demonstrate that an unknown or interrupted local process does not cause blind resubmission.

## Slice 1C · Static Craft Canary

After execution infrastructure passes, validate that the specialist layer improves execution rather than merely adding documents. Use one bounded static task with enough difficulty to exercise:

```text
applicable buyer / evidence basis
→ ads or organic strategy as appropriate
→ image direction
→ typography / layout
→ route compilation
→ evidence/rights QA
→ realism/performance QA
```

Where practical, compare a generic-spec baseline with the specialist-method version using the same route, inputs and rubric. The goal is to test decision quality, not to prove one prompt universally wins. Store defects, trade-offs and repairs as calibration cases.

## Slice 2 · Critical Provider-Independence Test

Later test the actual difficult dependency:

```text
recurring identity
+
PT-BR talking performance
+
required voice identity / exact-audio route
+
lipsync
+
final-resolution acceptance
```

Static generation alone does not prove meaningful independence from a workflow platform.

Canonical test scope, evidence retention and pass/non-proof semantics live in `AI_Creative_Skill_Implementation_Validation_Plan_Pre-v0.3.md`.

# 26. Companion Documents and Version Resolution

The Architecture names **document families and responsibility owners**. It does not maintain a second copy of every current filename/version.

Current versions are resolved exclusively through:

```text
AI_Creative_Skill_Current_Design_Manifest
```

The current manifest is the single design index for:

```text
document family
current version
role
status
supersession / compatibility notes
current Specialist Method versions
```

Companion families include:

```text
AI_Creative_Skill_Project_Profile_Pilot01
AI_Creative_Skill_Work_Profile_Ads
AI_Creative_Skill_Work_Profile_Organic
AI_Creative_Skill_Execution_Contracts
AI_Media_Provider_Registry
AI_Creative_Skill_Specialist_Method_System
AI_Creative_Skill_Calibration_and_Experience_Memory
AI_Creative_Skill_Runtime_Activation_and_Packaging
AI_Creative_Skill_Route_Recipe_Spec
AI_Creative_Skill_Implementation_Validation_Plan
AI_Creative_Skill_Method_Provenance_Map
AI_Creative_Skill_External_Skill_Analysis_Ledger
current Specialist Method families
```

## 26.1 Parent identity versus validation snapshot

A companion may distinguish:

```text
PARENT_DOCUMENT
=
stable document-family identity

LAST_VALIDATED_AGAINST
=
specific parent version against which this document was last checked
```

Legacy fields written as:

```text
PARENT = <versioned filename>
```

must be interpreted as a historical **last-validated-against snapshot**, not as a requirement that the child be version-bumped whenever the parent increments.

```text
NEWER PARENT VERSION
!=
AUTOMATIC CHILD INVALIDATION
```

Revalidation is required when the parent change materially affects an interface, authority rule, contract, state semantic, behavior or responsibility consumed by the child. A pointer-only, index-only, provenance-only or unrelated editorial parent change does not require a child version bump.

## 26.2 Version-bump discipline

Create a new document version when that document's own normative behavior, method, contract, interface, evidence treatment or materially useful content changes.

Do **not** create a new child version solely because:

```text
a parent filename/version changed
another companion advanced independently
the manifest was refreshed
a provenance pointer moved without changing method behavior
```

When only the current-version index changes, update the Current Design Manifest instead of the Architecture or every dependent document.

Responsibility remains:

- Core / Architecture: stable behavior, interfaces and ownership boundaries.
- Project Profiles: project-specific operational policy.
- Work Profiles: work-class intent, evidence and commercial/editorial policy.
- Specialist Methods: domain craft procedure, decision rules, examples and acceptance rubrics.
- Calibration / Experience Memory: scoped causal lessons, benchmark cases, preferences and failure memory.
- Execution Contracts: record/state semantics.
- Provider Registry: volatile provider/model/price/integration facts and scoped route benchmark instances.
- Runtime Activation / Packaging: future skill-discovery, thin-router and overlap/ownership semantics.
- Route Recipe Specification: executable binding format for one concrete route.
- Implementation Validation Plan: canary scope, retained evidence and explicit non-proof boundaries.
- External Skill Analysis Ledger: adjudicated integration decisions after independent analysis and report cross-check.
- Provenance Map: high-level source-to-method lineage.
- Current Design Manifest: current-version resolution only; it is not runtime authority and does not redefine document content.

# 27. Explicit Non-Goals

This design does not automatically:

- launch ad campaigns;
- publish social content;
- contact clients;
- purchase products;
- create real testimonials;
- treat generated stress-tests as real evidence;
- bypass provider/platform refusals;
- spend outside approval;
- declare provider independence before benchmarks pass.

---

# 28. Current Design Decision

```text
NEW CREATIVE SKILL
=
SELF-CONTAINED GOVERNANCE
+
GENERALIST CREATIVE ORCHESTRATOR
+
PROJECT PROFILES
+
WORK PROFILES
+
JUST-IN-TIME SPECIALIST METHODS
+
PROVIDER-AGNOSTIC EXECUTION
+
SPECIALIST QA / REPAIR
+
CALIBRATION / EXPERIENCE MEMORY
+
TRACEABLE LEARNING
+
THIN ACTIVATION / PACKAGING CONTRACT
+
VERSIONED EXECUTABLE ROUTE RECIPES
```

The `/generate` blueprint is treated as a useful lightweight execution pattern, not as the whole creative system. The current design priority is to deepen and behavior-test specialist craft for existing capabilities before adding broad new domains.


---

# 27. V2.3 Reactivation Candidate Delta

This section is additive to the V2.2.1 parent architecture and is not canonical outside the isolated V2.3 candidate branch.

```text
REACTIVATED WORK PROFILE
=
RESEARCH_ONLY

NEW NARROW SPECIALIST CANDIDATE
=
PRODUCT_MARKETPLACE_INTELLIGENCE

NEW TOP-LEVEL ORCHESTRATOR
=
NO

SUPPLIER_SOURCING_DUE_DILIGENCE SPECIALIST
=
NOT CREATED
ABLATED AS UNNECESSARY FOR CURRENT U1/U2 EVIDENCE
```

Cross-profile project flow:

```text
PROJECT PROFILE / CONTINUITY
→ BOUNDED TASK
→ WORK PROFILE OWNER
→ JIT SPECIALIST METHODS
→ AUTHORIZED EXECUTION ROUTE
→ RESULT + EVIDENCE + STATE UPDATE
→ HANDOFF / NEXT TASK
```

Final-deliverable precedence applies:

```text
RESEARCH SUPPORTS ADS
→ ADS OWNS FINAL AD DELIVERABLE

RESEARCH SUPPORTS ORGANIC
→ ORGANIC_CONTENT OWNS FINAL ORGANIC DELIVERABLE

STANDALONE RESEARCH / SYNTHESIS
→ RESEARCH_ONLY OWNS
```

The handoff packet and profile-switch invariants are normative through the V2.3 Execution Contracts candidate.


---

## V2.4 real-world hardening — task guidance without second owner

Stage 0/1 must resolve **deliverable type and scope** (`FULL`, `BOUNDED_PARTIAL`, `DRAFT`) as well as task completion and project continuity. Before each final handoff apply the Manifest-current `Deliverable Completeness Catalog` with the task's narrower method rubrics. A complete deliverable with missing substantive mandatory material must be repaired within scope or marked `PARTIAL/BLOCKED`; neither a remembered template nor a filled heading proves completion.

For meaningful persistent multi-stage projects, recover accepted assets/authority, present a **concise optional next-action guide** after the bounded requested deliverable: completed, pending, recommended next action + value, dependencies, and whether authorization exists. The guide does not execute adjacent tasks. A small direct request omits the guide. The user can skip, reorder or revise creative stages within safe authority; suggestions are not blockers.

`Creative Intent` may produce an exploratory treatment before production script. For multi-beat video prefer iterative concept ⇄ storyboard ⇄ script until accepted, but distinguish storyboard as planning/diagnostic from canonical character/product/environment reference and provider input. Video families are treatment choices (narrative, demo, editorial, motion design, explainer, creator/UGC, hybrids), **not new Work Profiles**. Product medium (physical vs digital) only changes relevant truth constraints (geometry/material/handling vs real UI/function/screens); not the common project/task ownership model.

Pre-production approval is distinct from quote, job authorization, asset acceptance, upscale, publishing and audience performance. The new completeness gate cannot grant any of those authorities.

