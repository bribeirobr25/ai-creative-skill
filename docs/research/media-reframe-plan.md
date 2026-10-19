# Media Reframe · R1 research index

**Status:** R1 evidence collected and local synthetic tests executed on **2026-10-20**. **Research candidate only**: not new runtime capability, not V2.6, not commercial/clean-host QA, not a release.

## Scope and approvals

Study portable image/video cropping, intelligent composition, still-image outpainting, temporally coherent video expansion, editorial layout and actual integration interfaces. Preserve a single shared authority/router/contracts/QA system and independent bounded entry/exit under [ADR-0002](../decisions/ADR-0002-capability-bounded-invocation.md).

No paid inference, uploading customer images/video, media publication, canon change, merge, source V2.5 edits or release without appropriate authorization.

## Current R1 artifacts

- **Evidence matrix, shortlist, risks and contract proposal:** [media-reframe-evaluation-2026-10-20.md](./media-reframe-evaluation-2026-10-20.md)
- **Reproducer (research only, synthetic local assets):** [media-reframe/r1_offline_smoke.py](./media-reframe/r1_offline_smoke.py)
- **Observed execution evidence including hashes:** [media-reframe/r1-local-test-2026-10-20.json](./media-reframe/r1-local-test-2026-10-20.json)
- **CI research smoke test:** [tests/test_media_reframe_research.py](../../tests/test_media_reframe_research.py)

## Verified decision boundary, NOT an implementation approval

1. Portable baseline image: Pillow crop with protected-box feasibility check, fallback pad/layout.
2. Portable baseline video: FFmpeg crop/scale/pad, explicit audio mapping, geometric and metadata QA.
3. Future smart tier: manual ROIs/trajectories immediately viable; automated OpenCV detection/tracking and shot logic **not tested**.
4. Future image expand: local Diffusers or gated vendor adapters; no cloud executions made.
5. Future video expand: separate R&D, genuine temporal/source fidelity **unverified**. Do not substitute a generative video-to-video model or independent frame expansions and claim faithful original-preserving video canvas expansion.

## Next gates

- Review R1 shortlist and agree minimum functionality/QA with owner before new versioned runtime integration.
- Extend tests on explicitly authorized realistic multi-subject/face/product/logo/audio material; no public samples from Della/diBoaS.
- Quote/authorize cost and privacy separately if a remote outpainting benchmark is later requested.
- PR #2 remains DRAFT; separate PR #5 is **upscale**, not reframe.

**Evidence quality:** documentary source citations are linked inside the matrix; only local synthetic tests are `TESTED`. Vendors are primarily `DOCUMENTED` or `UNKNOWN` for actual reframe routes. No semantic perceptual approval was obtained.
