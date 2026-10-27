# Execution record · R1 (self-review, no external feedback)

- Start (UTC): 2026-10-21T12:56:23Z
- End (UTC): 2026-10-21T12:59Z (system clock; perceived active time about 10 to 12 minutes)
- Method: same `WEB_PREVIEW` / FAST profile (Web Experience v0.2, step 7 QA: 1440/390, 320 overflow, 768 useful) and `rubric.md`. r0 left untouched; r1 = copy of r0 plus CSS-only changes.

## Review against the rubric (r0 evidence, including the screens not inspected in R0: 320, 768, mobile how/waitlist)
- Art direction, typography, images, components, interactions, fidelity: no relevant problem found. Ledger-on-paper idea holds on every route; required copy and testids intact.
- Responsiveness (problems found):
  1. 320px: the hero "Practice, at a glance" ledger card squeezed labels into 2 to 3 line stacks ("When / you / claim") beside the numbers.
  2. 390px and 320px: the four-column mobile nav made "How it works" and "Your system" run together visually (390) and wrap to two lines (320).
  3. 768px: hero plate limited to 560px and left-aligned left a dead right side under a full-width title, and the display sizes stayed near their minimum, so the tablet hero read as an enlarged phone layout.

## Fixes (r1/styles.css only, appended "R1 refinements" block)
- Ledger rows stack label above number at ≤420px (clean two-line rows, numbers 22px).
- Mobile nav uses content-sized columns with `space-between` and tighter padding; all four labels sit on one line at 390 and 320, with 48px tap height preserved.
- ≤900px: display type scales up (`clamp(42px, 7.6vw, 72px)`; page titles `clamp(38px, 6.4vw, 60px)`), hero plate goes full width with a 16:9 crop (object-position 50% 75% keeps palm, shore and sea); ≤560px returns to the 3:2 crop.

## Preserved
HTML, JS, copy, routes, testids, assets, fonts, desktop composition (1440 rules unchanged: all new rules are inside max-width media queries).

## Checks (Playwright, `evidence-r1/qa.py`, screenshots in `evidence-r1/`)
- Same 50-check suite as R0 against r1: 50/50 PASS (overflow at 1440/390/768/320 on all routes, no external requests, no JS errors, nav + back/forward, 8 steps, CTA href, 40/30/0 and 70/50/0 references, invalid/valid email, FAQ keyboard, focus, alt, reduced motion).
- Visual: compared 320/390/768 home hero before and after; full 768 home reviewed. `diff -rq r0 r1`: only styles.css differs.
- Regressions: none observed.

## Remaining limitations
Same as R0 (no `web-delivery` JSON record, reduced motion verified by computed style, no screen-reader test). Tablet layouts of how/system/waitlist checked by overflow test only.
