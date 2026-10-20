# DQB-01 research adapter and evidence

Bounded experimental scripts and inputs, not a new runtime/validation harness. Canonical skill, installed plugin and contracts remain untouched. Main base: `39a0bfa`; input freeze: `881ca0b`. No dependency on unmerged PRs #7/#9/#10.

See [decision report](../../docs/research/dqb01/relatorio-decisao.md), [gallery](../../docs/research/dqb01/galeria.html), [protocol](../../docs/research/dqb01/protocolo.md), [reviewer procedure](../../docs/research/dqb01/entrega-revisores.md), and [competitor preflight](../../docs/research/dqb01/higgsfield-preflight.md).

## Outputs and scope

- `runs/{A,B}/{r0,r1}`: four frozen HTML/CSS/JS sites and identical licensed assets.
- `results/r0-reviewed`, `results/r1-reviewed`: coordinator browser checks and same-size JPEG screenshots. Each round: 100 passes, zero failures, four additional homepage overflow smokes.
- `results/r0-A`, `results/r0-B`: first adapter outputs, including six whitespace false failures. Retained as historical runs; canonical results use normalized text over unchanged R0 files.
- `results/layout-r*.json`: measured boxes, not aesthetic scores.
- `results/delivery-integrity.json`: site hashes excluding executor diagnostics; original R0 manifests also preserve local diagnostics hashes.
- `results/executor-records`: executor self-reports, host paths normalized. References to raw QA folders remain historical/local; those folders are intentionally excluded from Git. Common coordinator QA and delivered site hashes are public/reproducible.
- `results/reviewer-packets.json`: original local ZIP receipt, **zero human responses**. ZIP container hashes can differ on regeneration due to metadata; site file hashes must match.
- `results/reviewer-packet-ui.json`: eight synthetic UI checks, never human feedback. Synthetic downloads discarded.

Photos are under Pexels License, not the repository code license. Credits/source URLs are in `shared/assets/credits.json`. Shared inputs, including the original host-specific Sites path, stay frozen; on another host, resolve an equivalent Sites version and document that execution-environment difference.

## Reproduce checks without paid services

Requires existing Python + Pillow and Node + Playwright/Chromium. Do not install/use paid generation services. Resolve the available runtime locally; configure `NODE_PATH` if Playwright is bundled outside normal Node resolution, and `CHROMIUM_EXECUTABLE` only when using a specific local browser binary.

From repository root:

```sh
python3 validation/dqb01/preflight.py
python3 -m http.server 8890 --bind 127.0.0.1 --directory validation/dqb01/runs
```

In another terminal, write reruns outside the preserved results:

```sh
node validation/dqb01/browser-checks.cjs http://127.0.0.1:8890 /tmp/dqb01-rerun-r0 A/r0 B/r0
node validation/dqb01/browser-checks.cjs http://127.0.0.1:8890 /tmp/dqb01-rerun-r1 A/r1 B/r1
node validation/dqb01/layout-metrics.cjs http://127.0.0.1:8890 /tmp/dqb01-layout-r1.json A/r1 B/r1
python3 validation/dqb01/package-review.py /tmp/dqb01-new-review-packets
node validation/dqb01/review-packet-checks.cjs /tmp/dqb01-new-review-packets /tmp/dqb01-packet-ui.json
```

The packet destination must not already contain the named packet directories. Each packet excludes executor `qa/` and `evidence/` folders, preserving all delivered site code and assets byte-for-byte. Keep the coordinator key separate from reviewers. Stop the local server after inspection. Opening the four site `index.html` files directly also worked in the tested Chromium; no deployment is needed.

Checks do not establish professional aesthetics, human usability, universal accessibility or native Higgsfield execution. Only a bounded keyboard activation is covered by the coordinator adapter; complete Tab sequences are executor self-QA. Scripts/screenshots use reduced motion and one desktop browser engine. No automated answer may be accepted as a genuine human review.
