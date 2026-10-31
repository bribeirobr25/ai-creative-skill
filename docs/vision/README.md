# System vision

**Status:** the direction the owner set on 2026-10-30, recorded in [ADR-0006](../decisions/ADR-0006-system-direction-agent-teams.md).
It is a guide for what to build and in which order, not a fixed specification. It authorizes no build, spend, connection, publication or external contact; each step in the sequence needs its own owner authorization.

**The goal in one sentence:** an agentic system, organized in areas with specialists, that helps its users reach their goals with good quality through guided steps, while leaving the agents as free as possible to be creative and use their best knowledge.

## Where this comes from

The project started as a skill to make ad videos easier with Higgsfield. It widened to other tools, then to research, websites, product photos, AI influencers and video post-production, and the V2.5 package grew to 38 reference documents, about 20 of them methods. The blind container test (October 2026) asked how much a skill should guide a model and how much it should leave open. The owner saw no quality difference; two blind AI judges found no clear winner and leaned slightly against the full package; on Claude the package was never loaded. The direction it pointed to: guide what the model cannot know or reliably skips, and leave the craft to the model. The test was small (one copy task and one image task, three runs each), so this is a direction, not a proof. This vision builds on that answer; it does not discard the earlier work.

## What the system is for

One system that helps people do creative work **and** run the business around it.

**1. Creating the work, in any format**
- Video: ad videos, motion graphics, AI films and series, cartoons, soap operas.
- Visual and brand: logos and brand identity, photoshoot campaigns, product photos, websites.
- People on screen: AI influencers, virtual spokespersons, talking-head and UGC-style videos.
- Words: books, scripts, copy for ads, pages and emails; titles, descriptions and thumbnails for videos.
- Channels and digital products: faceless video channels, guides, templates and other digital products to sell.
- Audio: voice-over, voices for characters, music and sound for videos.
- Marketing content: ad creative and organic posts.
- New formats are added as new specialists (see "Adding an area or a specialist").

**2. Running the business around the work**
- Market, competitor and trend research, for data and for inspiration.
- Offer and pricing: what to sell, to whom, for how much.
- Finding leads, outreach by email, closing deals.
- Selling goods: marketplace listings and storefronts (for example Amazon, Etsy, a shop), product pages.
- Creating, posting and managing ads; measuring what works.

**Who it serves**
- A brand that needs creative work.
- A solopreneur building an AI service company, an AI marketing agency or an AI product company, to sell services or goods.
- A creator selling their own creative work: books, cartoons, series, music.
- An agency serving many clients, where each client's brand, data and approvals stay separate.

## How a user works with the system

Guided steps are the main way the system improves outcomes. A user should never face a blank page, and never be locked into one path.

1. **Intake.** The user states a goal ("launch my AI marketing agency", "a 10-episode cartoon", "sell my product on Etsy"). The system gathers what it needs: who the user is, the brand or story, the audience, budget, deadlines, what already exists, and the user's taste.
2. **Plan from a playbook.** A playbook is a proven sequence for a type of goal, across areas. Example for a new service business: research the niche, define the offer, build the brand, the website, the content, the ads, then the leads and outreach. The plan states each step, its deliverable, its cost estimate and where the user approves.
3. **Guided stages with checkpoints.** Each deliverable moves through proven stages, for example brief, then storyboard, then generation, then review. The user approves at the checkpoints that matter: the brief, the direction, a stage's execution scope with its spend limit, and anything published, sent or contacted. An execution scope says what is generated, what may vary, how many items and attempts, and with which kind of tool. Inside it, agents generate and explore variants without asking each time. Money left in the budget is not permission: anything outside the scope (another tool, another deliverable, more attempts) needs a new approval.
4. **Delivery.** Finished work in a usable form: files, a live site, a published post, a sent campaign, a listed product, a book in a store, an episode on a channel.
5. **Measure and learn.** Results flow back: ad performance, site visits, replies, sales, the user's own ratings. They feed the plan's next steps and the specialists' own experience.

At any point the user can see what is happening, what it costs so far, what is waiting for approval and what was learned. How this is shown (records, the host's own views, or a dashboard) is decided in the shared-core design; a dedicated dashboard is not yet in scope.

For an agency, the end client may be the approver: approvals, revision rounds and feedback are recorded per client, separate from the agency's own.

## How it is organized: areas, leads and specialists

The skill idea evolves into areas of agents. Each area has a lead that plans, assigns and reviews; specialists do one kind of work. A starting map, not a fixed list:

| Area | Lead decides | Specialists (examples) |
|---|---|---|
| Research | What to scan, how fresh it must be | Market and competitors, trends, inspiration boards, marketplace research, audience research |
| Visual & Brand | Direction and consistency across outputs | Logos and identity, photoshoots and product photos, websites, motion graphics |
| Story | Story bible and continuity | Books, scripts, series and soap operas, cartoons, AI films |
| Growth | Campaign plan and use of the budget | Ad creative and ad videos, organic content, AI influencers and spokespersons, ad management, measurement |
| Sales | Offer, pipeline, deals | Offer and pricing, leads, outreach, deals, marketplace listings and storefronts |

**Production** is shared by every area: image generation, video generation, editing and assembly (clips into long pieces for films, series and soap operas), post-production (reframe, upscale, repair) and voice and audio. Other shared specialists: copy, translation and localization, and independent quality review.

**A project lead** turns the user's goal into a plan across areas and keeps it on track. Most user goals cross areas: a product launch needs Research, Visual & Brand, Growth and Sales.

**How agents work together**
- Agents hand work to each other through shared, dated records, not through chat history. The research board feeds the leads; ad results feed back to the creative specialists.
- Each project has one shared context every agent reads: facts, brand kit or story bible, decisions, approvals, the asset library. It follows the record contract of [ADR-0005 D5](../decisions/ADR-0005-PROPOSED-container-decision-and-adr-0004-disposition.md#d5--memory-one-contract-separate-instances-no-new-engine); the Project Brain is the first instance and the template.
- An agent can ask another agent for what it needs ("Research: what hooks do competitors in this niche use this month?") instead of guessing. Requests and answers are recorded, so the user can follow them.
- Review is independent: the final check against the required elements is done by a reviewer with a fresh context and no stake in the verdict, not by the lead that produced the work. Repair rounds are capped; at the cap the question goes to the user.
- Leads coordinate; they hold no authority of their own. Only the user grants permissions, and no agent passes a permission to another. This is why the earlier rejection of "permanent agent orgs, CEO authority and scheduled routines" (External Skill Analysis Ledger, ai-agent-team) does not apply: what it rejected was authority and unchecked automation, which this design also excludes.
- Each agent must actually load its knowledge. The container test showed a skill that was installed but never read; the vertical slice checks that each pack is used.
- Every agent earns its place: it exists only if the checks show it does better than a generalist doing the same job. More agents means more cost and more handoffs that can fail.

## The business half, in the same depth

The same rules apply to business work: proven stages, required elements, and the model deciding how.

- **Sales:** ideal customer, lead list, qualification, outreach sequence, follow-up, proposal, contract, invoice and payment, client onboarding. Required elements include consent to contact, a clear offer and a recorded next step.
- **Ad management:** launch within budget, pacing, testing variants, watching for creative fatigue, kill-or-scale rules, reporting. Required elements include the platform's policies, the AI-disclosure rules and a spend cap.
- **Selling goods:** listing, product page, pricing, fulfilment hand-off, reviews handled honestly (no synthetic testimonials).

## Guidance and freedom

Models improve fast. Guidance that dictates *how* ages and can hold a better model back. Guidance that says *what* and *why* keeps its value.

**Guidance fixes**
- What the model cannot know: the user's facts, brand and taste; niche and market knowledge; past results; how specific tools fail.
- Steps models reliably skip: closing and verification steps, such as producing and checking the delivery record. In the October style test only 1 of 18 runs did it, and only the shared checker caught a visible defect.
- Proven stages, in order. Example: brief, then storyboard, then generation, for an ad video or motion graphics. The storyboard is also a cheap checkpoint before paid generation.
- Required elements of a good result. Examples: an ad campaign has a niche, a hook, an offer and a call to action; a book has a premise, characters and a structure; a logo works small, in one colour and does not resemble an existing mark.
- Limits: spending, sending, publishing, contacting people, rights.
- What "done" means for each deliverable.

**The model decides** everything else: which idea, which hook, the style, the wording, how the storyboard is drawn, the order of its own steps, which allowed tool to use. The model's own knowledge comes first; a knowledge pack adds what the model lacks, it does not replace what the model knows.

**Freedom rules**
- Open by default: anything not fixed by guidance is the agent's choice.
- A proven stage is a default, not a cage. An agent may skip or change it when it has a better way, if it says why. Never skipped: a checkpoint that protects money, publication, contact or rights, and the closing and verification steps. A standing permission the user has granted is how the user answers such a checkpoint in advance, not a skip.
- Agents propose, not only follow: alternative directions, a better tool, a question the user did not ask. Real alternatives need an outside input (the user's choice, a different style brief, a rule): asking the same agent for options produced the same direction in the October tests.
- Every piece of guidance earns its place. It stays only while checks or real results get worse without it, and it is re-tested when models change. The test exists so that guidance a newer model no longer needs is dropped. How it is measured is an open owner decision (see "How quality is judged"); until then, guidance and agents are adopted provisionally and marked unproven.

## Knowledge per specialist: three layers and a learning loop

| Layer | Example (motion graphics) | Example (script writer) | How it changes |
|---|---|---|---|
| Proven core | Storyboard first, timing, readability | Structure, character goals, a hook in the first seconds | Rarely; only with strong evidence |
| Current knowledge | Styles and techniques in use now; what leading studios and competitors do | Formats and tropes working now in the genre and on each platform | Refreshed from sources on a schedule; expires |
| Own experience | What the user approved or rejected; what performed | What readers or viewers responded to | Grows with every project |

**The learning loop, per specialist**
1. **Sources:** a vetted list per specialty, each rated for reliability.
2. **Intake:** new material is pulled on a schedule.
3. **Analysis:** patterns and why they work, not copies; each finding keeps its source and date.
4. **Candidates:** findings become candidate learnings, kept apart from trusted knowledge.
5. **Adoption, by layer:**
   - **Current knowledge** (trends, competitors, tools) is added with its source, reliability, date and expiry, once a reliable source states it or two sources agree. It is knowledge the agent may use, not a rule it must follow, and it is visible in the digest, where the user can remove it. Waiting for results would make it expire before it is ever used.
   - **The proven core and any rule** change only through an act the user or owner makes on purpose, with evidence that results improve. Nothing becomes a rule automatically.
6. **Expiry:** current knowledge is re-checked or dropped when its date passes.

**Safeguards**
- Learning means curated, dated knowledge the agent reads, not retraining a model, so the user can always see what an agent learned and from where.
- A trend can be added beside the proven core; replacing a core practice needs evidence.
- Fetched web content is data, never instructions. A page cannot change an agent's rules.
- Patterns, not copies: no reuse of other people's work, brands or likenesses.
- The user gets a short digest per specialist (learned, adopted, expired) and can remove any item.
- Scheduled learning and research cost money and run outside any one project. They draw on an operating budget the owner sets for the system, never on a user's project budget.
- Learning from one user's private results stays with that user unless they agree to share it.

## Research has a shelf life

Every market, competitor or trend finding carries the date it was checked and a date to check again (for example two weeks for trends, one to two months for competitors). When the date passes, the system re-runs the research on a schedule or reminds the user, and shows what changed since last time. The Brain's `review_by` field and the "due for review" list in `brain status` are the first form of this.

The same applies to tools: what a tool can do, what it costs and how it fails also changes, so tool knowledge carries dates too.

## Tools and connections, by permission level

Tools stay replaceable; the provider registry in the frozen package is already provider-neutral. Examples: Higgsfield, Runway and image or video APIs for creation; Perplexity, Amazon, Google Shopping, Etsy and TikTok for research; Meta Ads, Instagram and TikTok for posting and ads; email and CRM tools for sales. Any other tool can be added.

| Level | Examples | Rule |
|---|---|---|
| Read | Marketplace, social and web research | Allowed; official APIs where they exist, within each platform's terms. Many marketplace and social APIs are restricted, so research often needs a paid data provider, which is the spend level |
| Spend | Image or video generation, paid APIs, paid research data, ad budget | Within an execution scope the user approves for a stage (what, how many, which tool class, spend limit); no per-job approval inside it, a new approval for anything outside it. Each paid attempt is traceable; a partial batch is never blindly re-run. Cost estimated before, reported after |
| Act outward | Posting, launching or changing ads, sending email, listing a product, publishing a book or episode | User approval per action, or a standing permission the user grants for a named action |
| Credentials | API keys, tokens, passwords | Never in the repository; held by the host or the user's own secret store |

- **Least privilege:** each agent gets only the tools and levels its job needs. A research agent cannot post; a script writer cannot spend.
- **Permissions are not carried:** these levels map onto the autonomy rules kept from ADR-0004 (I3 `permissions_carried: NONE`, I4 autonomy per action class) and the frozen package's autonomy envelope. A standing permission is an entry the user grants, recorded with its authority, re-checked on every effect and never passed on by delegation.
- **Once only:** an outward action that may have run is never blindly repeated (ADR-0004 two-level idempotency, kept by ADR-0005).
- [ADR-0003](../decisions/ADR-0003-PROPOSED-development-review-and-publication-safety.md) and its gates protect what is published to this repository; outward actions for users follow the autonomy rules above.

## Rights, compliance and trust

Cross-cutting rules every area follows. They are limits, so guidance fixes them.

- **Rights:** use only material the user may use; record the source, tool and licence of every asset; check new logos and names against existing marks before adoption.
- **Likeness:** no real person's face or voice without consent; AI influencers and spokespersons are clearly fictional or used with consent.
- **AI disclosure:** follow each platform's and each country's rules for labelling AI-generated content and ads.
- **Advertising and marketplace policies:** each platform's ad and listing rules are part of the required elements.
- **Outreach:** email and contact follow consent and anti-spam law in the recipient's country; opt-outs are honoured.
- **Truthful claims:** claims only from the user's facts; unknowns stay unknown.
- **Privacy:** each user's and each client's data stays separate and private; nothing private enters the public repository.
- **Accessibility:** websites meet common accessibility standards (WCAG), videos carry captions, images carry alt text.
- **Human professionals:** some steps need a person, for example a lawyer for a trademark search, a real photoshoot, or a voice actor's consent. The system says so and prepares the handoff instead of pretending.

## Assets and continuity

- **Brand kit:** logo, colours, fonts, voice and examples, read by every agent working for that brand.
- **Story bible and character sheets:** characters, world, canon, episode state, voices, for books, series, cartoons and AI influencers.
- **Asset library:** every generated or supplied asset with its version, source, tool, prompt and rights, so work can be reused, continued and audited.
- Continuity across long projects is tested with the memory scenarios T01–T08 (ADR-0004, kept by ADR-0005).

## Languages and markets

Users and their audiences work in many languages and countries. Content is created in the audience's language and adapted to local culture, platforms and law, not only translated.

## Adding an area or a specialist

A new format ("among other creative work") is added as a specialist with a short definition:
- the deliverables it produces and what "done" means;
- the required elements and the proven stages, with checkpoints;
- its knowledge pack: vetted sources and starting knowledge;
- the tools it may use, and at which level;
- the checks that show it earns its place.

## Where the existing work fits

| Existing work | Role in the new direction |
|---|---|
| V2.5 package (frozen, `src/`) | Raw material: its methods are mined into knowledge packs, marked unproven until they earn their place; the package itself is not edited |
| Methods for ads strategy, ad funnel, buyer research, scripts, image, video, audio and voice, talking persona, typography, organic content, marketplace, localized repair, QA and rights | Starting knowledge for the Growth, Visual & Brand, Story, Research and Sales specialists |
| Website research (DQB-01/02/03, style catalogue, niche layouts, preference profile) | Websites specialist knowledge; owner taste goes to the private half |
| Photoshoot prompt study and its learnings | Photoshoot specialist knowledge (clean references, shot list) |
| Video reframe and upscale benchmarks | Production: post-production knowledge and tool facts |
| Specialist Method System (task-relative creative latitude §6.2, divergence before convergence §6.4) | The guidance-and-freedom balance, already worked out for creative tasks |
| Deliverable Completeness Catalog and `contracts/deliverable_contracts_v0.1.json` | Required elements and "done" per deliverable |
| Execution Contracts (approvals, budget ledger, job states, autonomy envelope) | Checkpoints, budgets and permission levels |
| Calibration and Experience Memory (barrier between observed and trusted knowledge, creative preference memory) | The candidate-versus-adopted split in the learning loop; own experience |
| Research Evidence Synthesis (freshness and verification before acting) | Research shelf life |
| Ad Funnel, Platform Meta, Buyer Research methods | Growth and Sales knowledge |
| Provider registry | Tool knowledge, dated |
| Creative-quality research (`docs/research/creative-quality/`, four-axis evaluation) | Starting point for the evaluation design |
| Intelligence lab (`experiments/intelligence`) | Input to the Research area design; Gate 0 still applies |
| Benchmark checks C1–C9 | Acceptance checks for agents and guidance |
| Project Brain and record contract | Template for shared project context |
| Safety gates, rulesets, pre-push check | Base for the act-outward level and for keeping private data out |

Pilot 01 stays abandoned and is not part of this direction.

## How quality is judged

- **Required elements present:** checked by the independent reviewer before delivery.
- **The user's judgement:** approvals, rejections and ratings, recorded as experience.
- **Real results:** ad performance, conversion, replies, sales, audience response, where the work is published.
- **Checks and simulation:** the benchmark checks and simulation over recorded evidence (the evaluation-method decision of 2026-10-30).

**Open owner decision: the evaluation design.** "Earns its place" needs evidence that results get worse without a piece of guidance or an agent. The benchmark checks C1–C9 test restraint and safety, not creative quality, and simulation can only reuse evidence already recorded. Live blind studies like the October test are no longer planned. A proposal for the shared-core design: recorded owner ratings on real work, comparisons inside real projects (the same deliverable with and without a pack), and the four-axis rubric from the creative-quality research. Until the owner decides, guidance and agents are adopted provisionally.

## Sequence

Each step is separately authorized by the owner.

1. **Record the direction** (this document and ADR-0006). Done.
2. **Before any real project:** back up the private half offline (it is the only copy of the study data and will hold client data); choose the agent host and check it against the kept contract and T01–T08, recorded in the benchmark log (ADR-0005 D6); decide the evaluation design; choose a secret store for credentials; decide the private-half layout; authorize the slice's budget; review its rights questions.
3. **Design the shared core.** Short specifications for: an agent role, a knowledge pack, a playbook, the shared project context (brand kit, story bible, asset library), a research record with freshness, the permission levels. Choose the agent host, preferring host-native agents, delegation and scheduling (ADR-0005 D6), and decide where new code lives (not `src/`, which stays frozen).
4. **One vertical slice on a real project, chosen by the owner.** One playbook end to end, for example: research, inspiration board, storyboard, generation, owner approval, manual posting, measurement. Generation and measurement run with tools the owner authorizes for the slice; posting stays manual. It tests intake, handoffs, pack loading, freshness, the memory scenarios T01–T08 and the permission levels on real work.
5. **The learning loop** for the slice's specialists.
6. **Connections, level by level:** read first; then spend within an approved execution scope; then act outward with approval.
7. **Widen area by area,** each new agent, pack and playbook earning its place through checks.

**Open threads, folded in**
- DQB-01, DQB-02 and DQB-03 still await the owner's review: closed as history or mined into the websites pack in step 3.
- Intelligence Gate 0: revisited as part of the Research area design in step 3.
- Memory scenarios T01–T08 and benchmark check C8: tested in the vertical slice.

## Not decided yet

- Which host or framework runs the agents.
- Where new code, knowledge packs and playbooks live, and which parts belong in the private half (client data, owner taste, account state).
- How future users reach the system: the owner's own tool first, a service for clients, or a product others install.
- The first real project for the slice, and its budget.
- Which connections come first.
- The evaluation design (see "How quality is judged").
