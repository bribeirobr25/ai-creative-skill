> **V2.4 CANDIDATE SCOPE:** Modified version of this method family. Read the final section “V2.4 real-world hardening” for current candidate additions. Historical V2.3 discussion and prior-source pointers below remain provenance, not active version resolution.

# AI Creative Skill · Specialist Method · Route Compilation · Pre-v0.14-V2.4-CANDIDATE

## Status

```text
METHOD ID = ROUTE_COMPILATION
VERSION = Pre-v0.14-V2.4-CANDIDATE
DATE = 2026-10-16
PARENT_DOCUMENT = AI_Creative_Skill_Specialist_Method_System
LAST_VALIDATED_AGAINST = AI_Creative_Skill_Specialist_Method_System_Pre-v0.11-V2-CANDIDATE.md
STATUS = DESIGN METHOD · NOT INSTALLED
```

GPT validation hardening branch (2026-10-10): Pre-v0.13-V2-CANDIDATE consumes scoped reference locators and produces the immutable canonical execution snapshot/fingerprint required by the V2 candidate Execution Contracts. It also makes approval freshness a final pre-submit compile gate; route/provider/model or creative-spec changes cannot ride on an approval for another execution snapshot.


This method converts provider-neutral production intent into a route-native execution request without silently changing the creative job. Validator correction round (operator-agreed window, 2026-10-09): Pre-v0.12 removes `authoritative_dimensions` as a separate reference-binding field (merged into `protected_dimensions`, accepted as an alias) and declares the preserve/change correspondence with Localized Repair §6; replaces "control reference" and "composition-map labels" with the canonical `COMPOSITION` reference (labels) role; and merges the pre-render checks that §10.1 repeated between its G3 and G4 additions (duration vs output contract, counts, reference scope/unused context), moving the "as above" context check out of OUTPUT / FORMAT into REFERENCES / COMPOSITION as the lint form of §7.1. No other behavior changes. Pre-v0.11 adds explicit coercion-sensitive parameter semantics so provider-side adjustments cannot silently mutate hard output requirements. Pre-v0.10 execution-context minimization, preserve/change bindings and deterministic pre-render lint remain in force.

---

# 1. Trigger

Required before provider/model execution when a generic production spec must be mapped to a concrete route.

```text
GENERIC CREATIVE SPEC
≠
READY PROVIDER REQUEST
```

---

# 2. Inputs

```text
production spec
Production Request.output_requirements
Project / Work Profile authority
specialist method outputs
Execution Route Contract
Execution Route Recipe
model spec
reusable Provider Adapter when implemented
current Registry facts
reference bindings, including reference_scope / locator
presentation mode
audio binding contract
auxiliary audio requirements
exact text requirements
approval / budget
known failure memory
```

---

# 3. Compilation Sequence

```text
1. IDENTIFY THE PRODUCTION JOB
2. EXTRACT HARD INVARIANTS / FORBIDDEN ELEMENTS
3. READ MODEL CAPABILITIES / LIMITS
4. RESOLVE EXECUTION ROUTE RECIPE + VERIFY FRESHNESS
5. READ ROUTE / PROVIDER INPUT SCHEMA
6. MAP REFERENCE ROLES
7. MAP AUDIO / SPEECH REQUIREMENTS
8. RESOLVE FINAL OUTPUT / DELIVERY REQUIREMENTS
9. CHECK DURATION / RESOLUTION / ASPECT LIMITS
10. DECOMPOSE UNSUPPORTED COMBINATIONS
11. ADAPT PROMPT STRUCTURE TO THE ROUTE
12. MAP PARAMETERS
13. COMPILE CHEAP PRE-RENDER VALIDATION GATES WHEN SUPPORTED
14. CHECK KNOWN FAILURES
15. VERIFY COST / APPROVAL BINDING
16. SNAPSHOT EXECUTION PARAMETERS / RECIPE VERSION
17. PRODUCE EXECUTION SPEC
```

Do not start from a vendor and work backward to a creative job.

---

# 4. Execution Route Recipe / Freshness Gate

Before route-native compilation, resolve the concrete recipe/binding for the selected route.

Required checks:

```text
Execution Route Recipe exists for the selected executable route
recipe state is VERIFIED or explicitly authorized for canary use; current Execution Route freshness from the Registry is FRESH or explicitly refreshed for the canary; the recipe validation snapshot is compatible with that current state
model/version still exists
endpoint/invocation surface still exists
request/response schema is current enough to submit
required reference/audio/text inputs remain supported
result retrieval path is known
route-specific execution limits are available when material
```

If the recipe is `STALE` or `INVALIDATED`, compilation must not silently proceed as if it were current. Refresh/revalidate, choose another eligible route, or stop according to the normal routing/approval boundary.

```text
EXECUTION ROUTE RECIPE
≠
CREATIVE AUTHORITY
```

The recipe does not decide what the creative should be. It only exposes how the selected route can currently receive and return the already-authorized job.

---

# 5. Same Intent ≠ Same Prompt

```text
SAME CREATIVE INTENT
≠
IDENTICAL PROMPT STRING
```

Different models may require different:

```text
prompt order
reference count
reference roles
negative constraints
camera syntax
speech placement
first/last-frame strategy
parameter mapping
segmentation
```

The compiler preserves intent and authority, not literal prompt text.

---

# 6. Capability Mismatch

If the route cannot satisfy a hard requirement:

```text
DO NOT OMIT IT SILENTLY
```

Options:

```text
select another eligible route
decompose into multiple stages
move exact text to finishing
move voice to replacement stage
split duration
stop for route invalidation
```

The chosen decomposition must preserve the user's completion condition.

---

# 7. Reference Compilation

For each reference, compile the smallest explicit binding the route needs:

```yaml
reference_ref:
reference_mode_or_role:
subject_group_ref:          # optional; multiple views/assets may represent one semantic subject
allowed_authority:
allowed_inheritance:
excluded_inheritance:
protected_dimensions:         # optional; especially source-media / `COMPOSITION` references; dimensions that must remain source-faithful
allowed_changes:              # optional; changes explicitly authorized against the source
required_new_interactions:    # optional; contact/occlusion/light/physics additions that must integrate coherently
end_state_requirements:       # optional
scene_or_stage_scope:       # optional; bind only where the reference is actually needed
route_native_binding_or_handle:
```

`allowed_inheritance` says what the route may carry from the reference. `excluded_inheritance` says what must **not** leak from it. Examples include using a character reference for identity/clothing without inheriting its background or lighting, or using a motion/audio source only for the authorized motion/audio dimension. These are authority/scoping constraints, not prompt-decoration fields.

`protected_dimensions` also carries what earlier versions called `authoritative_dimensions`; the old name is read as an alias, not a separate field. Correspondence with Localized Repair §6: `protected_dimensions` = PRESERVE; `allowed_changes` = VARY / FIX; any change not declared in `allowed_changes` = FORBIDDEN CHANGE.

Provider handles do not become project authority. A route that cannot express or reliably preserve a required inheritance boundary must surface that limitation, decompose the job, or use another eligible route rather than silently broadening reference authority.

Multiple views of the same subject may retain distinct asset IDs while sharing one `subject_group_ref`. This prevents view count from becoming false subject count. For complex scenes, bind only the references required by the relevant scene/stage where practical rather than dumping every available reference into every generation.

Reference overload should be reduced by assigning one clear role per reference where practical.

Scoped external-method heuristic:

```text
IF exact identity / logo fidelity is required
AND an authoritative permitted reference exists
AND the selected route supports that reference correctly
THEN prefer explicit reference binding over textual reconstruction
```

This is not a universal rule and is not `PROJECT_EMPIRICAL` merely because an external guide recommends it. Project restrictions, contamination risk and route behavior may override it.

## 7.1 Execution-context minimization

Compile each execution unit with the **smallest authorized context needed to execute that unit correctly**.

```text
EXECUTION CONTEXT
=
REQUIRED AUTHORITY + REQUIRED REFERENCES + REQUIRED CONTINUITY
!=
RAW PROJECT ARCHIVE
!=
ACCIDENTAL CHAT MEMORY
```

Applicable rules:

```text
- do not rely on “as above”, implicit prior scene memory or an unbound earlier conversation state
- do not attach subjects/references that are irrelevant to the current execution unit
- if the route intentionally supports continuation/context carry, bind that continuation source explicitly
- preserve stable project IDs/authority even when the provider requires temporary handles
- source-media bindings must declare what the source controls, what is protected and what is allowed to change
```

This is a compilation boundary, not a ban on multi-shot or continuation routes. A validated route may carry context when the carry itself is explicit and scoped.

---

## 7.2 Scoped-Reference Compilation

For `SEMANTIC_REGION`, `SPATIAL_REGION`, `SUBJECT` or `PANEL` bindings, compile only the declared surface/meaning into the route request. If the route cannot address the required scope reliably, either create an authorized derived reference/crop or mark capability mismatch. Do not downgrade the binding to `WHOLE_ASSET` merely because the provider API is simpler.

**Mandatory derived crops (2.6).** When the target route cannot bind a reference to a region or role (for example GPT Image inside a chat GPT, which receives whole attached images), the derived crop is not optional:

- one product per reference; crop away third-party brands, props, cosmetics, hands and phone/UI overlays wherever a rectangle allows;
- whatever cannot be cropped without cutting the product is named in the prompt as "not part of the product";
- each crop records its role, what it may control, what it must not pass on, and its parent photo with the crop box;
- rectangular crop only: no retouching, resampling or pixel edits; the parent photo stays the authority and the crop adds nothing.

Evidence: in a blind review of two prompt packs for the same real product photos, the pack with one-product crops scored 4/5 on reference selection against 2/5 for uncropped photos carrying third-party brands and overlays (`docs/research/photoshoot-prompts-skill-vs-manual-2026-10-21.md`).

---

# 8. Prompt Collision Check

Before submission detect:

```text
contradictory instructions
duplicate exact speech
hard invariant vs style conflict
camera vs action conflict
duration vs speech conflict
reference conflict
exact-audio requirement unsupported by route
excess simultaneous actions
unresolved delegated creative choice that can violate authorized intent
physical-property contradiction, such as requiring a rigid object to deform unless that deformation is intentional
route parameter vs prompt duplication/conflict for the same controlled dimension
unnecessary negative prompt lists
```

Remove redundant instructions rather than merely adding more text.

Delegated phrases such as “whatever looks best”, “add more if it looks better” or “pick the coolest angle” are not automatically invalid, but they are a collision when the project already has authoritative subject count, composition, proof, continuity or camera requirements that the delegation could override. Compile the resolved choice instead of outsourcing authority back to the model.

When the selected, **validated** route exposes a native parameter that owns a camera/light/lens or similar dimension, map that authoritative dimension to the parameter and remove redundant prose when duplication can create conflict or attention dilution. Do not prefer a vendor parameter merely because a tutorial claims it is stronger; route evidence must justify the mapping.

Low-information quality/style tokens are not globally banned. Flag or remove them when they crowd, contradict or obscure material executable constraints rather than because a third-party tutorial labels them “bad prompts”.

---

# 9. Known-Failure Preflight

Consult route/model failure memory.

A mitigation becomes a hard compilation rule only when its scope and evidence justify it.

Examples:

```text
repeated wrong-language behavior
reference contamination
prompt duplication causing speech repetition
identity drift under a framing pattern
provider-specific text rendering weakness
```

---

# 10. Execution Spec Output

```yaml
execution_spec_id:
production_request_ref:
execution_snapshot_ref:
execution_fingerprint:
canonical_serialization_version:
approval_binding_ref:
route_id:
route_recipe_ref:
route_recipe_version:
current_route_freshness_state:
route_freshness_checked_at:
recipe_validated_against_route_freshness:
compiled_prompt_or_instructions:
parameter_map:
parameter_snapshot_ref:
coercion_sensitive_parameters:
coercion_policy:
reference_bindings:
  # each binding may carry reference_ref / role / subject_group_ref /
  # allowed_inheritance / excluded_inheritance / protected_dimensions /
  # allowed_changes / reference_scope / reference_locator / scene_or_stage_scope
audio_mapping:
text_mapping:
segmentation_plan:
resolved_output_requirements:
pre_render_validation_gates:
post_processing_plan:
hard_invariants:
forbidden_elements:
known_failure_checks:
unsupported_requirements:
acceptance_criteria:
```


## 10.1 Resolved output contract and cheap pre-render gates

`ProductionRequest.output_requirements` is the requested/authorized delivery requirement entering compilation. `ExecutionSpec.resolved_output_requirements` is the route-valid realization produced after resolving Project/Work/Profile authority, the selected route recipe and current route constraints.

```text
ProductionRequest.output_requirements
→ ROUTE COMPILATION
→ ExecutionSpec.resolved_output_requirements
```

Compilation must make the final delivery surface explicit when it is material. Do not invent a generic export preset or silently replace a project requirement with a vendor default.

```yaml
resolved_output_requirements:
  duration_or_timing_ref:
  aspect_ratio_or_dimensions:
  frame_rate_if_material:
  container_or_delivery_format:
  codec_or_compatibility_constraints_if_required:
  alpha_or_transparency_if_required:
  audio_inclusion:
  route_output_constraints:
```

`route_output_constraints` describes what the selected route can or must output; it is not a validation checklist. `pre_render_validation_gates` describes cheap checks that can fail before a costly/full render. Keep these concepts separate.

### Provider-coercion boundary

When the selected route is known to coerce/adjust submitted values, mark every material hard field that must survive unchanged, for example duration, aspect/dimensions, resolution/quality, reference count/role or another Project/Work requirement.

```yaml
coercion_sensitive_parameters:
  - aspect_ratio
  - duration
coercion_policy: HARD_MISMATCH_REQUIRES_REPLAN_OR_REAUTHORIZATION
```

Compilation owns the requested/resolved intent; execution owns the provider-effective observation. If the provider later reports an adjustment, the attempt must reconcile it against these fields before acceptance. Do not compile a provider default as if it were the user's/project's requirement.

When the route supports inexpensive linting, static checks, representative-frame previews or other deterministic validation before the costly/full render, compile those checks as **pre-render gates**. They may catch layout, missing-asset, text, timing or configuration failures early.

For timed, multi-shot or reference-dense work, applicable cheap gates may include:

```text
TIMING
- declared windows are ordered and contiguous when the spec requires contiguity
- no unintended gap/overlap exists
- final timed window and route/page duration parameter agree with the compiled timing contract and with the duration in `resolved_output_requirements`

SPEECH / AUDIO
- each exact spoken line has one canonical execution location unless the validated route explicitly requires duplication
- a line assigned to a bounded window is plausibly compatible with that authoritative/measured window
- speech text, timing evidence and route-native speech placement do not contradict one another

REFERENCES / COMPOSITION
- every required reference binding resolves to an approved/authorized asset
- each execution unit carries only references/context with a declared role and scope in that unit (§7, §7.1): no reference merely because it exists in the project, no unused bound context, and no dependency on unbound “as above” / accidental prior-chat context
- declared shot / beat / subject counts agree with the actual compiled set when that set is deterministically inspectable; independently of that condition, semantic subject counts, `COMPOSITION` reference labels and `subject_group_ref` relationships do not create false extra subjects
- required repeated-item counts agree with the compiled composition contract
- text instructions do not contradict authoritative scale / position / trajectory bindings
- attributes are attached to the intended semantic entity when this is statically detectable
- a source-media binding has explicit protected dimensions and allowed changes when source fidelity is material
- any claimed shared block / invariant reused across units is actually identical where exact reuse is part of the contract

OUTPUT / FORMAT
- aspect ratio and frame rate do not contradict `resolved_output_requirements` (duration is checked under TIMING)
- declared format/cut mode agrees with the compiled unit structure when the route exposes that distinction

CONTROL OWNERSHIP
- route-native camera/lens/light/duration parameters and prose do not issue competing instructions for the same dimension
```

These are conditional checks, not a universal provider syntax. A route that cannot represent a requested exact timing or reference boundary must surface that limitation rather than passing lint by pretending it can.

Final-artifact acceptance semantics are owned by `QA_REALISM_PERFORMANCE`; a pre-render gate result is diagnostic/preventive evidence, not the final creative verdict. Deterministic compositing/finishing may be one execution surface within the current route stack; its existence does not by itself require a separate Specialist Method.

---

## 10.2 Canonical Execution Snapshot / Approval Gate

After route-native request compilation and deterministic lint, resolve the canonical immutable execution snapshot through Execution Contracts.

```text
COMPILED REQUEST
→ CANONICALIZE
→ EXECUTION FINGERPRINT
→ COMPARE WITH APPLICABLE APPROVAL / BATCH TEMPLATE
→ ONLY THEN SUBMISSION ELIGIBILITY
```

A material difference in route/provider/model, references or revisions, claims/evidence, exact text, locale/market/jurisdiction, output count, duration, resolution/aspect, prompt/spec or other protected execution semantics requires a new fingerprint and may make prior approval stale. Non-semantic logging/filename changes do not.

---

# 11. Acceptance Rubric

Compilation passes when:

```text
all hard requirements have an explicit execution location
material requested output requirements are transformed into explicit `resolved_output_requirements` rather than inherited from vendor defaults; coercion-sensitive hard fields are identified so provider-effective adjustments cannot be silently accepted
applicable cheap pre-render gates are compiled without being confused with final acceptance
timing/speech/reference/count/duration/output-contract checks are applied when their contracts are material and representable
execution units contain only required/scoped context and do not rely on accidental prior-chat memory
source-media bindings preserve declared protected dimensions while exposing allowed changes
no required authority disappeared
route-native syntax/parameters are valid enough for submission
current Execution Route freshness and the Recipe validation snapshot were both resolved and retained in provenance
parameter snapshot can be recovered for audit/reproduction
canonical execution snapshot + fingerprint were produced and the applicable approval/batch-template relation is current at submission eligibility
known failure patterns were checked
unsupported requirements are surfaced
creative intent remains unchanged
```

A shorter route-native prompt can be better than a literal transcription of the generic spec.

---

# 12. Compilation vs Execution Mechanics

```text
ROUTE COMPILATION
=
map authorized creative intent into route-native instructions / parameters

EXECUTION ROUTE RECIPE
=
invoke the selected route correctly
```

A compiler may produce a valid execution spec without itself performing the HTTP/MCP/UI call. A recipe may know an endpoint perfectly while having no authority to alter creative intent. Keeping these separate prevents provider mechanics from leaking backward into strategy and craft.


---

## V2.4 real-world hardening — semantic-preserving narrative vs technical compilation

Compile requested `VIDEO_CREATIVE_DIRECTION` into an eligible model-specific representation while preserving creative invariants and open zones. Continuous narrative is preferred for routes demonstrated to perform coherent drama; do not forcibly produce timestamps merely because a model accepts them. A different route requiring exact UI cuts/lipsync must receive measured timing. Provider selection may not override narrative owner, product identity, canonical characters, reference role/authority or approval. Report inability to preserve a mandated dimension before spending.

For real/digital product scenes verify product truth before compiling; do not invent functionality/visual UI states or recast an exact product name as visual similarity. Preserve submitted reference manifests, model/mode, actual prompt, quoted parameters, and provider-effective output as separately evidenced facts.

