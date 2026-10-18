> **V2.4 CANDIDATE SCOPE:** Modified version of this method family. Read the final section “V2.4 real-world hardening” for current candidate additions. Historical V2.3 discussion and prior-source pointers below remain provenance, not active version resolution.

# AI Creative Skill · Runtime Activation and Packaging · Pre-v0.8-V2.4-CANDIDATE

## Status

```text
DOCUMENT TYPE
=
RUNTIME ACTIVATION / PACKAGING DESIGN

VERSION
=
Pre-v0.8-V2.4-CANDIDATE

DATE
=
2026-10-16

PARENT_DOCUMENT
=
AI_Creative_Skill_Architecture_Spec

LAST_VALIDATED_AGAINST
=
AI_Creative_Skill_Architecture_Spec_Pre-v0.16-V2.3-CANDIDATE.md

STATUS
=
DESIGN DOCUMENT
NOT INSTALLED
HOST/RUNTIME NOT YET CHOSEN
```

This document defines how the future packaged skill should be discovered, activated and kept thin. It does not define creative craft, provider preference or spend authority.

Pre-v0.6 adds an overlap/activation canary for broad third-party skills so availability cannot seize current project authority or silently widen planning into generation, spend or publication. Existing host-neutral package-source, version-promotion, personal/sandbox separation and clean-distribution discipline remains in force. Host-specific plugin files and commands remain deferred until a runtime is selected.

---

# 1. Purpose

The package must solve two different problems without confusing them:

```text
ACTIVATION
=
should this skill handle/orchestrate the request?

ROUTING INSIDE THE SKILL
=
what bounded task path, profiles, methods and Execution Route are required?
```

Activation happens before Stage 0. It never authorizes generation, research, publication or spend.

---

# 2. Thin Router Principle

The final `SKILL.md` should be a thin router/orchestrator, not a copy of the entire architecture.

It should contain or point to only what is necessary to:

```text
recognize relevant requests
state hard activation boundaries
resolve package entry points
load authority/profile/method/runtime files just in time
preserve task completion / stop behavior
```

Deep craft remains in Specialist Methods. Volatile facts remain in the Registry. Concrete provider mechanics remain in Execution Route Recipes; reusable Provider Adapters are introduced only when implementation demonstrates the need.

```text
SKILL.md
≠
ALL KNOWLEDGE IN ONE FILE
```

---

# 3. Positive Activation Intents

The actual frontmatter/description must be tuned to the chosen host, but should cover semantic intents such as:

```text
generate / create / edit / adapt an image
create / edit / adapt a video
create or review creative assets
write or revise a creative script when the creative skill owns the requested deliverable
create variants from an approved concept/asset
review / QA / repair generated creative media
resume an interrupted creative-generation task
benchmark eligible creative-generation routes
```

Standalone research/synthesis should activate `RESEARCH_ONLY` when research itself is the bounded deliverable and the V2.3 candidate profile is available.

Supporting research inside an Ads/Organic final deliverable is a bounded subtask. It does not seize final-deliverable ownership.

Work-specific research or performance analysis otherwise activates only when the requested deliverable belongs to an applicable Work Profile or authorized extension.

Do not rely only on literal slash commands or a fixed list of English phrases.

---

# 4. Negative Activation Boundaries

Do not activate merely because a message contains words like “image”, “video”, “ad” or “content” when the requested deliverable is actually outside this skill.

Typical non-ownership cases include:

```text
pure factual Q&A with no creative deliverable
generic file conversion unrelated to creative production
ordinary conversation
software/API debugging whose goal is not this creative runtime
a task explicitly owned by another current authority/runtime and not delegated here
publication/campaign launch when no such authority exists
```

If the skill is already active and the user asks a small bounded subtask inside the current work, continue only if that subtask remains within the task/authority boundary.

---

# 5. Overlap / Ownership Resolution

When more than one installed capability could plausibly help:

```text
1. RESPECT SYSTEM / SAFETY / PLATFORM BOUNDARIES
2. RESPECT EXPLICIT USER TARGET / REQUESTED WORKSPACE
3. RESOLVE CURRENT PROJECT AUTHORITY
4. IDENTIFY WHO OWNS THE REQUESTED DELIVERABLE
5. DELEGATE ONLY BOUNDED SUBTASKS WHEN USEFUL
```

A broader creative skill should not seize a request that is explicitly owned by a narrower current authority. A narrow tool/capability should not silently become the orchestrator for a broader creative request merely because it can execute one technical step.

```text
OWNERSHIP
≠
CAPABILITY AVAILABILITY
```

No external governance skill is a mandatory dependency of this system.

## 5.1 V2.3 Final-Deliverable Precedence

For mixed requests:

```text
1. DECOMPOSE BOUNDED WORK UNITS
2. RESOLVE DEPENDENCIES
3. IDENTIFY THE FINAL REQUESTED DELIVERABLE
4. ASSIGN SUPPORTING RESEARCH TO RESEARCH_ONLY WHEN NEEDED
5. KEEP FINAL-DELIVERABLE OWNERSHIP WITH ADS / ORGANIC / OTHER APPLICABLE PROFILE
6. HAND OFF ONLY SCOPED STATE / EVIDENCE
```

Examples:

```text
"analyze these TikTok videos to see which products people want"
→ RESEARCH_ONLY

"research TikTok trends and then create a post"
→ RESEARCH_ONLY subtask
→ ORGANIC_CONTENT final owner

"research competitors and create three ads"
→ RESEARCH_ONLY subtask
→ ADS final owner

"find the exact product from these photos"
→ RESEARCH_ONLY + PRODUCT_MARKETPLACE_INTELLIGENCE

"use Higgsfield for the current video"
→ current creative owner remains unchanged
→ execution route changes
```

Provider/tool choice never becomes Work Profile ownership.


---

# 6. Activation Does Not Grant Authority

Even after activation:

```text
research may still be unnecessary
generation may still be unauthorized
spend may still require approval
a canonical reference may still be missing
a Project Profile may block a route
the requested deliverable may end before execution
```

Therefore:

```text
ACTIVATE
→ STAGE 0 AUTHORITY + TASK-PATH ROUTING
→ STAGE 1 STATE RECOVERY / MINIMUM SUFFICIENT TASK PATH
```

Never skip directly from activation to a paid provider call.

---

# 7. Just-in-Time Load Order

Typical load order after activation:

```text
1. CORE routing / authority rules
2. relevant Project Profile if any
3. relevant Work Profile
4. Specialist Method Stack required by the bounded task
5. current Model / Provider / Execution Route facts only when execution is needed
6. Execution Route Recipe only for the chosen executable route
7. calibration/failure cases only when materially relevant
```

Do not load all methods, providers and benchmark history for every request.

---

# 8. User-Facing Communication

Surface decisions that materially affect the user, for example:

```text
missing authority/input that blocks completion
material route/provider swap
cost quote / approval request
meaningful quality or evidence trade-off
unverified result dimension
final accepted/repaired deliverable
```

Do not narrate routine internal plumbing such as worker IDs, state-validation commands, file-loading mechanics or every internal routing branch unless the user specifically asks or the information is necessary to explain a blocker.

Ask only for information whose absence changes a material decision.

---

# 9. Completion / Exit

The runtime package must preserve the Architecture Task Completion Boundary.

```text
REQUESTED DELIVERABLE SATISFIED
→ persist required state/provenance
→ deliver
→ END TASK
```

Completion does not imply authorization for adjacent creative stages, additional variants, publication or spend.

---

# 10. Human-Readable File Naming

A packaged runtime may use a project-specific readable naming template, for example:

```text
{project}_{subject-or-deliverable}_{variant-or-part}_{timestamp}.{ext}
```

Rules:

```text
filename = convenience
asset_id = identity
hash = integrity
sidecar/index = lineage + provenance
```

Renaming a physical file must not rewrite or sever immutable asset identity.

---

# 11. Secrets / Host Packaging

The package must use the secure secret mechanism appropriate to its actual runtime.

```text
DO NOT STANDARDIZE ON .env
UNTIL THE CHOSEN HOST/RUNTIME MAKES THAT THE APPROPRIATE MECHANISM
```

Provider/Execution Route Recipe records may contain secret locators or binding names, never secret values.

---

# 12. Target Package Shape

## 12.0 Illustrative Tree Only

The following tree is illustrative only. **Only this tree is illustrative; §§12.1–12.4 below are normative packaging-design requirements.**

```text
creative-skill/
├── SKILL.md                    # thin activation/router layer
├── rules/
├── projects/
├── work/
├── methods/
├── calibration/
├── models/
├── providers/
├── routes/                     # concrete Route Recipes on demand
├── scripts/
└── tests/
```

Do not create empty files solely to make the tree look complete.

---

## 12.1 Authoritative Package Source and Installed Copies

The future runtime package must distinguish the **authoritative editable source** from installed, cached or copied runtime instances.

```text
AUTHORITATIVE PACKAGE SOURCE
→ REVIEW / VERSION / VALIDATE
→ DISTRIBUTED PACKAGE
→ INSTALLED / CACHED COPY
```

```text
INSTALLED COPY
!=
SILENT EDITING AUTHORITY
```

Material package changes should be made in the declared source, assigned an identifiable version, validated, and then promoted/distributed. A local edit to an installed copy does not become canonical merely because it runs successfully. The source mechanism may eventually be Git, a managed artifact store or another host-appropriate system; this design does not mandate GitHub.

The package source should support recovery or rollback to a known prior accepted version. Promotion to a newer package version is a governed change, not an implicit side effect of one contributor editing a file.

## 12.2 Shared / Team vs Personal / Sandbox Material

Do not equate a private shared repository with permission to place every project artifact inside it.

```text
SHARED / TEAM PACKAGE
= intentionally shareable project/company methods and runtime material

PERSONAL / SANDBOX PACKAGE
= private experiments, personal workflows, unapproved third-party skills, local-only context
```

Secrets, personal data, sensitive identity/voice references and experimental material remain governed by their own authority and access rules. They are not promoted into a shared package merely because all current collaborators are trusted.

## 12.3 Separately Invokable Package Units

A subprocess may become a separately invokable packaged unit when both are true:

```text
1. it has independent user/task value
2. it has a stable enough input/output boundary to run without forcing adjacent stages
```

If a subprocess only makes sense as an internal step of one bounded workflow, keep it internal rather than creating another public skill/plugin surface.

This is a packaging criterion, **not** a replacement for the Specialist Method System Growth Rule. A separately invokable package unit does not automatically imply a new Specialist Method, permanent agent or new authority domain.

## 12.4 Update and Promotion Discipline

Automatic synchronization may be convenient, but a new canonical package version must not bypass validation and governance.

```text
CHANGE
→ SOURCE REVISION
→ REQUIRED REVIEW / VALIDATION
→ ACCEPTED VERSION
→ DISTRIBUTION / UPDATE
```

Do not adopt host auto-update behavior as permission for unreviewed rules to change between runs. When a host supports automatic retrieval, the promoted version/channel remains the controlled boundary.

Host-specific marketplace files, commands, restart requirements and update mechanics are volatile implementation facts and must be verified against the selected runtime before use.

---

# 13. Acceptance Criteria for the Future SKILL.md

The eventual router passes packaging review when:

```text
activation description is specific enough to avoid obvious false positives
negative boundaries are explicit
activation never implies spend/generation authorization
overlap/ownership behavior is documented
JIT loading is possible
Core authority/order is preserved
Task Completion Boundary is preserved
provider/model specifics do not leak into generic activation text
host-required frontmatter / manifest shape is validated against the selected runtime
authoritative package source/version is identifiable
installed copies are non-authoritative for edits
shared package material respects sensitivity/access boundaries
package updates pass the declared promotion/validation gate
overlap canary prevents a broad third-party trigger from seizing current project authority or auto-executing
```

## 13.1 Overlapping third-party activation canary

The future package must include an overlap test for broad installed third-party skills/capabilities that could match the same request. Use a realistic ambiguous case such as:

```text
INPUT
= product image + “make a content plan / campaign” request

AVAILABLE
= current project authority + broad third-party content-factory capability
```

Expected result:

```text
1. resolve current project/work-profile authority first
2. select the narrow owner of the requested deliverable
3. invoke any third-party capability only as an explicitly bounded subtask when useful
4. do not let activation trigger generation, spend, publishing or adjacent campaign work
5. require normal route/budget/approval gates for any paid execution
```

A third-party skill being installed, discoverable or strongly matched is **availability**, not authority. The canary fails if a broad trigger seizes orchestration from the current project or silently widens a planning request into production/publication.


This document is design guidance. The real `SKILL.md` should be written only after the host/runtime and its skill-discovery semantics are chosen.


---

# 15. V2.3 Research-Only Reactivation Candidate

Positive standalone intents may include:

```text
research / compare / verify / synthesize current evidence
market / trend scan when research itself is the deliverable
buyer/review evidence synthesis
product / marketplace lookup and exact-match research
social/video evidence inspection for a research conclusion
```

Negative/overlap boundaries remain:

```text
existing image/video URL used as evidence
!=
image/video creation request

platform name
!=
Organic ownership

product photo lookup
!=
Image Direction ownership

research mentioned inside a requested ad/post
!=
RESEARCH_ONLY final ownership
```

`RESEARCH_ONLY` may complete without generation, publishing, contact, purchase or spend.

Packaging status in this branch is logical only. Whether it later lives in one physical skill package or a sibling package remains a host/runtime decision after behavior is validated.


---

## V2.4 real-world hardening — host-enforced method and output discipline

The thin host router must instruct activation to (1) resolve deliverable type/scope; (2) load Manifest and relevant Project/Work/Method; (3) load the completeness contract when a complete deliverable is requested; (4) select minimum stage path; (5) conduct substantive per-item validation before final handoff; (6) present one useful recommended next action only when there is an ongoing multi-stage project; (7) never treat guidance as authorization for spend, publication or generation.

The host must not claim a method was loaded unless file access occurred; `SKILL.md` availability alone is not usage. When JIT could not load the required method or output validator, disclose limitation, preserve `PARTIAL` or `UNVERIFIED`, and do not claim formal compliance. Host-specific capabilities are checked per tool rather than inferred from plugin installation.

