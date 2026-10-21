# Execution record: R1 self-review, diBoaS Practice website

- Start (UTC, container clock): 2026-10-21 12:56:30 (copy of r0 to r1)
- End (UTC, container clock): 2026-10-21 12:59:15 (last build hash), record written right after
- Note: as in R0, the container clock reads shorter than the felt work time. I estimate about 10 to 12 minutes of active work, which is inside the 15-minute limit.
- Delivery: `/tmp/r3/f58/r1/index.html`. r0 is unchanged (hashes still e3eb8062 / 704c2ea8 / 60ee06f4).
- r1 hashes (sha256): index.html `46380803...556a`, styles.css `fcfb949d...26ca`, app.js `83e9812d...6d83`.
- Method used for the review: the same files read in R0 (Web Experience profile: browser QA at 1440/390 with 768/320, form truth, UI truth, phone readability from Typography & Layout) and `rubric.md`. No new method files were read.

## Problems found (self-review against the rubric)

1. Clarity/usability, UI/interactions (390 px): on Your system, the results panel sat below the inputs. On a phone the visitor typed percentages and saw no change near the fields.
2. Typography/hierarchy (1440 px home): the hero title at up to 92 px broke into five lines with single words per line ("Practice / money / decisions / before they're / real."). The stair step was awkward and pushed the actions down.
3. Responsiveness (390 px): the sticky two-row header (logo, CTA, four nav links) covered about 13% of the screen while scrolling and overlapped content in long views.
4. Art direction/identity (brand colour rule): the home "Your system" teaser drew its example bars in teal, but teal is reserved for action and live data, and those bars are a static example.
5. Found while fixing item 1, before delivery: my first version of the new inline Available line computed `1000 - sum of percentages` (for example 930 for 70%), which was a misleading amount. Fixed before delivery to `1000 x (100 - sum) / 100`, and a check now confirms it matches the receipt.

Checked and judged OK, so no change: colour contrast measured for the key pairs (copper text on paper 5.24:1, muted ink on paper 5.96:1, teal on paper 4.82:1, paper on teal button 5.2:1, light text on deep ink 7.9 to 11.5:1, error red on paper 5.95:1). Form state after browser back/forward stays as entered (verified). The R0 note about "inputs reset after back/forward" was a screenshot from a fresh browser context, not a bug.

## Fixes made in r1

- Your system form: under "Assigned: X% of 100%" there is now a live line "N practice credits stay in Available." in teal (live data). It is hidden while there is an error, so no misleading amount shows. The receipt and all `data-testid` elements are unchanged.
- Hero (desktop): grid set to 1.2fr / .8fr, title clamp max lowered to 78 px. The title now reads in three lines ("Practice money / decisions before / they're real."). The at-a-glance card is slightly wider and offset, and its labels no longer wrap.
- Header: not sticky at 900 px and below. It stays sticky on desktop. Navigation is unchanged and still visible at the top of every view, and the footer nav repeats it.
- Teaser example bars: now ink grey, with the copper hatch for Available. Teal stays for actions and live data only.

## Preserved

All required copy, FAQ answers, footer text, routes, `data-testid` hooks, the 40/30/0 and 70/50/0 behaviour, waitlist behaviour, images and crops (except the hero column width), type system and colour system.

## Regressions and checks

- Full QA script `evidence-r1/qa.py` (same 38 checks as R0, pointed at r1): 38/38 PASS. Covers no external requests, nav visibility at 1440/768/390/320, CTA href and same tab, eight how-steps, reference results, error, back/forward, waitlist invalid/valid, FAQ keyboard, skip link, alt, banned words, no horizontal overflow at four widths on four routes, reduced motion.
- Added 2 checks: the inline Available equals the receipt Available (300 for 40/30/0), and the inline line is hidden on error. Both PASS.
- Visual: 1440 hero screenshot (`evidence-r1/1440-hero.png`), 390 form in error and valid states (`evidence-r1/390-form-pair.png`), full-page screenshots regenerated in `evidence-r1/`.
- No regressions found.

## Remaining limitations

- Self-review only; no human, screen reader or real-device test.
- On mobile the full receipt (per-goal amounts and bar) is still below the form; only the Available line was brought next to the inputs.
- No `web-delivery` JSON record was produced or schema-validated.
