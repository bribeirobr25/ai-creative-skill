# Execution record · R0 · diBoaS Practice

- Start (UTC): 2026-10-21T12:44:20Z
- End (UTC): 2026-10-21T12:53Z (system clock; approx. 25 to 30 minutes of active work as perceived)
- Route: `WEB_PREVIEW`, mode FAST, `execution_mode` MANUAL_SPEC_GUIDED (built by hand with host file/shell tools following the Web Experience profile; the skill's scripts do not generate sites).

## Method files actually read
- `ai-creative-skill/SKILL.md` (full): routed to WEB_PREVIEW per "Web Experience · new in V2.5".
- `references/AI_Creative_Skill_Work_Profile_Web_Experience_v0.2.md` (full): FAST flow, "Diverge, then choose", QA viewports 1440/390/320 (+768), scroll before judging images, form truth, reduced motion.
- `references/AI_Creative_Skill_V2.5_Integration_Manifest.md` (full).
- `references/AI_Creative_Skill_Deliverable_Completeness_Catalog_Pre-v0.1-V2.4-CANDIDATE.md`: headings only (grep). Its contracts (character bible, content idea, storyboard, video direction, reference manifest) do not cover websites, so not applied.
- `web/docs/DELTA_AND_GATES.md` (first 60 lines): form classes (`LOCAL_CALCULATION`), browser-evidence gates.
- `web/schemas/web_delivery_v0.2.schema.json` (first ~6000 chars): record shape. Optional delivery record not produced (see limitations).
- `scripts/creative_web.py --help` only. Preview helper not used; the site is opened via `file://` as the instructions require.

## WEB_BRIEF (summary)
Truth: `brief.md` only. Audience: smart adult failed by the financial system, including older non-technical readers. Primary action: "Start practicing" to https://app.diboas.com (same tab). Secondary: local waitlist. Unknowns kept out: no amounts, fees caps, returns, counts or app screens. Forms: Your system = `LOCAL_CALCULATION`; waitlist = local validation only, confirmation states nothing was sent.

## Direction: diverge, then choose
- A. "The ledger on paper" (chosen). Type-led hero in Fraunces with a copper italic turn ("before they're real."), paper surfaces, ruled ledger lines, numbered entries, copper as the editorial accent and teal only on actions and live numbers. Derived from the tagline "Your money deserves an explanation" and the brief's "Every dollar is explained / Every balance reconciles". Photography supporting, framed in plates.
- B. "Coast at dawn": full-bleed Practice watercolour coast hero with overlaid type, night coast for dark sections, very spacious. Lost because a full-bleed pale illustration weakens text contrast and hierarchy for an older reader, and it reads more as a mood piece than an explanation.
- C. "Calendar that keeps moving": split hero with a CSS week-calendar, Space Grotesk throughout, dense deep-ink grid, photos as texture. Lost because density and a dark, techy surface fight the brief's calm peer voice and the paper/copper warmth.
- Borrowed from B (one element): the Practice app illustrations as the product's "window": light coast framed in the hero plate under a ledger card; night coast behind the dark "Real money is not live" band.
- Type: Fraunces (display, quotes), Inter (body), Space Grotesk (labels, buttons). Colours exactly from the brief; no #000/#fff, no gradients other than an ink scrim over the night illustration.

## Structure
Hash routes: `#/` home, `#/how` (eight steps), `#/system` (local preview), `#/waitlist`. Home: hero + ledger card (only brief numbers: 10,000 / 1,000 / 20,000), What Practice is, eight-step cycle overview, "it can fall" quote with older-man photo, Your system teaser, FAQ (5 items, the four required answers verbatim plus progress-saved fact), dark waitlist band. Footer with all six required lines verbatim on every route. Images used: practice-coast-light, practice-coast-night, morning-pause, moment-of-ease, how-it-works-path, veil-of-dawn, logos (unaltered).

## Checks performed (Playwright Chromium, file://; script `evidence-r0/qa.py`; final run 50/50 PASS)
- No horizontal overflow on all four routes at 1440×900, 390×844, 768×1024, 320×740 (full-page scroll before capture).
- Zero non-file network requests and zero JS errors at all four viewports.
- Nav testids reach each view on desktop and mobile; browser back/forward across hash routes.
- 8 visible `how-step` on `#/how`; `cta-practice` href = https://app.diboas.com with no target.
- System: empty start gives 0/0/0 and 1,000 Available; 40/30/0 gives 400/300/0 and 300; 70/50/0 shows error and "Not calculated" (no negative values); 101 and 2.5 show error.
- Waitlist: invalid email shows inline error and no confirmation; valid email shows confirmation containing "nothing was sent".
- FAQ toggles with Enter and Space (native details/summary); visible focus outline on Tab; all images have alt; `prefers-reduced-motion: reduce` neutralises animation (observed computed duration).
- Visual review of screenshots (desktop home/how/system/waitlist, mobile home/system): fixed the hero plate crop (4:5 crop showed only sky; now natural 3:2 with the ledger card overlapping), removed "0" placeholders (could read as pre-filled), changed "Until then" to "Today, Practice is open" (avoids implying a launch), error state now empties the split bar.
- Copy scan: no em-dashes, none of the banned words in authored copy ("crypto-assets" appears only inside the required verbatim footer line).
- Evidence: `evidence-r0/*.png`, `evidence-r0/contact.jpg` (asset contact sheet).

## Known limitations
- Optional `web-delivery-r0.json` record not written or validated (time budget); QA evidence is the script and screenshots, not schema records.
- Screenshots reviewed for desktop and mobile main routes; 768 and 320 checked by overflow test and one home capture each, not reviewed in detail.
- Reduced motion verified by computed style only; screen reader output not tested.
- Full-page screenshots show the sticky desktop header mid-page (capture artefact, not a layout bug).
- Fonts limited to Fraunces, Inter, Space Grotesk (trimmed `fonts/fonts.css`; OFL licences copied).
- Status: PREVIEW_DRAFT, QA verdict PASS for the checks listed; not user-approved.
