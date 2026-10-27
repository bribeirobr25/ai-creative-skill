# AI Creative Skill

**Status do `main`: 2.6.0-dev.** Linha de desenvolvimento sobre a baseline **V2.5.0**, atestada no commit
`39a0bfa39270ea4b685b0f862e7dbf647cf81d77`. Não é release, não tem certificação de qualidade de produção nem de host limpo.
Metadados do plugin: versão `0.3.0`.

A fonte em `src/ai-creative-skill/` corresponde à candidata ativa [web-runtime-2.6-v1](validation/candidates/web-runtime-2.6-v1/README.md),
que acumula o boundary hardening (preview, router, revision, validate, schema `0.2.1-candidate`) e as correções de runtime
observadas no DQB-02 (router com pedidos naturais, QA com evidência fora do site, rotas `#/`, 320 px, imagens lazy).
O builder original recusa essa fonte por design; a V2.5 continua verificável byte a byte pelo gate de integridade.

This is the public, provider-neutral source of the AI Creative Skill. The only canonical implementation tree is `src/ai-creative-skill/`. The Agent Skill and OpenAI Portable Plugin ZIPs are **generated artifacts**, not source trees that should be edited independently.

## Build & check

```bash
pip install -r validation/requirements.txt
python -m validation.release_integrity      # V2.5.0 exportada de 39a0bfa: testes, smoke e builders originais
python -m validation.candidate_integrity    # fonte atual = inventário revisado da candidata
python -m validation.candidate_tests        # testes de regressão e Web Experience da fonte atual
```

Uma nova mudança em `src/` exige uma nova candidata: escopo revisado em `CANDIDATE_SCOPES`, manifesto e
`validation/candidates/ACTIVE.json`. Candidatas anteriores e hashes históricos nunca são reescritos.
Runtime tests require optional local packages described in the source installation guide. No paid providers or GPU inference are called by repository CI.

## Governance

- `main`: 2.6.0-dev, integração validada por dois gates (integridade imutável da V2.5 e candidata).
- V2.5.0: commit `39a0bfa`, referência de release preservada.
- Pesquisas concluídas ficam em `docs/research/`; evidência pesada (sites, fotos, capturas) fica nas branches dos PRs fechados.
- Every capability belongs to the shared creative architecture **and** may run and finish independently at the user-requested boundary.
- Changes to canon, paid inference, publication and releases require separate authority.
- **PUBLIC repository:** only publish code, generic documentation and permitted examples. Never commit client media, user data, API keys or third-party weights.
- Distributed skill works without access to this GitHub repository or the owner's Google Drive.

## Repository

- `src/ai-creative-skill/`: canonical source (V2.5 plus the reviewed boundary-hardening candidate).
- `packaging/`: original plugin descriptor and deterministic two-format build.
- `docs/migration/`: hashes and provenance.
- `docs/decisions/`: architecture decisions (ADR-0001 source of truth, ADR-0002 bounded capability invocation).
- `docs/research/`: research records (creative quality, DQB-01, DQB-02, media reframe, video upscale, preference profiles).
- `assets/manifests/`: storage-neutral asset schema, no actual media.
- `.github/workflows/`: offline CI only.

Original ZIP releases and old snapshots remain preserved in Google Drive.

## Reusable validation

The [validation harness](validation/README.md) adds synthetic canonical-helper probes,
controlled fault/mutation tests, fictional journey definitions and illustrative cost
simulations. Read the [initial findings](validation/reports/2026-10-20-findings.md):
known defects remain explicit FAILs, and a green regression check is not production approval.
No paid provider calls, private assets or installed-skill changes are involved.
