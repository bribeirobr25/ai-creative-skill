# Review

**Sources:** ADR-0006 D2, D3, D7, D9; V2.5 SMS §10.1 (self-check), §11 (review independence); EC §12 (review verdict), §22 (repair record); Completeness Catalog §1, §3 (`deliverable_check`); QA Realism §1, §3.1 (preflight ≠ acceptance), §9 (severity); ARCH §21 (uninspected = unverified); the four-axis rubric in `docs/research/creative-quality/evaluation.md`; benchmark log BL-2026-10-29-01 and the 2026-10-22 learnings audit.

## Three evaluation boundaries

| Boundary | Question | Evaluated on | Needs generation? |
|---|---|---|---|
| **A · Direction and plan** | Does the concept, script, storyboard, design direction or plan meet the objective, constraints and required elements? | The deliverable document | No |
| **B · Execution package** | Does the prompt, parameter set, code or payload faithfully carry the approved direction, and is it complete, feasible, within rights and suited to the tool? | The package ([project-context.md](project-context.md#execution-packages)) | No |
| **C · Observed result** | Does the generated or rendered asset have the fidelity, continuity, quality and technical conformance expected? | The asset itself | Yes, or a local render |

Rules:
1. **V1 · Predicted is not observed.** A boundary-B verdict is *predicted readiness*; only boundary C is *observed acceptance* (QA Realism §3.1). A strong prompt never proves a strong asset: some failures do not depend on the prompt (small labels garbled in 11 of 11 images in the photoshoot study, fixed by compositing the real label).
2. **V2 · Cheapest valid boundary first.** Check at A and B before paying for C. Code-based deliverables (websites, SVG logos, code-based animation) can reach C by local rendering, without generation credits.
3. **V3 · Uninspected is unverified.** A dimension nobody looked at is `UNVERIFIED`, never passed (ARCH §21); sampled frames cannot certify motion or audio.

## Review record

Extends EC §12 without changing its verdict vocabulary:

```yaml
review:
  review_id:            # required
  subject_ref:          # required: deliverable, package or asset, with version
  boundary:             # required: A | B | C
  criteria_ref:         # required: required elements and "done" (playbook stage or pack)
  reviewer_type:        # required: HUMAN | MODEL | TECHNICAL | MIXED
  reviewer_independence:  # required: INDEPENDENT | MIXED | SELF_REVIEW | UNKNOWN (SMS §11)
  verdict:              # required: ACCEPTED | REPAIR | BLOCKED | UNVERIFIED
  findings:             # each: dimension, severity BLOCKER | REPAIR_REQUIRED | NOTE, evidence ref
  uninspected: []       # dimensions not checked
  repair_round:         # when part of a repair loop
```

## Who reviews

- **Closing check, by the owner.** Before any handoff the owner checks its deliverable against the required elements and marks each `PASS`, `MISSING`, `INSUFFICIENT`, `UNKNOWN` or `NOT_APPLICABLE`, and the whole `PASS`, `PARTIAL`, `BLOCKED` or `UNVERIFIED`, never silently complete (Completeness Catalog §3). Closing and verification steps are never skipped (ADR-0006 D2): in the October style test only 1 of 18 runs produced and validated its delivery record.
- **Final review, independent.** Acceptance needs a reviewer that did not produce the work: fresh context, the artifact plus criteria plus authoritative references, no desired verdict, read-only while judging (SMS §11). If that is not available, the review is labelled what it is, never "independent".
- **The user's judgement** at the checkpoints that matter, recorded as approvals or feedback, is a separate act from review.

## Repair

1. Repair rounds are capped. The default is one round after the first review, unless the scope or a narrower pack sets another limit; at the cap the task stops with `STOP_REPAIR_LIMIT_REACHED` and the question goes to the user (ADR-0006 D3; EC §22 `escalation_state`).
2. Repair the smallest surface that fixes the cause, and re-check what was already accepted (V2.5 Localized Repair, cited by EC §22).
3. A `NOTE` never triggers paid regeneration by itself.

## Judges and scores

A model judge's score is a signal, not an authority. No overall numeric score decides acceptance, and a fidelity or truth defect is never averaged away by aesthetics (four-axis rubric). "Every output scored 1–10, under 8 goes back" is not adopted: judges share systematic biases, such as preferring longer or more familiar output.

## Calibration

Whether boundary-B verdicts predict boundary-C results is unknown. Because each execution package links its preflight review, its result assets and their acceptance, real projects accumulate the evidence to measure it without extra spend. A small, separately authorized sample may calibrate a route or a model change. How this evidence is used to decide that guidance or an agent earns its place is the open evaluation decision (ADR-0006 D9). Nothing here authorizes or redefines the deferred Video Director evaluation.
