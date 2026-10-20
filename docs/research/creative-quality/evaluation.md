# Quality Acceptance Framework

This research rubric references existing QA/Execution Contracts; it does not replace their authority or define a new production state machine.

## Four separate axes

| Axis | Observable evidence | Reviewer judgment / acceptance |
|---|---|---|
| Aesthetic | Rendered hierarchy, spacing, framing, type sizes, scene variety, lighting/material cues | Intentionality, coherence, finish and suitability to audience; explain with image/region evidence |
| Fidelity | Source-text/assets hashes; logo/label correspondence; original reference views; protected-region comparison | Does framing/lighting alter apparent identity or material? Are unknown surfaces or claims invented? |
| Technical / functional | Dimensions, duration, frame rate; real browser interactions; errors, overflow, focus, reduced-motion | Does the delivered experience satisfy the requested operation? Partial coverage stays partial |
| Efficiency | Generation calls, changed bytes, review passes, measured local transfer sizes; known elapsed run time | Human effort and accepted-output cost; do not infer vendor effort or margins |

Illustrative aesthetic scale: **1** unusable/contradictory; **2** weak or materially unfinished; **3** coherent competent draft; **4** strong intentional execution in observed scope; **5** exceptional, with independent audience-appropriate review. Ordinal scores are judgments, not measurements. Never average a critical fidelity or truth defect away. No overall numerical “quality score” or invented percentage lift.

A PASS for image loading cannot imply visible prominence: B loaded its hero but rendered it at 6.59px high. A matching asset hash cannot prove the CSS crop preserves the product. Both were observed in the experiment's review boundary.

## Case and review procedure

1. Fix brief, protected information, asset manifest, tool/version, output geometry and allowed budget/review passes.
2. Distinguish archive provenance from installed-method execution. Record unknown prompt/model/attempt data as UNKNOWN.
3. Capture desktop 1440×900 and mobile 390×844 plus interaction state. Keep original and failed candidates.
4. Apply the same bounded browser assertions to all candidates. Derive targeted visual assertions from the task; the 160px hero minimum is only this experiment's collapse detector, not a universal design rule.
5. Inspect screenshots at equivalent display scale. Record failures before repairs. One planned B→C review pass here; no best-of-many selection concealed.
6. Separate observed metric, automated-reviewer interpretation and human acceptance. Final authority stays with the project owner.

## Rejection and unknowns

Incorrect identity/name/logo, fabricated product geometry or commercial claim, fake checkout, unauthorized publication/spend, and loss of a required visible element block acceptance regardless of aesthetics. Unreadable small text or absent source coverage is UNVERIFIED, not PASS. A visually appealing historical artifact can remain approved for its historical use while a newly inspected specification mismatch is separately recorded; this investigation does not revoke or broaden canon approvals.

## Blinded review packet

The private packet contains equal-size A/C captures and a label mapping stored separately. Prepared for future review only: **zero independent reviews executed**. Ask two reviewers to choose a preference or tie and explain composition, fidelity, CTA clarity and mobile behavior separately. Counterbalance label/order. Reveal the mapping only after each response. This small review is directional, not statistical population evidence.

## Relevant T-cases

The 100 browser assertions are **not 100 executions of the proposed T-scenarios**.

| Prior scenario | Application here | Coverage limit |
|---|---|---|
| T12: repair caption without regenerating person/product | Analogous localized CSS repair with unchanged HTML/JS/assets | Does not execute the original caption-edit scenario |
| T14: vertical requested, horizontal delivered | Actual M016 dimensions versus associated article prompt inspected | Observed mismatch; not a test that the runtime automatically blocks acceptance |
| T23: repeat affected website journey after script/resource change | Actual browser retest after stylesheet changes, across both viewports | Research adapter execution, not installed route automation |
| T28: free skill versus paid execution | No generation call; price-only quote distinguishes future paid execution | Budget boundary respected; not a full simulation of an agent following a misleading “free” recipe |
| T07: reference crest conflicts with instruction to remove it | Reference-authority question retained in media analysis | Exact conflict-resolution scenario NOT RUN |
| T11: hidden/blurred label | Small-text and source-view limitations marked UNVERIFIED | Inspection finding; no general all-frame label validator tested |

Remaining T01–T28 cases are not relabeled PASS or duplicated as artificial coverage.
