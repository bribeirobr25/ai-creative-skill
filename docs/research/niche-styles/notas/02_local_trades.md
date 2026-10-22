# Local Trades & Home Services: Web Design Style, Layout and UI/UX Conventions

Scope: plumbers, electricians, HVAC/heating, auto mechanics/garages, painters/decorators, cleaning, gardeners/landscapers, movers, roofers/handymen. Visual design, layout and UI/UX only. Research date: 2026-10-22. Most sources are US agency blogs (they sell trade websites, so they have a commercial bias). European examples are scarce in the evidence: only UK (BOXT, idstudio landscape clients). Evidence is mostly practitioner observation, not controlled studies. Points marked "(synthesis)" are my inference.

## 1. Visitor goals and primary conversion actions; how the UI supports them

### Takeaway
Visitors are often urgent, on mobile and searching locally, and the main action is a phone call, with "book/quote" second and text/WhatsApp/chat third. Every current playbook puts a tap-to-call number in a sticky header (top right), adds a booking or quote CTA beside it, and keeps quote forms to about 4–5 fields, using a multi-step "tool-like" flow where pricing needs inputs.

### Cited Findings
- Google/Ipsos survey (Sept 2013, n=3,000 US smartphone searchers; **old evidence**, self-reported): 70% of mobile searchers have used click-to-call from search results. 47% would be more likely to look at other brands if there was no phone number. Local-services searchers were the most likely of all verticals to call (home-services searches: 66% "extremely/very likely" to call). The most common reason to call was to schedule an appointment, followed by hours, price comparison and service questions. — [Think with Google / Ipsos, The Role of Click to Call in the Path to Purchase](https://www.thinkwithgoogle.com/_qs/documents/1454/click-to-call_research-studies_hz2ytgv.pdf)
- "Nearly 70% of home service customers book providers online" (GetApp research, cited second-hand). Online booking and quote forms let customers make requests outside business hours. — [WebFX, Home Services Website Design handbook (Oct 2025, updated Sept 2026)](https://www.webfx.com/blog/home-services/website-design-handbook/)
- Recommended pattern: phone number in the top-right header on every page, tap-to-call, sticky header so it stays visible on scroll. Hero has a primary CTA above the fold ("phone number, a quote button, or both"). — [Redefine Web, Home Service Web Design Best Practices (Jul 2026)](https://redefineweb.com/blog/home-service-web-design-best-practices/)
- Quote/contact form: limit to 4–5 fields (name, phone, service needed, zip/address; email optional). Use inline validation, put the form above the fold rather than at the bottom, and follow it with a confirmation page that explains next steps. — [Redefine Web (Jul 2026)](https://redefineweb.com/blog/home-service-web-design-best-practices/)
- Sticky mobile navigation keeps booking reachable ("Schedule Now" next to a visible phone number, Parker & Sons). A booking CTA is visible on every page (Genz-Ryan). A "quick-estimate" button is built for speed (The Grounds Guys). — [WebFX (2025/26)](https://www.webfx.com/blog/home-services/website-design-handbook/)
- 2026 HVAC essentials: mobile-first, "obvious conversion paths (call, book, or text)", phone number next to the menu CTA, a "Get a quote" form at the top of selling pages. — [Hook Agency, HVAC websites (Jan 2026)](https://hookagency.com/hvac-websites/)
- Observed in 20 real US plumbing sites (screenshots Aug 2026): sticky call buttons and sticky red "Call Us" pills; phone and city shown as separate tappable pills under the subheading; dual side-by-side CTAs (call + message); a dark contact bar grouping phone, WhatsApp, form and booking link (Top Level Drain Cleaning); phone placed inside a CTA card next to "Send Message" and "Book" (CW Plumbing). — [UENI, Plumbing Website Design: 20 Real Examples (Aug 2026)](https://ueni.com/blog/plumber-websites/)
- Multi-step forms: practitioner case data shows large uplifts. A B2C financial lead-gen form went from 11% to 46% with a "tool-like" multi-step form, and a consulting enquiry form from 0.96% to 8.1%. **Caveats:** the author sells a multi-step form tool, the data is from 2014–2016 or undated, and there are no sample sizes or significance tests. The author also notes short forms still work in some contexts. — [Venture Harbour, Why multi-step lead forms get up to 300% more conversions (2016, page edited 2026)](https://ventureharbour.com/multi-step-lead-forms-get-300-conversions/)
- Baymard (adjacent evidence, e-commerce checkout, 2024): the average checkout has 11.3 fields, but "most sites need only 8". 42% of test participants typed their full name into "First Name", which supports a single "Name" field. Hiding optional fields such as Address Line 2 reduces stalls (about 30% of participants paused there). — [Baymard, Checkout Optimization: 5 Ways to Minimize Form Fields (Jun 2024)](https://baymard.com/blog/checkout-flow-average-form-fields)
- Productised home-services model (UK): the hero headline is "Get a fixed price in minutes", the primary CTA "Get your boiler quote" leads into a separate multi-step quote app, and the secondary link is "Or speak with our helpful sales team". Product cards show "Installed from £X". — [BOXT homepage (fetched Oct 2026)](https://www.boxt.co.uk/)
- Zip-code entry inside the booking CTA ("Book Appointment Now" with zip entry) at Midtown Chimney Sweeps. Live chat at King of Maids. Instant estimates at Maid First. — [htmlburger, Cleaning websites examples (Feb 2024, mod. Jan 2025)](https://htmlburger.com/blog/cleaning-websites-examples/)

### Inferences
- (synthesis) The conversion actions split by sub-niche urgency. **Emergency trades** (plumbing, drains, electrical faults, HVAC breakdowns, lockouts, roof leaks) put the call first: sticky phone in the header plus a mobile bottom bar with Call, and optionally WhatsApp/Text. **Scheduled or recurring services** (cleaning, lawn care, servicing, MOT/inspection) put booking first: a booking widget or zip-code entry that leads into time slots. **High-ticket projects** (landscaping design, roofing replacement, painting, moving, boiler/heat-pump installs) put the quote first: a multi-step estimator with service, then property size, then timing, then contact details.
- (synthesis) A good default mobile action bar is two or three equal-width buttons fixed to the bottom ("Call now" as the primary filled button, "Get quote" or "Book" as a secondary, and WhatsApp in markets where it dominates, such as Brazil, much of Europe, India and LatAm). The bar should have an opaque background and stay within NN/g's content-to-chrome guidance (section 3).
- (synthesis) Multi-step forms suit trades where the price depends on inputs. A single short form (4–5 fields) is enough for "call me back" requests. The "foot-in-the-door" first step should be a low-effort tap choice (service type or zip code), not a name or email field.

### Gaps
- No recent (2023–2026) independent, non-Google study on mobile call behaviour for home services. The best data is the 2013 Ipsos/Google survey.
- No controlled study found that tests a sticky bottom call bar against a header-only phone number in trades. Agency claims that a top-right phone number "outperforms" other placements cite unnamed "eye-tracking research" ([Redefine Web](https://redefineweb.com/blog/home-service-web-design-best-practices/)), so treat that claim as unverified.
- Not verified: WhatsApp click-to-chat adoption rates in European or Brazilian trade sites.

## 2. Dominant layout and page patterns

### Takeaway
The canonical trade homepage stacks the following: a utility top bar (licence, phone, city, offer or emergency notice), a sticky header with the phone number and CTA, a hero showing a real team or van with a local headline, a CTA and a Google rating badge, a differentiator icon list, a services grid, a review carousel, a process (3–4 steps), a service-area block, an FAQ, and a footer with the address. Inner pages are one per service and one per location.

### Cited Findings
- Hero: a specific local headline naming the service and the place ("HVAC Repair and Installation in Reading, PA"), a trust sub-headline (licensed, insured, years in business), and a primary CTA above the fold. — [Redefine Web (2026)](https://redefineweb.com/blog/home-service-web-design-best-practices/)
- Service pages: one dedicated page per service with sections for problem, service, process, why choose us and CTA, plus reviews specific to that service. — [Redefine Web (2026)](https://redefineweb.com/blog/home-service-web-design-best-practices/)
- Service areas shown on the homepage, with dedicated location pages per area. Before/after galleries organised by service type. A landing page for each service with photos and pricing where possible. Emergency services made obvious with badges, dedicated sections and repetition. — [WebFX (2025/26)](https://www.webfx.com/blog/home-services/website-design-handbook/)
- Utility/top-bar patterns seen in real plumbing sites (2026): an emergency bar across the top with a sticky call button (Helpers United, CW Plumbing); a bar beneath the hero listing phone numbers for two locations (Bison); a financing offer in the top bar and "Monthly Payments" in the nav (Platinum Mechanical); the licence number in a slim bar above the nav (Quartz); licence/bonded/insured, then city and phone, in the top bar (G.P Plumbing); a 10% senior/veteran discount bar (Twin Pros, Kuma); three city names in the H1 (Ellite American); navigation split by job type. — [UENI (2026)](https://ueni.com/blog/plumber-websites/)
- Hero imagery patterns: the owner beside his van (Helpers United, Brian Ray's), the full crew in front of two branded vans (Bison), a night-time van photo (Platinum), the company's own signwritten van as the hero carrying phone and licence (In-Line), a split hero of message plus product (Freshwater, Ads Mechanical), and a warm real customer-interaction photo (Arbuckle). — [UENI (2026)](https://ueni.com/blog/plumber-websites/)
- HVAC: a smiling couple in the hero, bulleted differentiators and a large phone number in the header (Jacobs Heating, described as strong above the fold); an emotional family-at-home hero (Alpine); a differentiator icon list plus an immediate lead form (Thelen); homepage coupons and a contact form framed by reviews (Tundra); "Book Appointment" buttons at the top (Smock, Genz Ryan). — [Hook Agency (Jan 2026)](https://hookagency.com/hvac-websites/)
- Framer "Electrician & Home Services" template section list: a service list with permit/warranty tags, a stats block, a customer story, a four-step process "explaining pricing upfront", verified reviews, and a service-area block with FAQ. — [Framer Marketplace, Electrical template](https://www.framer.com/community/marketplace/templates/electrical/)
- Auto repair: phone and/or booking above the fold, often repeated in the nav. Heroes show storefronts, cars on lifts or technicians. Coupon blocks for popular services (Barkley Tire), a contact form overlaid on a grayscale workshop photo (Galson), location cards in the hero banner for multi-site chains (Community Tire Pros), and text-to-quote for mobile repair (Bumper Buddies). — [FreshySites, Top 25 auto repair websites of 2026](https://freshysites.com/blog/top-auto-repair-websites/)
- Productised/installer model: a mega-menu by product with a quote button and starting price in each column, product cards with image, price and two CTAs, and a numbered three-step "How it works". — [BOXT (Oct 2026)](https://www.boxt.co.uk/)
- Landscape/garden design: side-by-side before/after images, and project case pages with goals, style, challenges, size, budget, timescale and a testimonial, grouped by category. Optional pricing estimator, 360° tours, online booking. — [idstudio, Landscape & garden web design (Jul 2025)](https://idstudio.co.uk/insights/web-design/landscape-garden-web-design/)

### Inferences
- (synthesis) A section-order template an AI builder can use as its default:
  1. Utility bar: emergency/24-7 notice or offer, licence, phone.
  2. Sticky header: logo, 4–6 nav items, phone link, filled CTA.
  3. Hero: H1 naming service and city, sub-line with credentials, two CTAs (Call + Quote/Book), rating badge, and a real photo of the team or van.
  4. Trust strip of logos and badges.
  5. Services grid (icon or photo cards).
  6. Differentiators (3–4 icon bullets).
  7. Before/after or project gallery.
  8. Reviews carousel with the platform logo.
  9. Process steps.
  10. Pricing/estimate block or "from" prices.
  11. Service-area block with map or town chips.
  12. FAQ accordion.
  13. Final CTA band.
  14. Footer with NAP (name, address, phone) and hours.
- (synthesis) As a UI pattern, a service-area page is the same template as a service page with the location swapped in (H1 with the town, local reviews, a map, chips linking to nearby towns). Town names usually appear as pill chips.
- (synthesis) Pricing blocks come in three shapes: "from £X" product cards for installs, packages or plans with a frequency toggle for cleaning and lawn care, and coupon/special-offer tiles for HVAC and auto.

### Gaps
- No design-specific sources found for movers, roofers or painters. The patterns above are inferred from adjacent trades.
- Not found: evidence on drag-handle before/after sliders versus side-by-side pairs.

## 3. UI/UX best practices with evidence

### Takeaway
Hard evidence is thin and mostly comes from adjacent fields (NN/g sticky headers, Baymard form fields, Google's 2013 click-to-call study). Trade-specific "stats" in agency blogs are often unsourced. Defensible principles: keep sticky chrome compact and opaque, use tap targets of at least 1 cm, use 16px or larger text, use minimal forms, make the site fast, and put proof above the fold.

### Cited Findings
- NN/g on sticky headers (Apr 2021): use them only if they serve a purpose. Tap targets should be at least 1 cm × 1 cm and text about 16pt, otherwise minimise height. Watch the content-to-chrome ratio on mobile: 13:1 is reasonable, while 2:1 from an oversized header is criticised. Use an opaque, contrasting background, not a translucent one. Avoid animation, and if a header shrinks it should do so fast and smoothly. A partially persistent header (one that reappears on scroll-up) should trigger after a few pixels and slide in over about 300–400 ms. The guidance is qualitative, not quantitative. — [NN/g, Sticky Headers: 5 Ways to Make Them Better](https://www.nngroup.com/articles/sticky-headers/)
- Baymard 2024: fewer fields beat fewer steps. Use a single Name field and hide optional fields. — [Baymard (2024)](https://baymard.com/blog/checkout-flow-average-form-fields)
- Mobile UI: thumb-sized tap targets for buttons, phone numbers and form fields; text readable without zoom; load under 3 s; compress images and reduce third-party scripts (chat, review and analytics widgets). Several numeric claims in this source, such as "1-second delay = up to 20% conversion loss" and "60% of searches on mobile", have no named source. — [Redefine Web (2026)](https://redefineweb.com/blog/home-service-web-design-best-practices/)
- More than 60% of US online searches happen on mobile (Semrush, cited second-hand). The 3-second load threshold is uncited. — [WebFX (2025/26)](https://www.webfx.com/blog/home-services/website-design-handbook/)
- Agency critiques (Hook Agency): reviews, badges and testimonials should sit above the fold, the nav contact link should stand out, and a smiling customer photo next to the hero helps. — [Hook Agency (2026)](https://hookagency.com/hvac-websites/)
- UI cleanliness: "Nothing overlays the content" is praised (Dirty Deeds Plumbing). Utility info sits in a thin strip rather than in pop-ups. — [UENI (2026)](https://ueni.com/blog/plumber-websites/)

### Inferences
- (synthesis) Pop-ups, discount modals and chat bubbles that cover the mobile CTA bar are the most common UX anti-pattern in this niche. If chat is used, the bubble shouldn't overlap the bottom action bar.
- (synthesis) Phone numbers should be real `tel:` links styled as buttons, not plain text. Show the number visibly, because users want to see it and some will dial from another phone.

### Gaps
- No NN/g or Baymard study specific to home services was found. Google has no current (2023–2026) public "local service UX" guidance beyond Core Web Vitals and mobile-friendliness.
- No verifiable recent A/B data on real versus stock photography in trades. Agencies claim real photos win ([Redefine Web](https://redefineweb.com/blog/home-service-web-design-best-practices/)) but give no figures.

## 4. Prototypical visual style

### Takeaway
The prototype is a light, dense, conversion-heavy **Flat/Material corporate-local** style: white or very light backgrounds, navy or bright blue as the primary colour, one hot accent (orange, red or yellow) reserved for CTAs, bold sans-serif headings, real team/van/job photos (stock is still common in templates), medium corner radius, pill-shaped CTAs, icon grids and little motion. It matches none of the trendy labels. The closest are **Flat/Material** with light **Bento**-like card grids. Heritage firms lean **Retro**. Premium landscaping and cleaning lean **Minimalist/Luxury/Organic**.

### Cited Findings
- HVAC palettes: Bob's AC uses navy, matte gray and bright blue with soft waves and mascots; Thelen uses blue and orange; Alpine uses purple, blue and orange with rounded corners, circles and swooshes; Tundra uses orange and blue in a bold industrial look with diagonals and sharp edges; MIDSummer uses muted blue, white and gray. Smock's red and white is called out as a deliberate contrast to "the cool tones typical of HVAC sites". — [Hook Agency (2026)](https://hookagency.com/hvac-websites/)
- Colour as meaning: blue and red signal cooling and heating (Parker & Sons). A bright, conversion-focused palette helps CTAs stand out. — [WebFX (2025/26)](https://www.webfx.com/blog/home-services/website-design-handbook/)
- Auto repair: bold, high-contrast palettes. Red, black, blue, orange and yellow accents recur, and black/white/red appears several times. Some dark heroes (premium vehicles on a dark backdrop). — [FreshySites (2026)](https://freshysites.com/blog/top-auto-repair-websites/)
- Plumbing: strong red branding, a red "Call for Fast Support" button, sticky red "Call Us" pills, tappable pills for phone and city, a round logo badge, and mascots (Kuma's cartoon bear). One site uses a restrained serif small-caps tagline "rather than heavy sans-serif", which implies heavy sans-serif is the norm. — [UENI (2026)](https://ueni.com/blog/plumber-websites/)
- Cleaning: white with pastel accents (Molly Maid), friendly rounded containers with illustrations and subtle animation (More Hands), gray/green/blue (Valley Sparkle), a bold orange CTA (PRO Housekeepers), and clean white with custom icons and trust badges (A Pristine Carpet Clean). — [htmlburger (2024/25)](https://htmlburger.com/blog/cleaning-websites-examples/)
- Wix template descriptions for trades: "warm brown aesthetic" for remodeling, "fresh, green style" for landscaping, "clean and inviting" or "bold and fresh, with strong colors" for cleaning, and "rugged, yet practical" with parallax for home improvement or handyman. — [Wix templates, Services & Maintenance](https://www.wix.com/website/templates/html/industrial/services-maintenance/2)

### Inferences
- (synthesis) Prototype tokens:
  - **Palette:** primary navy (#0B2545-ish) or royal blue; one safety accent (orange #F97316, red #DC2626 or yellow #FACC15) used only on CTAs and badges; light gray section backgrounds; green for landscaping and eco cleaning; red/black for auto.
  - **Type:** bold geometric or grotesque sans (Montserrat, Poppins, Inter, Barlow, Oswald-style condensed for auto/roofing) at 700–800 weight; uppercase is common in buttons.
  - **Radius:** 6–12px on cards, full pills on CTAs and chips.
  - **Density:** high; many CTAs repeated every 1–2 sections.
  - **Motion:** minimal (fade-ups, review carousel, occasional parallax).
  - **Imagery:** real team, van, job-site photos and before/after; stock "smiling technician" in cheaper templates; icon sets for services.
- (synthesis) Mapping to labels:
  - **Flat/Material (dominant)**.
  - **Bento** cards for service grids (secondary, newer templates).
  - **Typographic-led / Neo-brutalist** only for challenger brands.
  - **Retro** for heritage, family-run and classic-car shops.
  - **Organic/Minimalist/Luxury/Editorial** for garden design and premium cleaning.
  - **Scandinavian** fits eco cleaning and Nordic-market trades.
  - **Illustrative** for mascots or neighbourhood illustration (Christian Brothers' illustrated banner).
  - Rare or misfit: Glassmorphism, Neumorphism, Y2K, Memphis, Immersive scroll, Kinetic typography, Collage.

### Gaps
- No quantitative survey of palette frequency across trade sites. The palette claims come from qualitative roundups.

## 5. Differentiating styles that keep trust, and styles to avoid

### Takeaway
Differentiation in trades works through brand character (mascot, bold single colour, retro heritage marks, signwritten van as hero), not through experimental layouts. The conversion skeleton (phone, CTA, reviews above the fold) should stay intact. Avoid styles that hide the phone or CTA, reduce contrast, or slow mobile load.

### Cited Findings
- J Blanton Plumbing (US, Jan 2025) rebranded with Geletka+ around a "bold color system", a modernised logo and a playful-but-professional character "J". The rationale: plumbing calls happen at high-stress moments, so the brand aims for trust and clarity. The new system covers the website, trucks and out-of-home ads. Colours and typefaces are not specified in the source. — [Reel Chicago (Jan 2025)](https://reelchicago.com/article/j-blanton-plumbing-partners-with-geletka-in-a-bold-new-brand-identity/)
- Mascots: Bob's AC uses custom mascots and Kuma Plumbing a cartoon bear "legible at small size". — [Hook Agency](https://hookagency.com/hvac-websites/); [UENI](https://ueni.com/blog/plumber-websites/)
- Retro/classic: Cathedral Automotive (restoration and fabrication) uses a vintage car image with a red/black palette, called out as a distinct "classic/retro style". — [FreshySites (2026)](https://freshysites.com/blog/top-auto-repair-websites/)
- Character-led cleaning brand: Men In Kilts (kilt-wearing team photos, brand colours matched to imagery, subtle scroll animations). — [htmlburger](https://htmlburger.com/blog/cleaning-websites-examples/)
- Contrarian colour: Smock HVAC's red and white against the typical cool HVAC tones. — [Hook Agency](https://hookagency.com/hvac-websites/)
- Signwritten van as hero (In-Line Plumbing), and a restrained serif small-caps tagline (I.P. Plumbing) as a quieter premium signal. — [UENI](https://ueni.com/blog/plumber-websites/)
- NN/g: translucent sticky headers hurt legibility, and animated or trailing headers distract. — [NN/g](https://www.nngroup.com/articles/sticky-headers/)

### Inferences
- (synthesis) Works:
  - **Retro/heritage** (badge or shield logos, script plus condensed sans, cream/red/navy, 1950s van illustrations) for long-established family firms, barbers-adjacent garages and classic-car workshops.
  - **Bold modern challenger**: one saturated brand colour, oversized type, flat illustrations or 3D characters; productised UK/EU installers fit here.
  - **Typographic-led / light Neo-brutalist**: thick outlines, chunky buttons, high contrast; brutalism's directness suits trades if contrast and tap targets stay good.
- (synthesis) Avoid:
  - **Glassmorphism**: translucent layers over photos reduce contrast for CTAs and the phone number, and NN/g warns against translucency in headers.
  - **Neumorphism**: low-contrast buttons with weak affordance for a primary "Call" action.
  - **Immersive scroll, kinetic typography, heavy 3D**: they slow mobile load, delay the CTA and frustrate urgent users.
  - **Y2K, Memphis, Collage**: playfulness reads as unserious for safety-critical trades such as gas or electrical.
  - **Dark/tech**: fine for auto and performance garages, but risky for cleaning, where light and "clean" connotations matter.
  - **Pure Swiss/Minimalist without visible CTAs**: hides the phone, and the minimal look reads as an agency rather than a local tradesperson.
  - **Generic stock photography**: undermines locality and trust; every agency source recommends real photos.

### Gaps
- No case study with before/after conversion data for a retro or bold rebrand of a trade website.
- No verifiable examples found of Neo-brutalist or Bento trade sites live in 2024–2026.

## 6. Sub-niches that diverge

### Takeaway
The main divergence runs along urgency and ticket size. Emergency plumbing, electrical and HVAC is call-first, dense and uses safety colours. Recurring cleaning and lawn care is booking-first, friendlier, rounded and pastel or green. Premium landscaping/garden design and luxury cleaning are portfolio-first and use Editorial/Luxury/Organic styling. Productised installers (boilers, solar, heat pumps) look like e-commerce. Auto garages tend to be high-contrast and sometimes dark.

### Cited Findings
- Landscape and garden design: professional photography has the biggest impact. Use drone footage, time-lapse and full-page imagery, and a clean, showcase-driven layout where the work is the focus. Use elegant, refined fonts for heritage (Kinross House) or a modern sans for contemporary work (RAAEL, minimalist). Take colours from the landscape (Rosebank's soft greens, earthy browns and neutrals). Show awards (e.g. BALI 2024, TrustMark) prominently. — [idstudio (Jul 2025)](https://idstudio.co.uk/insights/web-design/landscape-garden-web-design/)
- Premium cleaning: Luxe Cleaning Co uses images of high-end properties, video and spacious sans-serif typography. Pretty Cleaning Services is modern, minimal and "luxurious" with before/after shots and scheduling from pre-estimated services. — [htmlburger](https://htmlburger.com/blog/cleaning-websites-examples/)
- Eco cleaning: the roundup gives no eco-styled example and mentions eco only as a 2025 trend. — [htmlburger](https://htmlburger.com/blog/cleaning-websites-examples/)
- Recurring cleaning and lawn care templates bundle booking and subscription pricing (Wix Bookings plus "subscription pricing plans"). — [Wix templates](https://www.wix.com/website/templates/html/industrial/services-maintenance/2)
- Productised heating and energy (UK): fixed-price online quote, "installed from" price cards, a product mega-menu, finance options and next-day install messaging. — [BOXT](https://www.boxt.co.uk/)
- Auto: classic/restoration (Cathedral, retro), premium (West Coast Tire Pros on dark backgrounds), and green for the hybrid specialist (Savage Hybrid Shop). — [FreshySites](https://freshysites.com/blog/top-auto-repair-websites/)

### Inferences
- (synthesis) Recommended style by sub-niche:

  | Sub-niche | Style | Conversion priority |
  |---|---|---|
  | Emergency plumbing / drains / electrical / HVAC repair | Flat/Material, navy plus orange or red, dense | Call |
  | Roofing / handyman | Same family; can go darker and more industrial (charcoal plus safety yellow or orange, condensed sans) | Call + quote |
  | Painting / decorating | Lighter, more editorial, colour-swatch accents, strong before/after gallery | Quote |
  | Cleaning, standard | Friendly Flat with rounded corners, light blue/teal/green, illustrations | Book |
  | Cleaning, eco | Organic/Scandinavian, sage/cream, natural textures | Book |
  | Cleaning, luxury | Minimalist/Luxury, neutral palette, generous whitespace | Book |
  | Lawn care / gardening maintenance | Fresh green Flat | Plans + book |
  | Premium landscape / garden design | Editorial/Luxury/Organic: full-bleed imagery, serif or refined sans, earthy palette, portfolio case studies | Consultation request |
  | Movers | Bold challenger branding, quote calculator | Multi-step quote (rooms, from/to, date) |
  | Auto garages, mainstream | High-contrast red/black/blue, cars on lifts | Book |
  | Auto, classic/performance | Retro or Dark/Luxury | Enquiry |
  | Productised installers | E-commerce card grid | Quote funnel |

### Gaps
- No design-specific sources found for movers, eco-cleaning sites or classic-car garages beyond the single Cathedral Automotive example.
- No continental-European or Brazilian trade-site design roundups were gathered. The global view is weak outside the US and UK.

## 7. Trust UI components (patterns, not copy)

### Takeaway
Trust is built from visual blocks placed near the CTA, not saved for the footer. The core set: a Google/Trustpilot rating badge in the hero, a review carousel with platform logos, a licence/insured/bonded strip, certification and association logo rows, a guarantee seal, real team and van photos, a years-in-business stat, financing and price-match badges, and emergency or response-time pills.

### Cited Findings
- Display licence numbers, certifications, insurance and affiliations; awards, guarantees and ratings above the fold; BBB and Google review marks; testimonials with stars on the home and service pages. — [WebFX](https://www.webfx.com/blog/home-services/website-design-handbook/)
- Review count and rating shown prominently, not in the footer. Years in business, licensing and insurance, service area and certification logos. Real photos of the team, trucks and work. — [Redefine Web](https://redefineweb.com/blog/home-service-web-design-best-practices/)
- Real-site placements: a Google rating badge in the first screen (Brian Ray's, Freshwater, Quartz); the licence number in a slim top bar (Quartz); the logo block carrying the licence and phone (Brian Ray's); licence/bonded/insured in the top bar (G.P); star rating and town pills next to the van hero (In-Line). — [UENI](https://ueni.com/blog/plumber-websites/)
- Review carousels with third-party logos. Google review plugin on the homepage (Smock). 5-star ratings above the fold (MIDSummer). — [Hook Agency](https://hookagency.com/hvac-websites/)
- UK installer: Trustpilot link, a "UK's most trusted" claim, a Price Match Promise (beats like-for-like quotes by £50), partner logos, Gas Safe and Refcom certification logos and FCA finance disclosures in the footer, plus hero trust bullets ("Installer workmanship guaranteed", "Finance options available"). — [BOXT](https://www.boxt.co.uk/)
- Framer trade template: a stats block with hard numbers, permit and warranty tags on service cards, and "verified reviews". — [Framer Electrical template](https://www.framer.com/community/marketplace/templates/electrical/)
- Auto: ASE badge (Cathedral), Google reviews built into the design (Eliot's), certifications and years in service prominent (Galson), warranties and free estimates above the fold (Pioneer). — [FreshySites](https://freshysites.com/blog/top-auto-repair-websites/)

### Inferences
- (synthesis) Component inventory for an AI builder:
  1. **Rating badge**: platform logo, stars and count; placed in the hero and header.
  2. **Credential strip**: a horizontal row of 3–6 icon+label chips (Licensed #, Insured, Bonded, Gas Safe/NICEIC/Meisterbetrieb-type local credential, years).
  3. **Logo wall** of associations and brands serviced.
  4. **Guarantee seal**: a circular badge such as "100% satisfaction" or "fixed price".
  5. **Response-time or availability pill**: "24/7", "Avg. arrival 60 min", or "Next-day install" with a live-dot indicator.
  6. **Team card**: photo, name, role, certification.
  7. **Van/fleet photo**.
  8. **Review card**: avatar, stars, platform icon, service tag, town.
  9. **Financing badge**.
  10. **Before/after pair** with a job caption.

### Gaps
- No evidence quantifying which trust component moves conversion most in trades.

## 8. Prototypicality evidence from template marketplaces and builders

### Takeaway
Builder and marketplace templates confirm the prototype: a services grid, testimonials, FAQ, quote form or booking app, service area, and process steps, with palettes of blue, warm brown, fresh green or "bold, strong colors". Framer's newer trade templates add stats blocks, permit/warranty tags and service-area plus FAQ blocks. WordPress/ThemeForest trade themes are generic multi-demo builders where booking is rarely built in.

### Cited Findings
- Framer Marketplace trade templates include Electrical ("premium", $59, sections listed in section 2), Airofix HVAC, Roofixa, Voltify, CarRepair and Aurix Home. Other trade templates in search results: PlumbingPro, Plumb Mate, Servix, ServiceHUB, Tradesman. — [Framer Electrical template page](https://www.framer.com/community/marketplace/templates/electrical/); [Framer PlumbingPro](https://www.framer.com/marketplace/templates/plumbingpro/); [Framer Plumb Mate](https://www.framer.com/marketplace/templates/plumb-mate/); [Framer ServiceHUB](https://framer.com/marketplace/templates/servicehub)
- Wix "Services & Maintenance" category: Landscaping (fresh green plus Wix Services), Cleaning Company (clean and inviting, Wix Bookings plus subscription plans), Cleaning v2 (bold strong colours), Home Improvement for plumbers, electricians and painters ("rugged, yet practical", parallax, reviews), HVAC Technician (testimonials, FAQs, prominent contact for quotes), Solar Installers (large vivid images, built-in quote form), Remodeling (warm brown). — [Wix templates](https://www.wix.com/website/templates/html/industrial/services-maintenance/2)
- WordPress trade themes (Envato Tuts+ roundup; dated 2021, retitled 2025): Air Supply, Repairer, Handylexo, HomeFix (bright, "energetic" colours), Buildguy, Airtech, Smartman, Plumbing (Elementor, appointment booking), Kempner, MrHandy (booking plus advanced forms), Boldman ("minimalist" demos), ProHauz (page transitions), Plumber. Common traits: responsive design, multiple demo homepages, one-click import, page builders. Booking is explicitly built in only for Plumbing and MrHandy. — [Envato Tuts+, WordPress themes for plumbers and home services](https://webdesign.tutsplus.com/wordpress-themes-for-plumbers-and-home-services--cms-36959a)

### Inferences
- (synthesis) Marketplace templates often look more "designed" than real trade sites, with more whitespace and stock imagery, while real high-converting sites are denser and more photo-of-own-van. An AI builder should default to template structure combined with the density, top-bar and real-photo conventions of real sites.

### Gaps
- Squarespace and ThemeForest bestseller rankings for trades could not be checked in the available calls. No sales or popularity data on which template styles dominate.

## 9. Real, current example sites (2023–2026)

### Takeaway
Representative live examples across trades, each with a style tag. Descriptions come from the cited 2024–2026 roundups unless they were fetched directly (BOXT). I did not visually inspect the others.

### Cited Findings
- **Jacobs Heating & Air Conditioning (Portland, US)**, https://jacobsheating.com. Smiling-couple hero, large header phone, bulleted differentiators. Classic Flat/Material local HVAC. — [Hook Agency (2026)](https://hookagency.com/hvac-websites/)
- **Bob's AC (US)**, https://bobsac.com. Navy, matte gray and bright blue, soft wave shapes, custom mascots, special offer by the form. Illustrative/mascot-led Flat. — [Hook Agency](https://hookagency.com/hvac-websites/)
- **Genz-Ryan (Minnesota, US)**, https://genzryan.com. Large "Book Appointment" buttons, Google rating badge top right, booking CTA on every page. Clean family-focused Flat. — [Hook Agency](https://hookagency.com/hvac-websites/); [WebFX](https://www.webfx.com/blog/home-services/website-design-handbook/)
- **Thelen Mechanical (US)**, https://thelenmechanical.com. Blue and orange, differentiator list, immediate lead form. Prototypical safety-colour Flat. — [Hook Agency](https://hookagency.com/hvac-websites/)
- **BOXT (UK)**, https://www.boxt.co.uk. "Fixed price in minutes" hero leading into a quote app, "installed from" product cards, numbered three-step process, Trustpilot, Gas Safe. Productised e-commerce style for home services (fetched Oct 2026). — [BOXT](https://www.boxt.co.uk/)
- **Men In Kilts (window/exterior cleaning, US/Canada)**, https://www.meninkilts.com. Character-led brand, kilt team photos, Google reviews, subtle scroll animation. Standout brand differentiation. — [htmlburger](https://htmlburger.com/blog/cleaning-websites-examples/)
- **Luxe Cleaning Co (Canada)**, https://luxecleaning.ca. High-end property imagery, video, spacious sans-serif. Luxury/Minimalist cleaning. — [htmlburger](https://htmlburger.com/blog/cleaning-websites-examples/)
- **More Hands Maid Service (US)**, https://morehands.com. Warm palette, rounded containers, illustrations, subtle animation. Friendly Illustrative/Claymorphism-adjacent. — [htmlburger](https://htmlburger.com/blog/cleaning-websites-examples/)
- **Cathedral Automotive (US)**, https://cathedralautomotive.com. Vintage car, red/black, ASE badge. Retro, for classic restoration. — [FreshySites (2026)](https://freshysites.com/blog/top-auto-repair-websites/)
- **West Coast Tire Pros (US)**, https://westcoasttire.com. Black, white and red, premium vehicles on a dark backdrop, live chat. Dark/premium auto. — [FreshySites](https://freshysites.com/blog/top-auto-repair-websites/)
- **Christian Brothers Automotive (US chain)**, https://cbac.com. Illustrated neighbourhood banner, teal ribbon, location links. Illustrative, family-friendly. — [FreshySites](https://freshysites.com/blog/top-auto-repair-websites/)
- **Rosebank Landscaping (UK, idstudio case)**, https://idstudio.co.uk/our-work/rosebank-landscaping/. Showcase-driven, soft greens and earth tones, professional photos and video. Organic/Minimalist. **Kinross House** (idstudio case), https://idstudio.co.uk/our-work/kinross-house/. Full-width image and video hero with elegant fonts. Luxury/Editorial heritage. — [idstudio (2025)](https://idstudio.co.uk/insights/web-design/landscape-garden-web-design/)

### Inferences
- (synthesis) For standout references, the shortlist is Men In Kilts (brand character), BOXT (productised UX), Cathedral Automotive (retro), and Kinross House or Rosebank (premium garden). For the prototype, use Jacobs Heating or Thelen.
- (synthesis) I could not confirm a live mover example: getbellhop.com, a once-prominent bold moving brand, now redirects to a domain-for-sale page (checked Oct 2026), so don't use it as an example.

### Gaps
- No verified live examples for painters/decorators, roofers, electricians or movers specifically, and none from continental Europe, Brazil, Japan or Australia apart from A Pristine Carpet Clean (AU, https://www.apristinecarpetclean.com.au/: clean white, custom icons, trust badges, per [htmlburger](https://htmlburger.com/blog/cleaning-websites-examples/)) and Height Cleaning (NZ, https://www.height.co.nz/).
- No Awwwards, Siteinspire or Land-book trade examples were retrieved. Gallery sites rarely feature local trades, which itself suggests the niche is conversion-driven rather than award-driven (inference).
