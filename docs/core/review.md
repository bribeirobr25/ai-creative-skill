# Review

**Sources:** ADR-0006 D2, D3, D7, D9; decision `evaluation-method`; V2.5 SMS §10.1 (self-check), §11 (review independence); EC §12 (review verdict), §22 (repair record); Localized Repair §8.1 (repair-round limit); Completeness Catalog §1, §3 (`deliverable_check`); QA Realism §1, §3, §3.1 (preflight ≠ acceptance), §9 (severity), §10; ARCH §21; frozen ledger §11.4; the four-axis rubric in `docs/research/creative-quality/evaluation.md`; the 2026-10-22 learnings audit (`docs/research/auditoria-aprendizados-2026-10-22.md`) and the style test (`docs/research/style-test-18/README.md`).

## Three evaluation boundaries

The framing is *new here*.

| Boundary | Question | Evaluated on | Result | Needs generation? |
|---|---|---|---|---|
| **A · Direction and plan** | Does the concept, script, storyboard, design direction or plan meet the objective, constraints and required elements? | The deliverable document | Verdict | No |
| **B · Execution package** | Does the prompt, parameter set, code or payload faithfully carry the approved direction, and is it complete, feasible, within rights and suited to the tool? | The package ([project-context.md](project-context.md#execution-packages)) | Readiness `READY`, `NOT_READY`, `UNVERIFIED` (*new here*) | No |
| **C · Observed result** | Does the generated or rendered asset have the fidelity, continuity, quality and technical conformance expected? | The asset | Verdict | Yes, or a local render |

1. **RV1 · Predicted is not observed.** Boundary B gives *predicted readiness*, never acceptance (QA Realism §3.1). A strong prompt does not prove a strong asset: in the 2026-10-22 audit (F-A4), small labels came out wrong in 11 of 11 collection shots, and compositing the real label fixed all 14 affected labels. A boundary-A verdict `ACCEPTED` is acceptance only when the plan itself is the deliverable (QA Realism §3.1).
2. **RV2 · Cheapest valid boundary first.** Check at A and B before paying for C. Code-based deliverables (websites, SVG logos, code-based animation) reach C by local rendering, without generation credits.
3. **RV3 · Uninspected is unverified.** A dimension nobody looked at is `UNVERIFIED`, never passed (QA Realism §3, §10); sampled frames cannot certify motion or audio (ARCH §21).

## Review record

```yaml
review:                 # plus the record envelope; extends EC §12 (asset_id generalized to subject_ref)
  subject_ref:          # required: deliverable, package or asset, with version
  boundary:             # required: A | B | C
  criteria_ref:         # required: required elements and "done" (playbook stage or pack)
  reviewer_type:        # required: HUMAN | MODEL | TECHNICAL | MIXED
  verdict:              # A and C: ACCEPTED | REPAIR | BLOCKED | UNVERIFIED
  readiness:            # B: READY | NOT_READY | UNVERIFIED
  findings:             # each: dimension, severity BLOCKER | REPAIR_REQUIRED | NOTE, evidence ref
  uninspected: []       # dimensions not checked
  repair_round:         # when part of a repair loop
  # derived on read: reviewer_independence (SMS §11), by comparing the reviewer with the subject's written_by
```

## Who reviews

- **Closing check, by the owner.** Before any handoff the owner checks its deliverable against the required elements: each `PASS`, `MISSING`, `INSUFFICIENT`, `UNKNOWN` or `NOT_APPLICABLE`, and the whole `PASS`, `PARTIAL`, `BLOCKED` or `UNVERIFIED`, never silently complete (Completeness Catalog §3). It is never skipped (ADR-0006 D2): in the October style test only 1 of 18 runs produced and validated its delivery record.
- **Acceptance, independent.** A final deliverable (the finished work a task hands to the user: an asset at C, or a plan when the plan is what was asked) is accepted only by a reviewer that did not produce it: fresh context, the artifact plus criteria plus authoritative references, no desired verdict, read-only while judging (SMS §11). Intermediate deliverables (an offer, a direction) may go to the user after the owner's closing check. A review that is not independent is labelled what it is.
- **The user's judgement** at the checkpoints that matter is an approval or feedback, a separate act from review.

## Repair

1. **RV4** Repair rounds are capped at the strictest applicable bound; the default is one round (Localized Repair §8.1). At the cap the task stops with `STOP_REPAIR_LIMIT_REACHED` and the question goes to the user (ADR-0006 D3; EC §22 `escalation_state`).
2. **RV5** Repair the smallest surface that fixes the cause, and re-check what was already accepted (Localized Repair).
3. **RV6** A `NOTE` never triggers paid regeneration by itself (QA Realism §9).

## Judges and scores

A model judge's score is a signal, not an authority: numeric self-scoring as acceptance authority is rejected (frozen ledger §11.4). No overall numeric score decides acceptance, and a fidelity or truth defect is never averaged away by aesthetics (four-axis rubric).

## Calibration

Whether boundary-B readiness predicts boundary-C results is unknown. Because each package links to its readiness review, its assets and their acceptance, real projects accumulate the evidence to measure it without extra spend. Any dedicated evaluation, including a paid calibration sample, needs a new `evaluation-method` decision (ADR-0006 D9). Nothing here authorizes or redefines the deferred Video Director evaluation.
