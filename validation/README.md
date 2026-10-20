# AI Creative Skill validation harness

Reusable, zero-provider-call probes against the **actual canonical Python helpers**. This is test infrastructure, not a second creative runtime. It does not install or change the skill, generate with AI, publish a site, or certify professional quality.

The initial assessment found six defect families across 16 failing cases. Read [the findings](reports/2026-10-20-findings.md) before interpreting a green CI run. See [methodology](methodology/design.md), [scenario register](scenarios/register.json), [economic assumptions](methodology/economics.md), and [baseline policy](decisions/001-evidence-and-regression.md).

## Reproduce

Python 3.11, FFmpeg/ffprobe and a Unix environment are required for the full baseline. Node is used by the existing Web suite. No model weights or provider credentials are needed. Dependencies are pinned in `requirements.txt`; install them in a disposable virtual environment. Package installation may use the network; the probes themselves use only files and a loopback preview server.

```sh
python3.11 -m venv .venv
.venv/bin/python -m pip install -r validation/requirements.txt
.venv/bin/python -m unittest discover -s tests -p 'test_*.py' -v
.venv/bin/python -m unittest discover -s src/ai-creative-skill/web/tests -p 'test_*.py' -v
.venv/bin/python -m validation.harness --host --check --output build/validation/current.json
.venv/bin/python src/ai-creative-skill/scripts/smoke_install.py
.venv/bin/python packaging/build.py --output-dir dist
```

Without `--host`, the harness omits preview process/network checks and real video encoding. It still executes actual image processing and mock fault injection. `--host` means these local integration probes are included; it **does not** mean an LLM/agent invocation was tested. Use `--host --check` for the complete acceptance baseline.

Outputs are a machine-readable report and a sibling `*-economics.json`. Every probe records expected/actual results, method, risk, input references and a reproduction entry. Environment and exact commit information apply to the whole report. The source tree hash is checked before/after probes. No generated media is retained in Git. Temporary fixtures and mutated copies are removed automatically.

## Interpretation

- `PASS`: the named, bounded assertion held in this execution.
- `FAIL`: the assertion did not hold. Known defects remain `FAIL` in every report.
- `BLOCKED`: required infrastructure was unavailable (for example, FFmpeg).
- `NOT_RUN`: a scenario is defined, but no execution evidence exists.
- `UNVERIFIED`: helper execution does not establish the broader quality or human acceptance claim.

`execution_performed: false` on journey records prevents a planned human/host evaluation mode from being mistaken for an actual review. `production_approval` is always `UNVERIFIED` in this version.

`--check` exits nonzero for an unexpected failure, a missing expected probe, changed known-failure evidence, a blocked dependency, or a previously failing test that now passes and needs baseline review. It exits zero when observed behavior matches the explicitly reviewed defect baseline. **This is a regression gate, not a release or production gate.** The final JSON includes both the defects and the gate result; no xfail is silently reported as a pass.

## Repository ownership

| Location | Responsibility |
|---|---|
| `src/ai-creative-skill/` | Unchanged canonical contracts/runtime; the system under test |
| `validation/harness.py`, `invariants.py` | Bounded probes and shared mutation/regression oracles |
| `validation/scenarios/register.json` | Risks, contracts, fixtures and deferred fictional journeys |
| `validation/fixtures/` | Original synthetic content; adversarial text is data, not instructions |
| `validation/generators/` | Deterministic small-domain pairwise generator |
| `validation/simulations/` | Illustrative economic model, isolated from actual execution |
| `validation/known_findings.json` | Explicit reviewed defect signatures and expected probe inventory |
| `tests/test_validation_harness.py` | Regression tests, oracle controls and simulation sanity checks |
| `.github/workflows/validate.yml` | Existing CI plus full probes and temporary JSON artifacts |
| `validation/reports/` | Immutable historical evidence and interpretation |

To add a capability, reference its existing contract, add a synthetic fixture and small probe, classify real versus mocked evidence, update the scenario register, and review the inventory delta. Never add an observed failure to the baseline merely to make CI green. Link a finding and exact evidence; corrections belong in separately authorized runtime work. Keep historical reports unchanged after subsequent fixes.

Initial source baseline: `main` at `39a0bfa39270ea4b685b0f862e7dbf647cf81d77`, skill V2.5.0 / plugin 0.3.0. PR [#2](https://github.com/bribeirobr25/ai-creative-skill/pull/2) (reframe) and [#5](https://github.com/bribeirobr25/ai-creative-skill/pull/5) (upscale research) remain independent. [Issue #1](https://github.com/bribeirobr25/ai-creative-skill/issues/1) supplies the independent-capability requirement. Neither research PR is treated as canonical implementation.
