# Integration readiness and minimal method delta

No canonical method is edited in this branch. Technical evidence can support a review
decision without authorizing merge, installation, production acceptance or release.

| Proposal / claim | State | Decision basis / remaining gate |
|---|---|---|
| P1: proportional rendered review of primary visual, hierarchy/action and key interaction | READY_FOR_INTEGRATION_CONSIDERATION | Actual Della regression plus educational mutation/restoration evidence; owner must review exact wording and release scope |
| P2: explicit intention in current direction fields | CANDIDATE_HELD_FOR_HUMAN_REVIEW | Existing fields suffice and two context-specific directions were executed; team explicitly holds stronger claims/requirements until independent A/C evidence |
| “C is aesthetically better than A” | AWAITING_HUMAN_REVIEW | Zero genuine independent responses; ties and dissent allowed |
| Generalized autonomous visual diagnosis | NEEDS_NEW_TEST | Single investigator, one natural defect and one known synthetic failure mode |
| Fixed 160px visual rule / universal image-first hero | REJECTED | Does not transfer to educational task or legitimate CTA-first brief |
| Mandatory moodboard, generated assets or extra revision on every request | REJECTED | B had no defect needing C; extra work is not automatically improvement |
| Image/video P3–P6 expansion | DEFERRED | Outside this phase; prior findings remain, no new paid media generation |
| Required dependency on unmerged harness #6/#7 | RESOLVED (2026-10-30 note): #6 and #7 merged on 2026-10-21; the package is frozen by ADR-0005, so no main-runtime integration is planned | Research dependency only |
| Production rollout / canonical release | NOT_AUTHORIZED | No merge/install/release authority in this task |

These labels are research decisions, **not new runtime status enums**. Canonical
`WEB_QA` remains PASS/PARTIAL/BLOCKED/UNVERIFIED and delivery state uses existing values.
Human preference is an external gate; do not inject `AWAITING_HUMAN_REVIEW` into the
canonical schema. The executed fictional record correctly stays `PARTIAL` and
`PREVIEW_REVIEWED` with `MANUAL_SPEC_GUIDED` execution.

## Minimal P1 wording candidate

> When visual presentation matters to the requested web operation, inspect the actual
> rendered composition at the requested formats against its intended focal point and
> action hierarchy. Confirm meaningful visibility of essential visual/content elements
> and exercise a key interaction. Distinguish an objective defect from a legitimate
> preference tradeoff. If a relevant defect is found, repair the smallest permitted
> surface and repeat affected visual and functional checks. Record evidence and limits
> in WEB_QA; retain pending human acceptance where required. If no relevant defect is
> found, a further revision is not mandatory.

Suggested placement: one short addition to existing Web Experience FAST step 7, referring
to step 3's direction. Do not add a Work Profile, router, provider rule, universal metric,
second harness, mandatory new document or generated-reference step.

## P2 mapping without a new contract

| Needed information | Existing field |
|---|---|
| Focal element, intended composition and hierarchy goal | `WEB_DIRECTION.visual_direction` |
| Action and utility priority | `WEB_DIRECTION.primary_cta_intent`, `WEB_BRIEF.task_completion_condition` |
| Protected brand/content | `WEB_DIRECTION.brand_alignment`, `claim_and_offer_boundaries`, existing asset preservation fields |
| Allowed variations | `WEB_DIRECTION.creative_open_zones` |
| What would be visibly inadequate | Concrete language in `visual_direction`; task-specific requirements in `WEB_QA.checks` |
| Local edit boundaries and affected checks | `WEB_REVISION` for applicable edits; no invented approval references |
| Evidence and acceptance limits | Existing QA result/mode/evidence/build/viewport fields and known limitations |

The fictional B record was validated with the **existing** schema/runtime and canonical
build hash. Early record wiring used logical evidence labels and a generic digest; the
validator rejected them. Binding concrete evidence under the local site, using canonical
hash/check IDs and accurately classifying the new provisional preview resolved those
record errors. No weakening or schema change was needed. The validator's success is
record consistency, not independent certification of the observations.

## Review and eventual promotion sequence

1. Review this stacked research PR against PR #9's verified branch; keep #9 and #6/#7
   separate and unchanged.
2. Complete human review and record owner decisions, including whether A/C preferences
   differ by viewport/goal. Never require C to win.
3. If accepted, prepare a small separately authorized canonical method candidate with
   the chosen P1 wording and bounded tests. P2 changes should reflect the human outcome.
4. Resolve whether harness #6/#7 is integrated or remains an optional development tool;
   the method must remain portable without this machine's browser paths.
5. Execute an unseen-fixture test with an independent operator, then follow existing
   owner review and release gates. Research PASS does not bypass them.
