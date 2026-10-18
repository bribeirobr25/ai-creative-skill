# Drive cleanup: decision register (2026-10-18)

**Project:** AI Creative Skill, historical Drive folder `influencer/` only.  
**Authority:** inventory/cleanup evidence, not permission to destroy unique history.  
**GitHub base:** AI Creative Skill V2.5.0 remains a baseline under validation.  
**Drive retained as media and historical safety source pending documented cut-over.**

## Corrected inventory

The 15 current top-level subfolders contain **693 immediate child entries combined** (not an exhaustive recursive total), after eliminating a confirmed empty branch-setup temporary directory. The earlier 434 figure understated the archive because its folder fetch was capped at the first 100 entries.

- `90_ARCHIVE`: **359 Markdown files**, completely paginated using Drive's document search. These include approximately 34 External Skill Analysis Ledger snapshots, 33 Current Design Manifest snapshots, 29 Provenance Map snapshots and other versions. The exact text and reverse dependencies of the 359 files have **not** been individually verified.
- `00_ACTIVE`: **31 Markdown files**, of which **11 exact text matches** are present in GitHub V2.5 and **20 have older/distinct basenames** (not declared duplicates).
- `analysis/my_skill_audit`: 43 native Google Docs and other audit artifacts; potentially unique evidence, not suitable for automatic public GitHub import.
- `analysis/future_capabilities_backlog`: Media Upscale, Web Experience, technical experiments and pilots; some image/video assets, native Docs and ZIPs are embedded.
- `utils`: vendor research material, PDFs, other people's example skills and bundles; rights and provenance require separate handling.
- `skill-real-test-1`: project-specific persona references and production material, excluded from generic public GitHub migration.
- `01_V2`–`07_V2.5` and `releases`: historical candidate directories, execution evidence and ZIP rollback assets, retained.

## Deletion disposition and gate

| Class | Quantity confirmed | Current decision | Reason |
| --- | ---: | --- | --- |
| Accidentally created, **empty** branch-setup folder | 1 folder | **DELETED**, verified absent on Drive | Confirmed exact parent/name and zero children |
| Same-name and **exact-content** V2.5 files in `00_ACTIVE` | 11 documents | **CANDIDATE ONLY / HOLD_LINK_REFERENCES** | Equal text to public GitHub; 1 revision and 0 comments each, but historical links and authority bindings may reference Drive IDs |
| Other `00_ACTIVE` files | 20 documents | **KEEP / NOT_PROVEN_REDUNDANT** | Different historical versions from GitHub V2.5; not byte-covered |
| `90_ARCHIVE` | 359 documents | **KEEP / AUDIT_HISTORICAL_VARIANTS** | Historical versions, not proven redundant merely by filenames |
| V2.5 original ZIPs and hash/evidence files | 7 direct entries | **KEEP / ROLLBACK** | Portable distribution rollback and source attestation |
| V2.0–V2.4 candidate ZIPs/docs/tests | several folders | **KEEP UNTIL RETENTION DECISION** | Not all historical candidates are committed to Git |
| Pilot character/product media and records | multiple subfolders | **KEEP IN PROJECT STORAGE** | Explicitly not skill source; cannot be placed indiscriminately on public GitHub |
| External/vendor research bundles | multiple files | **KEEP PENDING RIGHTS REVIEW** | No right to republish third-party material follows from Drive access |
| `30_INBOX` empty operational folder | 1 folder | **KEEP** | Existing operational entry point, not accidental temp |

### 11 exact matching documents (not yet deleted)

- `AI_Creative_Skill_External_Skill_Analysis_Ledger_Pre-v0.35.md`
- `AI_Media_Provider_Registry_v0.12.md`
- `AI_Creative_Skill_Project_Profile_Pilot01_Pre-v0.7.md`
- `AI_Creative_Skill_Method_Typography_Layout_Pre-v0.8.md`
- `AI_Creative_Skill_Method_Provenance_Map_Pre-v0.30.md`
- `AI_Creative_Skill_Work_Profile_Ads_Pre-v0.8.md`
- `AI_Creative_Skill_Method_Video_Evidence_Inspection_Pre-v0.7.md`
- `AI_Creative_Skill_Method_Ad_Funnel_Intelligence_Pre-v0.4.md`
- `AI_Creative_Skill_Method_Research_Evidence_Synthesis_Pre-v0.3.md`
- `AI_Creative_Skill_Method_Buyer_Research_Pre-v0.3.md`
- `AI_Creative_Skill_Method_Platform_Meta_Pre-v0.1.md`

**Exact-match details:** connector text comparison returned byte-equivalent character content for all 11 matching files. Drive revision lists returned one available revision and no prior revision; comment reads returned zero comments for all 11. This does **not** preserve original Drive IDs or links, or prove all external historical references migrated.

## Before permanent deletion of any document

1. Verify all current versions and authority/link dependencies, including references in prior delivery notes and current Pilot workflow.
2. Confirm source-content retention with committed GitHub version and successful readback of every candidate.
3. Keep rollback packages and evidence until explicit retention choice.
4. Check sensitive content, third-party license and external references; public GitHub is **not** the place for project-private media.
5. Delete only an exact, explicitly classified item after final revalidation of title, ID, parent and current content. Log the action, timestamp and exact result.

## Recorded actions in this phase

- **Published to GitHub candidate:** select release changelogs, V2.5 validation evidence, Drive inventory and 11-file equality/revision/metadata records.
- **Deleted in Drive:** only the folder named `_EMPTY_TMP_CREATED_DURING_BRANCH_SETUP`, verified empty immediately before deletion and absent on readback. No files or media were deleted.
- **NOT performed:** deleting `00_ACTIVE`, `90_ARCHIVE`, projects, release ZIPs, analysis or utility files.

## Engineering decision

Stop equating "Drive should primarily store media" with "delete all old documents today". Until the explicit preservation gate is met, the Drive contains historical-only sources. New AI Creative Skill design documentation must be created in GitHub, not duplicated into Drive. R1 research can proceed safely in parallel with any residual cold-archive decision.
