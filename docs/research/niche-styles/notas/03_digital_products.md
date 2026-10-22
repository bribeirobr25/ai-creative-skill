# Digital Products & Tech Websites — Visual Style, Layout & UI/UX by Niche
Niches: (a) SaaS / B2B software, (b) AI tools / startups, (c) mobile apps (app landing pages), (d) online courses, coaches & creator businesses, (e) digital downloads / templates / digital-goods marketplaces, (f) agencies & B2B consultancies.

Research date: 2026-10-22. Scope: visual design, layout, UI/UX only.

How to read reliability: NN/g = strong primary usability research (some of it old, flagged below). Vendor blogs (Kajabi, m3ter, template sellers) = practitioner opinion or secondhand stats. "Observation" = the researcher's own description of live sites from prior knowledge (up to mid-2026), not re-checked live in this session. The report writer should label these as synthesis.

---

## 1. Visitor goals and primary conversion actions per niche (and how the UI supports them)

### Takeaway
Each niche has one dominant conversion action, and the page should be built around a single primary CTA for it: SaaS = "Start free / Get started" plus a secondary "Book a demo"; AI = "Try it" (often an inline prompt box); apps = store download (badges / QR / smart banner); courses = enroll / buy (checkout-only sales page); digital goods = buy / download (product page → short checkout); agencies = "Start a project / Book a call" after browsing work. B2B buyers want enough information (pricing, demos, proof) to shortlist a vendor *without* talking to sales.

### Cited Findings
- **B2B / SaaS:** B2B buyers expect B2C-level usability (Jakob's Law). They worry that sales reps will be pushy, so sites should give information upfront so contact isn't required. Forms should explain why each field is asked. Sites should show at least an email address and phone number, and should offer free trials without a credit card — [NN/g, "B2B trust from B2C", Fessenden, 2019](https://www.nngroup.com/articles/b2b-trust-from-b2c/)
- **B2B / SaaS:** Product demos (screenshots, videos, live demos) help buyers who can't install software without approval — [NN/g 2019](https://www.nngroup.com/articles/b2b-trust-from-b2c/)
- **B2B / SaaS:** Early-stage B2B prospects need only "a general idea of cost levels". The site's job at that stage is to "survive the pruning process" — [NN/g, "Show Prices for Common Scenarios", Nielsen, 2006 — OLD but still cited](https://www.nngroup.com/articles/show-prices-for-common-scenarios/)
- **Linear-style SaaS:** The style uses "few calls to action" and one-dimensional sequential scrolling — [LogRocket, Schwarz, June 2025](https://blog.logrocket.com/ux-design/linear-design)
- **Bento sections:** A bento section should share one primary CTA. Giving every tile its own CTA hurts — [BuildMVPFast opinion piece, July 2026](https://www.buildmvpfast.com/blog/bento-grid-helps-vs-hurts-conversion-2026)
- **Mobile apps:** In the author's own tally of 15 app landing pages, a CTA sat above the fold on 15/15 and a device mockup appeared on 14/15. The source is unsourced and promotional. Its claim that a 5–10% visit→download rate is "average" also has no source — [The Swift Kit, Apr 2026](https://theswiftk.it.com/blog/best-app-landing-page-examples-2026)
- **Courses / creators:** Sales pages should have no navigation; "the only link should lead to checkout". Short-form (<500 words) suits familiar audiences or simple courses, long-form suits complex or premium ones — [Kajabi blog, orig. 2017, updated Jul 2026](https://www.kajabi.com/blog/how-to-create-an-amazing-sales-page-today)
- **Pricing pages:** Removing nav bars on the pricing page is attributed to a Basecamp A/B test with "11–20% higher checkout completion". This is secondhand, unlinked and labeled "directional" by the author — [m3ter, May 2025](https://www.m3ter.com/blog/15-data-driven-pricing-page-optimizations)

### Inferences
- Synthesis, primary action per niche, as a builder default:
  - **SaaS PLG:** "Get started free" (primary) plus "Talk to sales / Book demo" (secondary ghost button), repeated in the header and the final CTA band.
  - **Enterprise B2B:** "Book a demo" as primary. Add a short form with field-justification microcopy, following NN/g.
  - **AI tools:** Put the action *in* the hero, as a prompt input or upload area ("the input is the hero"). Observation: lovable.dev, bolt.new and v0.dev use a chat or prompt box as the hero element. Not verified live this session.
  - **App:** On desktop, show App Store / Google Play badges plus a QR code. On iOS Safari, use the native Smart App Banner rather than custom interstitials. That banner guidance is from general knowledge; the Apple doc could not be fetched (see Gaps).
  - **Course:** Use an "Enroll / Join" button that jumps to the pricing or payment-plan block. The CTA should repeat after each major section.
  - **Digital goods:** Use a "Buy / I want this" button with the price shown on it, a "pay what you want" field where relevant, and an overlay or one-page checkout.
  - **Agency:** The primary conversion follows browsing case studies: "Start a project" leads to a qualifying form (budget, timeline, services) or a calendar booking.

### Gaps
- No rigorous, recent cross-niche benchmark tying a specific primary-CTA layout to conversion rates was found. Most published conversion stats are vendor-secondhand.
- Apple's Smart App Banner documentation page needs JavaScript and could not be fetched, so Apple's exact wording on custom banners was not verified.

---

## 2. Dominant layout and page patterns per niche

### Takeaway
SaaS and AI converge on one skeleton: a centered typographic hero with a product UI screenshot or video → logo wall → bento or alternating feature sections → metrics / testimonials → pricing (3–4 tiers plus a comparison table) → FAQ → final CTA band → mega-footer. Apps replace the product screenshot with device mockups and store badges. Courses use a long-form single-column sales page with a curriculum accordion. Digital-goods sites use a product-page or marketplace-grid pattern. Agencies are portfolio-first: case-study grids or a scroll stream with large type and motion.

### Cited Findings
**(a) SaaS / B2B**
- Linear-style layout: content in one sequential column; no zigzag; consistent text alignment; dark mode; bold type; gradients; glassmorphism — [LogRocket 2025](https://blog.logrocket.com/ux-design/linear-design)
- The bento grid spread across SaaS landing pages around 2024, copied from Apple's 2023 iPhone/AirPods feature pages. It works best *below* a single-message hero, with one dominant anchor tile. Vercel, Stripe, Ramp and Notion are named as shipping bento layouts in 2023–24. Linear and Raycast open with one sentence and one dominant product tile, with the bento grid lower down — [BuildMVPFast, Jul 2026](https://www.buildmvpfast.com/blog/bento-grid-helps-vs-hurts-conversion-2026)
- Bento was "popularized by Apple's summary slides". The layout is compartments, each showcasing one feature, with a clear hierarchy — [SaaSFrame (undated)](https://www.saasframe.io/blog/the-bento-layout-trend)
- Pricing comparison tables should use clear check / "x" icons. Low-contrast text for unavailable features hurts legibility — [NN/g 2019](https://www.nngroup.com/articles/b2b-trust-from-b2c/)
- Where exact pricing is impossible, show sample prices for typical scenarios. A configurator should be optional, not the only path — [NN/g 2006](https://www.nngroup.com/articles/show-prices-for-common-scenarios/)
- Linear-product UI conventions spill into marketing sites: command palette (⌘K), shortcut hints, a 4px spacing grid, muted grey palette with color reserved for status, and dark default with a purple accent. Linear's own mobile experience "feels like a desktop layout on a phone" — [925studios, Mar 2026](https://www.925studios.co/blog/linear-design-breakdown-saas-ui-2026)

**(b) AI tools**
- AI brands moved away from literal robot imagery toward abstraction: gradients, glows, blur, sparkles, light orbs — [Indie Hackers / Hyzo, Jul 2026](https://www.indiehackers.com/post/the-ai-purple-problem-why-every-ai-brand-looks-the-same-6cb0aa2a02)
- Commenters on that article recommend showing real output or workflow screenshots instead of abstract visuals. One commenter claims SocialPost.ai converted better after the switch. This is anecdotal — [same source](https://www.indiehackers.com/post/the-ai-purple-problem-why-every-ai-brand-looks-the-same-6cb0aa2a02)

**(c) Mobile apps** — patterns in 15 app pages, all from [The Swift Kit, Apr 2026](https://theswiftk.it.com/blog/best-app-landing-page-examples-2026). The source is promotional; some entries are stale (Apollo for Reddit shut down in 2023).
- Device mockups are near-universal.
- Hero types seen:
  - illustration plus mockup (Headspace)
  - mascot plus mockup (Duolingo)
  - real-time data background (Flighty)
  - full-bleed photo shot with the app (Halide)
  - single annotated screenshot (Things 3, Bear)
  - multi-device shot (Craft)
  - auto-playing muted 10–15 s video (Loom)
- Award badges are used as proof, e.g. "Apple Design Award Winner" (Flighty).
- 1Password leads with security certifications before screenshots.

**(d) Courses / creators** — section order from [Kajabi, updated Jul 2026](https://www.kajabi.com/blog/how-to-create-an-amazing-sales-page-today):
1. Headline / promise
2. Benefit bullets
3. Video (creator intro, overview, testimonial videos)
4. Story
5. Credibility data
6. Testimonials with name and photo
7. Results proof (before / after)
8. Offer / bundle with value anchoring
9. Guarantee
10. CTA
11. Instructor bio
12. No navigation

The Kajabi article does *not* explicitly cover a curriculum section, payment-plan tiers or an FAQ (see Gaps).

**(e) Digital goods**
- Gumroad's design system, per a third-party summary: cream canvas `#f4f4f0`, white cards, hot pink `#ff90e8`, 1px black borders on nearly everything, hard 4px offset shadows with no blur, monospace tabular numerals for prices, an 8px button radius and a 12px card radius — [webdesignhot design-md, May 2026](https://www.webdesignhot.com/api/design-md/gumroad.md)

**(f) Agencies** — patterns from 12 agency sites, research current to Apr 2026, all from [Krishaweb, May 2026](https://www.krishaweb.com/blog/best-creative-agency-websites.txt). Caveat: the list includes Ueno, which closed after Twitter acquired it in 2021, so the source's currency is questionable.
- Homepage as scrolling portfolio stream (Instrument)
- Motion-led homepage (Fantasy, Hello Monday)
- Restrained, authoritative sites with selective projects (Wolff Olins)
- Archive filterable by partner, discipline or client (Pentagram)
- Thumbnail grid of projects (Hello Monday)
- Case studies with brief, process and constraints (Area 17)
- Single-discipline focus with a concise process section (Koto)
- Point-of-view-first hero (Huge)

### Inferences
- **Synthesis — section stacks a builder can use:**
  - **SaaS:** Nav (logo · Product ▾ · Solutions ▾ · Pricing · Docs · Customers · Login · [Get started]) → Hero (H1 ≤ 10 words, sub, 2 CTAs, product UI screenshot in a browser frame or video) → logo wall (5–8 grayscale logos, "Trusted by…") → 3-up value props → bento feature grid (one large anchor tile) → alternating feature deep-dives with real UI → integrations grid → metrics band → testimonial or case-study cards → security / compliance strip (SOC 2, GDPR, ISO badges) → pricing teaser → FAQ accordion → final CTA band → mega-footer (incl. Changelog, Docs, Status).
  - **SaaS docs / changelog:** Docs use 3 columns: left sidebar nav, content, right "on this page" TOC, plus ⌘K search. The changelog is a dated reverse-chronological feed with version tags and an image or video per entry. Observation, as seen on Linear, Vercel, Stripe docs; not re-verified live.
  - **AI:** Same as SaaS, plus a hero with a live prompt input or an interactive demo (audio player, before/after slider, generated gallery). Add a model or benchmark comparison block, an API / code snippet tabs block, and usage-based pricing with credits.
  - **App:** Nav (minimal) → Hero (headline, store badges, QR on desktop, phone mockup or video) → rating / downloads / award strip → 3–5 feature sections, each with a phone screenshot → widget / multi-device section → reviews carousel (App Store quotes) → pricing (free / Pro) if subscription → FAQ → repeated badges → footer with privacy / support links.
  - **Course:** No-nav header → hero with promise, instructor photo or video, and CTA → "is this for you" two-column (for / not for) → outcomes → curriculum accordion (modules → lessons, durations, lesson count, total hours) → instructor bio → testimonial wall (video plus screenshots of DMs or results) → bonuses → pricing (one-time vs payment plan, sometimes a 3-tier VIP) → guarantee badge → FAQ → final CTA. Sticky "Enroll" bar on mobile.
  - **Digital goods (single creator):** Product page with a large cover or preview gallery (carousel or interactive preview / live demo link) → "What's inside" checklist (file formats, page count, compatibility e.g. Figma / Notion / Framer) → price plus buy button (sticky on mobile) → license tiers (personal / commercial) → reviews / ratings → creator card → related products.
  - **Digital goods (marketplace):** Search-first header → category chips → card grid (thumbnail, title, creator, price, rating) → filters sidebar.
  - **Digital goods checkout:** Overlay or one-page checkout, with email first, Apple Pay / Google Pay / Link, and instant download plus email delivery.
  - **Agency:** Oversized typographic hero or showreel → selected work grid (large, image-led cards with client and discipline tags, hover video previews) → services list (often a plain text list or accordion) → clients logo wall → approach / process steps → awards / press → team / culture → big "Let's talk" footer CTA with email address in large type.

### Gaps
- No quantitative study found on curriculum-accordion vs. flat module lists for course conversion.
- No primary data found on overlay vs. redirect checkouts for digital goods.
- Changelog / docs patterns rest on observation only. No design-research source was found.

---

## 3. UI/UX best practices with evidence (NN/g, conversion and pricing-page research)

### Takeaway
The strongest evidence is NN/g on B2B transparency:
- show prices, or typical-scenario prices
- avoid credit-card-gated trials
- explain form fields
- use clear comparison tables
- show demos

Pricing-page conventions are widely repeated, but the figures cited for them are mostly secondhand and unverifiable. These conventions are:
- 3–4 tiers
- a highlighted "Most popular" plan
- a monthly / annual toggle defaulted to annual
- a guarantee or trial
- testimonials near pricing

Treat those numbers as directional only. Bento grids help only below a clear hero, with one anchor tile.

### Cited Findings
- Hiding prices adds a step, can make a product seem unaffordable, and makes the company seem to be hiding something — [NN/g 2019](https://www.nngroup.com/articles/b2b-trust-from-b2c/)
- Missing B2B prices was named the "#1 Web design mistake of 2002". An overly precise calculator (ZIP code, weight, dimensions) frustrated testers, while a simple table of typical-case prices worked — [NN/g 2006, old](https://www.nngroup.com/articles/show-prices-for-common-scenarios/)
- Testimonials that start with doubt and end in confidence were valued, and the author's job title and affiliation matter. Case studies should span varied industries. Showing physical locations, employees and stated values adds credibility — [NN/g 2019](https://www.nngroup.com/articles/b2b-trust-from-b2c/)
- Pricing-page figures listed below are "only directional". All are secondhand and unlinked, so treat them as low reliability — [m3ter, May 2025](https://www.m3ter.com/blog/15-data-driven-pricing-page-optimizations)
  - Highlighting a "Most popular" plan: 16–30% lift (attributed to ProfitWell)
  - Limiting to 3–4 plans: 15–25% (Pricing Intelligently)
  - Annual toggle defaulted to annual: 20–30% more annual adoption (Baremetrics)
  - Testimonials near pricing: up to 30% (CXL)
  - Free trial or money-back guarantee: 20–35% (Dropbox / Basecamp)
  - Most expensive plan shown first: 10–20% higher AOV (CXL)
  - Bold "% off" on the annual option: 18% (Crazy Egg)
  - Mobile optimization: 19% (Crazy Egg)
- Bento grids hurt when:
  - they sit above the fold
  - tiles are equal-sized and compete
  - each tile has its own CTA
  - the product fits in one sentence
  - they collapse into a long single column on mobile
- The suggested fix is to cut half the tiles and enlarge one. This is opinion grounded in NN/g F-pattern and visual-hierarchy work and in Hick's Law; no A/B data is given — [BuildMVPFast, Jul 2026](https://www.buildmvpfast.com/blog/bento-grid-helps-vs-hurts-conversion-2026)
- Dark mode in Linear-style sites is "mostly an aesthetic choice, not a proven advantage" — [LogRocket 2025](https://blog.logrocket.com/ux-design/linear-design)
- Keyboard-first and dense UI suits developers and PMs. Copying it for other audiences is a mistake: "match the interaction model to your audience" — [925studios 2026](https://www.925studios.co/blog/linear-design-breakdown-saas-ui-2026)
- Course pages: put names and photos on testimonials (prefer video). Use a guarantee window long enough to sample the course but too short to finish it. Use no navigation — [Kajabi, updated 2026](https://www.kajabi.com/blog/how-to-create-an-amazing-sales-page-today)
- Apps: a captioned, muted, auto-playing hero video under 3MB (Loom). The claimed "~2× conversion" for it has no source — [The Swift Kit 2026](https://theswiftk.it.com/blog/best-app-landing-page-examples-2026)

### Inferences
- Synthesis for a builder:
  - Default to a visible pricing page, using 3 tiers plus an Enterprise "Contact" column. Highlight the middle tier. Default the toggle to annual and show the savings %. Put a feature comparison table below, with sticky column headers. Add an FAQ under the table.
  - For enterprise-only products, show "starting at" or typical-scenario pricing rather than nothing, per NN/g.
  - Trial CTAs should state "No credit card required" as microcopy under the button, per NN/g's no-card trial recommendation.
  - Mobile: collapse comparison tables into per-plan accordions or a horizontally swipeable plan picker. Keep a sticky bottom CTA bar on long sales pages. This is synthesis, not sourced.

### Gaps
- No current (2024–26) NN/g article specifically on SaaS pricing pages or logo walls was retrieved. The NN/g B2B report ([B2B Website Usability report](https://www.nngroup.com/reports/b2b-websites-usability/)) exists but is paywalled and was not read.
- The original ProfitWell / Baremetrics / CXL studies behind the m3ter numbers were not located. Their figures cannot be verified.

---

## 4. Prototypical visual style per niche (mapped to style labels)

### Takeaway
- **SaaS / dev tools:** "Linear / Vercel dark tech" (Dark/tech + Minimalist + Aurora/gradient glow + Bento) and the lighter "shadcn / Tailwind clean" variant.
- **AI:** the same, plus purple-blue gradients and orbs (Aurora/gradient, Glassmorphism).
- **Apps:** Flat/Material-ish clean with device mockups and soft gradients, plus Illustrative / mascot for consumer apps.
- **Creators / courses:** warm, personal, "Notion-like" pastel / Organic with the face-forward instructor photo.
- **Digital goods:** Minimalist marketplace grids. Neo-brutalist (Gumroad) is the indie-creator signature.
- **Agencies:** Typographic-led / Swiss / Editorial with Kinetic typography and Immersive scroll (WebGL).

### Cited Findings
- **Linear-style traits:** dark mode, bold sans typography, complex gradients, glassmorphism, linear flow. Linear's 2025 site moved toward monochrome black / white with fewer accents. Users cited: Linear, Raycast, GitHub, Reflect, Stripe, Wise — [LogRocket, Jun 2025](https://blog.logrocket.com/ux-design/linear-design)
- **Linear-style product visual traits:** dark default plus purple accent, muted grey palette with color reserved for status, 4px grid — [925studios, Mar 2026](https://www.925studios.co/blog/linear-design-breakdown-saas-ui-2026)
- **AI branding:** purple (between "trust" blue and "energy" pink), gradients, glows, blur, sparkles, light orbs. Examples: Google Gemini (blue-red-purple gradients), Microsoft 365 Copilot (blue / purple / pink abstract backgrounds), OpenAI business materials (purple / pink / blue gradients) — [Indie Hackers / Hyzo, Jul 2026](https://www.indiehackers.com/post/the-ai-purple-problem-why-every-ai-brand-looks-the-same-6cb0aa2a02)
- **AI-generated sites:** a recurring "purple gradient website" problem is discussed — [prg.sh via scour.ing](https://scour.ing/@emschwartz/p/https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website) (search snippet only, not fetched)
- **Gumroad = Neo-brutalist:** flat high-contrast, hard borders, offset solid shadows, pink / yellow / teal flat blocks, "handmade" creator-commerce feel — [webdesignhot, May 2026](https://www.webdesignhot.com/api/design-md/gumroad.md)
- **Agencies:** "considered typography", motion-led homepages (Fantasy, Hello Monday), restrained authoritative style (Wolff Olins) — [Krishaweb, May 2026](https://www.krishaweb.com/blog/best-creative-agency-websites.txt)
- **Apps:** dark plus 3D device renders with parallax (Fantastical), illustration (Headspace), mascot (Duolingo), minimal white (Bear) — [The Swift Kit, Apr 2026](https://theswiftk.it.com/blog/best-app-landing-page-examples-2026)

### Inferences
Synthesis — style label map: primary / secondary labels, and what to avoid by default.

| Niche | Prototypical (most sites) | Common secondary | Differentiating options | Avoid by default |
|---|---|---|---|---|
| (a) SaaS / B2B | Minimalist + Dark/tech ("Linear/Vercel") or light "shadcn / Tailwind" Flat; Bento features | Aurora/gradient glows, subtle Glassmorphism, grid-line backgrounds | Illustrative / Retro (PostHog), Editorial serif (Stripe-like editorial), Neo-brutalist, Swiss bold color (Raycast-style single bold accent) | Neumorphism, Claymorphism, Maximalist, Cyberpunk (low legibility for B2B buyers) |
| (b) AI | Dark/tech + Aurora/gradient (purple-blue), orbs / glow, Glassmorphism | Bento, kinetic "typing" demos | Warm Editorial / Organic (cream, serif, hand illustration), Retrofuturism / pixel, Typographic-led monochrome, real-output-led galleries | The purple-orb / sparkle-icon cliché; robot imagery |
| (c) Mobile apps | Flat/Material clean + device mockups + soft gradient backgrounds | Illustrative / mascot (consumer), Dark/tech + 3D device renders (pro tools) | Product-as-hero (live data / full-bleed real output), Claymorphism / 3D-icon playful (consumer, kids, fintech), Y2K for Gen-Z social | Heavy Immersive scroll that delays badges; Brutalist |
| (d) Courses / creators | Warm personal Minimalist / "Notion-like" pastel, Organic, big instructor portrait | Editorial serif (premium coaches), Illustrative doodles | Editorial magazine (MasterClass-cinematic Dark/Luxury), Neo-brutalist (indie maker), Collage / Retro (creative-arts teachers) | Dark/tech SaaS look (feels impersonal); Cyberpunk |
| (e) Digital goods | Minimalist marketplace grid (white, card thumbnails) | Neo-brutalist (Gumroad lineage), Bento previews | Retro / Y2K / Maximalist for niche template creators; interactive live-preview heroes | Glassmorphism over product previews (hurts legibility of the goods) |
| (f) Agencies | Typographic-led / Swiss / Editorial + Kinetic typography + Immersive scroll (WebGL, smooth scroll) | Dark/tech, Collage | Brutalist / Neo-brutalist, Maximalist, Retro, playful Illustrative; restrained "quiet luxury" editorial for B2B consultancies | Template-like SaaS look (signals "not creative"); for consultancies, avoid heavy WebGL that hides substance |

- "shadcn / Tailwind look" is the researcher's label for the light variant: white or off-white backgrounds, zinc/neutral grays, 1px borders, 8–12px radius cards, Inter / Geist type, subtle shadows, pill badges ("New → Announcing X"), and grid or dot-pattern backgrounds fading out. No external source in this session explicitly documents this label (see Gaps).
- B2B consultancies (as opposed to creative agencies) skew Corporate Minimalist / Editorial. They show fewer motion effects, and their pages are led by insights, articles and case-study cards. This is synthesis.

### Gaps
- No source explicitly quantifies the "shadcn / Tailwind look" or credits it as a named style.
- No source quantifies the share of SaaS sites in dark vs. light mode. The 925studios "50/50 chance it looks like Linear" claim is explicitly unsourced ([925studios](https://www.925studios.co/blog/linear-design-breakdown-saas-ui-2026)).
- No dedicated source on creator / course visual styles (pastel / Notion-like) was found. That row is observation-based.

---

## 5. Saturation: generic looks, successful differentiators, styles to avoid

### Takeaway
The Linear-style dark SaaS look, purple-gradient AI branding and the Apple-derived bento grid are explicitly described in 2025–26 sources as oversaturated and generic. Differentiation that works keeps the conversion skeleton but changes the visual system:
- one bold brand color (Raycast)
- illustrative or retro personality (PostHog — observation)
- warm editorial anti-purple (Anthropic / Claude — observation)
- real product output instead of abstract art

### Cited Findings
- "Almost every SaaS website looks the same". "The appeal is starting to wear off due to oversaturation". Trend-following products "look monotonous". GitHub's 2025 site added more color and glassmorphism "and looks worse for it". Raycast kept its bold color, dropped its gradient and developed a distinct identity. Sans-serif fonts are "becoming stale" — [LogRocket, Jun 2025](https://blog.logrocket.com/ux-design/linear-design)
- "Copying Linear's aesthetics without understanding the reasoning behind each choice is why most clones feel hollow" — [925studios, Mar 2026](https://www.925studios.co/blog/linear-design-breakdown-saas-ui-2026)
- Purple AI branding "wears out faster" because AI "has no physical equivalent". The article recommends light backgrounds, warmth, specificity and plain language, and asks: "Does our brand really need to look like yet another AI brand?" It contrasts Apple Intelligence's integrated, non-purple-robot approach — [Indie Hackers / Hyzo, Jul 2026](https://www.indiehackers.com/post/the-ai-purple-problem-why-every-ai-brand-looks-the-same-6cb0aa2a02)
- Commenter suggestion: a five-second recall test (hide the hero; can people name the job the product does?) — [same](https://www.indiehackers.com/post/the-ai-purple-problem-why-every-ai-brand-looks-the-same-6cb0aa2a02)
- Bento grids spread "without regard to whether they fit the product". bentogrids.com is cited as illustrating saturation. Creative Boom (2026) is quoted on trends creatives are tired of: "It's bad because it uses them without thought, without purpose" — [BuildMVPFast, Jul 2026](https://www.buildmvpfast.com/blog/bento-grid-helps-vs-hurts-conversion-2026)
- Glassmorphism is "easy to apply but hard to make distinctive" — [LogRocket 2025](https://blog.logrocket.com/ux-design/linear-design)
- Vibe-coded / AI-built sites converge on the same purple gradients. The sources are search snippets only, not fetched: [prg.sh](https://scour.ing/@emschwartz/p/https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website) and [YC podcast summary](https://summify.io/discover/common-mistakes-with-vibe-coded-websites-DNSXlB/)

### Inferences
- **Generic markers to flag, synthesis.** The more of these a site combines, the more it reads as a template:
  - near-black background with a purple / blue radial glow behind the hero
  - pill "announcement" badge above the H1
  - gradient-text H1
  - Inter / Geist only
  - grayscale logo marquee
  - 6-tile equal bento
  - sparkle ✦ icon for AI
  - glass cards
  - 3-tier pricing with a purple "Popular" ribbon
- **Differentiators, observations to verify live:**
  - PostHog: illustrative hedgehog mascot plus a retro desktop-OS / window UI site. Retro + Illustrative.
  - Anthropic / Claude: cream / clay palette, serif headings, hand-drawn illustrations. Editorial / Organic, anti-purple.
  - Mistral AI: orange-to-yellow pixel / retro gradients. Retrofuturism / Retro.
  - Stripe: light editorial with an animated gradient "wave" hero. Aurora but executed as signature brand art.
  - Raycast: dark with a single saturated red. Sourced via LogRocket.
  - Gumroad: Neo-brutalist. Sourced via webdesignhot.
  - For agencies, the differentiator *is* expected; the generic agency site is the Webflow / Framer agency template (big sans hero, marquee of services, work grid).
- **Avoid for conversion-critical tech pages:**
  - Neumorphism, because of low contrast. This is a general accessibility concern, not sourced here.
  - Heavy Immersive scroll or scroll-jacking on SaaS / app / course pages, where it delays the CTA.
  - Cyberpunk / Maximalist for B2B trust contexts.

### Gaps
- No quantitative study measuring brand recall or conversion of "generic Linear look" vs. differentiated SaaS sites was found.
- The Creative Boom 2026 "tired trends" piece was not fetched directly.

---

## 6. Trust UI components (as UI patterns)

### Takeaway
The core trust kit for tech sites is:
- logo wall
- metrics band
- named testimonials (photo, title, company)
- case-study cards
- security / compliance badge strip
- transparent pricing
- visible company reality (team, locations)

Apps add ratings, download counts and awards. Creators add result screenshots and video testimonials. Agencies use client logos, awards and the work itself.

### Cited Findings
- **Testimonials:** use author title and affiliation; "doubt → confidence" narratives work. **Case studies:** across varied industries. **Credibility:** physical locations, employees, values. **Contact:** email plus phone. **Trial:** no credit card — [NN/g 2019](https://www.nngroup.com/articles/b2b-trust-from-b2c/)
- That NN/g article does not discuss logo walls, so there is no NN/g evidence on logos from this session — [NN/g 2019](https://www.nngroup.com/articles/b2b-trust-from-b2c/)
- **Apps:**
  - "65 million users" counter under the hero (Headspace)
  - "Apple Design Award Winner" (Flighty)
  - security certifications and audit reports before screenshots (1Password)
  - user-generated home-screen gallery as social proof (Widgetsmith)
  - "Shot on Halide" gallery
  - Source: [The Swift Kit 2026](https://theswiftk.it.com/blog/best-app-landing-page-examples-2026)
- **Courses:** testimonials with name and photo, ideally video; before / after results; credibility numbers; guarantee — [Kajabi 2026](https://www.kajabi.com/blog/how-to-create-an-amazing-sales-page-today)
- **Agencies:** case studies framed around business outcomes (Huge); client-logo thumbnail grid (Hello Monday); selective high-profile projects (Wolff Olins) — [Krishaweb 2026](https://www.krishaweb.com/blog/best-creative-agency-websites.txt)
- **Pricing:** testimonials placed near pricing, with a claimed lift that is secondhand and low reliability — [m3ter 2025](https://www.m3ter.com/blog/15-data-driven-pricing-page-optimizations)

### Inferences
Synthesis — component specs a builder can generate:
- **Logo wall:** 5–8 monochrome logos, equal optical size, a single row or a slow marquee, with a label ("Trusted by 4,000+ teams"). On mobile, use a 2–3 column grid or a marquee.
- **Metrics band:** 3–4 large numerals plus a short label, using tabular figures.
- **Testimonial card:** quote, avatar, name, title, company logo. Optionally add a metric chip ("−40% churn") and a link to the case study.
- **Case-study card:** company logo, industry tag, a headline result metric, a thumbnail, and "Read story →".
- **Security strip (SaaS / fintech / AI):** SOC 2 / ISO 27001 / GDPR / HIPAA badges and a link to a Trust Center page.
- **App rating chip:** "4.8 ★ · 20k ratings" plus store badges.
- **Creator proof:** screenshot collage of DMs and results, plus a video testimonial grid.
- **Digital goods:** sales count ("2,341 sold"), star rating, review list, creator profile card, "instant download" and refund-policy note near the buy button.
- **Agency:** awards row (Awwwards, FWA, Cannes, D&AD, Webby), press logos, client logos, and named team portraits.

### Gaps
- No primary research located on logo-wall effectiveness, badge placement, or the trust lift from security badges in 2024–26.

---

## 7. Prototypicality evidence from template marketplaces and galleries

### Takeaway
The galleries and marketplaces confirm that SaaS / tech / AI / app / agency are major, standalone design categories. Lapa Ninja tracks style-tags such as "Minimal" (its 2nd-largest tag), "Gradient", "Bento Grid" and "Retro". Framer groups AI, Apps, Fintech and SaaS under "Software". Course / education and marketplace pages are much thinner categories.

### Cited Findings
- **Lapa Ninja (Oct 2026):** 7,511 pages total — [Lapa Ninja](https://www.lapa.ninja/)

  | Lapa Ninja tag | Pages |
  |---|---|
  | Minimal | 3,051 |
  | Technology | 1,489 |
  | Illustration | 1,454 |
  | Portfolio | 1,067 |
  | Productivity | 994 |
  | Agency | 971 |
  | Studio | 862 |
  | App | 780 |
  | Typography | 712 |
  | SaaS | 691 |
  | Software | 652 |
  | Gradient | 464 |
  | Design Tools | 461 |
  | Education | 434 |
  | Dev Tools | 239 |
  | AI | 208 |
  | 3D Websites | 156 |
  | Isometric | 146 |
  | Retro Style | 102 |
  | Bento Grid | 75 |
  | Course | 39 |
  | Marketplace | 1 |

- **Framer Marketplace templates:** "Software" groups AI, Apps, Fintech and SaaS. "Agency" groups Architecture, Design, Marketing and Web. "Ecommerce" includes "Digital". "Services" includes Consulting and Education. There is no explicit "Course" or "Startup" category. No counts are shown — [Framer templates](https://www.framer.com/marketplace/templates/)
- **Webflow templates:** "Portfolio & Agency" and "Technology" are top-level categories. SaaS, AI, Mobile App and Course were not shown as top-level categories on the fetched page, out of 7,000+ templates total — [Webflow templates](https://webflow.com/templates)

### Inferences
- "Minimal" being the second-largest tag on Lapa Ninja (≈41% of all entries) supports Minimalist as the default baseline across tech landing pages. "Gradient" (464) far outnumbers "Retro Style" (102), and Bento (75) is small as a tagged style. That suggests bento is under-tagged or treated as a component rather than a style.
- Agency / Studio / Portfolio together (~2,900) rival tech categories. This is consistent with agencies as a major, design-forward niche.
- Course / Marketplace are niche categories in galleries. Creator-course design is mostly produced inside platforms (Kajabi, Teachable, Podia, Stan) rather than showcased in galleries. That last point is synthesis.

### Gaps
- SaaS Landing Page (saaslandingpage.com), Land-book, Godly and Awwwards category counts were not fetched in this session (tool budget).
- Squarespace template categories were not checked.
- Framer and Webflow do not publish per-category counts.

---

## 8. Real, current (2023–2026) example sites per niche

### Takeaway
Below are 4–8 examples per niche with a style label. Entries marked [S] have a source in this session that names the site and its pattern. Entries marked [O] are researcher observation from prior knowledge (≤ mid-2026) and should be spot-checked live before publishing.

### Cited Findings
- **SaaS:** Linear, Raycast, GitHub, Reflect, Stripe and Wise are cited as Linear-style exemplars. Raycast is called a successful differentiator; GitHub 2025 a weaker one — [LogRocket 2025](https://blog.logrocket.com/ux-design/linear-design). Vercel, Stripe, Ramp and Notion are cited as bento adopters (2023–24) — [BuildMVPFast 2026](https://www.buildmvpfast.com/blog/bento-grid-helps-vs-hurts-conversion-2026)
- **AI:** Google Gemini, Microsoft 365 Copilot and OpenAI are cited for purple / blue / pink gradient branding — [Indie Hackers 2026](https://www.indiehackers.com/post/the-ai-purple-problem-why-every-ai-brand-looks-the-same-6cb0aa2a02)
- **Apps:** Headspace, Duolingo, Flighty, Halide, Things 3, Fantastical, Craft, Loom, 1Password and Bear, with the patterns described in section 2 — [The Swift Kit 2026](https://theswiftk.it.com/blog/best-app-landing-page-examples-2026)
- **Agencies:** [hugeinc.com](https://www.hugeinc.com/), [instrument.com](https://www.instrument.com/), [fantasy.co](https://fantasy.co/), [wolffolins.com](https://www.wolffolins.com/), [area17.com](https://area17.com/), [hellomonday.com](https://www.hellomonday.com/), [ideo.com](https://www.ideo.com/), [pentagram.com](https://www.pentagram.com/), [wearecollins.com](https://www.wearecollins.com/), [koto.studio](https://koto.studio/) — [Krishaweb 2026](https://www.krishaweb.com/blog/best-creative-agency-websites.txt). Exclude Ueno, which is defunct.
- **Digital goods:** Gumroad is Neo-brutalist — [webdesignhot 2026](https://www.webdesignhot.com/api/design-md/gumroad.md)

### Inferences
Example roster with style labels. [S] = sourced above, [O] = observation; verify live.

**(a) SaaS / B2B**
- https://linear.app — Dark/tech Minimalist, monochrome 2025 refresh, product-UI hero, bento below [S]
- https://vercel.com — black/white Swiss-minimal, Geist type, grid-line backgrounds, dark/light [S bento; O style]
- https://stripe.com — light Editorial, animated gradient-wave hero, dense feature storytelling [S; O style]
- https://www.raycast.com — Dark/tech, single bold red accent, centered hero plus download CTA [S]
- https://attio.com — light shadcn-like Minimalist, crisp product UI [O]
- https://posthog.com — Illustrative + Retro (desktop-OS window UI, hedgehog mascot), the differentiator [O]
- https://www.notion.com — light, hand-drawn Illustrative, bento features [S bento; O style]
- https://resend.com — Dark/tech with 3D object hero, developer-focused code blocks [O]

**(b) AI tools**
- https://www.anthropic.com / https://claude.ai — warm cream Editorial / Organic, serif, hand illustrations, anti-purple [O]
- https://openai.com — Typographic-led Minimalist, large type, gradient imagery in business materials [S gradient; O site]
- https://lovable.dev — Aurora/gradient background, prompt-box-as-hero [O]
- https://cursor.com — Dark/tech, product-demo-led (editor UI video) [O]
- https://elevenlabs.io — light Minimalist with an interactive audio demo in the hero [O]
- https://mistral.ai — Retro / pixel orange gradient, Retrofuturism [O]
- https://runwayml.com — Dark cinematic, video- and output-gallery-led [O]
- https://www.perplexity.ai — restrained Minimalist / Editorial, teal accent [O]

**(c) Mobile apps**
- https://flighty.com — product-as-hero (live flight data), Dark/tech, award badge [S]
- https://culturedcode.com/things/ — Minimalist, large annotated screenshots [S]
- https://www.headspace.com — Illustrative, warm orange, user-count proof [S]
- https://www.duolingo.com — Flat Illustrative, mascot-driven, bright green [S]
- https://flexibits.com/fantastical — Dark + 3D device renders with parallax [S]
- https://www.halide.cam — full-bleed photography from the app, camera UI overlay [S]
- https://1password.com — trust-first: certifications before screenshots [S]
- https://www.opal.so — Dark, soft gradient glow, phone mockups (wellbeing / screen-time) [O]

**(d) Courses, coaches, creators**
- https://www.masterclass.com — cinematic Dark/Luxury, video-trailer heroes, instructor portraits [O]
- https://maven.com — clean light Minimalist marketplace of cohort courses, instructor cards, syllabus / curriculum sections [O]
- https://www.domestika.org — marketplace grid, warm Illustrative, course-trailer cards [O]
- https://aliabdaal.com — personal-brand creator site, warm Minimalist, face-forward, newsletter and course funnels [O]
- https://www.justinwelsh.me — solopreneur creator, Minimalist light, product cards for digital courses [O]
- https://www.coursera.org — Corporate Flat/Material, catalog grid plus syllabus accordion [O]
- Note: buildspace.so (a famous Neo-brutal / Retro creator-education site) shut down in 2024, so do not use it as a current example [O]

**(e) Digital downloads / templates / marketplaces**
- https://gumroad.com — Neo-brutalist (cream, hot pink, black borders, hard shadows) [S]
- https://www.framer.com/marketplace/ — Dark/tech template marketplace grid with live preview [S existence; O style]
- https://creativemarket.com — light Minimalist marketplace grid, large thumbnails [O]
- https://ui8.net — Dark/tech marketplace for UI kits, large preview cards [O]
- https://www.notion.com/templates — light Illustrative gallery of templates with creator attribution [O]
- https://elements.envato.com — subscription marketplace, search-first Minimalist grid [O]
- https://www.lemonsqueezy.com — playful Aurora/gradient plus Illustrative merchant-of-record checkout (acquired by Stripe 2024; status should be verified) [O]

**(f) Agencies & B2B consultancies**
- https://www.pentagram.com — Swiss / Typographic, archive filterable by partner / discipline [S]
- https://www.instrument.com — scrolling portfolio stream, Editorial [S]
- https://www.hellomonday.com — playful motion, Kinetic / Illustrative [S]
- https://fantasy.co — motion-led, spatial layout [S]
- https://koto.studio — Minimal Swiss, concise process, single-discipline focus [S]
- https://locomotive.ca — Immersive scroll / smooth-scroll WebGL agency, Kinetic typography (author of locomotive-scroll) [O; case-study page exists: https://locomotive.ca/en/work/k72]
- https://www.wolffolins.com — restrained authoritative Editorial [S]
- https://www.ideo.com — consultancy-style, methodology and thought leadership first, Editorial [S]

### Gaps
- [O] entries were not re-verified live in this session. Sites redesign frequently: Linear redesigned in 2025 and GitHub changed in 2025, per [LogRocket](https://blog.logrocket.com/ux-design/linear-design).
- No Awwwards "Site of the Year 2025" winners list was fetched, so agency examples rely on one listicle with at least one stale entry (Ueno).
- Global coverage is weak. Examples are mostly US/EU. No sourced examples from Asia or LatAm tech sites were gathered.
