# AI Creative Skill · Project context snapshot · 2026-10-27

**Type:** dated context snapshot (session recovery record). **Not** an authority document, decision, approval or canon change.
**Why it exists:** a working session was interrupted by an OS update. The context was rebuilt from GitHub, the repository and an owner-supplied transcript of the planning conversation. This file keeps that consolidated picture, so the next session doesn't have to reconstruct it.
**Baseline when written:** `main` = `23c6dd641d5554178da67698c0008c8934811be4`. PR #17 head = `0baac348d94aa8006bde7ae374de331d5cfeaff7`. PR #30 head = `1487512035e5734dea62530af5e7e1a77cbcd416`.
**Freshness rule:** everything below is a snapshot. Re-read live GitHub state (PRs, issues, checks, ruleset) before acting on it.

---

## 1. What the project is, and why

**AI Creative Skill** is a provider-neutral skill for AI agents, distributed as an Agent Skill ZIP and an OpenAI-style portable plugin ZIP. It turns a request into validated creative output: research, paid ads, organic/social content, image, video, audio and script, talking personas, typography and layout, and (since V2.5) functional **websites/landing pages** and **image/video upscaling**.

From the Architecture Spec §1: *"The skill is not a prompt collection and not merely an API wrapper. It is a decision, execution, verification and learning system."*

**Why it is built:** the owner runs real creative work on recurring projects:
- Pilot 01, a recurring-persona project;
- Della, a product brand;
- diBoaS, the owner's own platform, used as a benchmark brief.

The skill exists to produce this work with less identity and canon drift, honest QA, controlled cost and no lock-in to any single vendor (Higgsfield, fal, Runway and so on).

### Core principles (Architecture Spec §§2–3, ADR-0001, ADR-0002)
- **Authority order:**
  1. law, platform and safety;
  2. explicit operator governance decision;
  3. project canon and locked approvals;
  4. Project Profile;
  5. Work Profile;
  6. specialist methods;
  7. creative core defaults;
  8. external methods and provider defaults.
- **Minimum sufficient task path and bounded completion:** do only what was asked, deliver, stop. Suggest at most one next step, and never execute it implicitly.
- **Unknown stays UNKNOWN.** Evidence ≠ instruction. Requirement ≠ compliance. Skill specification ≠ skill behaviour.
- **Activation is not authorization.** Spend, publication, generation, contact with third parties and canon changes are always gated separately.
- **Order of choice:** capability, then model, then execution route. Provider choice never changes task ownership.
- **ADR-0001:** one canonical source tree (`src/ai-creative-skill/`). ZIPs are generated, never edited. Media and private material live outside Git. The installed skill must work without GitHub or Drive.
- **ADR-0002:** every capability shares the common architecture **and** can be invoked and finish on its own (ENTRY → EXECUTION → VERIFICATION → EXIT → optional NEXT). There are three modes: end-to-end, standalone capability, standalone sub-operation. Acceptance tests T1–T7 are not yet run (Issue #1).

### Shape of the skill (`src/ai-creative-skill/`)
- `SKILL.md`: a thin host router. Stage 0 ownership resolution, then the Work Profiles: `RESEARCH_ONLY`, `ADS`, `ORGANIC_CONTENT`, `WEB_EXPERIENCE` (with `WEB_RESEARCH_ONLY`, `WEB_CONCEPT_ONLY`, `WEB_PREVIEW` (FAST, build-first), `WEB_EDIT` and `WEB_PUBLICATION`), and `MEDIA_UPSCALE`.
- `references/`: about 38 normative documents, mostly the inherited V2.4 family. They cover:
  - Architecture Spec, Execution Contracts, Specialist Method System, Runtime Activation;
  - Calibration & Experience Memory, Current Design Manifest;
  - methods for research, buyer research, ad funnel, product/marketplace, image, video, audio/voice, script, talking persona, typography, route compilation, QA, localized repair, media upscale;
  - Provider Registry, the Pilot 01 Project Profile, release gates and the V2.5 Integration Manifest.
- **Runtimes:**
  - `web/runtime/`: router, validate, preview, qa, revision, migrate, cli;
  - `media/runtime/`: Pillow/FFmpeg Lanczos and experimental Real-ESRGAN;
  - `scripts/`: `creative_web.py`, `creative_media.py`, `validate_deliverable.py`, `smoke_install.py`;
  - `contracts/deliverable_contracts_v0.1.json`.
- **Five responsibility layers:** Governance & State · Creative Core · Production Specification · Replaceable Execution · QA/Delivery/Learning.

---

## 2. History

| Version | Date | Essence |
|---|---|---|
| V2.0 | 10-10 | Transactional contracts (snapshot/fingerprint, exact approval binding, cancellation). About 3.6M zero-cost regression checks |
| V2.1 | 10-10 | Async/callback hardening after the Z2/Z3 validations |
| V2.2 / V2.2.1 | 10-11 | Creative latitude (`PRESERVE / BOUNDED_VARIATION / OPEN_EXPLORATION`, `SAFE…EXPERIMENTAL`). V2.2.1 exists in two **unreconciled** historical versions (A/B) |
| V2.3 | 10-11 | Architecture reactivation from real-user evidence: `RESEARCH_ONLY`, `PRODUCT_MARKETPLACE_INTELLIGENCE`, `HANDOFF_PACKET`, `PROFILE_SWITCH_EVENT`, `PROJECT_CONTINUITY_STATE`, `AUTONOMY_ENVELOPE` |
| V2.4 | 10-16 | Real-world hardening: completeness per deliverable, storyboard/script iteration, product fidelity, localized-repair preservation |
| **V2.5.0** | 10-18 | Web Experience + Media Upscale. Moved from Drive into GitHub with SHA-256 attestation (74 files). **Immutable baseline at `39a0bfa`**, plugin version 0.3.0 |
| **2.6.0-dev** | 10-21 → | The `main` development line. **Not a release** |

V2.0–V2.4 were developed as candidate branches in Google Drive (`00_ACTIVE`, `90_ARCHIVE` and so on). Drive is kept as the media and history store; see `docs/migration/`.

---

## 3. What is implemented on `main`

| Area | State |
|---|---|
| V2.5.0 core (methods, contracts, profiles, router) | ✅ preserved byte for byte, verified by CI |
| Boundary hardening v1 (PR #7) | ✅ **the only change to `src/` since V2.5.** Fixed F01–F06: preview containment, publication rights and use-scope, protected-content verdict, linked-asset retest, negation routing, whitespace-only content |
| Web Experience runtime | ✅ local: routing, contracts, preview, static QA. The site itself is built by the host agent |
| Conventional upscale (Pillow/FFmpeg) | ✅ executable where dependencies exist |
| Neural upscale (Real-ESRGAN) | 🟡 experimental; needs checkpoints and hardware; fidelity not approved |
| Validation harness (PR #6) | ✅ synthetic probes, mutations, pairwise cases, illustrative economics |
| Security gate (PR #20) | ✅ publication guard on every PR, plus the history audit and private triage tools |
| Intelligence Architecture v0.3 (PR #18) | Docs merged. **Gate 0 not passed** |
| Intelligence offline lab S1–S3 (PR #23) | ✅ synthetic only: 222 tests, no real sources |
| Research records | Creative quality phases 1–2, DQB-01, DQB-02, video upscale, media reframe, owner preference profile |

### Governance and CI
- **Two-gate model:**
  - `release_integrity` exports `39a0bfa` and re-runs the original V2.5 tests, smoke test and builders;
  - `candidate_integrity` + `candidate_tests` check the current source against a separately versioned candidate inventory.
  
  Historical hashes are never regenerated. Any new `src/` change needs a new reviewed candidate inventory.
- **Workflows:**

  | Workflow | Jobs | Required |
  |---|---|---|
  | `validate.yml` | `Immutable V2.5 integrity`, `Boundary hardening candidate` | yes |
  | `publication-guard.yml` | `scan-publication-diff` | yes |
  | `intelligence-consolidated-review.yml` | `Single-package synthetic integration` | no |
  | `reframe-quality-r1.yml` | path-filtered | no |

- **Ruleset "Push Protection"** is active on `main`: squash-only, linear history, no force push or deletion, the three required checks, review threads must be resolved, **0 required approvals**. Secret scanning and push protection are on.
- **Publication guard:**
  - **BLOCK:** tokens and keys, signed URLs, realistic Drive IDs, private filenames, binary-patch tricks.
  - **REVIEW:** emails, share links, binaries and media.
  
  It scans the added lines and each commit, and does not check EXIF or pixels.
- **Security audit S0:** closed by owner attestation, with residual limitations. One stable Drive folder link remains in three `src/` files (`media/README_PTBR.md` and `media/registry/provider_capabilities_v0.2.json`/`v0.3.json`). It will be fixed in milestone M0b.
- **Packaging:** `packaging/build.py` is **deliberately pinned to V2.5** (manifest plus attestation), so a 2.6 release needs a new, independent builder.

---

## 4. Research and validation: findings so far

| Date | Study | Outcome |
|---|---|---|
| 10-18 | Video upscale 480p→1080p | Higgsfield ran Topaz Starlight. It kept texture but **invented label text**; Real-ESRGAN looked plastic. Fidelity PARTIAL. The method-doc edits were not applied |
| 10-20 | Validation baseline (PR #6) | 139 PASS / 16 FAIL (six families). Decision 001: known failures stay FAIL; a green CI run is not approval |
| 10-20 | Boundary hardening (PR #7) | 308 PASS / 0 FAIL → merged into `src/` |
| 10-20 | Media reframe R1 | Pillow/FFmpeg crop works; tracking and outpainting not proven; research candidate only |
| 10-20 | Creative Quality phase 1 | *"The clearest demonstrated improvement is the review loop."* A hero image collapsed to 6.59 px while every functional check passed |
| 10-20 | Creative Quality phase 2 | P1 (rendered visual checkpoint) ready for integration consideration; human review packet has 0 responses; not landed |
| 10-20 | DQB-01 | AWAITING_HUMAN_REVIEW; no aesthetic gain shown; condition C (native Higgsfield) never run |
| 10-21 | Visual Direction Candidate v0.1 (PR #12) | Closed without merge |
| 10-21 | DQB-02 | INCONCLUSIVE, leaning REVISE. Same fonts in 8 of 8 runs; about 33% more time; no measurable visual difference |
| 10-21 | Photoshoot prompts, skill vs manual (in PR #29) | Skill 36/45 vs manual 29/45; five gaps (no `PRODUCT_CONTENT` profile, no shot taxonomy, and others) |
| 10-22 | DQB-03 (PR #29) | INCONCLUSIVE. "Diverge, then choose" did not change the chosen direction → not adopted. Field test of #17 found no regressions |
| 10-22 | 18-style site test and learnings audit (PR #28) | Same hero photo on 13 of 18 sites; only 1 of 18 executors wrote the delivery record. Audit has 23 finding IDs and a 19-item backlog |

**Recurring weaknesses:**
- Visual defects get past functional QA.
- First-pass design converges on the same look.
- Reference steps are ignored.
- Small text and labels break under generation, upscale and reframe.
- No evidence from a clean host or an automatically activated agent: the seven journeys and T1–T7 have never run.
- Unix-only runtime.
- Vendor parity has not been measured.

**Recurring review limits:**
- Zero independent blind human reviewers in any study.
- Coordinator and owner feedback was non-blind.
- n = 1–2 per condition.
- Agents were isolated by instruction only.
- Chromium only.

**Owner web preference profile** (`docs/research/preference-profiles/…v0.1.md`): 18 preferences (P01–P18), such as rounded-rectangle images instead of arches, uniform product grids, and at most two lines of hero title on mobile. It is a research candidate, **not installed**, and belongs in a Project Profile. The owner tends to combine components from several alternatives.

---

## 5. Intelligence (Track D)

- **Goal:** an in-house intelligence capability for content, products and ads. It has two routes: analytics on the owner's own accounts, and licensed external market discovery. No unlicensed scraping, no "viral score", no automatic spend or publishing.
- **Gate 0 (G0-01..05):** a single research owner and vocabulary, a typed MetricObservation, no paid call without Approval + Ledger, field/purpose/retention rights, and typed geo/time bases. State: `GATE_0_NOT_PASSED / OWNER_ACCEPTANCE_PENDING`. Unresolved questions include who owns the metric method and the §24 SourceCapabilityRecord amendment.
- **Stages:**
  - S0: closed by attestation.
  - S1–S3: synthetic lab merged via #23.
  - **S4** (resilience): not started.
  - **S5** (first real source): not authorized.
  - **S6** (integration into `src/`): not authorized.
- The lab always reports `may_access_real_source / may_spend / may_store_real_data / may_publish = false`. Approved TikTok developer access is administrative access, **not** operational authorization.
- `docs/research/intelligence/STATUS.md` still describes #20 and #23 as unmerged candidates. It must say "synthetic code merged; canonical authority not approved".

---

## 6. The evolution: proposal v1.1 → ADR-0004 (PR #30)

### Where it came from (owner requests)
1. A **memory manager** so information is never lost and memory updates efficiently as a project goes on.
2. **Content repurposing**: trailers, shorts and teasers from longer videos.
3. **Agents named after professions:**
   - Leads Finder: ICP fit, running ads, website photos.
   - Outreach: drafts and sends emails daily, and asks the Leads Finder for more leads.
   - Ads Specialist: works for existing clients, lowers acquisition cost, studies competitors' winning ads, requests footage, and sends reminders when materials are late.
   - Later: Ads Writer, Photographer, Graphic Designer, Video Maker, Social Media Manager, and a suggested Performance Analyst.
4. **Agent-to-agent chat**, so agents can request work from each other.
5. **Quick visual dashboards**, for example a simple CRM: a header with open rate, replies and calls booked, and a board with New Lead / Emailed / Replied / Call Booked.

### Refinements adopted in the planning conversation
- Agents are **roles on top of the existing methods**, not new sources of authority. No per-agent memory and no duplicated methods.
- **Six memory categories:** project canon, project state, decisions, asset memory, experience memory, operational memory. Memory is event-based, not a single file rewritten over and over. An agent may record what happened, but **may not promote a hypothesis to canon**. Periodic consolidation catches contradictions and stale facts.
- **Content repurposing is an invocable capability**, not a new Work Profile. It combines Video Direction, Organic Content Craft §2.1 (atomization), Reframe, Audio, Localized Repair and QA, with asset lineage and rights tracking.
- **Competitor ads:** study their hooks, structure, pacing, proof and CTAs. **Never copy creatives.** "Popular" does not mean a lower CPA or a higher ROAS.
- **The Ads Specialist has creative autonomy inside the `AUTONOMY_ENVELOPE`.** Changes to budget, launches and publication remain gated.
- **Agent chat runs on structured messages and persistent tasks.** A reminder at 18:00 needs a real scheduler and notifications, not a rule written into a prompt.
- **Outreach:** in Germany, UWG §7 generally requires prior consent for email advertising, including B2B. GDPR gives people the right to object, and opt-outs must be honoured. Outreach therefore **prepares messages only** until the legal basis is set and the owner approves sending.
- **The CRM is a view of the event store**, not a separate database.

### Architecture (ADR-0004 PROPOSED)
- **L1, skill core:** portable, `src/`, packaged.
- **L2, invocable capabilities:** run stateless (everything in the request) or stateful (receive the retrieved context and *propose* events). L2 never imports L3.
- **L3, state and memory:** an optional service holding the event store, materialized state, decisions, assets and lineage, experience, operational state, context retrieval, and a separate erasable store for personal data.
- **L4, Agent Workspace:** optional and separately versioned. Agent Role Contracts, coordinator, tasks, messages, scheduler, notifications, dashboards and CRM, all as views of L3.
- **Cross-cutting responsibilities** (not mandatory servers):
  - [C] contracts;
  - [G] governance and security (approvals, Budget Ledger, STOP, autonomy, privacy, guard, CI, ruleset);
  - [A] adapters;
  - [V] validation.

### Invariants (v1.1 §1, summarized)
1. One authority per subject.
2. Bounded invocation (ADR-0002).
3. Skill canon ≠ project canon.
4. Delegation never widens permissions (`permissions_carried: NONE`).
5. Autonomy is set per action class.
6. Memory is event-based and idempotent, and keeps fact / request / decision distinct.
7. A new concept needs an owner, a versioned contract and a reason. EC §1.1 is for aliases only. New Specialist Methods go through the Growth Rule.
8. `src/` changes only through a versioned candidate inventory, and V2.5 stays immutable.
9. Nothing private goes in the public repo.
10. Immutable history and erasable personal data coexist.
11. Maturity, validation and authorization are distinct dimensions, always stated explicitly.

### Contract core (specified and tested in pre-M2)
- **Event fields:**
  - identity and schema: `event_id`, `idempotency_key`, `schema_family/schema_version`, `project_id`;
  - what it is: `event_kind` (OBSERVED · CHANGE_REQUESTED · DECISION_RECORDED), `event_type` (the specific happening, e.g. ASSET_CREATED), `object_type/object_id`;
  - concurrency: `expected_revision/resulting_revision` (a stale write gets `STALE_WRITE_REJECTED`, EC §2.3);
  - who and why: `actor`, `authority_ref` (mandatory for decisions), `causation_id/correlation_id`, `evidence_refs`, `supersedes`;
  - privacy: `privacy_class/retention_policy_ref`, `personal_data_refs`;
  - time: `occurred_at/recorded_at`.
- **Task fields:** id, idempotency key, project, capability, requester and assignee, inputs, status, dependencies, optional deadline, authorization limits, completion condition, revision, correlation, `permissions_carried: NONE`.
- **Message kinds:** conversation, task_request or handoff. Every executable delegation becomes a task.
- **Capability Registry:** a derived view with three dimensions: technical maturity, contextual validation (always scoped to host, route, version and date) and authorization (read from the existing owners). It is never a new certification authority.
- **Agent Role Contract:** goal, capabilities and tools, memory scope, autonomy envelope, limits on delegation, retries, cost and concurrency, and escalation rules.
- **Technology:**
  - SQLite from M2, with JSONL only as an audit export;
  - PostgreSQL only for real multi-user needs;
  - a semantic index only later, and always rebuildable;
  - media stays outside the database.

### The three adjustments added before ADR-0004 (now included in it)
1. **Privacy:** storing only references does not anonymize anyone. Actor, IDs, timestamps, paths, logs, exports, indexes and backups can identify people, so deletion must be verifiable, including backups. Never promise absolute deletion.
2. **External idempotency:** event idempotency ≠ idempotency of external effects. Every external operation keeps an attempt identity, durable state and reconciliation, and an unknown state never authorizes automatic resubmission. M2 tests local recovery; before M4/M5, a simulated external job with a lost confirmation is tested.
3. **2.6 packaging:** a new, independent builder. The V2.5 reproduction path is preserved, and the 2.6 ZIPs that were actually built are installed on a clean host.

### Repository boundary
- New areas: `apps/agent-workspace/` (generic L3/L4 code) and `schemas/` (canonical [C] until promoted to `src/` in a post-2.6 candidate, e.g. 2.7).
- `src/` never imports `apps/` or `experiments/`.
- Databases, operational logs, media, client data, credentials and per-client configuration stay **outside** the repo. This is enforced by `.gitignore` plus scanner **BLOCK** rules, which today only mark `.db/.sqlite` as REVIEW, plus adversarial tests that include `git add -f`.

### Explicitly not now
- All layers at once.
- Pre-approving contract fields for future milestones.
- A vector database, message broker or microservices.
- Continuously running autonomous agents.
- Real spend, publishing or sending email.
- Real Intelligence sources.
- Widening the scope of #17.
- Another general redesign.

---

## 7. Implementation sequence

```text
Track A  Core & distribution   M0 ─► M0b ─► M1 ─► [release 2.6 gate] ─► 2.7 candidate (schemas)
Track B  Memory & operation    pre-M2 ─► M2 ─► M3 ─► M4 ─► M5 ─► M6   (isolated in apps/; own gate)
Track C  Real quality          QB-1 product ─► QB-2 character ─► QB-3 video/audio ─► QB-4 upscale/reframe
Track D  Intelligence          decisions ─► S4 synthetic ─► S5 real-source canary ─► M7
```

| Milestone | Usable delivery | Done when | Owner decision |
|---|---|---|---|
| **M0** | #17 updated from main and merged without widening scope; STATUS.md fixed; Issue #24 updated | CI green on the exact head; **the 7 browser tests actually run** (SKIP ≠ PASS); audit closed | Merge #17 (D-M0-01) |
| **M0b** | Drive link → logical IDs in a separate candidate after #17; act at the source (folder permissions) | Inventory verified; scanner clean | Merge; source action |
| **M1** | 2.6 builder; real ZIPs on a clean host; T1–T7 on website, research and photo direction; contextual validation records | Reproducible runs; failures recorded; human acceptance | Release 2.6 (D-M1-01) |
| **pre-M2** | Event and task schemas plus contract tests (idempotency, revision, kinds, privacy) | Schemas validated; independent review | Accept the core (D-P2-01) |
| **M2** | SQLite Memory v1, CLI (record / query / resume), erasable store tested with fixtures, boundary rules | 8 pilot scenarios + adversarial boundary tests | Storage, retention, pilot project (D-M2-01, D-M2-02) |
| **M3** | Repurposing v1: cutting by supplied timecodes first, then multi-format; transcription only when needed; lineage | Duration, audio, FPS and framing checked; human editorial review | Transcription tool; rights to the material |
| **M4** | Ads Specialist + Writer + Video Maker with role contracts, persistent tasks and the registry | Correct delegation, no loops, no inherited authority, within cost | Autonomy envelopes (D-M4-01) |
| **M5** | Dashboards, a persistent scheduler, notifications, crash recovery | Reminder fires on time; dashboard matches state | Hosting and credentials (D-M5-01) |
| **M6** | CRM with fictitious data first; ICP qualification; prepared messages only | Pipeline is a view of the events; privacy active before any real leads | Real data; legal basis per market |
| **M7** | First research with an authorized real source | Read-only test; coverage, rights and cost explicit | Gate 0, source, credentials, rights (D-D-01) |

**Dependencies:**
- M2 ← pre-M2.
- M4 ← M1 (registry) + M2 (tasks).
- M5 ← M4.
- M6 with real data ← privacy work from M2/M5.
- M7 ← Track D decisions.
- Schemas into `src/` ← release 2.6.
- Track B does not wait for 2.6.
- The order of the QB benchmarks may change if material is ready.

**Memory pilot: the 8 M2 acceptance scenarios**
1. Record decisions and asset references with provenance.
2. Restart without losing state.
3. Run an independent operation from the recovered context.
4. Record the delivery and its lineage.
5. Revoked decisions never come back as current.
6. The same operation runs stateless.
7. Interrupt before confirmation, resume, and show no duplicate task, event or asset.
8. An authority change (EC §10.1) invalidates **only** the dependents it actually affects (`ACCEPTANCE_INVALIDATED`).

Also required:
- A stale write is rejected.
- Project A never reads or affects project B.
- A forced database or log commit is blocked.
- A legitimate fixture passes.
- Deletion reaches content, metadata, indexes and copy expiry, or the backup limitation is documented honestly.

**Process for every milestone:** a closed acceptance checklist before any code, then its own branch, local tests, required CI, the scanner, independent review in proportion to risk, and a merge authorized by the owner. Each functional delivery includes a demo. The loop is build → use on a real case → record → short retrospective → versioned adjustment. Metrics: time to delivery, number of repairs, first-try acceptance, cost, and reproducible failures opened and closed.

---

## 8. Open work on GitHub (at snapshot time)

| PR | What | State |
|---|---|---|
| **#17** `feature/web-runtime-2.6` | 2.6.0-dev web runtime. **v1:** natural build-request routing; 1440/390/320 checks; lazy images; undecoded images; `#/route` links not counted as broken; path redaction; `--project-root`. **v2:** collapsed-image detection; `file://` audit without a preview server; `--static-only`; mandatory delivery record (`record`, `UNFILLED_FIELD`); web profile steps 6–8; Route Compilation §7.2 reference crops; Image Direction §§5.1/9.1 and Localized Repair §6.2 label composites. 83 candidate tests; `release_approved: false` | Open and mergeable, but **3 commits behind main**. `scan-publication-diff` has **never run on it**. No GitHub review; v1 was independently reviewed, v2 was not. **Audit item 3 (F-C2, text normalisation) is missing**, although the PR says it covers items 2–8 |
| **#28** `research/style-catalog-2026-10-22` | Learnings audit, a 4-axis style catalog (aesthetic, layout, surface, motion) with 18 cards, styles by niche (47 niches), 18-style test summary | Open, green, research only. The body says 25 findings; the audit has 23 IDs |
| **#29** `research/dqb03-slim` | DQB-03 (text-only slim) + photoshoot prompt comparison | Open, green. Replaces the closed #27 (binaries blocked by the guard) |
| **#30** `docs/a0-agent-workspace-adr0004-20261027` | A0: ADR-0004 PROPOSED, M0 checklist, pre-M2/M2/pilot checklist, execution register | **Draft**, green. Technical review comment (12:06): *"DOCUMENTATION REVIEW PASS / READY FOR OWNER DECISION"*. Not an approval |

**Learnings audit backlog (#28), not yet in the v1.1 inventory:**
- **2.7:**
  - a `PRODUCT_CONTENT` profile and shot list;
  - a prompt-pack recipe for running outside the skill;
  - a fabric zoom check;
  - style catalog v1;
  - the owner chooses the direction, and the hero image is a recorded decision;
  - the preference profile with a conflict rule;
  - port the collector's checks into `qa.py`;
  - resized images for the web;
  - a benchmark guide and privacy checklist.
- **3.0:** a label compositing script; automatic style recommendation.

**Other branches:** everything else is merged, superseded or abandoned on purpose. The experiment branches for DQB-02/03 directions stay unmerged, and heavy visual evidence stays on the closed PR branches.

**Issues:**
- #1: ADR-0002 T1–T7.
- #4: six mixed ZIP archives in Drive `utils`.
- #24: the ruleset now exists. Still open:
  - 0 approvals required;
  - no CODEOWNERS file;
  - actions not pinned to commit SHAs;
  - tags not protected;
  - no test yet that a failing check really blocks a merge;
  - the issue text is out of date.

---

## 9. Pending owner decisions

**A0 / roadmap (execution register):**

| ID | Decision |
|---|---|
| D-A0-01 | Approve or revise ADR-0004 |
| D-A0-02 | Authorize the squash merge of #30 |
| D-M0-01 | Authorize the #17 merge |
| D-M1-01 | Approve release 2.6 |
| D-P2-01 | Accept the event/task core |
| D-M2-01 | Storage, retention, project and assets |
| D-M2-02 | Accept/merge Memory v1 |
| D-M4-01 | Agent autonomy envelopes |
| D-M5-01 | Hosting, credentials, notifications |
| D-D-01 | S4 scope, then Gate 0/S5 |

Also: who owns Track C, and which benchmark comes first (by M1); the transcription tool (M3); real personal data and the legal basis per market (M6).

**Intelligence:**
- Accept Gate 0 / v0.3.
- Choose the owner of the metric method (a RES amendment or a new Specialist Method) and reconcile `engagement_observed`.
- Confirm the §24 SourceCapabilityRecord amendment.
- Decide who owns the identity of third-party creators and channels.

**Governance:**
- Formally accept ADR-0003, which is still PROPOSED although #20 is merged.
- Close out Issue #24.
- Classify the Issue #4 archives.

**The six open questions in the learnings audit:**
1. AI disclosure on sites.
2. Label compositing as the standard approach.
3. The Croissant lining.
4. Whether the owner's preferences apply globally or only to Della.
5. Recommend one style or two to three.
6. Merge 2.6 with items 1–8 now.

---

## 10. Discrepancies and risks found in this session

1. **In-tree docs are behind the merges.** Intelligence `STATUS.md` and Issue #24 predate #18, #20 and #23.
2. **#17 is behind main**, the new required check has never run on it, and audit item 3 is missing.
3. **"Pilot 01" means two things.** In the A0 memory plan, "Piloto 01" is a small real project (Della was suggested). In the skill canon, Pilot 01 is the recurring-persona project, run by a separate private operations skill and under a documentation freeze. **Recommendation:** rename the memory pilot (for example "Memory Pilot MP-01") before M2.
4. **The proposal v1.1 is not committed.** ADR-0004 and the register cite it as an owner attachment, and the #30 review asks for that reference to be preserved. This snapshot summarizes it; the full text remains with the owner.
5. **Two AI tools work on the repo in parallel.** ChatGPT, through a GitHub connector, did the planning, A0 and the review; Claude Code web did #28/#29. The v1.1 inventory was written when only #17 was open. Use the execution register as the single list of open work and update it whenever any tool opens or closes work.
6. **The skill is not installed in the owner's own agent account** (checked 2026-10-27), so M1 will be its first real host install. A broad-trigger third-party content skill (`higgsfield-content-factory`, which auto-schedules to Meta Ads) is present in the owner's synced skills. Pilot 01 Project Profile §3.1 records that it stays disabled during Pilot work, so check whether it is enabled.
7. **The relationship between the AI Creative Skill and the separate Pilot 01 operations skill is undefined.** It must be settled before any Pilot 01 data enters Memory v1.
8. The publication guard checks PR diffs only. It does not audit history retroactively and does not check EXIF.

---

## 11. Recommended next steps (not authorized by this document)

1. **Small A0 follow-up on the #30 branch:**
   - commit the proposal v1.1 text (sanitized);
   - rename the memory pilot;
   - add the #28/#29 backlog and the missing item 3 to the execution register.
2. Owner decisions **D-A0-01** and **D-A0-02**.
3. **M0:**
   - bring #17 up to date from main;
   - add item 3;
   - let the three required checks run;
   - run the 7 browser tests for real;
   - get an independent review of v2;
   - reconcile STATUS.md and Issue #24;
   - owner authorizes the merge.
4. **pre-M2, in parallel and isolated:** event and task schemas plus contract tests, under their own authorization.
5. Merge the research PRs #28 and #29, which are independent of the above.

---

## 12. Source index

- Repo: `README.md`, `CHANGELOG.md`, `docs/decisions/ADR-0001..0003`, `docs/history/`, `docs/migration/`, `docs/research/**`, `validation/**`, `security/README.md`, `.github/workflows/`, `packaging/build.py`, `src/ai-creative-skill/SKILL.md` and `references/` (Architecture Spec §§1–4, Pilot 01 Project Profile, V2.5 Integration Manifest, Release Gates v2.5, Web Experience profile v0.2, Media Upscale README).
- Branches: `origin/feature/web-runtime-2.6`, `origin/docs/a0-agent-workspace-adr0004-20261027` (all 4 files), `origin/research/style-catalog-2026-10-22`, `origin/research/dqb03-slim`.
- GitHub: PRs #17, #18, #20–#30 (bodies, comments, reviews), Issues #1, #4, #24, the ruleset.
- Owner-supplied transcript of the planning conversation (2026-10-26/27): the capability inventory, the owner's requests, the evolution proposal v1.1, the three adjustments, the A0 authorization and its delivery.
