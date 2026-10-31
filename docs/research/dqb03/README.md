# DQB-03 — Divergent Directions Method Validation

**Piloto com marcas reais: 2 marcas × 2 condições × 2 repetições = 8 execuções, cada uma com R0 e R1 (16 sites).
Revisão do proprietário pendente: `AWAITING_HUMAN_REVIEW`.**

Pergunta: pedir ao agente duas ou três direções contrastantes antes de escolher (B, `experiment/web-divergent-directions-v0-1`, guardada na tag `archive/web-divergent-directions-v0-1` desde 2026-10-31)
melhora e diversifica os sites em relação ao método atual (A, candidata `web-runtime-2.6-v1` do PR #17)?

Resumo exploratório: B foi seguido e não custou mais, mas quase não mudou o resultado. As alternativas se repetem entre
execuções e a direção escolhida é a mesma que A escolhe sem o passo (Fraunces no título em 8/8, mesma imagem de
abertura por marca em 4/4). Formal: `INCONCLUSIVE`; inclinação: não adotar B como está e testar a escolha de direção
pelo proprietário. O runtime do #17 se comportou bem nas 16 entregas reais.

- [Protocolo congelado](protocolo.md) · [Relatório de decisão](relatorio-decisao.md) · [Emendas](emendas.md)
- Briefing D2 diBoaS, instruções, rubrica e ferramentas: `validation/dqb03/shared/`, `validation/dqb03/tools/`
- Evidência comum (16 entregas), convergência, esforço e mapa de condições: `validation/dqb03/results/`
- Registros dos executores e hashes da diBoaS: `validation/dqb03/runs/`. As folhas comparativas (imagens) ficam fora do
  repositório, como no DQB-01/02 slim: o guard de publicação bloqueia binários adicionados.

**Privacidade:** a Della Berlin é uma marca real com material privado. O briefing D1, as fotos, os sites, as capturas,
as folhas comparativas e os registros dos executores da Della ficam fora deste repositório (só hashes aqui).
