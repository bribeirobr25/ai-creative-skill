# Editorial / Magazine, Collage / Scrapbook, and Maximalist Web Design: Reference for an AI Website Builder

Scope note: three styles, researched together. Each key question below has per-style sub-headings. Sources are web articles fetched in Oct 2026. W3C/MDN links are canonical spec references cited for standards facts; they were **not fetched this session** and are cited from stable, well-known spec content. Anything under "Inferences" is **my synthesized recommendation** unless a source is attached. CSS values in Inferences are starting defaults I am proposing for a static HTML/CSS/vanilla-JS build, not values taken from a source.

Source quality warning: web search for these style names returned mostly SEO aggregator pages and spam mirrors (for example, several "scrapbook trend 2025" results were on unrelated domains such as carmi.illinois.gov and demo.evennia.com, and I did not use them). The usable sources are Webflow, Figma, Envato, KOTA, Designmodo, Smashing Magazine (Rachel Andrew), Awwwards, Really Good Designs, Subframe, FreeFrontend, Alpha Efficiency, a Medium post, a dev.to post and a small agency blog. Primary studio case studies were scarce.

---

## 1. Definition, origin and signature traits (4–6 per style)

### Takeaway
Editorial design brings print-magazine composition to the web: type hierarchy, asymmetric grids, large photography and a restrained palette. Collage/scrapbook layers paper textures, cut-outs, tape and hand-drawn marks so the page reads as made by hand. Maximalism deliberately fills space with clashing colour, mixed typefaces, patterns, layers and playful motion. 2025–2026 trend reports put collage and maximalism inside a wider "louder, more human" move away from 2010s flat minimalism.

### Cited Findings

**Editorial / magazine**
- Subframe's 25-example roundup (Feb 14 2025) gives no formal definition. It frames editorial sites as balancing form and function so readers can reach content easily and stay engaged. Recurring traits in its examples: minimalist layouts that let imagery and type lead, bold or elegant typography, striking photography for storytelling, restrained or monochrome palettes (sometimes with one bold accent), and clear navigation — [Subframe](https://www.subframe.com/tips/editorial-website-design-examples)
- One 2026 practitioner article says editorial layouts are replacing single hero sections. Its pattern: one primary story, two secondary stories and two to four smaller blocks, all above the fold. The largest cell is at least 1.6× its neighbour, because "balanced grids read as feature tables" — [Pravin Kumar, 2026](https://www.pravinkumar.co/blog/editorial-layouts-replace-hero-sections-webflow-2026)
- KOTA's 2026 trends describe an editorial-adjacent palette of "warm, tactile neutrals" (mushroom tones, chalky off-whites, rusted neutrals) that feel "editorial, textured and handcrafted", often paired with grain. It also notes a preference for unstaged "candid camera roll" photography — [KOTA, Nov 2025, mod. Oct 2026](https://kota.co.uk/blog/branding-inspiration-brand-design-trends-for-2026)
- Figma's 2026 trend page (Trend 4, bold typography) says "Typography is taking center stage in 2026, moving beyond legibility into storytelling". It recommends oversized headers, type layered over imagery and text animated on scroll — [Figma](https://www.figma.com/resource-library/web-design-trends/)

**Collage / scrapbook / cut-and-paste**
- Designmodo (first published 2013, updated Feb 16 2026) defines scrapbook style as imitating physical scrapbooking or collage by layering textures, images and decorative elements into a dimensional, multilayered look. It calls the style attention-grabbing but hard to execute — [Designmodo](https://designmodo.com/scrapbook-website-design/)
- Designmodo's traits: paper-based textures (cardboard cut-outs, thick paper blocks), non-uniform or patchy backgrounds (watercolour or grunge), overlapping layers with clear separation, neat shadows for depth, hand-drawn lettering and scribbles, vintage or fabric details (tags, badges, aged frames), cut-out images with folded corners, and tag-like menus — [Designmodo](https://designmodo.com/scrapbook-website-design/)
- Alpha Efficiency (Aug 26 2024): "Scrapbooking is all about layering." Its traits are overlapping imagery, torn-paper effects, polaroid-like images, nostalgic or retro feel, asymmetry that stays balanced, decorative handwriting or retro type, and subtle grunge or aged-paper texture — [Alpha Efficiency](https://alphaefficiency.com/scrapbook-style-web-design)
- Figma 2026 (Trend 11): scrapbook-style design with "sticker graphics, torn textures, cutout photos, and hand-drawn fonts", described as messy on purpose — [Figma](https://www.figma.com/resource-library/web-design-trends/)
- KOTA 2026 places collage under "controlled chaos". Type, imagery, tape and staples become compositional elements, and pages feel closer to protest posters or DIY zines than corporate brand books. Disruptive layouts are fine "provided the infrastructure stays calm" — [KOTA](https://kota.co.uk/blog/branding-inspiration-brand-design-trends-for-2026)

**Maximalism**
- Webflow (updated Oct 24 2025): maximalism rejects convention in favour of creative excess and "embraces discord and incongruity". "When you want to be loud, maximalism is here to express your creativity." — [Webflow](https://webflow.com/blog/maximalism-web-design)
- Webflow's traits: absurdity (quirky illustration, pointless animations, easter eggs), daring oversaturated colour that breaks colour-theory rules, conflicting textures and patterns, repetition, filled space with margins pushed to the edges, layering, retro references (8-bit, '70s pulp type, '80s camp), multiple fonts, and visual discordance in perspective and scale. It traces the origins to 1960s psychedelic poster art (Wes Wilson) — [Webflow](https://webflow.com/blog/maximalism-web-design)
- Envato (Oct 14 2025) on "brand maximalism": brands reject the flat, minimal 2010s look for branding that is "louder, funnier, stranger, and far more human". Traits: mixed serif, sans, script and stylized type; sticker-bomb graphics; and grain, glitch, halftone and scanned textures — [Envato](https://author.envato.com/hub/trend-deep-dive-brand-maximalism/)
- Figma 2026 (Trend 10): rich colours, overlapping visuals, bold fonts and dense compositions. It names Spotify and Liquid Death and advises energetic layouts "that pop without overwhelming the viewer" — [Figma](https://www.figma.com/resource-library/web-design-trends/)

### Inferences
- First-glance recognition test (synthesized):
  - **Editorial:** a large serif or condensed headline, an asymmetric multi-column grid, captions or bylines in small caps or mono, generous whitespace, a single accent colour, and full-bleed photography.
  - **Collage:** visible paper edges and texture, rotated elements (±1–8°), tape or stickers, cut-out (background-removed) photos with shadows, handwriting accents, and elements overlapping section boundaries.
  - **Maximalism:** almost no empty background, three or more saturated hues, three or more typefaces, repeated patterns or marquees, playful cursor or hover motion, and dense layering.
- Collage and maximalism overlap heavily: collage is often one *technique* inside maximalism. Editorial can absorb either one as an accent (for example, a collage feature story inside a calm magazine shell). The catalog should allow combinations, such as "editorial shell + collage hero".

### Gaps
- No authoritative design-history source (book or museum) was fetched. Origin claims beyond Webflow's psychedelic-poster lineage (for example Dada/Hannah Höch for collage, Brody/Carson/Emigre for editorial, Memphis for maximalism) are well known but **unsourced here**.

---

## 2. Recognised sub-variants within each style

### Takeaway
None of the sources formally define sub-variants. The groupings below combine what sources imply with my own synthesis, marked as such. The useful axes are: print genre for editorial, material and medium for collage, and the dominant layer for maximalism.

### Cited Findings
- Alpha Efficiency names three scrapbook directions: **traditional** (physical materials: printed photos, paper, paint, adhesives), **digital** (built in Figma or Canva with imagery, textures and playful fonts), and **hybrid** (start from a physical brainstorm, then build digitally) — [Alpha Efficiency](https://alphaefficiency.com/scrapbook-style-web-design)
- A Medium post describes a "hybrid style" that pairs vintage elements such as photo corners with clean, modern layouts — [Shariq Khan, Medium, Aug 2024](https://shariqkhan74.medium.com/scrapbook-layering-in-website-design-trends-techniques-and-best-practices-18f19b5a3bcd)
- KOTA ties collage to a **zine revival** and to brutalist/anti-design collage, citing W+K Amsterdam's Foam Talent Call — [KOTA](https://kota.co.uk/blog/branding-inspiration-brand-design-trends-for-2026); [It's Nice That, Foam](https://www.itsnicethat.com/articles/wieden-and-kennedy-amsterdam-foam-graphic-design-project-241125)
- KOTA describes riso/print texture as a related direction: misregistration, heavy grain and overprinted colours — [KOTA](https://kota.co.uk/blog/branding-inspiration-brand-design-trends-for-2026)
- Webflow names only **psychedelic maximalism** formally. Its examples imply retro/8-bit gaming maximalism (Y-N10, Vintageria, The Geek Designer), Geocities-style web chaos (Dino's Tomato Pie) and absurdist brand personas (Pablito Planeta) — [Webflow](https://webflow.com/blog/maximalism-web-design)
- Envato implies **tech maximalism** (brutalist forms, pixel and serif fonts, transparent cases; Nothing), **heritage maximalism** (Burberry's revived Equestrian Knight logo, 2023), and **sticker-bomb or texture maximalism** — [Envato](https://author.envato.com/hub/trend-deep-dive-brand-maximalism/)
- Figma lists anti-design/neo-brutalism (Balenciaga, Diesel, Mailchimp) as a separate neighbouring trend — [Figma](https://www.figma.com/resource-library/web-design-trends/)

### Inferences (synthesized taxonomy for the catalog)

**Editorial**
1. **Fashion/luxury magazine.** Hairline or high-contrast Didone serif, big photography, lots of whitespace, a near-monochrome palette and slow fades. Use for fashion, beauty, hospitality, galleries and premium DTC.
2. **Newspaper/broadsheet.** Dense multi-column grid, rules between columns, a masthead, datelines, serif body text and many headlines per screen. Use for media, newsletters, think tanks, B2B content hubs and "journal" sections.
3. **Indie/culture magazine (Kinfolk-type "slow" editorial).** Warm neutrals, grain, candid photography, a humanist serif with small caps, and long-form reading. Use for lifestyle, food, craft and wellness. This matches KOTA's "warm, tactile neutrals" ([KOTA](https://kota.co.uk/blog/branding-inspiration-brand-design-trends-for-2026)).
4. **Experimental/Swiss-editorial (Brody/Carson lineage).** Grotesk headlines, oversized numerals, rotated labels and text set into image. Use for agencies, architecture, design studios and music.

**Collage**
1. **Analog scrapbook.** Kraft or cream paper, washi tape, polaroids, handwriting and stitched or stapled details. Use for kids, family, bakeries, crafts, weddings and personal blogs.
2. **Digital/editorial collage.** Clean background with background-removed cut-outs, flat colour shapes and halftone; tidy and graphic. Use for DTC beverage and beauty (the Ghia-type layout in [KOTA](https://kota.co.uk/blog/branding-inspiration-brand-design-trends-for-2026)), campaigns and portfolios.
3. **Punk/zine collage.** Photocopy grain, ransom-note mixed letters, torn edges and black-and-white with one spot colour. Use for music, events, bars, streetwear and activism.
4. **Riso/print collage.** Two or three spot inks, `mix-blend-mode: multiply` overprint and misregistration offsets. Use for studios, publishers and illustrators.

**Maximalism**
1. **Pattern/ornament maximalism.** Wallpaper patterns, florals and borders on borders. Use for interiors, fashion and heritage brands.
2. **Typographic maximalism.** Screen-filling type, many families, marquees and kinetic headlines; images are secondary. Use for agencies, events and music.
3. **Retro/pixel/Y2K maximalism.** 8-bit sprites, Geocities widgets, gloss gradients and cursor toys. Use for gaming, Gen-Z fashion and nightlife. Matches Y-N10, Dino's and Vintageria ([Webflow](https://webflow.com/blog/maximalism-web-design)) and KOTA's Y2K gloss ([KOTA](https://kota.co.uk/blog/branding-inspiration-brand-design-trends-for-2026)).
4. **Brand/candy maximalism (CPG).** Saturated brand colours, mascots, stickers, oversized product shots and repeated CTAs. Use for food and drink, CPG and toys. Examples: BEHAVE, Curry Cafe ([Webflow](https://webflow.com/blog/maximalism-web-design)) and Liquid Death ([Figma](https://www.figma.com/resource-library/web-design-trends/)).

### Gaps
- No source gives an industry-standard taxonomy of sub-variants for any of the three styles. Treat the above as a catalog design decision.

---

## 3. Most-used layouts: hero patterns, grids, navigation, product grids, section rhythm, mobile

### Takeaway
Editorial is the only style with documented grid mechanics: named-line CSS Grid with content/full breakout lanes, 8–12 column asymmetric grids, and multi-column text. Collage and maximalism are usually built on an ordinary grid, with overlap and rotation layered on top. On mobile, all three collapse to one column, keep one or two signature overlaps, and reduce rotation.

### Cited Findings
- Rachel Andrew's Smashing article (Oct 4 2019) on editorial patterns uses named grid lines with `-start`/`-end` suffixes, which create implicit areas (`content`, `full`, `center`, `start-half`, `end-half`). Breakout items span `full` while text stays in `content` or `center`. `grid-template-columns: subgrid` passes the parent's tracks and line names to children. In 2019 subgrid worked only in Firefox Nightly, so that claim is **outdated**; subgrid now ships in all major engines (see the MDN reference in Inferences) — [Smashing Magazine](https://www.smashingmagazine.com/2019/10/editorial-design-patterns-css-grid-subgrid-naming/)
- Verbatim example from the article:
  ```css
  .full-2 { grid-column: full; display: grid; grid-template-columns: subgrid; }
  .full-2 > div { grid-column: center; }
  .content li:nth-child(2) { grid-column: start-half; }
  .content li:nth-child(3) { grid-column: end-half; }
  ```
  — [Smashing Magazine](https://www.smashingmagazine.com/2019/10/editorial-design-patterns-css-grid-subgrid-naming/)
- A FreeFrontend editorial demo (2026) uses a strict 8-column grid, `repeat(8, 1fr)`. Overlap comes from grid line coordinates, not absolute positioning: `.page-one__photo { grid-column: 1/8; grid-row: 1/4; z-index: -1 }` and `.page-one__header { grid-column: 7/9; grid-row: 2/3 }`. Dense text flows with the `columns` property, media queries remap columns and rows, and the demo is under 5 KB with zero JavaScript — [FreeFrontend](https://freefrontend.com/code/editorial-css-grid-magazine-layout-2026-03-31/)
- Editorial "front page" hero pattern: four-column named-area grid at desktop (checked at 1440px), two columns on tablet with the primary story spanning both, one column on mobile ordered by priority. Tertiary cards have four fields (image, eyebrow, headline, link) and no description. Use two weights, one accent colour and one image crop ratio for secondary and tertiary images. Primary headline is 8–14 words with a one- or two-line deck. On mobile, separate primary from secondary stories with a thin accent line or background shade and enlarge tertiary images — [Pravin Kumar](https://www.pravinkumar.co/blog/editorial-layouts-replace-hero-sections-webflow-2026)
- The same article cites performance statistics (NN/g 2026 decision time 7.4 s; Baymard 2025: editorial ecommerce homepages had 23% lower add-to-cart than product-first pages; and others). It does **not link the underlying studies**, and I could not verify them. Treat them as unverified — [Pravin Kumar](https://www.pravinkumar.co/blog/editorial-layouts-replace-hero-sections-webflow-2026)
- Scrapbook navigation can use tag-like menus and collage-style widget arrangements. Designmodo's Putzengel example puts each section on its own layer to keep the layout clear — [Designmodo](https://designmodo.com/scrapbook-website-design/)
- Maximalist layout guidance: fill negative space, push margins to the edge, layer visuals, and build off-balance compositions with unusual perspective and scale. Curry Cafe repeats CTAs; Y-N10 uses a diagonal scroll — [Webflow](https://webflow.com/blog/maximalism-web-design)
- Choreus (maximalist) uses a full-bleed slideshow of artist work with large type that steers toward hiring — [Jack Christian](https://jackchristian.com.au/blog/my-top-5-maximalist-websites/)

### Inferences (synthesized defaults)

**Editorial grid** (named-line breakout, modern version of the Smashing pattern):
```css
.page {
  --gutter: clamp(1rem, 2.5vw, 2rem);
  --measure: 68ch;                 /* 60–75ch reading measure */
  display: grid;
  column-gap: var(--gutter);
  grid-template-columns:
    [full-start] minmax(var(--gutter), 1fr)
    [wide-start] minmax(0, 12rem)
    [content-start] min(var(--measure), 100% - 2*var(--gutter)) [content-end]
    minmax(0, 12rem) [wide-end]
    minmax(var(--gutter), 1fr) [full-end];
}
.page > * { grid-column: content; }
.page > .wide { grid-column: wide; }
.page > .bleed { grid-column: full; }
```
- **Front page / index:** 12 columns, 24px gutter, max-width 1280–1440px. Lead story spans 7–8 columns and the side stack 4–5 (about 1.6:1 or more). Below it, 3- or 4-up cards with one crop ratio (4:5 or 3:2).
- **Article page:** 680–720px measure, wide images break out to 960–1100px, full-bleed images span 100vw. Pull quotes break into the wide lane.
- **Product grids (editorial commerce):** 2-up at large size alternating with 3- or 4-up, interrupted every 6–8 products by a full-width "story" tile. Captions sit under the image: product name in serif, price in small caps.
- **Navigation:** a centred masthead wordmark, a thin section bar below it (uppercase, letter-spacing about 0.08em), a hamburger only under 768px, and an optional sticky slim bar after scroll.
- **Section rhythm:** large feature, then dense 3-up, then full-bleed image with caption, then a quote band, then a 2-col text-and-image row. Use horizontal hairline rules (1px currentColor at 20–30% opacity) as separators.

**Collage layout:**
- Use a normal 12-column grid with `grid-template-areas`. Put collage pieces in overlapping cells (same row/column ranges) and set `z-index` explicitly. Rotate pieces with a CSS custom property (`--r`).
- **Hero:** central headline on a paper card, surrounded by three to seven cut-out photos and stickers. The DOM order is headline, CTA, then decorations (which are `aria-hidden`).
- **Product grid:** polaroid cards in a regular grid with alternating small rotations (`nth-child`: -2°, 1.5°, -1°, 2.5°). On hover, straighten the card and lift it.
- **Mobile:** keep one or two overlaps, set rotations to ±1–2° or 0 for any card that contains text, and hide some decorative stickers below 600px (`display: none`).

**Maximalist layout:**
- Full-bleed coloured section blocks with no white background, and a marquee band between sections. Use an asymmetric grid with oversized type crossing column lines. Repeat the CTA every one to two screens. Cards use thick borders (3–4px) and hard offset shadows (`6px 6px 0 #000`).
- **Mobile:** keep the colour blocking and type scale (use `clamp`), stop marquees under reduced motion, stack layers, and keep a single primary CTA visible.

### Gaps
- I found no source-backed numeric gutter or max-width values for collage or maximalist sites. The numbers above are my synthesis.
- I could not fetch live sites to measure their grids. Browser inspection would be needed.

---

## 4. Typography: families, scale, weights, tracking, line-height, free pairings

### Takeaway
Editorial pairs a display serif (Didone, transitional or soft "wonky" serif) with a neutral grotesk or a mono for meta text. It uses a steep scale (display 4–8× body) and tight display tracking. Collage mixes a bold grotesk or serif with handwriting and typewriter accents. Maximalism mixes three or more families (pixel, decorative, condensed, script) and often treats type as image. All three styles still need a plain, legible body face.

### Cited Findings
- Editorial pattern guidance: two weights in total, one for headlines and one for body — [Pravin Kumar](https://www.pravinkumar.co/blog/editorial-layouts-replace-hero-sections-webflow-2026)
- Editorial readability: use clean, legible fonts, a consistent hierarchy and enough text/background contrast — [Subframe](https://www.subframe.com/tips/editorial-website-design-examples)
- Maximalist type: combine multiple typefaces, including retro and mismatched ones, but pair busy visuals with clear, legible type. The cited reference is Keeli McCarthy's *Wimmen's Comix* cover, which sets clean type against a swirling background — [Webflow](https://webflow.com/blog/maximalism-web-design)
- Brand maximalism type: mixed serif, sans, script and stylized faces; decorative serifs (Burberry); handwritten fonts; pixel fonts (Nothing); custom typefaces (Pepsi) — [Envato](https://author.envato.com/hub/trend-deep-dive-brand-maximalism/)
- Scrapbook type: handwriting-style or retro fonts used as design elements; playful fonts for headings and quotes, overlaid on images or patterns — [Alpha Efficiency](https://alphaefficiency.com/scrapbook-style-web-design); [Medium](https://shariqkhan74.medium.com/scrapbook-layering-in-website-design-trends-techniques-and-best-practices-18f19b5a3bcd)
- 2026 type trends: high-contrast blackletter and serif revivals (modern gothic), kinetic headlines, deliberate use of default system fonts in anti-design, and hand-drawn type as an authenticity signal — [KOTA](https://kota.co.uk/blog/branding-inspiration-brand-design-trends-for-2026)
- A pairing directory lists Newsreader + Instrument Serif and Fraunces + Instrument Sans, all Google Fonts families — [maxibestof: Newsreader × Instrument Serif](https://maxibestof.one/typefaces/newsreader/pairing/instrument-serif); [maxibestof: Fraunces × Instrument Sans](https://maxibestof.nuxt.dev/typefaces/fraunces/pairing/instrument-sans)
- WCAG 1.4.12 Text Spacing: content must survive user overrides of line-height 1.5×, paragraph spacing 2×, letter-spacing 0.12em and word-spacing 0.16em without loss. Fixed-height text boxes on collage cards break under these overrides — [W3C WCAG 2.2 Understanding 1.4.12](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html)

### Inferences (synthesized; all families listed are on Google Fonts. Verify each licence (OFL or Apache) before self-hosting via Fontsource)

**Editorial pairings**

| Sub-variant | Display | Text | Meta/caption |
|---|---|---|---|
| Fashion | Bodoni Moda or Playfair Display (opsz) | Inter or Instrument Sans | IBM Plex Mono |
| Newspaper | Libre Caslon Display / Libre Caslon Text, or Newsreader (opsz) | Source Serif 4 | Inter, small caps |
| Indie/slow | Fraunces (soft, opsz), Instrument Serif, Gloock | Newsreader or EB Garamond | DM Mono |
| Swiss-experimental | Inter Tight / Archivo (wide) / Space Grotesk | Inter | JetBrains Mono |

Editorial type settings:
- Scale ratio 1.333–1.5 (perfect fourth to perfect fifth).
- Body `clamp(1.0625rem, 0.95rem + 0.35vw, 1.25rem)`, line-height 1.5–1.65.
- H1 display `clamp(2.75rem, 1rem + 6vw, 7.5rem)`, line-height 0.95–1.05, letter-spacing -0.02 to -0.04em, weight 300–500 for Didones and 600–800 for grotesks.
- Kicker/eyebrow: 0.75–0.8125rem, uppercase, letter-spacing 0.08–0.14em.
- Captions: 0.8125–0.875rem, line-height 1.4, muted colour that still passes 4.5:1.
- Drop cap: `initial-letter: 3` where supported, with a `::first-letter` float fallback.
- Use `font-variant-numeric: oldstyle-nums proportional-nums` in body text and `font-feature-settings: "smcp"` for small caps where the font supports them.
- Set `text-wrap: balance` on headlines and `text-wrap: pretty` on paragraphs (progressive enhancement).

**Collage pairings**
- Structure: Archivo Black, Anton or DM Serif Display.
- Body: Inter or Work Sans.
- Accents: Caveat, Permanent Marker or Gochi Hand (handwriting); Special Elite or Courier Prime (typewriter); Rubik or Bricolage Grotesque for friendly UI.
- Settings: handwriting only at 1.25rem or larger, for short phrases (≤ 8 words), never body text. Use "ransom-note" mixed letters only on decorative headings. Render them as real text with `aria-label` on the wrapper, or as an SVG with `<title>`. Do not use separate span-per-letter with different fonts unless the accessible name is preserved.

**Maximalist pairings**
- Condensed display: Anton, Bebas Neue, Big Shoulders Display.
- Expressive: Unbounded, Syne, Climate Crisis, Shrikhand, Bungee, Monoton.
- Pixel: Press Start 2P, VT323, Silkscreen.
- Plain body: Inter, Rubik or Space Grotesk.
- Cap the page at four families (synthesized limit), with body text always in one plain family. Display sizes can reach 12–20vw on hero words. Keep tracking on condensed caps around 0 to +0.02em.
- Variable fonts (Fraunces, Bricolage Grotesque, Unbounded, Syne) let one file cover several "personalities", which helps performance.

### Gaps
- Typewolf and Fonts In Use pages were not successfully retrieved, so there are no "fonts used on real editorial sites" data points from them.
- I did not verify licences individually. Google Fonts families are generally OFL or Apache 2.0.

---

## 5. Colour: palettes and contrast practice

### Takeaway
Editorial is mostly monochrome or warm-neutral with one accent. Collage uses paper neutrals (kraft, cream, newsprint) with two or three spot colours and multiply overprint. Maximalism uses oversaturated, deliberately clashing palettes. In every style, text must sit on a solid or scrimmed surface to meet WCAG AA.

### Cited Findings
- Editorial examples tend toward restrained or monochrome palettes, sometimes with one bold accent (for example, Cole Haan's yellow background) — [Subframe](https://www.subframe.com/tips/editorial-website-design-examples)
- Editorial front pages should use one accent colour across the layout — [Pravin Kumar](https://www.pravinkumar.co/blog/editorial-layouts-replace-hero-sections-webflow-2026)
- 2026 warm editorial neutrals: mushroom tones, chalky off-whites, rusted neutrals, often with grain. KOTA also names "hyper-chromatic, cinematic colour" (saturated blocks, dramatic gradients) as a separate trend — [KOTA](https://kota.co.uk/blog/branding-inspiration-brand-design-trends-for-2026)
- Maximalist colour: contrasting, oversaturated palettes that break colour-theory rules, balanced with restrained elements. Example: Mack and Pouya Photography uses pink, yellow and blue — [Webflow](https://webflow.com/blog/maximalism-web-design)
- Pest Stop Boys uses vibrant colours with large type — [Jack Christian](https://jackchristian.com.au/blog/my-top-5-maximalist-websites/)
- The Awwwards "Collage" SOTD (collagecrafting.com, 2017) used a two-colour #000/#FFF palette. Collage does not have to be colourful. This example is **older practice** — [Awwwards](https://www.awwwards.com/sites/collage)
- WCAG 2.2 SC 1.4.3 requires 4.5:1 for normal text and 3:1 for large text (≥ 24px regular or ≥ 18.66px bold) — [W3C 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
- SC 1.4.11 requires 3:1 for UI component boundaries and meaningful graphics — [W3C 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)

### Inferences (synthesized starter palettes; check every text pair with a contrast checker)
- **Editorial fashion:** ink `#111111`, paper `#FAFAF7`, mid-grey caption `#5C5C5C` (about 6.5:1 on paper), accent `#C8102E` or another single brand colour.
- **Editorial slow:** paper `#F2EDE4`, ink `#2B2622`, muted `#6B5F55`, accent rust `#A4492B`.
- **Newspaper:** newsprint `#F4F1EA`, ink `#1A1A1A`, rule `#1A1A1A` at 25%.
- **Collage analog:** kraft `#C8A97E` (as background only, with text on cream cards), cream `#FFF8E7`, tape `#F4E3A1` at about 70% opacity, marker red `#D7263D`, ink `#1E1E1E`.
- **Collage riso:** fluoro pink `#FF48B0`, blue `#0078BF`, yellow `#FFE800` overprinted with `mix-blend-mode: multiply` on `#FBF8F1`.
- **Maximalist candy:** `#FF3EA5`, `#FFD400`, `#00C2FF`, `#7A2BFF`, `#00D27A`, plus `#0B0B0B` for text plates.
- **Contrast rule for loud palettes:** put body text on solid "plates" (cards or bands) of ink-on-light or light-on-ink. Never place body text directly on patterns or photos. On images, use a scrim (`linear-gradient(transparent, rgb(0 0 0 / .65))`) or a solid label background.
- Check headline-on-saturated pairs. White on `#FF3EA5` is about 3:1, so it is acceptable only for large text, and black on it is safer. Yellow `#FFD400` fails with white text and needs dark ink.
- Provide `@media (prefers-contrast: more)` to drop textures and patterns behind text, and `forced-colors: active` to remove decorative backgrounds.

### Gaps
- No source gave specific hex palettes for any style. The palettes above are synthesized.

---

## 6. Components and details

### Takeaway
Signature components are what make the styles legible to users and to the AI builder. Editorial relies on pull quotes, drop caps, captions, bylines, kickers and rules. Collage relies on tape, stickers, torn edges, polaroids, paper clips, handwriting and doodles. Maximalism relies on marquees, sticker-bombs, patterned borders, mascots, cursor toys, easter eggs and badges.

### Cited Findings
- **Scrapbook components:** cardboard cut-outs, thick paper blocks, tags, badges, aged frames, textile backgrounds, cut-out images with slightly folded corners, protruding elements and tag-like menus — [Designmodo](https://designmodo.com/scrapbook-website-design/)
- Polaroid-like images, torn-paper effects and aged-paper texture — [Alpha Efficiency](https://alphaefficiency.com/scrapbook-style-web-design)
- Photo corners, faded florals and distressed edges — [Medium](https://shariqkhan74.medium.com/scrapbook-layering-in-website-design-trends-techniques-and-best-practices-18f19b5a3bcd)
- Sticker graphics, torn textures, cut-out photos and hand-drawn fonts — [Figma](https://www.figma.com/resource-library/web-design-trends/)
- Tape and staples as compositional elements — [KOTA](https://kota.co.uk/blog/branding-inspiration-brand-design-trends-for-2026)
- **CSS paper techniques** (Suzanne Aitchison, Jan 2021):
  - Folded paper is an `::after` pseudo-element with two layered linear gradients (left-to-right and top-to-bottom), placed after the text so the text appears folded too.
  - Tape is semi-transparent (`opacity: 0.5`) with a small dotted border on the ends, so they look serrated as if cut.
  - A pinned card's pin is built from linear and radial gradients.
  - A tear-off "contact me" slip is angled with `skew` plus gradients.
  - Contact links are marked up as list items so screen readers announce a list and the content degrades to a plain list without CSS. `rem` units keep the effect intact when users scale text.
  - The author had not solved torn or crumpled edges in that post.
  — [dev.to](https://dev.to/s_aitchison/3-experiments-with-css-paper-effects-2o56)
- A 2026 CSS folded-corner technique article exists — [Kitty Giraudel, Mar 2026](https://kittygiraudel.com/2026/03/05/folded-corner-with-css/) (search result only; not fetched)
- Combining `clip-path` and masks for paper shapes — [CSS IRL, "Paper Snowflakes"](https://css-irl.info/paper-snowflakes-combining-clipping-and-masking-in-css/) (search result only; not fetched)
- **Maximalist components:** quirky illustrations, pointless animations, meta jokes, easter eggs, blinking CTAs and a visitor counter (Dino's Tomato Pie), and repeated CTAs (Curry Cafe) — [Webflow](https://webflow.com/blog/maximalism-web-design)
- Butterfly cursor and hover animations on flowers in the hero (Ellen Porteus) — [Jack Christian](https://jackchristian.com.au/blog/my-top-5-maximalist-websites/)
- Sticker-bomb layering of icons, illustrations and emojis — [Envato](https://author.envato.com/hub/trend-deep-dive-brand-maximalism/)
- **Editorial components:** tertiary cards with image, eyebrow, headline and link; primary story with headline, deck, visual and one CTA — [Pravin Kumar](https://www.pravinkumar.co/blog/editorial-layouts-replace-hero-sections-webflow-2026)

### Inferences (synthesized component specs)

**Editorial**
- **Pull quote:** `<figure class="pullquote"><blockquote><p>…</p></blockquote><figcaption>— Name</figcaption></figure>`. Set it in the display serif at 1.75–2.5rem, line-height 1.15, with a 2px rule above and below or a 4px left rule in the accent colour. Break it into the wide lane. Do not duplicate body text in a visually-only pull quote. If you must, mark the duplicate `aria-hidden="true"`.
- **Drop cap:**
  ```css
  .lede::first-letter { initial-letter: 3 2; font-family: var(--display); margin-inline-end: .1em; }
  @supports not (initial-letter: 1) {
    .lede::first-letter { float: left; font-size: 4.2em; line-height: .8; padding: .06em .08em 0 0; }
  }
  ```
- **Caption/credit:** `figcaption` at 0.8125rem with the photographer credit in uppercase mono. Put a caption on every image.
- **Byline/dateline row:** author, `<time datetime>`, read time and section, in small caps.
- **Kicker:** a section label above the headline, uppercase, in the accent colour.
- **Hairline rules:** `border-block-start: 1px solid color-mix(in srgb, currentColor 25%, transparent)`.
- **Footnotes/sidenotes:** on wide screens, sidenotes go in the right margin column. On mobile they become inline toggles (`<details>`).
- **Table of contents** for long reads, and an optional reading-progress bar (static, or a scroll-driven animation).

**Collage**
- **Tape:** a `::before` of 90×28px, `background: rgb(244 227 161 / .7)`, `rotate: -4deg`, with jagged ends from `clip-path: polygon(…)` zig-zags or `mask: conic-gradient`, and a light shadow.
- **Polaroid:** a white frame with 12px padding and 40px bottom padding, `box-shadow: 0 1px 2px rgb(0 0 0 / .15), 0 8px 20px rgb(0 0 0 / .12)`, rotation from `--r`, and a handwritten caption in the bottom band.
- **Sticker:** a circle or die-cut SVG with a 4–6px white outline, applied with `filter: drop-shadow(0 0 0 #fff)` chains or an SVG stroke, plus a soft shadow. Hover: `scale(1.06) rotate(-3deg)`.
- **Torn edge:** an SVG path or `clip-path: polygon()` with 20–40 irregular points on one edge, or `mask-image` from a torn-edge PNG or SVG. Reuse one mask across sections.
- **Paper clip / pin / staple:** small inline SVGs, `aria-hidden`.
- **Doodles:** hand-drawn SVG underlines, circles and arrows that point to CTAs, animated with `stroke-dashoffset` on reveal (reduced-motion: show them already drawn).
- **Cut-out photo:** a transparent WebP or AVIF product or person with `filter: drop-shadow(0 6px 10px rgb(0 0 0 / .25))` and a white "cut" outline via SVG `feMorphology` dilate.

**Maximalist**
- **Marquee band:** a duplicated inline track animated with `translateX`, a pause control (WCAG 2.2.2), and stopped under reduced motion.
- **Sticker-bomb cluster:** absolutely positioned badges inside a relatively positioned hero, all decorative.
- **Patterned borders and frames:** `border-image` with SVG patterns, or repeating `conic-gradient` checkerboards.
- **Hard-shadow cards:** `border: 3px solid #000; box-shadow: 6px 6px 0 #000`. On hover the card moves to `translate(-2px,-2px)` and the shadow grows to `8px 8px`.
- **Cursor toy:** a custom cursor follower. It must not replace the native cursor for text or inputs, and is off under reduced motion or `(pointer: coarse)`.
- **Easter eggs:** harmless, never blocking content.

### Gaps
- Exact code for torn and crumpled edges and for washi tape was not available from fetched sources. The dev.to CodePens were not readable as text.

---

## 7. Effects, motion and CSS/JS techniques (plain HTML/CSS/vanilla JS)

### Takeaway
Everything these styles need can be done without frameworks: CSS Grid overlap via line coordinates, `rotate`/`translate` custom properties, `clip-path`/`mask`, `mix-blend-mode` for overprint, SVG `feTurbulence`/`feDisplacementMap` for grain and rough edges, CSS `@keyframes` marquees, and IntersectionObserver or scroll-driven animations for reveals. All motion must be gated by `prefers-reduced-motion`.

### Cited Findings
- Grid-line overlap with `z-index: -1` is a zero-JavaScript editorial technique. The demo cites support as Chrome 57+, Edge 16+, Firefox 52+, Safari 10.1+ — [FreeFrontend](https://freefrontend.com/code/editorial-css-grid-magazine-layout-2026-03-31/)
- Subgrid keeps nested content aligned with parent named lines — [Smashing](https://www.smashingmagazine.com/2019/10/editorial-design-patterns-css-grid-subgrid-naming/)
- The Awwwards "Collage" SOTD (2017) used WebGL, PixiJS, GSAP and jQuery. Its Dev Award scores were Animations 8.00 and Accessibility 7.38. This is **older practice**; the heavy WebGL/jQuery stack is not needed for 2026 static builds — [Awwwards](https://www.awwwards.com/sites/collage)
- Maximalist motion examples: scroll-driven, bubbly 3D effects with audio (Slosh Seltzer), scroll animations (Choreus), and a butterfly cursor (Ellen Porteus) — [Jack Christian](https://jackchristian.com.au/blog/my-top-5-maximalist-websites/)
- Figma 2026: animate text on scroll and layer type over imagery — [Figma](https://www.figma.com/resource-library/web-design-trends/)
- Texture vocabulary: grain, glitch, halftone and scanned textures — [Envato](https://author.envato.com/hub/trend-deep-dive-brand-maximalism/)
- Riso texture: misregistration, heavy grain and overprinted colours — [KOTA](https://kota.co.uk/blog/branding-inspiration-brand-design-trends-for-2026)
- WCAG 2.2 SC 2.3.3 (AAA) says motion triggered by interaction can be disabled. Honouring `prefers-reduced-motion` is the standard technique — [W3C 2.3.3](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html)
- SC 2.2.2 (AA) requires a pause, stop or hide mechanism for auto-moving content that lasts more than 5 seconds and runs alongside other content. This applies to marquees and carousels — [W3C 2.2.2](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)
- SC 2.3.1 (A): nothing may flash more than three times per second. This matters for maximalist blink and glitch effects — [W3C 2.3.1](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html)
- MDN references: `clip-path` ([MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/clip-path)), `mask-image` ([MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/mask-image)), `mix-blend-mode` ([MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/mix-blend-mode)), `feTurbulence` ([MDN](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feTurbulence)), `initial-letter` ([MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/initial-letter)), subgrid ([MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout/Subgrid)), scroll-driven animations ([MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll-driven_animations)) — canonical references, not fetched

### Inferences (synthesized code recipes)

**Shared tokens and motion gate**
```css
:root { --ease: cubic-bezier(.2,.7,.2,1); --dur: 600ms; }
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: .01ms !important; animation-iteration-count: 1 !important;
    transition-duration: .01ms !important; scroll-behavior: auto !important; }
}
```

**Editorial motion: quiet**
- Fade or translate-up reveals of 12–24px over 500–700ms, staggered by 60–80ms. Fire once via IntersectionObserver with `threshold: .15`.
- Image reveal via `clip-path: inset(0 0 100% 0)` to `inset(0)` over 800ms.
- Optional scroll-driven progress bar: `animation-timeline: scroll()`, wrapped in `@supports (animation-timeline: scroll())`.

**Grain overlay (all three styles; strongest in collage)**
```html
<svg width="0" height="0" aria-hidden="true" style="position:absolute">
  <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".8" numOctaves="3" stitchTiles="stitch"/>
  <feColorMatrix type="saturate" values="0"/></filter></svg>
```
```css
body::after { content:""; position:fixed; inset:0; pointer-events:none; z-index:9999;
  filter:url(#grain); opacity:.06; mix-blend-mode:multiply; }
```
- Performance alternative: a 256×256 tiled noise PNG or WebP (~10–20 KB) as `background-image`. A live full-viewport `feTurbulence` repaints on scroll in some browsers, so prefer the static tile. Suggested opacity: 0.04–0.08 for editorial, 0.10–0.18 for collage.

**Collage rotation and overlap**
```css
.collage { display:grid; grid-template-columns:repeat(12,1fr); grid-auto-rows:minmax(4rem,auto); }
.piece { grid-column:var(--c); grid-row:var(--rw); rotate:var(--r,0deg); z-index:var(--z,1);
  transition: rotate .3s var(--ease), translate .3s var(--ease); }
.piece:hover, .piece:focus-within { rotate:0deg; translate:0 -4px; }
@media (max-width:600px){ .piece { grid-column:1/-1; grid-row:auto; rotate:calc(var(--r,0deg) * .3); } }
```
- Rough or torn edge via SVG displacement: `feTurbulence baseFrequency="0.04" numOctaves="2"` feeding `feDisplacementMap scale="6–12"`, applied to a paper card's background element, never to text.
- Riso overprint: two copies of the same image or text in spot colours with `mix-blend-mode:multiply`, the second offset by `translate(2px,-1px)` for misregistration.
- Halftone: `background: radial-gradient(circle, #000 1px, transparent 1.5px) 0 0/6px 6px`, masked over an image, or an SVG pattern.
- Cut-out outline: SVG `feMorphology operator="dilate" radius="4"` on alpha, flooded white, composited under the source.

**Maximalist motion**
```css
.marquee { overflow:hidden; }
.marquee__track { display:flex; width:max-content; animation: marquee 30s linear infinite; }
.marquee:hover .marquee__track, .marquee.is-paused .marquee__track { animation-play-state: paused; }
@keyframes marquee { to { transform: translateX(-50%); } }
@media (prefers-reduced-motion: reduce){ .marquee__track { animation: none; } }
```
- Provide a visible pause button that toggles `.is-paused` (WCAG 2.2.2). Duplicate the track content with `aria-hidden="true"` on the copy.
- Use spring-ish hover, for example `transition: transform .25s cubic-bezier(.34,1.56,.64,1)`.
- Run cursor followers via `requestAnimationFrame` and pointer events only when `matchMedia('(pointer:fine) and (prefers-reduced-motion:no-preference)')` matches.
- Pattern backgrounds should be CSS gradients (no requests), for example a checkerboard: `repeating-conic-gradient(#FFD400 0 25%, #FF3EA5 0 50%) 0 0/40px 40px`.
- For "Geocities" effects such as blink, keep the rate at 1 Hz or slower, which is far below the 3-flashes-per-second threshold. Avoid red flashes.

### Gaps
- No fetched source benchmarks the paint cost of full-screen SVG filters or `mix-blend-mode` layers. The performance advice above is synthesized general practice.

---

## 8. Accessibility pitfalls and fixes; performance notes

### Takeaway
None of the trend sources address accessibility, and Webflow, Alpha Efficiency and the Medium post explicitly omit it. The main risks are text on busy backgrounds, rotated or handwritten text, DOM order that differs from visual order in overlapping grids, auto-moving marquees, decorative images announced by screen readers, and heavy textures or images that hurt LCP.

### Cited Findings
- Webflow's maximalism article does not address accessibility or readability for dense, high-contrast or animated designs — [Webflow](https://webflow.com/blog/maximalism-web-design)
- Alpha Efficiency gives no accessibility guidance on contrast, decorative-font legibility or motion — [Alpha Efficiency](https://alphaefficiency.com/scrapbook-style-web-design)
- Designmodo warns that a poorly organized scrapbook design "will look messy and heavy" and says to plan the structure first — [Designmodo](https://designmodo.com/scrapbook-website-design/)
- Semantic list markup and `rem` units keep paper-effect components usable without CSS and when text is scaled — [dev.to](https://dev.to/s_aitchison/3-experiments-with-css-paper-effects-2o56)
- Editorial readability tips: legible fonts, consistent hierarchy, sufficient contrast, and images optimized for fast loading — [Subframe](https://www.subframe.com/tips/editorial-website-design-examples)
- WCAG 1.3.2 Meaningful Sequence: when order affects meaning, the programmatic reading order must be correct. CSS grid placement can make visual order diverge from DOM order — [W3C 1.3.2](https://www.w3.org/WAI/WCAG22/Understanding/meaningful-sequence.html)
- WCAG 2.4.3 Focus Order — [W3C 2.4.3](https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html)
- WCAG 2.2 SC 2.4.11 Focus Not Obscured (Minimum, AA): a focused element must not be entirely hidden by author content. Overlapping collage pieces and sticky bars can violate this — [W3C 2.4.11](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html)
- WCAG 1.4.10 Reflow: no two-dimensional scroll at 320 CSS px width. Wide collages and rotated elements that overflow the viewport fail this — [W3C 1.4.10](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)
- The 2017 Collage SOTD scored Accessibility 7.38/10 in Awwwards' Dev Award — [Awwwards](https://www.awwwards.com/sites/collage)

### Inferences (synthesized checklist)

**Busy backgrounds (collage, maximalism).** Put all body text on solid plates. Keep texture opacity behind text at 0.08 or below, or drop it there. Ensure 4.5:1 against the *worst* pixel under the text. In `prefers-contrast: more` and `forced-colors`, remove patterns and textures.

**Rotated text.**
- Keep any rotated element containing more than a few words within ±3°.
- Never rotate body copy or form fields.
- Rotated text keeps its accessible text but can clip on zoom, so test at 200% and 400%.
- Vertical labels (`writing-mode: vertical-rl`) are acceptable for short decorative labels only.

**Handwriting and decorative fonts.** Use them only for short accents of 1.25rem or larger. Do not use them for navigation, prices or instructions. Ransom-note headings need one accessible name (real text, or SVG with `<title>`).

**Reading order.**
- Write HTML in reading order: headline, deck, CTA, then decorations. Place pieces visually with grid; never reorder with CSS for content that matters.
- Avoid `order` and `grid-auto-flow: dense` for content cards.
- Mark decorative stickers, tape and doodles `aria-hidden="true"` with `alt=""` on their images.
- Any sticker that carries meaning, such as "New" or "-20%", must exist as real text in the card.

**Focus.**
- Use visible focus rings (`outline: 3px solid; outline-offset: 3px`) with 3:1 contrast against both paper and colour backgrounds.
- Raise `z-index` on `:focus-within` so overlapped cards come forward (WCAG 2.4.11).

**Motion.**
- Marquees and auto-carousels need a pause control (2.2.2).
- No flashing above 3 Hz (2.3.1).
- Gate parallax, cursor toys, scroll-jacking and diagonal scrolls behind `prefers-reduced-motion: no-preference`.
- Never hijack native scroll; Y-N10-style diagonal scroll (cited by [Webflow](https://webflow.com/blog/maximalism-web-design)) is an anti-pattern for accessibility.

**Editorial specifics.**
- Keep the measure at 75ch or less, with line-height ≥ 1.5 for body text.
- Pull quotes must not create duplicate announcements.
- Use `<article>`, `<header>`, `<figure>/<figcaption>`, `<time>`, and a clear h1 to h3 hierarchy.
- Image captions are not alt text; still write alt.
- Light-grey caption text is a common failure, so keep it at 4.5:1 or above.

**Audio.** Sound (as on Slosh Seltzer per [Jack Christian](https://jackchristian.com.au/blog/my-top-5-maximalist-websites/)) must be off by default and user-initiated (WCAG 1.4.2 Audio Control).

**Performance (synthesized).**
- Use AVIF or WebP with `srcset`/`sizes`, and `loading="lazy"` for everything except the LCP image, which gets `fetchpriority="high"`.
- Cut-out PNGs are heavy, so use WebP or AVIF with alpha.
- Texture as one tiled image or a CSS gradient, not per-section JPEGs.
- Fonts:
  - Self-host WOFF2 subsets with `font-display: swap`.
  - Preload one or two critical faces only.
  - Prefer variable fonts so one file covers several weights.
  - Maximalist pages with four families should cap total font payload at about 150–200 KB.
- Limit simultaneous `mix-blend-mode`, `filter` and `backdrop-filter` layers, since each can force extra compositing. Use `will-change` sparingly and only during animation.
- Animate only `transform` and `opacity` to protect INP and CLS. Reserve image space with `aspect-ratio` to avoid CLS in overlapping grids.

### Gaps
- I found no source that audits real collage or maximalist sites with WCAG tooling (for example axe or Lighthouse scores). Including such an audit would strengthen the catalog.

---

## 9. Best-fit brands/industries, poor fits, anti-patterns

### Takeaway
Editorial fits content-rich, premium or story-led brands. Collage fits personal, crafty, youth, food and drink, and music brands. Maximalism fits brands whose personality is the product (CPG, entertainment, Gen-Z fashion, events). All three are poor fits for trust-critical, task-heavy UIs such as banking dashboards, healthcare portals and complex SaaS apps, unless confined to marketing pages.

### Cited Findings
- Scrapbook suits fashion and beauty, creative agencies, artists and musicians, DIY brands, food and beverage, retro brands, and maximalist brands — [Alpha Efficiency](https://alphaefficiency.com/scrapbook-style-web-design)
- Scrapbook also fits brands that prioritize authenticity, storytelling and emotional connection: boutiques, personal blogs, event sites — [Medium](https://shariqkhan74.medium.com/scrapbook-layering-in-website-design-trends-techniques-and-best-practices-18f19b5a3bcd)
- Collage suits lifestyle brands and personal portfolios that want a playful, individual feel — [Figma](https://www.figma.com/resource-library/web-design-trends/)
- Maximalism "isn't for every audience" and is polarizing; reactions range from love to hatred — [Webflow](https://webflow.com/blog/maximalism-web-design)
- Anti-design suits edgy fashion brands, experimental agencies and creative portfolios. Figma advises trying it in a separate exploration so the core design system stays intact — [Figma](https://www.figma.com/resource-library/web-design-trends/)
- Collage "controlled chaos" works "provided the infrastructure stays calm" — [KOTA](https://kota.co.uk/blog/branding-inspiration-brand-design-trends-for-2026)
- Unverified claim: editorial ecommerce homepages had 23% lower add-to-cart rates than product-first pages (attributed to Baymard 2025, no link provided) — [Pravin Kumar](https://www.pravinkumar.co/blog/editorial-layouts-replace-hero-sections-webflow-2026)
- Maximalist brand examples by sector: an experiential art venue (Meow Wolf), candy (BEHAVE), Gen-Z vintage fashion (Vintageria), restaurants (Curry Cafe, Dino's Tomato Pie), photography (Mack and Pouya) — [Webflow](https://webflow.com/blog/maximalism-web-design)
- Pest control (Pest Stop Boys) and seltzer (Slosh) — [Jack Christian](https://jackchristian.com.au/blog/my-top-5-maximalist-websites/)
- Beverage, consumer tech, heritage fashion, soft drinks, edtech and footwear (Liquid Death, Nothing, Burberry, Pepsi, Duolingo, Crocs) — [Envato](https://author.envato.com/hub/trend-deep-dive-brand-maximalism/)

### Inferences (synthesized fit matrix)

| Style | Best fits | Use carefully | Poor fits |
|---|---|---|---|
| Editorial | Publishers, journals, fashion/beauty, hospitality, architecture, galleries, premium DTC with stories, consultancies with thought leadership, nonprofits | Ecommerce homepages (keep products above the fold or add a product rail) | Utility apps, price-led discount retail |
| Collage | Bakeries/cafés, craft and handmade goods (for example, a handmade bag brand), kids/family, music and events, bars, zines, illustrators, Gen-Z beauty, NA beverages, campaigns | Agencies and portfolios (can look unpolished) | Finance, legal, medical, B2B SaaS, government |
| Maximalist | CPG snacks and drinks, entertainment venues, festivals, gaming, streetwear, toys, nightlife, creative studios, music | Restaurants (menu and hours must stay plain and fast) | Healthcare, finance, legal, enterprise, accessibility-critical public services, older audiences |

**Anti-patterns (synthesized):**
- Decoration that hides the CTA or price.
- Every element rotated, which makes everything equally loud and loses hierarchy.
- Body text on texture or pattern.
- More than four typefaces.
- Fake "magazine" layouts with lorem-like filler and no real editorial content.
- Pull quotes repeating the previous paragraph verbatim.
- Editorial ecommerce that hides products below long stories.
- Marquees without a pause control.
- Scroll-jacking or diagonal scroll.
- Auto-playing audio.
- Cut-out images without alpha optimisation (multi-MB PNGs).
- Collage made of stock clip-art stickers that are not brand-specific.
- Maximalism without a consistent system: no tokens, random colours per section.
- Ignoring mobile, so the desktop collage is simply scaled down into illegibility.

### Gaps
- I found no verified conversion or performance studies comparing these styles. The Pravin Kumar statistics are unsourced.

---

## 10. Real example websites (2023–2026) and authoritative articles

### Takeaway
Current example sites are easy to name for editorial and maximalism. Collage examples on live, recent sites are thin in fetchable sources. Several sources only point to Dribbble shots or old (2013, 2017) sites. Every URL below should be spot-checked live before it goes into the catalog. I did not visit any of them this session.

### Cited Findings

**Editorial / magazine** (listed in a roundup published Nov 2024 and updated Jul 2025)
- The New Yorker: https://www.newyorker.com (minimalist, classic, easy to navigate)
- WIRED: https://www.wired.com (modern, colourful, interactive features)
- Exhibition Magazine: https://exhibition-magazine.com (minimalist, high-quality art photography, organized sections)
- Assemble Papers: https://assemblepapers.com.au (clean, simple, warm eco tones)
- Hunger Magazine: https://hungermag.com (edgy, large visuals)
- Vessel Magazine: https://vessel-magazine.no (elegant, minimalist)
- Scandinavian Mind: https://scandinavianmind.com (crisp, minimalist, neutral tones)
- Rolling Stone: https://www.rollingstone.com (bold typography)

— all from [Really Good Designs](https://reallygooddesigns.com/best-magazine-websites)

- Editorial concepts (Dribbble shots, not live sites): Cole Haan editorial landing page, Undercover, and a magazine-style landing page — [Subframe](https://www.subframe.com/tips/editorial-website-design-examples)

**Collage / scrapbook**
- Collage (collagecrafting.com) by Locomotive, Awwwards SOTD **July 18 2017** (older; black/white; WebGL, PixiJS) — [Awwwards](https://www.awwwards.com/sites/collage)
- Le Moderne restaurant (https://restaurant-lemoderne.fr/), Brokedesign (https://www.brokedesign.com) and Helmy Bern (https://www.snowboard-zezula.cz/bern) appear in Designmodo's scrapbook list. The list dates from 2013 with a 2026 update; the age of individual entries is unclear — [Designmodo](https://designmodo.com/scrapbook-website-design/)
- Ghia (non-alcoholic aperitif) collage-like website layout, cited via a Dribbble shot: https://dribbble.com/shots/26375242-Ghia-Colorful-Bold-Non-Alcoholic-Beverage-Company-Website-Page — [KOTA](https://kota.co.uk/blog/branding-inspiration-brand-design-trends-for-2026)
- Tyler Upchurch (https://www.tylerupchurch.com/): ripped textures, jagged layers and fractured photos in illustration; a portfolio site — [KOTA](https://kota.co.uk/blog/branding-inspiration-brand-design-trends-for-2026)
- La Palatine is cited as blending real photos with digital elements, but no URL was given and a search did not find it — [Figma](https://www.figma.com/resource-library/web-design-trends/)
- Ellen Porteus (https://www.ellenporteus.com): illustrated hero with a butterfly cursor. It sits between collage and maximalism — [Jack Christian](https://jackchristian.com.au/blog/my-top-5-maximalist-websites/)

**Maximalist**
- Meow Wolf: https://meowwolf.com — [Webflow](https://webflow.com/blog/maximalism-web-design)
- BEHAVE candy: https://www.eatbehave.com — [Webflow](https://webflow.com/blog/maximalism-web-design)
- Pablito Planeta: https://www.pablitoplaneta.com — [Webflow](https://webflow.com/blog/maximalism-web-design)
- Y-N10: https://y-n10.com — [Webflow](https://webflow.com/blog/maximalism-web-design)
- Vintageria: https://www.vintageria.it — [Webflow](https://webflow.com/blog/maximalism-web-design)
- Dino's Tomato Pie: https://www.dinostomatopie.com — [Webflow](https://webflow.com/blog/maximalism-web-design)
- Curry Cafe: http://curry.cafe — [Webflow](https://webflow.com/blog/maximalism-web-design)
- The Geek Designer: https://thegeekdesigner.com — [Webflow](https://webflow.com/blog/maximalism-web-design)
- Choreus: https://www.choreus.co; Pest Stop Boys: https://peststopboys.co.uk; Slosh Seltzer: https://sloshseltzer.com — [Jack Christian](https://jackchristian.com.au/blog/my-top-5-maximalist-websites/)
- Liquid Death: https://liquiddeath.com (named as maximalism example) — [Figma](https://www.figma.com/resource-library/web-design-trends/); [Envato](https://author.envato.com/hub/trend-deep-dive-brand-maximalism/)

**Authoritative articles and guides**
- Rachel Andrew, "Editorial Design Patterns With CSS Grid And Named Columns", Smashing Magazine, 2019 (technique still valid; subgrid support statement outdated) — https://www.smashingmagazine.com/2019/10/editorial-design-patterns-css-grid-subgrid-naming/
- Webflow, "Maximalism: How designers are turning up the volume of their work" (updated Oct 2025) — https://webflow.com/blog/maximalism-web-design
- Figma, "Top Web Design Trends for 2026" (likely late 2025) — https://www.figma.com/resource-library/web-design-trends/
- KOTA, "Branding inspiration: design trends for 2026" (Nov 2025, mod. Oct 2026) — https://kota.co.uk/blog/branding-inspiration-brand-design-trends-for-2026
- Envato, "Trend Deep Dive: Brand Maximalism" (Oct 2025) — https://author.envato.com/hub/trend-deep-dive-brand-maximalism/
- Designmodo, "Crafty Multilayerness – Scrapbook Style in Web Design" (updated Feb 2026) — https://designmodo.com/scrapbook-website-design/
- Creative Bloq, "Rebirth of the zine" (cited by KOTA; not fetched) — https://www.creativebloq.com/features/rebirth-of-the-zine
- It's Nice That on W+K Amsterdam × Foam collage graphics (cited by KOTA; not fetched) — https://www.itsnicethat.com/articles/wieden-and-kennedy-amsterdam-foam-graphic-design-project-241125
- Suzanne Aitchison, "3 experiments with CSS paper effects", dev.to, 2021 — https://dev.to/s_aitchison/3-experiments-with-css-paper-effects-2o56
- FreeFrontend, editorial CSS grid magazine layout (2026) — https://freefrontend.com/code/editorial-css-grid-magazine-layout-2026-03-31/

### Inferences
- Candidate examples from my background knowledge, **not verified this session**. Check each before including:
  - Editorial: The Pudding (pudding.cool), Kinfolk (kinfolk.com), Apartamento (apartamentomagazine.com), It's Nice That (itsnicethat.com), Bloomberg Businessweek features, Aesop's The Fabulist.
  - Maximalist or playful CPG: Fishwife (eatfishwife.com), Omsom, Graza, Poolsuite (poolsuite.net), MSCHF (mschf.com).
  - Collage: Spotify Wrapped campaign pages and Ghia's live site (ghia.com).
- The editorial example list from Really Good Designs is largely large media brands. For a catalog aimed at SMB brands, smaller indie-magazine examples (Exhibition, Assemble Papers, Vessel, Scandinavian Mind) are closer analogues.

### Gaps
- **Collage:** I could not verify four to six *current, live (2023–2026)* collage or scrapbook websites from fetchable sources. Results pointed to Dribbble shots, a 2017 Awwwards SOTD, and a 2013-origin Designmodo list. Recommended follow-up: browse Awwwards, Godly and Siteinspire tag pages ("collage", "scrapbook", "paper", "zine") in a real browser.
- Typewolf, Fonts In Use, Godly and Siteinspire pages were not retrieved, because search did not surface them for these queries.
- I visited none of the example sites, so their current design state (redesigns since publication) is unknown.
