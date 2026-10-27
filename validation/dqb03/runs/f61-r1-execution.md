# Execution record · run f61 · R0

- Start (UTC): 2026-10-21T12:54:40Z (first command, reading INSTRUCTIONS.md)
- End (UTC): 2026-10-21T13:05:15Z (after record validation, while writing this file)
- Active time: about 11 minutes by the machine clock.
- Deliverable: `r0/index.html` (+ `styles.css`, `app.js`, `assets/`, `fonts/`). Hash routes `#/`, `#/how`, `#/system`, `#/waitlist`; `#/how?step=N` deep-links a step.

## Method files actually read

- `ai-creative-skill/SKILL.md` (full). Routed to `WEB_PREVIEW`, FAST mode.
- `references/AI_Creative_Skill_Work_Profile_Web_Experience_v0.2.md` (full): FAST flow (brief, direction, minimal assets, build, browser QA, deliver and stop).
- `web/docs/DELTA_AND_GATES.md` (full): form modes, evidence per check, preview gates.
- `references/AI_Creative_Skill_Deliverable_Completeness_Catalog_Pre-v0.1-V2.4-CANDIDATE.md` (partial: headings and section 1 "Execution sequence"; it has no web contract, so no further rubric applied).
- `web/schemas/web_delivery_v0.2.schema.json` (properties, $defs, allOf) and `web/runtime/validate.py` (lines ~45-125, check logic and build hash) to produce a valid delivery record.
- Not read: the other references (ads, organic, video, audio, typography etc.) as the method does not point to them for a web preview.

## WEB_BRIEF (summary)

Digital product, financial-facing. Product truth is only `brief.md`. Unknowns kept unknown: no app screenshots, no real-money terms, no launch timing. Primary action: "Start practicing" to https://app.diboas.com, same tab. Claim boundary: never sell, promise or advise; credits are never money; diBoaS is not a bank; footer verbatim.

## Direction decisions ("the rehearsal ledger")

- Paper `#f4f0e8`/`#ebe5d8` ground, ink `#14110f`, copper `#b67d44`/`#875a2b` for rules, eyebrows and step numbers; deep ink `#0b1f24` for the time machine band, the waitlist and the footer. Teal `#0f766e` only on buttons, links and live numbers (calculator amounts, weekly 1,000); `#14b8a6`/`#0d9488` only in the calculator split bar and status dot. No pure black/white, no gradients except ink overlays on photos.
- Type: Fraunces (Practice app font) for display and step titles, Inter for reading, Space Grotesk for figures and labels. All local from the shared pool.
- Home: hero with the Practice coast illustration (light) framed as a slightly tilted paper print, four plain facts strip, an eight-column "cycle rail" (each cell links to its step), Your system teaser (morning-pause photo), a dark "time machine" band that states loss plainly over veil-of-dawn, real-money section (saved-through-time notebook), FAQ accordion.
- How: eight steps in three groups, each anchored by a sticky portrait crop (how-it-works goal/path/move), quotes set in serif italic, reference cost shown as two plain values with its "for information only" note.
- Your system: calculator card, empty inputs (nothing pre-filled, treated as 0), live split bar, Available row; error state hides all amounts ("Not shown") and explains the total; decimals or out-of-range also error. Side photo of the older man for the older reader.
- Waitlist: dark page under the night coast illustration; local email check; confirmation says nothing was sent and no account was created.
- Supporting copy was kept to brief facts; no extra numbers.

## Checks performed (Playwright Chromium, file://)

Script `evidence-r0/qa/qa.py`, results `evidence-r0/qa-results.json`, screenshots in `evidence-r0/`. All 41 checks PASS:
- No horizontal overflow and all visible images decoded for 4 routes at 1440x900, 390x844, 768x1024, 320x740 (after full scroll).
- 8 `how-step` on the how view (and 8 in the document).
- Your system: 40/30/0 gives 400/300/0 and 300 Available; 70/50/0 shows `system-error` and no amounts; 100/0/0 gives 1,000/0/0/0; 12.5 errors.
- Waitlist: invalid email shows inline error, no confirmation; valid shows local confirmation with "Nothing was sent".
- FAQ toggles with Enter and Space; focus outline visible on Tab; back/forward history between routes; all nav testids work; mobile menu open, navigate, Escape.
- Every `cta-practice` is https://app.diboas.com with no target; the only external link in the page.
- Reduced motion: animation duration ~0 under `reduce`.
- No non-file network requests on any route/viewport.
- Static: grep for banned words and em-dashes; only hits are the required verbatim footer/FAQ text ("guarantee", "crypto-assets").
- Delivery record `web-delivery-r0.json` validated with `scripts/creative_web.py validate` -> ok, no errors (build hash f82387af...).
- Screenshot review by the executor at 1440 and 390 led to fixes: hero crop (empty sky), brighter time-machine band, instant scroll on route change, error moved above the goals, dark-page CTA switched to teal.

## Known limitations

- No human visual review; only executor screenshot review.
- Tested only in Chromium; no Safari/Firefox, no real screen reader pass.
- Waitlist is a local check only by design; nothing is stored.
- Full-page screenshots with the sticky header can show it mid-page; this is a capture artifact.
- The truths strip borders run to the container edge while text aligns with the gutter, a minor alignment choice at 1440.
