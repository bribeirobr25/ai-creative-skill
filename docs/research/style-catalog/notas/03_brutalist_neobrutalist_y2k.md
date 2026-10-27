# Brutalist, Neo-brutalist and Y2K Web Design: a practical reference for an AI website builder

Scope: three styles. (A) Brutalist web design, (B) Neo-brutalism / neubrutalism, (C) Y2K web design, including the revival, chrome/holographic, cyber, Y2K techno-skeuomorphism and the adjacent Frutiger Aero.
Target: static HTML/CSS/vanilla JS, self-hosted OFL fonts, WCAG 2.2 AA, prefers-reduced-motion.
Convention: anything under "Inferences" is a synthesized recommendation from this researcher and has no single source. Everything under "Cited Findings" has a source link.

---

## 1. Definition, origin and signature traits

### Takeaway
Web brutalism (named around 2014–2016 by Pascal Deville's brutalistwebsites.com) is "raw": it exposes HTML structure, uses default-like controls, and either strips away styling (functional) or deliberately breaks convention (artistic). Neo-brutalism keeps the loud, raw surface (thick black outlines, zero-blur offset shadows, flat clashing colour, big type) but puts it on top of conventional, usable UX. Y2K is a maximalist, techno-optimistic revival of roughly 1995–2004 digital culture: chrome, gloss, translucent plastic, bubbles, gradients, pixel type. Frutiger Aero (about 2005–2013) is a later, nature-and-glass cousin of Y2K.

### Cited Findings

**A. Brutalist web design**
- The term gained traction around 2016 and is credited to Pascal Deville, who created brutalistwebsites.com to catalog such sites. Deville borrowed the name from architecture ("béton brut", raw concrete) and described the style as "ruggedness and lack of concern to look comfortable or easy". He saw it as a younger generation's reaction against the lightness and frivolity of mainstream web design — [LogRocket](https://blog.logrocket.com/ux-design/web-brutalism/)
- daisyUI dates the "raw-web revival" catalogued by Brutalist Websites to 2014 — [daisyUI Neubrutalism](https://trends.daisyui.com/trend/neubrutalism/). The 2014 and 2016 dates conflict a little. Read 2014 as the start of the directory and about 2016 as the point where the trend went mainstream.
- On the architectural origin, Alison Smithson used "New Brutalism" in 1953, and Le Corbusier's raw concrete was an important precedent. The web use of the name is "an analogy rather than a direct architectural method" — [daisyUI Brutalism](https://trends.daisyui.com/trend/brutalism/)
- Signature elements: raw HTML-like structure, default-style controls, stark contrast, an exposed grid, oversized typography and minimal polish — [daisyUI Brutalism](https://trends.daisyui.com/trend/brutalism/)
- Vitaly Friedman (*Smashing Book 6*): "Brutalism in architecture is characterized by unconcerned aesthetics, not intentionally broken aesthetics." Awwwards: brutalism "laughs in the face of rationalism and functionality" — quoted in [Smashing Magazine, F. O'Brien, 2020-01-08](https://www.smashingmagazine.com/2020/01/split-personality-brutalist-web-development/)
- The David Bryant Copeland manifesto (brutalist-web.design) defines the functional reading in seven rules:
  1. "Content is readable on all reasonable screens and devices."
  2. "Only hyperlinks and buttons respond to clicks."
  3. "Hyperlinks are underlined and buttons look like buttons."
  4. "The back button works as expected."
  5. "View content by scrolling."
  6. "Decoration when needed and no unrelated content."
  7. "Performance is a feature."

  — [brutalist-web.design](https://brutalist-web.design/)

**B. Neo-brutalism / neubrutalism**
- NN/g (Hayat Sheikh, 2025-04-11) defines neobrutalism (also spelled neubrutalism) as an evolution of brutalism that uses "raw, unrefined elements": bold colours, simple shapes and deliberately unpolished details. It combines brutalist styling with nostalgic 1990s graphic-design elements and emerged as a reaction against sleek minimalism. NN/g lists five traits:
  - high contrast and bright colours
  - thick lines and geometric shapes
  - stark, solid, single-colour offset drop shadows
  - bold, quirky type used as a focal point and balanced by whitespace
  - skeuomorphic retro cues such as Windows 98-style buttons and monospace fonts

  — [NN/g "Neobrutalism"](https://www.nngroup.com/articles/neobrutalism/)
- daisyUI also calls it "Neo Brutalism" or "Neo Memphis": it "wraps conventional UX in loud geometric blocks, dark outlines, hard offset shadows, flat color, and exaggerated type." Period: early 2020s to the present. The label crystallised across design platforms in the early 2020s — [daisyUI Neubrutalism](https://trends.daisyui.com/trend/neubrutalism/)
- Bejamas frames it as a reaction against neumorphism and glassmorphism (rounded edges, soft gradients, coloured shadows). Its traits: flat components, quirky grotesque type, thick black outlines, hard offset shadows that read as "another black rectangle below the buttons", 45° isometric pseudo-3D, generous whitespace, and cartoonish illustration inspired by old games and ads — [Bejamas](https://bejamas.com/insights/field-notes/neubrutalism-web-design-trend)
- O'Brien (via LogRocket) treats "neu-brutalism" as a friendlier, cartoonish third type that blends functional and jarring brutalism — [LogRocket](https://blog.logrocket.com/ux-design/web-brutalism/)

**C. Y2K**
- Webflow: Y2K recreates late-1990s to early-2000s internet culture: "digital, spacey, and a little over the top". It grew from the mainstreaming of the internet and excitement about the new millennium, and it was shaped by hip-hop and rave culture, toy packaging and early iPod-era ads. Slow connections and low-resolution screens pushed designers toward chunky type and bright, simple graphics — [Webflow](https://webflow.com/blog/y2k-aesthetic)
- daisyUI dates the source period to the mid-1990s through about 2001, with a major revival from the late 2010s. Signature elements: chrome gradients, translucent plastic, bubble lettering, lens flares, compact-device motifs and glossy icons. The 2020s use of "Y2K" is "broader and less historically precise", covering early-2000s fashion in general — [daisyUI Y2K](https://trends.daisyui.com/trend/y2k/)
- The Consumer Aesthetics Research Institute (CARI) lists the Y2K Aesthetic under the 1990s with motifs such as "silver eyeshadow, shiny clothing, Oakleys, gradients, and blobby electronics". It credits foundational research to Evan Collins, Froyo Tam and Terrell Davis — [CARI Y2K Aesthetic](https://cari.institute/aesthetics/y2k-aesthetic). (CARI is the body often called the "Y2K Aesthetic Institute".)
- Frutiger Aero covers roughly 2005–2013. The name was coined retrospectively in 2017, credited by CARI to Froyo Tam and Sofi Xian, and blends Adrian Frutiger's humanist type legacy with Windows Aero. Traits: a blue-green palette, glossy gel controls, bubbles and water, open skies, grass and optimistic technology — [daisyUI Frutiger Aero](https://trends.daisyui.com/trend/frutiger-aero/)

### Inferences
- First-glance recognisability tests (synthesized):
  - Brutalist: looks like unstyled HTML, or like a poster that ignores the grid. Mostly black and white with one harsh accent. Sharp corners.
  - Neo-brutalist: every card and button has a 2–4px black border and a solid black offset shadow, with flat saturated fills on an off-white page.
  - Y2K: metallic or iridescent surfaces, rounded "gel" or bubble shapes, sparkles and stars, and a techno or pixel display face.
  - Frutiger Aero: sky, water and glass, with blue-green gloss.
- For the catalog, Frutiger Aero should be a sub-variant or adjacent entry of Y2K rather than a style of its own, because the two share gloss and gel controls and are often conflated online.

### Gaps
- brutalistwebsites.com itself was not fetched, so its exact launch date (2014 vs 2016) is not confirmed from the primary source.
- No authoritative source names who popularised neo-brutalism. Gumroad's 2021 rebrand is widely credited in design circles, but this was not verified in this session.

---

## 2. Recognised sub-variants and when to use each

### Takeaway
Brutalism splits into two broad types: functional ("l'Internet Brut", raw HTML) and expressive/jarring ("l'Internet Fou", art-led and anti-design). Deville further splits it into purists, UX minimalists and anti-ists. Neo-brutalism varies by colour (candy multi-accent vs mono or limited accent) and by radius (hard 0 vs a soft 4–8px "component library" look). Y2K has several sourced directions: chrome/techno-futurist, candy/pastel bubblegum, multichrome gradient/holographic, pixel or retro-PC (cyber), techno-skeuomorphic media player, low-fi purist and the Frutiger Aero cousin.

### Cited Findings

**A. Brutalism**
- O'Brien's two types:
  - Type One, "l'Internet Brut": raw materials are HTML (and some CSS), with light backgrounds, black text, blue links and little styling. Examples: Craigslist, Wikipedia, A List Apart, Old Reddit, Bloomberg, Freecycle, CERN's first website.
  - Type Two, "l'Internet Fou": aesthetics deliberately broken, closer to Dada and Expressionism, with usability "an afterthought" or "actively sabotaged". Examples: Toiletpaper magazine, jisooeom.com.

  — [Smashing Magazine](https://www.smashingmagazine.com/2020/01/split-personality-brutalist-web-development/)
- Deville's three micro-styles are purists, UX minimalists and anti-ists (artists). UX minimalists "see efficiency and performance as the main driver of Web Brutalism" — [Smashing Magazine](https://www.smashingmagazine.com/2020/01/split-personality-brutalist-web-development/)
- LogRocket's naming of the same split: **Functional** (white or black backgrounds, system fonts, blue hyperlinks, a boxy HTML look, no drop-downs), **Jarring** (asymmetry, no clear grid, irregular colours, oversized type, clashing typefaces) and **Neu-brutalism** — [LogRocket](https://blog.logrocket.com/ux-design/web-brutalism/)

**B. Neo-brutalism**
- Radius variants are a hard 0 (closer to true brutalism) or 4–8px (common in component libraries). Beyond about 12px the style "reads as a different look" — [The Plus Addons](https://theplusaddons.com/blog/neo-brutalism-web-design/)
- Colour: a black and off-white base plus one to three saturated accents (yellow, coral, blue, green, lavender) — [daisyUI Neubrutalism](https://trends.daisyui.com/trend/neubrutalism/). NN/g recommends limiting the palette to two or three bold, high-contrast colours — [NN/g](https://www.nngroup.com/articles/neobrutalism/)
- On dark surfaces an inverted shadow is used (`6px 6px 0 #fff`), seen on feastables.com — [The Plus Addons](https://theplusaddons.com/blog/neo-brutalism-web-design/)

**C. Y2K directions**
- Webflow names six directions:
  - chrome / metallic / holographic accents
  - gradients and multichrome
  - bubbles and blobs (gel pill buttons, large blurred blobs)
  - glow / neon on dark
  - glitch (RGB split, scan lines)
  - lo-fi graphics (pixel art, GIF loops, fisheye, grain, flash photography, duotone)

  It names four palettes: electric, candy brights, blended multichrome and monochrome editorial — [Webflow](https://webflow.com/blog/y2k-aesthetic)
- Wix Studio (Aaron Gelbman, 2024-12-18) names seven directions:
  - vibrant retro-kitsch
  - retrofuturist (mesh or animated) gradients
  - alternative iconography (stickers, smileys, butterflies)
  - pixel and retro-PC nostalgia (old windows, pixel cursors)
  - low-fi purist (default fonts, clip-art)
  - bold ornamental type
  - "analogue UX" (MacOS-style windows with modern usability)

  — [Wix Studio](https://www.wix.com/studio/blog/y2k-design)
- **Y2K Techno-Skeuomorphism** (aliases: Y2K Media Player UI, Chrome Futurism, Skinnable UI, Millennium Futurism) is modelled on futuristic audio equipment: brushed silver shells, blue LCDs, beveled transport buttons, rotary dials, EQ sliders and custom-shaped windows. Best for music, audio tools and games — [daisyUI](https://trends.daisyui.com/trend/y2k-techno-skeuomorphism/)
- daisyUI also lists adjacent styles: Cybercore, Seapunk, Frutiger Aero, 2K1 (2001–2004), UrBling, Aqua UI, Vaporwave and Synthwave — [daisyUI Y2K](https://trends.daisyui.com/trend/y2k/), [daisyUI index](https://trends.daisyui.com/trend/neo-brutalism/)

### Inferences
Synthesized catalog sub-variants, each with a "when to use":

- **Brutalist**
  - **B1 Raw/HTML (functional)**: system fonts, blue underlined links, one column. Use for manifestos, documentation, indie publishers and dev tools that want to look honest and fast.
  - **B2 Typographic/editorial brutalism**: giant grotesk or mono type, exposed grid lines, black and white with one accent. Use for studios, cultural institutions, festivals and portfolios.
  - **B3 Anti-design/jarring (art)**: collage, overlaps, clashing faces. Use only for art, fashion and music projects where conversion is secondary.
- **Neo-brutalist**
  - **N1 Candy**: off-white page, 3 accents, 3px borders, 6px shadows, radius 0–8px. Use for creator tools, SaaS marketing and consumer startups.
  - **N2 Mono / limited**: black, white and a single accent (yellow or lime). More "serious" and suits B2B dev tools.
  - **N3 Soft / rounded**: radius 8–12px, pastel fills, 2px borders. Friendlier, for edtech, kids' products and food.
  - **N4 Dark inverted**: dark surface with white borders and shadows. Use for gaming or night-life brands.
- **Y2K**
  - **Y1 Chrome / techno-futurist**: silver, ice blue, chrome type, techno display faces.
  - **Y2 Candy / pastel bubblegum**: pink, aqua, lime, rounded display faces, sparkles and stickers. Use for beauty, fashion, youth and creators.
  - **Y3 Cyber / pixel / retro-PC**: dark or black page, neon, pixel fonts, OS windows, glitch.
  - **Y4 Frutiger Aero**: sky, water, glass, blue-green, humanist rounded sans. Use for eco-tech and nostalgic campaigns.
  - **Optional Y5 Techno-skeuomorphic media player**: for music and audio.

### Gaps
- No formal taxonomy names "candy" vs "mono" neo-brutalism. Those labels are this catalog's own.

---

## 3. Most used layouts and page patterns, including mobile

### Takeaway
Brutalism exposes document flow: full-width sections, visible grid rules, abrupt scale changes and plain lists rather than cards. Neo-brutalism uses conventional SaaS or e-commerce layouts (hero, feature cards, pricing, FAQ) built from outlined, shadowed blocks on an irregular modular or bento grid. Y2K uses layered, desktop-like compositions: floating windows, bubbles, product cutouts, and a hero built on a large gradient or chrome background.

### Cited Findings
- **Brutalism**
  - Layout: expose document flow, grid and navigation, with oversized content blocks, abrupt scale changes and full-width sections. Content density is either sparse or dense, document-like lists, "kept explicit rather than wrapped in cards". Imagery: unpolished photos, scans and screenshots with honest aspect ratios and visible captions — [daisyUI Brutalism](https://trends.daisyui.com/trend/brutalism/)
  - Functional brutalism uses no drop-down menus and a boxy HTML look — [LogRocket](https://blog.logrocket.com/ux-design/web-brutalism/). Navigation by scrolling and a working back button are core rules — [brutalist-web.design](https://brutalist-web.design/)
- **Neo-brutalism**
  - "Conventional navigation and task flow beneath an irregular modular grid", oversize controls and occasional overlap. Imagery: flat outlined illustrations, pseudo-3D objects, graph-paper motifs, browser-window fragments. Use the large (`*-lg`) component sizes — [daisyUI Neubrutalism](https://trends.daisyui.com/trend/neubrutalism/)
  - NN/g recommends 24–32px of padding around dense shapes and borders, and headlines about twice the size of body text — [NN/g](https://www.nngroup.com/articles/neobrutalism/)
  - Card padding of 24px in the reference card — [The Plus Addons](https://theplusaddons.com/blog/neo-brutalism-web-design/)
- **Y2K**
  - Layout: "layered, desktop-like compositions with compact device-style windows, floating bubbles, product cutouts, and small interface chrome". Medium density with many small collectible details. "Primary actions stay large, and chrome ornament must not crowd labels" — [daisyUI Y2K](https://trends.daisyui.com/trend/y2k/)
  - Use chrome as an accent on hero cards, feature blocks and CTAs rather than on whole layouts. Use blobs as a background layer behind hero content — [Webflow](https://webflow.com/blog/y2k-aesthetic)
  - Frutiger Aero layout: glossy utility panels over open landscape depth (sky or water scenes), with clear toolbars and friendly modules — [daisyUI Frutiger Aero](https://trends.daisyui.com/trend/frutiger-aero/)
  - Techno-skeuomorphic layout: one compact, custom-contoured console with a dominant display, transport cluster and docked subpanels — [daisyUI](https://trends.daisyui.com/trend/y2k-techno-skeuomorphism/)
  - Horizontal scrolling text and marquee-like micro-interactions, and MacOS-style windows — [Wix Studio](https://www.wix.com/studio/blog/y2k-design)

### Inferences
Synthesized page patterns for the builder:

**Brutalist**
- Hero options:
  - (a) a massive single-line wordmark at about 12–20vw that bleeds off the edge, plus a one-line description
  - (b) a plain `<h1>` with a list of links (raw)
  - (c) a full-bleed image with a caption block
- Grid: a visible 12-column grid drawn with 1–2px rules (`border-left` on columns), or a single column of 60–75ch for raw.
- Navigation: an inline text link row at the top (no hamburger on desktop), or a sticky bar with a border-bottom. Use an index or table list for collections (name | year | category rows) instead of cards.
- Product or collection grid: a table, or a 2–4 column grid with 1px gaps exposed by a black background (the `gap` shows through as rules).
- Footer: a dense text block.
- Section rhythm: hard section breaks with full-width rules and no soft transitions.
- Mobile: collapse to one column, keep the links visible (wrapping inline list), and clamp giant type with `clamp()` so words don't overflow. Use `overflow-wrap:anywhere` or `hyphens:auto` for long display words.

**Neo-brutalist**
- Hero: a left-aligned huge headline, a highlighted word (marker-style background span), two bordered CTAs and a right-side illustration or product screenshot in a bordered "browser window" frame. Sticker badges are rotated -3° to 6°.
- Feature section: a bento grid of bordered cards in alternating accent fills.
- Logo row: in a bordered strip, or a marquee.
- Pricing: 3 bordered cards, with the featured one lifted by a larger shadow and an accent fill.
- FAQ: bordered `<details>` accordions.
- Footer: an inverted black block.
- Product grid: 2–4 columns of cards with a bordered image well, title, price chip and add-to-cart button.
- Navigation: a bordered top bar with a CTA button. On mobile, a bordered drawer.
- Mobile: reduce shadow offsets from 6–8px to 3–4px, keep borders at 2–3px, stack the bento grid to one column, and keep tap targets at 44px or more.

**Y2K**
- Hero: a chrome or iridescent headline over a gradient-mesh or blob background, with a floating product cutout and sparkles. Or a "desktop" hero holding 2–3 draggable-looking windows (title bar plus content).
- Collection grid: rounded 16–32px glossy cards, or windows with title bars.
- Navigation: a pill-shaped glossy nav bar, or a taskbar or dock motif at the bottom (desktop only).
- Section rhythm: alternate gradient bands, with marquees between sections.
- Mobile: drop the multi-window overlap and stack windows as full-width cards. Reduce blob count and size to save GPU and paint. Keep body text on solid or near-solid panels.

### Gaps
- No source gave quantitative layout statistics (e.g. the share of neo-brutalist sites using bento grids).

---

## 4. Typography: families, scale, weights, and free/OFL options

### Takeaway
- Brutalism uses system faces, grotesques, serif defaults or monospace, with blunt scale contrast and underlined links.
- Neo-brutalism uses a heavy or quirky grotesk display face (Syne, Archivo Black) with a calm sans or mono for body (Space Grotesk, DM Sans, Space Mono).
- Y2K uses techno, wide, bubble or pixel display faces (Audiowide, Michroma, Syncopate, Zen Dots, Orbitron) with a clean sans for body. Frutiger Aero uses rounded humanist sans (Nunito Sans, Varela Round, Quicksand).

### Cited Findings
- **Brutalism.** Suggested faces: Archivo Black, Space Mono, IBM Plex Mono, Work Sans, Courier Prime. Also system sans, grotesque, serif or monospace, "with blunt scale contrasts, underlined links, and clear semantic heading levels" — [daisyUI Brutalism](https://trends.daisyui.com/trend/brutalism/). Functional brutalism uses system fonts — [LogRocket](https://blog.logrocket.com/ux-design/web-brutalism/)
- **Neo-brutalism**
  - Display: Syne and Archivo Black. Functional and body: Space Grotesk, DM Sans and Space Mono. Use "a calm sans-serif or mono for body copy" — [daisyUI Neubrutalism](https://trends.daisyui.com/trend/neubrutalism/)
  - NN/g: pair bold headlines with clean, neutral body fonts. Decorative or condensed faces are hard to read in body text — [NN/g](https://www.nngroup.com/articles/neobrutalism/)
  - Bejamas: "quirky grotesque typefaces", serif and sans — [Bejamas](https://bejamas.com/insights/field-notes/neubrutalism-web-design-trend)
- **Y2K**
  - Suggested faces: Audiowide, Michroma, Righteous, Syncopate, Zen Dots. Pair bubble or techno display lettering with a compact clean sans or a pixel accent — [daisyUI Y2K](https://trends.daisyui.com/trend/y2k/)
  - Techno-skeuomorphic: Share Tech Mono, Orbitron, Chakra Petch, Audiowide, Michroma, with segmented or bitmap numerals for readouts — [daisyUI](https://trends.daisyui.com/trend/y2k-techno-skeuomorphism/)
  - Frutiger Aero: Ubuntu, Nunito Sans, Varela Round, Quicksand, M PLUS Rounded 1c — [daisyUI Frutiger Aero](https://trends.daisyui.com/trend/frutiger-aero/)
  - Pixel or bitmap faces for headings, techno/rave faces, and rounded sans, with a clean sans for body — [Webflow](https://webflow.com/blog/y2k-aesthetic)
  - Chrome-text recipe values: `font-size: clamp(3rem, 10vw, 8rem); font-weight: 800; letter-spacing: -0.02em`. Body text at 16px minimum — [The Plus Addons Y2K](https://theplusaddons.com/blog/y2k-web-design.md)
  - Wix cites Comic Sans, Times New Roman and other default fonts as intentional low-fi choices — [Wix Studio](https://www.wix.com/studio/blog/y2k-design)

### Inferences
- **Licensing (from this researcher's knowledge; verify each font's licence file before bundling)**
  - Under the SIL Open Font License on Google Fonts: Space Grotesk, Space Mono, Archivo / Archivo Black, IBM Plex Mono / Sans, Work Sans, Syne, DM Sans, Courier Prime, Audiowide, Michroma, Righteous, Syncopate, Zen Dots, Orbitron, Share Tech Mono, Chakra Petch, Nunito Sans, Varela Round, Quicksand and M PLUS Rounded 1c.
  - **Ubuntu uses the Ubuntu Font Licence, not OFL.** Substitute Nunito Sans or Varela Round if you require OFL only.
  - OFL pixel options for Y2K/cyber: VT323, Press Start 2P, Silkscreen, Pixelify Sans. Wide display options: Unbounded, Krona One, Monoton (neon).
- **Synthesized type scales**
  - Brutalist: body 16–18px with system-ui or mono. Ratio 1.5–2.0, with display at 8–20vw clamped. Weights 400 and 700/900 only. Uppercase display, letter-spacing -0.03em on giant type.
  - Neo-brutalist: body 16–18px in Space Grotesk or DM Sans at 400/500. h1 at `clamp(2.5rem, 6vw + 1rem, 6rem)` in a 700–800 display face. Line-height 1.0–1.1 for display and 1.5–1.6 for body. NN/g's "headline ≈ 2× body" is the minimum contrast.
  - Y2K: a display face only for h1/h2 and logos, a clean sans for body at 16px+ and 1.5 line-height, and mono or pixel for labels and badges (12–14px at minimum, so watch legibility).
- Self-host as WOFF2 with `font-display: swap`. Subset Latin. Preload only the display face used in the hero.

### Gaps
- No source gave font-usage frequency data for these styles.

---

## 5. Colour: palettes and contrast practice

### Takeaway
Brutalism is black and white plus one harsh utility accent (default blue or red). Neo-brutalism is black and off-white plus one to three saturated flat accents, always with black text on the accents, which gives high contrast. Y2K is silver, ice blue, hot pink, lime and white, with metallic gradients. Its weak spot is contrast on chrome or gradient text and on neon-on-neon pairings.

### Cited Findings
- **Brutalism:** black and white with one harsh utility accent. Default-like link and focus colours may be kept. daisyUI mapping:
  - primary: harsh blue or red
  - base: white / light grey / darker structural grey

  — [daisyUI Brutalism](https://trends.daisyui.com/trend/brutalism/)
- **Neo-brutalism:** a black and off-white base with one to three saturated accents (yellow, coral, blue, green, lavender). Page theme colour `#f1f0eb` — [daisyUI Neubrutalism](https://trends.daisyui.com/trend/neubrutalism/)
- **Neo-brutalism hex palette** with contrast against black text (`#000`):

  | Colour | Hex | Contrast |
  |---|---|---|
  | White card | `#FFFFFF` | 21:1 |
  | Off-white page | `#FAF7F0` | 19.63:1 |
  | Lime | `#C4F000` | 15.81:1 |
  | Yellow | `#FFDE00` | 15.70:1 |
  | Cyan | `#00E5FF` | 13.65:1 |
  | Hot pink | `#FF69B4` | 7.93:1 |

  Focus blue is `#0044FF`. A neumorphic pairing (`#E0E0E0`/`#A3B1C6`) measures only 1.65:1 by comparison — [The Plus Addons](https://theplusaddons.com/blog/neo-brutalism-web-design/)
- Bejamas: bright, high-contrast pairings (red and blue, red and green), pure black and white, and no desaturated colours — [Bejamas](https://bejamas.com/insights/field-notes/neubrutalism-web-design-trend)
- NN/g: pairings such as yellow and cyan can fail readability. Limit the palette to two or three colours and use a contrast checker — [NN/g](https://www.nngroup.com/articles/neobrutalism/)
- **Y2K:** silver, ice blue, hot pink, lime, white and translucent plastic tones, with metallic gradients and sharp glossy highlights — [daisyUI Y2K](https://trends.daisyui.com/trend/y2k/)
- **Webflow Y2K palettes:**
  - electric: electric blue, teal, neon green, hot pink, silver
  - candy brights: aqua, bubblegum pink, tangerine, which "need more negative space"
  - multichrome: teal, electric blue, violet, magenta
  - monochrome editorial

  Pair loud backgrounds with neutral text, use 3–4 related gradient colours, and keep text on high-contrast cards — [Webflow](https://webflow.com/blog/y2k-aesthetic)
- **Chrome grey stops:** `#f8f8f8, #b9c4cc, #5d6a75, #ffffff, #8e9aa5, #d8dee3, #6f7b86`. Accents: lime `#b6ff3d` and cyan `#00e5ff`. Chrome type is mid-grey and often fails contrast on light backgrounds. Lime on cyan is "close to unreadable" — [The Plus Addons Y2K](https://theplusaddons.com/blog/y2k-web-design.md)
- **Techno-skeuomorphic:** brushed silver, graphite, gunmetal and black, with icy blue LCD fields and tiny red, green or amber status lights — [daisyUI](https://trends.daisyui.com/trend/y2k-techno-skeuomorphism/)
- **Frutiger Aero:** vivid sky blue, grass green, aqua, white and sunny yellow, with high-key lighting — [daisyUI Frutiger Aero](https://trends.daisyui.com/trend/frutiger-aero/)

### Inferences
- Rule for neo-brutalism: text on accents is always `#000` (or `#111`). Never put white text on yellow, lime or cyan.
- Rule for Y2K: put the chrome or gradient headline on a dark navy or black background, where mid-grey chrome stops reach better contrast, or give it a 1–2px dark `-webkit-text-stroke` or a text-shadow outline. Treat chrome text as large text (WCAG 3:1) only if it is at least 24px regular or 18.66px bold. Body text must sit on solid panels.
- Synthesized starter tokens:
  - Brutalist raw: `--bg:#fff; --fg:#000; --link:#0000EE; --visited:#551A8B; --accent:#FF0000`
  - Neo candy: `--bg:#FAF7F0; --ink:#000; --a1:#FFDE00; --a2:#FF69B4; --a3:#00E5FF; --a4:#C4F000`
  - Y2K chrome: `--bg:#0b1020; --ice:#bfe6ff; --pink:#ff5fc8; --lime:#b6ff3d; --silver:#c9d1d9`
  - Y2K pastel: `--bg:#fff4fb; --pink:#ffb3e1; --aqua:#a8f0ff; --lilac:#d7c4ff; --ink:#2a1440`
  - Frutiger Aero: `--sky:#3fa9f5; --aqua:#7fe0e6; --grass:#5cc84a; --white:#fff; --ink:#0b2a3c`

  These are synthesized and must be contrast-checked.

### Gaps
- No sources measured contrast for typical Y2K pastel palettes.

---

## 6. Components and details with concrete CSS values

### Takeaway
Neo-brutalism has the best-documented numbers:
- border 2–5px solid black (3–4px typical)
- shadow 4–8px offset with 0 blur
- radius 0–8px (beyond 12px it reads as a different style)
- hover moves the element halfway into its shadow, and active moves it fully in (shadow goes to 0), with transitions of 100ms or less

Brutalism uses radius 0–0.25rem, thick rules and native controls. Y2K uses radius 1–2rem, multi-stop chrome gradients clipped to text, and clip-path sparkles.

### Cited Findings
- **Neo-brutalism**
  - Border roughly 2–5px, near-black; the example card uses `4px solid #000`. Hard offset shadow with zero blur, e.g. `6px 6px 0 #000`, and neobrutalism.dev uses `4px 4px 0 0 rgba(0,0,0,1)`. Radius 0–8px (example 6px), with the style changing beyond about 12px. Card padding 24px — [The Plus Addons](https://theplusaddons.com/blog/neo-brutalism-web-design/)
  - Button states:
    - base: `box-shadow: 6px 6px 0 #000`, transition 80ms on transform and box-shadow
    - hover/focus-visible: `transform: translate(3px,3px); box-shadow: 3px 3px 0 #000`
    - active: `translate(6px,6px); box-shadow: 0 0 0 #000`
    - keep transitions at or under about 100ms, and disable them under `prefers-reduced-motion: reduce`
    - focus: `outline: 3px solid #0044FF; outline-offset: 3px`
    - page-builder equivalents: blur 0, spread 0, equal horizontal and vertical offsets, typically 4–8

    — [The Plus Addons](https://theplusaddons.com/blog/neo-brutalism-web-design/)
  - The source also has an internal inconsistency: its anatomy figure says 14px offset while its code says 6px — [The Plus Addons](https://theplusaddons.com/blog/neo-brutalism-web-design/)
  - Motion grammar: "Lift by increasing the hard shadow, press by translating into the shadow, with abrupt slides, stamps, or tilts". Radius `0` or `0.25rem`, `--depth:1` — [daisyUI Neubrutalism](https://trends.daisyui.com/trend/neubrutalism/)
  - NN/g mentions Windows 98-style buttons and signalling interactivity with underlines, hover states or colour shifts — [NN/g](https://www.nngroup.com/articles/neobrutalism/)
  - neobrutalism.dev is a 64-component library for React and Tailwind v4, built on shadcn/ui and Base UI, with selectable palettes — [neobrutalism.dev](https://www.neobrutalism.dev/)
- **Brutalism:** all radius `0` or `0.25rem`, "thick rules and exposed borders, plus native controls and full-bleed media" — [daisyUI Brutalism](https://trends.daisyui.com/trend/brutalism/). "Hyperlinks are underlined and buttons look like buttons" — [brutalist-web.design](https://brutalist-web.design/)
- **Y2K**
  - Radius `1rem`–`2rem`, `--depth:1`. Shapes: bubbles, capsules, chrome stars, rounded device shells, translucent tabs and beveled compact windows — [daisyUI Y2K](https://trends.daisyui.com/trend/y2k/)
  - Chrome text recipe (verbatim). `color: transparent` is required. The uneven stops make it read as metal — [The Plus Addons Y2K](https://theplusaddons.com/blog/y2k-web-design.md)
    ```css
    .chrome{font-size:clamp(3rem,10vw,8rem);font-weight:800;letter-spacing:-0.02em;
      background:linear-gradient(180deg,#f8f8f8 0%,#b9c4cc 28%,#5d6a75 46%,#ffffff 52%,#8e9aa5 58%,#d8dee3 78%,#6f7b86 100%);
      background-clip:text;color:transparent;}
    ```
  - Sparkle recipe (verbatim). Moving the inner points from 60/40 to 55/45 gives thinner, sharper arms. Mark sparkles `aria-hidden="true"`. Use `image-rendering: pixelated` for pixel sprites — [The Plus Addons Y2K](https://theplusaddons.com/blog/y2k-web-design.md)
    ```css
    .sparkle{width:64px;aspect-ratio:1;background:linear-gradient(135deg,#b6ff3d,#00e5ff);
      clip-path:polygon(50% 0%,60% 40%,100% 50%,60% 60%,50% 100%,40% 60%,0% 50%,40% 40%);}
    ```
  - Techno-skeuomorphic: radius `0.75rem`–`1.5rem`, `--noise:1`, compact `*-sm` controls — [daisyUI](https://trends.daisyui.com/trend/y2k-techno-skeuomorphism/)
  - Frutiger Aero: radius `1rem`–`2rem`. Gel buttons, glass orbs, leaf tabs, water droplets, soft bevels — [daisyUI Frutiger Aero](https://trends.daisyui.com/trend/frutiger-aero/)

### Inferences
Synthesized vanilla CSS recipes, untested in this session. Validate before shipping.

```css
/* Neo-brutalist button (candy) */
:root{--ink:#000;--bw:3px;--sh:6px;--r:6px}
.nb-btn{font:700 1rem/1 "Space Grotesk",system-ui;padding:.875rem 1.25rem;min-height:44px;
  background:#FFDE00;color:var(--ink);border:var(--bw) solid var(--ink);border-radius:var(--r);
  box-shadow:var(--sh) var(--sh) 0 var(--ink);transition:transform 80ms,box-shadow 80ms}
.nb-btn:hover{transform:translate(3px,3px);box-shadow:3px 3px 0 var(--ink)}
.nb-btn:active{transform:translate(var(--sh),var(--sh));box-shadow:0 0 0 var(--ink)}
.nb-btn:focus-visible{outline:3px solid #0044FF;outline-offset:3px}
@media (max-width:600px){:root{--sh:4px;--bw:2px}}
@media (prefers-reduced-motion:reduce){.nb-btn{transition:none}}
/* Neo-brutalist card */
.nb-card{background:#fff;border:var(--bw) solid var(--ink);border-radius:var(--r);
  box-shadow:8px 8px 0 var(--ink);padding:24px}
/* Highlighted word */
.nb-mark{background:#C4F000;padding:0 .2em;border:2px solid #000;box-decoration-break:clone}
/* Sticker badge */
.nb-sticker{display:inline-block;transform:rotate(-4deg);border:2px solid #000;border-radius:999px;padding:.25rem .75rem;background:#FF69B4}

/* Brutalist raw */
body.raw{font:16px/1.5 system-ui,sans-serif;max-width:72ch;margin:2rem auto;padding:0 1rem;color:#000;background:#fff}
.raw a{color:#0000EE;text-decoration:underline;text-underline-offset:.15em}
.raw a:visited{color:#551A8B}
/* Brutalist exposed grid (gap shows as rules) */
.b-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:2px;background:#000;border:2px solid #000}
.b-grid>*{background:#fff;padding:1rem}
.b-mega{font:900 clamp(3rem,14vw,14rem)/.85 "Archivo Black",sans-serif;text-transform:uppercase;letter-spacing:-.04em;overflow-wrap:anywhere}

/* Y2K holographic surface */
.holo{background:
  linear-gradient(115deg,rgba(255,255,255,.6) 0%,transparent 40%,rgba(255,255,255,.4) 60%,transparent 80%),
  conic-gradient(from 200deg at 30% 40%,#ff9de2,#a6c1ff,#9effe9,#fffaa3,#ff9de2);
  border-radius:24px;border:1px solid rgba(255,255,255,.8)}
/* Y2K gel / aqua pill button */
.gel{border-radius:999px;padding:.8rem 1.6rem;color:#06223a;font-weight:700;border:1px solid #2b7bd6;
  background:linear-gradient(180deg,#e9f6ff 0%,#9fd3ff 49%,#5aa9f5 50%,#8fd0ff 100%);
  box-shadow:inset 0 1px 0 #fff,inset 0 -2px 6px rgba(0,60,140,.35),0 4px 10px rgba(0,80,180,.3)}
/* Y2K retro window chrome */
.win{border:2px solid #000;border-radius:8px;background:#fff;box-shadow:4px 4px 0 #000}
.win>.bar{display:flex;justify-content:space-between;align-items:center;padding:.3rem .5rem;
  background:linear-gradient(90deg,#ff5fc8,#7aa8ff);color:#fff;font:12px "Silkscreen",monospace;border-bottom:2px solid #000}
/* Neon glow (cyber) */
.neon{color:#e9fffb;text-shadow:0 0 4px #00e5ff,0 0 12px #00e5ff,0 0 24px #ff5fc8}
```

- The holographic animation option is a slow `background-position` shift. A pointer-tilt variant uses `--x/--y` set from JS on `pointermove` that drive gradient angles. Gate both behind reduced-motion.
- Window chrome in the Win98/XP style can come from a third-party CSS library (98.css, XP.css). Licences and the current state of those projects were not checked here, so self-implement if unsure.

### Gaps
- neobrutalism.dev's exact token values were not exposed in fetched content. The `4px 4px 0 0` figure comes from a secondary source (The Plus Addons).
- No sourced holographic or gel-button recipes were found. The recipes above are synthesized.
- Gumroad's live CSS was not checked. One source reports the served homepage has no box-shadow declarations ([The Plus Addons](https://theplusaddons.com/blog/neo-brutalism-web-design/)), so Gumroad may no longer be a pure neo-brutalist reference.

---

## 7. Effects and motion in plain HTML/CSS/JS

### Takeaway
Brutalism uses immediate state changes, hard cuts, native scrolling and occasional raw marquees, with no smooth decorative transitions. Neo-brutalism uses "lift by increasing the hard shadow, press by translating into the shadow", plus stamps, tilts and abrupt slides, in 100ms or less. Y2K uses loading shines, bubble floats, window pops, lens-flare sweeps, spring easing, short glitch bursts, marquees and holographic sheen.

### Cited Findings
- **Brutalism:** "Immediate state changes, hard cuts, native scrolling, and occasional raw marquees. Smooth decorative transitions are avoided" — [daisyUI Brutalism](https://trends.daisyui.com/trend/brutalism/)
- **Neo-brutalism:** hard-shadow lift and press, abrupt slides, stamps and tilts — [daisyUI Neubrutalism](https://trends.daisyui.com/trend/neubrutalism/). Transitions at or under about 100ms, disabled under reduced motion — [The Plus Addons](https://theplusaddons.com/blog/neo-brutalism-web-design/)
- **Y2K:** loading shines, bubble floats, window pops, lens-flare sweeps, and springy device interactions with "quick, glossy timing" — [daisyUI Y2K](https://trends.daisyui.com/trend/y2k/). Glitch should be "brief and targeted", and glow or gradients should go on a few key components only — [Webflow](https://webflow.com/blog/y2k-aesthetic)
- **Frutiger Aero:** floating bubbles, rippling water, sweeping glossy highlights, growing leaves, buoyant window transitions — "optimistic rather than futuristic" — [daisyUI Frutiger Aero](https://trends.daisyui.com/trend/frutiger-aero/)
- **Techno-skeuomorphic:** knobs rotate, sliders snap, meters pulse, LCD text scrolls, discs spin — [daisyUI](https://trends.daisyui.com/trend/y2k-techno-skeuomorphism/)
- Horizontal scrolling text and micro-interactions — [Wix Studio](https://www.wix.com/studio/blog/y2k-design)

### Inferences
Synthesized techniques:
- **Marquee (all three styles)**
  - Build: a duplicated inline track using `@keyframes` on `transform: translateX(-50%)` over a linear 20–40s loop.
  - Pause on `:hover` and `:focus-within`.
  - Under reduced motion, use `animation: none` and let it wrap or scroll.
  - Mark the duplicate copy `aria-hidden="true"`.
  - Any motion longer than 5 seconds needs a pause control (WCAG 2.2.2).
- **Neo-brutalist "stamp-in" reveal:** `IntersectionObserver` adds `.in`. Keyframes run from `scale(1.15) rotate(-3deg); opacity:0` to `scale(1) rotate(0)` in 180ms `steps(3)` or cubic-bezier(.2,1.6,.4,1).
- **Brutalist hover:** an instant colour invert (`a:hover{background:#000;color:#fff}`) with no transition. Optionally a custom cursor or an exposed `outline:1px solid red` grid toggle as a playful dev-mode easter egg.
- **Y2K shine sweep:** a pseudo-element with a `linear-gradient(110deg, transparent 40%, rgba(255,255,255,.8) 50%, transparent 60%)` moving across a button over 1.2s on hover.
- **Y2K bubble float:** absolutely positioned radial-gradient circles with `@keyframes float { to { transform: translateY(-20px) } }` alternate over 4–8s, staggered by `animation-delay`.
- **Y2K glitch:** two pseudo-elements offset ±2px in `#ff00ff` and `#00ffff` with `mix-blend-mode: screen`, animated `clip-path: inset()` in `steps()`. Fire once on load or hover for under 600ms, never in a continuous loop.
- **Window drag:** about 30 lines of pointer-events JS. Make it optional and keyboard-accessible, or purely decorative.
- **Reduced motion:** wrap everything in `@media (prefers-reduced-motion: no-preference) { ... }` so motion is opt-in, which is better than turning it off afterwards.

### Gaps
- No source provided benchmarked timing values for Y2K animations.

---

## 8. Accessibility pitfalls and fixes; performance notes

### Takeaway
- **Brutalism:** functional brutalism is inherently fast and accessible. "Jarring" brutalism risks a weak hierarchy, unclear interaction and sabotaged usability.
- **Neo-brutalism:** text contrast is usually excellent with black text on bright fills. The risks are colour-on-colour pairings, decorative type in body copy, overwhelming density, and CTAs lost among equally loud blocks.
- **Y2K:** the main issues are contrast on chrome and gradient text, neon-on-neon pairings, motion (glitch, flashing), text baked into images, and GPU-heavy blurs and blobs.

### Cited Findings
- **Brutalism**
  - Critics say jarring brutalism inverts design's purpose and can lack hierarchy and a clear user journey. Bold type and high contrast can help some low-vision users — [LogRocket](https://blog.logrocket.com/ux-design/web-brutalism/)
  - Type Two usability is "an afterthought" or "actively sabotaged" — [Smashing Magazine](https://www.smashingmagazine.com/2020/01/split-personality-brutalist-web-development/)
  - "Performance is a feature". Only links and buttons should respond to clicks, and the back button must work — [brutalist-web.design](https://brutalist-web.design/)
  - UX minimalists believe "the radical limitation of possibilities can boost conversions" (opinion, no data) — [Smashing Magazine](https://www.smashingmagazine.com/2020/01/split-personality-brutalist-web-development/)
- **Neo-brutalism**
  - NN/g risks: overwhelming users, yellow/cyan-type pairings failing readability, decorative or condensed type in body text, hard-to-recognise interactive elements, and weakened hierarchy and CTA prominence.
  - NN/g fixes: contrast-check, use two or three colours, neutral body fonts, 24–32px padding, interactivity cues (underline, hover, colour shift), size-based hierarchy, and user testing.

  — [NN/g](https://www.nngroup.com/articles/neobrutalism/)
  - High contrast helps readability for some users but "can cause anxiety for others". The style is not ideal for finance, healthcare and banking — [Bejamas](https://bejamas.com/insights/field-notes/neubrutalism-web-design-trend)
  - Focus ring `3px solid #0044FF` with a 3px offset. Reduced-motion handling — [The Plus Addons](https://theplusaddons.com/blog/neo-brutalism-web-design/)
- **Y2K**
  - Check `background-clip:text` contrast. Chrome is mid-grey and often fails on light backgrounds: "Keep it for display headings that are decorative, and never for body copy." Body at 16px minimum. Fix neon pairings rather than dropping the palette. Use real webfont text, not text in images. `aria-hidden` on sparkles — [The Plus Addons Y2K](https://theplusaddons.com/blog/y2k-web-design.md)
  - Keep lo-fi assets lightweight with bold outlines so they load quickly and display well on mobile. Limit glitch to avoid overwhelming visitors and raising bounce rates — [Webflow](https://webflow.com/blog/y2k-aesthetic)
  - "Chrome ornament must not crowd labels" — [daisyUI Y2K](https://trends.daisyui.com/trend/y2k/)

### Inferences
Synthesized WCAG 2.2 AA checklist per style.

**All three styles**
- Text contrast of 4.5:1, and 3:1 for large text and for UI component boundaries (1.4.11).
- Visible focus that is not obscured (2.4.11 Focus Not Obscured, Minimum, new in 2.2). Sticky bordered nav bars in neo-brutalism and Y2K can cover focused items, so add `scroll-padding-top`.
- Target size of at least 24×24px (2.5.8, new in 2.2), with 44px recommended.
- Pause/stop/hide for marquees and moving blobs (2.2.2). No more than 3 flashes per second for glitch (2.3.1). Honour `prefers-reduced-motion`.
- Under reflow at 320px (1.4.10), giant brutalist type must not cause horizontal scroll. Use `clamp()` and `overflow-wrap`.
- Under text spacing (1.4.12), a fixed-height bordered card must not clip text. Avoid fixed heights.

**Brutalist**
- Don't rely on colour alone for links. Keep underlines.
- Rotated or overlapping text must keep DOM reading order.
- Custom cursors must not hide the pointer.
- Raw tables need `<th scope>`.

**Neo-brutalist**
- The 3px black border helps meet 1.4.11 for controls.
- The press transform must not be the only state cue. Pair it with an `aria-pressed` or `aria-expanded` state where relevant.
- Rotated sticker text below 18px gets hard to read, so keep rotation within ±6°.

**Y2K**
- Give chrome headlines a solid fallback colour via `@supports not (background-clip:text)`. Some add a dark stroke.
- Translucent "glass" panels need an opaque enough backing (alpha 0.85 or more) behind body text, because text over blurred gradients varies in contrast.
- Pixel fonts are hard to read below 16px, so use them for labels only.

**Performance (synthesized)**
- **Brutalist:** near-zero JS, and system fonts mean zero font bytes, which is ideal for Core Web Vitals.
- **Neo-brutalist:** cheap. Hard shadows are non-blurred and paint-light. Animate only `transform` and `box-shadow` on small elements, or use a pseudo-element shadow and animate `transform` only.
- **Y2K:**
  - Large `filter: blur()` blobs and `backdrop-filter` are paint- and GPU-heavy, especially on mobile. Limit them to 2–3 blobs, prefer pre-blurred SVG or AVIF images, and use `will-change` sparingly.
  - Gradient animations on large areas cause repaints. Animate `transform` or `opacity` of an overlay instead.
  - GIF loops are heavy, so use muted, looping MP4/WebM with `playsinline`, or animated AVIF.

### Gaps
- No empirical studies were found comparing task success or conversion for these styles.

---

## 9. Best-fit brands and industries, poor fits, anti-patterns

### Takeaway
- **Brutalism:** editorial, artists, cultural institutions, countercultural brands, studios and developer or manifesto sites.
- **Neo-brutalism:** startups, creator tools, portfolios, youth and DTC brands, and expressive marketing pages. It is a poor fit for finance, healthcare and banking.
- **Y2K:** fashion, beauty, music, social, youth and Gen-Z DTC. Frutiger Aero suits nostalgic, eco-tech and playful utilities. Y2K is a poor fit for banks and serious B2B.

### Cited Findings
- **Brutalism** best fits: editorial sites, artist portfolios, cultural projects and countercultural brands — [daisyUI Brutalism](https://trends.daisyui.com/trend/brutalism/)
- **Neo-brutalism**
  - Best fits: startup sites, creator products, portfolios, cultural projects, youth brands and expressive marketing pages — [daisyUI Neubrutalism](https://trends.daisyui.com/trend/neubrutalism/)
  - Poor fits: finance, healthcare and banking, where clarity and reliability are critical — [Bejamas](https://bejamas.com/insights/field-notes/neubrutalism-web-design-trend)
- **Y2K**
  - Best fits: fashion, beauty, music, social products and youth brands — [daisyUI Y2K](https://trends.daisyui.com/trend/y2k/)
  - Suits DTC clothing brands, not banks. Match it to the audience — [Wix Studio](https://www.wix.com/studio/blog/y2k-design)
  - Frutiger Aero: nostalgic campaigns, eco-tech, playful utilities and youth experiences — [daisyUI Frutiger Aero](https://trends.daisyui.com/trend/frutiger-aero/)
  - Techno-skeuomorphic: music products, audio tools, games, retro utilities and hardware controllers — [daisyUI](https://trends.daisyui.com/trend/y2k-techno-skeuomorphism/)

### Inferences
Synthesized anti-patterns, each treated as a "don't" for the builder.

**Brutalist**
- Mixing in soft shadows, gradients or large radii, which turns it into "unfinished corporate".
- Hiding navigation in clever gimmicks.
- Removing link underlines.
- Giant type that overflows on mobile.
- Using the jarring variant for e-commerce checkout or forms.

**Neo-brutalist**
- Every element at the same visual weight, so there is no hierarchy (NN/g).
- More than three accents.
- White text on yellow or lime.
- Blurred shadows or gradients (which break the style).
- Radius above 12px.
- Inconsistent shadow directions or offsets.
- Applying borders to body text containers so densely that the page becomes a wall of boxes.

**Y2K**
- Chrome or gradient body text.
- Several display faces at once.
- Continuous glitch or flashing.
- Text baked into images.
- Too many blobs, sparkles and windows, so the CTA is lost.
- Mixing Frutiger Aero nature imagery with cyber neon in the same page without intent.

**Brand mapping examples (relevant to an SMB web agency)**
- Indie bookshop or gallery: B2.
- SaaS or creator tool: N1/N2.
- Café or food truck: N3 (soft).
- Cosmetics or makeup bag brand, Gen-Z fashion: Y2 (candy/pastel), or Y1 chrome for accents.
- Music producer or club night: Y3 cyber or techno-skeuomorphic.
- Eco or wellness app: Y4 Frutiger Aero.
- Law firm, bank, clinic: avoid all three, or use only a restrained B1 typographic minimalism.

### Gaps
- No quantitative data was found on brand-fit outcomes.

---

## 10. Real examples (2023–2026) and authoritative articles

### Takeaway
Current, sourced example lists come mostly from NN/g (2025), Bejamas, LogRocket, The Plus Addons and Webflow. The canonical brutalist directory is brutalistwebsites.com. Live status in October 2026 was not verified site by site in this session, so the builder should treat these URLs as "check before citing".

### Cited Findings
**A. Brutalist examples**
- Functional examples:
  - Bloomberg: https://www.bloomberg.com/
  - 56 Digital: https://56.digital/
  - Craigslist: https://craigslist.org

  — [LogRocket](https://blog.logrocket.com/ux-design/web-brutalism/), [Smashing](https://www.smashingmagazine.com/2020/01/split-personality-brutalist-web-development/)
- Jarring/typographic examples:
  - Twomuch.Studio: https://twomuch.studio/
  - A2-Type: https://a2-type.co.uk/

  — [LogRocket](https://blog.logrocket.com/ux-design/web-brutalism/)
- Brutalist style examples:
  - Théâtre Saint-Gervais Geneva: https://saintgervais.ch/
  - Kane Robinson: https://kanerobinson.com/
  - Studio Push: https://studio-push.com/

  — [Bejamas](https://bejamas.com/insights/field-notes/neubrutalism-web-design-trend)
- Drudge Report: https://www.drudgereport.com/ — [LogRocket](https://blog.logrocket.com/ux-design/web-brutalism/), also cited by [NN/g](https://www.nngroup.com/articles/neobrutalism/)
- Art/anti examples:
  - Toiletpaper magazine: https://www.toiletpapermagazine.org/
  - Ji Soo Eom: https://jisooeom.com/

  — [Smashing](https://www.smashingmagazine.com/2020/01/split-personality-brutalist-web-development/)
- Manifesto: https://brutalist-web.design/ (David Bryant Copeland). Directory: https://brutalistwebsites.com/

**B. Neo-brutalist examples**
- NN/g (April 2025) cites:
  - Gumroad
  - Figma's brand refresh
  - Tony's Chocolonely e-commerce by Tinloof
  - 99percentoffsale.com
  - byooooob.com
  - cyanbanister.com
  - bieffeforniture.it
  - Dodonut
  - The API World landing page
  - Sui Overflow 2025 (sui.io/overflow)
  - Halo Lab "Look Beyond Limits"

  — [NN/g](https://www.nngroup.com/articles/neobrutalism/)
- Bejamas cites:
  - Gumroad: https://gumroad.com/
  - Figma: https://www.figma.com/
  - The Great Lake Michigan: https://thegreatlake.fun/
  - Plus: https://cleanwith.plus/
  - Budapest Park: https://www.budapestpark.hu/en

  — [Bejamas](https://bejamas.com/insights/field-notes/neubrutalism-web-design-trend)
- Feastables (https://feastables.com/) uses hard shadows in production, confirmed by the source. neobrutalism.dev is a component library. Gumroad's current homepage was reported to lack box-shadows — [The Plus Addons](https://theplusaddons.com/blog/neo-brutalism-web-design/)
- Reference guide: https://neubrutalism.co (linked by [Manual do Usuário, 2026-08-26](https://manualdousuario.net/en/neubrutalism-web-design/))

**C. Y2K examples**
- Webflow (current article) cites:
  - DigiValet: https://digivalet-toffeenut.webflow.io/ (chrome and holographic hero)
  - Byooooob: https://www.byooooob.com/ (candy)
  - Pasha Ink: https://pashaink.com/ (multichrome gradients)
  - Griffo House: https://www.griffo.house/ (monochrome)
  - Walrus: https://www.walrus.xyz/ (pixel headings with a readable sans)
  - AKARI by Lusion: https://akari.lusion.co/ (glow on dark)
  - Nifty Portal: https://portal.thenifty.com/ (brief glitch)
  - Chronically Online Magazine: https://com.manychat.com/ (fisheye, grain, metallic)
  - Poison Studio: https://www.poison.studio/
  - Unbias by SISTA: https://unbias-by-sista.webflow.io/ (blurred blobs)

  — [Webflow](https://webflow.com/blog/y2k-aesthetic)
- Wix Studio (Dec 2024) cites, by name only without URLs: WebLabNY (floating metallic keychains), SpaceHey (MySpace-style social platform), Olivia Rodrigo's site, Starface (sticker icons), Public Domain (MacOS-style), Digital Fatigue (PC windows) — [Wix Studio](https://www.wix.com/studio/blog/y2k-design)
- Live demos:
  - https://trends.daisyui.com/y2k/demo/ — [daisyUI Y2K](https://trends.daisyui.com/trend/y2k/)
  - https://trends.daisyui.com/frutiger-aero/demo/ — [daisyUI Frutiger Aero](https://trends.daisyui.com/trend/frutiger-aero/)

**Authoritative articles and guides**
- NN/g, "Neobrutalism" (H. Sheikh, 2025-04-11): https://www.nngroup.com/articles/neobrutalism/
- Smashing Magazine, "The Split Personality of Brutalist Web Development" (F. O'Brien, 2020-01-08): https://www.smashingmagazine.com/2020/01/split-personality-brutalist-web-development/ (older practice, but the canonical taxonomy)
- LogRocket, "Web brutalism": https://blog.logrocket.com/ux-design/web-brutalism/
- Bejamas, Neubrutalism field notes: https://bejamas.com/insights/field-notes/neubrutalism-web-design-trend
- brutalist-web.design manifesto: https://brutalist-web.design/
- Webflow, Y2K aesthetic: https://webflow.com/blog/y2k-aesthetic
- Wix Studio, Y2K design (2024-12-18): https://www.wix.com/studio/blog/y2k-design
- daisyUI Trends:
  - Brutalism: https://trends.daisyui.com/trend/brutalism/
  - Neubrutalism: https://trends.daisyui.com/trend/neubrutalism/
  - Y2K: https://trends.daisyui.com/trend/y2k/
  - Y2K Techno-Skeuomorphism: https://trends.daisyui.com/trend/y2k-techno-skeuomorphism/
  - Frutiger Aero: https://trends.daisyui.com/trend/frutiger-aero/
- CARI (Consumer Aesthetics Research Institute): https://cari.institute/aesthetics/y2k-aesthetic
- The Plus Addons:
  - neo-brutalism CSS (numbers and contrast table): https://theplusaddons.com/blog/neo-brutalism-web-design/
  - Y2K CSS recipes: https://theplusaddons.com/blog/y2k-web-design/
- Older practice (2016), for history only:
  - Adobe blog, "Brutalist Web Designers Eschew Rules for UX Best Practices": https://blog.adobe.com/en/publish/2016/12/01/brutalist-web-designers-eschew-rules-for-ux-best-practices
  - WebdesignerDepot, "The rise and rise of the brutalist design trend": https://www.webdesignerdepot.com/2016/08/the-rise-and-rise-of-the-brutalist-design-trend/

### Inferences
- byooooob.com is cited both as neo-brutalist (NN/g) and as Y2K candy (Webflow). The two styles overlap in the "candy" zone, so the builder should treat N1 and Y2 as neighbours.
- For a Y2K chrome reference with a large brand, check Awwwards, Godly and Siteinspire collections tagged "Y2K", "chrome" or "retro". These were not fetched in this session.

### Gaps
- The live status and current design of each example URL was not verified in October 2026. Sites redesign often, and Gumroad is already flagged as possibly changed.
- Awwwards, Godly, Siteinspire and Dribbble collections were not fetched, so no curated "2025–2026 winners" list is included.
- The CSS-Tricks articles were not retrieved.
- The Wix Y2K examples lack URLs.
- The CARI history page (https://cari.institute/history) was not fetched.
