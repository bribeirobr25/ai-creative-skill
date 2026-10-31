# Video Director v0.1 · Knowledge packs

**Status:** proposal. Three packs for the Director, plus a separate register that belongs to Production. Nothing here is a proven rule unless tagged `rule` with its authority.

## How to read an item

| Tag | Meaning | How the Director uses it |
|---|---|---|
| `rule` | Approved limit, with its authority | Must follow |
| `evidence` | Backed by evidence recorded in this project (cited) | Strong default |
| `provisional` | Adopted for v0.1 so it can be tested; not yet proven | Default it may adapt, saying why |
| `current` | Dated knowledge about tools or the market, with source and expiry | Use while valid; re-check after expiry |
| `technique` | An optional "how" | May use, change or ignore |
| `hypothesis` | A claim to test (performance, "works best") | Never a rule; can be tried and measured |

Each item also says whether it is **required**, **recommended** or an **option**.

**Loading:** the Core is short and always loaded. Each task adds only the one or two cards it needs. The reference library is used for moodboards and reference studies. The tool register is for Production, not the Director.

**Sources:**
- the frozen V2.5 methods (cited by section);
- this project's research records (cited by file);
- four AI-assistant research conversations kept in the private half (`research/video-2026-10`). These are leads, not primary sources: where they agree, that is a hypothesis, not a validation, and their tool claims are unverified.

---

## Pack 1 · Video Direction Core

| # | Item | Tag | Strength | Basis |
|---|---|---|---|---|
| C1 | Consider the four information categories (references, creative direction, look, sequence) for every job; their form and depth follow the job | `provisional` | required to consider | Owner experience; V2.5 Video Direction §3.1; the research conversations agree |
| C2 | Planning depth follows continuity, number of identities, fidelity risk, regeneration cost, editing complexity, user experience and deliverable; no fixed scene-count thresholds | `provisional` | required | Owner description; V2.5 Video Direction §3.1, §4 complexity budget |
| C3 | Resolve composition and continuity on still frames before motion when that is cheaper than fixing a clip | `provisional` | recommended | V2.5 Video Direction §3.1; research conversations |
| C4 | Before any paid step, check feasibility: actions fit the duration, references support the identities, the route can do the motion and audio, the script fits, transitions say what is preserved and what changes, known failures were checked | `provisional` | required | V2.5 Video Direction §12 |
| C5 | No paid step before the user approves the execution scope; money left in a budget authorizes nothing outside the scope | `rule` | required | ADR-0006 D6 |
| C6 | A reference only secures what it shows. Identity-bearing references should be clean and isolated, and cover the views the motion will reveal (a front-only photo cannot guarantee the back in a turn) | `evidence` + `provisional` | required | Photoshoot study: clean references were the largest fidelity gain (`docs/research/auditoria-aprendizados-2026-10-22.md`); V2.5 Image Direction §5.1 |
| C7 | Products, interfaces and claims come from the user's real material and approved facts; real interface captures, not invented screens; unknowns stay unknown | `rule` | required | ADR-0006 D8; benchmark check C3 |
| C8 | State what must not change in a transformation or a series of shots (the invariants), and what may | `provisional` | recommended | V2.5 Video Direction §9.1; Specialist Method System §6.2 |
| C9 | On-screen text, numbers and logos are planned for precise rendering in the graphics or edit layer, not left to the video model | `provisional` | recommended | V2.5 Image Direction §9 (text modes); the research conversations report garbled text as a common model failure (`current`, unverified) |
| C10 | Every shot creates useful change: new information, a demonstration, a progression, a reveal or a consequence | `provisional` | recommended | V2.5 Video Direction §3 |
| C11 | Fix what carries identity and leave the rest open: each dimension is preserve, bounded variation or open exploration | `provisional` | required | V2.5 Specialist Method System §6.2 |
| C12 | Explore distinct concepts only when that serves the job; real alternatives need an outside input (the user's choice, a different style brief, a rule) | `evidence` + `provisional` | recommended | Same-agent alternatives repeated one direction (audit of 2026-10-22); Specialist Method System §6.4 |
| C13 | The closing and verification steps are never skipped; acceptance needs an independent review | `evidence` + `rule` | required | Only 1 of 18 runs did the closing step (audit of 2026-10-22); ADR-0006 D2, D3 |
| C14 | Say which of the three kinds of quality (artistic, technical, commercial) matter most for this job | `provisional` | required | Owner description |
| C15 | Sound is directed, not added at the end: ambience, sounds of materials and actions, and accents that mark transformations | `technique` | option | Research conversation (motion study) |
| C16 | Name unwanted third-party brands, logos and real likenesses as things to avoid | `evidence` + `rule` | required | A legible third-party brand appeared in 1–2 of 9 test images (benchmark log, BL-2026-10-29-01); check C9 |
| C17 | No synthetic testimonials, reviews or generated demonstrations presented as real; real customers' words only with consent and labelled when re-enacted or voiced by an avatar; consent for any real likeness or voice; follow AI-disclosure and platform ad rules | `rule` | required | ADR-0006 D4, D8 |
| C18 | Plan reusable assets when the objective suggests other versions; never forced | `provisional` | option | Owner description; studio example of a reusable shot library (Pack 3) |

---

## Pack 2 · Format and medium cards

A card adds only what changes for that type or medium. The Core still applies. Beats are default shapes, not formulas (`technique`), and every "performs best" claim is a `hypothesis`.

### Video types

| Card | Purpose | Default shape (`technique`) | Most decisive information | Watch for |
|---|---|---|---|---|
| Feature showcase / product demo | Make the product desirable and its value clear | Hero → feature close-up → use → context → call to action | Product references from the angles the motion shows | Shape, label and material drift; physically wrong contact |
| Launch teaser | Anticipation and a reveal | Tease → build → reveal → payoff, with the reveal timed precisely | Look references and reveal timing | Reveal too early; payoff not held long enough (V2.5 Video Direction §10) |
| UGC-style ad | Feel native in a social feed | Hook → problem → demo → proof → call to action | The product in hand; a consistent persona reference | A generated "customer" is not a real customer (C17); "lo-fi outperforms" is a `hypothesis` |
| Software demo | Prove one workflow works | Context → input → action → result → next step | Real interface captures | Invented screens (C7); unreadable text (C9) |
| Explainer | Make a complex idea simple | Problem → idea → how it works → benefit | Script and visual metaphors | Too many ideas per scene |
| Talking head / avatar | Trust through direct address | Script-led, with supporting footage | Script naturalness; consented face and voice references | Consent and disclosure (C17); likely its own Production route |
| Before / after | Show a transformation | Locked camera, fixed invariants, a clear change | The invariants (C8) | Generated "proof" presented as real (C17); platform restrictions in health and beauty |

### Media

| Card | When it fits | Production route | Watch for |
|---|---|---|---|
| Cinematic / photoreal generation | Physical products, emotion, atmosphere, lifestyle | Reference-based generation from approved still frames | Identity drift between shots; physics and hands; text |
| Motion graphics | Information, structure, data, interfaces, brand systems, text-heavy pieces | Often code-based and deterministic, so text, numbers and colours stay exact; a separate Production route | Licence terms of programmatic tools (`current`, see register); not automatically cheaper |
| Avatar / talking head | Presenter-led, multilingual, frequent updates | Avatar and voice route | Consent, disclosure, lip sync |
| Illustrated / parallax | Story-led or budget-aware pieces | Generated or drawn stills animated with pans, depth and masks | Reads as video only if the motion is purposeful |
| Hybrid | Most strong pieces: photoreal hero moments with precise graphics on top | Several routes, joined in the edit | Consistent look across routes |

**Techniques** (options only, chosen per job): kinetic typography, morphing, parallax, transitions that share colour, direction, shape, texture or energy, macro camera, high-speed or time-remapped motion, stop-motion look.

**Editing rhythms** (`technique`): contemplative, progressive, explosive, rhythmic.

---

## Pack 3 · Professional motion reference library

**How to study a reference** (`technique`): look at movement, camera, materials, simulations, transitions, lighting and sound. For each, ask what principle makes it work and how it could be rebuilt with control.

The Director takes principles, never identity or protected elements (C16, C17). It works from the studios' own published project pages and credits. What follows is our interpretation, not a frame-by-frame analysis. The owner's reviewer reported checking three of these pages on 2026-10-31; we have not re-checked them here.

| Work (studio, year) | Principle to study | Source page |
|---|---|---|
| VIZIO: More of Everything (NotReal, 2024) | Product qualities turned into visual chapters; shifts of material and scale; transitions linked by idea, not by object; published research and development on materials, light and simulation | notreal.tv/project/vizio · behance.net/gallery/207772045 |
| Microsoft Surface Laptop 5 (BUCK) | A sensorial, tactile language; coloured lighting used to link scenes; transitions designed together with the animation | buck.co |
| Pepsi Crave (BUCK) | Practical high-speed liquid footage with motion control; a library of standalone shots produced for reuse across campaigns and regions (see C18) | buck.co/work/pepsi-crave |
| Coppel: Foodie (Plenty, 2019) | Worldbuilding: every object, set and pattern belongs to one coherent universe | behance.net/gallery/77063715 |
| ServiceNow: AI Platform (NotReal) | A motion branding system: reusable rules for entry, hold, easing and exit; 2D, 3D, interface and sound specialists credited on one system | behance.net/gallery/250339529 |

Studios named in the research for later study (not yet reviewed): FutureDeluxe, ManvsMachine, Tendril, Giant Ant, Oddfellows, Instrument.

Archives: Stash, Behance, Vimeo Staff Picks, Motionographer.

For performance evidence, as opposed to inspiration: platform ad libraries (TikTok Creative Center, Meta Ad Library). They show what runs, not what it earns, so any conversion claim stays a `hypothesis` until measured.

---

## Production tool register (placeholder, owned by Production)

Not loaded by the Director, which recommends routes by kind, never by a single provider. Every item is `current`: it needs a vendor source and an expiry date before use, and is unverified until then. These claims come from the research conversations:

| Claim | Status |
|---|---|
| OpenAI Sora discontinued: app 2026-04-26, API 2026-09-24 | Reported verified on the OpenAI Help Center by the owner's reviewer; re-check before relying on it |
| Model limits: Veo 3.1 clips of about 8 s; Kling 4.0 up to 30 s, 15 references, 10 keyframes; Seedance 2.5 up to 30 s and up to 30 images, 10 videos and 10 audio clips; Pika H3 Flex up to 12 references and five audio stems; Wan 3.0, Runway Gen-4.5, Luma Ray 3, MiniMax H3 | Unverified; the conversations disagree in places |
| Prices around $0.05–0.40 per generated second | Unverified |
| Programmatic motion graphics (for example Remotion) renders frame-exact from code | Plausible; commercial licensing depends on the organization and the use, so check terms before use |
| "Three takes per usable shot", "motion slider 2–4 of 10", fixed production times | `technique` / `hypothesis`, not rules |

---

## Not adopted from the research

| Claim | Why |
|---|---|
| AI avatars delivering scripted testimonials, "diverse faces", invented results such as "I saved 12 hours a week" | Synthetic testimonials presented as real (C17) |
| Personalized videos generated and sent automatically from a CRM trigger | An outward action; needs a standing permission and consent law, never a default |
| Founder digital twins and voice cloning without explicit consent and disclosure | C17 |
| "Lo-fi UGC outperforms", "9–15 s performs best", "highest ROI" | Universal performance claims; `hypothesis` until measured with the user's own results |
| Fixed thresholds such as "more than 5 scenes means a full treatment" | Not supported; C2 decides depth by factors |
| Prompt formulas and fixed tool settings as rules | The "how" belongs to the model and to Production's dated notes |
