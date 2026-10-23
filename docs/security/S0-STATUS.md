# S0 · Encerramento administrativo e riscos residuais · 2026-10-24

**Status:** `CLOSED_BY_OWNER_ATTESTATION_WITH_RESIDUAL_LIMITATIONS`.
**Authority:** declaração do proprietário de que imagens e vídeos sob sua responsabilidade foram produzidos por ele (IA ou captura própria) e textos são de sua autoria. A S0 foi encerrada por decisão expressa do proprietário, não por perícia integral de cada arquivo.

## Sanitized result

A auditoria automatizada anterior percorreu referências públicas alcançáveis e não identificou padrões conhecidos de credenciais bloqueantes nos textos examinados. Os candidatos de links foram classificados por formato/permissão atual conhecida, **não** por uma garantia de acesso histórico. A inspeção visual e de EXIF foi amostral, não certificação de direitos ou de ausência total de dados pessoais. Um endereço repetido de atribuição técnica de coautoria necessita classificação contextual; não tratar repetições como pessoas ou vazamentos diferentes.

**Atenção persistente:** uma referência estável a uma pasta Drive ainda existe em documentação e registry de mídia atualmente distribuídos em `src/`. São ocorrências de um recurso, e não demonstração de acesso público indevido. A substituição por IDs lógicos depende de candidate inventory/manifest versionado e coordenação com o PR #17, não de edição furtiva do release atual. Não reproduzir URL, ID ou endereço em relatório público.

## Policy for future changes

- S0 histórica **fechada**; abrir incidente direcionado apenas se aparecer evidência nova e concreta.
- Segredos e links assinados ativos: revogar/rotacionar na origem primeiro. Histórico/forks/caches exigem decisão separada.
- Antes de cada novo push/connector write, fazer preflight; CI é segunda barreira, não previne publicação inicial.
- Direitos de elementos de terceiros, licença de ferramenta IA, EXIF, metadados Git, ACLs passadas e objetos externos permanecem limites não certificados.
- Auditoria de todo o histórico é **manual/advisory**, separada do check obrigatório de diff/commits de um PR.
- ADR-0003 permanece proposta até aceite explícito. PR #20 Draft, sem merge/release.
