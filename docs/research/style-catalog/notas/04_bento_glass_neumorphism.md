# Bento grids, Glassmorphism (incl. Apple Liquid Glass) and Neumorphism / Soft UI: a practical reference for an AI website builder

Scope: web/UI use, current practice 2025–2026. Target: static HTML/CSS/vanilla JS, self-hosted OFL fonts, WCAG 2.2 AA, `prefers-reduced-motion`, `prefers-reduced-transparency`.
Conventions: **[B]** = Bento, **[G]** = Glassmorphism / Liquid Glass, **[N]** = Neumorphism. Anything marked **(synthesized)** is the researcher's recommendation, not a quote from a source. Anything marked **(not fetched)** comes from a standard reference that was not re-read in this session.

---

## 1. Definition, origin and the signature traits

### Takeaway
Bento is a layout system: modular tiles of different sizes in a single grid, inspired by Japanese bento boxes and made popular by Apple's product keynotes and pages. Glassmorphism is a surface/material style: translucent, blurred panes over colourful backgrounds. Apple pushed it into a new "Liquid Glass" phase in June 2025. Neumorphism is a surface style too: elements the same colour as the background, picked out only by paired light and dark shadows. It peaked in 2019–2020 and declined by 2021, so treat it as a niche accent today.

### Cited Findings
**[B] Bento**
- Defined as "meticulously organized web layouts reminiscent of Japanese bento boxes", arranging content in distinct compartments. The concept comes from serving several dishes in one segmented box. Apple uses the pattern in product promo infographics and videos, and CSS Grid plus minimalism drove its rise. — [freeCodeCamp, David Jaja, 4 Apr 2024](https://www.freecodecamp.org/news/bento-grids-in-web-design/)
- Principles: group related content per cell, vary box sizes for hierarchy, build hierarchy with colour, type and placement as well as size, treat the centre as a focal point, limit the grid to **≤ 9 boxes**, and an optional "swirl" reading pattern. — [freeCodeCamp](https://www.freecodecamp.org/news/bento-grids-in-web-design/)
- Typical traits: content compartmentalized so each section is distinct, mixed media (images, text, icons) in one grid, varied block sizes for emphasis, clear boundaries plus generous whitespace, bold type on a muted palette, interactive hover elements. — [Mockuuups Studio, "Best Bento Grid Design Examples [2026]"](https://mockuuups.studio/blog/post/best-bento-grid-design-examples/)

**[G] Glassmorphism**
- NN/g definition: "a visual-design style that uses varying levels of see-through translucency to create depth and separate foreground from background, resembling frosted glass". Most effective over gradients or complex backgrounds, and popular since 2020. Design systems file it under "material". Microsoft Fluent calls it **Acrylic**, and Apple Vision Pro uses glassmorphic SwiftUI materials. — [NN/g, Megan Brown, 7 Jun 2024](https://www.nngroup.com/articles/glassmorphism/)
- NN/g's three levers: **opacity** (their examples are 90/60/30%), **background blur** (at 30% opacity, 25px keeps edges somewhat distinguishable and 100px blends the background together), and **strokes/gradients** (a low-opacity or gradient stroke adds thickness, and gradient fills mimic reflection). — [NN/g](https://www.nngroup.com/articles/glassmorphism/)
- **Liquid Glass**: announced at WWDC on **9 June 2025** for iOS/iPadOS/macOS Tahoe/tvOS/visionOS/watchOS 26. It is a translucent material that "refracts and reflects" the content behind it, and Apple named visionOS as an influence. — [Wikipedia: Liquid Glass](https://en.wikipedia.org/wiki/Liquid_Glass)
- Liquid Glass traits per WWDC25 session 219: **lensing** (bends and concentrates light while background content stays sharp), **adaptivity** (small elements flip light/dark for legibility, large ones adapt but don't flip), **thickness scales with size** (deeper shadows and stronger refraction on bigger elements), **interaction response** (elements deform and illuminate on touch), and **scroll-edge effects** that dissolve content under the glass. — [Apple WWDC25 "Meet Liquid Glass" (session 219)](https://developer.apple.com/fr/videos/play/wwdc2025/219/)

**[N] Neumorphism / Soft UI**
- Definition: a GUI style, also called soft UI, between skeuomorphism and flat design. Elements **match the background colour** and are told apart only by surrounding shadows and highlights, so they look extruded or recessed. Soft, light look, often pastel and low contrast. — [Wikipedia: Neumorphism](https://en.wikipedia.org/wiki/Neumorphism)
- Origin: concepts trace back to Oleksandr (Alexander) Plyuto's Dribbble banking-app mockup. **Jason Kelly coined "neumorphism" in 2019** (neo + skeuomorphism). Huawei HarmonyOS on the Honor Vision TV (Aug 2019) was a proto-example. — [Wikipedia](https://en.wikipedia.org/wiki/Neumorphism). **Conflict:** Webflow dates the Plyuto concept to **2020** — [Webflow, Jeff Cardello, updated 24 Oct 2025](https://webflow.com/blog/neumorphism).
- Traits: elements look embedded in or lifted from a faint background, with light, subtle shadows, rounded corners and thin lines, generous grey/white space and neutral palettes. It blends skeuomorphic physicality with flat minimalism. — [Webflow](https://webflow.com/blog/neumorphism)
- Decline: macOS Big Sur (Nov 2020) brought it mainstream and with that came heavy criticism. By 2021 most designers had moved on — [Webflow](https://webflow.com/blog/neumorphism). Wikipedia says designer adoption fell by 2021 as glassmorphism took over, and that Big Sur is actually closer to glassmorphism — [Wikipedia](https://en.wikipedia.org/wiki/Neumorphism).

### Inferences
- Signature-trait checklists for a generator (synthesized):
  - **[B]**: (1) one CSS grid with 4–12 columns; (2) 5–9 tiles with mixed spans (1×1, 2×1, 1×2, 2×2); (3) uniform gap; (4) one shared corner radius; (5) one tile = one idea, each with its own media or metric; (6) one dominant "hero" tile.
  - **[G]**: (1) translucent fill with alpha around 0.1–0.6; (2) `backdrop-filter: blur()` plus saturate; (3) a 1px light rim or gradient border; (4) a vivid, controlled background (gradient blobs or a photo); (5) a soft drop shadow for lift; (6) optional grain/noise.
  - **[N]**: (1) a monochrome mid-tone background, never pure white or black; (2) element fill equals the background; (3) paired light (top-left) and dark (bottom-right) shadows; (4) large radii; (5) inset shadows for pressed or input states; (6) a minimal accent colour.
- Bento and glass/neumorphism stack: bento is a *layout*, the other two are *surface treatments*. A "glass bento" or "soft bento" is a valid combination.

### Gaps
- No primary source fetched for who first called the web layout "bento" (Apple's 2020s keynote slides are commonly cited, but there's no dated primary source). Michał Malewicz's role in popularizing neumorphism (his 2019 UX Collective article) wasn't verified in this session.

---

## 2. Recognised sub-variants and when to use each

### Takeaway
There are no formal taxonomies. Sources do support these working sub-variants: **[B]** product/feature bento (Apple style), dashboard bento, editorial/portfolio/link-in-bio bento. **[G]** light frosted glass, dark glass, "clear" vs "regular" Liquid Glass, and SVG-refraction "liquid glass" on the web. **[N]** light soft UI, dark soft UI, and flat-neumorphic hybrids (the only variant sources recommend today).

### Cited Findings
**[B]**
- **Product-page bento**: hero tile 2×2, feature/detail tiles 1×1, highlight tile 2×1. **Dashboard bento**: a KPI row of 4 small tiles, a large chart spanning 3–4 columns, secondary widgets at 2 columns. — [StudioMeyer, Matthias Meyer, 24 Nov 2025 (updated 30 Sep 2026)](https://studiomeyer.io/en/blog/bento-grid-layouts)
- **Storytelling bento** (Apple.com), where each square works like a page that leads to the next. **Interactive bento** (create.video, hover reveals animations). **Minimal editorial bento** (literal.club, bold type, muted palette). **Link-in-bio/profile bento** (bento.me). **Case-study bento** (Koto Studio WhatsApp case). — [Mockuuups](https://mockuuups.studio/blog/post/best-bento-grid-design-examples/)
- Early adopters include online magazines, educational sites and portfolios. — [freeCodeCamp](https://www.freecodecamp.org/news/bento-grids-in-web-design/)

**[G]**
- **Regular vs Clear** Liquid Glass. Regular is "versatile and adaptive". Clear is fully transparent and **needs a dimming layer**. Use Clear only when the element sits over media-rich content, the content layer can tolerate dimming, and the content on top is bold and bright. **Never mix the two.** — [Apple WWDC25 session 219](https://developer.apple.com/fr/videos/play/wwdc2025/219/)
- **Tinted glass**: tint selectively for primary actions only. Tinting gives a frosted, coloured glass that improves legibility. — [Apple WWDC25 session 219](https://developer.apple.com/fr/videos/play/wwdc2025/219/)
- **High-blur "acrylic" glass** for components shown over unknown backgrounds (context menus). **Low-blur glass** only over simple, controlled backgrounds. — [NN/g](https://www.nngroup.com/articles/glassmorphism/)
- **Web "liquid glass" via SVG refraction**: `backdrop-filter: url(#svgFilter)` with `feDisplacementMap`. This works **only in Chromium** (Chrome, Edge, Brave). Safari and Firefox don't support SVG filters as backdrop-filter input. — [LogRocket, Rahul Chhodde, 8 Dec 2025](https://blog.logrocket.com/how-create-liquid-glass-effects-css-and-svg/)
- Apple increased navigation-bar opacity after the first beta, iOS 26.1 added a transparency toggle, and WWDC 2026 (iOS 27) reduced default transparency and added a clear↔tinted slider. — [Wikipedia: Liquid Glass](https://en.wikipedia.org/wiki/Liquid_Glass)

**[N]**
- Light-direction variants: top-left, top-right, bottom-left, bottom-right, set by which shadow gets positive or negative offsets. Surface variants: **flat**, **convex** (gradient light→dark matching the light source), **concave** (gradient reversed), and **pressed/inset**. — [CSS-Tricks, Adrian Bece, 20 Mar 2020](https://css-tricks.com/?p=304931)
- The recommended modern direction is a **hybrid**: use neumorphism "sparingly, mainly as an accent alongside another design system" — [CSS-Tricks](https://css-tricks.com/?p=304931). Mix flat and neumorphic elements, since neumorphism "shouldn't be the dominant style" — [OpenReplay, 3 Oct 2022](https://blog.openreplay.com/implementing-neumorphic-shadows/). Limited uses such as cards, subtle backgrounds and decorative framing, with stronger edge contrast (e.g. the Webflow Showcase site *Light and Day*). — [Webflow](https://webflow.com/blog/neumorphism)

### Inferences
- Variant picker for a generator (synthesized):
  - **[B] Product bento (Apple)**: launches, feature pages, hardware or SaaS feature tours. Big imagery, one stat or claim per tile, dark or light neutral background.
  - **[B] Dashboard bento**: analytics, fintech, admin and "results" sections. Dense tiles, KPI row first, charts in the wide tiles.
  - **[B] Editorial/portfolio bento**: agencies, creators, link-in-bio, About pages. Mixed photo, quote and social tiles, playful colour per tile.
  - **[G] Light frosted**: wellness, beauty, consumer apps. White panes at α 0.25–0.5 over pastel gradients.
  - **[G] Dark glass**: crypto, Web3, AI, gaming, music. Panes at `rgb(255 255 255 / .06–.12)` or `rgb(15 15 20 / .4–.6)` over neon blobs or a photo.
  - **[G] Liquid-glass (web)**: progressive enhancement only, on Chromium, applied to a few floating controls (nav pill, tab bar, CTA), never content cards.
  - **[N] Light soft UI**: calm product showcases, smart-home and audio-device concepts. Background around `#e0e5ec`.
  - **[N] Dark soft UI**: dark-mode dashboards and music players. Background around `#2a2d32`, with a "light" shadow only slightly lighter than the background.
  - **[N] Hybrid**: flat, high-contrast text and buttons with neumorphic decorative cards or toggles. This is the default recommendation.

### Gaps
- No authoritative source names a standard bento "variant" taxonomy. The variant labels above are synthesized from example sets. No primary sources on dark-mode neumorphism values.

---

## 3. Most used layouts and page patterns (spans, gaps, radius, widths, areas, hero, nav, mobile)

### Takeaway
Bento tiles use spans of 1×1, 2×1, 1×2 and 2×2 on a 4–6 column grid with 16–24px gaps, recomposing to 2–3 columns on tablet and 1–2 on mobile. Glass sites use a sticky translucent header or nav pill over a gradient-blob hero, plus glass cards or modals. Neumorphic pages are single-column showcases or small dashboards on one flat background.

### Cited Findings
**[B]**
- Columns: **desktop (≥1024px) 4–6**, **tablet (768–1023px) 2–3**, **mobile (<768px) 1–2**, stacked linearly. Build mobile-first. Gaps of **16–24px** between tiles, never below 16px. Use `repeat()` + `minmax()` (Tailwind `col-span-2`, `row-span-2`). **No more than 1–2 hero tiles per viewport height.** — [StudioMeyer](https://studiomeyer.io/en/blog/bento-grid-layouts)
- Tutorial recipe: `grid-template-columns: repeat(6, 1fr)`, `gap: 1.5vw`, `max-width: 1500px`, placement through `grid-template-areas` (`hero`, `aside2`…`aside5`). Media queries switch to **4 columns at 1000px** and **3 columns at 750px** (stacked). — [freeCodeCamp](https://www.freecodecamp.org/news/bento-grids-in-web-design/)
- Accessibility: tab order must be logical and must not contradict the visual order. — [StudioMeyer](https://studiomeyer.io/en/blog/bento-grid-layouts)
- MDN reference for `grid-template-areas` recipes. — [MDN: Grid template areas](https://developer.mozilla.org/docs/Web/CSS/CSS_Grid_Layout/Grid_Template_Areas)

**[G]**
- Typical sticky-header pattern: a frosted header with `backdrop-filter: blur(16px)` and an extended-height backdrop child so content just below also feeds the blur. — [Josh W. Comeau, 2 Dec 2024, updated 13 Oct 2026](https://joshwcomeau.com/css/backdrop-filter)
- Apple: use glass **only on the navigation layer** floating above content, never in the content area, and **no glass on glass**. — [Apple WWDC25 session 219](https://developer.apple.com/fr/videos/play/wwdc2025/219/)
- Glass works best over gradients or complex backgrounds. When you control the backdrop, keep it simple or single-colour. — [NN/g](https://www.nngroup.com/articles/glassmorphism/)

**[N]**
- Needs extra padding and margin, so it suits **larger cards and static containers** better than small controls. Avoid inputs, selects and progress bars with complex states. — [CSS-Tricks](https://css-tricks.com/?p=304931)

### Inferences
- **Bento scale (synthesized)**: max-width 1120–1280px for marketing (1440–1600px for dashboards); 16px side gutter on mobile. Gap and radius by density:

  | density | gap | tile radius | tile padding |
  |---|---|---|---|
  | compact (dashboard) | 12–16px | 12–16px | 16–20px |
  | standard (SaaS) | 16–20px | 20–24px | 24–32px |
  | airy (Apple product) | 20–24px | 24–32px | 32–48px |

  Keep nested radius = outer radius − padding (concentric corners) for inner media.
- **grid-template-areas recipes (synthesized)**:
  ```css
  .bento{display:grid;gap:var(--gap,20px);grid-template-columns:repeat(4,minmax(0,1fr));
         grid-auto-rows:minmax(180px,auto);max-width:1200px;margin-inline:auto;padding-inline:16px}
  /* A: "hero + 4" (product) */
  .bento--a{grid-template-areas:"hero hero a b" "hero hero c c" "d e e f"}
  /* B: "feature tour" 6-col */
  .bento--b{grid-template-columns:repeat(6,1fr);
            grid-template-areas:"hero hero hero hero s1 s1" "hero hero hero hero s2 s2" "m1 m1 m2 m2 m3 m3"}
  /* C: dashboard */
  .bento--c{grid-template-areas:"k1 k2 k3 k4" "chart chart chart side" "chart chart chart side" "t1 t1 t2 t2"}
  @media (max-width:1023px){.bento{grid-template-columns:repeat(2,1fr)}
    .bento--a{grid-template-areas:"hero hero" "a b" "c c" "d e" "f f"}}
  @media (max-width:640px){.bento{grid-template-columns:1fr;grid-template-areas:none}
    .bento>*{grid-area:auto!important}}
  ```
  Alternative without areas: `.span-2{grid-column:span 2}.tall{grid-row:span 2}` with `grid-auto-flow: dense`. **Caution:** `dense` reorders visually, not in the DOM, so keep the DOM order logical (see §7).
- **Mobile recomposition rules (synthesized)**: (1) the hero tile stays first and full-width; (2) 2×2 becomes full-width with a 4:3 or 1:1 aspect; (3) pairs of small 1×1 metric tiles can stay 2-up at ≥360px; (4) decorative tiles can drop out (`display:none` only if not content); (5) a horizontal scroll-snap row is an option for 4+ small feature tiles.
- **Bento page skeleton (synthesized)**: centered hero headline, then a bento "features" section (6–9 tiles), then a social proof strip, a second bento ("how it works" or metrics), pricing and a CTA. Nav is usually plain or a glass pill.
- **Glass page skeleton (synthesized)**: fixed gradient-mesh or blob background (position fixed, z-index −1), sticky glass header or floating nav pill (top 12–16px, radius 999px), hero with a glass card or CTA, glass feature cards in a 3-col grid, glass pricing cards with the highlighted plan tinted. Modals use a dimming layer plus a glass dialog.
- **Neumorphic page skeleton (synthesized)**: one background colour across the page, centered hero device or illustration, 2–3 raised feature cards, a pressed toggle or segmented control demo, and a flat high-contrast CTA button (hybrid).

### Gaps
- No source gave measured gap/radius values from Apple, Linear or Vercel CSS. The scale table above is synthesized.

---

## 4. Typography and colour practice; free/OFL fonts

### Takeaway
All three styles lean on clean neo-grotesque or geometric sans faces. Bento leans on strong size contrast inside tiles (big number or headline, small label). Glass needs high-contrast type: white text on dark glass, or near-black on light glass, with weight 500+. Neumorphism needs one mid-tone background and a single saturated accent for state.

### Cited Findings
- [B] Pair bold typography with a muted palette and generous whitespace. — [Mockuuups](https://mockuuups.studio/blog/post/best-bento-grid-design-examples/)
- [B] Build hierarchy with colour, typography and placement, not just box size. — [freeCodeCamp](https://www.freecodecamp.org/news/bento-grids-in-web-design/)
- [G] Check text contrast across the whole component, because translucency puts text over many colours. Use more blur over intricate backgrounds. — [NN/g](https://www.nngroup.com/articles/glassmorphism/)
- [G] Liquid Glass small elements (symbols, text) flip between light and dark to stay legible. — [Apple WWDC25 session 219](https://developer.apple.com/fr/videos/play/wwdc2025/219/)
- [N] Backgrounds near pure white or black make the shadow contrast hard to achieve. — [CSS-Tricks](https://css-tricks.com/?p=304931)
- [N] Neutral grey/white palettes and simple colour schemes. — [Webflow](https://webflow.com/blog/neumorphism)
- [N] Example backgrounds `#e0e0e0` / `#ebecf0` with light shadow `#fff` and dark shadow `#babebc`. — [OpenReplay](https://blog.openreplay.com/implementing-neumorphic-shadows/)

### Inferences
- **OFL font shortlist (synthesized; check each licence at the source before shipping):**
  - Bento/SaaS: **Inter** (or Inter Display), **Geist**, **Manrope**, **Plus Jakarta Sans**, **DM Sans**. Data tiles: **JetBrains Mono** or **Geist Mono** for numbers. Editorial bento: **Instrument Serif** or **Fraunces** for headlines.
  - Glass: **Inter**, **Outfit**, **Sora**, **Space Grotesk** (tech/crypto), **Figtree**.
  - Neumorphism: rounded geometric faces that fit the soft forms: **Nunito**, **Quicksand** (headings only), **Poppins**, **Manrope**.
  - Avoid "Satoshi", "General Sans" and "SF Pro" for self-hosted OFL builds. They use other licences (Fontshare ITF FFL, or Apple's licence that restricts use to Apple platforms).
- **Type scale (synthesized)**: bento tile title 20–28px/600, tile metric 40–72px/600–700 with tight tracking (−0.02em), tile label 13–14px/500. Glass body is never below 16px and never weight 300 over glass. Neumorphic text is a flat colour with ≥ 4.5:1 contrast against the mid-tone background (e.g. `#2d3436` on `#e0e5ec`), never "embossed".
- **Colour practice (synthesized)**:
  - [B] Neutral page background (`#f5f5f7`-like light or `#0a0a0a`-like dark) with tiles one step lighter or darker. Give 1–2 tiles a brand colour or gradient as accents.
  - [G] Background of 2–4 saturated blobs (e.g. `#7c3aed`, `#06b6d4`, `#f472b6`) blurred 80–120px. Text on glass is `#fff` on dark glass and `#0b0b10` on light glass.
  - [N] Background HSL lightness 85–92% (light) or 15–20% (dark), saturation ≤ 15%. One accent (e.g. `#6c5ce7`) only for active, on and focus states.

### Gaps
- No fetched source compared fonts for these styles. The font list is the researcher's synthesis. Licence status should be confirmed on Google Fonts or GitHub at build time.

---

## 5. Concrete CSS recipes and values

### Takeaway
The numbers that hold up across sources: glass blur of **~10–25px** for typical UI (NN/g: 25px keeps edges, 100px fully melts the background), fills of **α 0.3–0.6** for legibility (web.dev examples use 0.3 and 0.5), saturate around 150%, an `@supports` fallback to an opaque fill around 0.95. Neumorphism uses a dual shadow with **equal and opposite offsets** and **blur ≈ 2× offset**, light and dark tones derived from the background, and `inset` for pressed states.

### Cited Findings
**[G] Glass values**
- web.dev examples: frosted glass `background: rgba(255,255,255,.3)` + `backdrop-filter: blur(.5rem)`; modal `blur(10px)` + `rgba(255,255,255,.5)`; stacked `brightness(150%) saturate(150%) blur(1rem)`. `backdrop-filter` ≠ `none` **creates a new stacking context**, and the element must be partly transparent. Fallback: `@supports not (backdrop-filter: none)`, then use a pre-blurred background image instead of a polyfill. "May harm performance. Test it before deploying." (Article dated 2019, so the support picture is older.) — [web.dev, Adam Argyle & Joe Medley](https://web.dev/articles/backdrop-filter)
- NN/g: at 30% opacity, 25px blur keeps edges somewhat distinguishable and 100px blends the background together. Use high blur for components over unknown backgrounds. — [NN/g](https://www.nngroup.com/articles/glassmorphism/)
- Josh Comeau's recipe:
  - `.backdrop{position:absolute;inset:0;height:200%;backdrop-filter:blur(16px);mask-image:linear-gradient(to bottom,black 0% 50%,transparent 50% 100%);pointer-events:none}`. This lets nearby content feed the blur.
  - Top-edge flicker fix: `background:linear-gradient(to bottom,hsl(0deg 0% 95%),transparent 50%)`.
  - Thicker glass: `hsl(0deg 0% 100% / .5–.6)`.
  - Glassy edge: a second element with `backdrop-filter: blur(12px) brightness(0.96)` (tutorial: `blur(8px) brightness(120%)`), `background: hsl(0 0% 100% / .1)`, 4–6px thickness via mask.
  - Rounded corners need an SVG `<mask>` because `border-radius` clips the wrong box.
  - Support: **>97% (caniuse, Oct 2026)**. Wrap in `@supports (backdrop-filter: blur(16px)) or (-webkit-backdrop-filter: blur(16px))`, with a fallback fill around 0.95 opacity.
  - Chromium before **Chrome 142 (Oct 2025)** trimmed before filtering, so `overflow:hidden` clipping failed.
  - Firefox bug: backdrop-filter fails on `position: sticky` inside an ancestor with overflow + border-radius (fix in Nightly, Sep 2026). `overscroll-behavior: none` fixed a flicker.
  - [Josh W. Comeau](https://joshwcomeau.com/css/backdrop-filter)
- Liquid Glass web recipe (LogRocket):
  - `backdrop-filter: url(#liquid-glass-button) brightness(150%)`, content layer `hsl(0 100% 100% / 15%)`, radius 60px, 300×56px button.
  - SVG chain: `feGaussianBlur stdDeviation=1`, then `feImage` (displacement map PNG with red/green radial gradients), then `feDisplacementMap scale=55 xChannelSelector=R yChannelSelector=G`, then `feColorMatrix type=saturate values=50`, then a specular-rim `feImage` with blur 1, `feComposite operator=in`, `feBlend`.
  - Chromium only. Feature-detect and fall back.
  - [LogRocket](https://blog.logrocket.com/how-create-liquid-glass-effects-css-and-svg/)
- `prefers-reduced-transparency: reduce | no-preference` is "limited availability", marked experimental: **Chrome/Edge 118+, Firefox 113, Samsung 25, no Safari (macOS/iOS)**. — [MDN mirror (w3cub)](https://docs.w3cub.com/css/@media/prefers-reduced-transparency); Firefox implementation tracking [bugzil.la/1736914](https://bugzil.la/1736914)

**[N] Neumorphic values**
- Two shadows, one light and one dark, with opposite-sign offsets. The sign pattern sets the light source (top-left: dark `+h +v`, light `−h −v`). Add `inset` for pressed. Background must equal (or nearly equal) the parent. Use `linear-gradient` at the light-source angle: **convex** = lighter stop on the light-shadow side, **concave** = reversed. A reader found 4 outer + 2 inset shadows smoother. — [CSS-Tricks](https://css-tricks.com/?p=304931)
- Hard-coded examples:
  - Button: `-5px -5px 10px rgb(207,206,206), 5px 5px 8px #babebc`
  - Container: `-5px -5px 10px #fff, 5px 5px 10px #babebc`
  - Input: `9px 9px 16px rgba(189,189,189,.6), -9px -9px 16px rgba(255,255,255,.5)`
  - Inset input: `inset 7px 2px 10px #babebc, inset -5px -5px 12px #fff`
  - Pressed: `inset 1px 1px 2px #babebc, inset -1px -1px 2px #fff`
  - Offset:blur ratio around 0.5–0.6.
  - [OpenReplay](https://blog.openreplay.com/implementing-neumorphic-shadows/)

### Inferences
- **Glass token recipe (synthesized, static CSS):**
  ```css
  :root{--glass-bg:rgb(255 255 255 / .18);--glass-bg-solid:rgb(248 248 252 / .96);
        --glass-border:rgb(255 255 255 / .35);--glass-blur:16px;--glass-sat:160%;
        --glass-shadow:0 8px 32px rgb(0 0 0 / .18);--radius:20px}
  .glass{background:var(--glass-bg-solid);border:1px solid var(--glass-border);
         border-radius:var(--radius);box-shadow:var(--glass-shadow), inset 0 1px 0 rgb(255 255 255 / .45)}
  @supports ((backdrop-filter:blur(1px)) or (-webkit-backdrop-filter:blur(1px))){
    .glass{background:var(--glass-bg);
      -webkit-backdrop-filter:blur(var(--glass-blur)) saturate(var(--glass-sat));
              backdrop-filter:blur(var(--glass-blur)) saturate(var(--glass-sat))}}
  .glass--dark{--glass-bg:rgb(17 17 24 / .45);--glass-bg-solid:rgb(17 17 24 / .94);
               --glass-border:rgb(255 255 255 / .12)}
  @media (prefers-reduced-transparency:reduce){
    .glass{background:var(--glass-bg-solid);backdrop-filter:none;-webkit-backdrop-filter:none}}
  @media (prefers-contrast:more){.glass{background:var(--glass-bg-solid);border-color:currentColor}}
  ```
  Blur ladder: 8px (subtle chip), 12–16px (cards, header), 20–24px (modals, menus over photos), 32–40px max (rarely). Go above 40px only on small elements, for performance (see §7). Fill alpha ladder: light glass 0.15–0.35 over controlled gradients, 0.5–0.7 over photos or video. Dark glass 0.35–0.6.
- **Gradient border (synthesized)**: `border:1px solid transparent; background:linear-gradient(var(--glass-bg),var(--glass-bg)) padding-box, linear-gradient(135deg,rgb(255 255 255/.6),rgb(255 255 255/.05)) border-box;`. Note that a translucent padding-box layer lets the border gradient show through. The alternative is a `::before` with `mask: linear-gradient(#000 0 0) content-box exclude, linear-gradient(#000 0 0)` (mask-composite).
- **Noise (synthesized)**: inline SVG data-URI `<feTurbulence type="fractalNoise" baseFrequency=".8" numOctaves="3" stitchTiles="stitch"/>` as a `::after` background at `opacity:.04–.08; mix-blend-mode:overlay; pointer-events:none`. Keep it a static image, not animated.
- **Liquid glass (web) progressive enhancement (synthesized)**: `CSS.supports('backdrop-filter','url(#x)')` can return true in browsers that parse the value but don't render SVG-filter backdrops, so it isn't a reliable check (not verified this session). The safest default is standard frosted glass for everyone. Apply an optional `.liquid` enhancement class only after a JS check, and keep the frosted fallback readable on its own. A cheaper "liquid" imitation without SVG: `backdrop-filter: blur(2px) saturate(180%) brightness(1.1)`, low fill (α 0.08–0.15), strong specular rim `inset 0 1px 0 rgb(255 255 255/.6), inset 0 -1px 0 rgb(255 255 255/.15), inset 0 0 0 1px rgb(255 255 255/.18)`, and a large soft outer shadow `0 10px 30px rgb(0 0 0/.2)`.
- **Neumorphic formula (synthesized from the CSS-Tricks rules plus generator conventions):**
  - distance `d` = 0.05–0.1 × element size (cards 8–20px, buttons 4–6px); blur `b = 2d`; spread 0.
  - Light shadow = background with HSL lightness +6 to +10 points (or `#fff` at α 0.6–0.9 on light themes). Dark shadow = background with lightness −12 to −18 points (or the background colour multiplied by about 0.85).
  - The widely used neumorphism.io generator outputs `20px 20px 60px #bebebe, -20px -20px 60px #ffffff` on `#e0e0e0`, i.e. ±15% intensity and blur = 3d. This was **not verified in this session**.
  ```css
  :root{--bg:#e0e5ec;--hi:#ffffff;--lo:#a3b1c6;--d:10px;--b:20px}
  .neu{background:var(--bg);border-radius:20px;box-shadow:calc(var(--d)*-1) calc(var(--d)*-1) var(--b) var(--hi), var(--d) var(--d) var(--b) var(--lo)}
  .neu--convex{background:linear-gradient(145deg,color-mix(in srgb,var(--bg),#fff 12%),color-mix(in srgb,var(--bg),#000 8%))}
  .neu--concave{background:linear-gradient(145deg,color-mix(in srgb,var(--bg),#000 8%),color-mix(in srgb,var(--bg),#fff 12%))}
  .neu--inset,.neu-btn:active,.neu-btn[aria-pressed="true"]{box-shadow:inset var(--d) var(--d) var(--b) var(--lo), inset calc(var(--d)*-1) calc(var(--d)*-1) var(--b) var(--hi)}
  [data-theme=dark]{--bg:#2a2d32;--hi:#363a40;--lo:#1e2024}
  ```
  The `color-mix()` derivation lets one `--bg` token drive everything. Add the a11y border from §7.
- **Bento tile recipe (synthesized)**: `.tile{border-radius:var(--r,24px);padding:clamp(20px,3vw,32px);background:var(--tile);overflow:hidden;position:relative;container-type:inline-size}`. Inside, use `@container (min-width:420px)` to switch between stacked and side-by-side layouts, so a tile looks right at any span.

### Gaps
- No fetched source gave measured backdrop-filter values from Apple.com or other production sites. Neumorphism.io's exact algorithm wasn't fetched. `prefers-reduced-transparency` support in Safari 26 (2025–26) wasn't re-checked. The w3cub mirror may lag MDN, and Firefox's support may sit behind a flag (the bug link exists).

---

## 6. Effects and motion (hover lift, tilt, spotlight, gradient border)

### Takeaway
Use motion sparingly. NN/g's Liquid Glass review found repeated morphing and pulsing controls distracting. Use small hover lifts (2–4px), cursor-follow spotlights and gradient borders on bento and glass, and pressed transitions on neumorphism. Gate all motion behind `prefers-reduced-motion`.

### Cited Findings
- Liquid Glass controls that morph, pulse or bubble pull attention from content and become distracting with repeated use. Floating controls that appear and vanish hurt predictability. — [NN/g, Raluca Budiu, 10 Oct 2025](https://www.nngroup.com/articles/liquid-glass/)
- Apple: glass elements react to interaction by deforming and lighting up gracefully. — [Apple WWDC25 session 219](https://developer.apple.com/fr/videos/play/wwdc2025/219/)
- Bento hover reveals and animations (create.video) encourage exploration. — [Mockuuups](https://mockuuups.studio/blog/post/best-bento-grid-design-examples/)
- Neumorphic pressed state = inset shadows on `:active`. — [CSS-Tricks](https://css-tricks.com/?p=304931); [OpenReplay](https://blog.openreplay.com/implementing-neumorphic-shadows/)

### Inferences
- **Recipes (synthesized, vanilla):**
  ```css
  .tile{transition:transform .25s cubic-bezier(.2,.8,.2,1),box-shadow .25s}
  .tile:hover{transform:translateY(-3px);box-shadow:0 12px 30px rgb(0 0 0/.12)}
  /* spotlight following the cursor */
  .tile::before{content:"";position:absolute;inset:0;border-radius:inherit;pointer-events:none;opacity:0;transition:opacity .3s;
    background:radial-gradient(400px circle at var(--mx,50%) var(--my,50%),rgb(255 255 255/.12),transparent 40%)}
  .tile:hover::before{opacity:1}
  /* animated gradient border (Chromium/Safari 16.4+/Firefox 128+ support @property) */
  @property --a{syntax:"<angle>";inherits:false;initial-value:0deg}
  .ring{border:1px solid transparent;background:linear-gradient(var(--tile),var(--tile)) padding-box,
        conic-gradient(from var(--a),#7c3aed,#06b6d4,#f472b6,#7c3aed) border-box;animation:spin 6s linear infinite}
  @keyframes spin{to{--a:360deg}}
  .neu-btn{transition:box-shadow .15s ease}
  @media (prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important}
    .tile:hover{transform:none}}
  ```
  ```js
  // spotlight + optional tilt (max 6deg), disabled for reduced motion / touch
  const rm = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine = matchMedia('(pointer: fine)').matches;
  document.querySelectorAll('.tile').forEach(el=>{
    el.addEventListener('pointermove',e=>{
      const r=el.getBoundingClientRect(), x=e.clientX-r.left, y=e.clientY-r.top;
      el.style.setProperty('--mx',x+'px'); el.style.setProperty('--my',y+'px');
      if(!rm && fine && el.dataset.tilt!==undefined){
        const rx=((y/r.height)-.5)*-6, ry=((x/r.width)-.5)*6;
        el.style.transform=`perspective(800px) rotateX(${rx}deg) rotateY(${ry}deg)`;}
    },{passive:true});
    el.addEventListener('pointerleave',()=>{el.style.transform='';});
  });
  ```
  Bento entrance: stagger the tile fade-up with IntersectionObserver (opacity 0→1, translateY 12px→0, 40–60ms stagger). Skip it under reduced motion. Also include the `@property` support note: [@property support versions not verified in this session].
- Glass motion: animate the background blobs (slow 20–40s drift), **not** the blur radius. Animating `backdrop-filter` or blur is expensive (see §7). Under reduced motion, freeze the blobs.
- Don't copy Liquid Glass morphing (e.g. tabs that turn into a search bar) onto the web. NN/g found it hurt predictability.

### Gaps
- No fetched source measured motion-duration norms for these styles. The durations and amplitudes above are synthesized. Browser support versions for `@property` weren't verified in this session.

---

## 7. Accessibility pitfalls and fixes; performance

### Takeaway
Glass fails on **text contrast over variable backdrops**. Neumorphism fails on **non-text contrast (1.4.11, 3:1) and state visibility**. Bento fails on **reading/tab order when visual placement differs from the DOM**. Sticky glass headers can also obscure focused elements, which is WCAG 2.2's new SC 2.4.11. Performance risk sits mostly with `backdrop-filter`: large blur radii, many blurred layers, full-viewport blurred elements and animated blur.

### Cited Findings
- [G] Check contrast across the whole component. Offer reduced transparency or increased contrast settings (Apple's settings replace glass with solid colours, which helps low-vision users). Otherwise make sure glass meets WCAG. Use glass "sparingly". — [NN/g](https://www.nngroup.com/articles/glassmorphism/)
- [G] Liquid Glass in iOS 26: text on photos loses contrast, text overlapping text is hard to read, floating controls blend into content, pale search bars are easy to miss, tap targets are crowded. — [NN/g, 10 Oct 2025](https://www.nngroup.com/articles/liquid-glass/)
- [G] Designers told Wired that transparency hurt legibility, especially in sunlight. Apple increased opacity after beta 1 and added transparency controls. — [Wikipedia: Liquid Glass](https://en.wikipedia.org/wiki/Liquid_Glass)
- [G] Liquid Glass supports Reduce Transparency, Increase Contrast and Reduce Motion automatically. — [Apple WWDC25 session 219](https://developer.apple.com/fr/videos/play/wwdc2025/219/)
- [G] `backdrop-filter` "may harm performance. Test it before deploying" and it creates a stacking context. — [web.dev](https://web.dev/articles/backdrop-filter)
- [G] `prefers-reduced-transparency` isn't supported in Safari or iOS Safari, so you can't rely on it alone. — [MDN mirror (w3cub)](https://docs.w3cub.com/css/@media/prefers-reduced-transparency)
- [N] Contrast checkers ignore shadows, which hurts low-vision and colour-blind users. Users can't tell what's interactive. Avoid stateful controls. — [CSS-Tricks](https://css-tricks.com/?p=304931)
- [N] Borders blend into the background and the focused vs unfocused state differs too little. (The article raises the issue but gives no fixes.) — [UX Collective, Michael J. Fordham, Jan 2020](https://uxdesign.cc/neumorphism-can-we-make-it-more-accessible-15be5fe2ef28)
- [N] Low contrast hides buttons and makes text hard to read. Monochrome shadow-only layouts hide interactivity and state, and hierarchy is weak. — [Webflow](https://webflow.com/blog/neumorphism)
- [N] Low-quality screens make clickable items hard to spot. Mix flat and neumorphic elements. — [OpenReplay](https://blog.openreplay.com/implementing-neumorphic-shadows/)
- [B] Tab order must be logical and must not contradict the visual order. — [StudioMeyer](https://studiomeyer.io/en/blog/bento-grid-layouts)
- WCAG 2.2 AA: 1.4.3 text contrast 4.5:1 (3:1 for large text); 1.4.11 non-text contrast 3:1; 2.4.7 focus visible; **2.4.11 Focus Not Obscured (Minimum)** (new in 2.2); **2.5.8 Target Size (Minimum) 24×24 CSS px** (new in 2.2); 1.3.2 meaningful sequence. — [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) (not fetched)

### Inferences
- **Glass fixes (synthesized):**
  1. Test contrast against the *worst* pixel of the backdrop. For dynamic or photo backdrops, put a 0.5–0.7 alpha base under text, or add a text-only scrim.
  2. Make the solid fill the default and apply glass inside `@supports`.
  3. Provide `prefers-reduced-transparency` **and** `prefers-contrast: more` overrides, plus an optional in-page "reduce transparency" toggle stored in localStorage (needed for Safari users).
  4. Sticky glass header: add `scroll-padding-top: <header height + 8px>` to `html` so focused or anchored elements aren't hidden (SC 2.4.11).
  5. Never put body copy on glass over video.
- **Neumorphism fixes (synthesized):**
  1. Give every interactive element a 1px border or outline at ≥ 3:1 against the background (e.g. `#8a97ab` on `#e0e5ec`, verify), or switch to a flat accent fill.
  2. Use a pressed state **plus** a colour or icon change (e.g. accent fill and `aria-pressed`), never shadow alone.
  3. Focus: `:focus-visible{outline:3px solid var(--accent);outline-offset:3px}` with ≥ 3:1 contrast.
  4. Text is never embossed or debossed, always flat with ≥ 4.5:1.
  5. Restrict neumorphism to decorative cards and large toggles.
- **Bento fixes (synthesized):**
  1. Write the DOM in reading or priority order, then place with `grid-template-areas`.
  2. Avoid `grid-auto-flow: dense` or `order` when it changes the meaningful sequence (SC 1.3.2, 2.4.3).
  3. Each tile is an `<article>` or `<li>` inside a `<ul>`, with a heading. For a whole-tile link, use one `<a>` with a stretched `::after`, not nested links.
  4. Keep text inside tiles at ≥ 4.5:1 over tile imagery, with a gradient scrim behind the text.
- **Performance (synthesized):**
  1. Cap the number of simultaneously visible backdrop-filtered elements (about 3–5).
  2. Avoid full-viewport backdrop-filter layers. Blur the *background image itself* once (pre-blurred asset or `filter: blur()` on a fixed layer) instead.
  3. Keep blur ≤ 24px on large surfaces.
  4. Never animate the blur radius. Animate transform or opacity only.
  5. On mobile, (`@media (max-width:768px)` or `(pointer:coarse)`), lower blur to 8–12px or switch to solid fills.
  6. Use `will-change: transform` only during an interaction.
  7. Large blurred gradient blobs: use `filter: blur()` on small elements scaled up, or pre-rendered WebP/AVIF images.
  8. Neumorphic multi-shadow stacks are cheap when static, but avoid transitioning large box-shadows on many elements. Transition the opacity of a pseudo-element that carries the shadow instead.

### Gaps
- No primary source measured backdrop-filter cost (fps or GPU memory) on mobile. The performance guidance above is synthesized from web.dev's general warning and common practice. No academic usability study on bento layouts was found.

---

## 8. Best-fit brands/industries, poor fits, anti-patterns

### Takeaway
Bento suits product feature tours, SaaS, devices, portfolios and dashboards. Glass suits tech, AI, crypto, music, wellness and beauty when the backdrop is controlled, and only for floating chrome. Neumorphism suits calm, tactile, low-density showcases (smart home, audio, wellness concepts) only as an accent. It's a poor fit for forms, data-dense apps, accessibility-critical public services, or anything with many states.

### Cited Findings
- [B] Early adopters: magazines, education sites, portfolios — [freeCodeCamp](https://www.freecodecamp.org/news/bento-grids-in-web-design/). Product pages and dashboards — [StudioMeyer](https://studiomeyer.io/en/blog/bento-grid-layouts). Brand presentations and case studies (Halo Lab, Koto) — [Mockuuups](https://mockuuups.studio/blog/post/best-bento-grid-design-examples/).
- [B] Anti-pattern: more than 9 boxes — [freeCodeCamp](https://www.freecodecamp.org/news/bento-grids-in-web-design/). More than 1–2 hero tiles per viewport — [StudioMeyer](https://studiomeyer.io/en/blog/bento-grid-layouts).
- [G] Use glass over gradients or complex backgrounds. Low translucency over video or photos overwhelms content. Use glass sparingly. — [NN/g](https://www.nngroup.com/articles/glassmorphism/)
- [G] Anti-patterns: glass in the content layer, glass on glass, mixing Regular and Clear, tinting everything. — [Apple WWDC25 session 219](https://developer.apple.com/fr/videos/play/wwdc2025/219/)
- [G] Anti-patterns: text over busy imagery or over other text, decorative motion, unstable or vanishing controls, cramped targets. — [NN/g Liquid Glass](https://www.nngroup.com/articles/liquid-glass/)
- [N] Poor fit with some brand identities, poor accessibility, hard to implement. — [Wikipedia](https://en.wikipedia.org/wiki/Neumorphism)
- [N] Anti-patterns: neumorphic inputs, selects and progress bars, using it as the dominant style, flattened hierarchy. — [CSS-Tricks](https://css-tricks.com/?p=304931); [OpenReplay](https://blog.openreplay.com/implementing-neumorphic-shadows/)
- [N] Works on cards, subtle backgrounds and decorative framing for non-functional images. — [Webflow](https://webflow.com/blog/neumorphism)

### Inferences
- **Fit matrix (synthesized):**
  - **[B] Strong fit:** SaaS/devtools (feature grids), consumer hardware, fintech/analytics (metric tiles), agencies/portfolios, link-in-bio, event pages (schedule, speakers, venue tiles), restaurants (menu highlights, hours, map, reviews). **Weak fit:** long-form editorial reading, legal or government content, single-message landing pages with nothing to compartmentalize.
  - **[G] Strong fit:** AI products, crypto/DeFi dashboards, music and streaming, gaming, beauty/cosmetics and wellness (light frosted), travel with hero photography (glass booking widget). **Weak fit:** healthcare forms, government, banking transaction flows, e-commerce product grids (glass behind product cards hurts colour fidelity), high-density data tables.
  - **[N] Strong fit (accent only):** smart-home or IoT control concepts, audio device or app showcases, meditation apps, calculators or "gadget" toy pages, portfolio experiments. **Weak fit:** anything form-heavy, e-commerce checkout, multi-state dashboards, low-vision audiences, brands with vivid identities (the style requires a monochrome background).
- **Generator anti-pattern rules (synthesized):**
  - [B] Use equal-size tiles only (that's a card grid, not bento). Don't give tiles different radii or gaps. Don't fill the grid with lorem-filler tiles. Keep one message per tile. Don't let more than about 30% of tiles carry dense text.
  - [G] No glass without a colourful backdrop (it reads as grey). No white text on light glass. No more than one blur layer stacked. Don't use glass on long paragraphs. Don't animate backdrop-filter.
  - [N] Never use pure #fff or #000 backgrounds. Don't use neumorphic body text. Don't rely on shadow-only state. Don't rely on shadow alone for the CTA.

### Gaps
- No fetched source gave industry adoption statistics for these styles. The fit matrix is synthesized.

---

## 9. Real example websites (2023–2026) and authoritative guides

### Takeaway
Bento has plenty of live, verifiable examples. Production web glass examples are mostly sticky headers and nav pills. Live neumorphic production websites are rare in 2025–2026, and the sources point to concepts and showcase sites rather than mainstream brands.

### Cited Findings
**[B] Examples**
- Apple.com (storytelling bento): http://apple.com. Literal (minimal, bold type): https://literal.club. Create.video (interactive hover bento): https://www.create.video. Procreate (five-block bento): https://procreate.com. Iconwerk (bento header): https://www.iconwerk.com. Bento.me (link-in-bio bento builder): https://bento.me/home. Koto Studio WhatsApp case study: https://koto.studio/work/whatsapp/. — all per [Mockuuups, 2026 roundup](https://mockuuups.studio/blog/post/best-bento-grid-design-examples/)
- Apple iPhone product page, Vercel, Linear, Spotify, Google Analytics are named as bento users (no URLs given). — [StudioMeyer](https://studiomeyer.io/en/blog/bento-grid-layouts)
- Inspiration gallery: BentoGrids.com. Demo: bentogrid.netlify.app. — [freeCodeCamp](https://www.freecodecamp.org/news/bento-grids-in-web-design/)

**[G] Examples / references**
- Microsoft Fluent "Acrylic" material and Apple visionOS/SwiftUI materials as reference systems. — [NN/g](https://www.nngroup.com/articles/glassmorphism/)
- Apple Liquid Glass across all OS 26 platforms. — [Wikipedia](https://en.wikipedia.org/wiki/Liquid_Glass)

**[N] Examples**
- *Light and Day* (Webflow Showcase, neumorphism with higher edge contrast), Plyuto's banking concept on Dribbble, macOS Big Sur icons. — [Webflow](https://webflow.com/blog/neumorphism)
- Huawei HarmonyOS (Honor Vision TV 2019; HarmonyOS 2 Design System, Red Dot 2021). — [Wikipedia](https://en.wikipedia.org/wiki/Neumorphism)

**Authoritative guides**
- NN/g, "Glassmorphism: Definition and Best Practices" (Megan Brown, 7 Jun 2024): https://www.nngroup.com/articles/glassmorphism/
- NN/g, "Liquid Glass Is Cracked, and Usability Suffers in iOS 26" (Raluca Budiu, 10 Oct 2025): https://www.nngroup.com/articles/liquid-glass/
- NN/g, "Skeuomorphism" (context for neumorphism): https://www.nngroup.com/articles/skeuomorphism/ (not fetched)
- Apple WWDC25 session 219 "Meet Liquid Glass": https://developer.apple.com/videos/play/wwdc2025/219/ (French-locale page fetched)
- web.dev, "Create OS-style backgrounds with backdrop-filter" (Argyle & Medley, 2019, older practice): https://web.dev/articles/backdrop-filter
- Josh W. Comeau, "Next-level frosted glass with backdrop-filter" (2024, updated Oct 2026): https://joshwcomeau.com/css/backdrop-filter
- LogRocket, "How to create Liquid Glass effects with CSS and SVG" (Dec 2025): https://blog.logrocket.com/how-create-liquid-glass-effects-css-and-svg/
- CSS-Tricks, "Neumorphism and CSS" (Adrian Bece, 2020, older practice but still the canonical shadow model): https://css-tricks.com/?p=304931
- Webflow, "The rise and fall of neumorphism" (updated Oct 2025): https://webflow.com/blog/neumorphism
- freeCodeCamp, "Bento Grids in Web Design" (Apr 2024): https://www.freecodecamp.org/news/bento-grids-in-web-design/
- StudioMeyer, "Bento grid layouts" (Nov 2025 / Sep 2026): https://studiomeyer.io/en/blog/bento-grid-layouts
- MDN, Grid template areas: https://developer.mozilla.org/docs/Web/CSS/CSS_Grid_Layout/Grid_Template_Areas

### Inferences
- Candidate glass examples worth checking manually before citing (synthesized, **not verified this session**): apple.com global nav (translucent blurred bar), linear.app (dark glass header plus glowing gradient borders), raycast.com (dark glass panels), vercel.com and stripe.com (translucent sticky headers). Treat them as "verify before use".
- For neumorphism, use generator and demo sites (neumorphism.io, CodePen collections) and Dribbble as visual references rather than claiming live brand sites. That itself is a signal that the style is niche in 2025–2026.

### Gaps
- Glassmorphism and neumorphism example roundups (mycodelesswebsite.com) were blocked by bot verification, so no third-party verified list of live glass or neumorphic sites (2023–2026) could be confirmed. Awwwards and Godly collections weren't fetched. A Smashing Magazine article on these styles wasn't located in this session. Apple's HIG "Materials" page (2025 Liquid Glass update) wasn't fetched directly, only the WWDC session.
