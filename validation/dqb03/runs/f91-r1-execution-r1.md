# Execution record, DQB-03 run f91, round R1

- Start (UTC): 2026-10-21T13:04:24Z
- End (UTC): 2026-10-21T13:06:25Z (container clock; about 10 minutes of active work)
- r0 left untouched (r0 hashes still match evidence-r0/build-hash.txt). r1 = copy of r0 plus the fixes below.
- Method: same as R0 (SKILL.md -> Work Profile Web Experience v0.2, QA guidance: 1440/390, 320 overflow, 768, keyboard, form truth). No new method files read. Rubric: rubric.md.

## Review findings (self-review against rubric and method)
1. Clarity/usability, UI (1440): the Your system error message sat at the bottom of the card, below the fold. A user who enters 70/50 sees red inputs and dashes but not why. Severity: medium.
2. Responsiveness (768): below 900px, "What Practice is" and "Your system" fell to one column. At tablet width this gave a ~480px-tall full-width portrait and a long single column, plus a full-width ledger card with numbers far from labels. Severity: low-medium.
3. Brand fidelity: "Real money that moves 0" in the hero ledger used teal, which the brief reserves for action and live data. That number is a static statement. Severity: low.
4. Observed but no change needed: functional checks, copy, required text, footer, images and 390/320 layouts were already in order.

## Fixes in r1
- index.html: moved the system-error element (same data-testid, role="alert") to the top of the calculator card, under "This week 1,000 practice credits" and above the goal rows. It is now visible without scrolling at 1440 (y about 666) and 768 (y about 552).
- styles.css: the split and system sections stay two-column down to 760px (single column only at 760px and below); the ledger card has a max-width of 36rem in single column; calculator rows are tighter between 761 and 1060px (100px input, 76px amount) so "Emergency reserve" stays on one line at 768; the ledger total "0" is ink, not teal.
- app.js: unchanged.

## Preserved
Direction ("Ledger on paper"), all copy, routes, data-testids, images and crops, mobile menu, waitlist behaviour, 390/320 layouts (the new 760px breakpoint keeps them identical).

## Checks on r1 (BROWSER_OBSERVED, Playwright Chromium; evidence-r1/qa.py, qa-result.json, shots/, build-hash.txt)
- 4 routes x 1440/390/768/320: overflow 0, no broken images, no console errors.
- No external requests; cta-practice -> https://app.diboas.com/ in the same tab (5 links).
- 8 how-step; 40/30/0 -> 400/300/0, Available 300; 70/50/0 -> error plus dashes; 12.5 -> error.
- Waitlist invalid -> error, no confirmation; valid -> confirmation.
- Back navigation, FAQ Enter/Space, mobile menu plus Escape, reduced motion: same results as R0 (PASS).
- Visual: system-error-1440.png and system-error-768.png (error in view), system 768 card, home 768 two-column section.

## Regressions
None detected by the checks above. Not re-inspected by eye in R1: 320 screenshots; they were checked automatically (overflow, images, errors).

## Remaining limitations
- The error uses an en dash for the hidden amounts.
- No web-delivery JSON record or schema validation.
- No user approval; nothing published.
