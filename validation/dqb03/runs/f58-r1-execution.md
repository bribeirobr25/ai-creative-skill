# Execution record: R0, diBoaS Practice website

- Start (UTC, container clock): 2026-10-21 12:44:18
- End (UTC, container clock): 2026-10-21 12:51 (approximately; last build hash at 12:50:48)
- Note: the container clock reports about 7 minutes between first and last command. My own estimate of active work (reading, building, QA, two screenshot review passes) is about 20 to 25 minutes. Both are given; the clock values are the only measured ones.
- Delivery: `/tmp/r3/f58/r0/index.html` (open via `file://`), with `styles.css`, `app.js`, `assets/`, `fonts/`.
- Build hashes (sha256): index.html `e3eb8062...b72b`, styles.css `704c2ea8...8394`, app.js `60ee06f4...cfb6cd`.

## Method files actually read

- `ai-creative-skill/SKILL.md` (full). Routed to `WEB_PREVIEW`, mode FAST.
- `references/AI_Creative_Skill_Work_Profile_Web_Experience_v0.2.md` (full). Followed the FAST flow: brief, provisional direction, reuse of supplied assets, build, browser QA at 1440/390 plus 320 overflow and 768, scroll before judging images, form truth, keyboard, reduced motion.
- `references/AI_Creative_Skill_V2.5_Integration_Manifest.md` (full).
- `references/AI_Creative_Skill_Deliverable_Completeness_Catalog_Pre-v0.1-V2.4-CANDIDATE.md` (full; none of its domain contracts apply to a website, so the brief's required-content list was used as the completeness checklist).
- `web/README_PTBR.md`, `web/docs/DELTA_AND_GATES.md` (full). Took the form taxonomy (`LOCAL_CALCULATION` for Your system, no fake successful signup) and the STATIC vs BROWSER_OBSERVED distinction.
- `scripts/creative_web.py` (full, a thin wrapper) and the first ~3,000 characters of `web/schemas/web_delivery_v0.2.schema.json` (top-level required fields and enums only).
- `references/AI_Creative_Skill_Method_Typography_Layout_Pre-v0.8.md`, partial: sections 1 Trigger, 3 Hierarchy, 4 Composition and Spacing, 5 Phone-Size Readability, 6 Controlled Finishing, 7 UI Truth, 10 Acceptance Rubric. Applied "UI truth" (the at-a-glance card and the split preview show only brief numbers, no fake app screen or balance) and phone readability.
- Not read: other references (Architecture, Execution Contracts, Image Direction, etc.), as the web profile did not require them for this bounded preview.

## Direction decisions (provisional)

- Idea: "a calm ledger on paper". Warm paper (#f4f0e8 / #ebe5d8) and editorial ink carry the page; copper is used for rules, step numerals and kickers; teal is used only for actions (buttons, links) and live data (the numbers and bars in Your system and the at-a-glance figures). Deep ink #0b1f24 for the dark bands (time machine, real money, waitlist, footer). No gradients beyond dark scrims over photos.
- Type: Fraunces (the Practice app face) for headlines and pull quotes, Inter for body at 17 to 18px for older readers, Space Grotesk for labels and tabular numerals. All self-hosted from `fonts/`.
- Images: the Practice app illustrations anchor the product (coast light in an arch on the hero; coast night behind the real-money band and the waitlist page). `veil-of-dawn` sits with the time machine message "It can fall." `moment-of-ease` (older man, coffee) sits with "No rush and no deadline". `how-it-works-path` in the How page sidebar. Cropped only with CSS `object-fit`.
- Structure: hash routes `#/`, `#/how`, `#/system`, `#/waitlist`; focus moves to the view heading on route change; active nav uses `aria-current`. Home: hero with both actions and an at-a-glance card, statement band, 8-step cycle grid, time machine band, Your system teaser, real money band, FAQ. FAQ uses native `details/summary` (keyboard operable).
- Your system: empty inputs (nothing pre-filled) count as 0. Sum over 100 or any value that is not a whole number 0 to 100 shows an error and replaces all amounts with an en dash, and the bar empties, so no negative or misleading amounts appear.
- Waitlist: local regex validation; invalid shows inline error and no confirmation; valid shows "Thank you. This is only a preview. Nothing was sent and your email was not stored. This page is not connected to a real waitlist."
- Copy: all brief quotes and FAQ answers verbatim; footer verbatim (including the required crypto-assets sentence, which is the only place that word appears). Added connective copy only, with no new facts or numbers.

## Checks performed (browser-observed, Playwright Chromium, `evidence-r0/qa.py`, results in `evidence-r0/qa-results.json`)

38 checks, 0 failures on the final build:
- No external requests on load (only file://). No page errors.
- nav-home/how/system/waitlist visible at 1440, 768, 390, 320.
- cta-practice href is `https://app.diboas.com`, no target (same tab).
- `#/how` shows exactly 8 visible `how-step`.
- 40/30/0 gives 400 / 300 / 0 / 300 in Available, no error. 70/50/0 shows error, no negative amount. 150 shows error.
- Browser back and forward between routes.
- Waitlist invalid email: error visible, confirmation hidden. Valid email: confirmation visible containing "Nothing was sent".
- 4 FAQ toggles; open with Enter and close with Space by keyboard.
- Skip link is first in tab order. All images have alt (decorative background has empty alt).
- Banned-word scan of visible text (em dash, Sandbox, yield, APY, DeFi, stablecoin, blockchain, risk-free, guaranteed, safe, passive income, unlock, seamless, empower, most popular, best): none found.
- No horizontal overflow at 1440, 768, 390, 320 on all four routes.
- `prefers-reduced-motion: reduce` observed: view animation duration collapses to 1e-06s.
- Visual review of full-page screenshots (1440 and 390: home, how, system, waitlist; 768 and 320 home). One repair pass: hero arch crop moved to keep the palm in frame, mobile arch shows the whole illustration, waitlist illustration made visible behind a left-side scrim, eyebrow dot alignment.

## Known limitations

- Self-review only; no independent or human review, no screen reader or physical device test.
- On mobile, the Your system results panel sits below the inputs, so the visitor scrolls to see the split (the results region is `aria-live`).
- Sticky header appears mid-page in full-page screenshots (a screenshot artifact, not a layout bug).
- The method's optional delivery record (`web-delivery-r0.json`) was not produced or schema-validated; the local preview helper (`creative_web.py preview`) was not used, the site was opened directly via `file://`.
- Teal is also used for the example bars on the home Your system teaser (illustrative data, labelled "Example split. You set your own.").
- Contrast was checked by eye, not measured with a tool.
