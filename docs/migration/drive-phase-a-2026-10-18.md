# Drive inventory and document migration · Phase A

**Date:** 2026-10-18

**Scope:** Google Drive `influencer/` source workspace; **not** the Della or diBoaS project drives, and not all of Google Drive.

## First-level inventory snapshot

The `influencer/` root contains 16 subfolders. Their immediate contents total **434 entries** in the connector's initial folder listings. Counts describe **immediate children only**; deeper subfolders and some archive pages are **not yet fully certified**.

| Area | Direct entries | Decision |
|---|---:|---|
| `00_ACTIVE` | 31 Markdown files | Compare against GitHub source references; do not delete until exact coverage verified |
| `01_V2` | 33 | Historical source candidate; retain pending coverage |
| `02_V2.1` | 33 | Historical source candidate; retain pending coverage |
| `03_V2.2` | 33 | Historical source candidate; retain pending coverage |
| `04_V2.2.1` (folder A) | 33 | Conflicting historical candidate; retain |
| `04_V2.2.1` (folder B) | 34 | Conflicting historical candidate; retain |
| `05_V2.3` | 13 | Contains nested historical sources/tests; retain |
| `06_V2.4` | 6 | Contains historical sources and nested validation; retain |
| `07_V2.5` | 7 | Release ZIPs, hashes, tests and release metadata; **retain rollback** |
| `90_ARCHIVE` | 100 shown | Historical versions; needs complete, potentially paginated validation |
| `analysis` | 52 | External research, reports and subfolders; selectively review |
| `utils` | 46 | Vendor/source bundles, PDF and ZIP; do not publish wholesale |
| `skill-real-test-1` | 11 | Pilot media/characters/continuity: **out of scope** |
| `releases` | 2 | Two legacy release candidate folders; retain |
| `30_INBOX` | 0 | Empty, candidate for later cleanup |
| Temporary setup folder | 0 | Empty, candidate for later cleanup |

## Completed

- Canonical V2.5 files imported into `src/ai-creative-skill/` and verified by CI in earlier migration.
- Selected historical release-change records copied to `docs/history/`, preserving both nonidentical V2.2.1 variants.
- Pilot project assets not imported into public GitHub.

## Pending before destructive cleanup

1. Exhaustive recursive Drive inventory and ownership/permissions check.
2. Byte/hash equality or explicit transformed-copy provenance for each removal candidate.
3. Check unique architecture research, calibration, evidence and pilot-specific privacy.
4. Preserve rollback ZIPs, evidence that may be required for claims and original historical sources when uniqueness remains unresolved.
5. Prepare a per-file deletion list after migration readback; never treat same-name files as duplicates.

**Deletion status: ZERO files deleted.** No promotion, publication of client assets, or change to installed V2.5.
