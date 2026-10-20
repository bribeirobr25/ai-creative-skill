# Boundary hardening v1 — review candidate, not a release

This candidate continues `feature/validation-boundary-hardening` at the team's confirmed commit `f76fe65495bfe9e16b395e108d13677bd0ea2d05`, based on PR #6. It fixes F01–F06 without modifying the installed skill, historical V2.5 hashes, or PR #6. The candidate is intended for a draft PR targeting `feature/validation-harness`.

## Reproduce the two independent gates

Use Python 3.11 with `validation/requirements.txt`, Node and FFmpeg/ffprobe. All generated fixtures are synthetic; HTTP uses loopback. From the repository root:

```sh
python -m validation.release_integrity --output build/validation/release-integrity.json
python -m validation.candidate_integrity --output build/validation/candidate-integrity.json
python -m validation.candidate_tests
python -m validation.harness --profile candidate --host --check --output build/validation/candidate.json
```

**Release gate:** exports the pinned original release at `39a0bfa39270ea4b685b0f862e7dbf647cf81d77` to a temporary directory, then runs its unchanged 40 unit tests, installation smoke and both deterministic builders. It first compares the current historical attestation, manifest, builder, descriptor and original packaging tests to their committed bytes. The original PR #6 defect expectations and reports are also byte-checked. This is integrity/reproducibility evidence, not a claim that the original release's known defects were repaired.

**Candidate gate:** verifies the separately versioned [source inventory](source-manifest.json), the exact six changed source paths, positive/negative regressions, actual HTTP and isolated mutations. The original release builder still rejects this modified source as V2.5; a dedicated test requires that rejection. No V2.5 hash is regenerated and no candidate ZIP is mislabeled as a release.

`candidate_tests` owns all current repository tests except the unchanged `test_packaging.py`, which is executed by the separate required release gate. It also runs the existing Web suite unchanged. Plain `unittest discover -s tests` or the original V2.5 smoke/build commands against modified candidate source intentionally fail its old integrity assertion: use the two-gate commands above. Neither CI job may be waived for integration.

## Results and traceability

The executed candidate currently produces **308 PASS, 0 FAIL, 0 BLOCKED, 7 NOT_RUN, 2 UNVERIFIED**. All 16 original failing IDs now pass. The unchanged gaps still concern real agent journeys and human/creative acceptance. The candidate unittest suite has 59 passing tests; the separate original-release gate has 40 passing tests plus smoke/build checks.

The 153 additional harness records are adjacent controls and seven new isolated mutants (in addition to the original three). This is targeted sensitivity, not a global mutation score. The source-read race test independently swaps a directory for an outside-root symlink after its descriptor is opened and verifies the original allowed bytes are read.

See [remediation ledger](remediation.json), [candidate report](../../reports/2026-10-20-boundary-candidate.json), [release check](../../reports/2026-10-20-boundary-release.json), [verification checks](../../reports/2026-10-20-boundary-checks.json), and [consolidated findings](../../reports/2026-10-20-boundary-findings.md). Reports are generated from committed code; the later evidence commit preserves the exact tested commit in each record. Current CI artifacts remain separate from immutable historical reports.

The old `known_findings.json` is unchanged. The candidate [expectations](expectations.json) admits **no expected failures**. A deliberately failing original ID is independently checked to fail the candidate gate. Missing probes, blocked tools and unexpected symptoms still fail. Running the candidate with `--profile historical --check` intentionally reports the fixed historical failures as requiring review; it does not rewrite that baseline.

## Boundary decisions and limitations

### F01: preview scope and ownership

GET and HEAD share a single decode/authentication/file-serving implementation. Hidden/dot paths, ambiguous/double encodings, control characters, symlinks (including internal ones), directory listings and nonregular files are denied. Ordinary HTML/CSS/JS, encoded spaces, indexed directories and query-versioned assets remain accessible. Files are opened component-by-component with directory descriptors and `O_NOFOLLOW`, preventing a symlink swap between validation and opening. The health endpoint is reserved across encoded/query/trailing-slash aliases; only its exact ownership token in the header can retrieve metadata, with `Cache-Control: no-store`. A same-name file cannot bypass this endpoint.

Compatibility boundary: filenames containing literal percent signs and all symlinks are deliberately unsupported. Directory listing is replaced by index-only serving. No claim of Windows support is added: descriptor flags and the existing process lifecycle require Unix. The threat boundary is path/ownership isolation on loopback, not a sandbox against a malicious same-OS-user process, mounts, hard links or modification of an already-open file. No private files were accessed in testing.

### F02: scoped rights evidence

The candidate introduces an explicitly versioned **`0.2.1-candidate`** optional asset field, `publication_clearance`, in the existing Web schema. This is a narrow proposal for integration review, not release promotion. `0.2.0` preview records remain accepted unchanged, but cannot carry the new field silently. Publication preflight now requires a current review record bound to both the asset and evidence bytes, a nonblank reviewer, the exact intended use in `allowed_uses`, and satisfied applicable conditions. This applies to publication states even if the route is mislabeled preview.

`RESTRICTED` with permission for the requested use and satisfied conditions passes; `UNKNOWN`, private-only permissions, mismatched purposes, stale/missing evidence and unsatisfied conditions fail. `use_scope` stays a string to avoid replacing the existing contract; a full structured jurisdiction/channel/territory/expiry license model is deferred. The new scoped evidence object carries only the minimum needed for this gate. `commercial_publication` and `public_website` are distinct purposes; one does not imply the other.

**A matching file hash and reviewer string do not prove legal validity, reviewer identity or deployment permission.** The validator verifies the presence, compatibility and freshness of review evidence. Actual license interpretation and trustworthy review provenance remain host/human responsibilities. The separate deployment-authority gate stays intact. The team should explicitly review this schema proposal and adapters before accepting integration; older validators cannot consume new candidate records.

### F03/F04: preservation and dependencies

Protected changes or missing protected regions always dominate the aggregate verdict as FAIL. Dependency invalidation covers added/removed/modified scripts and styles, static JS imports, CSS imports/URLs, referenced assets, URL/attribute/order changes, inline code and document structure outside named regions. Cycles are bounded and the graph is capped. Unreferenced files do not trigger retests.

Dynamic imports/fetches, external content, inline JS resolution, embedded documents, base URLs and unresolved dependencies conservatively require browser inspection. This is a bounded static graph, not a complete JS/CSS interpreter. It does not certify browser behavior, visual equivalence, pixel preservation or content outside the named preservation contract. Unsupported constructs must not be promoted to a perceptual PASS.

### F05/F06: bounded interpretation and completeness

PT/EN negative requests, accent/case changes, publication instructions mentioned as research, and explicit route conflicts are covered. Contradictory or multi-operation requests return ambiguity instead of silently expanding scope or dropping work. An explicit route remains a routing hint and does not grant publication authority. This small deterministic pre-router is not a general language-understanding or prompt-injection certification.

Whitespace-only required strings are rejected, including Unicode whitespace; legitimate numeric zero, false and nonblank strings remain accepted under the existing shape contract. Structural success still reports semantic verification as false.

## Next integration gate

Review the security boundary and rights-schema proposal, require both candidate and historical CI jobs on the exact PR head, and review all 16 remediation mappings. Then run host/browser interaction and authority/provenance journeys against this candidate. Packaging/version promotion and installation require a later explicit release decision. No paid/provider testing or professional-quality certification follows from these results.
