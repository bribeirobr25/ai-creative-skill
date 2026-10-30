# V2.5.0 migration record

The original Agent Skill (74 files) and Portable Plugin (75 files) ZIPs **no longer exist**: the Drive copies were deleted by the owner's request (see [drive-cleanup-execution-2026-10-19.md](drive-cleanup-execution-2026-10-19.md); confirmed by the owner on 2026-10-30), and no GitHub Release was published. Their original SHA-256 list survives in [`docs/history/evidence/v2.5.0-original-zip-hashes.txt`](../history/evidence/v2.5.0-original-zip-hashes.txt). This import preserves the 74 shared core files, with SHA-256 manifest integrity and package provenance in `v2.5.0-source-attestation.json`.

The tagged import baseline is not a production certification. The recreated ZIPs may differ from original binary ZIP metadata, but their contents must match byte-for-byte. No historical Git commits are invented for V2.4 or earlier. The V2.5 packages can be rebuilt from commit `39a0bfa` with the original builders (`python -m validation.release_integrity`).

Import scan (2026-10-18, bounded and local): no common private-key headers, GitHub/OpenAI key signatures, emails or phone numbers were found in the 74 imported files, and no project audiovisual files, credentials or neural weights were included. This was not a legal or privacy clearance.

Before release promotion: verify source attestation, offline tests, target host behavior, review/rights gates and human approval. Public repository was authorized by the owner. Avoid secrets, personal materials and redistributed third-party media.
