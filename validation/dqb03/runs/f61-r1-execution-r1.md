# Execution record · run f61 · R1 (single review round)

- Start (UTC): 2026-10-21T13:06:12Z (copied r0 to r1; r0 not modified)
- End (UTC): 2026-10-21T13:08Z
- Active time: about 2 minutes by the machine clock (well within the 15-minute limit).
- Method used for the review: WEB_EXPERIENCE Work Profile v0.2 QA step (browser evidence at 1440/390, 320 overflow, 768, full-scroll image crop review, form truth, CTA, keyboard) and rubric.md dimensions. No new method files read.
- r0 integrity: `web-delivery-r0.json` still validates against r0 (hashes unchanged).

## Problems found (from r0 screenshots at 1440, 768, 390, 320)

1. Images (390, 768 how view): the portrait image `how-it-works-goal.jpg` was cropped to 16:9 at 50% 45%, cutting the face at the chin. The other two portrait crops were also arbitrary.
2. Clarity (home facts strip, every viewport): the fourth item read "Yours / progress is saved in the browser on this device", which is awkward and leans on a vague label.
3. Composition (1440 home): the facts strip borders ran to the container edge while the text sat on the gutter, so the strip did not line up with the hero and the cycle rail.
4. Typography (1440 home): the hero title broke into 4 lines with "before" alone on one line.
5. Composition (waitlist view, all viewports): the dark waitlist page and the dark footer merged with no visible boundary.

## Fixes made in r1

1. How view below 900px: images at 4:3 with a crop set for each image (goal 50% 12% keeps the face, path 50% 55%, move 50% 62%). The images are not distorted.
2. Fourth fact changed to "This device / Practice progress is saved in the browser on this device." (brief wording).
3. Facts strip now has the same width as the content column (inset by the gutter), so it lines up with the hero and the cycle rail.
4. Display size capped at 80px (was 86px). The hero title now sets in 3 balanced lines at 1440.
5. The footer top rule is now copper (rgba of #b67d44) so the footer reads as its own block under the dark waitlist page.

## Preserved

All copy, routes, test IDs, interactions, the calculator logic, the waitlist logic, the palette, the type and the image choices are unchanged apart from the items above. `app.js` is byte-identical to r0.

## Checks performed and regressions

- Re-ran the same Playwright script against r1 (`evidence-r1/qa.py`, results in `evidence-r1/qa-results.json`, screenshots in `evidence-r1/`): 41/41 PASS. That covers overflow and image decoding for 4 routes x 4 viewports, the reference calculator results and the error state, waitlist invalid/valid, FAQ keyboard, history navigation, mobile menu and Escape, CTA targets and the only external link, reduced motion, and no external requests.
- Visual re-check of the 1440 home and the 390 how view. Fixes confirmed. No regression seen.
- `web-delivery-r1.json` validated with `scripts/creative_web.py validate` -> ok (build hash 07148cf9...).

## Known limitations (unchanged)

No human visual review; Chromium only; no screen reader pass; waitlist is local only by design.
