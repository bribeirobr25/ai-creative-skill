# Web Design Styles Catalog — 01: Minimalist, Swiss / International Typographic Style, Luxury / Elegant

Research date: 2026-10-21. Implementation target: static HTML/CSS/vanilla JS, self-hosted OFL fonts, WCAG 2.2 AA, prefers-reduced-motion.

Conventions in these notes:
- Lines ending with a [Source](URL) are cited findings from pages actually read in this session (or, where marked "(spec, not fetched this session)", well-established W3C spec text whose URL is given for verification).
- Everything under "Inferences" is **synthesized recommendation** by the researcher (concrete CSS numbers, sub-variant names, layout specs) — usable as defaults, but not sourced to a single authority.
- Source quality note: the strongest sources are NN/g (two research articles), Wikipedia (history), web.dev (reduced motion), W3C WCAG. Swiss-on-web and luxury sources found are mostly agency/vendor blogs (Justinmind/UX Planet 2018, Tilda 2022, IIAD 2025, KIJO 2024, Limely 2026, Cedilla 2025) — useful for consensus traits, weak for hard numbers. **None of the sources read gave concrete pixel/rem values for grids or type scales**, so all numeric settings below are synthesized.

---

## Q1. Definition, origin and 4–6 signature traits (per style)

### Takeaway
Minimalism = removing everything that doesn't serve user goals (roots: 1960s minimal art, Mies van der Rohe, Tufte, Nielsen's 1995 heuristic; Google as early web pioneer). Swiss/International Typographic Style = 1950s Swiss modernism built on mathematical grids, sans-serif grotesks, flush-left/ragged-right text, asymmetry and objective photography. Luxury web design = restraint plus craft cues: serif or refined type, very generous whitespace, restrained/monochrome or dark-and-gold palettes, editorial photography/film, slow purposeful motion, sparse navigation and "concierge" CTAs.

### Cited Findings
**Minimalist**
- NN/g defines the goal of minimalist web design as presenting content and features "in a simple, direct way", often by removing elements that don't support users' goals (Kate Moran, 28 Jun 2015) — [NN/g: The Roots of Minimalism in Web Design](https://www.nngroup.com/articles/roots-minimalism-web-design/)
- Origins per NN/g: post-WWII minimalist art (1960s, reacting against abstract expressionism, drawing on Bauhaus; monochromatic palettes, geometric forms, industrial materials); Mies van der Rohe's "Less is more"; HCI roots in Tufte's data-ink ratio, John M. Carroll's minimalism in technical communication (1990), and Nielsen's 1995 heuristics ("aesthetic and minimalist design"); Google credited as an early web pioneer in the 2000s — [NN/g](https://www.nngroup.com/articles/roots-minimalism-web-design/)
- NN/g's defining characteristics: flat textures; limited colour palettes (often grayscale with one accent colour); generous negative space; lower amounts of content; a high ratio of meaningful elements to total elements — [NN/g](https://www.nngroup.com/articles/roots-minimalism-web-design/)

**Swiss / International Typographic Style**
- Emerged 1930s–1950s, building on 1920s modernist typography (Constructivism, De Stijl, Bauhaus); Basel School of Design reworked its foundation course with grid-based techniques in 1908; Ernst Keller began teaching at the Kunstgewerbeschule Zürich in 1918; early pioneers include Max Bill and Théo Ballmer — [Wikipedia: International Typographic Style](https://en.wikipedia.org/wiki/International_Typographic_Style)
- Josef Müller-Brockmann sought objective, impersonal graphic expression and often used large photographs; Rudolph de Harak brought the style to the US (1960s McGraw-Hill covers); the periodical *New Graphic Design* (Neue Grafik), launched 1959, spread the style internationally — [Wikipedia](https://en.wikipedia.org/wiki/International_Typographic_Style)
- Defining characteristics: grid-based structure, asymmetric layouts, sans-serif typefaces, flush-left/ragged-right text, photography preferred over illustration, simplicity/clarity/objectivity. Typefaces: Akzidenz-Grotesk, Univers, Helvetica (originally Neue Haas Grotesk, Max Miedinger & Eduard Hoffmann) — [Wikipedia](https://en.wikipedia.org/wiki/International_Typographic_Style)
- Web translation (Justinmind on UX Planet, 18 Sep 2018): mathematically constructed grids ("The grid system is an aid, not a guarantee" — Müller-Brockmann), sans-serif only, asymmetric composition, flush-left ragged-right (not justified), fewer UI elements each with a purpose, hierarchy built from size/colour/weight/position/contrast, photography over illustration as "more objective", generous negative space; "form follows function" — [UX Planet / Justinmind](https://uxplanet.org/swiss-style-web-design-everything-you-need-to-know-2b128fd327b9)
- Tilda (4 May 2022) describes web Swiss Style as "quickly perceived, universal, efficient, and highly informative", avoids decoration, uses strict modular grids (suggests 3 or 4 columns in its editor) and hierarchical sans-serif text (bold title → subtitle → body) — [Tilda Blog](https://blog-en.tilda.cc/tpost/zsxaujziu1-swiss-style-in-web-design)

**Luxury / elegant**
- IIAD (12 Jun 2025) lists the cues that make sites "feel expensive": classic serif fonts for timelessness/authority (Dior, Rolex); one or two font families; thin, well-spaced headings on clean backgrounds (Bottega Veneta "quiet luxury"); generous negative space (Hermès); restrained monochrome palettes (Chanel) or dark mode with deep blacks and gold accents (Cartier); moody, film-like imagery and ambient video loops (Burberry); slow, smooth motion — "revealing rather than reacting"; sparse curated navigation; subtle CTAs ("Request a Consultation" rather than "Shop Now"); exclusivity cues ("Price Upon Request", gated/member areas) — [IIAD: Why Some Websites Just Feel Expensive](https://www.iiad.edu.in/the-circle/why-some-websites-just-feel-expensive/)
- KIJO (London luxury agency, 1 Nov 2024): luxury typography "often favours bespoke or minimalist fonts"; whitespace reads as "deliberate and confident"; high-quality, consistently styled imagery and behind-the-scenes video; subtle, purposeful motion; frictionless navigation; smooth scrolling and fast loading — [KIJO](https://kijo.london/blog/luxury-website-design)

### Inferences (synthesized)
- **Minimalist — 5 signature traits for a generator**: (1) one dominant element per viewport; (2) ≥40–50% of the viewport empty; (3) 1 neutral + 1 accent colour max; (4) a single type family in 2–3 weights; (5) no decorative textures, gradients or shadows (or one very subtle elevation level).
- **Swiss — 6 signature traits**: (1) visible-feeling modular grid (often 12 columns, content snapped to 2/3/4/6-col spans); (2) neo-grotesk sans only; (3) flush-left/ragged-right everywhere, no centred body text; (4) asymmetric composition with large type as image; (5) strong scale contrast (huge headline vs small body); (6) flat colour fields — classic triad white/black/red (Swiss red ≈ `#E30613`/`#FF0000` family) — plus objective photography.
- **Luxury — 6 signature traits**: (1) high-contrast serif or Didone display type (or very refined wide-tracked sans); (2) extreme whitespace and slow vertical rhythm (fewer things per screen than any other style); (3) full-bleed editorial photography/film as the hero; (4) restrained palette: ivory/bone/black, optional metallic or deep jewel accent; (5) slow, eased motion (600–1200 ms reveals); (6) small, wide-tracked uppercase UI labels and understated, text-link CTAs.
- Key distinction for a classifier: Minimal = *reduction*; Swiss = *structure/system*; Luxury = *restraint + craft + emotion*. Many luxury sites are built on minimal/Swiss bones — the difference is serif type, photography mood, motion tempo and copy register.

### Gaps
- No authoritative source found that formally defines "luxury web design" as a style; definitions come from agency blogs.
- Wikipedia page read did not discuss Armin Hofmann or Emil Ruder in body text (Ruder only in references); their contributions (Basel school, Ruder's *Typographie*) are known but not sourced here.

---

## Q2. Recognised sub-variants / directions (2–4 per style)

### Takeaway
None of the sources read formally codify sub-variants; the names below are synthesized from the traits sources attribute to specific brands (e.g., IIAD contrasts Bottega's "quiet luxury" vs Cartier's dark-and-gold vs Chanel's monochrome; Limely contrasts editorial-collage Abask vs functional COS). Treat names as catalog labels.

### Cited Findings
- IIAD distinguishes several luxury registers: quiet luxury with thin, well-spaced headings (Bottega Veneta); restrained monochrome (Chanel); soft gradients and deep palettes (Rolls-Royce); dark mode with deep blacks and gold (Cartier) — [IIAD](https://www.iiad.edu.in/the-circle/why-some-websites-just-feel-expensive/)
- Limely (3 Mar 2026, updated 18 Jun 2026) shows the minimal-luxury spectrum: calm neutral palette with ample negative space (Rêve En Vert); craftsmanship-focused uncluttered pages (The Row); editorial collage layouts with generous whitespace (Abask); "simple, functional" typography with clear structured grids (COS); atmospheric/edgy photography (DeMellier) — [Limely](https://www.limely.co.uk/blog/top-10-minimalist-luxury-ecommerce-websites)
- NN/g notes minimalism "should never be a final product" in its extreme form and that rigid adherence produces "wastefully low information density" — relevant to choosing between "stark" and "functional" minimal — [NN/g](https://www.nngroup.com/articles/roots-minimalism-web-design/)

### Inferences (synthesized catalog sub-variants)
**Minimalist**
1. **Stark / Mono minimal** — pure white `#FFFFFF` or off-black, black type, zero accent or one saturated accent, single sans. Use: architects, portfolios, design studios, tech manifestos.
2. **Warm minimal (Japandi / soft)** — bone/oat backgrounds (`#F5F1EA`–`#EFE9DF`), warm greys, muted earth accent (clay, sage), soft humanist sans or a light serif headline, 4–8 px radii. Use: wellness, ceramics, interior, skincare, bakeries, boutique hotels.
3. **Functional / product minimal** — SaaS/product UIs: neutral greys, one brand accent, dense-but-calm components, 1px hairline borders, subtle shadows. Use: software, fintech, B2B. (NN/g's caution on low density applies least here.)
4. **Typographic / text-only minimal** — no imagery, the type *is* the layout (big name, list of projects). Use: personal sites, writers, consultants.

**Swiss / International**
1. **Classic Swiss (Zürich/Müller-Brockmann)** — strict 12-col grid, neo-grotesk, white/black/red, large photography, asymmetric posters-as-sections. Use: cultural institutions, exhibitions, architecture, events.
2. **Neo-Swiss / New Grotesk** — contemporary grotesks (Inter, Instrument Sans, Geist), oversized headlines with tight negative tracking, monochrome + one neon/vivid accent, small mono metadata. Use: agencies, studios, tech brands, conferences. (Most common on current award galleries.)
3. **Swiss-Brutalist / Visible-grid** — exposed grid lines, 1px rules everywhere, monospace labels, index/table layouts, minimal imagery. Use: type foundries, archives, developer tools, art publications.
4. **Editorial Swiss (Basel)** — more photography, multi-column text, captions/indices, slightly warmer palette. Use: magazines, museums, research/editorial brands.

**Luxury / elegant**
1. **Quiet luxury** — ivory/stone, near-black text, refined sans or light serif, almost no motion, tiny uppercase labels, products on neutral backgrounds (The Row, Totême, Bottega). Use: fashion, leather goods, high-end minimal brands.
2. **Heritage maison** — Didone/Garamond serifs, centred wordmark, black/white with gold or house colour, crafted film, storytelling chapters (Hermès, Chanel, Cartier). Use: jewellery, watches, heritage fashion, champagne.
3. **Dark opulent** — deep black/navy/forest backgrounds, gold/champagne accents, cinematic video, slow reveals (Cartier dark, Rolls-Royce). Use: automotive, high jewellery, spirits, nightlife, premium real estate.
4. **Editorial-fashion luxury** — collage/asymmetric grids, mixed image sizes, large serif headlines, magazine pacing (Abask, Jacquemus-type). Use: concept stores, designers, creative-led fashion, beauty.
5. (Optional) **Hospitality / wellness luxury** — warm palettes, serif + sans, full-bleed landscape photography, booking CTA as primary (Aman-type, ESPA). Use: hotels, spas, residences.

### Gaps
- No design-history or NN/g source names these sub-variants; they are researcher-defined labels.
- Jacquemus and Aman are named from general knowledge as archetypes; their current (2026) sites were not inspected in this session.

---

## Q3. Most-used layouts: hero patterns, grids, navigation, product/collection grids, section rhythm, mobile

### Takeaway
Sources agree qualitatively: minimal = few elements, generous space; Swiss = strict modular grid (3–4 or 12 columns), asymmetry, flush-left; luxury = full-bleed imagery hero, sparse curated nav, simple uncluttered product grids, gradual "exhibition" pacing. Concrete grid numbers were not in any source; defaults below are synthesized.

### Cited Findings
- Swiss web layouts place elements on a mathematically constructed grid; asymmetric composition; content structured around F- and Z-pattern reading — [UX Planet / Justinmind](https://uxplanet.org/swiss-style-web-design-everything-you-need-to-know-2b128fd327b9)
- Tilda suggests customizing a modular grid with 3 or 4 columns for Swiss web layouts — [Tilda](https://blog-en.tilda.cc/tpost/zsxaujziu1-swiss-style-in-web-design)
- Luxury navigation should be sparse, curated, distraction-free; content revealed gradually "like a curated exhibition"; 360° zoomable product views (Gucci) — [IIAD](https://www.iiad.edu.in/the-circle/why-some-websites-just-feel-expensive/)
- Luxury e-commerce product grids described as "simple grids" (The Row), "curated, uncluttered grids" (Totême), "grid-based presentation" (Chanel), "clear, structured grids" (COS), "image-led filter structure" (Arket); Abask uses "editorial collage layouts" — [Limely](https://www.limely.co.uk/blog/top-10-minimalist-luxury-ecommerce-websites)
- NN/g notes hidden global navigation as a minimalism-influenced trend — [NN/g](https://www.nngroup.com/articles/roots-minimalism-web-design/)
- Flat/minimal designs work best with low information density, a traditional/consistent layout, and interactive elements that stand out — [NN/g: Flat UI Elements Attract Less Attention](https://www.nngroup.com/articles/flat-ui-less-attention-cause-uncertainty/)

### Inferences (synthesized defaults)
**Shared base**: `--container: min(100% - 2*var(--gutter-x), var(--max))`; page side gutter `clamp(16px, 4vw, 48px)` (16px at phone width per target). Use CSS Grid `grid-template-columns: repeat(12, minmax(0,1fr))` with `column-gap: var(--gap)`.

**Minimalist**
- Grid: 12 col, gap 24–32px desktop / 16px mobile; text measure `max-width: 60–68ch`; container max 1200–1280px (functional) or 1040px (stark/typographic).
- Hero patterns: (a) single sentence H1 left-aligned in the upper-left third, lots of space, one CTA; (b) centred product on plain field; (c) split 50/50 text + one image.
- Nav: logo left, 3–5 visible text links right (avoid hamburger on desktop); mobile: visible "Menu" text button opening full-screen overlay.
- Collection grid: 3 col desktop / 2 col tablet / 1–2 col mobile, image ratio 4:5 or 1:1, name + price below in small text, no card chrome.
- Section rhythm: vertical padding `clamp(64px, 10vw, 160px)`; one idea per section.

**Swiss**
- Grid: 12 col (or 6/4 modular), gap 16–24px, *visible alignment*: all text starts on column lines; container max 1440–1600px or fluid full-width with gutters (Swiss often uses full width).
- Hero patterns: (a) oversized headline spanning 8–12 cols, set flush-left, with small metadata in columns 1–3; (b) poster hero — full-width photo + headline overlapping grid lines; (c) index hero — table/list of projects with year/client/category columns.
- Nav: horizontal text links in a top bar aligned to grid columns, often numbered (01, 02…), or sticky top-left wordmark + top-right links; mobile collapses to a 2-column link list or "Menu" overlay.
- Collection/project grids: asymmetric spans (e.g., 7+5, 4+4+4, 8 offset 4), captions as small text with mono numbers; list/table view toggle.
- Rhythm: baseline-ish spacing on an 8px unit; sections separated by 1px rules rather than big padding; padding 48–96px.
- Mobile: collapse to 4-col grid (gap 12–16px), keep flush-left, reduce display size via `clamp()`, keep rules and numbering.

**Luxury**
- Grid: 12 col, gap 20–32px; content max 1440px but heroes full-bleed (100vw/100svh); text blocks narrow (`max-width: 36–48ch`) and often centred for intros.
- Hero patterns: (a) full-bleed image/video with small centred wordmark and a single text-link CTA ("Discover"); (b) split editorial — large image 7 cols + serif headline 4 cols; (c) still-life product on neutral field, centred.
- Nav: centred wordmark with minimal links split left/right, or 2–4 links + "Menu"; utility (search, account, bag) as small uppercase text or thin icons; transparent over hero → solid on scroll.
- Product grid: 2 col (editorial) to 4 col (catalogue) desktop, 2 col mobile; image ratio 3:4 or 4:5 on neutral `#F2F0EC`-type background; name in uppercase small caps-ish, price below or hidden; hover swaps to second image; occasional full-width editorial tile breaking the grid every 6–8 products.
- Rhythm: largest section spacing of the three styles `clamp(96px, 14vw, 240px)`; alternating full-bleed image / narrow text "chapters".
- Mobile: hero 100svh with image cropped art-directed via `<picture>`; nav to "Menu" text; keep 2-col grid; reduce letter-spacing on uppercase labels slightly.

### Gaps
- No source provided concrete column/gutter/max-width values for any style; all numbers above are synthesized.
- NN/g's quantitative study on hidden navigation ("Hamburger Menus and Hidden Navigation Hurt UX Metrics", 2016 — https://www.nngroup.com/articles/hamburger-menus/) was not fetched in this session; its figures should be verified before citing.

---

## Q4. Typography: families, scale ratios, sizes, weights, tracking, line-height; free OFL pairings

### Takeaway
Sources specify classifications (minimal: one family; Swiss: sans-serif only, Akzidenz/Helvetica/Univers lineage; luxury: classic serifs/Didones, one weight, wide-tracked caps, one serif + one sans). Only luxury tracking got a number (+50 to +200 for wordmarks). Free OFL options on Google Fonts are well documented for luxury (Cedilla list).

### Cited Findings
- Swiss typefaces: Akzidenz-Grotesk, Univers, Helvetica (Neue Haas Grotesk) — [Wikipedia](https://en.wikipedia.org/wiki/International_Typographic_Style)
- Justinmind suggests Montserrat, Open Sans, Lato, Helvetica for Swiss web; serif fonts excluded — [UX Planet](https://uxplanet.org/swiss-style-web-design-everything-you-need-to-know-2b128fd327b9) (note: Montserrat is geometric, not neo-grotesk — stylistically a loose fit; dated 2018)
- Tilda suggests Helvetica, Futura, Tilda Sans; hierarchy bold title → subtitle → body — [Tilda](https://blog-en.tilda.cc/tpost/zsxaujziu1-swiss-style-in-web-design)
- Luxury: classic serif fonts; limit to one or two families; proper kerning; thin, well-spaced headings — [IIAD](https://www.iiad.edu.in/the-circle/why-some-websites-just-feel-expensive/)
- Cedilla (23 Feb 2025, updated 30 May 2026) — 13 free OFL Google Fonts for luxury: Playfair Display (high-contrast transitional; pair with Inter or Source Sans; very widely used so less distinctive), EB Garamond (old-style, good for long body text with generous leading), Cormorant / Cormorant Garamond (display sizes; wide tracking for quiet-luxury logos), Bodoni Moda (Didone with optical sizes; "Don't use Bodoni at 12pt — it'll fall apart on screen"), Oranienbaum, Cinzel (all caps, wide tracking; pair with Tenor Sans or EB Garamond), Italiana (single weight; logos/hero), Cardo, Forum (warmer than Cinzel; hotels/spas), Marcellus (boutiques/restaurants), Tenor Sans (refined sans), Della Respira (engraved caps; invitations) — [Cedilla Studio](https://www.cedilla.studio/blog/free-luxury-fonts)
- Cedilla's setting guidance: luxury wordmark tracking roughly +50 to +200 (i.e., 0.05–0.2em); one weight throughout (regular or light), hierarchy via size and spacing not bold; one serif + clean sans; avoid serif+serif — [Cedilla Studio](https://www.cedilla.studio/blog/free-luxury-fonts)
- WCAG 2.2 SC 1.4.12 Text Spacing (AA): content must survive user overrides of line-height 1.5×, paragraph spacing 2×, letter-spacing 0.12em, word-spacing 0.16em without loss — [W3C Understanding 1.4.12](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html) (spec, not fetched this session)

### Inferences (synthesized defaults; all fonts named are OFL on Google Fonts / Fontsource)
**Type scale ratios** (modular): minimal 1.2 (minor third) or 1.25; Swiss 1.333–1.5 or a non-modular "jump" scale (body 16–18px, display 96–200px); luxury 1.25–1.333 for UI with a separate oversized display size. Implement fluid sizes with `clamp()`, e.g. `--step-5: clamp(2.5rem, 1.2rem + 6vw, 6rem)`.

| Setting | Minimalist | Swiss | Luxury |
|---|---|---|---|
| Body size | 16–18px | 15–18px | 16–18px (serif body 18–20px) |
| Body line-height | 1.5–1.65 | 1.4–1.5 | 1.6–1.75 |
| Display line-height | 1.05–1.15 | 0.9–1.0 | 1.0–1.15 |
| Display tracking | −0.01 to −0.02em | −0.02 to −0.04em | 0 to −0.01em (serif); caps +0.08–0.2em |
| Small UI labels | 12–14px, +0.02em | 11–13px, often mono, uppercase +0.04em | 11–13px uppercase +0.12–0.2em |
| Weights | 400/500 (+600) | 400/500/700 (bold for hierarchy) | 300/400 only (Cedilla) + italic |
| Families | 1 | 1 sans (+1 mono optional) | 1 serif + 1 sans |

**Pairings (OFL)**
- Minimal stark: Inter (or Inter Tight for display) alone; Geist + Geist Mono; Manrope alone.
- Minimal warm: Instrument Serif (display) + Instrument Sans; Fraunces (soft, opsz) + DM Sans; Newsreader + Public Sans.
- Swiss classic: Inter / Archivo / Schibsted Grotesk / Instrument Sans (closest free neo-grotesk feel to Helvetica/Akzidenz); Arimo is metric-compatible with Arial/Helvetica as fallback.
- Swiss neo/brutalist: Space Grotesk or Hanken Grotesk + IBM Plex Mono / JetBrains Mono / Space Mono for metadata.
- Luxury quiet: Cormorant Garamond (display, light, wide-tracked caps for wordmark) + Jost or Tenor Sans (UI).
- Luxury heritage: Bodoni Moda (display ≥32px only) + Inter/Jost; Cinzel wordmark + EB Garamond body (Cedilla).
- Luxury editorial: Playfair Display or Gilda Display + Work Sans; Italiana (hero only) + Marcellus/Jost.
- Avoid as luxury defaults: Montserrat-everywhere, Playfair+Montserrat (overused template combo), script fonts for body.

**Self-hosting**: subset to Latin/Latin-Ext WOFF2 via Fontsource packages or google-webfonts-helper, `font-display: swap`, preload only the hero face, prefer variable fonts (Inter, Fraunces, Bodoni Moda, Cormorant are variable) to cut requests; use `size-adjust`/`ascent-override` fallback metrics to reduce CLS.

### Gaps
- No primary source gave numeric type scales or line-heights for any of the three styles (table is synthesized).
- Typewolf / Fonts In Use pages were not read in this session; no citation for "most used" fonts on real luxury or Swiss sites.

---

## Q5. Colour: palettes, number of colours, contrast practice

### Takeaway
Minimal: grayscale + one accent (NN/g). Swiss: flat fields, classic white/black/red (a template example in Justinmind uses white/blue/black). Luxury: monochrome (Chanel), deep palettes/soft gradients (Rolls-Royce), black + gold (Cartier). WCAG AA requires 4.5:1 for body text and 3:1 for large text and UI components.

### Cited Findings
- Minimal: limited palettes, often grayscale with one accent — [NN/g](https://www.nngroup.com/articles/roots-minimalism-web-design/)
- Swiss template example uses three colours: white, blue, black — [UX Planet](https://uxplanet.org/swiss-style-web-design-everything-you-need-to-know-2b128fd327b9)
- Luxury: restrained monochrome (Chanel); soft gradients + deep palettes (Rolls-Royce); dark mode with deep blacks and gold accents (Cartier) — [IIAD](https://www.iiad.edu.in/the-circle/why-some-websites-just-feel-expensive/)
- Rêve En Vert uses a calm neutral palette; Fendi uses clean white backgrounds — [Limely](https://www.limely.co.uk/blog/top-10-minimalist-luxury-ecommerce-websites)
- NN/g recommends inline links in a contrasting colour; low-contrast link styling causes users to overlook them — [NN/g](https://www.nngroup.com/articles/flat-ui-less-attention-cause-uncertainty/)
- WCAG 2.2 SC 1.4.3 Contrast (Minimum, AA): 4.5:1 for normal text, 3:1 for large text (≥24px regular or ≥18.66px bold) — [W3C Understanding 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) (spec, not fetched this session)
- WCAG 2.2 SC 1.4.11 Non-text Contrast (AA): 3:1 for UI component boundaries/states and meaningful graphics — [W3C Understanding 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) (spec, not fetched this session)

### Inferences (synthesized palettes as CSS tokens)
- **Minimal stark** (3 colours): `--bg:#FFFFFF; --fg:#111111; --muted:#6B6B6B` (5.3:1 on white — OK for text); accent optional `#0047FF`.
- **Minimal warm** (4–5): `--bg:#F5F1EA; --surface:#ECE6DC; --fg:#2B2622; --muted:#6E655C` (≈5:1 on bg, verify); `--accent:#A0522D` (clay) or `#6F7D5C` (sage — check text use ≥4.5:1).
- **Swiss classic** (3): `--bg:#FFFFFF; --fg:#000000; --accent:#E30613` (Swiss red; ~4.9:1 on white — OK for large text and UI, borderline for small text: verify; for small red text use `#C8000F`).
- **Neo-Swiss** (3–4): `--bg:#F2F2F0; --fg:#0A0A0A; --accent:#FF4F00` or `#2B50FF`; neon accents (e.g. `#D4FF3F`) only as fills behind black text, never as text on white.
- **Luxury quiet** (3–4): `--bg:#F7F4EF (ivory); --surface:#EDE8E0; --fg:#1A1A1A; --muted:#5E5A55`.
- **Luxury dark opulent** (3–4): `--bg:#0B0B0C; --fg:#F2EEE6; --muted:#A39E95; --gold:#C9A96E` (gold on near-black ≈ 8:1 — good; gold on ivory fails for text — use gold only for rules/icons on light backgrounds or darken to `#8A6D3B`).
- Rule: max 1 accent; neutrals do 90% of the work; define tokens on `:root` and a dark-mode set under `prefers-color-scheme`.
- Luxury pitfall: light-grey-on-ivory "elegant" captions (e.g. `#B5AFA6` on `#F7F4EF` ≈ 2:1) fail AA — keep muted text ≥4.5:1.

### Gaps
- No source quantified typical palette sizes beyond NN/g's "grayscale + one accent" and the Swiss 3-colour example; Swiss red hex values are from general knowledge, not a cited source. Contrast ratios above are researcher estimates — run a checker before shipping.

---

## Q6. Components and details: buttons, cards, rules, imagery, iconography

### Takeaway
Cited guidance is mainly about signifiers (NN/g: flat buttons/links must still look clickable) and imagery (Swiss: objective photography; luxury: film-like, craftsmanship, 360° zoom, ambient video). Component specs are synthesized.

### Cited Findings
- Weak signifiers (flat, unstyled links/buttons) cost 22% more task time and 25% more fixations in a 71-participant eyetracking study; strong signifiers = colour contrast, underlines, button shapes — [NN/g, Kate Moran, 3 Sep 2017](https://www.nngroup.com/articles/flat-ui-less-attention-cause-uncertainty/)
- Swiss: photography over illustration as "more objective"; Tilda suggests minimal photos/illustrations and simple abstract forms — [UX Planet](https://uxplanet.org/swiss-style-web-design-everything-you-need-to-know-2b128fd327b9); [Tilda](https://blog-en.tilda.cc/tpost/zsxaujziu1-swiss-style-in-web-design)
- Müller-Brockmann often used large photographs — [Wikipedia](https://en.wikipedia.org/wiki/International_Typographic_Style)
- Luxury imagery: rich photography, video and editorial copy; moody film-like imagery over plain product shots; zoomable 360° views; ambient video loops; refined hover micro-interactions — [IIAD](https://www.iiad.edu.in/the-circle/why-some-websites-just-feel-expensive/)
- Fendi: high-impact imagery on clean white backgrounds; DeMellier: atmospheric photography; Abask: lifestyle imagery given room — [Limely](https://www.limely.co.uk/blog/top-10-minimalist-luxury-ecommerce-websites)
- WCAG 2.2 SC 2.5.8 Target Size (Minimum, AA, new in 2.2): pointer targets at least 24×24 CSS px (or sufficient spacing) — [W3C Understanding 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) (spec, not fetched this session)

### Inferences (synthesized component specs)
| Component | Minimalist | Swiss | Luxury |
|---|---|---|---|
| Primary button | Solid `--fg` bg, white text, 44–48px tall, padding 0 24px, radius 0–6px (warm: 8px / pill) | Solid black or red rectangle, radius 0, uppercase or sentence case 14–16px, often full-column-width | Outline 1px `--fg` or solid black, radius 0, height 48–52px, uppercase 12–13px tracking 0.15em; or text link with underline |
| Secondary / link | Underlined text (`text-underline-offset: .2em; text-decoration-thickness: 1px`) | Text + arrow "→", underline on hover | Small caps text with 1px underline animating width |
| Cards | No border/shadow; image + text only; or 1px `#E5E5E5` border (functional) | No card: content on grid cells separated by 1px rules | No card chrome; image on neutral field, text centred or left beneath |
| Rules/dividers | Rare; 1px `rgba(0,0,0,.08)` | Core motif: 1px or 2px solid black full-width/column rules | Hairline 1px or 0.5px (`transform: scaleY(.5)`) in muted/gold |
| Radius | 0–8px (consistent) | 0 | 0 (occasional arched image masks in hospitality) |
| Shadows | None or `0 1px 2px rgba(0,0,0,.06)` | None | None (dark opulent may use soft glow on gold, sparingly) |
| Image ratios | 4:5, 1:1, 16:9 | Full-bleed, 3:2, 4:3, cropped tight/asymmetric | 3:4 / 4:5 portraits, 21:9 cinematic heroes, 100svh |
| Image treatment | Product on plain bg, soft natural light | High-contrast, B/W or duotone, objective | Editorial, moody, grain allowed, consistent colour grade |
| Icons | Thin outline 1.5px stroke (Lucide/Phosphor Light), 20–24px | Few or none; arrows, plus signs, numbers | Text labels preferred ("Search", "Bag (2)"); if icons, 1px stroke |

- Always keep link underlines (or a non-colour cue) in body copy to satisfy NN/g signifier evidence and WCAG 1.4.1 (Use of Colour).
- Interactive targets ≥44×44px recommended (exceeds 2.5.8's 24px minimum) — important for luxury's tiny uppercase labels.

### Gaps
- No source gave measured button/card dimensions for these styles; table is synthesized.

---

## Q7. Effects, motion and configurations (concrete CSS; plain HTML/CSS/JS)

### Takeaway
Luxury motion is "slow, smooth and purposeful… revealing rather than reacting" (IIAD); minimal and Swiss motion should be minimal and functional. All motion must be gated with `prefers-reduced-motion` (web.dev patterns). Concrete durations/easings are synthesized.

### Cited Findings
- Luxury: slow, smooth, purposeful animation; soft scroll-triggered effects and gentle fades (Apple cited); refined micro-interactions; transitions that build anticipation — [IIAD](https://www.iiad.edu.in/the-circle/why-some-websites-just-feel-expensive/)
- Luxury: smooth transitions, hover effects, refined animations; motion minimal and purposeful; smooth scrolling — [KIJO](https://kijo.london/blog/luxury-website-design)
- `prefers-reduced-motion` returns `no-preference` or `reduce`; supported Chrome 74, Edge 79, Firefox 63, Safari 10.1; patterns: wrap animations in `@media (prefers-reduced-motion: no-preference)`, load `animations.css` with `media="(prefers-reduced-motion: no-preference)"`, listen to `matchMedia('(prefers-reduced-motion: reduce)')` change events to stop JS animations, use `<picture><source media="(prefers-reduced-motion: no-preference)">` to serve animated images only when allowed — [web.dev, Thomas Steiner (2019)](https://web.dev/articles/prefers-reduced-motion)
- Users with vestibular disorders can experience dizziness, nausea and migraines from motion — [web.dev](https://web.dev/articles/prefers-reduced-motion)
- WCAG 2.2 SC 2.2.2 Pause, Stop, Hide (Level A): moving/auto-updating content that starts automatically, lasts >5 s and is shown with other content needs a mechanism to pause/stop/hide — applies to ambient hero video and carousels — [W3C Understanding 2.2.2](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html) (spec, not fetched this session)

### Inferences (synthesized tokens and snippets)
```css
:root{
  /* spacing scale (8px base) */
  --s-1:4px; --s0:8px; --s1:16px; --s2:24px; --s3:32px; --s4:48px; --s5:64px; --s6:96px; --s7:128px; --s8:192px;
  /* easing */
  --ease-out: cubic-bezier(.22,1,.36,1);      /* easeOutQuint-like: luxury reveals */
  --ease-std: cubic-bezier(.2,0,0,1);         /* functional UI */
  --ease-swiss: cubic-bezier(.65,0,.35,1);    /* crisp in-out for wipes */
}
/* Minimal: 150–250ms hover, opacity/colour only */
.min a, .min button{transition:color .2s var(--ease-std), background-color .2s var(--ease-std), opacity .2s;}
/* Swiss: instant or 120–200ms, hard state changes (invert colours), mask/clip wipes 400–600ms */
.swiss .row:hover{background:#000;color:#fff;}            /* no transition or .12s */
/* Luxury: 300–500ms hovers, 800–1200ms reveals, image zoom scale 1.03–1.05 over 1.2–1.6s */
.lux .img{overflow:hidden}
.lux .img img{transition:transform 1.4s var(--ease-out)}
.lux .img:hover img{transform:scale(1.04)}
.lux .link{background:linear-gradient(currentColor,currentColor) 0 100%/0 1px no-repeat;transition:background-size .5s var(--ease-out)}
.lux .link:hover,.lux .link:focus-visible{background-size:100% 1px}

/* Reveal-on-scroll, gated */
@media (prefers-reduced-motion: no-preference){
  .reveal{opacity:0;transform:translateY(24px);transition:opacity .9s var(--ease-out),transform .9s var(--ease-out)}
  .reveal.is-in{opacity:1;transform:none}
}
@media (prefers-reduced-motion: reduce){
  *,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important;scroll-behavior:auto!important}
}
```
```js
// IntersectionObserver reveal; disabled when reduced motion
const rm = matchMedia('(prefers-reduced-motion: reduce)');
if (!rm.matches) {
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
  }), { rootMargin: '0px 0px -10% 0px', threshold: 0.1 });
  document.querySelectorAll('.reveal').forEach(el => io.observe(el));
} else document.querySelectorAll('.reveal').forEach(el => el.classList.add('is-in'));
```
- Ensure `.reveal` content is visible without JS (add `.js` class on `<html>` and scope hidden state to `.js .reveal`).
- Border widths: minimal 1px hairlines; Swiss 1px (dense) or 2–4px (poster rules); luxury 1px or 0.5px.
- Sticky header shrink/colour change on scroll: use `IntersectionObserver` on a sentinel rather than scroll listeners.
- Luxury hero video: `<video autoplay muted loop playsinline poster>` + visible pause button (WCAG 2.2.2); don't autoplay when `reduce`.
- Avoid scroll-jacking/smooth-scroll libraries by default; if used (luxury), disable under `reduce` and keep native keyboard scrolling.
- Swiss signature effects: text marquee (gate with reduced motion + pause), hover row inversion in index lists, `mix-blend-mode: difference` cursor/labels, clip-path image wipes.
- Optional modern CSS: `animation-timeline: view()` scroll-driven reveals (progressive enhancement; check browser support, Firefox support was behind flag as of the researcher's knowledge — verify), View Transitions API for page fades on static multi-page sites (`@view-transition { navigation: auto; }`) — gate both with reduced motion.

### Gaps
- No source gave concrete durations/easing for any style; all values are synthesized. Browser-support status of scroll-driven animations and cross-document view transitions in late 2026 was not verified in this session.

---

## Q8. Accessibility pitfalls and fixes; performance notes

### Takeaway
Typical failures: minimal → invisible signifiers, hidden nav, low-contrast greys; Swiss → huge tight display type overflowing on mobile, colour-only meaning (red), dense small mono text; luxury → low-contrast thin serif/grey text, tiny tracked caps, autoplay video without pause, heavy media hurting load times, mystery-meat icons. Fixes: strong signifiers (NN/g), WCAG 2.2 AA contrast/target size/focus, reduced-motion gating (web.dev), pause controls.

### Cited Findings
- Visual-only minimalism that hides important elements can "increas[e] complexity rather than reducing it"; rigid adherence causes "wastefully low information density" and poor findability/discoverability; Windows 8 cited as cautionary tale — [NN/g](https://www.nngroup.com/articles/roots-minimalism-web-design/)
- Weak signifiers → 22% longer task time, 25% more fixations; in the Brilliant Earth case 86% of strong-version vs 50% of weak-version participants went from heading to target link; caution with "ultraflat" designs on content-heavy or unfamiliar layouts — [NN/g](https://www.nngroup.com/articles/flat-ui-less-attention-cause-uncertainty/)
- Bodoni falls apart at small sizes on screen ("Don't use Bodoni at 12pt") — [Cedilla Studio](https://www.cedilla.studio/blog/free-luxury-fonts)
- Luxury sites should have smooth scrolling and "instantaneous loading times" — [KIJO](https://kijo.london/blog/luxury-website-design)
- Reduced-motion media query and JS patterns; vestibular symptoms — [web.dev](https://web.dev/articles/prefers-reduced-motion)
- WCAG 2.2 AA references (spec, not fetched this session): 1.4.3 contrast — [W3C](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html); 1.4.11 non-text contrast — [W3C](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html); 1.4.12 text spacing — [W3C](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html); 2.2.2 pause/stop/hide — [W3C](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html); 2.4.11 Focus Not Obscured (Minimum, AA, new in 2.2 — sticky headers must not fully hide focused elements) — [W3C](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html); 2.5.8 target size 24×24 — [W3C](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)

### Inferences (synthesized checklist)
- **All styles**: visible `:focus-visible` outline (2px solid `--fg` or accent, `outline-offset: 3px`) — never remove outlines for "cleanliness"; `scroll-padding-top` equal to sticky header height (2.4.11); skip link; semantic landmarks; `alt` text for editorial images; respect 200% zoom/reflow at 320px (1.4.10).
- **Minimal**: keep primary nav visible on desktop; underline links; buttons need shape/fill, not text alone; muted grey text ≥ `#767676` on white (4.5:1).
- **Swiss**: use `clamp()` + `overflow-wrap: anywhere`/`hyphens: auto` (with `lang`) for giant headlines so they don't overflow at 320px; don't encode meaning only in red; mono metadata ≥12px; tables/indices built as real `<table>` or lists; text-over-photo needs a scrim.
- **Luxury**: no light weights (<300) for body; serif body ≥18px; uppercase labels ≥12px with `letter-spacing` ≤0.2em (WCAG 1.4.12 must still work); text over hero video needs gradient scrim (`linear-gradient(to top, rgba(0,0,0,.55), transparent 60%)`); pause button on video; "Price upon request"/gated content must still be keyboard-reachable; avoid icon-only nav.
- **Performance**: hero image as AVIF/WebP with `srcset`/`sizes`, `fetchpriority="high"` on LCP image, `loading="lazy"` below fold, explicit `width/height` or `aspect-ratio` to prevent CLS; hero video ≤2–4 MB, H.264/AV1, poster image, `preload="none"` or `metadata`; fonts WOFF2-subset, ≤2–3 files preloaded; minimal/Swiss sites should comfortably hit LCP <2.5s, CLS <0.1, INP <200ms (Core Web Vitals "good" thresholds — from general knowledge, see web.dev/vitals).

### Gaps
- No source measured accessibility or performance of luxury sites specifically. Core Web Vitals thresholds cited from general knowledge (web.dev/articles/vitals), not fetched this session.

---

## Q9. Best-fit brands/industries, poor fits, anti-patterns and common mistakes

### Takeaway
NN/g: choose minimalism only if it fits site, brand and content; flat/minimal works best with low information density and conventional layouts. Luxury sources: mass-market cues ("Shop Now", clutter, discount banners) undermine luxury. Swiss suits information-heavy, cultural, architectural and tech-adjacent brands; it looks generic when reduced to "Helvetica + grid" without scale contrast.

### Cited Findings
- Decide whether minimalism fits the site, brand and content; focus on user tasks rather than just cutting features; don't rely on visual minimalism alone — [NN/g](https://www.nngroup.com/articles/roots-minimalism-web-design/)
- Flat designs work best with low information density, traditional/consistent layout, standout interactive elements; caution for content-heavy sites — [NN/g](https://www.nngroup.com/articles/flat-ui-less-attention-cause-uncertainty/)
- Luxury: subtle CTAs like "Request a Consultation" vs mass-market "Shop Now"; personalised, concierge-like checkout; exclusivity cues — [IIAD](https://www.iiad.edu.in/the-circle/why-some-websites-just-feel-expensive/)
- Playfair Display is so widely used it may feel less distinctive; avoid stacking two serifs — [Cedilla Studio](https://www.cedilla.studio/blog/free-luxury-fonts)
- Swiss: "The grid system is an aid, not a guarantee" (Müller-Brockmann) — [UX Planet](https://uxplanet.org/swiss-style-web-design-everything-you-need-to-know-2b128fd327b9)

### Inferences (synthesized)
**Minimalist** — Best: architecture, interior, ceramics, skincare, wellness, SaaS, portfolios, single-product launches, Berlin-style SMB services. Poor: large catalogues/marketplaces, news, government portals, discount retail, children's brands. Anti-patterns: "empty template" look (centred H1 + stock photo + 3 icon cards); hidden nav on desktop; grey-on-grey low-contrast text; removing labels from icons; giant whitespace with no hierarchy; everything same size/weight.

**Swiss** — Best: museums, galleries, festivals, architecture, design studios, type foundries, publishers, conferences, research, engineering/tech brands, Swiss/German B2B. Poor: romantic/emotional consumer brands (weddings, kids), luxury heritage (unless editorial), food comfort brands. Anti-patterns: Helvetica-ish font + 12-col grid but no scale contrast (looks like a Bootstrap template); centred text; decorative gradients/shadows/rounded cards; random asymmetry not tied to columns; red used everywhere; oversized type that breaks on mobile.

**Luxury** — Best: fashion, leather goods, jewellery/watches, fragrance/beauty premium, boutique hotels/spas, fine dining, premium real estate, automotive, handmade artisanal brands. Poor: discount/value retail, utilitarian SaaS, public services, high-SKU marketplaces needing dense filtering. Anti-patterns: gold gradients + script fonts + black (reads as cheap "luxury template"); Playfair+Montserrat default; too many fonts; stock photography; urgency/discount banners, pop-ups, countdowns; "Shop Now!" loud buttons; cluttered mega-menus; low-res or inconsistent product photography; autoplay sound; slow-loading video heroes; motion everywhere (fast, bouncy easings).

### Gaps
- No empirical source (conversion/usability study) on luxury-specific anti-patterns; listed items are synthesized from agency consensus and design practice.

---

## Q10. Real, current (2023–2026) example websites and authoritative articles

### Takeaway
Verified via 2025–2026 sources in this session: luxury/minimal-luxury examples from Limely (2026) and IIAD (2025); recent minimal examples from Minimal Gallery's live feed (Oct 2026). Swiss-style live examples could not be verified from galleries in this session (Siteinspire/Awwwards pages returned no listings); candidate examples are flagged as unverified.

### Cited Findings
**Luxury / minimal-luxury (featured in 2025–2026 articles)**
- The Row — https://www.therow.com/en-gb (minimal navigation, simple grids, craftsmanship focus) — [Limely 2026](https://www.limely.co.uk/blog/top-10-minimalist-luxury-ecommerce-websites)
- Aesop — https://www.aesop.com/ (refined consistent typography, distinctive photography and video) — [Limely 2026](https://www.limely.co.uk/blog/top-10-minimalist-luxury-ecommerce-websites)
- Totême — https://int.toteme.com/ (spacious, curated uncluttered grids) — [Limely 2026](https://www.limely.co.uk/blog/top-10-minimalist-luxury-ecommerce-websites)
- Chanel — https://www.chanel.com/gb/ ; Fendi — https://www.fendi.com/gb-en/ ; Abask (editorial collage) — https://www.abask.com/ ; DeMellier — https://demellierlondon.com/ ; Rêve En Vert — https://reve-en-vert.com/ ; COS — https://www.cos.com/en-gb ; Arket — https://www.arket.com/en-gb/ — [Limely 2026](https://www.limely.co.uk/blog/top-10-minimalist-luxury-ecommerce-websites)
- Hermès — https://www.hermes.com/us/en/ (generous negative space) — [IIAD 2025](https://www.iiad.edu.in/the-circle/why-some-websites-just-feel-expensive/)
- Hospitality luxury examples: ESPA Life at Corinthia — https://espalifeatcorinthia.com/ ; Crown Pavilions — https://www.crownpavilions.com/ — [KIJO 2024](https://kijo.london/blog/luxury-website-design)

**Minimalist (Minimal Gallery feed, Sept–Oct 2026)** — [Minimal Gallery](https://minimal.gallery/)
- Union Boulangerie — https://unionboulangerie.com/en/ (bakery; warm-minimal candidate)
- Odyssee Clinic — https://www.odysseeclinic.com.au/ (clinic/wellness)
- Flowlife — https://www.flowlife.com/
- Spek — https://spek.app/ (app/product minimal)
- Unify — https://www.unifygtm.com/ (SaaS functional minimal)
- How&How — https://how.studio/ ; GRNDWRK STUDIO — https://grndwrk.studio/ ; Grafik — https://grafik.nz/ (studio/agency minimal; possible Swiss-leaning)
- Note: Minimal Gallery does not tag sub-styles per entry; sub-variant fit above is the researcher's guess from names, not inspected.

**Authoritative articles/guides**
- NN/g — The Roots of Minimalism in Web Design (2015): https://www.nngroup.com/articles/roots-minimalism-web-design/
- NN/g — Flat UI Elements Attract Less Attention and Cause Uncertainty (2017): https://www.nngroup.com/articles/flat-ui-less-attention-cause-uncertainty/
- Wikipedia — International Typographic Style: https://en.wikipedia.org/wiki/International_Typographic_Style
- Justinmind / UX Planet — Swiss style web design (2018, older practice): https://uxplanet.org/swiss-style-web-design-everything-you-need-to-know-2b128fd327b9
- Tilda — Swiss style in web design (2022): https://blog-en.tilda.cc/tpost/zsxaujziu1-swiss-style-in-web-design
- IIAD — The UI/UX of Luxury (2025): https://www.iiad.edu.in/the-circle/why-some-websites-just-feel-expensive/
- KIJO — Luxury website design principles (2024): https://kijo.london/blog/luxury-website-design
- Cedilla — Free luxury fonts (2025/2026): https://www.cedilla.studio/blog/free-luxury-fonts
- web.dev — prefers-reduced-motion (2019, still current API): https://web.dev/articles/prefers-reduced-motion

### Inferences
- Swiss candidates for the catalog (well-known Swiss-modernist web presences; **NOT verified live in this session** — check before publishing): Grilli Type (grillitype.com), Dinamo (abcdinamo.com), Museum für Gestaltung Zürich (museum-gestaltung.ch), Swiss Design Awards (swissdesignawards.ch), Experimental Jetset (experimentaljetset.nl). Functional-minimal candidates (also unverified this session): linear.app, vercel.com.
- The luxury list doubles as a quiet-luxury reference set (The Row, Totême, COS/Arket at premium-accessible end) vs heritage maison (Hermès, Chanel, Fendi) vs editorial (Abask).

### Gaps
- Siteinspire and Awwwards collection pages returned no parsable listings; no gallery-verified Swiss-style examples from 2023–2026 were obtained.
- Typewolf, Fonts In Use, Godly, Land-book were not read (tool-call budget).
- Older sources flagged: UX Planet/Justinmind (2018), NN/g (2015, 2017), web.dev (2019) — principles remain valid but examples/fonts in them are dated.
