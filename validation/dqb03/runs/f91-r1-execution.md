# Execution record, DQB-03 run f91 (R0)

- Start (UTC): 2026-10-21T12:54:39Z (first shell command)
- End (UTC): 2026-10-21T13:03:33Z (container clock; approximate active work about 25 minutes of wall time)
- Route: WEB_PREVIEW, FAST flow (Work Profile Web Experience v0.2).

## Method files actually read
- ai-creative-skill/SKILL.md (full). Routing: "If the user requests a landing page, website or functional preview, route to WEB_PREVIEW ... Default FAST ... actually build and open navigable desktop/mobile preview → QA".
- references/AI_Creative_Skill_Work_Profile_Web_Experience_v0.2.md (full). Applied: minimal FAST flow steps 1-8, step 3 "Diverge, then choose" (two or three contrasting directions, record losers, borrow at most one element), QA at 1440/390, 320 overflow, 768 optional, scroll full page before judging images, keyboard/CTA/form-truth risks, reduced motion observed.
- references/AI_Creative_Skill_Deliverable_Completeness_Catalog_Pre-v0.1-V2.4-CANDIDATE.md: grep only for web/site/landing (SKILL.md says to load it for full deliverables); it contains no web contract, so nothing further applied.
- web/docs/DELTA_AND_GATES.md (first 60 lines, partial): form classes (LOCAL_CALCULATION vs real capture), STATIC vs BROWSER evidence.
- scripts/creative_web.py --help only. Not used: preview server (file:// opened directly in Chromium, as INSTRUCTIONS allow) and schema validation of a delivery record (optional, skipped for time).
- Not read: other references (ads, media, video, etc.) as the method says load only what the task needs.

## WEB_BRIEF (condensed)
- Truth: brief.md only. Audience: adult failed by the financial system, including older non-technical reader. Primary action: "Start practicing" -> https://app.diboas.com same tab. Secondary: waitlist (local only).
- Unknowns kept unknown: no app screenshots, no figures beyond the brief.
- Forms: Your system = LOCAL_CALCULATION; waitlist = local validation only, confirmation states nothing was sent and no real list was joined (no fake signup).

## Direction (step 3, diverge then choose)
- A. "Ledger on paper" (CHOSEN): type-led hero, large Fraunces serif on paper #f4f0e8 with an italic copper second line; a ruled ledger card built in HTML (10,000 / 1,000 / 20,000 / real money that moves 0, all brief numbers, labelled as a drawing not an app screen); copper hairlines and double rule totals; photography supporting, not protagonist. Derived from the tagline "Your money deserves an explanation" and "Every cent accounted for. Every balance reconciles."
- B. "Coast, day and night": full-bleed Practice coast illustration hero with overlaid type, deep ink #0b1f24 dominant, weeks as a horizontal timeline. Lost: overlaid type on a pale watercolour weakens legibility for an older reader and makes the page feel like a product mood piece rather than an explanation.
- C. "Human split": split hero with the older-man portrait, sans-only (Space Grotesk/Inter), card grid of steps. Lost: closest to a generic fintech template; risks reading as testimonial/social proof with an unnamed person.
- Borrowed one element from B: the coast illustration as a full-width band under the hero (light, Practice today) and the night coast as the deep-ink waitlist surface (real money, later).
- Type: Fraunces (display/headings, numbers), Inter (body), Space Grotesk (labels, buttons). Teal only on actions and live/calculated numbers; copper for ornaments and labels; deep ink for night band, waitlist and footer.

## Build
- r0/index.html, r0/styles.css, r0/app.js; assets/ and fonts/ copied. No framework, no network. Hash routes: #/ , #/how, #/system, #/waitlist with back/forward, aria-current, focus to h1 on route change, mobile menu disclosure (Escape closes).
- Build hashes: evidence-r0/build-hash.txt.

## Checks (BROWSER_OBSERVED, Playwright Chromium, file://, same build hash)
Script evidence-r0/qa.py, output evidence-r0/qa-result.json, screenshots evidence-r0/shots/.
- 4 routes x 1440, 390, 768, 320 after full-page scroll: horizontal overflow 0 everywhere; no broken images; no console errors: PASS.
- External requests on load and navigation: none: PASS. All cta-practice links -> https://app.diboas.com/, no target: PASS.
- how-step visible on #/how: 8: PASS.
- Your system: initial 0/0/0, Available 1,000; 40/30/0 -> 400/300/0, Available 300, no error: PASS; 70/50/0 -> error visible, amounts and Available show a dash (no negative values): PASS; 12.5 -> error (whole numbers): PASS.
- Waitlist: invalid email -> inline error, no confirmation: PASS; valid -> confirmation, no error: PASS.
- Back navigation #/how -> #/system -> back -> #/how visible: PASS.
- FAQ keyboard: Enter opens, Space closes, 4 faq-item: PASS. Visible focus ring screenshot faq-focus-1440.png.
- Mobile 390: menu opens, link navigates and closes menu; Escape closes and returns focus to menu button: PASS.
- prefers-reduced-motion: route animation computed as none: PASS.
- data-testid counts all present (see qa-result.json).
- Copy scan for banned words (yield, APY, DeFi, safe, unlock, seamless, empower, Sandbox, best, rewards, em-dash, etc.): only hits are verbatim required text (FAQ "not a guarantee", footer "guarantees", "Rewards", "crypto-assets").
- Visual review of screenshots: home 1440/390, how 1440, system 390 and error state 1440, waitlist 1440/390; fixed coast band crop, older-man crop on mobile, and waitlist night illustration visibility during the run.

## Known limitations
- At 1440 the Your system error message sits below the fold under "Stays in Available"; inputs turn red and amounts switch to a dash immediately, but the text of the error needs a scroll.
- Calculator amounts are shown as a dash during an error (en dash character, not an em-dash).
- Delivery record (web_delivery JSON) not produced and not schema-validated; creative_web.py preview server not used (file:// served directly).
- 768 and 320 screenshots were checked numerically (overflow, images, errors), only partially by eye.
- No human/user approval; QA PASS is not approval. Nothing published.
