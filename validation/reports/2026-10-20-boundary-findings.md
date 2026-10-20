# Boundary hardening — corrected candidate evidence

The six confirmed defect families are corrected in the candidate source. The original 16 failing IDs now pass, with positive, negative and adjacent controls. The full candidate harness reports **308 PASS, 0 FAIL, 0 BLOCKED, 7 NOT_RUN, 2 UNVERIFIED**; the 59 candidate unittest tests pass. The separate pinned-release gate passes its original 40 tests, smoke and both builders. These are bounded technical results, not commercial or human-quality certification.

The work continues the team's existing corrections, rather than replacing PR #6 or repeating migration/media research. [Candidate methodology and compatibility decisions](../candidates/boundary-hardening-v1/README.md) describe the complete reproduction commands and residual limitations. [The remediation ledger](../candidates/boundary-hardening-v1/remediation.json) maps every original FAIL to its correction, test IDs, prior commits and verified implementation commit. [The original report](2026-10-20-findings.md) remains unchanged.

| Family | Correction beyond the preliminary branch | Current bounded evidence |
|---|---|---|
| F01 | One GET/HEAD path policy; authenticated reserved health aliases; no-follow directory-descriptor opens; index-only directories; nonregular-file rejection | Original two failures pass; 86 HTTP controls cover prohibited and legitimate requests. Independent directory-swap test passes. Deliberately removed no-follow and health-auth checks are detected. |
| F02 | Asset/evidence-bound, use-compatible review evidence; candidate schema version; publication-state bypass protection | Original two failures pass; allowed restricted use and legacy preview pass, while incompatible purposes/conditions and stale or missing proof fail. Review-record validity is structural, not legal certification. |
| F03 | Protected failures/missing regions dominate CSS/JS partial status | Original combined-change failure passes; protected deletion and combined dependency changes fail as intended. A mutant weakening the aggregate verdict is detected. |
| F04 | Referenced dependency graph and document-shell invalidation, including transitive imports and assets; unrelated files ignored | Original newly linked script case passes; scripts/styles/imports/assets/query/attribute/layout changes invalidate; unchanged/unlinked controls do not. Dependency suppression mutant is detected. |
| F05 | Negation/conflict handling and bounded informational versus execution intent | Four original failures pass; mixed/contradictory requests block as ambiguous, allowed publication keeps its authority gate. Negation-removal mutant is detected. |
| F06 | Required-string whitespace detection without truthiness-based rejection | Six original failures pass; zero/false remain structurally accepted. Unicode-whitespace regression and a whitespace-check mutant are detected. |

The first local HTTP run exposed a **test expectation issue**, not a runtime defect: macOS resolves `/var` temporary paths to `/private/var`. The owner-response test now compares resolved roots, matching the lifecycle's canonical identity. Both token contents and authenticated health behavior remain checked. No failure was waived to accommodate this.

The original release builder is unchanged and deliberately refuses to label the modified candidate as V2.5. CI now has separate mandatory jobs for immutable release integrity and candidate correctness. Historical reports/known-failure expectations are byte-compared against PR #6's committed evidence; candidate expectations contain no accepted failures. A missing/reintroduced original defect fails the candidate gate.

Residual integration questions are explicit: approval of the narrow `publication_clearance` schema proposal; trusted review provenance and license interpretation; browser/agent end-to-end behavior; static dependency-analysis limits; and Unix-only preview lifecycle. All seven previously unexecuted journeys and both unverified acceptance records retain their status. No claim of Windows, legal, perceptual or commercial certification is made.

Recommendation: approve this candidate only for **integration review** after exact-head CI and schema/security review. Keep release promotion and installation separate. No merge, paid inference, private media publication or project-canon change is included.

## Original-ID remediation index

Each current PASS is recorded in the candidate report; historical FAIL records are unchanged.

| Original ID | Family | Candidate result |
|---|---|---|
| `ROUTE-research_negated_publish` | F05 | PASS |
| `ROUTE-research_negated_publish_en` | F05 | PASS |
| `ROUTE-research_domain` | F05 | PASS |
| `ROUTE-preview_negated_publish` | F05 | PASS |
| `WEB-rights-UNKNOWN-PROVISIONAL` | F02 | PASS |
| `WEB-rights-RESTRICTED-APPROVED_FOR_THIS_USE` | F02 | PASS |
| `PRESERVE-protected-plus-css` | F03 | PASS |
| `PRESERVE-new-script` | F04 | PASS |
| `SHAPE-whitespace-CHARACTER_BIBLE` | F06 | PASS |
| `SHAPE-whitespace-CONTENT_IDEA` | F06 | PASS |
| `SHAPE-whitespace-STORYBOARD_PLAN` | F06 | PASS |
| `SHAPE-whitespace-VIDEO_CREATIVE_DIRECTION` | F06 | PASS |
| `SHAPE-whitespace-REFERENCE_MANIFEST` | F06 | PASS |
| `SHAPE-whitespace-PROJECT_NEXT_ACTION` | F06 | PASS |
| `PREVIEW-encoded-hidden` | F01 | PASS |
| `PREVIEW-symlink-escape` | F01 | PASS |
