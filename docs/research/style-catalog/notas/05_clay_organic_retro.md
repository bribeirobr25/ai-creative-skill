# Clay / Organic / Retro — three web design styles for a website-generation catalogue

Scope: (1) Claymorphism / soft 3D / "puffy" UI, (2) Organic / natural (earthy, handmade, wellness), (3) Retro / vintage (60s–70s, mid-century, 80s/synthwave, 90s web).
Target: static HTML/CSS/vanilla JS, self-hosted OFL fonts, WCAG 2.2 AA, prefers-reduced-motion.
Labelling: anything under "Inferences" is a synthesized recommendation (my own build guidance or calculation), not a sourced fact. Contrast ratios marked "computed" were calculated in this session with the WCAG 2.x relative-luminance formula.

Source-quality note: the most structured, consistent per-style source found was the daisyUI "UI design trends" catalogue (trends.daisyui.com). It is a component-library vendor's reference, not an academic source, but each page cites museum/encyclopaedic sources for origins. The setproduct.com claymorphism guide (Jun 2026) is the most numeric clay source; one of its contrast claims is wrong (see Q4). Several search hits were spam/scraped domains (e.g. oldstore.motogp.com, carmi.illinois.gov, app.parkhill.com) and were not used.

---

## Q1. Definition, origin and signature traits (per style)

### Takeaway
Claymorphism is a 2021-era Dribbble/Behance UI label for inflated, pastel, large-radius components built from one outer shadow plus two inner shadows. "Organic" is an umbrella over blob/biomorphic UI, biophilic design, wabi-sabi and cottagecore, all built on irregular curves, earthy palettes, texture and slow motion. "Retro" is not one style but a family of era revivals: 60s–70s psychedelic/groovy, mid-century modern, 80s synthwave/Memphis and 90s Web 1.0, each with its own palette and type.

### Cited Findings

**Claymorphism**
- Michal Malewicz published "Claymorphism in user interfaces" on UX Collective on 20 Dec 2021. He framed it as a trend "stepping outside of the UI world and into the art space" and a way to satisfy the desire for "an illusion of depth on our flat screens". He argued neumorphism "didn't really take off" mainly because it looked dull, not because of accessibility. — [UX Collective / Malewicz](https://uxdesign.cc/claymorphism-in-user-interfaces-1757fabaa377)
- daisyUI dates it to around 2021 to the early 2020s, from UI and 3D-illustration communities. The style is "commonly attributed" to Michał Malewicz, but a single origin is hard to prove. It calls it "a contemporary interface label, not a historic art movement". — [daisyUI: Claymorphism](https://trends.daisyui.com/trend/claymorphism/)
- OpenReplay (Oct 2022) says the style emerged on Dribbble and Behance in 2022, gives Malewicz much of the credit for its popularity and links it to Web3 UI. — [OpenReplay](https://blog.openreplay.com/implementing-claymorphism-with-css/) *(Note: dates differ slightly from Malewicz's Dec 2021 article; the term was in circulation by late 2021.)*
- OpenReplay's traits: pale, pastel and vibrant hues; large rounded corners; an outer shadow combined with a double inner shadow; a soft, 3D, inflated, "fluffy" look. — [OpenReplay](https://blog.openreplay.com/implementing-claymorphism-with-css/)
- LogRocket (May 2024) calls it a "reimagined neomorphism". Its visual references are stuffed toys, clouds, balloons, pool toys and claymation (Wallace & Gromit). Traits: tactile, clay-like rounded corners; discrete layered surfaces with outer shadows for separation and inner shadows for thick edges; buttons that look like solid blocks; vivid colour cues on interactive elements; restrained typography; clay-style illustrations and avatars. — [LogRocket](https://blog.logrocket.com/ux-design/what-is-claymorphism-web-design/)
- daisyUI traits: inflated components, oversized radii, chunky icons, toy-like depth. Layout is floating, centred clusters of a few chunky modules with low-to-medium density and short copy. Motion is buoyant lifts, slight squash-and-stretch and a gentle bounce on success. — [daisyUI: Claymorphism](https://trends.daisyui.com/trend/claymorphism/)

**Organic / natural**
- daisyUI defines "Organic / Blob Design" as fluid silhouettes, asymmetric curves, soft blobs, rounded containers and freeform layouts that replace rigid geometry. It descends from early-20th-century biomorphic art and was revived in the late 2010s, when vector tools and flexible layouts made irregular shapes easy to use. — [daisyUI: Organic/Blob](https://trends.daisyui.com/trend/organic-blob-design/) (citing [Tate, "Biomorphic"](https://www.tate.org.uk/art/art-terms/b/biomorphic))
- Biophilic design uses "organic shapes, botanical imagery, earthy colors, natural textures, and gentle motion". Its conceptual roots run from the 1960s to the 1980s: Fromm used "biophilia", E. O. Wilson's *Biophilia* (1984) popularised it, and Kellert developed the design framework. The source warns that screens "cannot reproduce all the spatial and sensory effects studied in architecture". — [daisyUI: Biophilic](https://trends.daisyui.com/trend/biophilic-design/)
- Wabi-sabi UI is built on asymmetry, weathered texture, muted earth tones and visible imperfection. It comes from Japanese tea culture (15th–16th c., Sen no Rikyū). The source notes that commercial "wabi-sabi" often shrinks to "a palette of beige ceramics". — [daisyUI: Wabi-Sabi](https://trends.daisyui.com/trend/wabi-sabi/)
- daisyUI groups 10 styles as "Organic and atmospheric UI": Organic/Blob, Biophilic, Wabi-Sabi, Cottagecore (pastoral, florals, handmade textures, gentle serif), Elvish, Solarpunk, Surf Crush, Frutiger Aero, Seapunk and Global Village Coffeehouse (earth tones, rough borders, woodcut-like suns/moons/spirals). — [daisyUI: Organic & atmospheric](https://trends.daisyui.com/organic-atmospheric-ui/)
- Its handmade/craft neighbours are Hand-Drawn UI, Collage, Scrapbook/Sticker UI and Punk/Zine. — [daisyUI index](https://trends.daisyui.com/)

**Retro / vintage**
- HubSpot (updated 23 Jun 2025) defines retro sites as having a "distinctly old-fashioned look and feel" through type, colour or graphics. Common devices are vintage and letterpress type, handwritten flourishes, period palettes (golds, greens, mustards) or 70s/80s brights, pixel graphics, halftone, collage/scrapbook, print-derived layouts (magazine, newspaper, zine, ledger) and paper or torn-paper textures. — [HubSpot](https://blog.hubspot.com/website/retro-websites)
- Wix Studio (15 Oct 2025) uses "newstalgia" for muted tones, faded imagery, TV static/VCR references and magazine-style type. It also lists 80s pixel art and monospaced pixel fonts; 2000s kitsch (GIFs, marquees, 3D bubble lettering); halftone/archival photos; and vibrant geometric retro. FAQ traits include grain and CRT/scanline textures. — [Wix Studio](https://www.wix.com/studio/blog/retro-web-design)
- Psychedelic (mid-1960s to early 1970s, San Francisco's Haight-Ashbury/Fillmore posters and London): warped lettering, kaleidoscopic patterns, saturated colour, liquid forms, dense ornament. — [daisyUI: Psychedelic](https://trends.daisyui.com/trend/psychedelic-design/)
- Mid-century modern (mid-1940s to late 1960s, postwar Europe/US, Nordic and Californian centres): clean geometry, warm muted colours, humanist illustration, tapered forms, optimistic motifs. The label was popularised later by Cara Greenberg's 1984 book. — [daisyUI: Mid-Century Modern](https://trends.daisyui.com/trend/mid-century-modern/)
- Synthwave/Outrun (mid-2000s to present): an internet-era reconstruction of 1980s film, game and TV aesthetics, not an original 80s genre. "Outrun" refers to Sega's 1986 game. Traits: neon horizon, wireframe grid, chrome lettering, sports-car silhouettes, night-drive glow. — [daisyUI: Synthwave](https://trends.daisyui.com/trend/synthwave-outrun/)
- Web 1.0/Webcore (1991 to late 1990s; "Webcore" is a later nostalgia label): browser-default type, blue underlined links, tiled backgrounds, beveled buttons, animated GIFs, badges, visitor counters, a hand-assembled look. — [daisyUI: Web 1.0](https://trends.daisyui.com/trend/web-1-0-webcore/)
- Other retro branches catalogued: Memphis (1980s), Vaporwave, Jet Age Optimism, American Kitsch, Retro-Futurism, Halftone/Comic, Y2K, Gen-X Soft Club. — [daisyUI index](https://trends.daisyui.com/)

### Inferences
- **Signature traits for a generator (synthesized):**
  - *Clay:* (1) inflated surfaces from 3–4 stacked shadows with inset highlight top-left and inset shade bottom-right; (2) radii of 16–32px, capsules at 999px; (3) 2–3 pastel families on a tinted off-white page; (4) rounded heavy sans; (5) chunky 3D or clay illustrations and icons; (6) springy press and hover motion.
  - *Organic:* (1) irregular blob and pebble shapes with wavy section edges; (2) earthy or botanical palette on cream or paper; (3) grain or paper texture; (4) soft serif or humanist sans with relaxed leading; (5) real nature, material and hand-made photography; (6) slow fades and drifts.
  - *Retro:* (1) an era-specific palette; (2) a period display face paired with a plain reading face; (3) print artefacts such as grain, halftone and misregistration; (4) graphic devices like sunbursts, stripes, badges and hard offset shadows; (5) print-derived or period-UI layouts; (6) controlled nostalgia in motion (marquee, neon flicker), always optional.
- Treat "retro" as a parent style with era presets, and "organic" as a parent with mood presets. Don't model either as one style, because palette, type and shape rules conflict across the sub-variants.

### Gaps
- No primary source pins who first coined "claymorphism" (Malewicz is "commonly attributed"). The full body of Malewicz's article (with its own recipe) was paywalled/truncated in the fetch.
- No authoritative trend report (e.g. a Dribbble or Awwwards annual report) with adoption numbers was found for any of the three styles.

---

## Q2. Recognised sub-variants and when to use each

### Takeaway
Clay splits into clay *UI* (shadow-built components) and *3D-illustration-led* clay (rendered Spline/Blender assets on otherwise flat UI). Organic splits into wellness/biophilic, earthy craft (wabi-sabi/handmade), botanical/cottagecore and playful blob. Retro splits by era: 60s–70s groovy/psychedelic, mid-century modern, 80s synthwave/Memphis, 90s Web 1.0, plus a cross-era "print newstalgia" (letterpress/zine/halftone).

### Cited Findings
- **Clay, UI-led vs illustration-led:** setproduct lists "3D and illustrated landing pages (Spline, Blender)" as a separate use case from component-level clay (buttons, cards, chips, toggles, inset inputs, floating pill nav, squircle app-icon tiles). — [setproduct](https://preview.setproduct.com/blog/claymorphism-design-guide)
- LogRocket names clay illustrations and avatars (e.g. NFT avatars by Amrit Pal Singh) as part of the style. Common uses: CTA buttons, chat apps, app icons, avatars. — [LogRocket](https://blog.logrocket.com/ux-design/what-is-claymorphism-web-design/)
- Adjacent soft-3D styles: Kawaii UI, Frutiger Aero (glossy blue/green, water, bubbles), Organic/Blob. — [daisyUI: Claymorphism](https://trends.daisyui.com/trend/claymorphism/)
- **Organic variants:**
  - Biophilic: leaf/moss/clay/bark/sky/mineral palette; wellness, sustainability, hospitality, healthcare. — [daisyUI: Biophilic](https://trends.daisyui.com/trend/biophilic-design/)
  - Wabi-sabi: radius 0–0.25rem, irregular edges; craft, hospitality, food, slow living, artisan commerce. — [daisyUI: Wabi-Sabi](https://trends.daisyui.com/trend/wabi-sabi/)
  - Organic/Blob: radius 1–2rem; wellness, creative tools, lifestyle, onboarding, approachable tech. — [daisyUI: Organic/Blob](https://trends.daisyui.com/trend/organic-blob-design/)
  - Cottagecore: florals, handmade textures, gentle serif, rural nostalgia. — [daisyUI: Organic & atmospheric](https://trends.daisyui.com/organic-atmospheric-ui/)
- **Retro variants:**
  - Psychedelic: music, festivals, fashion, entertainment, experimental campaigns. — [daisyUI: Psychedelic](https://trends.daisyui.com/trend/psychedelic-design/)
  - Mid-century: architecture, furniture, lifestyle, editorial, hospitality, design-led commerce. — [daisyUI: MCM](https://trends.daisyui.com/trend/mid-century-modern/)
  - Synthwave: games, music, automotive, nightlife, streaming. — [daisyUI: Synthwave](https://trends.daisyui.com/trend/synthwave-outrun/)
  - Web 1.0: personal sites, art projects, developer communities, games. — [daisyUI: Web 1.0](https://trends.daisyui.com/trend/web-1-0-webcore/)
- Print/editorial retro examples: Ikony (newspaper/zine grid), Old Iron Press (letterpress, red/black/white), Dunderville (stamped logo, paper texture), Mondo (oversized halftone, torn paper). 70s soul/funk example: Paak House (brights on black, long shadows, thick outlines). — [HubSpot](https://blog.hubspot.com/website/retro-websites)

### Inferences
Decision table (synthesized):

| Style | Sub-variant | Use when | Radius | Density |
|---|---|---|---|---|
| Clay | **Clay UI** | App or SaaS landing, onboarding, kids/edu, friendly fintech | 16–32px | Low–med |
| Clay | **3D-illustration-led** | Brand needs personality but content is denser; UI stays flat or lightly soft, hero/feature art carries the clay | 12–20px | Med |
| Organic | **Wellness / biophilic** | Spa, yoga, therapy, supplements, clean beauty | 12–24px | Low |
| Organic | **Earthy craft / wabi-sabi** | Ceramics, coffee, bakery, slow fashion, artisan shop | 0–4px, irregular masks | Low |
| Organic | **Botanical / cottagecore** | Florist, tea, garden, handmade bags/cosmetics, small-batch food | 8–16px + arches | Low–med |
| Organic | **Playful blob** | Approachable tech/SaaS, creative tools | 24px + blobs | Med |
| Retro | **70s groovy / psychedelic** | Music, festival, bar, vintage clothing, cafés | 16–32px, pills | Low–med |
| Retro | **Mid-century modern** | Furniture, architecture, hotel, design shop, editorial | 4–16px | Med |
| Retro | **80s synthwave** | Gaming, music, nightlife, events (dark theme) | 4–16px | Low–med |
| Retro | **90s Web 1.0** | Personal/portfolio, indie dev, art, games; ironic/nostalgic brands | 0–4px | Med–high |
| Retro | **Print newstalgia** (letterpress/zine/halftone) | Print shops, bookshops, magazines, craft brewers | 0–8px | Med |

### Gaps
- No source formally names "clay UI vs 3D-illustration-led" as industry categories. The split is my synthesis from setproduct's use cases and LogRocket's illustration examples.

---

## Q3. Most used layouts and page patterns, including mobile

### Takeaway
Clay uses centred floating hero clusters, bento-style card groups, pill nav and big rounded CTAs at low density. Organic uses open, path-like flows with asymmetric overlaps, blob-masked images, wavy section transitions and generous whitespace on a single reading spine. Retro borrows print grids (magazine, zine, newspaper, ledger) or period UI (cockpit horizon for synthwave, table layout and side nav for 90s web).

### Cited Findings
- Clay layout: floating, centred clusters of a few chunky modules with space around each, low-to-medium density, short copy. — [daisyUI: Claymorphism](https://trends.daisyui.com/trend/claymorphism/)
- Clay components: floating pill or top-rounded bottom nav; card padding 24–28; minimum gap between clay siblings 16; tap targets ≥48×48; buttons 52–56px tall; 8pt spacing scale 4/8/12/16/24/32/48. Elevation: L0 flat, L1 resting card, L2 floating sheet (12px offset, 32px blur). Don't stack clay three or more levels deep. — [setproduct](https://preview.setproduct.com/blog/claymorphism-design-guide)
- Organic/Blob layout: sections follow a loose, flowing path with asymmetric overlaps while text and controls keep "one dependable reading spine". Keep type on calm regions, not wrapped around curves, and avoid long text inside narrow blob extremities. — [daisyUI: Organic/Blob](https://trends.daisyui.com/trend/organic-blob-design/)
- Biophilic layout: open flow inspired by paths and clearings, alternating broad natural imagery with calm content zones and soft section transitions. — [daisyUI: Biophilic](https://trends.daisyui.com/trend/biophilic-design/)
- Wabi-sabi layout: quiet asymmetry, irregular margins, visible pauses, one crafted object or passage per space. — [daisyUI: Wabi-Sabi](https://trends.daisyui.com/trend/wabi-sabi/)
- Mid-century layout: functional modular blocks with relaxed asymmetry, mixing clean product grids with open illustrated or photographic spaces. — [daisyUI: MCM](https://trends.daisyui.com/trend/mid-century-modern/)
- Psychedelic layout: radial or spiral composition with a strong centre. Put schedules, prices and controls on calmer solid fields. — [daisyUI: Psychedelic](https://trends.daisyui.com/trend/psychedelic-design/)
- Synthwave layout: cinematic, with a low neon horizon, deep perspective grid and cockpit-like foreground. Keep actions near stable screen edges. — [daisyUI: Synthwave](https://trends.daisyui.com/trend/synthwave-outrun/)
- Web 1.0 layout: visible document flow, table-like framing, persistent side navigation, stacked sections. — [daisyUI: Web 1.0](https://trends.daisyui.com/trend/web-1-0-webcore/)
- Retro sites in practice:
  - KLR (parallax, vintage interiors)
  - Bialetti (animated scrapbook photos)
  - Ikony (zine grid, large type)
  - Harvard Film Archive (ledger-style blog)
  - Bonjour Market (marquee scrolling type)
  - Dunderville / Accord (magazine layout)
  - Bonnie Hong (80s desktop layout, cursor trail)

  — [HubSpot](https://blog.hubspot.com/website/retro-websites)
- Wellness-site patterns: Heights uses a floating cloud animation in the hero; Vitl uses pastel information cards and infographics; Dirtea uses bespoke icons with standout ratings and reviews; Inessa uses a neutral earthy palette with authentic imagery. — [Limely (Feb 2025, upd. Jun 2026)](https://www.limely.co.uk/blog/our-top-10-health-wellness-websites)

### Inferences
Synthesized page blueprints:

- **Clay landing:**
  - Header is a floating pill nav (`position: sticky; top: 12px`) on a tinted page.
  - Hero is a centred H1 (≤8 words), sub-copy, then a primary coral button plus a secondary lavender one. Below that, a 3D/clay hero object, or 3 floating cards slightly rotated (±3°).
  - Then a bento grid of 4–6 pastel cards (`grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 24px`).
  - Then pricing as 3 clay cards with the middle one raised to L2.
  - Then FAQ accordions as inset "wells", then a big rounded CTA band.
  - Mobile: single column, cards full-width, bottom pill nav optional, keep 16px gutters.
- **Clay product grid:** square pastel tiles (radius 28px) with the product cut-out centred, name and price below, a capsule "Add" button, and a soft colour per category.
- **Organic landing:**
  - Hero is full-bleed nature/material photo, or a split layout (text left, blob-masked image right overlapping the next section).
  - Then a wavy SVG divider into a cream section with a 3-up feature row (icons hand-drawn or line).
  - Then an ingredient/process story as alternating image–text rows with arch- or pebble-masked images, then testimonials on a sand panel.
  - Footer has a torn or wavy top edge.
  - Section rhythm is generous: `padding-block: clamp(4rem, 10vw, 8rem)`.
  - Mobile: blobs scale down or hide (`display:none` below 480px for decorative ones), images become full-width with rounded tops; never place text inside blob extremities.
- **Organic product grid:** 2–4 columns, off-white cards with no shadow (or a 1px warm border), arch-top image mask, serif product name, muted price.
- **Retro 70s:** centred hero with a sunburst or rainbow-stripe background, groovy display headline (with a hard offset shadow), circular "badge" stickers, stripe-banded section separators, menu/price lists on solid cream panels.
- **Mid-century:** a 12-column modular grid with colour-field blocks, geometric illustration, a restrained sans and product grid.
- **Synthwave:** dark full-viewport hero with a perspective grid floor and sun disc, neon headline, content on solid dark panels.
- **90s web:** a two-column table-like layout (left nav 180–200px), beveled buttons, `<marquee>`-style CSS ticker, guestbook/badge footer.
- Every retro layout should collapse to a single column on mobile. Synthwave grid floors and sunbursts should become static backgrounds there.

### Gaps
- No source gave measured data (e.g. heat-maps or conversion) comparing these layouts. All blueprint values above are synthesized.

---

## Q4. Typography and colour (families, OFL options, scale, palettes, contrast)

### Takeaway
Clay uses rounded sans (Fredoka, Nunito, Quicksand, Baloo 2) at weights 500/600/700. Organic uses soft or organic serifs (Fraunces, Lora, Alegreya, Cormorant) with humanist sans. Retro uses an era display face (Shrikhand, Monoton, Orbitron, VT323, Josefin Sans/League Spartan) used large only, paired with a plain reading face. Pastels and earth tones often fail contrast with white text, so dark text on light tints is the safe default (computed ratios below).

### Cited Findings
**Typography**
- *Clay, setproduct:*
  - Families: Quicksand, Nunito, Outfit, Fredoka (rounded sans).
  - Weights: 500 body, 600 labels, 700 headings.
  - Sizes: H1 28–32, H2 22, body 16 minimum, caption 13.
  - Letter-spacing 0.01em on body; line-height 1.4 body / 1.2 headings.
  - Avoid sharp grotesks such as Inter or Helvetica.

  — [setproduct](https://preview.setproduct.com/blog/claymorphism-design-guide)
- *Clay, daisyUI:* Fredoka, Baloo 2, Nunito, M PLUS Rounded 1c, Sniglet. Pair rounded heavy display with a simpler friendly sans and keep headings short. — [daisyUI: Claymorphism](https://trends.daisyui.com/trend/claymorphism/)
- *Organic/Blob:* Fraunces, Gabarito, Varela Round, Quicksand, Urbanist, with "a warm humanist sans-serif or soft display serif, generous leading". — [daisyUI: Organic/Blob](https://trends.daisyui.com/trend/organic-blob-design/)
- *Biophilic:* Fraunces, Lora, Alegreya, Nunito Sans, Cormorant Infant, with open forms, relaxed leading and sentence-case headings. — [daisyUI: Biophilic](https://trends.daisyui.com/trend/biophilic-design/)
- *Wabi-sabi:* Shippori Mincho, Zen Old Mincho, Sawarabi Mincho, Yuji Syuku, Noto Serif JP, set at modest scale. — [daisyUI: Wabi-Sabi](https://trends.daisyui.com/trend/wabi-sabi/)
- *Psychedelic/70s:* Shrikhand, Fascinate, Modak, Monoton, Yatra One, "only at large sizes", paired with a plain reading face. — [daisyUI: Psychedelic](https://trends.daisyui.com/trend/psychedelic-design/)
- *Mid-century:* Josefin Sans, Libre Franklin, Fira Sans, League Spartan, Bitter (humanist sans with a restrained slab/serif). — [daisyUI: MCM](https://trends.daisyui.com/trend/mid-century-modern/)
- *Synthwave:* Orbitron, Audiowide, Monoton, Russo One, Bruno Ace SC; italic techno or chrome display for titles, condensed sans or mono for controls. — [daisyUI: Synthwave](https://trends.daisyui.com/trend/synthwave-outrun/)
- *Web 1.0:* Tinos, Arimo, Cousine, Comic Neue, VT323; browser-default serif, sans or mono, with decorative fonts limited to banners and logos. — [daisyUI: Web 1.0](https://trends.daisyui.com/trend/web-1-0-webcore/)
- *70s commercial display faces* (mostly paid or marketplace): Frunch, The Sooky 70s, Popsmile, Sugar Peachy, Retrozoid, Novecento Slab Rough. Traits: bold, groovy, psychedelic, scripts, rounded edges, outline usage, warm brights. — [Fabrik Brands](https://fabrikbrands.com/best-70s-fonts-for-retro-design/) (licences not stated; not suitable for an OFL-only pipeline without checking)

**Colour**
- *Clay palette, setproduct:*
  - App background #F7F5FB; raised sheet #FFFFFF.
  - Surfaces: lavender #B8A6FF, sky #9EC9F0, mint #7DD4A8, peach #FFB59E, pink #F5B8D0, lemon #F5D77A.
  - Primary action coral #FF7A6B.
  - Text #2E2A3F (strong) and #6B6580 (muted).
  - Shadow hue = surface colour darkened about 15%, never grey. Avoid a pure #FFF page background.

  — [setproduct](https://preview.setproduct.com/blog/claymorphism-design-guide)
- *Clay palette, daisyUI:* 2–3 soft pastel families with warm shaded sides and dark readable text, on creamy tinted bases. — [daisyUI: Claymorphism](https://trends.daisyui.com/trend/claymorphism/)
- *Organic palettes:*
  - Blob: botanical, fruit or mineral tones in soft pairings on cream / pale mineral / tinted earth. — [daisyUI: Organic/Blob](https://trends.daisyui.com/trend/organic-blob-design/)
  - Biophilic: leaf, moss, clay, bark, sky, mineral. — [daisyUI: Biophilic](https://trends.daisyui.com/trend/biophilic-design/)
  - Wabi-sabi: weathered clay, ash, moss, tea, linen, charcoal, oxidized metal, "no polished, high-saturation accents". — [daisyUI: Wabi-Sabi](https://trends.daisyui.com/trend/wabi-sabi/)
- *Retro palettes:*
  - Mid-century: mustard, olive, burnt orange, teal, walnut, warm cream. — [daisyUI: MCM](https://trends.daisyui.com/trend/mid-century-modern/)
  - Psychedelic: saturated complementary near-neon hues balanced with dark pockets (deep purple, violet-black). — [daisyUI: Psychedelic](https://trends.daisyui.com/trend/psychedelic-design/)
  - Synthwave: midnight navy, black, electric magenta, cyan, violet, sunset orange, chrome white. — [daisyUI: Synthwave](https://trends.daisyui.com/trend/synthwave-outrun/)
  - Web 1.0: browser-safe colours, blue links, purple visited links, white/grey/silver. — [daisyUI: Web 1.0](https://trends.daisyui.com/trend/web-1-0-webcore/)
  - In practice: mustard/green (KLR), peach on maroon (Bialetti), gold/black/red (Heritage Type), red/black/white letterpress (Old Iron Press). — [HubSpot](https://blog.hubspot.com/website/retro-websites)
- **Contradiction:** setproduct says white text on coral #FF7A6B meets "at least 4.5". The computed ratio is **2.55:1, which fails AA**. Dark text #2E2A3F on #FF7A6B is 5.43:1 and passes. — claim from [setproduct](https://preview.setproduct.com/blog/claymorphism-design-guide); ratio computed in this session.

### Inferences
**Recommended OFL type pairings** (synthesized; all are Google Fonts families, which are distributed under OFL or Apache; verify each licence file when self-hosting):

| Variant | Display | Text | Scale (synthesized) |
|---|---|---|---|
| Clay UI | Fredoka 600–700 or Baloo 2 800 | Nunito 400–600 | `clamp(2.25rem, 5vw + 1rem, 4rem)` H1; body 1rem–1.125rem; lh 1.5 |
| Wellness | Fraunces (SOFT/WONK axes, opsz) 400–600 | Nunito Sans / Lora 400 | H1 `clamp(2.5rem, 6vw, 5rem)` weight 400–500; lh 1.6–1.7 |
| Earthy craft | Cormorant / Young Serif / Shippori Mincho | Alegreya Sans / Lora | modest H1 ≤3.5rem; generous letter-spacing on small caps labels 0.08em |
| Botanical | Fraunces italic / Cormorant italic | Lora | italic accents for one word per headline |
| 70s groovy | Shrikhand / Modak / Righteous | DM Sans / Work Sans | H1 4–7rem, tight lh 0.95–1.05; display only ≥32px |
| Mid-century | League Spartan / Josefin Sans (caps, tracking 0.1em) | Libre Franklin / Bitter | H1 3–5rem |
| Synthwave | Monoton / Orbitron / Audiowide | Space Mono / Rajdhani | neon titles ≥40px only |
| 90s web | Tinos / Comic Neue / VT323 (banners) | Arimo / Tinos 16px | browser-ish 16px body, h1 2em |

**Example hex sets with computed WCAG contrast** (palettes synthesized; ratios computed):

- *Clay (setproduct-based):*
  - Text #2E2A3F on lavender #B8A6FF = 6.54; on mint #7DD4A8 = 7.8; on lemon #F5D77A = 9.8; on page #F7F5FB = 12.78.
  - Muted #6B6580 on #F7F5FB = 5.11.
  - **White on #B8A6FF = 2.11 (fail)**; white on coral = 2.55 (fail). Use dark text on all pastels.
- *Organic wellness/earthy:*
  - Cream #F4EFE6, ink #2B2A26 (12.54), moss #4F6B3A (text on cream 5.24; white on moss 6.01), terracotta #B5563A (on cream 4.21, **large text only**; white on terracotta 4.82), sage #A3B18A (ink on sage 6.3), muted #6E6A5E (on cream 4.72).
- *70s groovy:*
  - Cream #F6E8C9, brown #3B2416 (11.94), orange #E36A2E (on cream **2.72, decorative only**; brown on orange 4.39, **large text only**), mustard #E2A72E (brown on mustard 6.76), rust #A8432A (on cream 4.94; white on rust 6.0), avocado #7A8B3C (cream on avocado 3.1, large/UI only).
- *Mid-century:*
  - Cream #F3EBDD, charcoal #2A2826 (12.4), teal #2F6F73 (on cream 4.87; white on teal 5.77), burnt orange #C8642B (on cream **3.34, large/UI only**), mustard #D9A441 (charcoal on mustard 6.53), walnut #5A3E2B.
- *Synthwave:*
  - Navy #0D0221, text #F5F3FF (18.27), magenta #FF2A6D (on navy 5.54; **white on magenta 3.62, fail** for body), cyan #05D9E8 (on navy 11.55), violet #7700A6, orange #FF8C42.
- *90s web:*
  - #FFFFFF bg, link #0000EE (9.4), visited #551A8B (11.01), silver #C0C0C0 (black on silver 11.54; #0000EE on silver 5.17).
- **Rule of thumb:** saturated mid-tone accents (orange, coral, magenta, terracotta) are for fills, shapes and ≥24px/≥18.66px-bold text, or for backgrounds carrying *dark* text. Body copy should always be the darkest ink on the lightest base. Non-text UI boundaries (buttons, inputs) need ≥3:1 against their surroundings (WCAG 1.4.11). Clay buttons often rely only on shadow for their boundary, so give them a fill colour that is ≥3:1 against the page or add a 2px border.

### Gaps
- Licences were not individually fetched for each Google Fonts family listed. Most are OFL; a few Google-hosted families have historically been Apache 2.0. Verify the LICENSE/OFL.txt shipped with each download.
- No authoritative source (e.g. Typewolf, Fonts In Use) was fetched for retro OFL alternatives to Cooper Black / Recoleta / ITC Avant Garde. Righteous, Young Serif and DM Sans in the table are my suggestions, not sourced.

---

## Q5. Concrete CSS recipes (shadows, blobs, textures, dividers, retro devices)

### Takeaway
Clay is one outer, colour-tinted drop shadow plus a white top-left inset and a darker bottom-right inset, at radius 24–32px. Organic relies on 8-value `border-radius` blobs or SVG paths, SVG wave dividers and an feTurbulence grain overlay. Retro uses conic-gradient sunbursts, repeating-linear-gradient stripes, radial-gradient halftone, hard offset `box-shadow`/`text-shadow` and grain.

### Cited Findings
- **OpenReplay clay recipe** (radius 30px): `background: rgba(165,79,29,.6); box-shadow: inset -0.6em -0.6em 1em rgba(165,79,29,.6), inset 0.4em 0.4em 0.5em rgba(245,230,221,.6), 0.8em 0.8em 2em rgba(165,79,29,.6);` (inset bottom-right darker, inset top-left cream highlight, outset drop). — [OpenReplay](https://blog.openreplay.com/implementing-claymorphism-with-css/)
- **setproduct clay card:**
  - Rest: `box-shadow: 8px 8px 24px rgba(108,76,240,.35), inset -6px -6px 16px rgba(80,50,200,.25), inset 6px 6px 16px rgba(255,255,255,.55);`
  - `:active`: `4px 4px 12px rgba(108,76,240,.3), inset -3px -3px 10px rgba(80,50,200,.3), inset 3px 3px 10px rgba(255,255,255,.4);`
  - 4-layer spec: colored drop 8/8/24 @0.35 (south-east) + white lift −8/−8/24 @0.6 + inset sheen 4/4/8 white @0.5 + inset depth −6/−6/12 @0.30. Light comes from top-left.
  - Inputs: inset only, `inset 3px 3px 8px rgba(H,.2), inset -3px -3px 8px #FFF`.
  - Radii: cards 28 (24–32), buttons 18 (16–20), chips 999, inputs 16, icon tiles 20; floor 16px on interactive elements.

  — [setproduct](https://preview.setproduct.com/blog/claymorphism-design-guide)
- daisyUI tokens:
  - Clay: `--radius-*` 1–2rem, `--depth: 1`. — [daisyUI: Claymorphism](https://trends.daisyui.com/trend/claymorphism/)
  - Blob: 1–2rem. — [daisyUI: Organic/Blob](https://trends.daisyui.com/trend/organic-blob-design/)
  - Biophilic: 0.75–1.5rem and `--noise: 1`. — [daisyUI: Biophilic](https://trends.daisyui.com/trend/biophilic-design/)
  - Wabi-sabi: 0–0.25rem and `--noise: 1`. — [daisyUI: Wabi-Sabi](https://trends.daisyui.com/trend/wabi-sabi/)
  - Mid-century: 0.25–1rem. — [daisyUI: MCM](https://trends.daisyui.com/trend/mid-century-modern/)
  - Psychedelic: 1–2rem. — [daisyUI: Psychedelic](https://trends.daisyui.com/trend/psychedelic-design/)
  - Synthwave: 0.25–1rem, `--depth:1`. — [daisyUI: Synthwave](https://trends.daisyui.com/trend/synthwave-outrun/)
  - Web 1.0: 0–0.25rem, `--depth:1`. — [daisyUI: Web 1.0](https://trends.daisyui.com/trend/web-1-0-webcore/)
- **Grain (CSS-Tricks, Jimmy Chion, Sep 2021):**
  - SVG: `<filter id="noiseFilter"><feTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3" stitchTiles="stitch"/></filter><rect width="100%" height="100%" filter="url(#noiseFilter)"/>`
  - Save it as a separate file and reference it by URL, because referencing by `id` from CSS doesn't work.
  - Layer it as `background: linear-gradient(...), url(noise.svg)` and boost with `filter: contrast(170%) brightness(1000%)`.
  - Blend with `mix-blend-mode: multiply` over a colour, with `isolation: isolate` on the wrapper.
  - Blink and WebKit render `mix-blend-mode` slightly differently; a commenter complained about performance.

  — [CSS-Tricks: Grainy Gradients](https://css-tricks.com/grainy-gradients/)
- Synthwave CSS techniques described (no values): pink-to-purple gradient sky with sun and grid ground; animated vertical stripes; infinite-loop pure-CSS perspective grid; 3D transforms for a highway; perspective neon text; single-div flickering neon. — [Speckyboy (Apr 2026)](https://speckyboy.com/css-javascript-snippets-synthwave/)
- Shape vocabularies:
  - Organic: blobs, pebble cards, soft waves, irregular circular crops. — [daisyUI: Organic/Blob](https://trends.daisyui.com/trend/organic-blob-design/)
  - Biophilic: leaf arcs, pebbles, branch-like dividers. — [daisyUI: Biophilic](https://trends.daisyui.com/trend/biophilic-design/)
  - Mid-century: boomerangs, lozenges, starbursts, tapered legs. — [daisyUI: MCM](https://trends.daisyui.com/trend/mid-century-modern/)
  - Psychedelic: paisleys, spirals, melting contours, wavy borders. — [daisyUI: Psychedelic](https://trends.daisyui.com/trend/psychedelic-design/)
  - Web 1.0: beveled buttons, 1px table borders, `<hr>`, native controls. — [daisyUI: Web 1.0](https://trends.daisyui.com/trend/web-1-0-webcore/)
  - Paak House: long shadows and thick outlines. — [HubSpot](https://blog.hubspot.com/website/retro-websites)

### Inferences
All code below is a synthesized recipe, written against the sourced values above.

**Clay tokens + components**
```css
:root{
  --page:#F7F5FB; --ink:#2E2A3F; --ink-2:#6B6580;
  --lav:#B8A6FF; --mint:#7DD4A8; --peach:#FFB59E; --lemon:#F5D77A; --cta:#FF7A6B;
  --r-card:28px; --r-btn:18px; --r-pill:999px;
}
/* shadow built from the surface hue: set --h per surface (RGB triplet of surface darkened ~15%) */
.clay{
  --h: 108 76 240;
  border-radius:var(--r-card); background:var(--lav); color:var(--ink);
  box-shadow:
    8px 8px 24px rgb(var(--h) / .35),
    -8px -8px 24px rgb(255 255 255 / .6),
    inset 4px 4px 8px rgb(255 255 255 / .5),
    inset -6px -6px 12px rgb(var(--h) / .30);
}
.clay--mint{ background:var(--mint); --h: 60 150 110; }
.clay-btn{
  min-height:54px; padding:0 24px; border:0; border-radius:var(--r-btn);
  background:var(--cta); color:var(--ink); font:600 1rem/1 Nunito, system-ui;
  --h: 200 80 70;
  box-shadow: 6px 6px 16px rgb(var(--h)/.35), inset 3px 3px 6px rgb(255 255 255/.5), inset -4px -4px 8px rgb(var(--h)/.3);
  transition: transform .14s ease, box-shadow .14s ease;
}
.clay-btn:hover{ transform:translateY(-2px); }
.clay-btn:active{ transform:scale(.97);
  box-shadow: 3px 3px 8px rgb(var(--h)/.3), inset 2px 2px 4px rgb(255 255 255/.4), inset -2px -2px 5px rgb(var(--h)/.3); }
.clay-btn:focus-visible{ outline:3px solid var(--ink); outline-offset:3px; }
.clay-input{ border:0; border-radius:16px; background:#EFEAF8; padding:14px 16px;
  box-shadow: inset 3px 3px 8px rgb(108 76 240/.2), inset -3px -3px 8px #fff; }
```
Note: the CTA uses dark ink text, because white on #FF7A6B fails contrast (2.55:1).

**Organic: blobs, masks, waves, grain**
```css
/* 8-value border-radius blob (horizontal / vertical radii) */
.blob{ border-radius: 63% 37% 54% 46% / 55% 48% 52% 45%; aspect-ratio:1; background:#A3B18A; }
/* slow morph — only when motion is allowed */
@media (prefers-reduced-motion: no-preference){
  .blob{ animation: morph 18s ease-in-out infinite alternate; }
  @keyframes morph{ to{ border-radius: 40% 60% 35% 65% / 60% 35% 65% 40%; } }
}
/* arch / pebble image masks */
.arch{ border-radius: 999px 999px 16px 16px; overflow:hidden; }
.pebble{ border-radius: 46% 54% 43% 57% / 52% 44% 56% 48%; overflow:hidden; }
/* SVG path mask for a hand-drawn blob (inline SVG <clipPath id="b" clipPathUnits="objectBoundingBox">) */
.img-blob{ clip-path:url(#b); }
```
```html
<svg width="0" height="0" aria-hidden="true"><clipPath id="b" clipPathUnits="objectBoundingBox">
  <path d="M.83,.17C.95,.3,.98,.52,.9,.7S.62,.97,.42,.95.08,.8.04,.6.1,.2.3,.08.71,.04.83,.17Z"/></clipPath></svg>
<!-- wavy section divider: sits at top of the next section, fill = next section colour -->
<svg class="wave" viewBox="0 0 1440 80" preserveAspectRatio="none" aria-hidden="true">
  <path d="M0,40 C240,80 480,0 720,40 C960,80 1200,10 1440,40 L1440,80 L0,80 Z" fill="#E6D9C3"/></svg>
```
```css
.wave{ display:block; width:100%; height:clamp(40px,6vw,80px); margin-bottom:-1px; }
/* paper grain overlay: noise.svg = CSS-Tricks feTurbulence file (baseFrequency .65–.9, numOctaves 3) */
body{ background:#F4EFE6; }
body::before{ content:""; position:fixed; inset:0; pointer-events:none; z-index:100;
  background:url(/img/noise.svg); opacity:.08; mix-blend-mode:multiply; }
/* hand-drawn underline */
.squiggle{ text-decoration: underline wavy #B5563A; text-underline-offset:.25em; text-decoration-thickness:2px; }
```

**Retro devices**
```css
/* 70s sunburst (rays) */
.sunburst{ background: repeating-conic-gradient(from 0deg at 50% 100%, #E2A72E 0 6deg, #F6E8C9 6deg 12deg); }
/* 70s rainbow stripe band */
.stripes{ background: linear-gradient(#A8432A 0 20%, #E36A2E 0 40%, #E2A72E 0 60%, #7A8B3C 0 80%, #3B2416 0); height:56px; }
/* rounded "racing" stripes around a pill */
.retro-pill{ border-radius:999px; box-shadow: 0 0 0 6px #E2A72E, 0 0 0 12px #E36A2E, 0 0 0 18px #A8432A; }
/* hard offset shadow (sticker / neo-retro) */
.offset{ border:3px solid #3B2416; border-radius:16px; box-shadow: 6px 6px 0 #3B2416; }
.offset:hover{ transform:translate(-2px,-2px); box-shadow: 8px 8px 0 #3B2416; }
/* stacked groovy text shadow (keep the text itself ≥ AA on its bg) */
.groovy{ font-family:Shrikhand, serif; color:#F6E8C9;
  text-shadow: 3px 3px 0 #E36A2E, 6px 6px 0 #E2A72E, 9px 9px 0 #A8432A; }
/* halftone dots */
.halftone{ background: radial-gradient(circle, #3B2416 1.2px, transparent 1.6px) 0 0/8px 8px; opacity:.25; }
/* circular badge: text on a path via SVG <textPath>; rotate slowly only with motion allowed */
/* synthwave grid floor */
.grid-floor{ position:absolute; inset:auto 0 0 0; height:45vh; transform: perspective(300px) rotateX(60deg); transform-origin:bottom;
  background: linear-gradient(#FF2A6D 2px, transparent 2px) 0 0/100% 40px, linear-gradient(90deg,#FF2A6D 2px, transparent 2px) 0 0/40px 100%; }
.sun{ border-radius:50%; background: linear-gradient(#FF8C42, #FF2A6D);
  -webkit-mask: repeating-linear-gradient(to bottom, #000 0 14px, transparent 14px 18px); mask: repeating-linear-gradient(to bottom,#000 0 14px,transparent 14px 18px); }
.neon{ color:#F5F3FF; text-shadow: 0 0 4px #fff, 0 0 12px #FF2A6D, 0 0 24px #FF2A6D; }
/* 90s beveled button */
.bevel{ background:#C0C0C0; border:2px solid; border-color:#fff #404040 #404040 #fff; padding:4px 12px; font:16px Arimo, sans-serif; }
.bevel:active{ border-color:#404040 #fff #fff #404040; }
/* CRT scanlines overlay */
.scanlines::after{ content:""; position:absolute; inset:0; pointer-events:none;
  background: repeating-linear-gradient(transparent 0 2px, rgb(0 0 0/.12) 2px 3px); }
```

### Gaps
- No source fetched gives authoritative values for halftone, sunburst, offset-shadow or synthwave grids. Values above are synthesized; Speckyboy points to CodePens without values.
- No measured performance data was found for feTurbulence overlays (only an anecdotal complaint).

---

## Q6. Effects and motion (plain HTML/CSS/JS)

### Takeaway
Clay motion is fast and springy: 140ms transitions, −2px hover lift, 0.97 press scale and a bounce on release or success. Organic motion is slow: morphs, drifts, breathing and crossfades at 600ms or more, paused near focused tasks. Retro motion is period-specific (marquee, neon flicker, grid scroll, slowly rotating badges) and must stay optional and non-essential.

### Cited Findings
- Clay: 140ms ease transitions on transform and box-shadow; hover translateY(−2px); press scale(0.97) with shadow offsets roughly halved; a "springy bounce on release" without values (points to Material motion). — [setproduct](https://preview.setproduct.com/blog/claymorphism-design-guide)
- Clay: buoyant lifts, slight squash-and-stretch, a gentle bounce on success; repeated motion slow and sparse. — [daisyUI: Claymorphism](https://trends.daisyui.com/trend/claymorphism/)
- Organic/Blob: silhouettes morph slowly, small accents float, sections ease into one another. — [daisyUI: Organic/Blob](https://trends.daisyui.com/trend/organic-blob-design/)
- Biophilic: slow movement suggesting breeze, growth, water, sunlight or breathing; "ambient effects should stop around focused tasks". — [daisyUI: Biophilic](https://trends.daisyui.com/trend/biophilic-design/)
- Wabi-sabi: slow, imperfect crossfades and hand-paced reveals; avoid machine-like precision or looping. — [daisyUI: Wabi-Sabi](https://trends.daisyui.com/trend/wabi-sabi/)
- Mid-century: simple sliding panels, gently rotating motifs, straightforward reveals. — [daisyUI: MCM](https://trends.daisyui.com/trend/mid-century-modern/)
- Psychedelic: morph, rotate, breathe and drift "at slow tempos without obscuring the next action". — [daisyUI: Psychedelic](https://trends.daisyui.com/trend/psychedelic-design/)
- Synthwave: grid moves toward the viewer, neon pulses, sun scans, light trails glide. — [daisyUI: Synthwave](https://trends.daisyui.com/trend/synthwave-outrun/)
- Web 1.0: looping GIFs, marquees, blinking marks and hover swaps are nostalgic artefacts, "not the only way to convey information". — [daisyUI: Web 1.0](https://trends.daisyui.com/trend/web-1-0-webcore/)
- Retro sites use scroll-animated scrapbook images (Bialetti, Kalso), marquee type (Bonjour Market) and a mouseover trail (Bonnie Hong). — [HubSpot](https://blog.hubspot.com/website/retro-websites)
- Heights uses a floating cloud animation in the hero. — [Limely](https://www.limely.co.uk/blog/our-top-10-health-wellness-websites)

### Inferences
Motion tokens (synthesized):
```css
:root{
  /* clay: overshoot springs */
  --ease-bounce: cubic-bezier(.34,1.56,.64,1);      /* "back-out" overshoot */
  --ease-squish: cubic-bezier(.68,-0.55,.27,1.55);  /* in-out back */
  /* CSS linear() spring (supported in current Chromium/Firefox/Safari; falls back if unsupported) */
  --ease-spring: linear(0, .5 7%, 1.06 15%, 1.02 22%, .99 30%, 1 45%);
  --t-fast:140ms; --t-pop:320ms;
  /* organic: slow, calm */
  --ease-calm: cubic-bezier(.25,.1,.25,1); --t-fade:800ms; --t-drift:12s;
}
.pop-in{ animation: pop var(--t-pop) var(--ease-bounce) both; }
@keyframes pop{ from{ transform:scale(.85); opacity:0 } to{ transform:none; opacity:1 } }
.fade-up{ opacity:0; transform:translateY(16px); transition: opacity var(--t-fade) var(--ease-calm), transform var(--t-fade) var(--ease-calm); }
.fade-up.is-in{ opacity:1; transform:none; }
.float{ animation: float 6s ease-in-out infinite alternate; }
@keyframes float{ to{ transform: translateY(-10px) rotate(1deg); } }
.marquee{ display:flex; gap:2rem; animation: tick 30s linear infinite; }
@keyframes tick{ to{ transform:translateX(-50%); } }
.flicker{ animation: flicker 4s steps(1) infinite; }
@keyframes flicker{ 0%,19%,22%,62%,64%,100%{opacity:1} 20%,63%{opacity:.55} }  /* keep < 3 flashes/s */

@media (prefers-reduced-motion: reduce){
  *,*::before,*::after{ animation-duration:.01ms !important; animation-iteration-count:1 !important;
    transition-duration:.01ms !important; scroll-behavior:auto !important; }
  .fade-up{ opacity:1; transform:none; }
}
```
```js
// Reveal-on-scroll (vanilla JS), skipped entirely under reduced motion
const rm = matchMedia('(prefers-reduced-motion: reduce)').matches;
const els = document.querySelectorAll('.fade-up');
if (rm || !('IntersectionObserver' in window)) els.forEach(e=>e.classList.add('is-in'));
else { const io = new IntersectionObserver((es)=>es.forEach(e=>{ if(e.isIntersecting){ e.target.classList.add('is-in'); io.unobserve(e.target);} }),{rootMargin:'0px 0px -10% 0px'});
  els.forEach(e=>io.observe(e)); }
// Marquee / rotating badge / grid scroll: add a visible pause button (WCAG 2.2.2) when the motion runs > 5s.
```

### Gaps
- No source gave numeric spring or easing values for clay. The cubic-bezier and linear() values above are common community values, not sourced.
- `linear()` browser support was not verified in this session; check caniuse before relying on it, and keep a cubic-bezier fallback.

---

## Q7. Accessibility pitfalls and fixes; performance notes

### Takeaway
The main risks are low-contrast text on pastels and earth tones, shadow-only boundaries and states (clay), text placed in or over busy blobs and textures (organic), and display faces, neon and motion used for content (retro). SVG noise and large blur shadows have a real rendering cost, so pre-render textures as small tiled files and limit animated shadows.

### Cited Findings
- Claymorphism has fewer obvious accessibility problems than neumorphism. Still keep a clear hierarchy, check colour pairs for low-contrast-sensitivity users and respect motion preferences for floating effects. — [OpenReplay](https://blog.openreplay.com/implementing-claymorphism-with-css/)
- Clay: text at WCAG AA 4.5:1 minimum; check every pastel pair; "don't rely on shadow alone to show state"; "keep the soft look on shapes, not on legibility"; tap targets ≥48×48. Avoid clay in dense data tables, analytics dashboards, enterprise/admin tools, text-heavy reading and low-contrast accessibility-critical flows. — [setproduct](https://preview.setproduct.com/blog/claymorphism-design-guide)
- Neumorphism's low contrast and unclear boundaries made interaction harder; claymorphism's distinct edges and colour cues are presented as remedies. — [LogRocket](https://blog.logrocket.com/ux-design/what-is-claymorphism-web-design/)
- Organic/Blob: keep interactive targets predictably sized despite irregular shapes; keep type off curves. — [daisyUI: Organic/Blob](https://trends.daisyui.com/trend/organic-blob-design/)
- Psychedelic: keep practical copy low density, put schedules/prices/controls on calm solid fields, preserve recognisable word silhouettes, and don't let motion obscure the next action. — [daisyUI: Psychedelic](https://trends.daisyui.com/trend/psychedelic-design/)
- Web 1.0: avoid novelty backgrounds behind text, keep obvious link styling, don't make motion the only carrier of information, and keep decorative fonts to banners. — [daisyUI: Web 1.0](https://trends.daisyui.com/trend/web-1-0-webcore/)
- Synthwave: the source has no accessibility section; dark/neon designs need explicit contrast and motion checks. — [daisyUI: Synthwave](https://trends.daisyui.com/trend/synthwave-outrun/)
- feTurbulence grain: no IE support; Blink/WebKit blend differences; anecdotal performance complaint. — [CSS-Tricks](https://css-tricks.com/grainy-gradients/)
- WCAG 2.2 criteria relevant here:
  - 1.4.3 Contrast (Minimum)
  - 1.4.11 Non-text Contrast
  - 2.2.2 Pause, Stop, Hide
  - 2.3.1 Three Flashes
  - 2.3.3 Animation from Interactions (AAA)
  - 2.4.7 / 2.4.11 Focus Visible / Focus Not Obscured
  - 2.5.8 Target Size (Minimum, 24×24 CSS px)

  — [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) (standard reference; not fetched in this session)

### Inferences
Pitfall → fix checklist (synthesized):
- **Clay**
  - *Pitfall:* white text on pastel or coral. *Fix:* dark ink text. Computed: white on #B8A6FF is 2.11 and white on #FF7A6B is 2.55, both fail; #2E2A3F on them passes.
  - *Pitfall:* button boundary made only of shadow. *Fix:* a fill ≥3:1 against the page, or a 2px darker border (1.4.11).
  - *Pitfall:* pressed or selected state shown only by a changed inset. *Fix:* also change colour or icon, plus `aria-pressed`/`aria-selected`.
  - *Pitfall:* focus ring lost against soft shadows. *Fix:* `outline: 3px solid var(--ink); outline-offset: 3px`.
  - *Pitfall:* Windows High Contrast / forced colours drops shadows, so cards vanish. *Fix:* `@media (forced-colors: active){ .clay{ border:2px solid CanvasText; } }`.
- **Organic**
  - *Pitfall:* text over photography or grain. *Fix:* a solid or ≥85%-opacity cream panel behind text; keep grain opacity ≤0.08–0.12 and disable it on text-heavy blocks.
  - *Pitfall:* light italic serifs at small sizes. *Fix:* use display serifs ≥24px, body ≥16–18px at weight 400 or more.
  - *Pitfall:* earthy mid-tones (terracotta, avocado, burnt orange) used as text. *Fix:* limit them to large text (≥3:1) or fills; computed terracotta on cream is 4.21 and burnt orange on cream is 3.34.
  - *Pitfall:* blob-shaped buttons with odd hit areas. *Fix:* keep the clickable element rectangular or pill-shaped and put the blob behind it as decoration.
- **Retro**
  - *Pitfall:* groovy, neon or pixel display faces used for body or nav. *Fix:* display faces only ≥32px, with the plain reading face for everything else.
  - *Pitfall:* neon glow muddies glyph edges. *Fix:* keep a solid near-white core colour (#F5F3FF on #0D0221 is 18.27).
  - *Pitfall:* flicker and blink. *Fix:* keep below 3 flashes/s (2.3.1) and switch them off under reduced motion.
  - *Pitfall:* marquees. *Fix:* a pause control (2.2.2), and duplicate the text in static form for screen readers (`aria-hidden` on the clone).
  - *Pitfall:* 90s tiled backgrounds. *Fix:* only in gutters, never behind body copy.
  - *Pitfall:* 90s blue links #0000EE on silver #C0C0C0. *Fix:* none needed for text, at 5.17 it passes, but check the visited purple on silver.
- **Performance**
  - Render feTurbulence once into a small tiled PNG/WebP (128–256px, about 5–20 KB) or a static `noise.svg` file. Do not apply a live `filter: url(#…)` to large or animated elements.
  - Use `position: fixed` + `pointer-events: none` for grain overlays, so they don't trigger layout.
  - Animate only `transform` and `opacity`. Avoid animating `box-shadow` on many elements; for clay hover, animate a pseudo-element's opacity holding the alternative shadow.
  - Large blur radii (≥32px) on dozens of cards can hurt scrolling on low-end phones, so reduce shadow layers on mobile (2 instead of 4).
  - Use `will-change: transform` sparingly.
  - Subset and self-host fonts as WOFF2 with `font-display: swap`. Load the display face for headings only and preload one or two files at most; variable Fraunces/Nunito can replace several static weights.
  - Pre-optimise 3D clay hero renders as AVIF/WebP with `width`/`height` set to avoid layout shift; prefer a static render over a runtime WebGL/Spline embed for a static-site target.

### Gaps
- No measured benchmarks (frame time, paint cost) for multi-layer box-shadows or SVG noise were found. The performance advice is general best practice and is synthesized.

---

## Q8. Best-fit and poor-fit brands; anti-patterns

### Takeaway
Clay fits playful consumer, kids/edu, onboarding and friendly fintech, and fails for dense data and serious enterprise. Organic fits wellness, clean beauty, food, hospitality and artisan commerce, and fails for data-heavy or high-tech precision brands. Retro fits music, festivals, food and drink, fashion, furniture, print and gaming, and fails for products needing neutral trust and clarity (healthcare, legal, banking core flows) unless used sparingly.

### Cited Findings
- **Clay fit:** onboarding, kids/edu, friendly fintech and savings apps, 3D landing pages, empty states and celebrations. **Avoid:** dense tables, analytics dashboards, enterprise and admin tools, text-heavy reading, low-contrast accessibility-critical flows. — [setproduct](https://preview.setproduct.com/blog/claymorphism-design-guide)
- **Clay anti-patterns:** grey or neutral shadows; button radius under 16px; a pure #FFF page; skipping the inset top-left sheen; stacking clay three or more levels deep; sharp grotesks (Inter/Helvetica); multiple saturated CTAs on one screen. — [setproduct](https://preview.setproduct.com/blog/claymorphism-design-guide)
- Clay can feel "too whimsical", which minimal typography offsets; it is "not a one-size-fits-all solution". — [LogRocket](https://blog.logrocket.com/ux-design/what-is-claymorphism-web-design/)
- Clay suits education, onboarding, creative tools and playful consumer products. — [daisyUI: Claymorphism](https://trends.daisyui.com/trend/claymorphism/)
- **Organic fit:**
  - Wellness, creative tools, lifestyle, onboarding, approachable tech. — [daisyUI: Organic/Blob](https://trends.daisyui.com/trend/organic-blob-design/)
  - Wellness, sustainability, hospitality, healthcare, lifestyle. — [daisyUI: Biophilic](https://trends.daisyui.com/trend/biophilic-design/)
  - Craft, hospitality, wellness, food, slow living, artisan commerce. — [daisyUI: Wabi-Sabi](https://trends.daisyui.com/trend/wabi-sabi/)
- **Organic anti-patterns:** biophilic design should use authentic plants, landscapes and material close-ups, "rather than generic leaf decoration". — [daisyUI: Biophilic](https://trends.daisyui.com/trend/biophilic-design/) Commercial wabi-sabi often shrinks to "a palette of beige ceramics". — [daisyUI: Wabi-Sabi](https://trends.daisyui.com/trend/wabi-sabi/)
- **Retro fit by era:**
  - Psychedelic: music, festivals, fashion, entertainment. — [daisyUI: Psychedelic](https://trends.daisyui.com/trend/psychedelic-design/)
  - Mid-century: architecture, furniture, editorial, hospitality. — [daisyUI: MCM](https://trends.daisyui.com/trend/mid-century-modern/)
  - Synthwave: games, music, automotive, nightlife, streaming. — [daisyUI: Synthwave](https://trends.daisyui.com/trend/synthwave-outrun/)
  - Web 1.0: personal sites, art, dev communities, games. — [daisyUI: Web 1.0](https://trends.daisyui.com/trend/web-1-0-webcore/)

### Inferences
- **Poor fits** (synthesized, since sources mostly didn't state them):
  - *Clay:* law firms, B2B infrastructure, medical clinical tools, luxury.
  - *Organic:* fintech trading, cybersecurity, dev tools. Exception: playful blob for approachable SaaS.
  - *Retro 70s/psychedelic:* healthcare, insurance, government.
  - *Synthwave:* family or wellness.
  - *90s web:* e-commerce checkout flows and premium brands, unless ironic.
  - *Mid-century:* crossovers are common and low-risk, the safest retro for businesses.
- **Anti-patterns** (synthesized):
  - *Clay:* applying the clay shadow to every element, including text containers and tables; mixing clay with glassmorphism on one screen; pastel-on-pastel with no dark anchor; 3D assets in mismatched lighting directions (keep light top-left, consistent with the shadow recipe).
  - *Organic:* stock leaf clip-art; grain on everything; blobs that crop faces or products awkwardly; too many competing curves (limit to 1–2 blob motifs per viewport); low-contrast beige-on-beige text.
  - *Retro:* mixing eras (70s groovy type with synthwave neon and 90s bevels) without intent; display fonts for body; texture overload (grain plus halftone plus scanlines together); costume nostalgia that hides the actual product.
- **Fit for the user's ecosystem** (light inference; the user's portfolio includes a handmade cosmetics-bag brand, retail cosmetics and SMB sites): organic "botanical/earthy craft" suits handmade goods; clay suits a friendly savings/fintech onboarding; retro mid-century or 70s suits cafés, bars and vintage retail among Berlin SMB clients.

### Gaps
- No source quantified conversion or trust effects of these styles by industry.

---

## Q9. Real current examples (2023–2026) and authoritative guides

### Takeaway
Retro and organic have plenty of live brand sites in 2025–2026 roundups. Clay examples in roundups are mostly templates, demos and Dribbble shots rather than named production sites. That is itself a signal: clay is used more as an accent (3D illustration, app icons, onboarding) than as a full-site system.

### Cited Findings
**Claymorphism (demos, templates and references; no third-party production sites found in sources)**
- daisyUI live claymorphism demo — https://trends.daisyui.com/claymorphism/demo/ — [daisyUI](https://trends.daisyui.com/trend/claymorphism/)
- setproduct "Claylo" clay landing template — https://preview.setproduct.com/templates/claylo — [setproduct](https://preview.setproduct.com/blog/claymorphism-design-guide)
- Amrit Pal Singh clay 3D avatars — https://amritpaldesign.com/nfts — [LogRocket](https://blog.logrocket.com/ux-design/what-is-claymorphism-web-design/)
- Slack is cited for rounded chat design (aesthetic reference only). — [LogRocket](https://blog.logrocket.com/ux-design/what-is-claymorphism-web-design/)
- Guides: [Malewicz, UX Collective, Dec 2021](https://uxdesign.cc/claymorphism-in-user-interfaces-1757fabaa377); [OpenReplay, Oct 2022](https://blog.openreplay.com/implementing-claymorphism-with-css/); [LogRocket, May 2024](https://blog.logrocket.com/ux-design/what-is-claymorphism-web-design/); [setproduct, Jun 2026](https://preview.setproduct.com/blog/claymorphism-design-guide); [daisyUI](https://trends.daisyui.com/trend/claymorphism/).

**Organic / natural (live brand sites listed in 2025–2026 roundups)**
- Āhua Skin Co (earthy tones, nature-driven) — https://ahuaskin.co.nz
- Bodha (serene, earthy, artisan) — https://bodha.com
- Herbivore Botanicals (apothecary, pastel, whitespace) — https://herbivorebotanicals.com
- True Botanicals (elegant serif, botanical photography) — https://truebotanicals.com
- Tata Harper (green/gold, garden photography) — https://tataharperskincare.com
- Salt & Stone (earth tones, outdoor photography) — https://saltandstone.com
- Farmacy (botanical green, farm story) — https://farmacybeauty.com

  — all from [Colorlib, Oct 2026](https://colorlib.com/wp/skincare-brand-website-examples/)
- Inessa (neutral, earthy palette) — https://www.inessawellness.com/
- Heights (floating cloud hero) — https://www.yourheights.com/
- Dirtea (bespoke icons, photography) — https://www.dirteaworld.com/
- Neom — https://neomwellbeing.com/

  — all from [Limely, upd. Jun 2026](https://www.limely.co.uk/blog/our-top-10-health-wellness-websites)
- Guides: [daisyUI Organic/Blob](https://trends.daisyui.com/trend/organic-blob-design/), [Biophilic](https://trends.daisyui.com/trend/biophilic-design/), [Wabi-Sabi](https://trends.daisyui.com/trend/wabi-sabi/), [Organic & atmospheric category](https://trends.daisyui.com/organic-atmospheric-ui/); [CSS-Tricks Grainy Gradients](https://css-tricks.com/grainy-gradients/); [Tate "Biomorphic"](https://www.tate.org.uk/art/art-terms/b/biomorphic).

**Retro / vintage**
- 70s: Paak House (soul/funk, brights on black, long shadows, thick outlines) — https://paakhouse.org/; Accord (orange/black 70s logo, magazine layout) — https://accord.dk/; Tonik (70s palette/type, old-desktop screen) — https://www.tonik.com/
- Mid-century/vintage European: KLR (mustard/green, vintage interiors) — https://www.klr-interieur.com/; Bialetti story (peach on maroon, scrapbook) — https://bialettistory.com/
- Print/letterpress/zine: Old Iron Press — https://www.oldironpress.com/; Ikony — https://www.ikony.tv/; Dunderville — https://www.dunderville.se/; Mondo (halftone, torn paper) — https://mondoshop.com/; Heritage Type — https://www.heritagetype.com/
- 80s/pixel: Bonnie Hong — https://www.bonniehong.com/; Crappy Explanation by Zajno (Atari pixel logos, Tron look) — https://music.zajno.com/

  — all from [HubSpot, upd. Jun 2025](https://blog.hubspot.com/website/retro-websites)
- Newstalgia/80s/geometric: Mac McAlister — https://www.themacmc.com/home; Three Uncles — https://www.threeuncles.co.uk/; StrategyFolk — https://www.strategyfolk.com.au/; Enigma — https://www.enigma.cc/; Treep Tours — https://www.treeptours.com/ — [Wix Studio, Oct 2025](https://www.wix.com/studio/blog/retro-web-design)
- Guides: [HubSpot](https://blog.hubspot.com/website/retro-websites); [Wix Studio](https://www.wix.com/studio/blog/retro-web-design); daisyUI era pages ([Psychedelic](https://trends.daisyui.com/trend/psychedelic-design/), [Mid-Century](https://trends.daisyui.com/trend/mid-century-modern/), [Synthwave](https://trends.daisyui.com/trend/synthwave-outrun/), [Web 1.0](https://trends.daisyui.com/trend/web-1-0-webcore/), plus [Memphis](https://trends.daisyui.com/trend/memphis-design/), [Vaporwave](https://trends.daisyui.com/trend/vaporwave/), [Y2K](https://trends.daisyui.com/trend/y2k/), [Halftone/Comic](https://trends.daisyui.com/trend/halftone-comic-book/)); [Speckyboy synthwave CSS snippets, Apr 2026](https://speckyboy.com/css-javascript-snippets-synthwave/).

### Inferences
- The example URLs come from roundups. I did not open each site in this session, so their current designs may have been redesigned since publication. A catalogue builder should screenshot-verify before citing them as canonical.
- For clay, use the daisyUI demo and the setproduct template as reference implementations, and treat production clay as an accent layer (3D hero art, icons, onboarding) rather than a full-site style.

### Gaps
- Awwwards, Godly, Siteinspire, Land-book and Dribbble collections were not fetched (budget). No curated 2025–2026 production claymorphism site list was found in fetched sources.
- Typewolf and Fonts In Use were not consulted for OFL retro/organic pairings.
- Example sites were not individually verified as live or still on-style in Oct 2026.
