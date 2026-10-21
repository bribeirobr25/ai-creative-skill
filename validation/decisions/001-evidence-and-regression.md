# Decision 001 — Preserve evidence without changing the runtime

Status: adopted for this validation branch, 2026-10-20.

The canonical source is release-attested and the assignment authorizes tests, reports and recommendations, not automatic runtime corrections. Keep all production files byte-identical; use isolated mutation copies and original synthetic fixtures. Reuse existing Python/unittest/CI instead of adding a second orchestrator or a hosted evaluation service.

A discovered failure cannot be marked PASS simply because it is known. Store failing IDs **and observed actual signatures** separately in `known_findings.json`. CI checks for unreviewed behavior changes and missing expected records. If a fix causes a known failure to pass, require reviewed baseline maintenance. Existing failures stay visible in JSON and the consolidated report. Green CI is not release approval.

Publish the harness implementation in one commit; generate evidence from that exact clean commit; add historical evidence in a subsequent commit. The later report commit does not pretend to be the code version that generated its own hash. CI artifacts report the actual checkout SHA and keep current evidence separate from historical evidence.

No calibration is invented for economic simulation. No agent behavior is inferred from fixture strings. No provider execution is inferred from a mock or unavailable adapter. Human acceptance remains unverified.

Rejected initial hypothesis: an empty `external_link_targets` list always invalidates `REAL_VERIFIED_LINK`. The synthetic page has a valid internal anchor; external targets are not required for that case. Replaced the proposed failure with a positive compatibility control. Broken real CTA behavior still requires browser interaction evidence and is not certified by this control.

Deferred: generic host adapter, independent prompt-injection/identity journeys, actual paid-provider reconciliation, Windows support and creative acceptance study. These are missing evidence, not automatically runtime defects or justification for replacing approved architecture. Existing PR #2 and PR #5 remain separate.

CI provenance follow-up: the first Linux run reproduced all outcomes, but its shallow checkout made `git log -- <source>` attribute source history to the checkout boundary. Keep full history in CI and report a null source-history commit for shallow local clones. Exact checkout SHA and content digest remain available. This corrects harness metadata, not a skill defect; the original local historical report used complete history and remains valid.
