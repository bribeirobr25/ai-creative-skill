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
- **Quality gate and measurements (NEW):** [media-reframe/r1-production-quality-gate-2026-10-20.md](./media-reframe/r1-production-quality-gate-2026-10-20.md)
- **Spatial + temporal reproducible benchmark:** [media-reframe/r1_quality_benchmark.py](./media-reframe/r1_quality_benchmark.py)
- **Persistent local synthetic measurements:** [media-reframe/r1-quality-observations-local-2026-10-20.json](./media-reframe/r1-quality-observations-local-2026-10-20.json)
- **Feature-branch quality CI with actual FFmpeg installation:** [.github/workflows/reframe-quality-r1.yml](../../.github/workflows/reframe-quality-r1.yml)

**Production boundary added 20/10:** Passing the deterministic geometry and video/audio smoke does not certify professional quality. Local resolution-loss tests (4K, 1080p, 720p, 480p to 1080×1920) found progressively worse image/microtext quality and verified copied decoded audio on a separate 24fps synthetic clip. The gate requires realistic rights-cleared examples + editorial/human assessment before any production acceptance. Only the research branch was updated; V2.5 source stays unchanged.

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
