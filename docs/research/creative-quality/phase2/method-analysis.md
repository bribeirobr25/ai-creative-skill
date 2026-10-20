# What the method did — and did not — establish

| Component | Della evidence | Transfer evidence | Interpretation |
|---|---|---|---|
| Creative direction | Full image-led composition versus earlier CTA/message | Explicit stage hierarchy and planning actions; message-first mobile retained | Different goals imply different valid compositions. More prompt detail is not isolated as causal |
| Asset organization | Same 16 images, with existing varied catalog backgrounds | Same single original SVG; content hierarchy changes via CSS | New media/model is unnecessary for these changes; cross-provider asset advantage remains unresolved |
| Implementation | B accidentally collapsed the mobile image | A/B function and render within the bounded checks; B increases page length | Direction can be implemented well or poorly; this is not a contest between adjective counts |
| Rendered inspection | Revealed a natural implementation defect | Confirms no natural repair needed; detects declared invisible-path mutation | Observation is useful even when the correct decision is to stop without editing |
| Acceptance criteria | Functional checks initially missed meaningful visibility | Opacity probe fails while content-fit, decoding and interaction checks pass | Visibility, fidelity, function and preference need separate evidence |
| Local repair | C fixes the collapsed image with unchanged protected bytes | R removes only the mutation and restores exact B | Bounded causal link between local change and objective repair; no proof of aesthetic preference |

## Effort and proportionality

Recorded work units are stronger evidence than invented time savings:

- Transfer A: one original 4-file fixture, one functional baseline.
- B: one CSS patch (+1,614 bytes), one planned visual inspection of hero/full page/dialog
  at two widths; no natural corrective iteration. Additional desktop whitespace and
  mobile page length are explicitly retained as preference tradeoffs.
- S: one declared 186-byte mutation including separator, outside the design comparison.
- R: one exact suffix removal and two viewport retests. No new creative variant.
- Eight viewport runs total, 21 assertions per run; initial A/B/S capture and R retest
  are separate sessions. Assertions are cheap repeatable observations, not eight human
  judgments. Screenshot timing windows and file fingerprints are in provenance; they
  are not total authoring time.
- Independent-review preparation: four recorded walkthroughs totaling about 68 seconds
  of measured browser/recording execution, plus packet/form preparation and validation.
  Reviewer effort is not measured because no human review occurred.
- Zero model calls, paid generations, media purchases or deployment operations.

Authoring, analysis, tool waits and documentation were interleaved by one investigator;
no reliable separate timer for “creative direction versus implementation” was recorded.
Do not infer a percentage productivity gain or compare these totals to an unknown
vendor production budget. Next timed transfer should record stage start/stop before
work, not reconstruct labor cost from file timestamps.

## Causal limits

The intervention is a bundle of explicit intention, CSS implementation, browser checks,
visual inspection and bounded repair. There is no randomized ablation isolating each
factor. The strongest causal evidence concerns the defect and its local reversal.
Aesthetic success, scan speed, human preference and conversion are not demonstrated.
The investigator authored the fixture and knew the sabotage; independent diagnosis on
an unseen defect is the next useful test. None of this is an automatic installed-skill
execution or a comprehensive detector for occlusion, cropping or tiny unreadable text.
