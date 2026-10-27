# Web design style, layout and UI/UX conventions: Hospitality, Food, Travel, Real Estate and Events

Niches: (a) hotels / boutique hotels / B&Bs / holiday rentals; (b) restaurants / cafés / bakeries / bars; (c) travel agencies / tours / experiences; (d) real estate agencies and property developers; (e) event venues and wedding/event services.
Scope: visual design, layout, UI/UX only. Research date: 2026-10-22. "Synthesis" marks the researcher's own inference. Items marked "[unverified]" come from general knowledge and were NOT checked against a live page this session.

---

## Q1. Visitor goals, main conversion actions, and the UI that supports them

### Takeaway
Every niche has one main "transaction" widget, and the strongest evidence-based rule across all of them is to make that widget visible right away. Hotels need a date/guest booking search above the fold. Restaurants need Reserve / Order / Menu in the header. Tours need an availability calendar plus a meeting-point map. Real estate needs a search bar with filters and a map. Venues need an enquiry / "schedule a tour" form. Boutique hotels are a special case: most visitors browse first, so the widget should be compact (progressive disclosure), not dominant.

### Cited Findings
**(a) Hotels / rentals**
- 99% of test participants on OTA, large-brand hotel and whole-property rental sites looked for the booking search on the homepage right away. 25% of benchmarked accommodation sites do not make booking search the primary homepage content. — [Baymard, Travel Accommodations booking search (Aug 2022)](https://baymard.com/blog/travel-accommodations-booking-search)
- At IHG, 78% of participants found the booking search below the fold. One Marriott participant took nearly 30 s to find a below-the-fold search. Cookie banners, travel advisories and chat widgets can cover low-placed search modules. — [Baymard (2022)](https://baymard.com/blog/travel-accommodations-booking-search)
- Boutique hotels differ: 73% of participants started by browsing property information and only 27% wanted to check availability first. Boutique sites still need a search module, because a lone "Book Now" button is easy to overlook (NobleDEN's "Book Now" under large animated imagery was missed). The recommended pattern is progressive disclosure: show only Check In / Check Out / Book Now, then reveal more fields on click (example: The Nolitan). — [Baymard (2022)](https://baymard.com/blog/travel-accommodations-booking-search)
- Recommended search-module styling: upper homepage, visible without scrolling, near full width, strong contrast against background imagery, a vibrant "Search" button, bold borders, larger inputs and font sizes, and all dropdowns fully visible without scrolling. Good examples: Booking.com, Airbnb (bright Search button over inspirational imagery), Plum Guide (near full width), Expedia. — [Baymard (2022)](https://baymard.com/blog/travel-accommodations-booking-search)
- Pickers that do not "adequately or accurately communicate availability" force users to verify availability another way, which leads to frustration and abandonment. — [Baymard date-picker examples](https://baymard.com/ecommerce-design-examples/date-picker)
- Sticky / floating "book now" widgets are a recognised pattern (One&Only Cape Town keeps a floating book widget visible while scrolling). Casin'anand Resort uses a fixed "check availability" option. — [HotelTechReport (orig. 2020, upd. Dec 2024)](https://hoteltechreport.com/news/hotel-website-designs); [htmlburger (Apr 2024, upd. Dec 2024)](https://htmlburger.com/blog/best-hotel-website-design/)
- Vendor best practice: keep required booking fields to a minimum and integrate a booking engine. — [htmlburger (2024)](https://htmlburger.com/blog/best-hotel-website-design/)

**(b) Restaurants / cafés / bars**
- Featured 2025 restaurant sites put "Order Now" / "Reserve" in the navigation or first section (Socrate: ordering button in nav; The Fifth: reservation button in nav; Sushi Seki: "Order Online" in first section; Craft House: phone, ordering and social in nav; Gramercy Tavern: homepage split into Bar vs Dining with reservations and private dining focus). — [UpMenu, 25 Best Restaurant Websites 2025 (vendor)](https://www.upmenu.com/blog/best-restaurant-websites-design/)
- Core pages per this vendor: home, menu/ordering, about, contact & location, hours, blog/news. Menu, hours, location and contact should be findable "within seconds". 2025 trend features: dietary menu filters, upsell at checkout, loyalty, order tracking, wallet payments. — [UpMenu (vendor)](https://www.upmenu.com/blog/best-restaurant-websites-design/)
- Claimed survey stats: 77% of diners visit a restaurant's website before choosing, and ~70% have been discouraged by a poorly designed site (PR Newswire survey, cited second-hand, not verified). — [UpMenu (vendor)](https://www.upmenu.com/blog/best-restaurant-websites-design/)

**(c) Tours / experiences**
- Baymard's tours research (1,700 h of testing; 7 sites benchmarked against 340+ parameters: Much Better Adventures, Take Walks, Extranomical Tours, Ziptrek Ecotours, Wild Rover Tours, Sea Saffron, Sea Paradise) recommends that the Tour Details page always include a map of the departure/meeting point. — [Baymard Tours & Experiences benchmark (Aug 2023)](https://baymard.com/research-articles/tours-and-experiences-benchmark-2023)
- Users opened the tour date picker to get tour information, and calendars that did not link to tour details forced long detours. Availability must be shown clearly and accurately. — [Baymard date-picker examples](https://baymard.com/ecommerce-design-examples/date-picker)

**(d) Real estate**
- In the NAR Generational Trends report (2022), buyers rated these website features "very useful": photos 84%, floor plans 55%, virtual tours 43%, video 28%. — [BoxBrownie citing NAR 2022](https://www.boxbrownie.com/b/the-nar-report-that-helps-sell-homes-in-a-slowdown)
- Recommended search patterns: intuitive filters, interactive maps and comparison tools. Campion & Company shows an MLS search filtering by neighbourhood, price and features. Damac Properties uses unit filters (floor, size, price) that highlight units on a 3D building model, which suits developers. — [Azuro Digital, 10 Best Real Estate Website Designs 2026 (Oct 2025, upd. Mar 2026)](https://azurodigital.com/real-estate-website-examples/)

**(e) Venues / weddings**
- Venue sites are built around CTAs to "inquire", "schedule a tour" and "book a date", with heavy photography and video plus testimonials. — [InsideOut portfolio, wedding venue websites](https://insideout.com/portfolio/wedding-venue-websites/)

### Inferences
- Synthesis: a primary-CTA map for an AI builder:
  - Chain or large hotel / rental platform: a full-width search bar (destination, dates, guests) in the hero.
  - Boutique hotel / B&B: a compact date bar (Check-in, Check-out, Book) over or under the hero, plus a sticky "Book" button in the header and a bottom bar on mobile.
  - Holiday rental (single property): an availability calendar with nightly price on the property page, plus a sticky price/"Reserve" card on desktop and a bottom bar on mobile.
  - Restaurant: header buttons Reserve (links to OpenTable/Resy/TheFork/SevenRooms widget) + Menu + Order. Show hours and address in the first screen or footer.
  - Café / bakery: Menu + Order/Pickup + Hours/Location. Reservations are often not needed.
  - Bar: Hours, Events/What's on, Book a table, Private hire.
  - Tour operator: Tour cards on the home page. The tour detail page has a sticky price + "Check availability" box, a calendar that shows sold-out and price per date, and a meeting-point map.
  - Travel agency (bespoke): an enquiry / "Start planning" form or consultation booking instead of instant booking.
  - Real estate agency: a search bar (Buy/Rent toggle, location, price, beds) and listing grid + map split view. On the detail page, "Schedule a viewing" / "Contact agent" is sticky.
  - Property developer: "Register interest" / "Download brochure" / "Book a viewing", plus a unit selector (floor plan / 3D building) and an availability table.
  - Venue / wedding services: "Check your date" / "Request brochure / pricing" / "Book a tour" forms, plus a gallery and testimonials.

### Gaps
- No public NN/g study found specifically on hotel or restaurant websites in 2024–2026. NN/g's general PDF guidance is used for menus (see Q3).
- No primary data found on restaurant reservation/ordering conversion by CTA placement. The restaurant stats are vendor-cited, second-hand.
- No UX research found on wedding venue sites specifically (agency portfolios only).

---

## Q2. Main layout and page patterns (heroes, room pages, galleries, menus, listing cards and detail pages, calendars, mobile)

### Takeaway
Hospitality and venues are dominated by full-bleed photo/video heroes followed by alternating image–text "story" sections. Real estate and OTAs are dominated by functional search → card grid → detail-page templates. Restaurants sit in between: an atmospheric hero, then very utilitarian menu/hours/location blocks.

### Cited Findings
- Hotel heroes: slow-motion video openers (Esperanza, Bungalows Key Largo), hero/drone video (Song Saa, Little Palm Island, Samsara Ubud), background video (Hotel Sanders, Royal Savoy Lausanne), full-screen heroes (Hotel 23, Hotel Neptun), "framed" background videos (Alta House). — [HotelTechReport (upd. Dec 2024)](https://hoteltechreport.com/news/hotel-website-designs); [htmlburger (2024)](https://htmlburger.com/blog/best-hotel-website-design/)
- Other hotel layout patterns:
  - Magazine-style layout with puzzle-like image blocks that work on mobile (Casa Angelina).
  - Single-page, no-scroll site with room galleries in the menu (The Maritime Hotel).
  - Scrolling text and animation over photos (Hotel Particulier).
  - Preloaders (Yoyogi Park Trunk, Hotarutei, Amariah).
  - Motion typography (Wake Medellín).
  - Custom cursors (Le Mirabeau spotlight cursor, Samsara Ubud circle cursor).
  - [HotelTechReport](https://hoteltechreport.com/news/hotel-website-designs); [htmlburger](https://htmlburger.com/blog/best-hotel-website-design/)
- Hotel navigation advice: group related content (dining, spa) under distinct headings and cross-link pages. Use short videos for amenities, experiences and local attractions. — [htmlburger (2024)](https://htmlburger.com/blog/best-hotel-website-design/)
- B&B patterns:
  - Images of the house at different times of day, with scrolling that reveals history and nearby attractions (Portland's White House).
  - Main menu given over to local-area guidance (The Black Walnut).
  - [HotelTechReport](https://hoteltechreport.com/news/hotel-website-designs)
- Restaurant hero patterns: homepage video (Restaurant DANIEL, Sushi Kushi, Tufino, Piatto, Urbane Café), full-bleed image (Vedge, Ra Sushi grid of full-bleed images), image sliders (Abuelo's, Socrate). Menu shown directly on the homepage (Maharaja), or a homepage menu slider (Abuelo's). Location selector leading to per-location menus for multi-site chains (Sushi Kushi). — [UpMenu (2025)](https://www.upmenu.com/blog/best-restaurant-websites-design/)
- Real estate patterns:
  - Full-screen imagery with interactive galleries and video tours (Altman Brothers).
  - Immersive full-screen photo/video (Caldera House).
  - Prominent sales metrics with MLS search (Campion).
  - 3D Unreal Engine tours with unit filters on a 3D model (Damac).
  - A "Stories" content section (Angela Andronache).
  - [Azuro Digital (2025/26)](https://azurodigital.com/real-estate-website-examples/)
- Listing quality gap: in a BoxBrownie study of 25,000+ US listings on realtor.com/Zillow (Mar–Jun 2021), 94% lacked a virtual tour, 84% lacked a floor plan (90% for single-family homes), and fewer than 30% used professional photo best practice (HDR/bracketed). [Older evidence, 2021] — [Inman (Jul 2021)](https://inman.com/2021/07/08/vast-majority-of-real-estate-listings-lack-good-visuals-study)
- Framer's marketplace groups templates as "Hospitality" (Food, Hotels, Restaurants, Travel) and "Events" (Conferences, Music, Sports, Weddings). Real-estate templates describe themselves as including "listing pages, galleries, and inquiry forms". — [Framer Marketplace, Real Estate](https://www.framer.com/marketplace/templates/category/real-estate/)

### Inferences
Synthesis: page templates an AI builder should generate.
- **Hotel / boutique / B&B**
  - Home: hero (video loop ≤15 s or still) with the date bar, intro statement, rooms teaser carousel, dining/spa/experiences split sections, location/neighbourhood map, reviews strip, press/awards logos, offers, footer with address, phone and booking.
  - Rooms index: cards showing photo, name, size m², bed type, max guests, "from" price, and View / Book.
  - Room detail: gallery (lightbox, 6–15 images), key facts icon row (size, bed, view, occupancy), amenities list, floor plan for suites, a sticky "Check availability" box, and "other rooms".
  - Mobile: a bottom sticky "Book" bar, a hamburger menu with Book as a separate visible button, and a full-screen date-picker sheet.
- **Holiday rental (single property)**: an Airbnb-like detail page. Mosaic gallery (1 large + 4 small), "Show all photos", key facts (guests, bedrooms, beds, baths), amenities, an inline calendar with min-stay rules, a sticky price card (desktop right column / mobile bottom bar), a location map, house rules, and reviews.
- **Restaurant**: atmospheric hero with Reserve / Menu buttons, short story, featured dishes, menu section (HTML, tabbed by service: Lunch / Dinner / Drinks / Desserts, with dietary icons), hours and address with an embedded map, private dining/events, gift cards, press, Instagram strip.
  - Multi-location brands need a location picker first.
  - Cafés / bakeries lean on product cards (pastries, coffee) and order-for-pickup.
  - Bars lean on events calendar, drinks list and private hire.
- **Tours**
  - Home: a destination/activity search or category tiles, then a featured tours grid.
  - Tour cards: image, duration, group size, rating, "from" price.
  - Tour detail: gallery, highlights, day-by-day itinerary accordion, inclusions/exclusions, meeting-point map, availability calendar with prices, a sticky booking box, reviews, FAQ.
- **Real estate**
  - Agency: search hero, then a results page with a list ↔ map split view (desktop) and a map/list toggle (mobile).
  - Listing cards: photo carousel, price, beds/baths/m², address, badge (New / Reduced / Under offer), favourite heart.
  - Listing detail: big gallery + "floor plan" + "virtual tour" + "video" tabs, key facts grid, description, features, map + neighbourhood, an energy rating where it applies (EU/UK), mortgage calculator, a sticky agent-contact card.
  - Developer: project landing with hero render/film, location, a residence-types grid, an interactive siteplan / 3D building unit picker with an availability table, amenities, a construction-progress timeline, gallery, brochure download, register-interest form.
- **Venue / wedding**: hero film, then spaces (capacity per layout: seated/standing), packages/pricing ("from" or brochure gate), a real-weddings gallery, preferred suppliers, accommodation, FAQ, testimonials, and an enquiry form with date, guest count and budget.

### Gaps
- No quantitative data found on the optimal number of gallery images, or on mosaic vs carousel galleries for hotels and rentals.
- Did not verify current (2026) live designs of each HotelTechReport example. That list began in 2020, so some sites may have been redesigned.

---

## Q3. UI/UX best practices with evidence (NN/g, Baymard, real-estate studies, menu usability)

### Takeaway
The hard evidence is concentrated in Baymard (accommodations 2022/2026; tours 2023), NN/g (PDF), and NAR/BoxBrownie (real-estate visuals). Restaurant-menu evidence is mostly NN/g's general PDF guidance plus accessibility arguments. Vendor articles add many uncited claims.

### Cited Findings
- **Baymard Travel Accommodations UX benchmark (Jan 15, 2026).**
  - Sites assessed: Booking.com, Airbnb, Hyatt, Best Western, Trip.com, Expedia, Shangri-La, Esmé Hotel and HomeToGo, against 590+ parameters.
  - Scores range from "poor" to "decent". Only one site/app rates "decent" and none reach "good".
  - Common issues: booking search not made primary on the homepage, missing transparent pricing, ineffective filters, weak reviews.
  - Sites generally do well on visual consistency, pricing visibility and clear imagery.
  - [Baymard 2026 benchmark](https://baymard.com/research-articles/travel-accommodations-ux-benchmark-2026)
- **Baymard principle**: users need "streamlined search and booking tools and well-organized, detailed content to compare and book with confidence", whether the site is an OTA, chain, boutique hotel or rental platform. — [Baymard 2026](https://baymard.com/research-articles/travel-accommodations-ux-benchmark-2026)
- **Baymard placement and styling rules**: booking search at the top, near full width, high contrast. Progressive disclosure for boutique hotels. Avoid cookie banners and chat widgets covering the search (Sonder; Plum Guide on mobile). — [Baymard (2022)](https://baymard.com/blog/travel-accommodations-booking-search)
- **Baymard tours**: meeting-point map on Tour Details. Link to third-party review sources, aggregate ratings, awards and endorsements. — [Baymard tours benchmark (2023)](https://baymard.com/research-articles/tours-and-experiences-benchmark-2023)
- **NN/g, "Avoid PDF for On-Screen Reading"** (Nielsen & Kaley, Jun 28, 2020):
  - PDFs are built for print, cause disorientation, block scan-and-scroll reading, are "suboptimal" on phones, are heavy (data and crashes), and pile up tabs on mobile.
  - Recommendations: HTML gateway pages, label PDF links with file size and page count, keep files small.
  - NN/g explicitly names "a one-page menu" among acceptable printable PDFs.
  - Evidence date: 2020, flagged as older but still current guidance.
  - [NN/g](https://www.nngroup.com/articles/avoid-pdf-for-on-screen-reading/)
- **PDF menu accessibility**: screen readers cannot interpret most PDFs, users cannot reflow or zoom, and keyboard navigation is not supported. Source is a vendor article with mostly uncited claims. — [JVF (2024/25)](https://jvf.com/why-restaurants-should-avoid-pdf-menus/); see also [BOIA, PDF menus accessibility](https://www.boia.org/blog/why-pdf-menus-are-a-problem-for-accessibility) (search result, not fetched)
- **Real estate**: buyers rate photos 84%, floor plans 55% and virtual tours 43% "very useful" (NAR 2022) [BoxBrownie/NAR](https://www.boxbrownie.com/b/the-nar-report-that-helps-sell-homes-in-a-slowdown). An NAR survey cited by Inman says 67% want floor plans and 58% want virtual tours [Inman 2021](https://inman.com/2021/07/08/vast-majority-of-real-estate-listings-lack-good-visuals-study). Note: the percentages differ by survey/year and question wording (want vs "very useful").
- **Real estate (agency view)**: mobile-first, because most property searches happen on phones/tablets. Fast load and smooth animation signal professionalism. Trust comes from specifics. — [Azuro Digital (2025/26)](https://azurodigital.com/real-estate-website-examples/)

### Inferences
- Synthesis, menu rule for the builder: always render the menu as responsive HTML (sections, prices aligned right, dietary/allergen icons, optional filters). Optionally add a "Download PDF (1 page, 300 KB)" link for printing. Never ship PDF-only menus.
- Synthesis, pricing transparency: show "from €X / night" on room cards, and totals including taxes and fees before the final step. This follows Baymard's finding that transparent pricing is a common failure.
- Synthesis, the dates/guests module on mobile should open as a full-screen sheet, so menus are fully visible without scrolling mid-entry (Baymard's scroll-mid-entry error finding).

### Gaps
- Baymard's detailed guidelines (date-picker specifics, room selection, gallery behaviour) are behind a paywall, so only the public summaries are cited.
- No peer-reviewed restaurant-menu usability study found. The evidence is NN/g's general PDF guidance plus vendor/accessibility org claims.
- No primary studies found on map-vs-list default views for property search.

---

## Q4. The typical visual style per niche (mapped to style labels)

### Takeaway
- Hotels: the default is **Luxury / Editorial**. That means a serif display face, a full-bleed photo/video hero, generous white space and muted palettes. Boutique and lifestyle hotels push towards **Editorial-magazine**, **Retro/Mid-century** or **Maximalist**.
- Restaurants: fine dining defaults to **Minimalist/Luxury**, and casual/QSR to **bold Flat** brand colour with big order buttons.
- Cafés and bakeries: **Organic / Illustrative**.
- Real estate agencies: a **clean Flat/Swiss listing UI**. Luxury agencies and developers: **Luxury minimal** with immersive video/3D.
- Tours: **Editorial travel** photography with card grids.
- Venues: **Romantic Editorial/Luxury** (serif, soft palettes, big galleries).

### Cited Findings
- **Luxury hotels**: minimalist design with large imagery and storytelling (7132), multimedia storytelling (Badrutt's Palace), custom cursors and drone video (Samsara Ubud, Le Mirabeau). — [HotelTechReport](https://hoteltechreport.com/news/hotel-website-designs)
- **Boutique hotels**:
  - Warm colours, trendy font, much white space (Vesper).
  - A dominant scrolling header with bold colours and large fonts (El Fenn, which reads as Maximalist).
  - Clean lines with the architecture as focus (Hotel Bella Grace).
  - Minimal sidebar menu over bright tropical colours (Donkey Bay Inn).
  - [HotelTechReport](https://hoteltechreport.com/news/hotel-website-designs)
- **Motels** (Retro / Kitsch / Mid-century): retro-tropical (The Drifter), bright colours and bold patterned wallpaper, "playful, kitschy" (Austin Motel), sepia photos mixed with illustrations and rustic fonts (Tourists). — [HotelTechReport](https://hoteltechreport.com/news/hotel-website-designs)
- **B&Bs** (Organic / homey): a homey, handmade-feeling logo and fonts, "deliberately informal" (Colette's), natural colours with simple branding (Kennebunkport Captains). — [HotelTechReport](https://hoteltechreport.com/news/hotel-website-designs)
- **Apart-hotels**: chic minimalist design for high-end positioning (La Réserve Paris), bright airy photos (Domio). — [HotelTechReport](https://hoteltechreport.com/news/hotel-website-designs)
- **General hotel guidance**: simple design, minimal layouts, big images, plenty of white space, custom/luxurious fonts. — [htmlburger (2024)](https://htmlburger.com/blog/best-hotel-website-design/)
- **Restaurants**:
  - Minimalist fine dining (Gramercy Tavern, Jungsik two-section homepage, Socrate).
  - Elegant with homepage video (DANIEL).
  - Minimal white and red with a Japanese aesthetic (A Single Pebble).
  - Nightlife-sleek, i.e. Dark (The Fifth).
  - Bold contrasting colours with big order buttons, i.e. Flat/QSR (The Kebab Shop, Russo's).
  - Vibrant Caribbean imagery (Kokomo).
  - [UpMenu (2025)](https://www.upmenu.com/blog/best-restaurant-websites-design/)
- **Real estate**:
  - Minimalist luxury with white space and a premium palette (Brightstone).
  - Warm luxury, video-forward (Kumara Wilcoxon).
  - Immersive earth-tone luxury (Caldera House).
  - Bold contemporary with dramatic typography, strong contrast and an "art-gallery feel" (Berdan), which is Typographic-led / Editorial.
  - Clean luxury with refined typography (Fridman Group).
  - Tech-forward luxury with 3D (Damac), which is Dark/tech plus Immersive.
  - [Azuro Digital (2025/26)](https://azurodigital.com/real-estate-website-examples/)
- **Venues**: photography- and video-led sites designed to help visitors picture the event. — [InsideOut](https://insideout.com/portfolio/wedding-venue-websites/)

### Inferences
Synthesis, the typical mapping (what MOST sites look like) for the builder's default recommendation:

| Sub-niche | Default style label(s) | Type | Palette | Signature components |
|---|---|---|---|---|
| Luxury hotel / resort | Luxury + Editorial + Immersive scroll (light) | High-contrast serif display (Didone/old-style) + thin sans; wide letter-spacing caps for nav | Off-white / sand / black / one deep accent (forest, navy, oxblood) | Full-bleed video hero, overlay date bar, slow fades, split image-text |
| Boutique / lifestyle hotel | Editorial (magazine) ± Retro/Mid-century or Maximalist | Characterful serif or quirky grotesk | Brand-specific, warmer, sometimes bold | Asymmetric image collage, illustrated touches, neighbourhood guide |
| B&B / guesthouse / agriturismo | Organic / Scandinavian-Japandi / rustic | Soft serif + humanist sans, some handwritten | Earth tones, linen, sage | Simple single page, host story, local guide, compact booking widget |
| Holiday rental (single/small portfolio) | Minimalist / Scandinavian, OTA-like UI | Clean sans | Neutral | Mosaic gallery, sticky price card, calendar |
| Motel / hostel | Retro / Mid-century / Y2K / Neo-brutalist | Display retro, chunky | Saturated | Patterns, stickers, playful illustration |
| Fine dining | Minimalist / Luxury (light or Dark) | Elegant serif or refined sans | Monochrome + 1 accent | Single image/video, sparse nav, Reserve |
| Casual restaurant / QSR / chain | Flat / bold brand, sometimes Neo-brutalist | Heavy sans | Brand colours | Big Order button, location picker, menu cards with photos |
| Café / bakery | Organic + Illustrative (hand-drawn), Scandinavian | Rounded/handwritten + sans | Cream, kraft, pastel | Product tiles, story, hours card, pickup ordering |
| Bar / cocktail / club | Dark + Retro/Art Deco or Kinetic typography | Condensed display / Deco | Dark with neon or gold | Events list, drinks, private hire |
| Tour operator / experiences | Editorial travel + card grid (Flat/Material UI) | Clean sans, bold headlines | Photo-led, a nature/adventure accent | Tour cards, filters, itinerary accordion, map |
| Luxury travel agency (bespoke) | Editorial / Luxury | Serif | Neutral | Story-led journeys, "Start planning" form |
| Real estate portal / agency | Swiss / Flat clean listing UI | Neutral sans (Inter-like) | White, one brand accent | Search bar, list+map split, cards |
| Luxury agency / boutique broker | Luxury minimal / Typographic-led | Serif or refined sans | Black/white/stone | Full-screen imagery, curated listings, sales stats |
| Property developer / new development | Luxury + Immersive scroll / Dark-tech (3D) | Serif or wide sans | Muted, render-driven | Hero film/renders, residence-types grid, unit picker, register interest |
| Wedding venue / event services | Editorial-romantic Luxury / Organic | Script or serif + sans | Blush, ivory, sage, gold | Gallery, spaces/capacities, packages, enquiry form |
| Corporate/conference venue | Clean corporate Swiss/Flat | Sans | Neutral | Capacity charts, floor plans, RFP form |

### Gaps
- No quantitative survey found that classifies hotel/restaurant site styles by share (e.g. "% using serif"). The mapping is qualitative synthesis from curated example lists, which have selection bias towards "beautiful" sites.

---

## Q5. Styles that stand out successfully, and styles to avoid

### Takeaway
Distinctive styles work when the booking/reservation path stays standard and visible. Brands that stand out with retro (Austin Motel), maximalist (El Fenn), motion-type (Wake Medellín) or 3D (Damac) styling keep a clear CTA. Heavy immersive treatments (preloaders, animated heroes without a search module, custom cursors, pop-ups) carry documented risks: missed booking CTAs, slow loads and covered widgets.

### Cited Findings
- Successful differentiators: retro/kitsch motels (Austin Motel, The Drifter, Tourists), maximalist bold colour and type (El Fenn), motion typography (Wake Medellín), custom shapes (Threehouse, Vunabaka), magazine-style puzzle layouts (Casa Angelina). — [HotelTechReport](https://hoteltechreport.com/news/hotel-website-designs); [htmlburger](https://htmlburger.com/blog/best-hotel-website-design/)
- Real estate differentiators: an art-gallery typographic style (Berdan), 3D Unreal Engine unit explorer (Damac), lifestyle storytelling (Indigo Road, Angela Andronache). — [Azuro Digital](https://azurodigital.com/real-estate-website-examples/)
- Risk evidence:
  - NobleDEN's lone "Book Now" under large animated imagery was missed by users.
  - Below-the-fold search led to delays and errors (IHG, Marriott).
  - Cookie banners and chat widgets covered search modules.
  - [Baymard (2022)](https://baymard.com/blog/travel-accommodations-booking-search)
- Hotel design guidance warns that video should not slow the page. — [HotelTechReport](https://hoteltechreport.com/news/hotel-website-designs)
- Google statistic (second-hand): 53% of mobile visits are abandoned when load time exceeds 3 s. — cited in [JVF](https://jvf.com/why-restaurants-should-avoid-pdf-menus/) (original Google source not linked; older, c. 2016–2018)

### Inferences
- Synthesis, avoid for these niches:
  - PDF-only menus.
  - Preloaders and fake-404 / intro animations before content (seen on Trunk and Hotarutei). They are memorable but delay the booking path, so use them only for flagship luxury/design brands with a skip option.
  - Hero carousels with auto-rotate and no booking bar.
  - Custom cursors on touch devices, where they do nothing.
  - Scroll-jacking on listing/search pages.
  - Glassmorphism date bars over busy photos without enough contrast (conflicts with Baymard's contrast rule).
  - Neumorphism/Claymorphism, which are rarely fit for photo-led hospitality and have weak contrast.
  - Brutalist raw layouts for luxury real estate or venues, where they undermine trust.
  - Pop-ups at entry (special-offer popups are common, e.g. La Fantaisie, but should be delayed and dismissible).
- Synthesis, safe differentiation levers: an expressive typeface and colour, art direction of photography, an illustrated map/neighbourhood guide, kinetic type confined to the hero headline, bento-grid "experiences/amenities" sections, an editorial journal. Keep the booking/search/reserve modules as standard UI patterns.

### Gaps
- No A/B test data found comparing immersive vs plain hotel homepages for direct-booking conversion.

---

## Q6. Trust UI components

### Takeaway
Trust blocks are niche-specific and mostly third-party:
- Hotels: TripAdvisor/Google/Booking.com ratings, awards (Michelin Keys, Condé Nast, Forbes), press logos, a direct-booking price guarantee.
- Restaurants: press quotes, Michelin/guide awards, Google/Yelp ratings.
- Tours: aggregate ratings plus third-party reviews (Tripadvisor, Trustpilot, GetYourGuide), awards, safety/licensing.
- Real estate: sales stats, testimonials, credentials, verified-agent badges.
- Venues: testimonials, "as featured in" wedding press, real-wedding galleries.

### Cited Findings
- Hotels:
  - Vesper highlights a 100% TripAdvisor rating on its homepage.
  - 18 Micon Street places review and press logos beside property images.
  - Nobnocket Inn shows award highlights and a "vote for us" call.
  - Badrutt's Palace is award-winning, with an events feed.
  - [HotelTechReport](https://hoteltechreport.com/news/hotel-website-designs)
- Hotel best practice: show authentic guest reviews and respond to them promptly. — [htmlburger](https://htmlburger.com/blog/best-hotel-website-design/)
- Weak review functionality is a common accommodation-site failure. — [Baymard 2026](https://baymard.com/research-articles/travel-accommodations-ux-benchmark-2026)
- Tours: link to third-party review sources, aggregate ratings, awards and endorsements. — [Baymard tours (2023)](https://baymard.com/research-articles/tours-and-experiences-benchmark-2023)
- Restaurants: Craft House shows its Yelp ranking up front, and DANIEL, Adda and Kokomo feature press sections. Social proof (reviews, press) is recommended. — [UpMenu](https://www.upmenu.com/blog/best-restaurant-websites-design/)
- Real estate: "Build trust with specifics": sales achievements, testimonials, credentials, market statistics (e.g. Campion's prominent sales metrics; Kumara Wilcoxon $1.3B+ career sales; Fridman Group $3B+). — [Azuro Digital](https://azurodigital.com/real-estate-website-examples/)
- Venues: client testimonials. — [InsideOut](https://insideout.com/portfolio/wedding-venue-websites/)

### Inferences
- Synthesis, reusable trust UI blocks for the builder:
  1. **Rating badge row**: platform logo + score + count (e.g. "Google 4.8 · 1,240 reviews"; "Tripadvisor Travellers' Choice"). Put it under the hero or near the booking widget.
  2. **Press/award logo strip**: monochrome logos.
  3. **Review carousel/cards**: quote, name, origin, date, source.
  4. **Direct-booking benefits box** (hotels): best price, free cancellation, perks, next to the booking widget.
  5. **Agent card** (real estate): photo, name, licence/verified badge, phone/WhatsApp, response time.
  6. **Sales-stats counters** (luxury agencies).
  7. **Certifications** (sustainability labels, tourism licence, insurance) for tours.
  8. **"Featured in" wedding press + real-wedding gallery** for venues.
  9. **Secure payment / cancellation-policy microcopy** near Book buttons (design element only).
- Synthesis: a review widget should show the source and date (the transparency principle consistent with Baymard's reviews findings). Avoid unsourced star ratings.

### Gaps
- No independent study found quantifying the conversion lift of specific badges (e.g. TripAdvisor widget) on hotel direct-booking sites.

---

## Q7. Evidence from template marketplaces and builders

### Takeaway
Every major builder has dedicated categories for these niches, which confirms that they are high-volume, convention-driven verticals. The template structures (listing pages, galleries, inquiry forms, booking widgets) mirror the patterns above.

### Cited Findings
- Framer Marketplace: a "Hospitality" parent category with Food, Hotels, Restaurants and Travel subcategories, and an "Events" parent with Conferences, Music, Sports and Weddings. The Real Estate category lists 24+ templates (e.g. Auren Estate, Vantara Living, VistaHaven, Property Manager, Prestix, Royal) described as including "listing pages, galleries, and inquiry forms". — [Framer Marketplace, Real Estate](https://www.framer.com/marketplace/templates/category/real-estate/)
- ThemeForest WordPress subcategories include Real Estate, Wedding, Directory & Listings, Entertainment and Retail. Restaurant, hotel and travel appear as popular searches rather than subcategories. — [ThemeForest WordPress](https://themeforest.net/category/wordpress)
- Webflow: there are dedicated hotel templates (e.g. Pedro Garay Hotel, Josefin Hotel, Rosello Hotel) and third-party hotel template sellers (BRIX Templates, Webestica). — search results: [Webflow Josefin Hotel](https://webflow.com/templates/html/josefin-hotel-hotel-website-template), [Webflow Rosello](https://webflow.com/templates/html/rosello-hotel-website-template), [BRIX hotel templates](https://brixtemplates.com/webflow-templates/hotel-webflow-templates), [Webestica hotel](https://www.webestica.com/category/hotel) (not fetched; names only)
- TemplateMonster has a "Wedding Venues" template collection. — [TemplateMonster (search result)](https://www.templatemonster.com/website-templates/28059.html)
- Squarespace wedding-website and venue templates are covered by third-party roundups. — [htmlburger Squarespace wedding](https://htmlburger.com/blog/squarespace-wedding-websites/) (not fetched)

### Inferences
- Synthesis: template thumbnails in these categories (from general familiarity, [unverified this session]) are dominated by:
  - Hotels: serif-headline + full-bleed hero + booking bar.
  - Restaurants: dark/moody food photography + serif or a large type menu.
  - Real estate: clean white with a search bar, or black luxury.
  - Travel: big landscape hero + tour cards.
  - Wedding: soft palette + script/serif.
- That supports the defaults in Q4.

### Gaps
- Could not retrieve template counts per category (ThemeForest and Framer pages did not show totals). Squarespace and Wix category pages were not fetched.
- Visual style of template thumbnails could not be assessed via text fetch.

---

## Q8. Real, current example sites per niche (with style notes)

### Takeaway
Below are verified-by-source examples (from 2024–2026 roundups) plus well-known references marked [unverified]. Roundups have selection bias and some originate earlier (HotelTechReport list first published 2020).

### Cited Findings
**(a) Hotels / B&Bs / rentals**
- One&Only Cape Town — https://www.oneandonlyresorts.com/cape-town — simple, striking, floating book widget (Luxury). — [HotelTechReport](https://hoteltechreport.com/news/hotel-website-designs)
- Casa Angelina — https://www.casangelina.com/ — magazine-style puzzle image blocks (Editorial). — [HotelTechReport](https://hoteltechreport.com/news/hotel-website-designs)
- El Fenn (Marrakech) — https://el-fenn.com/ — bold colours, large fonts (Maximalist). — [HotelTechReport](https://hoteltechreport.com/news/hotel-website-designs)
- Austin Motel — https://austinmotel.com/ — patterned, kitschy (Retro). — [HotelTechReport](https://hoteltechreport.com/news/hotel-website-designs)
- 7132 Hotel (Vals) — https://7132.com/en — minimal, large imagery (Minimalist Luxury). — [HotelTechReport](https://hoteltechreport.com/news/hotel-website-designs)
- Samsara Ubud — https://www.samsaraubud.com/ — custom cursor, drone video (Immersive/Organic Luxury). — [HotelTechReport](https://hoteltechreport.com/news/hotel-website-designs)
- Royal Savoy Lausanne — https://royalsavoylausanne.com/en — custom fonts, background video (Luxury). — [htmlburger 2024](https://htmlburger.com/blog/best-hotel-website-design/)
- Wake Medellín — https://www.wakemedellin.com/ — motion typography (Kinetic typography). — [htmlburger 2024](https://htmlburger.com/blog/best-hotel-website-design/)
- Wolny Las — https://wolnylas.pl/ — serene forest imagery (Organic/Japandi). — [htmlburger 2024](https://htmlburger.com/blog/best-hotel-website-design/)
- Colette's B&B — https://colettes.com/ — homey handmade fonts (Organic/Illustrative B&B). — [HotelTechReport](https://hoteltechreport.com/news/hotel-website-designs)
- Booking UX references: The Nolitan (progressive-disclosure date bar), Plum Guide (full-width search), Esmé Hotel (benchmarked boutique). — [Baymard](https://baymard.com/blog/travel-accommodations-booking-search); [Baymard 2026](https://baymard.com/research-articles/travel-accommodations-ux-benchmark-2026)

**(b) Restaurants / cafés / bars**
- Gramercy Tavern — https://www.gramercytavern.com/ — minimalist, bar/dining split. — [UpMenu](https://www.upmenu.com/blog/best-restaurant-websites-design/)
- Restaurant DANIEL — https://www.danielnyc.com/ — elegant, homepage video (Luxury). — [UpMenu](https://www.upmenu.com/blog/best-restaurant-websites-design/)
- Jungsik — https://www.jungsik.com/ — minimalist two-section (fine-dining Minimalist). — [UpMenu](https://www.upmenu.com/blog/best-restaurant-websites-design/)
- A Single Pebble — https://asinglepebble.com/ — white/red Japanese aesthetic (Minimalist/Japandi). — [UpMenu](https://www.upmenu.com/blog/best-restaurant-websites-design/)
- The Dead Rabbit (bar) — https://thedeadrabbit.com/ — toned contrasting colours, heritage content. — [UpMenu](https://www.upmenu.com/blog/best-restaurant-websites-design/)
- The Fifth (rooftop bar) — https://www.thefifthoc.com/ — sleek nightlife (Dark). — [UpMenu](https://www.upmenu.com/blog/best-restaurant-websites-design/)
- The Kebab Shop — https://thekebabshop.com/ — bold colours, big order button (Flat/QSR). — [UpMenu](https://www.upmenu.com/blog/best-restaurant-websites-design/)
- Kokomo — https://www.kokomonyc.com/ — vibrant Caribbean imagery. — [UpMenu](https://www.upmenu.com/blog/best-restaurant-websites-design/)
- Cafés/bakeries: UpMenu has separate café and bakery roundups ([cafés](https://www.upmenu.com/blog/best-cafe-coffee-shop-websites), [bakeries](https://www.upmenu.com/blog/best-bakery-websites), [bars](https://www.upmenu.com/blog/best-bar-websites)). Not fetched, so no specific sites are cited here.

**(c) Travel / tours / experiences**
- Baymard-benchmarked tour sites: Much Better Adventures, Take Walks, Ziptrek Ecotours, Wild Rover Tours, Extranomical Tours. Kid & Coe appears in the date-picker examples. — [Baymard tours](https://baymard.com/research-articles/tours-and-experiences-benchmark-2023); [Baymard date picker](https://baymard.com/ecommerce-design-examples/date-picker)
- Destination sites (DMO, editorial travel): Go Hawaii https://www.gohawaii.com, Visit California https://www.visitcalifornia.com, Discover Puerto Rico https://www.discoverpuertorico.com, Visit Philadelphia https://www.visitphilly.com. All are visual-storytelling and immersive-media led. — [CyberOptik (undated; ©2026)](https://www.cyberoptik.net/blog/best-travel-tourism-websites)

**(d) Real estate**
- Campion & Company — https://campionre.com/ — clean, MLS filters, sales metrics. — [Azuro](https://azurodigital.com/real-estate-website-examples/)
- The Altman Brothers — https://www.thealtmanbrothers.com/ — full-screen imagery, video tours (Luxury minimal). — [Azuro](https://azurodigital.com/real-estate-website-examples/)
- Caldera House — https://calderahouse.com/ — immersive, earth tones. — [Azuro](https://azurodigital.com/real-estate-website-examples/)
- Berdan Real Estate — https://berdanrealestate.com/ — dramatic typography, art-gallery feel (Typographic-led/Editorial). — [Azuro](https://azurodigital.com/real-estate-website-examples/)
- The Fridman Group — https://thefridmangroup.com/ — clean luxury, advanced filters. — [Azuro](https://azurodigital.com/real-estate-website-examples/)
- Damac Properties (developer) — https://www.damacproperties.com/ — 3D Unreal tours, unit filters on a 3D model (Dark/tech + Immersive). — [Azuro](https://azurodigital.com/real-estate-website-examples/)
- Berrow Projects (UK property developer case study) — [Solve agency](https://solve.co.uk/transformations/berrow-projects-website/) (search result, not fetched)

**(e) Venues / weddings**
- Hawk Valley Retreat — https://hawkvalleyretreat.com/cording-event-barn/elopements-and-weddings/ ; Bent Creek Lodge — https://bentcreeknc.com/weddings-elopements/ ; Kelly's Resort — https://kellysresort.com/weddings-events/ ; Odessa By The Sea — https://odessabythesea.com/weddings/ — photo/video-led, testimonials, inquiry/tour CTAs (one agency's portfolio, so style is homogeneous). — [InsideOut](https://insideout.com/portfolio/wedding-venue-websites/)
- Old Luxters Barn (Oxfordshire, UK venue) — [Kontrolit showcase](https://www.kontrolit.net/showcase/old-luxters-barn.htm); Granite Ridge Estate & Barn — [HubSpot Inspire](https://designers.hubspot.com/inspire/granite-ridge-estate-barn) (search results, not fetched)

### Inferences
- [unverified, from general knowledge; check live before citing] Widely referenced additional examples:
  - Hotels: Aman (aman.com, Luxury minimal serif), The Hoxton (thehoxton.com, Editorial lifestyle), Ace Hotel (acehotel.com, Typographic/retro), Soho House, Habita/Grupo Habita (Mexico, Minimalist).
  - Restaurants: Noma (noma.dk, Minimalist), Lyle's/St. John (London, typographic minimal), Tartine (Organic bakery), Sweetgreen (Flat bold ordering).
  - Tours / travel: GetYourGuide and Airbnb Experiences (Flat UI marketplace patterns), Black Tomato and Intrepid Travel (Editorial travel).
  - Real estate: Rightmove, Zillow and Idealista (list+map Flat UI), Compass and Sotheby's International Realty (luxury minimal), The Modern House (UK, Editorial agency).
  - Venues: Hedsor House and Babington House (UK, Luxury editorial).
- Synthesis: European/Asian examples are under-represented in the cited roundups (mostly US-centric). A global builder should treat the patterns as global (they are driven by booking engines and portals used worldwide) and adapt only language, currency and date formats.

### Gaps
- Could not verify 2025–2026 redesign status of each example site live.
- Wedding/venue examples come only from agency portfolios (homogeneous style). No independent "best venue websites" roundup with 2024–2026 dates was fetched.
- Few non-US examples have source confirmation (exceptions: 7132, Royal Savoy, Wolny Las, El Fenn, Hotel Neptun, Damac).
