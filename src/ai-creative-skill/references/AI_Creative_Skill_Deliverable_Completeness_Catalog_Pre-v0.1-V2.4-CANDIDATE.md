# AI Creative Skill — Deliverable Completeness Catalog · Pre-v0.1-V2.4-CANDIDATE

**OWNER:** Specialist Method System governs selection; narrower methods own domain meaning. **STATUS:** V2.4 candidate; not a new Work Profile or top-level orchestrator. Machine-readable mirror: `../contracts/deliverable_contracts_v0.1.json`.

## 1. Execution sequence

`USER REQUEST → bounded deliverable and completion condition → resolve Project/Work authority → load applicable specialist(s) and this deliverable contract → produce → per-item structural + semantic self-check → smallest authorized repair → handoff/deliver or accurately mark PARTIAL/BLOCKED`.

The completeness gate is **mandatory for a complete in-scope deliverable**, not for a request for a title only, a discussion of options, an early draft, a partial asset, or a stopped/blocked task. Preserve user-requested smaller scope. Never widen the task to produce unrequested assets, spend, publish, solicit customers, buy, or create adjacent deliverables.

Requirement classes: `REQUIRED`, `CONDITIONAL`, `OPTIONAL`, and `CREATIVE_OPEN`. Conditional requirements are activated only by a grounded trigger. `REQUIRED` means present with *substantive domain content*, not an empty heading or generic filler. Unknown source facts remain `UNKNOWN`/`UNVERIFIED`, not invented to satisfy a shape. `WAIVED` is permitted only for a recorded legitimate scope exclusion or inapplicability with an authority reference; never self-waive a known critical requirement.

For batches, the gate runs on **each item**, not merely on a heading in a wrapper. A ten-idea deliverable requires ten individually coherent ideas. The author may add meaningful creative material beyond the minimum. A valid addition must respect canon, claims, product identity, privacy/rights, evidence, approval and expressive latitude.

## 2. Domain contracts

### CHARACTER_BIBLE — complete new persona/AI influencer
- REQUIRED: unique name/identity, role/territory, backstory with relevant causal history, distinctive visual identity that can be compared with cohort, personality/motivation/contradiction, USP (reason to follow or role in story), fiction/disclosure boundaries, canon `PRESERVE` vs scene-level `VARY`.
- CONDITIONAL: recurring on-camera speaker → voice/performance direction; image production → identity reference authority and approval; claims about real organizations/achievements → verified evidence or unverified/fiction labeling.
- OPTIONAL: relationships, prop signature, story arcs, production styling, monetization hypotheses. A request for *three possible names* does not trigger the complete Bible.
- OWNERSHIP: Organic/Ads owner and applicable Script/Performance + Image Direction; Talking Persona only when visible recurring speech applies. If a separate Character Design method is ever proposed, run necessity/ablation first; no new method in V2.4.

### CONTENT_IDEA — fully developed creative idea
- REQUIRED **per idea**: `Hook` (spoken, visual or text), `Format & Hold` (mechanism sustaining attention), `Setting` (where/why the action belongs there), `Why It Works` (split observed evidence vs hypothesis), `Payoff / audience value`. Do not pretend a trend or performance forecast is proven.
- CONDITIONAL: persona fit, applicable market/platform evidence/claims, and explicit product if a product concept.
- OPTIONAL: series potential, variation, on-screen text, footage feasibility.
- An idea is **not yet a script**: avoid locking seconds, shot list and dialogue before selection unless requested.

### STORYBOARD_PLAN — previsualization planning
- REQUIRED: narrative/concept reference, ordered material beats, character and prop blocking/space, protected reveals, critical continuity and handoff states, reference roles, declared creative open zones.
- CONDITIONAL: multipart seam, physical product canonical anchor, dialogue roles, visual panel images when the user requested visual storyboard.
- Default behavior before motion production: **resolve the storyboard decision**; propose/generate previsualization for multi-beat, multi-shot, multi-character, uncertain product interactions, multi-chapter or expensive motion. Can skip creating new panels when a valid accepted storyboard exists, when a genuinely unambiguous one-shot is in scope, or when the user explicitly declines; document why. Generating expensive external panels requires appropriate authority.
- Storyboard is a reversible **planning object**, not an exact shot-timing constraint, a provider input mandate, or a second source of canonical face/product truth. Concept ⇄ storyboard ⇄ script revision until accepted; do not generate dozens of movement-reference images.

### VIDEO_CREATIVE_DIRECTION — approved script intended for generation
- REQUIRED: `Intent`, `Setting & Atmosphere`, `Script & Creative Direction` (continuous director-style explanation unless another mode is justified), `Creative Invariants`, `Creative Open Zones`, overall delivery constraints.
- `Text on Screen` is OPTIONAL or CONDITIONAL if the job requires exact visible words. `Speech` and speaker assignment only when there is dialogue. Timelines are required only if route/audio/editorial authority makes frame or event timing material. Include global duration or budget without forcibly dividing every beat into 0–2s boxes.
- Route compiler may translate to `CONTINUOUS_UNIT`, `ORDERED_BEATS`, `BOUNDED_WINDOWS`, or `DETERMINISTIC_EDIT_POINTS` without rewriting creative intent. Approved improvisation must not become new canon or unsupported claims.

### REFERENCE_MANIFEST — each actual provider submission
- REQUIRED: stable IDs, source and authority role, allowed/excluded inheritance, approval state, **selected inputs actually submitted** and their order. Library availability != required upload of every reference. Distinguish canonical product/photo from generated moodboards and storyboard frames.
- CONDITIONAL: real product proof, multi-chapter approved seam, cross-cast/look reuse.

### PROJECT_NEXT_ACTION — non-blocking continuation guidance
- REQUIRED when materially useful: what is done, what project state is pending, the recommended next step and its value, whether it is authorized. If a bounded task simply finishes a trivial request, omit the progress panel. A suggested step is **not an executable authorization**. Preserve persistent project vs bounded task separation.

## 3. Completeness verdict, evidence, scope

Proposed supplemental schema, not a replacement for `Review Verdict` or `Work Card`:

```yaml
deliverable_check_id:
work_id:
deliverable_type:
deliverable_scope:       # FULL | BOUNDED_PARTIAL | DRAFT
contract_version:
method_version_refs:
required_checks:        # per field: PASS | MISSING | INSUFFICIENT | UNKNOWN | NOT_APPLICABLE
conditional_triggers:
per_item_results:       # every item when a batch
source_and_canon_refs:
self_check_repair_passes:
result:                 # PASS | PARTIAL | BLOCKED | UNVERIFIED
remaining_findings:
reviewer_independence:  # SELF_REVIEW | INDEPENDENT | MIXED | UNKNOWN
```

`PASS` requires substantive field content and applicable semantic checks. `PARTIAL` may be delivered honestly when intentionally partial or constrained; no false COMPLETE. Self-check is not independent verification. Do not create unbounded revision loops (use the narrower method's bounded retry limit). The included JSON/Python validator checks shapes, *not* semantic truth, model activation, rights or audiovisual quality.

## 4. Evaluation cases / regression anchors

- Influencer: character backstory absent; USP absent; all faces visually interchangeable; fields are headings only.
- Bia: 10 ideas but only first one has Hook/Format/Setting/Why; a fake claim about a proven trend; user asks for names only.
- Nina: leading supertopmodel intent silently overwritten by secondary brand curatorship.
- Della: product is a print of croissants, not pastry; two characters and phone/pouch/table object state; Paris historical references cannot override current Berlin.
- Direction: dialogue and physical gesture occur together; no forced per-second script for narrative; mandatory timing remains for UI demonstration/cuts.
- Workflow: task completes, project remains open, recommendations do not imply generation/publishing/budget approval.
