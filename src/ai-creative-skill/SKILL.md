---
name: ai-creative-skill
description: Use for evidence-grounded creative research and production (ads, organic, image, video, audio), creating or editing a functional landing page or website from a product photo/service/idea, image/video upscaling and postproduction, and scoped creative QA/repair. Prefer build-first FAST preview for website requests and provider-agnostic local media routes when available. Never infer permission for paid services or public deployment.
---

# AI Creative Skill · V2.5 Integrated Host Router

This `SKILL.md` is the thin host adapter for the V2.5 integrated distribution, with the inherited V2.4 method family preserved. It is not a replacement for the packaged architecture, profiles, methods, contracts, or project authority.

## Status boundary

- Installable V2.5 release with experimental Web Experience and Neural Upscale routes. Installing does not prove production readiness or modify external project canon.
- Activation is not authorization.
- Do not infer permission to spend, generate, publish, purchase, contact suppliers, sign contracts, transfer money, change account ownership, inspect unrelated repositories, or perform destructive actions.
- Preserve `UNKNOWN` when evidence is insufficient.
- A tool, provider, connector, model, marketplace, image, video, or URL being available does not make it the owner of the task.

## Canonical entry points

Load only what the current bounded task needs from `references/`.

1. Version resolution: `AI_Creative_Skill_V2.5_Integration_Manifest.md`, then inherited `AI_Creative_Skill_Current_Design_Manifest_Pre-v0.40-V2.4-CANDIDATE.md`
2. Core authority/task routing when material: `AI_Creative_Skill_Architecture_Spec_Pre-v0.17-V2.4-CANDIDATE.md`
3. Runtime activation/ownership when routing or overlaps matter: `AI_Creative_Skill_Runtime_Activation_and_Packaging_Pre-v0.8-V2.4-CANDIDATE.md`
4. Execution/approval/state semantics only when execution or persistent state is material: `AI_Creative_Skill_Execution_Contracts_Pre-v0.21-V2.4-CANDIDATE.md`
5. Specialist method selection: `AI_Creative_Skill_Specialist_Method_System_Pre-v0.14-V2.4-CANDIDATE.md`

Do not load every reference for every request.

## Activation

Activate when this workflow owns or materially orchestrates the requested deliverable, including:

- standalone research, comparison, verification, market/trend scan, buyer/review synthesis, or product/marketplace research where research itself is the bounded deliverable;
- paid-ad creative strategy or production;
- organic/social creative strategy or production;
- image, video, audio, script, talking-persona, typography/layout creation or adaptation;
- review, QA, localized repair, benchmarking, or resume of applicable creative work;
- a mixed request whose final deliverable belongs to Ads/Organic while bounded research is needed first.

Do not activate merely because a message contains words such as image, video, product, ad, content, TikTok, Instagram, marketplace, provider, or model.

Typical non-ownership includes ordinary factual Q&A, generic writing unrelated to an applicable Work Profile, unrelated software/API debugging, pure file conversion, a task explicitly owned by another current authority, or publication/purchase/contract action when no applicable authority exists.

## Stage 0 · Resolve ownership before work

For each request:

1. Respect system/safety/platform requirements.
2. Respect explicit user target, workspace, exclusions, and project authority.
3. Identify the final requested deliverable and completion condition.
4. Decompose mixed requests into bounded work units only when dependencies require it.
5. Resolve the Work Profile owner.
6. Load only the required specialist methods.
7. Keep provider/tool choice separate from method/work ownership.

Final-deliverable precedence examples:

- analyze social videos to identify wanted products → `RESEARCH_ONLY`;
- research trends, then create a post → Research bounded subtask, `ORGANIC_CONTENT` final owner;
- research competitors, then create ads → Research bounded subtask, `ADS` final owner;
- find the exact product from references → `RESEARCH_ONLY` + `PRODUCT_MARKETPLACE_INTELLIGENCE`;
- use a named provider for the current video → creative owner remains unchanged; only the eligible execution route may change.

## Web Experience · new in V2.5

If the user requests a **landing page, website or functional preview**, route to `WEB_PREVIEW` (or `WEB_EDIT` for an existing site). Use `AI_Creative_Skill_Work_Profile_Web_Experience_v0.2.md`. An image of a physical product, service description or idea can be sufficient to begin. Default **FAST**: brief → small targeted research if needed → provisional direction → reused/minimal assets → **actually build and open** navigable desktop/mobile preview → QA → user revisions. Never stop at a plan when a working page is requested. `WEB_RESEARCH_ONLY` and `WEB_CONCEPT_ONLY` stop at bounded requests.

Host development/browser skills and tools may be used as **bounded optional execution adapters**; do not claim they are part of this skill or require a named external skill. Detect available capabilities; if none can build or open an interactive site, report that limitation honestly. Do not automatically publish, register domains, capture personal information or fabricate a completed form. Use `web/schemas/web_delivery_v0.2.schema.json` and `scripts/creative_web.py` for deterministic routing, lifecycle and contract validation. They do **not** generate the website on their own.

## Media Upscale · new in V2.5

If the final deliverable is **image/video upscale**, consult `AI_Creative_Skill_Method_Media_Upscale_v0.3.md`, registry `media/registry/provider_capabilities_v0.3.json` and `scripts/creative_media.py`. Distinguish image from video, interpolation from neural SR, 1080p from 4K, and technical completion from visual fidelity approval. Discover local route availability per host; never mandate Higgsfield/fal/Runway or assume credentials/credits. Conventional Pillow/FFmpeg routes are optional based on installed dependencies. Neural routes require separately provisioned checkpoints/hardware and remain experimental. Unknown or mock remote routes must never submit. Preserve approved source, face/product, logos/labels, audio and FPS. No paid execution or public upload without explicit authority.

## Research Only

When research itself is the deliverable, load:

- `AI_Creative_Skill_Work_Profile_Research_Pre-v0.1-V2.3-CANDIDATE.md`
- `AI_Creative_Skill_Method_Research_Evidence_Synthesis_Pre-v0.3.md`

Add only when needed:

- buyer/review interpretation → `AI_Creative_Skill_Method_Buyer_Research_Pre-v0.3.md`
- product/listing/seller/variant identity or exact-match semantics → `AI_Creative_Skill_Method_Product_Marketplace_Intelligence_Pre-v0.1-V2.3-CANDIDATE.md`
- video evidence inspection → `AI_Creative_Skill_Method_Video_Evidence_Inspection_Pre-v0.7.md`
- ad/funnel evidence → `AI_Creative_Skill_Method_Ad_Funnel_Intelligence_Pre-v0.4.md`

Research completion does not authorize generation, publication, supplier contact, purchase, or spend.

## Ads / Organic

For final ad deliverables, load `AI_Creative_Skill_Work_Profile_Ads_Pre-v0.8.md` and only the specialist methods required by that task.

For final organic/editorial/social deliverables, load `AI_Creative_Skill_Work_Profile_Organic_Pre-v0.7-V2.4-CANDIDATE.md` and only the specialist methods required by that task.

Supporting research does not become final owner merely because it runs first.

## Product / marketplace identity

When an exact entity matters:

- distinguish product family, product variant, listing, seller, brand, and source product reference;
- obey `EXACT_MATCH_REQUIRED`, `SIMILAR_ALLOWED`, or `SIMILAR_AS_FALLBACK_ONLY` as resolved from user/project authority;
- never promote visual similarity into manufacturer/source certainty;
- preserve stable source/canonical product identity through downstream handoff;
- allow presentation copy to vary only as presentation copy, never as silent rewrite of source identity;
- keep PARTIAL, insufficient evidence, and UNKNOWN distinct from NO_RESULTS or confirmed facts.

## Cross-profile handoff

When ownership changes between bounded tasks, use the V2.3-inherited `HANDOFF_PACKET` / `PROFILE_SWITCH_EVENT` semantics from Architecture and Execution Contracts.

A handoff may transfer relevant state/evidence/constraints, but must not silently transfer authority for spend, publication, purchase, contracts, destructive actions, account ownership, or unrelated resources.

Preserve project continuity across task completion. Completing one bounded task does not close a persistent project.

## Autonomy

When the user grants broad autonomy, resolve it by action class under the V2.3 `AUTONOMY_ENVELOPE`; do not reduce it to a global boolean.

A persistent exclusion remains in force until explicitly changed. Tool access or connector availability never widens that exclusion.

## Execution

If real external execution is required:

1. Resolve authority and eligibility first.
2. Resolve capability before model, model before execution route.
3. Use Provider Registry/Route Recipe facts only when execution is actually needed.
4. Respect quote, approval, budget, snapshot/fingerprint, job/retrieval, ingest, QA, repair, and stop semantics from current packaged references.
5. Do not silently swap provider/route or infer success from a provider response without required ingest/review evidence.

## Completion

Use the minimum sufficient task path.

When the requested completion condition is satisfied:

- persist only required state/provenance;
- deliver the requested result;
- end the bounded task;
- do not auto-expand into adjacent research, generation, variants, publishing, purchase, or spend.

A subsequent user request gets a new routing decision while persistent project state remains available according to authority and freshness.


## V2.4 mandatory deliverable checks and non-blocking creative guidance

When a full in-scope deliverable is requested, after resolving owner and minimum required method stack, **load** `AI_Creative_Skill_Deliverable_Completeness_Catalog_Pre-v0.1-V2.4-CANDIDATE.md`. Use the applicable contract and method rubrics before delivering. `FULL` character bible, each `CONTENT_IDEA` in a batch, narrative video direction, storyboard plan, selected reference manifest and project next-action guidance have distinct requirements. Structural completeness without actual useful content is a fail. When the host cannot load a mandatory reference or required fact is unknown, disclose `PARTIAL`/`UNVERIFIED` rather than claiming full compliance; no invented biography, source or seller proof.

For an original AI influencer/character requested as *complete*, include a causal backstory, distinguishing look, personality, unique value, canon vs scene variation and appropriate disclosure; visual/audio attributes only as applicable. For ideas, include **Hook**, **Format & Hold**, **Setting**, **Why It Works** (clearly evidence vs hypothesis) and payoff **for every idea**. Optional creative enrichment is encouraged, never a reason to omit required fields or rewrite protected intent.

For a multi-beat video, guide naturally from concept/intent to optional exploratory storyboard to revised narrative script, then references/preflight/approved generation. Storyboard is a planning artifact and *not* a forced shot-by-shot provider command. Prefer narrative `Setting & Atmosphere` + continuous `Script & Creative Direction` + invariants + creative-open zones for story-led film; `Text on Screen` is optional, and exact timestamps only when the job actually requires them. An approved existing storyboard or simple one-shot can avoid redundant creation. User may skip nonessential planning steps; do not override a direct bounded request.

When ongoing project context makes it useful, after completing the requested task briefly say what was done and recommend **one** high-value next step; do not execute it without applicable authority. `USER APPROVED SCRIPT` != `GENERATION AUTHORIZED` != `PUBLISHED`. Confirm host capability, reference authority, price/approval and actual QA before any external paid generation. Record method-use provenance honestly: a description of the skill is not evidence that references were loaded. Preserve earlier authority/ownership/cross-profile and budget semantics.


When Python/file execution is available, the optional deterministic shape checker is bundled at `scripts/validate_deliverable.py` and its machine-readable contract at `contracts/deliverable_contracts_v0.1.json`. Run per-item completeness validation for FULL deliverables. The checker detects absent/blank fields only; human/model semantic QA remains mandatory and cannot be described as deterministic validation. If host cannot execute scripts, use the same bounded rubric self-review and mark its evidence honestly.
