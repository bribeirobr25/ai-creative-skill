> **V2.4 CANDIDATE SCOPE:** Modified version of this method family. Read the final section “V2.4 real-world hardening” for current candidate additions. Historical V2.3 discussion and prior-source pointers below remain provenance, not active version resolution.

# AI Creative Skill · Specialist Method · Localized Repair · Pre-v0.12-V2.4-CANDIDATE

## Status

```text
METHOD ID = LOCALIZED_REPAIR
VERSION = Pre-v0.12-V2.4-CANDIDATE
DATE = 2026-10-16
PARENT_DOCUMENT = AI_Creative_Skill_Specialist_Method_System
LAST_VALIDATED_AGAINST = AI_Creative_Skill_Specialist_Method_System_Pre-v0.10.md
STATUS = DESIGN METHOD · NOT INSTALLED
```

This method repairs the smallest causal surface while preserving accepted work. Pre-v0.11 adds a locality/dependency eligibility gate for targeted media edits and explicit post-edit verification of preserved state, so a visually small change is not misclassified as local when it actually reopens action, timing, geometry, contact, occlusion or other coupled dependencies. Existing addressable-feedback, bounded-loop, deterministic-target and shared-temporal-dependency discipline remains in force.

---

# 1. Trigger

Use when an asset is mostly valid but contains a localized defect.

```text
LOCAL DEFECT
→ LOCAL REPAIR
```

Do not default to full regeneration.

---

# 2. Diagnose Before Action

Record:

```text
defect
where / when it appears
likely root cause
what is currently correct
what is at risk if regenerated
available repair surfaces
```

A repair should target cause, not merely add words like "realistic" to a prompt.

## 2.1 Addressable operator feedback resolution

When a repair originates from the canonical Operator Review / Repair Feedback Record in Execution Contracts, preserve the record and item references instead of translating them into an unauditable paraphrase. Resolve the addressed surface before changing anything:

```text
OPERATOR FEEDBACK ITEM
+ UNIT / TIMESTAMP / REGION / SOURCE LOCATOR WHEN AVAILABLE
→ INSPECT / RESOLVE THAT EVIDENCE LOCATION
→ CLASSIFY EXACT EDIT vs SEMANTIC NOTE vs STATUS
→ DIAGNOSE CURRENT DEFECT / AUTHORITY
→ REPAIR THE SMALLEST CAUSAL SURFACE
```

For `EXACT_EDIT`, an explicit before→after or target value may become the deterministic absolute target when it is within current authority, still matches the current artifact/version and does not conflict with stronger Project/Work/Profile constraints. Do not add interpretation where none is needed.

For `SEMANTIC_NOTE`, the note identifies where/what to inspect; it is not yet a repair instruction. Use the targeted evidence to establish the defect and root cause before choosing the surface.

For `STATUS`, preserve review state. An `ACCEPTED` unit is protected by default and must not be touched merely because another unit needs repair.

Prefer stable scene/segment/element/layer identifiers across repair versions where the route supports them. If the identifier changes, keep an explicit mapping or mark the locator unresolved; never silently assume that the same label still names the same unit.

---

# 3. Repair Surface Hierarchy

Prefer the narrowest reliable surface:

```text
word / phrase / clause / sentence when the defect is textual
paragraph / script beat / post-copy unit only when the defect spans that unit
controlled text layer
caption timing
audio layer
voice replacement
lipsync stage
localized image/video edit
color / relight / grade
reframe
single shot regeneration
canonical reference repair
full regeneration only when upstream defect requires it
```

---

## 3.1 Locality / dependency eligibility gate

A defect may occupy a small region while the requested **change** is causally non-local. Before choosing a targeted image/video edit, relight, object swap or similar surface, classify whether accepted surrounding state can remain valid.

```text
TARGETED / LOCAL REPAIR ELIGIBLE
=
requested change is addressable
+ accepted surrounding state can remain valid
+ changed surface does not require coupled action / contact / occlusion / timing / geometry changes outside the target

NONLOCAL DEPENDENCY
→ escalate to the smallest upstream unit that can represent the new state reliably
```

Signals that a nominally local edit may require affected-shot or upstream regeneration include:

```text
underlying action / acting performance materially changes
duration / rhythm / beat order / shot structure changes
new interaction introduces contact or occlusion absent from the source
replacement object changes size / shape / geometry enough to alter surrounding motion or visibility
several coupled elements across the frame must change coherently
requested edit invalidates accepted timing / camera / spatial state outside the addressed region
```

A tool exposing a local-edit control does **not** prove that the requested semantic change is local. Tool capability is subordinate to dependency analysis.

---

# 4. Regression Risk

Before retry:

```yaml
repair_target:
accepted_state:
weakly_anchored_state:
regression_risk:
mitigation:
```

Strengthen anchors where possible before regenerating a stage that can drift.

## 4.1 Addressable accepted-state protection

When accepted state is addressable by scene, segment, element, layer or region, preserve those unit references explicitly.

```text
ACCEPTED SUB-SURFACE
→ PRESERVE BY DEFAULT

CAUSAL REPAIR REQUIRES TOUCHING IT
→ RECORD REOPENING REASON
→ INVALIDATE ONLY THE AFFECTED ACCEPTANCE SCOPE
→ RE-REVIEW THAT SCOPE AFTER REPAIR
```

Do not let a local note silently reopen the whole artifact.

## 4.2 Post-edit preserved-state verification

After a targeted media edit, compare the result against the accepted source/state for the components declared preserved. Use the normal viewing condition required by the medium, and inspect the touched dependency region more closely where necessary.

```text
PRESERVED_COMPONENT
→ verify it still matches the applicable accepted state / authority

TOUCHED OR COUPLED COMPONENT
→ re-review the affected acceptance scope
```

For video this may include, when material, identity, opening/hook, camera path, timing/rhythm, spatial relationships, lighting continuity, speech/audio synchronization and lipsync. Do not accept a provider promise that “everything else stays the same” as evidence; verify the delivered result.

---

# 5. One Main Causal Change

For diagnosis and learning, prefer one primary causal change per retry when practical.

If multiple changes are inseparable, record them explicitly.

For deterministic or parametric repair surfaces, prefer an authoritative **absolute target** when one is known:

```text
"set caption bottom offset to the resolved safe-area target"
>
"move it a little higher"

"match approved reference loudness / declared target"
>
"make it louder"
```

Examples may include timing, position, crop, opacity, gain, loudness target, line break or exact text. The target must come from Project/Work/Profile authority, the accepted reference, the current route/output spec or an explicit operator instruction. Do not invent precision.

When a deterministic repair can be applied without touching accepted media/performance, freeze the unaffected state rather than rerunning upstream generation.


## 5.1 Shared temporal dependency groups

Some finishing surfaces bind several accepted layers to one timing transform, for example a source clip with synchronized captions, overlays or proof markers. When the defect is caused by a **shared** move/trim/speed/duration transform, repair the dependency group atomically when the route supports it.

```text
SHARED TIMING DEFECT
+ SYNCHRONIZED CHILD LAYERS
→ TARGET THE SHARED TEMPORAL TRANSFORM / GROUP
→ PRESERVE CHILD-LEVEL SOURCE EVIDENCE
→ RECHECK THE SYNCHRONIZED RESULT
```

Do not independently retime each child merely because each layer exposes its own timing fields. That can convert one repair into several slightly different timelines.

Keep the distinction explicit:

```text
GROUP-LEVEL DEFECT
→ GROUP-LEVEL REPAIR WHEN RELIABLE

CHILD-SPECIFIC DEFECT
→ CHILD-SPECIFIC REPAIR
```

Source-relative transcript/caption evidence remains source evidence; an edit transform may change display timing without rewriting the original evidence timestamps. The concrete grouping mechanism (`Sequence`, parent timeline node, NLE compound item or equivalent) belongs to the selected finishing route, not to this provider-neutral method.

---

# 6. Protected Components

The repair request should declare:

```text
PRESERVE
VARY / FIX
FORBIDDEN CHANGE
```

Examples:

```text
wrong CTA
→ preserve image
→ replace text layer

correct voice, bad lipsync
→ preserve approved audio
→ repair sync stage

AI/chatbot residue in otherwise approved caption
→ preserve protected facts / terms / disclosure
→ remove or rewrite only the residue

flat color, good performance
→ preserve clip/audio
→ relight/grade
```

---

# 6.1 Text repair and semantic preservation

For copy, caption, subtitle or script repair, identify the exact textual defect before rewriting the surrounding passage.

Use the minimum effective edit. Preserve clear, distinctive material around the defect even if a broader rewrite would make the passage more uniform. Structure, cadence, bluntness, uncertainty, humor or digression should remain when they are valid parts of the intended voice.

```text
TEXT DEFECT AT CLAUSE LEVEL
!=
AUTHORITY TO REWRITE THE WHOLE PARAGRAPH
```

Protected text may include:

```text
exact approved speech
quotes / attribution
names / dates / numbers
price / quantity / offer terms
claim-registry allowed wording
required disclosure / safety language
code / commands / paths / identifiers
```

After the repair, compare before/after meaning. Check that no fact, number, claim scope, ordering, offer term or required disclosure was added, dropped or changed unintentionally.

When the defect originates from a Script or QA text finding, carry the canonical finding by reference:

```yaml
text_finding_ref:
```

`SCRIPT_PERFORMANCE` owns the text-finding fields. This method adds repair planning around the finding rather than copying the finding schema.


If the source is already exact approved/canonical text, naturalness review is diagnostic only unless authority explicitly reopens wording.

---

# 7. Dependent Assets

If the defect is upstream, identify affected dependents.

A wrong canonical product reference may require downstream regeneration. A wrong subtitle should not.

---

# 8. Bounded Review ↔ Repair Loop and Stop

Before the first repair round, resolve and declare:

```yaml
repair_round_limit:
repair_rounds_used:
completion_criteria_ref:
escalation_state:  # NOT_REQUIRED | OPERATOR_REQUIRED | RESOLVED
```

### 8.1 Repair-round limit authority

`LOCALIZED_REPAIR` owns the **resolution rule** for `repair_round_limit`; it does not invent a project-wide optimization target. Resolve the value before automated iterative repair using the strictest applicable bound from:

```text
1. explicit Project Profile repair policy
2. explicit Work Profile repair policy
3. operator / task-specific instruction or approval
4. approval / budget / max-attempt constraints that further cap the plan
```

If none of those authorities supplies a numeric limit, use the conservative execution default:

```text
repair_round_limit = 1
```

That default authorizes one bounded repair attempt under the current repair plan and **does not** authorize a second automatic retry. A further round requires a newly resolved limit or operator decision. This is a governance stop, not a claim that one round is empirically optimal.

Every round must target a named defect and return to the applicable acceptance rubric. Completion means the declared material criteria pass; it does not mean “keep improving”.

Stop paid repair when:

```text
repair round limit reached
budget cap reached
required capability absent
root cause remains unknown after reasonable diagnosis
operator rejects direction
```

If the round limit is reached while a material criterion still fails:

```text
STOP_REPAIR_LIMIT_REACHED
→ preserve resumable state + accepted upstream work
→ set escalation_state = OPERATOR_REQUIRED
→ no automatic extra retry
```

---

# 9. Output

```yaml
repair_plan_id:
source_asset:
operator_feedback_record_ref:
feedback_item_refs:
repair_target_locator:
  unit_ref:
  time_ref:
  spatial_ref:
  source_locator_ref:
defect:
root_cause:
repair_surface:
locality_assessment:  # LOCAL_ELIGIBLE | NONLOCAL_DEPENDENCY | UNCERTAIN
coupled_dependencies:
repair_dependency_group_ref_if_applicable:
shared_temporal_transform_target_if_applicable:
primary_change:
absolute_target_or_ref_if_applicable:
preserved_components:
preserved_state_verification:
accepted_state_at_risk:
reopened_accepted_units:
regression_mitigation:
affected_dependents:
operation:
acceptance_check:
repair_round_limit:
repair_rounds_used:
completion_criteria_ref:
escalation_state:
text_finding_ref:
protected_text_refs:
semantic_fidelity_check:
change_delta_summary:
```


When wording changes materially, `change_delta_summary` should state what changed and what was intentionally preserved. It is an audit/provenance aid, not an unsolicited offer for additional work.


---

## V2.4 real-world hardening — failure containment for real video edits

Before editing a user-approved video, determine whether the actual execution route can guarantee `protected_dimensions` (frame region, camera, background, audio, timing). A provider `video_edit` option does NOT prove localized or pixel-preserving modification. If preservation is unsupported or `UNKNOWN`, mark as risky regeneration and offer crop, trim, compositing, or deterministic overlay (when authorized) before consuming another paid edit.

Specify exact target change; run pre/post comparison on both modified surface and protected remainder, including sound; if the provider changed an unrelated camera angle/character identity, the edit FAILS and must not be delivered as repaired. User's approval of creative imperfections does not automatically authorize further attempts/spend.

