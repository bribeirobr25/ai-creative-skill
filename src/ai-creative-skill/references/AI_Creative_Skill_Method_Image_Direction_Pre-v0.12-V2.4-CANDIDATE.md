> **V2.4 CANDIDATE SCOPE:** Modified version of this method family. Read the final section “V2.4 real-world hardening” for current candidate additions. Historical V2.3 discussion and prior-source pointers below remain provenance, not active version resolution.

# AI Creative Skill · Specialist Method · Image Direction · Pre-v0.12-V2.4-CANDIDATE

## Status

```text
METHOD ID = IMAGE_DIRECTION
VERSION = Pre-v0.12-V2.4-CANDIDATE
DATE = 2026-10-16
PARENT_DOCUMENT = AI_Creative_Skill_Specialist_Method_System
LAST_VALIDATED_AGAINST = AI_Creative_Skill_Specialist_Method_System_Pre-v0.12-V2.2-CANDIDATE.md
STATUS = DESIGN METHOD · NOT INSTALLED
```

GPT validation hardening branch (2026-10-10): Pre-v0.10-V2-CANDIDATE formalizes scoped composite references (`WHOLE_ASSET | SEMANTIC_REGION | SPATIAL_REGION | SUBJECT | PANEL`) and separates visible/reference text from display authority and factual claim evidence. This resolves the moodboard/multi-panel ambiguity found in behavioral simulation without broadening any reference authority.

Z4/Z4.1 creative-balance hardening branch (2026-10-11): Pre-v0.11-V2.2-CANDIDATE consumes task-relative creative latitude so character/product/environment/art-direction continuity can remain stable while camera, composition, lighting, focus, blocking and concept are explored only where authorized. It also makes canon anchoring explicit for longitudinal visual work.


This method defines professional still-image direction before route-specific prompt compilation. Validator correction round (operator-agreed window, 2026-10-09): Pre-v0.9 adds a pointer to project reference restrictions (the active Project Profile; pointer in §10), including their precedence over the §9.1 brand-mark rule; makes the `COMPOSITION` map scope explicit (default stations / arrangement / counts / clearance; relative scale and trajectory only when the map is authoritative for them), prefers color/shape over letters/numbers, keeps map text out where the project forbids readable text in generation references, and binds map marks/colors/labels to `excluded_inheritance`; adds the foreground-obstruction check to recurring-environment readiness; makes the output count check apply whenever a count is material, not only in multi-region/layout jobs; aligns the aggregate coverage name (`overall_state`) between §5.1 and §6.1; clarifies that §11.1 `item labels` are semantic identity, with rendered labels following §9 and project text policy; and names `subject_group_ref`. Pre-v0.8 renumbered the former §10.3 "State-specific derived references" to §10.4 when §10.3 "Extracted visual-rule evidence state" was inserted; that renumbering is declared here. No other behavior changes. Pre-v0.8 adds evidence-state labels for extracted visual rules and deterministic preservation of approved official brand marks when generative re-rendering is unnecessary. Pre-v0.7 composition, state-specific derived-reference and identity-reference-readiness semantics remain in force.

---

# 1. Trigger

Use for:

```text
final static ads
organic stills
product sheets
character sheets
environment plates
video start frames
reference images
localized image repair
```

---

# 2. Start With the Job

Before visual styling, define:

```text
asset purpose
primary message / role
visible evidence
primary identity authority
placement / aspect
hard invariants
flexible choices
forbidden content
reference roles
text mode
planned action space
```

A beautiful image that fails the asset's job is not accepted.

---

## 2.1 Visual Identity / Continuity vs Expression

Resolve visual dimensions through the current task's `creative_latitude_ref` rather than assuming that a modality-wide list is always preserved or always variable.

Examples only:

```text
IDENTITY / CONTINUITY-BEARING IN SOME TASKS
→ recurring character identity
→ verified product truth
→ recurring environment geography
→ canonical art style / palette when locked
→ wardrobe or light state when the current scene/sequence makes them continuity-critical

EXPRESSION-BEARING IN SOME TASKS
→ camera angle / distance / lens feel
→ composition / foreground strategy
→ blocking / pose
→ focus behavior
→ lighting treatment when not continuity-locked
→ visual metaphor / concept
```

The same dimension may change role by task. Lighting can be `PRESERVE` inside one continuous scene and `OPEN_EXPLORATION` for a new concept. Wardrobe may be free for a one-off ad and canonical for a recurring character.

Explicit user instructions narrow only the named legitimate dimensions. `Be creative with camera` does not loosen character identity, product truth, claims or rights. `Keep the same lighting` does not freeze unrelated composition choices.

For longitudinal visual work, anchor identity-bearing dimensions to current canonical/approved references. A previous accepted frame may supplement continuity when Project authority permits it, but a chain of generated derivatives must not silently replace the original identity/world authority.

```text
SAME IDENTITY / WORLD
+
NEW EXPRESSION
=
VALID TARGET

SAME EVERYTHING
!=
STRONGER CONSISTENCY BY DEFAULT
```

---


# 3. Spatial Map

Describe the scene in observable spatial terms.

For each important subject/object:

```text
left / center / right
foreground / midground / background
apparent scale
orientation
visibility
relationship to other objects
support / contact surface
overlap
negative space
```

The model should not have to invent the hierarchy from adjectives alone.

---

# 4. Occupancy and Hierarchy

Determine:

```text
what dominates first glance
how much frame it occupies
what must remain unobstructed
where action/copy needs space
what secondary objects are actually necessary
```

Do not add decorative clutter that competes with product, face, proof or CTA.

---

# 5. Product Truth

For physical products, use a structured truth pack where available:

```text
shape
proportions
materials
finish
hardware
labels / logo placement
color variant
packaging
included items
excluded items
verified visible features
```

Do not invent internal compartments, accessories, packaging or material properties.

## 5.1 Product-reference readiness

When a product must remain materially consistent across several assets, views or downstream motion units, resolve whether the available product references actually establish the visible truth required by the current task. A single attractive front view is not automatically sufficient for a rear, sole, underside, opening, side-panel or packaging-dependent shot.

```yaml
product_authority_ref:
product_reference_refs:
product_reference_coverage:
  required_views_or_surfaces:
  geometry_and_proportion:      # ADEQUATE | PARTIAL | MISSING | NOT_REQUIRED
  label_logo_placement:         # ADEQUATE | PARTIAL | MISSING | NOT_REQUIRED
  material_finish:              # ADEQUATE | PARTIAL | MISSING | NOT_REQUIRED
  color_variant:                # ADEQUATE | PARTIAL | MISSING | NOT_REQUIRED
  packaging_or_inclusions:      # ADEQUATE | PARTIAL | MISSING | NOT_REQUIRED
  overall_state:                # ADEQUATE | PARTIAL | MISSING | NOT_REQUIRED
```

Coverage is task-relative. Use only the fields needed to judge whether the current requested view/state is anchored; do not manufacture a full technical sheet when one verified view is enough.

Multiple images or panels may represent **one semantic product**. Preserve that relationship into Route Compilation through the existing subject grouping/reference-binding semantics (`subject_group_ref`, Route Compilation §7) rather than treating each view as a separate product identity.

```text
MULTI-VIEW REFERENCE PACK
=
MORE COVERAGE OF ONE AUTHORIZED PRODUCT WHEN THE ASSETS ACTUALLY AGREE

MULTI-VIEW REFERENCE PACK
!=
MANDATORY FOUR-VIEW SHEET
!=
PERMISSION TO INVENT UNSEEN PRODUCT SURFACES
```

For a real product, derived reference sheets must remain grounded in verified product authority. If an unseen surface is not established, mark coverage partial/missing, change the shot, obtain better authority or keep the uncertain surface out of material product claims.

**Declared vs observed (2.6).** A product fact declared by a brief, caption or metadata file that the reference photos contradict is a conflict to resolve with the owner before use, never a fact. Until resolved, prompts describe only what the photos show and mark the declared detail unknown. Observed failures: a lining declared "with small dots" that the interior photos show plain; a hair clip used as a prop recorded as an "applied flower" of the product, which a website executor then published as a product detail.

---

# 6. Character Realism

Where people appear, specify observable posture/action rather than vague mood alone.

Check:

```text
body balance
hand-object contact
finger placement
face / gaze
age consistency
wardrobe authority
skin/material realism
relationship to product / scene
```

Random skin texture, grain or blur is not a substitute for realism.

## 6.1 Recurring-character reference readiness

When a recurring character/persona must remain recognizable across assets, resolve the usable identity-reference pack before generation rather than treating one attractive portrait as automatically sufficient for every downstream view.

```yaml
identity_authority_ref:
identity_anchor_refs:       # small canonical visible traits resolved from project/persona authority
reference_coverage:
  face_detail:              # ADEQUATE | PARTIAL | MISSING | NOT_REQUIRED
  full_body_proportion:     # ADEQUATE | PARTIAL | MISSING | NOT_REQUIRED
  profile_or_angle:         # ADEQUATE | PARTIAL | MISSING | NOT_REQUIRED
  wardrobe_or_styling:      # ADEQUATE | PARTIAL | MISSING | NOT_REQUIRED
  visible_anchor_coverage:  # ADEQUATE | PARTIAL | MISSING
  overall_state:            # ADEQUATE | PARTIAL | MISSING | NOT_REQUIRED
```

`overall_state` is the aggregate coverage verdict for the required view/state, with the same name and values as in §5.1. `visible_anchor_coverage` is one dimension of that verdict (whether the resolved `identity_anchor_refs` are visibly established), not a second aggregate.

Coverage is task-relative. Do not require a profile, full body or any fixed panel layout when the current asset does not need it. Conversely, do not claim a reference is ready for a required angle/body state that it does not actually establish.

`identity_anchor_refs` are consumed from Project/Profile/canonical identity authority. They are consistency aids, not a replacement for the authoritative identity source and not an invitation for the method to invent new permanent traits. Where an anchor definition or wording is canonical, preserve its meaning consistently across derivatives; route-native compilation may change syntax, but may not silently change the identity trait.

When a reference sheet/panel contains **multiple visible instances of the recurring identity**, those instances must not materially disagree about the identity being locked. If conflicting faces/body traits are present, repair, simplify or reject the reference before it becomes an identity anchor.

A route or production may choose a single visible face source as a contamination-reduction tactic, but this is **not a universal panel law**. The provider-neutral requirement is one coherent identity authority, not “headless body panels” or any fixed layout.

```text
REFERENCE COVERAGE
=
WHAT THE CURRENT AUTHORITY ACTUALLY ESTABLISHES

REFERENCE COVERAGE
!=
MANDATORY THREE-PANEL / PROVIDER-SPECIFIC CHARACTER SHEET
```

## 6.2 Task-relative recurring-identity challenge canary

Reference coverage states what the current authority establishes. It does not by itself prove that a recurring identity remains robust across every view/state the upcoming production will require.

```text
INPUT REFERENCE COVERAGE
!=
PROVEN ROBUSTNESS ACROSS REQUIRED HARD VIEWS
```

When recurring identity is high-risk and the asset will scale across many downstream outputs, Image Direction may request a **task-relative challenge canary** through the existing Calibration mechanism before expensive scale. Stress only states that matter to the actual job, for example profile, high/low angle, wider framing, materially different lighting or a motion-start frame when those conditions are expected downstream.

Compare canary results against stable `identity_authority_ref` / approved anchors, not merely against the previous generated derivative. The number of attempts, exact views and acceptance threshold come from current task risk, budget and Calibration authority. Do not import a universal 8–12 generation rule, fixed landmark metric or provider-specific identity system.

---

# 7. Camera and Perspective

Define only what materially affects the image:

```text
camera height
view angle
focal feel / perspective
subject distance
crop
product plane / face visibility
```

Avoid impossible mixed perspective or dramatic lens effects that distort the product or face.

---

# 8. Light, Local Color and Materials

Lighting should have a plausible source and support the commercial/creative hierarchy.

Specify:

```text
key direction
soft/hard quality
fill / contrast level
material reflections
local product colors
background relationship
```

Preserve clean middle tones when the objective requires readable product/material information.

Avoid using aggressive grading to hide weak geometry or artificial materials.

When an identity/character reference and the target environment come from different lighting conditions, do not silently inherit the reference image's studio/key/background illumination into the scene. Unless Project authority explicitly says otherwise, the target environment / scene authority resolves the final lighting. Re-light the subject so key/fill direction, local color response, contact shadow and plausible surface bounce/interaction make the subject physically belong in the target scene.

```text
IDENTITY REFERENCE
→ MAY CONTROL IDENTITY / AUTHORIZED APPEARANCE

IDENTITY REFERENCE LIGHTING
!=
SCENE LIGHTING AUTHORITY BY DEFAULT
```

Do not turn this into one fixed lighting recipe. The requirement is coherent authority and physical integration, not a mandatory key/fill ratio or a source-specific studio setup.

---

# 9. Text Modes

Separate:

```text
PHOTOGRAPHIC / SCENE CONTENT
PHYSICAL TEXT IN THE WORLD
CONTROLLED GRAPHIC / OVERLAY TEXT
```

Exact copy that matters should normally use controlled finishing unless the selected route has validated text fidelity for that task.

Do not inherit text/logo from a style reference accidentally.

---

## 9.1 Official brand-mark preservation

When an official logo/brand mark is supplied as authority, changing scene, size, position or background does not authorize the image model to redraw it. Prefer deterministic placement/compositing when the mark can remain a flat graphic. Use generation for physically interacting treatments only when that interaction is requested and the selected route can preserve the approved mark adequately.

```text
OFFICIAL BRAND MARK
→ preserve spelling / geometry / proportions / approved color variant
→ deterministic placement when physical interaction is unnecessary
```

Embossing, foil, engraving or one-color reproduction must use an approved suitable variant or explicit authority; do not let the model invent a new logo variant. Repeated generation failure is a reason to move the mark to a controlled finishing layer, not to accept drift.

**Marks applied on the product (2.6).** Woven or printed labels, tags and stitched marks follow the same rule. Image models render a label correctly when it is large in frame and garble it when it is small: in one photoshoot, 22 of 25 enlarged labels in single-product shots were correct (the 3 failures were small labels in lifestyle scenes) and 11 of 11 labels in multi-product shots were garbled. When the label will render small in the output (about 120 px wide or less; this threshold is an inference from those cases), plan a deterministic composite from a real photo of the label (Localized Repair §6.2) instead of relying on generated text. A generated label at larger size is acceptable only after a letter-by-letter check at zoom.

Project reference restrictions prevail over this section. When the active Project Profile forbids visible brands, logos or readable text in generation reference images (pointer in §10), the mark is not supplied as a generation reference and is added only through controlled finishing/compositing unless the operator changes that project rule.

---

## 9.2 Visible Text Is Not Claim Evidence

Keep distinct:

```text
VISIBLE_TEXT
= text observed in pixels / reference content

DISPLAY_AUTHORITY
= authority to preserve/render that text in the bounded deliverable

CLAIM_EVIDENCE_AUTHORITY
= evidence that permits the proposition to be asserted as a factual/commercial claim
```

A package or poster may supply `VISIBLE_TEXT` or even `DISPLAY_AUTHORITY` without authorizing the wording as a new claim elsewhere. Claim use remains owned by `QA_EVIDENCE_RIGHTS`.

---

# 10. Reference Roles

Every reference has a declared role:

```text
CHARACTER_IDENTITY
PRODUCT_IDENTITY
ENVIRONMENT_GEOMETRY
STYLE
COMPOSITION
TEXT_CONTENT
```

At direction time, resolve what each role is allowed to contribute and what must remain excluded. `ROUTE_COMPILATION` owns the route-native `allowed_inheritance` / `excluded_inheritance` binding; Image Direction supplies the creative/authority intent that binding must preserve. A `CHARACTER_IDENTITY` reference therefore does not automatically authorize its background, lighting, readable text or unrelated props.

Project reference restrictions narrow these roles further. In Pilot 01 (Project Profile Pilot01 §11) an environment reference contributes geometry / spatial identity only unless more is declared, wardrobe is described in words (no wardrobe-only image reference; §6.1 `wardrobe_or_styling` coverage is then resolved from the written wardrobe authority), and generation reference images carry no visible brand, logo or readable text.

A `COMPOSITION` reference may be a blocking/layout map whose authority is deliberately narrow:

```text
COMPOSITION / BLOCKING MAP MAY OWN
→ subject/object stations
→ relative arrangement
→ explicit counts
→ movement / clearance zones when material
→ relative scale / proportion between named subjects or objects when the map is authoritative for that relationship
→ trajectory/path geometry when the reference is explicitly scoped to a movement path

COMPOSITION / BLOCKING MAP DOES NOT SILENTLY OWN
→ identity
→ wardrobe
→ environment appearance / lighting
→ product truth
→ readable text
→ map marks / arrows / labels as scene content unless separate text/content authority explicitly requires them
```

By default the map owns stations, arrangement, counts and clearance. Relative scale and trajectory are owned only when the map is explicitly authoritative for that relationship or path; otherwise they remain with the other declared authorities.

Prefer color or shape to identify mapped subjects; use letters or numbers only when color/shape is insufficient and the project permits readable text in that reference. When the active Project Profile forbids readable text in generation reference images, the map carries no text. If colors, numbers or labels identify mapped subjects, bind each label to the intended semantic subject/reference. The label is positional metadata, not wardrobe or identity authority. Map strokes, colors, arrows and labels are never inherited by the final image unless separate text/content authority explicitly requires them; record them in the binding's `excluded_inheritance` (Route Compilation §7). Scope the map to the shot/location/view for which its geometry is meaningful; a top-down left/right relationship does not automatically become screen-left/screen-right under every camera angle.

Check reference readiness before use. Reject or scope references with conflicting identity, old packaging, unreadable defining details or contaminating text. When the route cannot bind a reference to a region or role, derive one-product crops as required by Route Compilation §7.2.

## 10.1 Cross-asset style continuity

When a still card/graphic must live beside accepted motion or another approved visual system, a clean accepted frame or derivative may be used as a `STYLE` reference **only when project/reference rules permit it**. Its role is palette, texture, lighting language or graphic treatment, not silent inheritance of identity, logo, readable text or unrelated scene content.

```text
ACCEPTED FRAME AS STYLE REFERENCE
≠
NEW IDENTITY AUTHORITY
≠
TEXT AUTHORITY
```

If a safe style reference cannot be made without contaminating protected identity/text/product truth, preserve style continuity through explicit art direction instead. Do not require any one provider or frame-extraction tactic.

## 10.2 Recurring-environment reference readiness

When location continuity is material across shots/assets, the environment reference should visibly establish the scene facts the production must preserve rather than relying on a generic text label such as “cozy kitchen.” Depending on the job, readiness may include:

```text
usable geography / room relationships
key fixed landmarks
material light direction / source relationship
time-of-day or other continuity state when authoritative
protected props / surfaces when materially recurring
subject stations / seats when downstream blocking depends on them
entry / exit or movement clearance when downstream action depends on it
camera/action room needed by an already-authorized shot plan
foreground objects placed so they do not accidentally block required proof/action
```

Action-readiness is task-relative. Do not force every environment plate to encode future camera paths or actor stations; add them only when downstream motion would otherwise have to invent material geometry.

A person-free establishing reference can be useful when it isolates environment geometry, but it is not universally mandatory. When the selected route can combine character and environment references, each keeps its declared role and inheritance boundary.

An accepted output frame may later supplement continuity when Project authority permits, but it does not replace the original/canonical character and environment authorities. Carrying only derivative-of-derivative references forward is not evidence that drift has been controlled.

## 10.3 Extracted visual-rule evidence state

When deriving reusable visual rules from supplied/official assets, label the basis of each material rule rather than flattening observation and fact into one authority class. Use the closest applicable project vocabulary; for visual extraction the following working labels are useful:

```text
SOURCE_DECLARED      = explicitly stated in authoritative supplied material
MEASURED             = deterministically measured from an authoritative asset
VISUALLY_OBSERVED    = repeatedly/clearly visible but not deterministically measured
INFERRED             = interpretation/hypothesis that may guide a draft but is not exact authority
```

Resolve conflicts by authority, not averaging. Explicit operator/project correction outranks extracted observations. Editable/source material outranks lossy derivatives for properties it directly defines. Never call an inferred/vision-estimated hex, font, spacing, radius or dimension exact. Record unresolved conflict instead of manufacturing a compromise.

These are evidence-state labels inside Image Direction, not a competing project-wide evidence taxonomy.

## 10.4 State-specific derived references

When a recurring subject/product/environment must enter a materially different visible state, a **state-specific derived reference** may be useful if text alone would leave the state ambiguous.

```yaml
state_reference:
  canonical_authority_ref:
  derived_reference_ref:
  state_semantics:
  valid_scope_or_window:
  allowed_inheritance:
  excluded_inheritance:
```

Examples of `state_semantics` may include wet/dry, damaged/intact, open/closed, dirty/clean or another project-authorized visible condition.

Rules:

```text
STATE-SPECIFIC DERIVED REFERENCE
=
DERIVATIVE OF ACCEPTED AUTHORITY
!=
NEW CANONICAL IDENTITY

use only when the state is materially useful downstream
preserve canonical identity/product/environment truth
scope the derivative to the state/window it represents
do not let a generated derivative invent permanent traits
```

For product/identity/reference sheets, multiple verified views may still belong to one semantic subject. If relative scale or trajectory is supplied by a composition/map reference, bind that authority narrowly and do not let the map become appearance authority.

---

## 10.5 Scoped Composite-Reference Binding

When one reference contains multiple panels, subjects, products, environments, texts or style signals, declare the smallest reliable authoritative scope:

```yaml
reference_scope:  # WHOLE_ASSET | SEMANTIC_REGION | SPATIAL_REGION | SUBJECT | PANEL
reference_locator:
authority:
allowed_inheritance:
excluded_inheritance:
```

A scoped role cannot silently promote the remainder of the asset. For example, `PANEL=2 / STYLE` may contribute palette/material/camera language while people, brand marks, product identity, copy and environment geometry elsewhere on the board remain excluded unless separately bound.

---

# 11. Prompt Preparation

The provider-neutral image spec should prioritize:

```text
job
hard invariants
spatial composition
identity / product truth
camera
light / material
text mode
creative_latitude_ref
creative_risk_level when applicable
allowed flexibility
acceptance checks
```

## 11.1 Specification shape follows the visual job

Do not force every image job into one prompt shape before route compilation.

For a **multi-region / layout / reference-sheet** job, make the visual structure explicit enough that repeated elements and regions are not left to accidental model interpretation. Where material, specify:

```text
named or addressable regions
relative position / hierarchy
item count
item labels or semantic identity
relationships between repeated items
exact text authority / text-content refs
required empty / protected space
```

Here `item labels` means semantic identity inside the specification. A label that must appear as rendered text follows §9 (Text Modes) and the project text policy; when the active Project Profile forbids requesting on-screen text from the generative model, rendered labels are added through controlled finishing.

A region map is a provider-neutral planning structure. It does **not** require JSON, a fixed grid, or any one vendor syntax. `ROUTE_COMPILATION` decides how the selected route should encode it.

For a **single coherent scene**, prefer an ordered scene specification that makes the subject/action/environment hierarchy easy to recover, for example:

```text
subject / product
→ action or pose
→ environment / spatial relation
→ camera / perspective
→ light / material / palette
→ text mode if any
→ acceptance-critical constraints
```

The exact order may change when the selected route has a better validated grammar. The transferable rule is to match specification structure to the visual job while preserving the same creative authority.

Before handoff, check that material visible regions are accounted for and that required repeated items have an explicit count/identity when ambiguity would change the asset.

Positive specification is default. Concise negative constraints are reserved for known route failures or explicit forbidden content.

---

# 12. Acceptance Rubric

Review at full resolution and intended display size.

Check:

```text
primary job legible
commercial / narrative hierarchy
identity fidelity
recurring-character reference coverage is adequate for the required view/state when material
identity/reference lighting does not leak into scene lighting without authority
product-reference coverage is adequate for the required visible view/surface/state when material
multiple views of one product remain one coherent product identity rather than drifting into incompatible variants
product geometry
materials / reflections
hands / anatomy
physical contact / weight
perspective
lighting coherence
negative space
multi-region/layout jobs preserve required region occupancy and semantic labels when material
declared item / repeated-item counts are checked against the actual output whenever the count is material, including single-scene prose-specified jobs
text/copy accuracy
mobile-size readability where relevant
cross-asset style continuity is coherent when the asset belongs to a mixed still/motion system
identity/world continuity is preserved without unnecessary repetition across dimensions declared open for expression
composition/blocking references preserve their narrow role without leaking identity/wardrobe/environment authority
composition maps preserve authorized relative scale/trajectory when material without rendering control marks as scene content
state-specific derived references remain scoped derivatives of accepted authority rather than becoming new identity/product canon
identity-reference packs do not contain unresolved material identity conflicts
recurring environments provide task-required spatial/action readiness when downstream motion depends on it
no accidental brands / unsupported claims
```

---

# 13. Example Contrast

Weak:

```text
"Premium cinematic product shot with elegant lighting."
```

Stronger:

```text
Product occupies ~45% of frame center-left, front label fully visible, slight three-quarter angle, rests on matte stone surface with contact shadow; soft window key from camera-left; empty upper-right copy space; no extra accessories; packaging proportions locked to PRODUCT_REF-02.
```

The transferable principle is observable composition, not this exact layout.


---

## V2.4 real-world hardening — storyboard as independent planning object

Image direction supports visually reviewing *sequence/space* through separate 16:9 storyboard panels or boards when material; distinguish `STORYBOARD_PLAN` from provider `START_FRAME`, `PRODUCT_IDENTITY` and `CHARACTER_IDENTITY`. A visual board may help inspect whether the intended actor is seated opposite the approaching character and whether product reveal, spatial blocking, props and camera line are coherent. A user request to correct panel 7 authorizes only that panel, never regeneration of all panels. Link repaired storyboard to prior approval and revised script version.

Do not demand an image per movement, line or second; do not automatically submit a whole storyboard collage or sheet as provider identity reference. For real product, source photographs beat generated visuals for dimensions/material/print. For digital product, real UI captures and functional specifications beat invented screens. Use minimum sufficient references and exact allowed inheritance.

