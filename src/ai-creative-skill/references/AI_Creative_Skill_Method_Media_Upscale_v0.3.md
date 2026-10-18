# MEDIA_UPSCALE · Specialist Method v0.3

**Operation:** use `IMAGE_UPSCALE` for still images and `VIDEO_UPSCALE` for video from any source, without conditioning the task on Higgsfield, fal.ai, Runway, or a specific subscription. The provider is an optional execution route, not a creative owner.

## Intake & route selection

Preserve original/hash, rights, source dimensions/FPS/timebase/audio, project/face/product references, user target resolution (1080p, 2K, 4K, 8K or custom), desired fidelity, output format and budget. Output dimensions are **route-specific**, not a global 1080p/4K cap. Preserve aspect ratio unless explicit crop/pad authority. No silent FPS interpolation.

Use capability registry to discover `DOCUMENTED` vs `AVAILABLE` vs `EXECUTED`. Quote route-specific dimensions, model limits, estimated incremental cash, subscription credit opportunity cost and unmeasured local compute; approve cost/transfer before submission. Do not promote a mock route, unconfigured API, or absent checkpoint to executable. DO NOT submit paid requests from this package.

`local.pillow.lanczos.image.v0.2`: conventional interpolation, not super-resolution. `local.ffmpeg.lanczos.video.v0.2`: conventional, 24fps/audio/temporal checks. `local.realesrgan.srvgg.image.v0.2` / `local.realesrgan.srvgg.video.v0.3`: neural **experimental** when compatible optional dependencies and verified checkpoint exist; per-frame SR does not guarantee temporal fidelity. Conservative blend 35% neural / 65% Lanczos is an experiment only, not production default. The other routes in the registry are mocks, not real remote adapters.

## Execute & QA

1. Use `scripts/creative_media.py routes` to check reality on THIS host; do not infer resources from another Work environment.
2. Use `quote` and obtain appropriate input, budget and provider-transfer authority; include device selection. For examples see `media/README_v0.3_PTBR.md`. Python tools are best-effort; without suitable host, return `BLOCKED_PROVIDER_UNAVAILABLE` or conventional choice, never fake neural result.
3. Run only explicit eligible route; preserve source. Enforce idempotency and UNKNOWN reconciliation; retrieve same job rather than submit again after download failure. Protect provider credentials and user images.
4. Technical QA: dimensions, pixel aspect, aspect ratio, FPS/frame count/duration, timecodes, audio PCM/hash, codec/decoding, output hash, continuity and temporal artifacts.
5. Human fidelity QA **separately**: faces, skin, eyes, hair; product form, logo, labels, typography, textile and color, background; compare to real authorized references. Upscaled text that looks clearer but is wrong **fails** brand authenticity. No guaranteed gain or universal best model.
6. Mark result `TECHNICAL_QA_PASS` separately from `FIDELITY_PASS`. For unresolved skin/label, quality `PARTIAL` and `INTERNAL_PREVIEW_ONLY`; do not publish as commercial master.

## Known execution evidence and limits

A separate Work pilot ran Real-ESRGAN on Apple M1/MPS for 5s 480x854→1080x1922 (120f/24fps) with audio preserved, but skin and small label fidelity remained partial. In this portable package, a CPU test validated 0.5s 96x170→192x340, not full-HD production. Image neural tests on product/face/storyboard were small and editorially unverified. Commercial Higgsfield output looks sharper in selected Della comparisons, but exact provider/model variant and genuine label fidelity remain unverified. No neural 4K run proven.

`media/models/README.md` describes **optional checkpoints**, not bundled by default. Requirements: Pillow/NumPy for images, FFmpeg for video, Torch for neural. Host may not permit installation or GPU. License requirements and compute cost are distinct from per-provider fees. Never assert that every host is able to run neural upscale for free.
