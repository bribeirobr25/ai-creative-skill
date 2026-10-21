# DQB-01 — Redação pós-execução

Em 21/10/2026, um caminho local do host foi redigido em `shared/executor-common.md` (linha 9): o segmento
do nome de usuário foi substituído por `<HOST_USER>`, como já era feito nos registros dos executores.
Nenhuma outra alteração de conteúdo foi feita.

- SHA-256 congelado em `results/input-manifest.json` e `results/preflight-checks.json`:
  `1c81275ccc7e85e38d75925df928d4f2150807aac133a01e252074f751d9b1b6` (arquivo original, usado na execução).
- SHA-256 do arquivo redigido: `c581b331b3c8115c4b5cbc4683e93f7a72e2274b6dddf2d961ffb0253ad93b3b`.

A divergência entre os dois hashes é esperada e decorre só desta redação.
