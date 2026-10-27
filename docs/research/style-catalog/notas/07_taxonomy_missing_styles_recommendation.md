# Cross-cutting: Style taxonomy, missing styles, and style recommendation for an AI website-generation skill

Research date: 2026-10-21. Older sources are marked "(older)" where the year matters. Anything not backed by a fetched source is marked **[Synthesized]** or placed under Gaps.

---

## Q1. How do galleries and taxonomies classify web design styles, and what multi-axis structure should the catalog use?

### Takeaway
No major gallery uses a pure "visual style" taxonomy. Awwwards and Siteinspire mix industry or category, visual-style tags, layout tags, interaction tags, and technology into separate filter facets. Our list of 18 mixes these axes in the same way, so the catalog should be split into orthogonal facets: visual style is the primary choice, and layout pattern, interaction/motion, surface effect, and industry fit are modifiers.

### Cited Findings
- **Awwwards** separates browsing into distinct facets: **Category** (mostly industry or site type, e.g. Architecture, E-Commerce, Fashion, Luxury, Magazine/Newspaper/Blog, Startups, Technology, Experimental, Promotional), **Tag** (a mix of visual style, layout, and interaction, e.g. *Clean, Colorful, Minimal, Flat Design, Retro, Illustration, Photographic, Typography, Vector, Big Background Images, Fullscreen, Horizontal Layout, Single page, Infinite Scroll, Parallax, Microinteractions, Transitions, Unusual Navigation, Storytelling, Sound-Audio, 3D, Data Visualization*), **Technology** (e.g. WebGL, Three.js, GSAP, Lottie, Locomotive Scroll, Framer, Webflow), **Font**, and **Color** (hex swatches). Its "Trending" menu also lists *Animated websites, Scrolling, One page design*. — [Awwwards websites directory](https://www.awwwards.com/websites/)
- So Awwwards treats "Minimal / Flat / Retro / Illustration / Typography" (visual style), "Horizontal Layout / Single page / Fullscreen" (layout), and "Parallax / Microinteractions / Transitions / Scrolling / Animation" (interaction) as peers in one flat tag list, and keeps industry and technology as separate facets. — [Awwwards](https://www.awwwards.com/websites/)
- **Siteinspire** filters on four facets: **Styles, Types, Subjects, Platforms**. Its popular categories mix style values (*Typographic, Minimal*), layout values (*Grid Layout, Unusual Layout*), site types (*Portfolio, E-Commerce*), and subjects (*Fashion, Art, Photography, Agencies & Consultancies, Design & Art Direction*). Platforms covers build technology (Webflow, WordPress, Framer, Shopify). — [Siteinspire](https://www.siteinspire.com/); [Lazyweb comparison page describing Siteinspire filters](https://experiments.lazyweb.com/vs/siteinspire.md)
- Siteinspire listing counts (as shown on the homepage on the research date): Typographic 2,105; Minimal 847; Grid Layout 672; Unusual Layout 671. This suggests typographic and minimal are the dominant "curated-quality" visual idioms. — [Siteinspire](https://www.siteinspire.com/)
- Trend reports mix axes too. Figma's "Top web design trends for 2026" lists visual styles (Neumorphism, Retrofuturism, Maximalism, Collage, Neo-brutalism/"anti-design"), color and type choices (Vibrant palettes, Bold typography, Dark mode), interaction (Motion design, Experimental navigation, Gamified design, 3D/immersive), and a production value (Sustainable web design). — [Figma Resource Library: Web design trends](https://www.figma.com/resource-library/web-design-trends/) (undated; refers to 2026 as "around the corner", so late 2025)
- Academic aesthetics research gives two higher-order axes that sit above individual styles. Lavie & Tractinsky's **classical aesthetics** (clean, clear, organized, symmetrical, pleasant, aesthetic) and **expressive aesthetics** (creative, original, fascinating, sophisticated, use of special effects). — [Anthony Hobday summary of Lavie & Tractinsky](https://anthonyhobday.com/blog/20221005.html); [Noam Tractinsky publications, BGU](https://www.bgu.ac.il/en/researcher/noam-tractinsky/publications/327435009/) (older: original paper 2004, IJHCS)
- Google/Basel research identifies **visual complexity** and **prototypicality** (how typical a site looks for its category) as the two factors behind fast aesthetic judgments. These are measurable, continuous axes along which any style can be placed. — [Google Research blog, 2012](https://research.google/blog/users-love-simple-and-familiar-designs-why-websites-need-to-make-a-great-first-impression/); [Tuch et al. paper, Google Research](https://research.google/pubs/the-role-of-visual-complexity-and-prototypicality-regarding-first-impression-of-websites-working-towards-understanding-aesthetic-judgments/) (older: 2012)

### Inferences
- **[Synthesized] Reclassifying our 18.**
  - **Visual style / aesthetic** (the primary pick): Minimalist, Swiss/International, Editorial/magazine, Brutalist, Neo-brutalist, Retro/vintage, Y2K, Maximalist, Organic/natural, Luxury/elegant, Dark/tech, Collage/scrapbook.
  - **Surface/material effect** (applied on top of a style): Glassmorphism, Neumorphism, Claymorphism/soft 3D.
  - **Layout pattern**: Bento grid. "Editorial" is partly a layout too, since it implies a magazine grid.
  - **Interaction/motion pattern**: Kinetic typography, Immersive/3D scroll.
  - "Dark/tech" is half a color mode and half a style. Better to split it into a dark-mode toggle (any style) and a "Tech/futurist" or "Cyberpunk/neon" style.
- **[Synthesized] Recommended catalog schema**, with each entry tagged on all facets:
  1. `aesthetic` (one primary, optional secondary): the "style family" the user chooses.
  2. `layout`: e.g. single-column narrative, editorial grid, bento/modular grid, split-screen, full-bleed hero, horizontal scroll, asymmetric/broken grid, card list, sidebar/docs.
  3. `surface`: flat, glass/translucent, soft-extruded (neumorphic), clay/3D-soft, grain/noise, paper/texture, gradient-mesh/aurora, duotone.
  4. `motion`: none/static, micro-interactions, scroll-reveal, parallax, kinetic type, scroll-driven 3D/WebGL, page transitions.
  5. `type_system`: grotesk/neo-grotesk, serif editorial, display/expressive, mono, handwritten/script.
  6. `color_mode`: light/dark/both, plus palette character (muted, vivid, monochrome, pastel, neon).
  7. Measurable dials taken from the research: `complexity` (low→high), `prototypicality` (conventional→experimental), `classical↔expressive`.
  8. Fit metadata: industries, price positioning, content type (photo-led, text-led, app/SaaS), brand-personality fit, accessibility risk level, performance cost.
- This mirrors how Awwwards keeps Category, Tag, and Technology separate. It also lets the skill combine values (e.g. Luxury aesthetic + editorial grid + flat surface + slow scroll-reveal) instead of multiplying near-duplicate styles.

### Gaps
- **Godly, Land-book, Dribbble, and Behance taxonomies were not verified.** The searches returned no usable pages, and I did not fetch their filter lists, so their facets cannot be cited.
- The full Siteinspire value lists for Styles, Types, and Subjects were not shown in the fetched page. Only the "popular categories" were visible.

---

## Q2. Which notable styles/aesthetics are missing from our list of 18?

### Takeaway
The most defensible additions are: **Flat/Material**, **Skeuomorphism/tactile realism**, **Bauhaus/geometric**, **Art Deco**, **Memphis** (and the separate *Corporate Memphis* illustration style), **Scandinavian/Japandi**, **Japanese/Wabi-sabi**, **Cyberpunk/neon** (and **Retrofuturism**), **Illustrative/hand-drawn**, **Anti-design/chaotic**, **Monochrome**, **Typographic-led**, and **Liquid Glass** as a 2025–26 surface effect. **Aurora/gradient mesh**, **Grainy gradients**, and **Duotone** are surfaces or treatments, not styles. **3D/WebGL product** is an interaction/media pattern.

### Cited Findings
- **Retrofuturism** (vintage visions of the future with neon, chrome, and pixel art) is named a 2026 web trend by Figma. — [Figma web design trends](https://www.figma.com/resource-library/web-design-trends/)
- Envato's Creative Trends 2026 names **Retro futurism** (marketplace searches for "neon lights" graphics +200% over 4 weeks), **Chaos packaging** (distorted, warped visuals; "distorted" searches +45% over 12 weeks; "graffiti" +13%), and **Dual aesthetics** ("experimental" textured graphics +61% over 4 weeks). These numbers are Envato marketplace search activity, not market-wide data. — [Campaign Brief, 16 Dec 2025](https://campaignbrief.com/?p=305818)
- Adobe Express's "Design trends for 2026" (12 Dec 2025) names tactile, sensory design with "puffy, soft textures and hyper-realistic objects" (supports **Skeuomorphism/tactile** and **Claymorphism**), "exaggerated, playful letters" (supports **Typographic-led / expressive type**), **Surreal/absurdist imagery**, **Organic and imperfect design** (hand-rendered and letterpress fonts, earthy textures), **Freeform zine-style layouts**, **Local and cultural flavor** (heritage patterns, regional typography), **Collage**, and **Maximalist/chaotic layouts**. — [Adobe Express, Design trends for 2026](https://www.adobe.com/express/learn/blog/design-trends-2026)
- Figma's 2026 list also includes **Neo-brutalism ("anti-design")**, **Maximalism**, **Collage**, **Neumorphism**, **Vibrant/neon gradients**, **Bold typography**, **Dark mode**, **3D and immersive**, and **Experimental navigation**. — [Figma](https://www.figma.com/resource-library/web-design-trends/)
- **Flat Design**, **Retro**, **Illustration**, **Vector**, **Minimal**, **Typography**, **Photographic**, and **Colorful** are standing tags on Awwwards. Flat design remains a catalogued category. — [Awwwards](https://www.awwwards.com/websites/)
- **Corporate Memphis (Alegria)**: flat, solid bright colors, cartoon figures with elastic limbs and small heads. Popularized when Facebook adopted it in 2017 (reportedly created at Buck). By 2022 companies were moving back toward 3D-like styles, and by 2023 its popularity had fallen and it was often used as parody. Named after the 1980s Memphis Group. — [Wikipedia: Corporate Memphis](https://en.wikipedia.org/wiki/Corporate_Memphis); see also [Creative Bloq, "Corporate Memphis style is dead"](https://creativebloq.com/news/corporate-memphis-style-is-dead)
- **Liquid Glass** is Apple's iOS 26 visual language (2025): translucent, refractive, constantly animating controls. NN/g's Raluca Budiu (10 Oct 2025) criticizes it for lost contrast over busy backgrounds, nearly invisible pale controls, purposeless motion ("Motion for motion's sake is not usability"), and smaller, crowded touch targets. — [NN/g, "Liquid Glass Is Cracked, and Usability Suffers in iOS 26"](https://www.nngroup.com/articles/liquid-glass/)
- **Neumorphism** has a documented accessibility problem. Low-contrast shadows make buttons blend into the background, and states (pressed or active) are unclear. Michal Malewicz, who popularized the term, suggests using it only for cards, never for essential controls. — [Built In, 3 Mar 2020](https://builtin.com/design-ux/neumorphism-accessibility) (older)

### Candidate additions **[Synthesized]**

Definitions are standard design vocabulary. Relevance notes rely on the cited trend sources where marked; otherwise they are my judgment.

| Candidate | One-line definition | Relevance 2024–26 | Axis |
|---|---|---|---|
| Flat / Material | Solid colors, no textures, simple shapes and icons; Material adds layered "paper" elevation and motion rules | Evergreen baseline for SaaS and apps; Awwwards "Flat Design" tag | Style (baseline) |
| Skeuomorphism / tactile realism | Interface mimics real materials (leather, metal, paper, buttons) | Returning as "tactile" and "hyper-realistic objects" (Adobe 2026) | Style + surface |
| Bauhaus / geometric | Primary colors, circles, squares, triangles, strict geometry, sans type | Niche but steady for art, culture, and design studios | Style |
| Art Deco | Symmetry, gold and black, stepped geometric ornament, high-contrast display serifs | Hospitality, bars, events, luxury heritage | Style (a luxury sub-style) |
| Memphis (1980s) | Clashing brights, squiggles, confetti shapes, terrazzo patterns | Playful brands, youth, events | Style |
| Corporate Memphis / Alegria | Flat cartoon people with elastic limbs, bright skin tones | Declining and used as parody since 2023 (Wikipedia). Include only as an "avoid / legacy" reference | Illustration style |
| Scandinavian / Japandi | Light neutrals, natural wood tones, generous whitespace, soft sans, warm minimalism | Interiors, furniture, wellness, D2C home | Style (a warm-minimal sub-style) |
| Japanese / Wabi-sabi | Asymmetry, imperfection, natural textures, quiet negative space, sometimes vertical type | Fits "organic and imperfect" (Adobe 2026); crafts, ceramics, tea, spa | Style |
| Cyberpunk / neon | Dark backgrounds, neon magenta and cyan, glitch, HUD elements, mono type | Retrofuturism and neon search spikes (Figma, Envato 2026); gaming, web3, music | Style |
| Retrofuturism | Vintage-future: chrome, neon, pixel, space-age curves | Named 2026 trend (Figma, Envato) | Style (distinct from Y2K and Retro) |
| Illustrative / hand-drawn | Custom illustration or doodles lead the page; handwritten type | Adobe 2026 "organic and imperfect", "collage... doodles" | Style |
| Anti-design / chaotic | Deliberately breaks grids, clashes, distorts; overlaps Brutalist | Envato "Chaos packaging", Figma neo-brutalism as "anti-design" | Style (extreme end of Brutalist) |
| Typographic-led / Swiss-punk | Type is the main visual; huge display type; Swiss-punk adds disruption to Swiss grids | Siteinspire "Typographic" is its largest style category; Adobe 2026 "exaggerated letters" | Style |
| Monochrome | Single hue or black and white with tonal variation | Evergreen for portfolios and fashion | Palette treatment (works across styles) |
| Duotone | Images or graphics mapped to two colors | Treatment | Surface/image treatment |
| Grainy gradients / noise | Soft gradients with film grain or noise | Treatment, often paired with aurora | Surface |
| Aurora / gradient mesh | Blurred, glowing multi-color mesh gradients as background | Common in AI and SaaS landing pages; overlaps "vibrant neon gradients" (Figma) | Surface |
| Liquid Glass | Refractive, dynamic translucent material (Apple 2025) | High awareness from 2025; strong usability caveats (NN/g) | Surface (an evolution of glassmorphism) |
| 3D / WebGL product | Real-time 3D product as hero (spin, configure) | Figma 2026 "3D and immersive"; Awwwards WebGL/Three.js tech | Interaction/media pattern |
| Surreal / absurdist | Dreamlike scale shifts, visual jokes, impossible objects | Adobe 2026 | Imagery direction (a modifier) |
| Cultural / heritage-local | Regional patterns, typography, and candid local photography | Adobe 2026 "Local and cultural flavor" | Style modifier |
| Zine / freeform | Loose, overlapping, asymmetric zine compositions | Adobe 2026 | Layout + style (close to Collage) |
| Gamified / playful UI | Points, badges, streaks, playful micro-interactions | Figma 2026 | Interaction pattern |

### Inferences
- **[Synthesized]** Priority additions as primary aesthetics: Flat/Material (needed as the "safe default"), Typographic-led, Illustrative/hand-drawn, Cyberpunk/Retrofuturism (both have 2026 trend signal), Scandinavian/Japandi (warm minimal), Wabi-sabi/Japanese, Art Deco, Bauhaus, Memphis, Skeuomorphic/tactile.
- **[Synthesized]** Model as surfaces/modifiers instead of styles: Aurora/mesh, Grain, Duotone, Monochrome, Liquid Glass, plus our existing Glass, Neu, and Clay.
- **[Synthesized]** Corporate Memphis should be a known anti-pattern ("dated 2017–2022 tech look"), not something the skill recommends by default.
- **[Synthesized]** "Anti-design" can be the high-expressiveness end of the Brutalist family instead of a separate entry, unless the skill wants a "chaos" option.

### Gaps
- No quantitative cross-gallery prevalence data for each candidate style was found. The Envato numbers are marketplace-internal search counts only.
- There is no fetched primary source defining Japandi, Swiss-punk, or Aurora UI. The definitions above are synthesized from general design vocabulary.

---

## Q3. How do designers and brand strategists map brand attributes to a visual style?

### Takeaway
Established practice moves from **words to visuals**. Collect brand adjectives (semantic differentials, metaphor questions, personality dimensions), cluster them into 2–3 themes, and present 2–3 **lightweight visual directions** (style tiles, mood boards) for the client to pick or merge, before any full mockups. Squarespace Blueprint productizes exactly this with seven brand personalities, each mapped to palettes and font pairs.

### Cited Findings
- **Style tiles (Samantha Warren, 2012)**: "a design deliverable that references website interface elements through font, color, and style collections" (older). — [A List Apart, "Style Tiles and How They Work", 27 Mar 2012](https://alistapart.com/article/style-tiles-and-how-they-work)
  - Process: (1) stakeholders list and rate visual goals; (2) **gather adjectives** through surveys and kickoff, using **metaphor questions** (e.g. "what vehicle would the site be?") and **semantic differential word pairs** (e.g. modern vs. old-fashioned), often with example sites; (3) find the most frequent adjectives and themes; (4) **present three tiles**. In the Washington Examiner case these were based on "clean", "strong", and "friendly". Stakeholders then combined elements into one approved tile. — [A List Apart](https://alistapart.com/article/style-tiles-and-how-they-work)
  - Style tiles are "more refined than a traditional identity mood board". Mood boards are often too vague for a web system. Presenting several full comps leads clients to mix and match into a "Frankencomp". — [A List Apart](https://alistapart.com/article/style-tiles-and-how-they-work)
- **Aaker's brand personality framework (1997)** has five dimensions: Sincerity, Excitement, Competence, Sophistication, Ruggedness. It is the standard academic scale for brand personality (older but canonical). — [Aaker 1997, "Dimensions of Brand Personality", Journal of Marketing Research (PDF)](https://gwern.net/doc/economics/1997-aaker.pdf)
- **Squarespace Blueprint AI** asks the user to pick one of **seven brand personalities**: Professional, Playful, Sophisticated, Friendly, Bold, Quirky, Innovative. Palettes are grouped by personality (four color schemes each), and each personality has **two font pairings (14 total)**, with a live preview as the user clicks through. — [Website Builder Expert, updated 30 May 2025](https://www.websitebuilderexpert.com/website-builders/squarespace-blueprint-ai/)
- **Relume** generates style "concepts" (colors, typography, UI element styling, homepage images) after the sitemap and wireframe stage. It offers a "surprise me" button for alternative directions, shuffling of colors, type, or UI while locking other parts, and a **Pitch Concepts** mode that presents the **top 3 concepts** to clients with short descriptions. — [Relume docs: Concept creation using the Style Guide builder](https://resources.relume.io/resources/docs/concept-creation-using-the-relume-style-guide-builder)
- **Classical vs. expressive aesthetics** (Lavie & Tractinsky) is a validated word-to-visual bridge. Classical adjectives (clean, clear, organized, symmetrical) map to restrained styles, and expressive adjectives (creative, original, fascinating, special effects) map to bold or experimental styles. — [Hobday summary](https://anthonyhobday.com/blog/20221005.html)
- **Audience demographics shift preferred complexity and colorfulness.** Across 2.4M ratings from about 40,000 participants: women liked colorful sites more than men; higher education lowered the preference for colorfulness; Russians preferred lower visual complexity; Macedonians liked highly colorful designs most (older: 2014). — [Reinecke & Gajos, CHI 2014](https://eecs.harvard.edu/~kgajos/papers/2014/reinecke14visual.shtml)
- **Prototypicality depends on category.** Sites that look atypical for their category are rated uglier even when simple. A style's acceptability therefore depends on industry conventions. — [Google Research blog, 2012](https://research.google/blog/users-love-simple-and-familiar-designs-why-websites-need-to-make-a-great-first-impression/)

### Inferences
- **[Synthesized] A recommendation pipeline for the skill that mirrors agency practice:**
  1. **Extract signals** from the minimal input:
     - From a photo: dominant palette, material and texture, lighting mood, product category, implied price tier.
     - From a phrase: adjectives, tone.
     - From a brand idea: audience, category, positioning.
  2. **Map them onto a small set of dials**: Aaker dimension (or Squarespace-style personality), classical↔expressive, complexity (low↔high), prototypicality (conventional↔experimental), warmth (cool/tech↔warm/organic), price tier (mass↔premium), content type (photo-led / text-led / app-SaaS).
  3. **Score each catalog style** against these dials using its fit metadata, and apply an industry-convention penalty for styles that are too atypical for the category.
  4. **Present three directions**, following Warren's three tiles and Relume's top-3 pitch: one **safe/prototypical** fit, one **on-brand-expressive** fit, and one **stretch**. Show each as a style-tile-like card (palette, type pair, one UI sample, one hero crop using the user's photo), with a single-sentence rationale tied to the extracted adjectives.
  5. **Allow mixing at the token level**: lock type, shuffle palette, as Relume and Durable do, instead of mixing whole comps. This avoids the "Frankencomp" problem.
- **[Synthesized] Example personality-to-style mapping** (a heuristic, not from a source):
  - Sincerity → Organic/natural, Scandinavian, Illustrative.
  - Excitement → Maximalist, Neo-brutalist, Y2K, Kinetic.
  - Competence → Swiss, Minimal, Flat/Material, Bento (SaaS).
  - Sophistication → Luxury, Editorial, Art Deco, Monochrome.
  - Ruggedness → Brutalist, Retro/vintage workwear, dark textured.
- **[Synthesized] Content type heuristics:**
  - Product-photography-led brands favor low-chrome styles (Minimal, Luxury, Editorial) that let images carry the page.
  - Text-heavy sites favor Editorial or Swiss.
  - App/SaaS favors Flat/Material, Bento, Dark/tech.
  - Glass, Liquid Glass, and Neumorphism should only be secondary surfaces where content density is low.

### Gaps
- I found no published, validated mapping from Aaker dimensions or archetypes to specific web styles. The archetype-to-visual guides surfaced in search (e.g. Tilda Education, Creativeans) are practitioner blogs and were not fetched or verified.
- No primary source on agency "design directions" practice was fetched beyond Warren and Relume. The "present 2–3 directions" norm is supported by those two sources only.

---

## Q4. How do AI website builders pick and offer styles, and what inputs do they ask for?

### Takeaway
Current AI builders take **business and purpose inputs**, not style inputs. They then generate one design and offer **shuffle/regenerate** controls for theme, palette, and fonts. Only Squarespace Blueprint gives an explicit style-choice step (seven personalities). Framer and the coding agents (v0, Lovable, Bolt) rely on free-text style adjectives in the prompt or a knowledge field, and default to a shadcn/Tailwind look. None found presents a named style catalog. That gap is an opportunity.

### Cited Findings
- **Wix AI builder**: a chatbot asks 4–5 questions about the site's purpose, content type, goals, and differentiators. It has no dedicated style question. It then generates a theme described in words, e.g. "modern fonts and a bold, electric design in shades of blue and black". Controls: "Generate new theme", "Shuffle these colors", "Continue with this Design", plus conversational changes (e.g. "pastel", "neon pink"). Only the previous five designs can be reverted to. — [Website Builder Expert, How to use Wix AI, updated 26 Aug 2025](https://www.websitebuilderexpert.com/website-builders/how-use-wix-ai/)
- **Squarespace Blueprint AI**: site title → one of 7 brand personalities → homepage sections (9) → pages (6) → color palette (4 per personality) → font pairing (2 per personality, 14 total) → generated template. — [Website Builder Expert, updated 30 May 2025](https://www.websitebuilderexpert.com/website-builders/squarespace-blueprint-ai/)
- **Durable**: a "Themes" panel ("Here are some theme options", "Generate more", "Confirm theme", "Undo theme") and a "Customize" panel with **Palette** (curated presets, or match from a brand color), **Corners** (sharp → rounded), **Fonts**, and **Shuffle** (remixes palette, corners, and fonts while keeping layout). — [Durable Help Center](https://help.durable.com/en/articles/15199763-designing-your-site-colors-fonts-and-corners)
- **Relume**: style guide concepts come after sitemap and wireframes. AI generates a concept, with "surprise me" for another, shuffle with locks, and present top 3 concepts. — [Relume docs](https://resources.relume.io/resources/docs/concept-creation-using-the-relume-style-guide-builder)
- **Framer AI** (older, 2023): style is set only through the prompt. The recommended prompt has five parts: goal, audience, content/sections, **style/theme/vibe adjectives** (e.g. minimalistic, vibrant, rustic), and extra details (palette, imagery, brand values). — [DesignProject.io, 31 Jul 2023](https://designproject.io/blog/better-framer-ai-prompts/). A 2025–26 update says Framer agents now generate light and dark themes automatically. — [Createwith, Framer updates](https://www.createwith.com/tool/framer/updates/framer-agents-now-generate-light-and-dark-themes-automatically) (not fetched; title only)
- **v0 / Lovable / Bolt**: no style presets. Style comes from a Knowledge/Context field (token lists, plain-language mood description, brand docs), from Tailwind config, or from Figma import. The default stack is React + Tailwind + shadcn/ui + Lucide, and v0 is the most shadcn-opinionated. The "shadcn look" appears when the prompter doesn't customize styles. — [Anna Arteeva, Substack, 8 Jun 2025](https://annaarteeva.substack.com/p/design-systems-lovable-bolt-v0-and)

### Inferences
- **[Synthesized]** Common UX primitives worth copying: (a) a **personality or vibe picker** (Squarespace); (b) **shuffle with locks** at the token level (Relume, Durable); (c) **regenerate / generate more** themes (Wix, Durable); (d) **pitch 3 concepts** (Relume); (e) a **version history** (Wix keeps 5).
- **[Synthesized] Differentiator for our skill**: none of the surveyed builders infers style from a **product photo**, and none exposes **named styles with rationale**. Pairing photo-derived signals with a named catalog and three explained directions would be distinctive.
- **[Synthesized]** Avoid the generic "AI look" by never shipping un-themed shadcn defaults. Each catalog style should define its own token set (type, radius, shadow, color, spacing, motion).

### Gaps
- I did not verify Lovable's or v0's 2026 product features directly (e.g. any newer theme pickers). The cited article is from June 2025.
- No primary docs were fetched for Hostinger AI, 10Web, or Webflow AI site builder.
- No academic research on automated style recommendation for websites was found within budget. Reinecke & Gajos' computational appeal model is the closest: it predicts appeal by demographic group from colorfulness and complexity.

---

## Q5. What does user-perception research say about first impressions, trust, and the risks of each style family?

### Takeaway
Aesthetic judgments form in about **17–50 ms** and stay stable with longer viewing. **Low complexity plus high prototypicality** wins first impressions, and visual design is the most-cited credibility cue. Expressive or trendy styles (brutalist, maximalist, anti-design, immersive 3D) therefore carry first-impression and trust risk outside creative categories. Translucent and soft-shadow surfaces (glass, Liquid Glass, neumorphism) carry documented legibility and accessibility risk.

### Cited Findings
- **Lindgaard et al. 2006**: people judged visual appeal after about **50 ms** exposure, and these snap ratings agreed well with ratings after longer viewing. Published in *Behaviour & Information Technology* 25:115–126 (older). — [Nature News, 13 Jan 2006](https://www.nature.com/news/2006/060109/full/news060109-13.html)
- **Tuch et al. / Google 2012**: aesthetic judgments form within **17–50 ms**. Highly complex sites are rated less beautiful even when familiar, and low-prototypicality sites are rated uglier even when simple. Both factors interact (older). — [Google Research blog](https://research.google/blog/users-love-simple-and-familiar-designs-why-websites-need-to-make-a-great-first-impression/); [paper page](https://research.google/pubs/the-role-of-visual-complexity-and-prototypicality-regarding-first-impression-of-websites-working-towards-understanding-aesthetic-judgments/)
- **Fogg et al. / Stanford & Consumer WebWatch 2002**: **46.1%** of comments about credibility referred to the site's design look. The study had 2,684 participants, 100 sites, and 10 content categories (older). — [ClickZ, 31 Oct 2002](https://clickz.com/study-for-site-cred-looks-matter/56564/)
- **Reinecke & Gajos 2014**: preferences for colorfulness and complexity vary by gender, education, and country (details in Q3). One style does not fit all audiences (older). — [Harvard](https://eecs.harvard.edu/~kgajos/papers/2014/reinecke14visual.shtml)
- **Liquid Glass / translucent surfaces**: contrast is lost over images and text, controls become nearly invisible, motion is purposeless, and touch targets shrink. — [NN/g, 10 Oct 2025](https://www.nngroup.com/articles/liquid-glass/)
- **Neumorphism**: buttons blend into the background, affordances and states are unclear, and it fails users with low vision or low-quality screens. Recommended only for cards, not essential controls (older, 2020). — [Built In](https://builtin.com/design-ux/neumorphism-accessibility)
- **Corporate Memphis**: perceived as generic and parodied by 2023. A credibility and "datedness" risk. — [Wikipedia](https://en.wikipedia.org/wiki/Corporate_Memphis)

### Inferences
- **[Synthesized] Risk profile by style family:**
  - **Low risk**: Minimal, Swiss, Flat/Material, Editorial, Scandinavian. Low complexity, high prototypicality.
  - **Medium risk** (depends on category fit): Luxury, Organic, Retro, Illustrative, Dark/tech, Bento, Art Deco, Japandi.
  - **High risk** (only for creative, youth, fashion, or entertainment categories where atypical is the norm): Brutalist, Neo-brutalist, Maximalist, Anti-design, Y2K, Collage, Cyberpunk, Memphis, Kinetic, Immersive 3D.
  - **Surface risk** (legibility and contrast): Glass, Liquid Glass, Neumorphism, Aurora backgrounds behind text.
  - **Motion risk** (vestibular; needs a `prefers-reduced-motion` fallback): Kinetic, Immersive/3D scroll, Parallax. This is general WCAG/CSS practice, not sourced in this round.
- **[Synthesized]** The recommender should raise the weight of prototypicality for trust-sensitive categories (finance, health, legal, B2B) and lower it for creative categories. The "stretch" direction should carry an explicit trade-off note (e.g. "memorable, but less conventional for fintech").
- **[Synthesized]** Every catalog entry should ship accessibility guardrails, e.g. a minimum contrast for text on glass (solid scrim fallback), visible borders on neumorphic controls, and reduced-motion variants.

### Gaps
- I found no recent (2023–26) peer-reviewed study comparing trust across *named* modern styles (e.g. brutalist vs. minimal). Most evidence is general (complexity, prototypicality) or practitioner critique.
- The full Tuch et al. sample size and effect sizes were not retrieved, because only the blog summary was fetched.
- WCAG references for motion and contrast are general knowledge and were not fetched this round.
