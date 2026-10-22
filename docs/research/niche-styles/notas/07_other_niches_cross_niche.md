# Web design style, layout and UI/UX conventions: other niches (non-profits, education, museums, creative portfolios, architects/interiors, personal brands, events) + cross-niche evidence

Scope: visual design, layout and UI/UX only. Global. Notes prepared Oct 2026. Evidence older than 2023 is flagged **[OLDER]**. Style-label mappings (Minimalist, Editorial, Brutalist, etc.) are **synthesis** unless a source uses the label itself. Example lists come mostly from agency/builder "best of" listicles (Numiko, Webflow, Framer, htmlburger, talks.co, Freshy, Colorlib). Their authors picked the sites, so they show good practice that someone curated. They are not random samples. Numiko designed some of the museum sites it lists and says so.

---

## (a) Non-profits / NGOs / charities: goals, conversion UI, patterns, style, examples

### Takeaway
The main conversion is a donation, ideally recurring. The evidence favours a donate button that is easy to find, a form with several preset amounts (including low ones) that are tied to concrete impact, a default matched to the ask (monthly when you are asking for monthly), and wallet payments, because most traffic is mobile while most revenue still comes from desktop. Current award-level charity sites pair this simple form with mission-first heroes using real photography or video and purposeful motion. A high-trust documentary or editorial look is the prototype.

### Cited Findings
- **Preset amounts:** CaringBridge tested its existing 3 suggested amounts ($70/$125/$300) against 6 lower-starting amounts ($25/$50/$75/$100/$250/$500), each with an "other" field. Conversion went from 0.96% to 2.0% (+104%, 98.7% confidence, n=4,159). The change in average gift was not significant (about −$4), revenue rose, and the 6-button version was rolled out site-wide. Feb 2015 **[OLDER]** — [NextAfter Experiment #930](https://www.nextafter.com/?p=11643)
- **Default to monthly when the ask is monthly:** Texas Public Policy Foundation defaulted a tabbed form to the monthly tab instead of one-time. Conversion went from 0.0% to 1.8% (4 recurring gifts vs 0; n=406; 95.6% confidence; Jan–Feb 2023). The sample is small. NextAfter noted that a one-time default can stop donors from ever seeing the monthly tab — [NextAfter Experiment #124702](https://www.nextafter.com/?p=49869)
- **Device split (M+R Benchmarks 2025):** 53% of nonprofit website visits are mobile vs 47% desktop. Desktop accounts for 55% of donation transactions and 70% of revenue. Average gift is $145 on desktop vs $76 on mobile — [M+R Benchmarks 2025, Website performance](https://2025.mrbenchmarks.com/website-performance.html)
- **Donation-page norms (M+R 2025):** PayPal offered by 76% of nonprofits, Apple Pay by 47%, Google Pay by 40%. One-time giving is pre-selected by 62%, and 90% offer a monthly option. Overall donation-page conversion rates appear only as chart images, so I could not extract them — [M+R Benchmarks 2025](https://2025.mrbenchmarks.com/website-performance.html)
- **NN/g "Donation Usability" (23 nonprofit sites, 2009) [OLDER]:** only 43% put their mission on the homepage and only 4% said on the homepage where the money goes. In 17% of cases users could not find where to donate. Turn-offs were 53% unclear content and 47% poor page design. Users wanted to understand the organisation's goals before giving. NN/g estimated that fixes "could easily double donations" — [NonprofitPro on NN/g report](https://www.nonprofitpro.com/article/nielsen-norman-group-releases-new-study-nonprofit-web-sites-estimates-organizations-could-double-online-donations-405368/)
- **2026 best-practice examples and traits (Numiko):**
  - Children's Society gives donation amounts context to lift conversion and uses careful animations.
  - WaterAid has a strong hero video and donation prompts showing how funds will be spent.
  - Obama Foundation uses a split-screen scroll (fixed left panel, scrolling right) and only five top-nav sections.
  - Farm Africa has a scroll-zoom on the word "solution" and filters by theme or country.
  - Surfers Against Sewage has an interactive map of local water quality and a strong, consistent identity.
  - SolarAid has a cursor-following spotlight that lights up images.
  - Age of Union pairs bold type with strong photography and video.
  - Eden Reforestation leads with a hero video plus stats.

  Trends Numiko names: hero video and bold imagery, purposeful motion, donation context tied to outcomes, simple navigation at scale, and interactivity tied to the mission — [Numiko, Best non-profit websites 2026](https://numiko.com/insights/the-best-non-profit-websites-2026)
- **Example URLs** (all from the Numiko 2026 list): https://www.childrenssociety.org.uk, https://www.wateraid.org/uk, https://www.obama.org, https://www.sas.org.uk, https://www.solar-aid.org, https://www.ageofunion.com, https://www.farmafrica.org, https://www.edenprojects.org — [Numiko 2026](https://numiko.com/insights/the-best-non-profit-websites-2026)
- **Builder taxonomy:** Squarespace's "Charities & Nonprofits" solution group splits into Faith Communities, Philanthropy & Advocacy, Community Groups, Environment & Conservation, Arts & Culture, and Youth & Education. ThemeForest has a dedicated "Nonprofit" HTML subcategory — [Squarespace templates](https://www.squarespace.com/templates); [ThemeForest site templates](https://themeforest.net/category/site-templates)

### Inferences
- **Page structure an AI builder should apply (synthesis):**
  - A sticky header "Donate" button in high contrast, also kept sticky at the bottom on mobile.
  - A hero with a mission statement, real photo or video, and a primary donate CTA.
  - An impact strip with stats ("£X provides Y").
  - Programmes or stories as cards, then proof (financial transparency, ratings, partner logos), then newsletter or volunteer actions.
  - A footer with registration details.
- **Donation form spec (synthesis from the cited tests):**
  - One-time/monthly toggle, defaulting to whatever the page asks for.
  - 4–6 preset amounts that start low, each with a one-line impact label, plus an "other" field.
  - Wallet buttons (Apple Pay, Google Pay, PayPal) at the top for mobile.
  - Embedded on the page instead of redirecting. The redirect point is a common practitioner recommendation that I did not verify with a test here.
- **Prototypical style:** Editorial/documentary. Large real photography, a warm humanist sans or serif, one strong brand accent colour, and a Minimalist base. Differentiating styles: Kinetic typography or Immersive scroll for storytelling (Farm Africa, Obama Foundation), Illustrative for child or community causes, and a bold Neo-brutalist identity for activist or campaign groups (Surfers Against Sewage fits a bold campaign look).
- **Styles to avoid:** Luxury (reads as spending donor money on show), Glassmorphism or Neumorphism (low contrast hurts accessibility on forms), and heavy Dark/tech.

### Gaps
- I found no 2024–2026 public A/B test isolating the visual style of a donation page as opposed to its mechanics.
- M+R donation-page conversion rates by sector and device sit only in chart images and the PDF.
- I found no reliable evidence comparing an embedded form with a redirect, or one-step with multi-step forms.

---

## (b) Schools, language schools and education providers: goals, conversion UI, patterns, style, examples

### Takeaway
The conversions are "enquire / book a visit / apply / enrol / take a level test / free trial". Usability evidence says the decisive UI is findable programmes and deadlines, authentic imagery instead of stock, scannable facts and outcomes, and navigation organised by audience. Universities lean institutional or editorial with real photography. Language schools split into two types: boutique or community sites with course grids and placement tests, and SaaS-style platforms such as Lingoda with a free trial.

### Cited Findings
- **NN/g university websites (57 sites tested with 33 users aged 16–68 in the US, Canada, UK and Taiwan; article 2014, updated 2016) [OLDER]:**
  - 48% of users did not realise the university offered a programme they wanted, even though it did.
  - Guidelines: identify the institution on every page, use authentic images (stock makes schools look generic), make the About page informative with a scannable fact list, surface rankings and stats, make deadlines and the application process easy to find, publish job-placement data, avoid "gimmicky", ad-like styling and vague labels such as "Do Stuff", and support internal search.

  — [NN/g, University Websites: Top 10 Design Guidelines](https://www.nngroup.com/articles/university-sites/)
- NN/g found that faculty pages persuade prospective students — [NN/g video](https://www.nngroup.com/videos/university-faculty-pages/)
- **University examples, 2026 (Freshy):**
  - RISD (https://www.risd.edu/): "minimalist, gallery-like, generous white space", images fade in on scroll.
  - Johns Hopkins (https://www.jhu.edu/): full-screen video loops, an immersive look.
  - Penn (https://www.upenn.edu/): unfiltered, realistic photography.
  - UT Austin admissions (https://admissions.utexas.edu/): looped video of real professors and an orange bottom action bar.
  - Goshen College (https://www.goshen.edu/): "Apply Now" and "Schedule a Visit" CTAs in a purple and gold palette.
  - Brown (https://www.brown.edu/): video autoplay deferred until scroll to help mobile performance.

  Trends Freshy names: real imagery over stock, navigation by user type (prospective, current, alumni), apply/visit CTAs early and repeated, and scroll-driven immersion — [Freshy Sites, Best college & university websites 2026](https://freshysites.com/web-design-development/best-college-and-university-websites/)
- **Language school examples (Colorlib):**
  - JP Linguistics (https://jplinguistics.com): free CEFR-based placement testing, boutique style.
  - Polyglottist (https://polyglottistlanguageacademy.com): course grid by language and prominent enrol CTAs.
  - Lingoda (https://lingoda.com): "modern SaaS-style", prominent free 7-day trial.
  - EF (https://ef.edu): high-end look with custom variable fonts, gradient overlays and sticky brochure CTAs.
  - Kaplan International (https://kaplaninternational.com): course finder and destination search.
  - Enforex (https://enforex.com): prominent course search and booking.
  - CactusBCN (https://cactusbcnlanguages.com): course catalogue with clear pricing and booking.
  - LTL (https://ltl-school.com): programme comparison tools and city landing pages.

  — [Colorlib, Language school website examples](https://colorlib.com/wp/language-school-website-examples/)
- **Builder taxonomy:** Squarespace "Education & Training" splits into Exam Prep Tutors, Music Teachers, Art Instruction, Dance Schools, Language Schools, and Vocational Training. Wix has an "Education" industry category, and Framer lists "Education" under Services — [Squarespace](https://www.squarespace.com/templates); [Wix templates](https://www.wix.com/website/templates); [Framer marketplace](https://www.framer.com/marketplace/templates/)

### Inferences
- **Page structure (synthesis):**
  - Hero with a real campus or class photo or video, plus a primary CTA ("Book a free trial / level test / visit") and a secondary "Download brochure".
  - A course finder with filters (language, level CEFR A1–C2, format online/in-person, intensity, start date).
  - Course cards showing price, schedule and level, then outcomes and accreditation badges, then testimonials (preferably video), then a teacher or faculty grid.
  - A visible start-date and deadline module, and FAQ.
  - Mobile: a sticky bottom action bar (UT Austin pattern).
- **Prototypical style:** Flat/Material or friendly Minimalist with a bright accent palette for language schools. Editorial/institutional serif-plus-sans for universities. Differentiators: Typographic-led Minimalist (RISD) for art and design schools, Illustrative or playful for children, SaaS-like Bento feature grids for online platforms (Lingoda, EF).
- **Styles to avoid:** "Gimmicky" ad-like styling (NN/g), stock-photo-heavy hero sliders, and Brutalist or Y2K unless the school is an art school.

### Gaps
- I found no 2023–2026 controlled study on language-school site conversion (for example, placement test vs trial CTA).
- The NN/g university data dates from 2014–16. I could not access a current NN/g higher-ed report.

---

## (c) Museums, galleries and cultural institutions: goals, conversion UI, patterns, style, examples

### Takeaway
About half of museum web visits are to plan a visit, so opening hours, open/closed status, tickets and "What's on" must sit above the fold. The other half browse collections or stories, which favours object-led collection search and storytelling pages. The prototype is an art-first Minimalist or Swiss/editorial look that lets the artworks lead. Contemporary venues can credibly go Brutalist or experimental, provided the logistics stay usable.

### Cited Findings
- **Visitor motivations [OLDER]:**
  - Indianapolis Museum of Art (2012, n=4,074): plan a visit 50%, personal information 21%, professional 16%, casual browsing 10%, book or buy 2.7%.
  - 15 Dutch museums (2013, about 41,000 responses): plan a visit 47% (range 35–57%), casual browsing 21%, personal 16%, professional 13%, book or buy 4%.

  — [Rui Guerra, Ecsite Spokes #5, 2014](https://www.ecsite.eu/sites/default/files/spokes5_website_motivations.pdf)
- **2026 museum and gallery trends (Numiko):** live open/closed indicators (Baltic, Guggenheim Bilbao), object-centric and story-led collections, scroll-driven motion, per-exhibition colour theming (Nordiska Museet, British Museum, Van Gogh Museum), clear navigation and search at scale (V&A, National Gallery, British Museum), login-free saved collections (MIT Museum, Cooper Hewitt "Shoebox"), and discreet top-left menus — [Numiko, Best museum & gallery websites 2026](https://numiko.com/insights/best-museum-and-gallery-websites-2026)
- **Specific sites (Numiko 2026):**
  - Rijksmuseum (https://www.rijksmuseum.nl/en): "art-first, simple but striking", smooth ticket flow.
  - Van Gogh Museum (https://www.vangoghmuseum.nl/en): horizontal-scroll homepage with a colour palette that shifts as you scroll.
  - National Gallery (https://www.nationalgallery.org.uk/): "understated, calm", discreet hamburger menu.
  - Nottingham Contemporary (https://www.nottinghamcontemporary.org/): "deliberately retro, brutalist aesthetic" with playful microinteractions.
  - Guggenheim Bilbao (https://www.guggenheim-bilbao.eus/en): full-screen video hero and tile layout with hover zoom (2023 Webby).
  - Baltic (https://baltic.art/): typographic loading animation and a persistent top-left block of visitor info.
  - MIT Museum (https://mitmuseum.mit.edu/): images behind coloured blocks with geometric "peepholes".
  - V&A (https://www.vam.ac.uk/): prominent search, 1.25M objects, "on display" indicators.

  — [Numiko 2026](https://numiko.com/insights/best-museum-and-gallery-websites-2026)
- Numiko discloses that it designed the Science Museum and British Museum sites — [Numiko 2026](https://numiko.com/insights/best-museum-and-gallery-websites-2026)
- **Commerce potential [OLDER]:** the Met made $4.5M in online membership sales (2012), and the V&A's online shop converted at 1.63% — [Ecsite Spokes #5](https://www.ecsite.eu/sites/default/files/spokes5_website_motivations.pdf)

### Inferences
- **Page structure (synthesis):**
  - A persistent "Visit" utility: today's hours plus open/closed status, a "Book tickets" CTA, and location.
  - Hero showing the current headline exhibition in its own colour theme.
  - A "What's on" grid of exhibitions and events, filterable by date and type.
  - "Plan your visit" content (prices, accessibility, getting there, café).
  - Entry points into the collection or stories, plus membership or donation, shop, and newsletter.
  - Ticketing: date picker, then time slot, then ticket types with quantity steppers.
- **Prototypical style:** Minimalist / Swiss grid with big imagery and restrained type, often black/white with per-exhibition accent colours. Differentiators: Immersive scroll or horizontal scroll (Van Gogh), Kinetic typography (Baltic), Brutalist or Neo-brutalist for contemporary art spaces (Nottingham Contemporary), and Editorial for story-led collections.
- **Styles to avoid:** Glassmorphism, Neumorphism or Claymorphism, which compete with the artworks. Heavy Maximalism hides visit logistics.

### Gaps
- The motivation data is from 2012–13. I found no 2023–2026 equivalent with published percentages; The Audience Agency's museum digital audience pages surfaced in search but were not fetched.
- I found no study on ticket-funnel UI specific to museums.

---

## (d) Creative portfolios (photographers, designers, illustrators): goals, conversion UI, patterns, style, examples

### Takeaway
The conversion is "contact / commission / hire / book", and the work itself is the interface. Conventions: lean navigation by category, large images or a grid that switches between grid and full view, project or case-study pages, and trust signals (client or publication logos, a portrait and short bio). Style should express the creator's own aesthetic. Minimalist white galleries are the prototype; differentiators include horizontal carousels, split screens, scroll-reactive reveals and bold typography.

### Cited Findings
- **Photography portfolios (Framer blog):**
  - Justin Bettman lets visitors toggle S/M/L views (a multi-column grid vs immersive).
  - Dao for Design uses large grey or black type on white and a staggered grid that collapses into columns on mobile.
  - Hannah Miles uses neutral tones, a fixed background name with photos scrolling over it, and category tabs.
  - Ausra Babiedaite uses a horizontal carousel and a colour-organised photo index.
  - Samuel Angibaud uses a split-screen homepage and a book-style image flip.
  - Keith Greenbaum uses a split-screen logo that changes colour and a lime accent.
  - Christopher Ireland uses a minimal three-item menu (Commercial, Creative, Community).

  The article gives no URLs, so these need verifying before use as references — [Framer, 13 photography portfolio websites](https://www.framer.com/blog/photography-portfolio-websites/)
- **Framer best practices:** show images at about 2400–2560×1600 px, keep navigation lean, match the site's style to the photographic point of view, show client or publication logos, include a self-portrait or bio, show at least 15–25 of your best images, and use a CMS — [Framer blog](https://www.framer.com/blog/photography-portfolio-websites/)
- **Design or UX portfolios (NN/g, Aug 2019) [OLDER]:**
  - Present 3–5 projects as detailed case studies, quality over quantity.
  - Each case study covers the problem, your role, the process, the solution, challenges, impact and learnings, with process visuals.
  - Hiring managers "very rarely" read portfolios word for word, so make them scannable.
  - Based on a survey of 204 UX hiring professionals.

  — [NN/g, UX design portfolios](https://www.nngroup.com/articles/ux-design-portfolios/)
- **Builder taxonomy:** Framer's "Portfolio" group (Artists, Designers, Photography, Resume) is listed first in its marketplace navigation. Wix has "Portfolio & CV" as a type plus Photography, Design and Creative Arts industries. Squarespace lists Photographers, Graphic Designers and Artists under Creative Services. Webflow's first category is "Portfolio & Agency" — [Framer](https://www.framer.com/marketplace/templates/); [Wix](https://www.wix.com/website/templates); [Squarespace](https://www.squarespace.com/templates); [Webflow](https://webflow.com/templates)

### Inferences
- **Page structure (synthesis):**
  - Name or logo, a 3–5 item menu (Work / About / Contact, plus categories for photographers).
  - Homepage made of a grid of work: masonry for photographers, uniform tiles or large cases for designers.
  - Project pages: full-bleed images for photographers; for designers, a case-study template (context, role, process, outcome).
  - About page with portrait, client logos and press, then a contact or booking form (with a date field for weddings and events).
- **Prototypical style:** Minimalist with a gallery-white or near-black background, small type and lots of whitespace. Differentiators: Typographic-led or Swiss for graphic designers, Kinetic typography and Immersive scroll for motion or 3D designers, Collage, Maximalist or Illustrative for illustrators, Brutalist or Neo-brutalist for experimental designers, Editorial for photojournalists.
- **Styles to avoid:** Styles that compete with the work, such as Glassmorphism, Claymorphism or busy Bento grids for photographers, and heavy colour frames around photos.

### Gaps
- The Framer article gives no URLs. I did not verify that these portfolios are live in 2026.
- I found no quantitative 2023–2026 study on portfolio-site conversion or reviewer dwell time.

---

## (e) Architects and interior designers: goals, conversion UI, patterns, style, examples

### Takeaway
The goals are to explore projects and contact or commission the firm. The dominant pattern is a full-screen hero image, a filterable project gallery by typology, project pages with large imagery and spec details, then studio/team, process or services, and contact. Minimalist / Swiss with generous whitespace and simple sans type is the clear prototype. Practitioners advise mirroring the firm's own architectural language in the layout.

### Cited Findings
- **Webflow's 2025 list of 12 architecture sites:**
  - Reload Architecture (https://www.reloadarchitecture.com/): full-screen image, simple typefaces, "generous whitespace in a minimalist style".
  - Blackbox Architectonics (https://www.blackboxarch.com/): bold hero, each scroll row layers in a project or CTA, a mix of F- and Z-patterns, minimalist type.
  - Felicity Christian Architect (https://www.fcarchitect.co.nz/): full-screen exterior and a large project gallery.
  - Gary Todd Architecture (https://www.garytoddarchitecture.co.nz/): headline over a full-screen exterior and an interactive gallery.
  - ArchUnion (https://archunion.art/): interactive glassmorphism elements for a glass-themed aesthetic.
  - SMP Architecture (https://www.smp-arch.com/projects): a typology gallery.
  - Studio MEMM: full-screen hero with off-centre overlapping squares.

  Several entries are *.webflow.io* showcase or template sites, not confirmed real firms — [Webflow, Top 12 architecture websites 2025](https://webflow.com/blog/best-architecture-websites)
- **Webflow best practices:** an interactive gallery spanning residential, commercial and industrial work; only the pages you need, with the menu in a consistent place; mobile-first; "mirror the client's architectural design" in layouts and interactions — [Webflow blog](https://webflow.com/blog/best-architecture-websites)
- **Builder taxonomy:** Squarespace lists Interior Designers and Architects under Creative Services. Framer lists Architecture under Agency and Furniture under Ecommerce — [Squarespace](https://www.squarespace.com/templates); [Framer](https://www.framer.com/marketplace/templates/)
- Plug and Play Design's "17 Best Architect Websites of 2025" surfaced in search but was not fetched — [Plug and Play Design](https://www.plugandplaydesign.co.uk/best-architect-websites-2025/)

### Inferences
- **Page structure (synthesis):**
  - Minimal header (logo left; Projects / Studio / Contact).
  - Full-bleed hero image or video of a signature project.
  - A project index with a grid/list toggle and typology filters (Residential / Commercial / Hospitality / Interiors).
  - Project page: a large image sequence plus a metadata table (location, year, area, status, collaborators) and a short narrative.
  - Studio page with team, process steps and awards/press, then contact with a map.
  - Interior designers add before/after sliders, mood boards or service tiers, and an enquiry form asking budget and timeline.
- **Prototypical style:** Minimalist / Swiss: monochrome, a grid-led layout, thin sans type, generous whitespace. Differentiators: Editorial (magazine-like project stories), Luxury (serif plus warm neutrals, for high-end residential or interiors), Organic (natural textures and earthy palettes for sustainable or biophilic practices), Brutalist (concrete-honest, for avant-garde studios), Immersive scroll or 3D for visualisation studios.
- **Styles to avoid:** Claymorphism, Y2K and Maximalism, which clash with the expected restraint. Glassmorphism works only as a deliberate conceptual link (ArchUnion), not as a default.

### Gaps
- I found no real 2024–2026 interior-designer examples with fetched details. Verified real firm URLs (beyond those Webflow listed) need a separate check.
- I found no quantitative conversion evidence for architecture sites.

---

## (f) Personal brands / speakers / authors: goals, conversion UI, patterns, style, examples

### Takeaway
The conversions are "book me to speak", "buy the book", "join the newsletter or lead magnet", and "buy a course or ticket". The standard pattern: a hero with portrait, name, tagline and booking or newsletter CTA; a speaker reel; client and media logos; topics; books; testimonials; and a page for event planners. The style follows the person's energy. Calm figures use Minimalist or warm Editorial; high-energy figures use bold, high-contrast or dark looks.

### Cited Findings
- **talks.co review of 27 speaker sites:**
  - Simon Sinek (simonsinek.com): sectioned layout, orange and blue scheme, newsletter, strong CTAs.
  - Jay Baer (jaybaer.com): hero video reel, brand logos as social proof, an availability CTA.
  - Tony Robbins (tonyrobbins.com): "bold, high-energy".
  - Mel Robbins (melrobbins.com): yellow accent, story-driven homepage.
  - Brené Brown (brenebrown.com): resource hub for books, talks and podcasts, warm design.
  - Eckhart Tolle (eckharttolle.com): "serene, minimalist".
  - Steven Bartlett (stevenbartlett.com): "magazine-style layout, HD background videos, career timeline".
  - Ken Hughes (kenhughes.info): dark theme with bold fonts.
  - Gary Vaynerchuk (garyvaynerchuk.com): content-first (blog, podcast, video).
  - Erick Rheam: a dedicated tab for event planners.

  — [talks.co, 27 best public speaker websites](https://talks.co/p/public-speaker-website)
- **Common structure per talks.co:** photo, name, tagline and expertise above the fold; topics, bio, books and contact in navigation; client logos, media and testimonials; a speaker reel; a booking CTA in the header; a lead magnet; an event-planner page; and "keep the design simple if your content is dense, or bold if your speaking style is high-energy" — [talks.co](https://talks.co/p/public-speaker-website)
- **Builder taxonomy:** Squarespace "Personal" splits into Resumés & CVs, Portfolios, Weddings, Freelancers, Creators, and Podcasts; Professional Services includes Professional Coaches. Webflow has a "Personal" category, ThemeForest has "Personal", and Framer's Portfolio group includes Resume — [Squarespace](https://www.squarespace.com/templates); [Webflow](https://webflow.com/templates); [ThemeForest](https://themeforest.net/category/site-templates); [Framer](https://www.framer.com/marketplace/templates/)
- Alliance Interactive's "35 Best Author Website Examples" surfaced in search but was not fetched — [Alliance Interactive](https://www.allianceinteractive.com/blog/best-author-website-examples/)

### Inferences
- **Page structure (synthesis):**
  - Hero with a large portrait (cut-out or full-bleed), name, a one-line positioning statement, primary CTA "Book [Name]" and secondary "Get the free guide".
  - A logo bar ("As seen in / Spoken at"), a speaker reel, and keynote topics as 3–4 cards.
  - A book module with cover mockup and buy buttons (retailer links), testimonials, and a newsletter band.
  - A media kit with downloadable photos, bio and tech rider, plus an event-planner enquiry form (date, location, audience size, budget).
  - Authors add a book-series grid, events or tour dates, and a reading-group kit.
- **Prototypical style:** Editorial (magazine layout, serif display plus large photography) or bold personal-brand marketing (high-contrast accent colour, big type). Differentiators: Typographic-led Minimalist for thought leaders, Dark/tech for tech or futurist speakers, Kinetic typography for creators, Organic or soft for wellness and spirituality (Eckhart Tolle), and Retro or Illustrative for fiction authors (genre-matched).
- **Styles to avoid:** Generic SaaS Bento or Glassmorphism, which make a person read like a software product. Over-designed Maximalism that hides the booking CTA.

### Gaps
- The talks.co list is a vendor listicle with no dates on individual site captures. I did not verify that each site still looks as described in 2026.
- I found no quantitative evidence on speaker or author site conversion.

---

## (g) Events, conferences and festivals: goals, conversion UI, patterns, style, examples

### Takeaway
The conversion is buy a ticket or register, with secondary goals of browsing the speakers or lineup, checking the schedule, sponsoring, and finding venue logistics. Conventions: date and location in the hero, a ticket CTA that is persistent and repeated, a speakers or lineup grid with headliner hierarchy, an agenda that filters by day, track or stage, ticket-tier cards, past-edition video, sponsor logos, and FAQ and map. Visually, events are the niche with the most licence for bold, kinetic, dark or maximalist branding, because each edition is a campaign. That licence must never come at the cost of ticket clarity or load speed during on-sale spikes.

### Cited Findings
- **Conference examples (htmlburger):**
  - Awwwards Conference (https://conference.awwwards.com/): red-hued city hero with ambient sound, ticket link top-right, highly interactive.
  - Web Summit (https://websummit.com/): press quote and two CTAs in the hero, speakers, highlight videos.
  - Red Hat Summit (https://www.redhat.com/en/summit): vibrant geometric shapes and an interactive quiz that builds a personalised agenda.
  - Ai4 (https://ai4.io/vegas/): venue, time and scale metrics on the homepage, dark futuristic graphics.
  - WaysConf (https://www.waysconf.com/): dark theme with an urgency reminder on CTAs.
  - Circles Conference (https://circlesconference.com/): bold red with animated elements.
  - Dublin Tech Summit (https://dublintechsummit.tech/): background video and a CTA that moves on scroll.
  - Inbound (https://www.inbound.com/): a downloadable "convince your boss" letter as a conversion aid.
  - Several entries are 2021–2024 editions **[OLDER]**.

  Best practices listed: answer key questions early, simple navigation, prominent and repeated CTAs, purposeful interactivity, social proof, seamless registration — [htmlburger, Conference websites](https://htmlburger.com/blog/conference-websites/)
- **Festival UX guidance (Ticket Fairy, Feb 2025):**
  - Lineup as a list or interactive grid with headliners visually separated, plus artist profiles (photo, video, bio, links).
  - Timetable showing times, stages and side events, with accordions and progressive disclosure.
  - Ticket section front and centre with tiers (single-day, multi-day, VIP), early-bird pricing and high-contrast purchase CTAs.
  - Short checkout, keep heavy media off the ticket path, compress images for on-sale spikes.
  - Sticky navigation for long schedules, an interactive site map (stages, food, toilets), an easy-to-find FAQ.
  - Templates "can speed up launch… but make sure the design can be customized enough to avoid looking like a generic clone".
  - No quantified mobile ticket share is given.

  — [Ticket Fairy festival website guide](https://www.ticketfairy.com/blog/2025/02/11/how-to-build-a-music-festival-website-the-perfect-guide/)
- **Builder taxonomy:** Framer "Events" splits into Conferences, Music, Sports, and Weddings. Squarespace "Events & Experiences" splits into Travel Agencies, Camps, Activities, Festivals, Concerts & Shows, and Restaurants & Bars. Wix has an "Events" industry. ThemeForest has "Wedding" and "Entertainment" subcategories. Webflow publishes a curated festival template list — [Framer](https://www.framer.com/marketplace/templates/); [Squarespace](https://www.squarespace.com/templates); [Wix](https://www.wix.com/website/templates); [ThemeForest](https://themeforest.net/category/site-templates); [Webflow festival list](https://webflow.com/list/festival)
- A Philly Music Fest 2025 site appears in the Made in Webflow showcase (details not fetched) — [Webflow showcase](https://webflow.com/made-in-webflow/website/philly-music-fest-2025-b354ea)

### Inferences
- **Page structure (synthesis):**
  - Hero with event name, date, city or venue, a countdown, and a primary "Get tickets" button (sticky in the header, and as a bottom bar on mobile).
  - Key metrics strip (attendees, speakers, days), then a speakers or lineup grid (headliners larger, then a tiered list).
  - Agenda with day tabs and track/stage filters. Each session shows time, title, speaker avatar and room, with "add to calendar" and a "my agenda" save.
  - Ticket-tier cards (price, inclusions, deadline/early-bird badge, "sold out" states), past-edition video and gallery, sponsor logo wall by tier.
  - Venue/map/travel, FAQ, newsletter for lineup announcements.
  - Festivals add a stage-by-time timetable grid (swipe horizontally on mobile) and a site map.
- **Prototypical style:**
  - Tech conferences: Dark/tech with gradients or Neo-brutalist; Bento for "why attend" grids.
  - Design conferences: Kinetic typography, Immersive scroll, Swiss.
  - Music festivals: Maximalist, Collage, Retro or Y2K, Illustrative poster-led art direction.
  - Weddings: Luxury, Editorial or Organic.
  - Academic or industry association events: Flat/Material minimal for clarity.
- **Styles to avoid:** Any style that slows the site down (heavy WebGL or autoplay video on the ticket path), and low-contrast Glassmorphism on CTAs and timetables.

### Gaps
- I found no published A/B data on ticket-page or agenda UI, and no source with mobile share of ticket sales.
- Several htmlburger examples are past editions. The current 2026 state of each site was not verified.

---

## Cross-niche 1: How builders and template marketplaces structure templates by industry (demand and prototypicality proxy)

### Takeaway
Every major marketplace organises templates by industry or use case, which confirms that "industry" is the primary mental model for choosing a design. Portfolio/creative, business/services, ecommerce, events and nonprofits/community recur across all of them. None of the platforms I checked publish per-category template counts, so counts can only be used as a proxy at the total level.

### Cited Findings
- **Framer marketplace (10 groups × 4 subcategories, no counts shown):**
  - Portfolio: Artists, Designers, Photography, Resume
  - Software: AI, Apps, Fintech, SaaS
  - Agency: Architecture, Design, Marketing, Web
  - Ecommerce: Beauty, Digital, Fashion, Furniture
  - Services: Consulting, Education, Home, Legal
  - Health: Fitness, Medical, Therapy, Wellness
  - Publishing: Blogs, Entertainment, Magazines, News
  - Real Estate: Agents, Construction, Listings, Management
  - Hospitality: Food, Hotels, Restaurants, Travel
  - Events: Conferences, Music, Sports, Weddings

  — [Framer marketplace templates](https://www.framer.com/marketplace/templates/)
- **Webflow:** "7,000+ free and premium website templates". Visible categories: Portfolio & Agency, Technology, Blog & Editorial, Personal, Professional Services, Real Estate, UI Kit, Retail (more behind "Browse all"). No per-category counts — [Webflow templates](https://webflow.com/templates)
- **ThemeForest HTML site templates:** "over 24,900". Subcategories: Corporate, Retail, Creative, Admin Templates, Technology, Personal, Entertainment, Specialty Pages, Nonprofit, Mobile, Miscellaneous, Wedding. No per-category counts on the page — [ThemeForest](https://themeforest.net/category/site-templates)
- **Squarespace:** organised by product type (Online Stores, Portfolios, Blogs, Services, Scheduling, Content & Memberships, Donations, Limited Releases) and by 10 "Solutions" groups: Creative Services; Professional Services; Education & Training; Beauty; Sports & Fitness; Health & Wellness; Home Services; Events & Experiences; Charities & Nonprofits; Personal. Each has 6 subtypes. No counts — [Squarespace templates](https://www.squarespace.com/templates)
- **Wix:** "2000+" templates (about 250 paginated pages). 15 industry categories: Business, Industrial, Health & Wellness, Events, Education, Communities, Fashion & Style, Beauty & Hair, Design, Photography, Music, Creative Arts, Video, Restaurants & Food, Travel & Tourism. Types: One Page, eCommerce, Portfolio & CV, Blog — [Wix templates](https://www.wix.com/website/templates)
- **Shopify Theme Store:** 1,343 themes (24 free, 1,319 paid). 20 industry filters (Art, Auto, Bags, Beauty, Clothing, Electronics, Entertainment, Food and drink, Garden, Hardware, Home, Jewelry and accessories, Kids, Office, Pets, Services, Shoes, Sports, Toys, Wellness). Catalog-size filters do show counts: One product 27, Few 102, Some 885, Lots 329 — [Shopify themes](https://themes.shopify.com/themes)

### Inferences
- The niches in this file map to builder categories as follows. Nonprofit appears in ThemeForest, Squarespace, and Wix (as Communities). Education appears in Framer, Squarespace and Wix. Events, including Weddings, appears in all six. Portfolio/creative appears in all six and is listed first in Framer and Webflow. Architecture and interiors appear in Framer and Squarespace. Personal appears in Webflow, ThemeForest and Squarespace. Museums or cultural institutions have no dedicated category anywhere. The closest are Squarespace's "Arts & Culture" under Nonprofits, and Wix's "Creative Arts".
- An AI builder could use a two-level taxonomy (about 10 industry groups × 4–6 subtypes, plus a separate "site type" axis: store, portfolio, blog, booking, donations, events). That mirrors how Squarespace separates industry from product type.

### Gaps
- Per-category template counts are not visible on Framer, Webflow, ThemeForest, Squarespace, Wix or Shopify pages, so I could not compute a demand ranking. Getting counts would need filtered pages or API scraping.

---

## Cross-niche 2: Industry conventions vs differentiation (prototypicality, trust, sameness, conversion)

### Takeaway
Strong evidence supports matching category prototypes. Users judge sites within 17–50 ms, and simple plus prototypical designs are rated most beautiful. Higher prototypicality improves attitudes toward the organisation (banking, 2025). Web layouts measurably converged between 2008/10 and 2016. The case for being distinctive rests on brand reasoning and award showcases, not on conversion data. The safe synthesis is "conventional structure, distinctive skin".

### Cited Findings
- **Tuch et al. (2012), International Journal of Human-Computer Studies 70(11):794–811:**
  - 119 real website screenshots varying in visual complexity and prototypicality.
  - Both factors affected aesthetic ratings within 50 ms. At 17 ms both still mattered, but prototypicality was weaker than complexity; it caught up as exposure time increased.
  - Low complexity plus high prototypicality was rated most appealing.

  **[OLDER but foundational]** — [edoc Unibas record](https://edoc.unibas.ch/21676); [Google Research publication](https://research.google/pubs/the-role-of-visual-complexity-and-prototypicality-regarding-first-impression-of-websites-working-towards-understanding-aesthetic-judgments/)
- **Google Research blog summary:** "Users strongly prefer designs that are simple and familiar". A highly complex site was rated less beautiful even when familiar, and an unfamiliar site was rated uglier even when simple. "Designs that contradict what users typically expect of a website may hurt users' first impression" — [Google Research blog, 2012](https://research.google/blog/users-love-simple-and-familiar-designs-why-websites-need-to-make-a-great-first-impression/)
- **Miniukovich & Figl dataset (Data in Brief, Dec 2023):** prototypicality, aesthetics, usability and trustworthiness ratings for about 3,150 homepages across three categories: banking (N=1,033), e-commerce (N=1,064) and university (N=1,059). There were 3,319 rating sessions. Prototypicality was measured as typicality, exemplar goodness and family resemblance. This shows that prototypicality is defined per category; the correlations are in the companion IJHCS 2023 paper (doi 10.1016/j.ijhcs.2023.103103), which I did not fetch — [PMC article](https://pmc.ncbi.nlm.nih.gov/articles/PMC10823051)
- **Figl, Miniukovich, Ernst & Lehrer (2025), Electronic Markets 35(1), art. 40:** in an online experiment on commercial-bank websites, "higher prototypicality significantly improves users' attitudes" toward the bank and toward it as an employer, and mediates the effect of message strength. Prototypicality is framed as an overarching variable that includes navigation structure, colour schemes and layout organisation — [IDEAS/RePEc](https://ideas.repec.org/a/spr/elmark/v35y2025i1d10.1007_s12525-025-00777-9.html); [CBS research portal, "The danger of not being typical"](https://research.cbs.dk/da/publications/the-danger-of-not-being-typical-the-positive-effect-of-webpage-pr/)
- **Measured homogenisation (Goree, Doosti, Crandall & Su, Indiana University, 2020):**
  - About 200,000 archived images of about 10,000 sites (Russell 1000, Alexa top 500, Webby nominees).
  - Average differences in colour, layout and AI-learned attributes peaked in 2008–2010 and fell through 2016.
  - Layout differences fell by more than 30%.
  - Code similarity did not rise, but use of shared libraries (Bootstrap, FontAwesome, jQuery UI) did, and sites using them looked more alike.

  **[OLDER]** — [Big Think summary](https://bigthink.com/technology-innovation/all-websites-look-the-same)
- **Jakob's Law (NN/g, 2017):** "Users spend most of their time on other sites" and "prefer your site to work the same way as all the other sites they already know" — [NN/g video](https://www.nngroup.com/videos/jakobs-law-internet-ux/)
- **"Sameness is OK" critique (Web Designer Depot, 2015, modified 2023) [OLDER]:**
  - Common look: full-width hero, centred headline, logo-left/menu-right header.
  - Causes: frameworks (Bootstrap, Foundation), templates, builders like Squarespace, flat design, responsive design.
  - Benefits: familiarity and lower cost. Risk: less innovation.
  - No data.

  — [Web Designer Depot](https://webdesignerdepot.com/every-website-looks-the-same-and-thats-ok/)
- **Niche-level counter-evidence that rule-breaking can work:** Numiko praises Nottingham Contemporary's "deliberately retro, brutalist aesthetic" as showing that "unconventional design can still work with a usable experience". This is a curator's opinion, not a test — [Numiko museums 2026](https://numiko.com/insights/best-museum-and-gallery-websites-2026)
- **NN/g education evidence:** ad-like "gimmicky" styling made users ignore sections, and stock imagery made schools look generic. Both deviations hurt in an institutional niche — [NN/g university sites](https://www.nngroup.com/articles/university-sites/)

### Inferences
- **Synthesis:**
  - Prototypicality matters most where trust or risk is high (banking, universities, charities taking payments). Keep structure, navigation placement and form conventions typical in those niches.
  - Differentiate through art direction instead: typography, colour, photography and motion.
  - Expressive niches (creative portfolios, contemporary art, festivals, design conferences) tolerate, and are rewarded for, lower prototypicality, because their visitors expect the site itself to be a sample of the work.
- A practical rule for an AI builder: keep the niche's structural prototype (IA, CTA positions, form patterns) and let the user's brand or "personality" input choose the stylistic distance from the prototype. Distance should be smaller for trust-critical niches and larger for expressive ones.

### Gaps
- **No source found** quantifying the conversion impact of distinctive vs conventional visual design by industry. This is a key gap; claims elsewhere are anecdotal.
- I did not obtain the correlation values between prototypicality and trust in the Miniukovich & Figl IJHCS 2023 paper (paywalled or not fetched).
- I found no 2023–2026 replication of the Goree et al. homogenisation measurement covering the AI-builder era.

---

## Cross-niche 3: How AI website builders map industries to styles/themes (inputs and defaults)

### Takeaway
Mainstream AI builders all ask for business type or industry first, but the visual style is driven mostly by a separate "personality/vibe" input or by later conversational tweaks. No vendor publishes an explicit industry-to-style mapping table. Squarespace Blueprint is the most explicit: 7 brand personalities, each controlling its own palettes and font pairings.

### Cited Findings
- **Squarespace Blueprint AI:**
  - Onboarding asks business type and site goal.
  - Step 1: site title plus one of 7 brand personalities (Professional, Playful, Sophisticated, Friendly, Bold, Quirky, Innovative). The personality shapes text tone, colour schemes and fonts.
  - Step 2: choose from 9 homepage section types, with a Layout Switcher.
  - Step 3: choose from 6 page types (About, Contact, Shop, Services, Appointments, Course).
  - Step 4: colour palettes grouped by personality, 4 per personality.
  - Step 5: 2 font pairings per personality (14 in total).
  - Colours and fonts cannot be customised inside Blueprint, only afterwards in the editor.

  — [Website Builder Expert, Squarespace Blueprint AI](https://www.websitebuilderexpert.com/?p=123850)
- **Wix AI website builder (conversational):** asks 4–5 questions, such as site name, type of content, goals (community, monetisation) and unique selling point; for stores it also asks audience and products. Style is chosen afterwards: either one of 2,000+ templates or an AI-generated theme refined by chat ("pastel", "neon pink"), with "Generate new theme" and "Shuffle colors". In the reviewer's video-game-review test the AI produced a "bold, electric" blue and black design — [Website Builder Expert, How to use Wix AI](https://www.websitebuilderexpert.com/website-builders/how-use-wix-ai/)
- **Durable:** asks business type (industry), business name and location, then generates a full site with images, copy and contact form in about 30 seconds. It "selects an appropriate template". The industry-specific logic is not documented — [TechRadar, Durable review](https://www.techradar.com/pro/software-services/durable)
- **Framer AI:** takes a free-text prompt ("Describe the site, audience, or page you need") with examples like "personal portfolio", "startup site" and "landing page". It generates structure, sections and copy. Typography and colour are adjusted on the canvas afterwards. No industry presets are described — [Framer AI website builder](https://www.framer.com/solutions/ai-website-builder/)
- **Hostinger AI builder:** support documentation exists. The fetch redirected to [hostinger.com/support/7266945-how-to-use-hostinger-ai-builder](https://www.hostinger.com/support/7266945-how-to-use-hostinger-ai-builder/) and was not completed; see Gaps — [Hostinger support (original URL)](https://support.hostinger.com/en/articles/7266945-how-to-use-hostinger-ai-website-builder)

### Inferences
- **Synthesis: the common pattern is two axes.** Axis 1 is industry or business type, which drives page set, sections and imagery (for example, Squarespace's 6 page types include Course, Appointments and Shop). Axis 2 is personality or vibe, which drives palette, type pairing and tone. An AI builder for these niches could adopt the same split. Example combinations:
  - Nonprofit + Friendly → warm Editorial
  - Museum + Sophisticated → Swiss/Minimalist
  - Festival + Bold or Quirky → Maximalist/Collage
  - Architect + Sophisticated → Minimalist/Swiss
  - Speaker + Bold → high-contrast personal brand
  - Language school + Playful or Friendly → Flat/Illustrative
- Squarespace's personality set (Professional, Playful, Sophisticated, Friendly, Bold, Quirky, Innovative) is a ready-made vocabulary to map onto this file's style labels. That mapping would be my own synthesis, not vendor data.

### Gaps
- I did not verify inputs and defaults for Hostinger AI or 10Web (Hostinger's fetch redirected, and 10Web was not reached).
- No vendor publicly documents an industry-to-palette/font/style mapping. I found no source on what defaults Durable or Wix apply for a given industry beyond single anecdotes.
