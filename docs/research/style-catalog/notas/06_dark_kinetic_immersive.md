# Dark / Tech, Kinetic Typography, Immersive Scroll Storytelling: web design style reference (2025–2026)

Notes for the website-generation catalog. Implementation target: static HTML/CSS/vanilla JS, self-hosted OFL fonts, WCAG 2.2 AA, prefers-reduced-motion.
Labels used: **[cited]** = from a source fetched in this session. **[synth]** = my recommendation built from the cited material plus general practice. **[unverified]** = from prior knowledge, not checked in this session; verify before using as fact.

---

## Q1. Dark / Tech style: definition, origin, signature traits, sub-variants

### Takeaway
The dark SaaS look is widely called "Linear style" or "Linear design", after the product-planning tool Linear. Its marks are a near-black background (not pure #000), monochrome palettes with high contrast, bold sans type, complex gradients or glows, soft shadows and glass, and one strict top-to-bottom reading path. Practitioners now say it is oversaturated and generic, so a site needs at least one distinctive element: a brand-tinted background, an unusual typeface, or a signature visual.

### Cited Findings
- **Definition:** "Linear design" is a layout style where content is "straightforward and sequential, highlighting logical progression." It is named after and was popularised by Linear, and it grew out of flat design's minimalism. — [LogRocket, Linear design](https://blog.logrocket.com/ux-design/linear-design)
- **Traits listed:** dark mode (the most obvious trait, though the author says "no real evidence it's better", so it is an aesthetic choice); bold typography; complex gradients for depth; glassmorphism; monochrome palettes with high contrast; soft shadows; strict linearity (no zig-zag content, one-dimensional scrolling, consistently aligned text, minimal CTAs). — [LogRocket](https://blog.logrocket.com/ux-design/linear-design)
- **How the reference sites changed:** Linear went from monochrome blue with a few bold colours (2024) to monochrome black and white with even fewer colours (2025). Raycast kept its bold red, dropped its gradient and added "noisy abstract visuals" in 2025. GitHub's 2025 site is criticised for leaning too heavily on glassmorphism and colour. — [LogRocket](https://blog.logrocket.com/ux-design/linear-design)
- **Background colour advice:** use the brand colour at 1–10% lightness. Pure black is "too black." — [LogRocket](https://blog.logrocket.com/ux-design/linear-design)
- **Critique:** the trend is oversaturated, many SaaS sites look alike, products become less memorable, and many such sites lack a light mode. — [LogRocket](https://blog.logrocket.com/ux-design/linear-design); see also [Anthony Hobday, A critique of the Linear website (2023)](https://anthonyhobday.com/blog/20230119.html) (not fetched) and [UX Collective / Bootcamp, The rise of Linear style design](https://bootcamp.uxdesign.cc/the-rise-of-linear-style-design-origins-trends-and-techniques-4fd96aab7646) (not fetched).
- **Linear's own UI redesign (March 28, 2024):**
  - Moved from HSL to an LCH-based theme generator, chosen because LCH is "perceptually uniform."
  - Each theme is defined by 3 variables (base colour, accent colour, contrast) instead of 98.
  - The colour calculations limit how much blue chrome is used, for a "more neutral, timeless" look.
  - A contrast variable can generate very high-contrast themes for accessibility (values of 30 and 100 are compared).
  - Early explorations built elevation from opacities of black and white.
  - Type: Inter Display for headings, Inter for all other text.
  - Page theme-color metadata: `#08090a`.
  — [Linear, How we redesigned the Linear UI](https://linear.app/now/how-we-redesigned-the-linear-ui)

### Inferences
**Sub-variants [synth]:**
1. **Linear/Vercel-style dark SaaS ("precision dark")**
   - Look: near-black, brand-tinted base (#08090a-ish); grey text ladder; one restrained accent; 1px hairline borders at about 6–10% white; subtle top-edge radial glow behind the hero; product screenshot in a bordered "window" frame; bento feature grid; logo wall; changelog and docs links.
   - Use for: dev tools, B2B SaaS, AI infrastructure, fintech dashboards.
2. **Cyber / neon / terminal**
   - Look: saturated accents (lime, cyan, magenta) on black; monospace-heavy; scanlines, noise, ASCII or CRT motifs; terminal-prompt hero; grid-line backgrounds; glitch micro-interactions.
   - Use for: security, crypto/web3, gaming, hackathons, devrel events. Poor fit for regulated finance or health.
3. **AI-lab "soft dark" / cinematic**
   - Look: dark charcoal or warm-dark grounds; large serif or grotesk display; gradient "aurora" or orb blobs; noisy abstract imagery (the Raycast 2025 direction cited above); generous whitespace.
   - Use for: AI model companies and research labs that want gravitas without hacker clichés.
4. **Luxury dark**
   - Look: black or deep brown base; high-contrast serif display (Didone style); gold or cream accent; full-bleed photography; very few UI elements.
   - Use for: watches, spirits, fashion, hospitality. This direction is borrowed from fashion and editorial design rather than the SaaS world.
- When to pick which [synth]: if the product is a tool developers use daily, use precision dark. Use cyber only when the audience self-identifies with hacker or gaming culture. Use cinematic for AI brands selling a vision. Use luxury dark for physical premium goods.

### Gaps
- No fetched source gives formal names or a taxonomy for the dark sub-variants. The four variants above are my synthesis.
- Vercel's design system (Geist) was not fetched. Geist and Geist Mono being OFL-licensed is [unverified] here; check [vercel.com/font](https://vercel.com/font).

---

## Q2. Dark / Tech: layouts, page patterns, navigation, mobile, typography, colour, techniques

### Takeaway
The standard page is a single, centred, linear column, max width about 1100–1280px:
- hero (headline, sub, 1–2 CTAs, framed product shot)
- logo strip
- bento feature grid
- deep-dive feature sections
- testimonials or metrics
- pricing
- final CTA
- multi-column footer

Contrast is the main risk: grey-on-near-black secondary text often fails 4.5:1.

### Cited Findings
- Linear design means minimal CTAs, minimal subject matter and one-dimensional scrolling. — [LogRocket](https://blog.logrocket.com/ux-design/linear-design)
- Linear uses Inter Display for headings and Inter for body; elevation comes from black and white opacities; there is a dedicated contrast variable. — [Linear](https://linear.app/now/how-we-redesigned-the-linear-ui)
- LogRocket also published a guide on implementing accessible Linear design across light and dark modes ([link](https://blog.logrocket.com/how-do-you-implement-accessible-linear-design-across-light-and-dark-modes/), not fetched).

### Inferences
**Layout patterns [synth]:**
- Sticky translucent top nav, 56–64px tall: `backdrop-filter: blur(12px)` over `rgb(8 9 10 / .7)`, with a 1px bottom border at about 8% white. Logo left, 4–6 links centre, "Log in" plus a primary CTA right.
- Mobile: hamburger opening a full-height sheet; CTA stays visible.
- Bento grid: `grid-template-columns: repeat(6, 1fr)` with tiles spanning 2, 3 or 4 columns. Collapses to 1 column below about 720px.
- Product "window" mockup: border-radius 12–16px, 1px border, inner top highlight, and a large soft glow behind it.

**Colour tokens (starting point) [synth]:**
- Backgrounds: `--bg: #08090a` (cited Linear theme colour); `--surface: #111214`; `--surface-2: #18191c`.
- Borders: `--border: rgb(255 255 255 / .08)`.
- Text: `--text: #f2f3f5`; `--text-2: #a1a3a8`. Check the secondary text against the background: it must be at least 4.5:1 for body text and at least 3:1 for large text or UI components (WCAG 2.2 AA, 1.4.3 / 1.4.11).
- Accent: one hue only. Define it in OKLCH or LCH so lightness steps look even, following Linear's LCH rationale.
- Avoid pure `#000` with pure `#fff` body text: halation makes long reading harder. Use off-white text around #e6e6e6–#f2f2f2.

**Recipes [synth], plain CSS:**
- **Grid-line background:**
  ```css
  background-image:
    linear-gradient(rgb(255 255 255 / .05) 1px, transparent 1px),
    linear-gradient(90deg, rgb(255 255 255 / .05) 1px, transparent 1px);
  background-size: 64px 64px;
  mask-image: radial-gradient(ellipse at 50% 0%, #000 30%, transparent 75%);
  ```
- **Dot grid:** `radial-gradient(rgb(255 255 255 / .08) 1px, transparent 1px) 0 0 / 24px 24px`.
- **Hero glow:** a pseudo-element with `background: radial-gradient(closest-side, oklch(70% .15 270 / .35), transparent)`, about 800×400px, `filter: blur(40px)`, `pointer-events: none`, placed behind the hero.
- **Gradient border, no extra markup:**
  ```css
  border: 1px solid transparent;
  background:
    linear-gradient(var(--surface), var(--surface)) padding-box,
    linear-gradient(135deg, rgb(255 255 255 / .25), rgb(255 255 255 / .02)) border-box;
  ```
  To animate the border angle, register the property with `@property --a { syntax: '<angle>'; inherits: false; initial-value: 0deg; }`, use `conic-gradient(from var(--a), …)`, and animate `--a`. Disable under reduced motion. Note: this repaints every frame and is not compositor-only, so use it on 1–2 elements at most.
- **Cursor-follow spotlight on cards:** a pointermove listener sets `--x`/`--y` on the card, and the card uses `background: radial-gradient(400px circle at var(--x) var(--y), rgb(255 255 255 / .06), transparent 40%)`. Throttle with requestAnimationFrame.
- **Noise texture:** an inline SVG `feTurbulence` used as a data-URI background at 3–6% opacity, which reduces gradient banding.

**Typography [synth/unverified licences]:**
- Inter or Inter Display (OFL; cited as Linear's choice).
- Geist and Geist Mono (Vercel; OFL [unverified]).
- Space Grotesk (OFL).
- IBM Plex Sans and Plex Mono (OFL).
- JetBrains Mono (OFL).
- Use mono only for code, labels, eyebrow text, and metrics. Set headings tight, letter-spacing -0.02 to -0.04em at 48–80px.

**Motion:** subtle only, 150–300ms ease-out on hover; fade-up reveals with `view()` (see Q7).

**Best fits [synth]:**
- Good fit: dev tools, AI/ML infrastructure, SaaS, crypto/DeFi, cybersecurity, gaming hardware, audio/creator tools.
- Poor fit: kids, food and hospitality (except luxury dark), healthcare patient-facing sites, government, local SMBs whose older audiences need high-legibility light pages, and content-heavy reading sites.

**Anti-patterns [synth + cited]:**
- Copying the template wholesale, which produces the "every SaaS looks alike" problem (LogRocket).
- Glass on everything (the GitHub 2025 critique).
- Low-contrast grey text.
- Several competing accent glows.
- No light mode or `prefers-color-scheme` option.
- Animated gradient borders on every card.
- Screenshot heroes shipped without width and height attributes, which causes CLS.

### Gaps
- No fetched source gives measured contrast data for actual SaaS dark sites.
- **Example sites:** commonly cited and current, but not fetched in this session.
  - [linear.app](https://linear.app) (cited via the Linear post)
  - [vercel.com](https://vercel.com)
  - [raycast.com](https://raycast.com) (cited via LogRocket)
  - [resend.com](https://resend.com)
  - [cursor.com](https://cursor.com)
  - [supabase.com](https://supabase.com)
  - Luxury dark [unverified as current]: rolex.com product pages.
  - Cyber [unverified]: many web3 and hackathon sites.

---

## Q3. Kinetic typography on the web: definition, traits, sub-variants

### Takeaway
On the web, kinetic typography means the type itself is the animated subject, through movement, transformation or timing, not just a fade-in. The main families are:
- marquees
- scroll-reactive type
- split-text reveals
- variable-font axis animation
- mask/clip reveals

All can be built without libraries using CSS animations, scroll-driven timelines and a small split script.

### Cited Findings
- **Definition:** "animated text where type is not displayed statically but brought to life through movement, transformation, or temporal sequencing." The type itself is the animation subject, which separates it from simple fade-ins. — [StudioMeyer, Kinetic typography (Nov 27, 2025; updated Sep 30, 2026)](https://studiomeyer.io/en/blog/kinetische-typografie)
- **Techniques named:**
  - scroll-triggered or scroll-reactive text: word-by-word reveal, parallax type, scale on scroll, colour transition
  - split-text by line, word or character
  - morphing text
  - variable-font animation (weight, width, slant, optical size, custom axes)
  - mask, clip and wipe reveals
  — [StudioMeyer](https://studiomeyer.io/en/blog/kinetische-typografie)
- **Numbers:**
  - Stagger: 30–50ms per character feels fluid; 100ms or more feels dramatic.
  - Word split suits headlines of 3–8 words; character split suits short text only.
  - Limit split-text to 2–3 elements per page.
  — [StudioMeyer](https://studiomeyer.io/en/blog/kinetische-typografie)
- **Tooling:** IntersectionObserver adds a class when an element enters view. GSAP ScrollTrigger is the usual library for scrub and pin. Subset fonts with glyphhanger or pyftsubset, because "a variable font is not automatically smaller." — [StudioMeyer](https://studiomeyer.io/en/blog/kinetische-typografie)
- Variable fonts let one file replace several static weights; animating weight and width on hover, scroll and viewport changes is common; custom axes (contrast, corner roundness, serif size) are possible. — [FontLab blog, Variable fonts in motion and UI (Mar 10, 2026)](https://blog.fontlab.com/2026/03/10/variable-fonts-in-motion-and-ui/) (light on code)
- Stripe is cited for subtle text animation; Apple product pages, Awwwards Site of the Day winners and type-foundry sites are cited as categories. — [StudioMeyer](https://studiomeyer.io/en/blog/kinetische-typografie)

### Inferences
**Sub-variants [synth]:**
1. **Marquee / ticker type**
   - What: huge display words in an endless horizontal loop, sometimes in two rows going opposite ways, or speed-linked to scroll.
   - Use for: brand energy, event lineups, agency and fashion sites.
   - Accessibility: needs a pause control (WCAG 2.2.2, see Q6).
2. **Scroll-reactive type**
   - What: words scale, shift, track or change colour as tied to scroll position, e.g. a sentence "lighting up" word by word as you scroll, or a giant headline that shrinks into the nav.
   - Use for: manifesto or mission sections, landing heroes.
3. **Variable-font axis animation**
   - What: weight, width, slant or custom axes breathe on hover, cursor proximity or scroll.
   - Use for: type foundries, creative studios, music and culture brands. Good for a playful but legible hero.
4. **Split-text reveal**
   - What: lines or words rise from a clipped mask, staggered, on load or entering view.
   - The most "safe" and corporate-friendly option: SaaS heroes, portfolios, editorial headlines.
- Optional fifth: **3D / perspective type** (letters rotating on X/Y, text on a cylinder). Use sparingly.

**Signature traits [synth]:**
- Oversized display type, often 10–20vw, as the main visual instead of images.
- Few words.
- Strong contrast: black/white or one vivid colour.
- Rhythm through stagger and repetition.
- Grotesk or condensed display faces.
- Motion that carries meaning (emphasis, sequence).

### Gaps
- No fetched source gives a formal taxonomy. The four variants are synthesised from the technique list.
- Fetched articles did not name current example sites with URLs. Candidate [unverified] examples to confirm before citing:
  - [Typewolf "Site of the Day"](https://www.typewolf.com/site-of-the-day)
  - [Awwwards typography collection](https://www.awwwards.com/websites/typography/)
  - [Dinamo](https://abcdinamo.com)
  - [Pangram Pangram](https://pangrampangram.com)
  - [Displaay](https://displaay.net)
  - [stripe.com](https://stripe.com) (cited above for subtle text animation)

---

## Q4. Kinetic typography: implementation (vanilla), typography choices, layouts, fits

### Takeaway
Build kinetic type with:
- a CSS keyframe marquee (duplicated content plus translateX -50%)
- `animation-timeline: view()` for scroll-linked reveals
- a 15-line split script (or CSS `--i` stagger)
- `font-variation-settings` / `font-weight` transitions

Animating font axes triggers layout, so keep it to short headline text.

### Cited Findings
- Animate only `transform` and `opacity`. Avoid `width`, `height`, `top`, `left`, `margin` and `font-size` (they trigger layout). `color` causes repaint, which is acceptable but not ideal. Measure `clip-path` on target devices. Use `will-change` selectively. Pause animations outside the viewport. Use requestAnimationFrame instead of setInterval. — [StudioMeyer](https://studiomeyer.io/en/blog/kinetische-typografie)
- Reduced motion: fall back to fades or static text; avoid infinite loops and autoplay; let users pause; keep contrast during animation; avoid flashing above 3Hz; provide a no-JS fallback where text is fully visible. — [StudioMeyer](https://studiomeyer.io/en/blog/kinetische-typografie)

### Inferences
**Recipes [synth]:**

- **Marquee, no library:**
  ```html
  <div class="marquee" aria-label="Brand · Brand · Brand">
    <div class="track" aria-hidden="true">
      <span>…</span><span>…</span>  <!-- content duplicated once -->
    </div>
  </div>
  ```
  ```css
  .track { display: flex; width: max-content; animation: m 30s linear infinite; }
  @keyframes m { to { transform: translateX(-50%); } }
  .marquee:hover .track,
  .marquee.paused .track { animation-play-state: paused; }
  @media (prefers-reduced-motion: reduce) { .track { animation: none; } }
  ```
  - Speed: about 40–80px/s for readable words. Edge fade: `mask-image: linear-gradient(90deg, transparent, #000 10%, #000 90%, transparent)`.
  - Add a visible pause/play `<button>`, required if the marquee runs more than 5s alongside other content (2.2.2).
  - Avoid the deprecated `<marquee>` element: axe rule "marquee elements must not be used" ([Rocket Validator / axe](https://rocketvalidator.com/accessibility-validation/marquee)).
- **Scroll-velocity marquee:** a rAF loop reads `scrollY` delta and adds it to the translate offset. Disable under reduced motion.
- **Split text, no library:**
  ```js
  el.setAttribute('aria-label', el.textContent);
  el.innerHTML = el.textContent.split(' ')
    .map((w, i) => `<span class="w" aria-hidden="true" style="--i:${i}"><span>${w}</span></span>`)
    .join(' ');
  ```
  ```css
  .w { display: inline-block; overflow: clip; }
  .w > span { display: inline-block; transform: translateY(110%);
    transition: transform .8s cubic-bezier(.2,.7,.2,1) calc(var(--i) * 40ms); }
  .in .w > span { transform: none; }
  ```
  - Trigger with IntersectionObserver (`threshold: .2`, `rootMargin: '0px 0px -10% 0px'`, unobserve after first hit).
  - Splitting single characters breaks screen-reader reading and ligatures. Keep aria-label on the parent; `Intl.Segmenter` handles grapheme-safe splitting (emoji, accents).
  - Re-split on resize only if splitting by line.
- **Scroll-lit sentence (CSS only):** each word gets `animation: lit linear both; animation-timeline: view(); animation-range: cover 30% cover 50%;`, going from `color: rgb(255 255 255 / .2)` to `#fff`.
  - Only colour changes, so it is not "motion animation" under the WCAG definition, which excludes colour and opacity changes ([W3C 2.3.3](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html)).
  - Check that the dim state still meets contrast, or treat it as decorative duplicated text.
- **Variable-font animation:**
  - Use the high-level properties `font-weight`, `font-stretch` and `font-style: oblique Xdeg` for registered axes. Use `font-variation-settings: "CASL" 1` only for custom axes.
  - Transition: `transition: font-weight .4s`. Hover "wave": per-letter `--i` delays.
  - Proximity effect: pointermove computes distance, then sets `--w` per span, then `font-variation-settings: "wght" var(--w)`.
  - Each frame causes text relayout, so limit it to one headline. Reserve width (fixed container or `font-variant-numeric: tabular-nums`) to avoid CLS-like shifts, and wrap in `prefers-reduced-motion: no-preference`.
  - Self-host with `@font-face { font-weight: 100 900; font-stretch: 75% 125%; }` ranges, WOFF2, subset, `font-display: swap`.
- **Free/OFL variable fonts [unverified licences, all on Google Fonts]:**
  - Roboto Flex: many axes, including wdth, wght, opsz, GRAD, XTRA.
  - Recursive: MONO, CASL, slnt, wght; good for tech plus playful.
  - Anybody: wdth 50–150, very elastic.
  - Big Shoulders Display: condensed.
  - Fraunces: SOFT, WONK, opsz serif.
  - Archivo: wdth.
  - Bricolage Grotesque: opsz, wdth.
  - Inter: wght, opsz.
  - Space Grotesk.
  - Unbounded: wide display.
  - Commercial icons of the style (Dinamo, Pangram) are not OFL.

**Layouts [synth]:**
- Full-viewport type hero (one statement at 12–18vw).
- Alternating marquee bands as section dividers.
- Manifesto section with scroll-lit words.
- Index/list pages with large hover-reactive row titles (agency work lists) and an image that follows the cursor.
- Footer with a giant wordmark.
- Mobile: cap display size with `clamp(2.5rem, 12vw, 9rem)`, drop per-character effects, keep at most one marquee, make hover effects tap-safe (no hover-only content).

**Fits [synth]:**
- Good fit: agencies and studios, fashion, music, festivals and events, sports, type foundries, bold DTC brands, campaign microsites.
- Poor fit: banking dashboards, medical, legal, long-form reading, accessibility-first public services, and any page where users must read text while it moves.

**Anti-patterns [synth]:**
- Animating body copy.
- Splitting every heading.
- Marquees without pause.
- Hiding critical text at `opacity: 0` until JS runs.
- Reveals that replay on every scroll.
- Several simultaneous loops.
- Animating `font-size` instead of `transform: scale`.

### Gaps
- No authoritative source fetched on the layout cost of variable-font axis animation. MDN's [Variable fonts guide](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_fonts/Variable_fonts_guide) is the recommended reference (not fetched).

---

## Q5. Immersive / scroll-driven / 3D storytelling: definition, sub-variants, layouts

### Takeaway
Immersive scroll sites turn the scrollbar into a timeline. Sections pin with `position: sticky`, and content (images, 3D scenes, text, video frames) changes with scroll progress. There are three main directions:
- **Parallax layers:** decorative depth.
- **Sticky scrollytelling:** pinned graphic with text steps; best for explanation.
- **WebGL/3D:** cinematic product and brand worlds; heaviest.

NN/g research shows that when the site alters scroll behaviour (scrolljacking), users get disoriented. Prefer native scroll and drive the effects from it.

### Cited Findings
- **Codrops sticky sections (Jan 31, 2024):** sticky sections of different sizes create stacking or collapsing effects; card stacking; rounded-corner and half-width variations; the focus is animating sections as they leave the viewport. The demo uses CSS `position: sticky` and JS animations, and the article says "CSS scroll-driven animations will very likely be able to replace them." Demo: tympanus.net/Development/StickySections/. — [Codrops](https://tympanus.net/codrops/2024/01/31/on-scroll-animation-ideas-for-sticky-sections)
- Codrops has also published experimental CSS-only carousels built with scroll-driven animations — [Codrops 2024](https://tympanus.net/codrops/2024/01/24/experimental-css-only-carousels-with-scroll-driven-animations) (not fetched).
- **NN/g on scrolljacking (Aug 6, 2023):** scrolljacking means changing scroll speed or direction. Findings:
  - most participants were at least mildly disoriented
  - lengthy jacks were read as bugs
  - scroll rates that are too fast make users miss content; too slow causes fatigue
  - horizontal movement from a vertical gesture confused users
  - text inside scrolljacks caused the most severe problems
  - mobile is worse
  - "false endings" made users think the page had ended

  It may be acceptable when it adds functional value (progressive disclosure, breaking down complexity, storytelling), is short, sits below the fold, and is user-tested. "In most cases, not worth adding on mobile." Recommendations: mix with normal sections, avoid direction changes, keep text minimal, provide escape routes such as a sticky nav. — [NN/g, Scrolljacking 101](https://www.nngroup.com/articles/scrolljacking-101/)
- Awwwards maintains "scrollytelling" inspiration collections — e.g. [Vizcom scrollytelling](https://www.awwwards.com/inspiration/scrollytelling-vizcom), [ECI](https://www.awwwards.com/inspiration/scrollytelling-eci), [scroll with depth effect](https://www.awwwards.com/inspiration/sgrappa-scroll-with-depth-effect) (listed in search results; not fetched).
- Immersive Garden's case study for Aten7 "Toom Archives" is an example of immersive digital worldbuilding — [immersive-g.com/projects/aten7](https://immersive-g.com/projects/aten7) (search result; not fetched).

### Inferences
**Sub-variants [synth]:**
1. **Parallax layers**
   - What: background, mid and foreground layers move at different rates; depth reveals; hero image slowly scales. Lowest cost.
   - Use for: travel, outdoor, hospitality, portfolios.
   - Mostly decorative, so it must be fully removable under reduced motion. The W3C cites "parallax with a global off switch" as a 2.3.3 example.
2. **Sticky scrollytelling (steps + pinned graphic)**
   - What: a tall section (e.g. `height: 300–500vh`) with a `position: sticky; top: 0; height: 100vh` stage. Text "steps" scroll past while the stage graphic, chart or image changes per step.
   - Origin: data journalism (NYT, The Pudding).
   - Use for: product explainers, annual reports, data stories, NGO impact, fintech "how it works." Best accessibility profile because it uses native scroll.
3. **Scroll-scrubbed media / pseudo-3D**
   - What: an image-sequence on canvas or video scrubbed by scroll (the Apple product-page pattern [unverified current]); CSS 3D card stacks, rotating carousels, camera "fly-through" with translateZ.
   - Use for: hardware and consumer products, automotive, launches.
4. **WebGL / real-time 3D worlds**
   - What: Three.js or OGL scenes, shaders, a camera on a scroll path, often with smooth-scroll (Lenis) plus GSAP ScrollTrigger.
   - Use for: flagship brand campaigns, studios, luxury, gaming, crypto launches.
   - Heaviest: needs a static fallback and is outside the "no libraries" target (see Q7).

**Layouts and patterns [synth]:**
- Pinned full-screen hero that de-scales into the page.
- Chapter structure with a progress indicator (scroll timeline bar or chapter dots).
- Alternating pinned "scenes" and normal-flow text sections, as NN/g recommends mixing.
- Horizontal gallery driven by vertical scroll inside a sticky stage. NN/g flags direction change as confusing: keep it short and show a visible progress cue.
- Stacking cards.
- Image mask/clip-path expanding to full-bleed.
- Closing CTA in normal flow.
- Nav: always-available sticky nav or skip-to-chapter links (escape route); `scroll-margin-top` on anchors.
- **Mobile:** reduce pin lengths by about 50%, replace WebGL with a poster image or short muted looping video (with a pause button), turn the horizontal pin into a native horizontal `scroll-snap` swipe row, and use `100svh`/`100dvh` instead of `100vh` so the mobile URL bar does not cause jumps.

**Best fits [synth]:**
- Good fit: product launches, hardware, automotive, luxury, campaigns and microsites, annual and impact reports, museums and culture, data journalism, award-chasing studio portfolios.
- Poor fit: e-commerce category and listing pages, SaaS pricing and docs, local service businesses, anything task-oriented (NN/g: goal-oriented users get annoyed and leave), SEO-heavy content pages.

**Anti-patterns [synth + NN/g]:**
- Hijacking wheel or touch to change scroll speed.
- Snap-locking every section.
- Very long pins (more than about 3–4 viewports) with no progress cue.
- Important text inside the pinned animation.
- Hero-only 3D that takes 5–10MB before first paint.
- No reduced-motion or low-power fallback.
- Hiding the scrollbar.
- Breaking browser find-in-page and anchor links.

### Gaps
- I could not verify Awwwards Site of the Year winners for 2024/2025 in this session; the search did not return a primary Awwwards page.
- **Example sites, commonly cited and not verified in this session; confirm they are live and current before use:**
  - [igloo.inc](https://www.igloo.inc) (WebGL, reported Awwwards SOTY 2024 [unverified])
  - [lusion.co](https://lusion.co) (WebGL studio)
  - [bruno-simon.com](https://bruno-simon.com) (3D portfolio)
  - [apple.com/airpods-pro](https://www.apple.com/airpods-pro/) (scroll-scrubbed product)
  - [landonorris.com](https://landonorris.com) [unverified]
  - [pudding.cool](https://pudding.cool) (sticky scrollytelling, data journalism)

---

## Q6. Accessibility rules applying to all three styles (WCAG 2.2, reduced motion, vestibular, scrolljacking)

### Takeaway
SC 2.2.2 Pause, Stop, Hide is Level A and is mandatory for AA. Any auto-starting motion that lasts more than 5s alongside other content (marquees, looping hero video, auto-carousels) needs a pause, stop or hide control. SC 2.3.3 Animation from Interactions is Level AAA, so it is not strictly required for AA. Still, honouring `prefers-reduced-motion` (W3C technique C39) is the expected baseline and costs almost nothing.

### Cited Findings
- **SC 2.3.3 (Level AAA):** "Motion animation triggered by interaction can be disabled, unless the animation is essential to the functionality or the information being conveyed." — [W3C Understanding 2.3.3](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html)
  - Motion animation = "addition of steps between conditions to create the illusion of movement." It excludes colour, blur (blur exclusion removed by errata) and opacity changes.
  - Examples: parallax with a global off switch; a page-flip transition disabled when the user enables reduce motion.
  - Vestibular reactions: dizziness, nausea, headaches; "severe reactions may require bed rest."
  - Scrolling the user controls is allowed, but non-essential motion added to scrolling should be avoidable.
  - Sufficient techniques: **C39** (CSS prefers-reduced-motion), **SCR40** (prefers-reduced-motion in JS), and a user preference toggle.
- **SC 2.2.2 (Level A):** moving, blinking or scrolling content that (1) starts automatically, (2) "lasts more than five seconds, and (3) is presented in parallel with other content" needs a mechanism to pause, stop or hide it, unless essential. — [W3C Understanding 2.2.2](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)
  - "Starts automatically" includes motion triggered indirectly, such as hovering, focusing, or "scrolling an element into view."
  - The scrolling stock ticker example (closest to a marquee) has pause and restart controls.
  - Failure F16: scrolling content without a pause mechanism.
  - Preloaders and full-page ads are exempt (not in parallel).
  - Best practice: one control that affects all moving elements.
- NN/g: scrolljacking disorients users and is worse on mobile; keep it short and below the fold, or avoid it. — [NN/g](https://www.nngroup.com/articles/scrolljacking-101/)
- Kinetic-type guidance: avoid flashing above 3Hz (cf. SC 2.3.1 Three Flashes, Level A); keep contrast during animation; no-JS fallback. — [StudioMeyer](https://studiomeyer.io/en/blog/kinetische-typografie)

### Inferences
**Default contract for generated sites [synth]:**
1. Author motion inside `@media (prefers-reduced-motion: no-preference)`. Do not try to undo motion afterwards. Final, visible states are the default.
2. In JS: `const reduce = matchMedia('(prefers-reduced-motion: reduce)');` and listen for `change`. Skip rAF loops, WebGL camera paths and split-text when it matches.
3. Add a site-level "Reduce motion / Pause animations" toggle in the header or footer. It sets `data-motion="off"` on `<html>`, is stored in localStorage, and covers both 2.2.2 (one control for all) and 2.3.3.
4. Every marquee, looping video or auto-carousel needs a visible pause button with `aria-pressed`. Muted autoplay video gets `playsinline` and pauses when reduce motion is set.
5. Do not change native scroll speed or direction. Do not use wheel `preventDefault`. Smooth-scroll libraries (Lenis) technically alter scroll feel; if used, disable them for reduced motion.
6. Keep reading text out of pinned or animated scenes, or duplicate it in normal flow.
7. Focus order and `:focus-visible` must survive transforms; anything pinned must not trap keyboard focus; skip links to chapters.
8. Reduced-motion fallbacks can still use opacity or colour cross-fades, which the W3C definition excludes from "motion."

### Gaps
- No session source quantifies how many users enable reduce motion.
- The WCAG 2.2 vs 3.0 draft position on motion was not checked.

---

## Q7. Core techniques and values: scroll-driven CSS, IntersectionObserver, sticky, 3D transforms, browser support, performance, libraries

### Takeaway
Since Chrome 115 (July 2023) and Safari 26 (Sept 2025), `animation-timeline: scroll()` and `view()` cover most reveal, progress, parallax and sticky-scene effects in pure CSS, off the main thread. Firefox stable still has them behind a flag as of mid-2026 per one secondary source, so treat them as progressive enhancement: final state by default, inside `@supports`, with an IntersectionObserver fallback for essential reveals. Libraries (GSAP, Lenis, Three.js) are only needed for complex timelines, smooth-scroll feel, or real 3D.

### Cited Findings
- **Browser support:**
  - Chrome and Edge shipped unflagged in Chrome 115 (July 2023).
  - Safari 26 (Sept 2025) supports it; threaded scroll-driven animations came in 26.4, with progress and `animation-play-state` fixes in 26.5.
  - Firefox is still behind `layout.css.scroll-driven-animations.enabled` as of Firefox 152 (June 2026), on by default in Nightly; it is an Interop 2026 priority.
  - caniuse global about 82.6%; not Baseline.

  — [BuildMVPFast (2026)](https://www.buildmvpfast.com/blog/css-scroll-driven-animations-replace-js-2026). Secondary source; Chrome 115 is confirmed by [Chrome for Developers](https://developer.chrome.com/docs/css-ui/scroll-driven-animations). The Safari and Firefox version details were not cross-checked against MDN or caniuse in this session.
- **Concepts:** a Scroll Progress Timeline maps a scroller's position to 0–100%; a View Progress Timeline maps an element's passage through its scroller. They work with the Web Animations API and CSS animations, so they "can run off the main thread." — [Chrome for Developers](https://developer.chrome.com/docs/css-ui/scroll-driven-animations)
- **Named timelines:** `scroll-timeline: --name inline`, `view-timeline-name: --x; view-timeline-axis: block`, and `timeline-scope: --tl` on a shared parent so non-descendants can use the timeline. Names must start with `--`. — [Chrome for Developers](https://developer.chrome.com/docs/css-ui/scroll-driven-animations)
- **Ranges:** `cover` (first to last intersection), `contain`, `entry`, `exit`, `entry-crossing`, `exit-crossing`. Offsets can be % or lengths, e.g. `animation-range: entry 0% entry 100%`. Ranges use the untransformed box. `view(block 20%)` insets the scrollport. JS: `new ScrollTimeline({source})`, `new ViewTimeline({subject, axis, inset})`, `el.animate(kf, {timeline, rangeStart:'entry 25%', rangeEnd:'cover 50%'})`. — [Chrome for Developers](https://developer.chrome.com/docs/css-ui/scroll-driven-animations)
- **Recommended patterns:**
  - progress bar: `animation: fill auto linear; animation-timeline: scroll(root block)`, scaleX 0 to 1
  - card reveal: `animation-timeline: view(); animation-range: entry 0% cover 40%`
  - fallback: finished state is the default; the animation is applied only inside `@media (prefers-reduced-motion: no-preference) { @supports (animation-timeline: view()) {…} }`

  — [BuildMVPFast](https://www.buildmvpfast.com/blog/css-scroll-driven-animations-replace-js-2026)
- Only `transform` and `opacity` stay on the compositor. Width, height and margin trigger layout; scroll listeners run on the main thread and cause jank. — [BuildMVPFast](https://www.buildmvpfast.com/blog/css-scroll-driven-animations-replace-js-2026); also [StudioMeyer](https://studiomeyer.io/en/blog/kinetische-typografie)
- Chrome published a performance case study comparing scroll-driven animations with JS approaches ([link](https://developer.chrome.com/en/blog/scroll-animation-performance-case-study/), not fetched) and a free video course ([link](https://developer.chrome.com/blog/scroll-driven-animations-video-course)).
- Codrops: sticky sections built with `position: sticky` plus JS today; expected to be replaced by CSS scroll-driven animations. — [Codrops](https://tympanus.net/codrops/2024/01/31/on-scroll-animation-ideas-for-sticky-sections)

### Inferences
**Recipes [synth]:**

- **Sticky scene (vanilla):**
  ```html
  <section class="scene" style="height:400vh">
    <div class="stage" style="position:sticky; top:0; height:100svh; overflow:clip">…</div>
  </section>
  ```
  - CSS-only progress: `.scene { view-timeline: --scene block; }` and children use `animation-timeline: --scene; animation-range: contain 0% contain 100%;`.
  - Fallback JS: compute `p = clamp(0, 1, -rect.top / (rect.height - innerHeight))` inside a rAF-throttled passive scroll listener, write `--p` to the stage, and let CSS do `transform: translateX(calc(var(--p) * -200%))`.
  - Use `overflow: clip`, not `hidden`, on ancestors: `overflow: hidden` on an ancestor breaks sticky.
- **Step scrollytelling with IntersectionObserver:** observe each `.step` with `rootMargin: '-50% 0px -50% 0px'` (fires when a step crosses the viewport centre) and set `stage.dataset.step = n`. CSS swaps or cross-fades graphics with `[data-step="2"] .fig-2 { opacity: 1 }`. Robust in all browsers and accessible: the text stays in normal flow.
- **Reveal-on-enter with IntersectionObserver:**
  ```js
  new IntersectionObserver(
    (es, o) => es.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('in'); o.unobserve(e.target); }
    }),
    { threshold: .15 }
  );
  ```
  Add a `.js` class on `<html>` before hiding anything, so content stays visible without JS.
- **CSS parallax:** `.layer { animation: px linear both; animation-timeline: scroll(root); } @keyframes px { to { transform: translateY(calc(var(--depth) * -30vh)); } }`. Depth 0.1–0.6. Disable under reduced motion.
- **CSS 3D:**
  - On the parent: `perspective: 800px–1200px` (natural); 300–600px is dramatic or distorted; above 2000px looks nearly flat. `perspective-origin: 50% 50%`.
  - On the child: `transform-style: preserve-3d`, then `rotateX/rotateY/translateZ`. `backface-visibility: hidden` for flip cards.
  - Card stack on scroll: each card sticky with `top: calc(10vh + var(--i) * 24px)`, scaling down 0.9–0.95 as the next card arrives, driven by `view()` `exit` range.
  - Cylinder / ring carousel: `rotateY(calc(var(--i) * 360deg / var(--n))) translateZ(radius)`.
- **Image mask expand:** `clip-path: inset(20% 30% round 24px)` animated to `inset(0 round 0)` over `view()` `entry` or `contain`. Measure on mobile (clip-path is not reliably compositor-only).
- **Scroll-scrubbed image sequence:** preload about 60–150 WebP frames (or one sprite), draw to `<canvas>` with the index from scroll progress. Heavy: lazy-start, cap at about 1–2MB per 100 frames on mobile, show a poster for reduced motion. A scroll-scrubbed `<video>` (setting currentTime) is jankier unless encoded all-keyframe.
- **Performance budget:** animate transform and opacity only; `will-change: transform` only on active pinned layers; `content-visibility: auto` on off-screen sections (with `contain-intrinsic-size` to avoid CLS); width and height on all media; passive listeners; no layout reads inside scroll handlers (read in rAF, batch writes). INP: keep pointermove handlers tiny and avoid main-thread work longer than 50ms. CLS: never inject split spans that change line-wrap after first paint; split before paint or reserve the size.

**When libraries are usually used vs the vanilla alternative [synth]:**

| Library | Usually used for | Vanilla alternative |
|---|---|---|
| GSAP plus ScrollTrigger / SplitText | Multi-step pinned timelines, scrub with easing, sequencing across elements | `view-timeline` + `timeline-scope`, or IntersectionObserver plus CSS transitions, or the rAF `--p` pattern |
| Lenis | Smooth, inertial scroll feel, syncing WebGL to scroll | Native scroll plus `scroll-behavior: smooth` for anchors only. Omit Lenis: it alters native scroll, NN/g risk. |
| Three.js / OGL | Real 3D models, shaders, particles | CSS 3D transforms, pre-rendered image sequences or video, `<model-viewer>` (a web component, still a library), or static renders. Within a no-library target, fake 3D with layered PNG/WebP plus CSS perspective. |

### Gaps
- Firefox's exact default-on status for scroll-driven animations in late 2026 rests on one secondary blog. Check MDN/caniuse at build time. The safe approach (progressive enhancement) is the same either way.
- The perspective values above are common practice, not cited from a source this session.
- No primary source fetched for INP/CLS thresholds (INP "good" ≤200ms and CLS ≤0.1 per web.dev are [unverified] here).
