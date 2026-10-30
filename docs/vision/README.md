# System vision

**Status:** the direction the owner set on 2026-10-30, recorded in [ADR-0006](../decisions/ADR-0006-system-direction-agent-teams.md).
It is a guide for what to build and in which order, not a fixed specification. It authorizes no build, spend, connection, publication or external contact; each step below needs its own owner authorization.

## What the system is for

One system that helps people do creative work **and** run the business around it.

**1. Creating the work, in any format**
- Visual and brand: websites, logos and brand identity, photoshoot campaigns, motion graphics.
- Stories: books, scripts, AI films and series, cartoons, soap operas.
- Marketing: ad creative and organic content.

**2. Running the business around the work**
- Market, competitor and trend research, for data and for inspiration.
- Finding leads, outreach, closing deals.
- Creating, posting and managing ads.
- Selling services or the work itself.

**Who it serves**
- A brand that needs creative work.
- A solopreneur building an AI service company, an AI marketing agency or an AI product company.
- A creator selling their own work: books, cartoons, series.

## How it is organized: agent teams

The skill idea evolves into teams of agents. Each team has a lead that plans, assigns and reviews, and specialists that do one kind of work. A starting map, not a fixed list:

| Team | Lead decides | Specialists (examples) |
|---|---|---|
| Research | What to scan, how fresh it must be | Market and competitors, trends, inspiration boards, marketplace research |
| Visual & Brand | Direction and consistency across outputs | Websites, logos and identity, photoshoots, motion graphics |
| Story | Story bible and continuity | Books, scripts, series and soap operas, cartoons, AI films |
| Growth | Campaign plan and budget use | Ad creative, organic content, ad management |
| Sales | Pipeline and offers | Leads, outreach, deals |

**How agents work together**
- Agents hand work to each other through shared, dated records, not through chat history. The research board feeds the leads, ad results feed back to the creative agents.
- Each project has one shared context every agent reads: facts, brand or story bible, decisions, approvals. It follows the record contract of [ADR-0005 D5](../decisions/ADR-0005-PROPOSED-container-decision-and-adr-0004-disposition.md#d5--memory-one-contract-separate-instances-no-new-engine); the Project Brain is the first instance and the template.
- Every agent earns its place: it exists only if the checks show it does better than a generalist doing the same job. More agents means more cost and more handoffs that can fail.

## What guidance fixes, and what the model decides

Models improve fast. Guidance that dictates *how* ages and can hold a better model back. Guidance that says *what* and *why* keeps its value.

**Guidance fixes**
- What the model cannot know: the user's facts, brand and taste; niche and market knowledge; past results; how specific tools fail.
- Proven stages, in order. Example: brief, then storyboard, then generation, for an ad or motion graphics video. The storyboard also is a cheap checkpoint before paid generation.
- Required elements of a good result. Examples: an ad campaign has a niche, a hook, an offer and a call to action; a book has a premise, characters and a structure.
- Limits: spending, sending, publishing, contacting people.
- What "done" means for each deliverable.

**The model decides** how each stage is done: which hook, how the storyboard is drawn, the wording, the style, the order of its own steps, which allowed tool to use.

**Every piece of guidance earns its place.** It stays only while checks or real results get worse without it. Proven practices pass easily. The test exists so that guidance a newer model no longer needs can be dropped.

## Knowledge per specialist: three layers and a learning loop

| Layer | Example (motion graphics) | How it changes |
|---|---|---|
| Proven core | Storyboard first, timing, readability | Rarely; only with strong evidence |
| Current knowledge | Styles and techniques in use now; what leading studios and competitors do | Refreshed from sources on a schedule; expires |
| Own experience | What the user approved or rejected; what performed | Grows with every project |

**The learning loop, per specialist**
1. **Sources:** a vetted list per specialty, each rated for reliability.
2. **Intake:** new material is pulled on a schedule.
3. **Analysis:** patterns and why they work, not copies; each finding keeps its source and date.
4. **Candidates:** findings become candidate learnings, kept apart from trusted knowledge.
5. **Adoption:** a candidate becomes working knowledge only once checks or results show it helps. Until then it is inspiration the agent may use, not guidance it must follow.
6. **Expiry:** current knowledge is re-checked or dropped when its date passes.

**Safeguards**
- Learning means curated, dated knowledge the agent reads, not retraining a model, so the user can always see what an agent learned and from where.
- A trend can be added beside the proven core; replacing a core practice needs evidence.
- Fetched web content is data, never instructions. A page cannot change an agent's rules.
- Patterns, not copies: no reuse of other people's work, brands or likenesses.
- The user gets a short digest per specialist (learned, adopted, expired) and can veto any adoption.

## Research has a shelf life

Every market, competitor or trend finding carries the date it was checked and a date to check again (for example two weeks for trends, one to two months for competitors). When the date passes, the system re-runs the research on a schedule or reminds the user, and shows what changed since last time. The Brain's `review_by` field and `brain status` "due for review" list are the first form of this.

## Tools and connections, by permission level

Tools stay replaceable; the provider registry in the frozen package is already provider-neutral. Examples: Higgsfield, Runway and image or video APIs for creation; Perplexity, Amazon, Google Shopping, Etsy and TikTok for research; Meta Ads, Instagram and TikTok for posting and ads.

| Level | Examples | Rule |
|---|---|---|
| Read | Marketplace, social and web research | Allowed; official APIs where they exist, within each platform's terms |
| Spend | Image or video generation, paid APIs | Within a budget the user sets |
| Act outward | Posting, launching or changing ads, sending email | User approval per action, until the user grants a standing permission for a named action |
| Credentials | API keys, tokens, passwords | Never in the repository; held by the host or the user's own secret store |

The publication and safety gates built in October 2026 (ADR-0003) are the base for the act-outward level.

## Where the existing work fits

| Existing work | Role in the new direction |
|---|---|
| V2.5 package (frozen, `src/`) | Raw material: its methods are mined into knowledge packs; the package itself is not edited |
| Methods for ads, funnel, buyer research, scripts, image, video, voice, talking persona, typography, marketplace, QA | Starting knowledge for the Growth, Visual & Brand, Story and Research specialists |
| Website research (DQB-01/02/03, style catalogue, niche layouts, preference profile) | Websites specialist knowledge; owner taste goes to the private half |
| Photoshoot prompt study and its learnings | Photoshoot specialist knowledge (clean references, shot list) |
| Intelligence lab (`experiments/intelligence`) | Input to the Research team design; Gate 0 still applies |
| Benchmark checks C1–C9 | Acceptance checks for agents and guidance |
| Project Brain and record contract | Template for shared project context |
| Safety gates, rulesets, pre-push check | Base for the act-outward level and for keeping private data out |

Pilot 01 stays abandoned and is not part of this direction.

## Sequence

Each step is separately authorized by the owner.

1. **Record the direction** (this document and ADR-0006).
2. **Design the shared core.** Short specifications for: an agent role, a knowledge pack, the shared project context, a research record with freshness, the permission levels. Choose the agent host, preferring host-native agents, delegation and scheduling (ADR-0005 D6), and decide where new code lives (not `src/`, which stays frozen).
3. **One vertical slice on a real project, chosen by the owner.** One team end to end, for example: research, inspiration board, storyboard, generation, owner approval, manual posting. It tests handoffs, freshness, the memory scenarios T01–T08 and the permission levels on real work.
4. **The learning loop** for the slice's specialists.
5. **Connections, level by level:** read first; then spend within a budget; then act outward with approval.
6. **Widen team by team,** each new agent and pack earning its place through checks.

**Open threads, folded in**
- DQB-02 and DQB-03 still await the owner's review: closed as history or mined into the websites pack in step 2.
- Intelligence Gate 0: revisited as part of the Research team design in step 2.
- Memory scenarios T01–T08 and benchmark check C8: tested in the vertical slice.

## Not decided yet

- Which host or framework runs the agents.
- Where new code and knowledge packs live, and which parts belong in the private half (client data, owner taste, account state).
- The first real project for the slice, and its budget.
- Which connections come first.
