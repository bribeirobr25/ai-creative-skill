# DQB-02 — Visual Direction Method Validation

**Piloto controlado executado: 2 briefings × 2 condições × 2 repetições = 8 execuções, cada uma com R0 e R1
(16 websites navegáveis). Revisão humana pendente: `AWAITING_HUMAN_REVIEW`.**

Pergunta: a candidata do PR #12 (`2cdc46b`) faz o mesmo agente produzir websites visualmente melhores na
primeira entrega do que a V2.5 (`39a0bfa`)?

Resumo da coordenação (exploratório, não cego): a candidata **foi seguida** (4/4 execuções B registraram
decisão de composição e tradeoff), **custou cerca de 33% mais tempo** no R0 e **não produziu diferença visual
mensurável**. As oito entregas convergiram para o mesmo sistema tipográfico e para estruturas de página
muito parecidas. Decisão formal: `INCONCLUSIVE`; inclinação: `REVISE CANDIDATE`.

> **Versão enxuta no `main`.** Esta cópia traz protocolo, relatórios, feedback, perfil de preferências, briefings,
> rubrica, registros dos executores, manifestos de hash, resultados JSON, ferramentas e as seis folhas comparativas
> (`validation/dqb02/results/comparisons/`). Ficam fora do `main` os 16 sites (HTML/CSS/JS), as 33 fotos do Wikimedia
> Commons (créditos e licenças em `shared/assets-*/credits.json`) e as 200 capturas de evidência, cerca de 51 MB.
> Esse material completo permanece no PR #13 (branch `research/dqb02-visual-direction`); as galerias e os comandos de
> reprodução abaixo funcionam a partir daquela branch.

## Começar aqui

- Revisores: [como receber e usar os pacotes cegos](entrega-revisores.md). **Não leia o resto antes de revisar.**
- [Protocolo congelado e regra de decisão](protocolo.md)
- [Relatório de decisão](relatorio-decisao.md)
- [Galeria R0](galeria-r0.html) e [galeria R1](galeria-r1.html) (condições reveladas)
- [Emendas e desvios](emendas.md)
- [Feedback do proprietário (não cego)](feedback-proprietario.md) e
  [perfil de preferências visuais v0.1](../preference-profiles/owner-web-visual-preferences-v0.1.md)
- Briefings: [B1 Miolo](../../../validation/dqb02/shared/briefing-b1-miolo.md) · [B2 Tábua](../../../validation/dqb02/shared/briefing-b2-tabua.md)
- Execuções, registros dos executores e hashes: `validation/dqb02/runs/`
- Evidência comum, convergência e esforço: `validation/dqb02/results/`
- Ferramentas: `validation/dqb02/tools/` (coletor de evidência, convergência, pacotes, restauração de assets)

## Reproduzir localmente

```bash
python3 validation/dqb02/tools/restore_assets.py        # repõe fotos/fontes e verifica hashes
python3 validation/dqb02/tools/check_site.py B1 validation/dqb02/runs/m13/r0 /tmp/out m13-r0
```

Sem gerações pagas, publicação, merge, release ou alteração da baseline V2.5. O CI de atestação da V2.5 falha
nesta linha de branches por design (a candidata altera um arquivo da fonte histórica) e não foi mascarado.
