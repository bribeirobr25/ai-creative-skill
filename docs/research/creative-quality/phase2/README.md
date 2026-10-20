# Phase 2 — validation and integration readiness

20 October 2026. Continuation of Issue #8 and draft PR #9 at verified head
`e35b6f5015aa072cd76ceb91fca7d8e1f25d630d`. The team review submitted at
18:05:30 UTC accepts research evidence for further validation, **not canonical edits,
merge or release**. Main remains `39a0bfa`; PRs #6/#7 remain open drafts and unchanged.

## Executive decision

**P1 is ready for consideration as a small, proportional rendered-QA checkpoint.**
The first experiment caught an actual mobile implementation regression. A second,
fictional educational website demonstrates the same distinction between functional
success and visual usefulness with a declared mutation control. It does not prove a
universal aesthetic improvement or an autonomous installed-skill capability.

**The human preference gate remains `AWAITING_HUMAN_REVIEW`.** No genuine human
reviewer was contacted or simulated. Two complete private counterbalanced packets now
include equal-resolution captures, four short actual interaction recordings, a local
response form, a coordinator key and intake checks. Zero independent human responses
have been received. P2's proposed concrete direction wording is a candidate; preference
claims and stronger mandatory requirements remain held as requested by the team.

## Delivered evidence

| Deliverable | Record |
|---|---|
| Independent A/C review package and response procedure | [Human review](human-review.md); private `CQ2-HUMAN-REVIEW` packets |
| Executed cross-category experiment | [Transfer experiment](transfer.md), original fictional fixture and real browser captures |
| Separate aesthetic/fidelity/usability/technical/effort results | [Transfer](transfer.md) and [method analysis](method-analysis.md) |
| Minimal method wording and integration decisions | [Integration assessment](integration.md) |
| Reproduction and dependencies | [Research tooling](../../../../validation/creative_quality/phase2/README.md) |
| Actual browser results | [166 PASS / 2 retained synthetic FAIL](../../../../validation/creative_quality/phase2/results/browser-summary.json) |
| Existing contract validation | [Validated record](../../../../validation/creative_quality/phase2/results/web-delivery.json), retained `PARTIAL` / `PREVIEW_REVIEWED` |
| Human gate | [Zero responses; awaiting review](../../../../validation/creative_quality/phase2/results/human-review-status.json) |

## Answers for the team

1. **Is rendered review useful?** Yes for the demonstrated objective failure boundary:
   decoded, correctly sized content can still be invisible or collapsed. A working
   interaction does not establish useful presentation.
2. **Does usefulness transfer?** Bounded evidence supports transfer to educational
   planning: the same workflow detects the hidden learning path at both viewports and
   confirms a precise restoration. The defect was deliberately injected and known to
   the investigator. This is not an independent discovery test or a natural defect-rate
   estimate.
3. **Preference or defect?** Della A/C's image-versus-CTA order is a legitimate tradeoff;
   the collapsed B image is a defect. Aurora A/B's emphasis, separators and spacing are
   alternatives; the invisible required learning path in S is a defect. Neither study
   proves a preferred composition.
4. **Negative impact?** Della C moves mobile CTA down about 240px. Aurora B moves mobile
   CTA up 4px, desktop CTA down about 39px and increases mobile page length by 307px.
   Its planning buttons are more prominent, but extra scrolling may be less useful.
   No detected copy/asset/focus/contrast regression in the observed scope. No measured
   conversion or broad accessibility claim.
5. **Smallest useful adjustment?** Add an intention-led check of actual composition,
   meaningful visual visibility and one key interaction at requested sizes; correct
   the smallest failed surface and retest only what changed. Reuse current records.
6. **What blocks promotion?** Owner approval of exact method wording and the release
   process remain required. P2/preference assertions additionally need real independent
   human evidence. Harness #6/#7 is not integrated; keep the adapter optional, with an
   explicit pinned checkout. Do not make it a main runtime dependency.
7. **Next highest-value experiment?** Two genuine independent A/C reviews, retaining
   ties/disagreement, with the owner deciding which composition suits the actual goal.
   Then have an uninformed operator apply the minimal checkpoint to one unseen fixture
   containing a different defect (for example an occluded action), using the same
   bounded repair budget. No paid generation is needed.

## Boundaries

No changes to canonical `src/`, installed skill, original projects, other PRs or public
websites. No paid model generation, outbound emails, merge or release. Fixture assets
are original geometric SVG and system fonts; no third-party media or customer material
is in public Git. Automation tests of the response form use explicitly synthetic data,
discard the export, and are never human evidence. Research completion includes the
prepared fallback package; it does **not** close the human preference or release gate.
