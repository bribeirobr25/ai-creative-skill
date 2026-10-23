# Revisão cruzada planejada · PR #19 · 2026-10-23

**Estado:** CHECKLIST DE REVISÃO, NÃO EXECUTADO. O PR permanece experimental, sintético e Draft. A existência deste documento **não equivale** a bug corrigido, revisão aprovada nem certificação de host.  
**Referências:** [roadmap e Security Gate no PR #18](https://github.com/bribeirobr25/ai-creative-skill/blob/proposal/intelligence-architecture-pre-v0-1-20261023/docs/research/intelligence/revised-roadmap-security-gate-2026-10-23.md), métodos canônicos em `src/ai-creative-skill/references/`; PR #17 reservado à sessão de website.

## Ordem e critérios

| ID | Observação da revisão externa | Exigência e teste de aceite |
|---|---|---|
| CRV-01 | README/descrição do PR podem apontar a testes/arquivos antigos | Gerar inventário exato do diff e contar testes pelo CI mais recente; não confundir commits. |
| CRV-02 | `NO_RESULTS` → `INSUFFICIENT_EVIDENCE` pode ser inadequado para toda pergunta | Criar dois testes independentes: busca exaustiva vazia perguntando “existe?” pode ser COMPLETO quando a pesquisa foi concluída; ranking de “top vídeos” sem registros deve expressar insuficiência, não inventar top. `NO_RESULTS` pertence ao outcome da fonte, `status` ao entregável. Preservar limites de cobertura. |
| CRV-03 | `derived_permission` booleano passado pelo caller | Deixar explicitamente somente sintético; impedir uso com dados externos e jamais projetá-lo como autoridade futura. Real source policy gate pertence ao PR #18. |
| CRV-04 | Monte Carlo toy model tem expectativas analíticas fechadas | Teste estatístico simples apenas verifica PRNG/contagem. Adicionar distribuições de falhas comuns, quotas, retry/backoff e sample gaps em **novo experimento explicitamente hipotético**, após definir invariantes. |
| CRV-05 | Filtro de coorte duplicado no `outlier_ratio` | Consolidar única seleção de observações e `selected_ids`; preservar comportamento e regressões atuais. |
| CRV-06 | Mesmo vídeo do baseline em dois instantes gera erro | Implementar política versionada de seleção única de snapshot por vídeo, age-match determinístico, tie-break e decisão quando não houver janela adequada; não inflar `baseline_n`. |
| CRV-07 | `limit` validado tarde no bridge | Validar nos primeiros passos antes de qualquer ranking/exception handling; teste negativo para `0`, valores negativos, `bool`, `NaN` e tipo incompatível quando apropriado. |
| CRV-08 | Flag de national top não propagada pelo bridge | Propagar parâmetro tipado; quando não há cobertura populacional verificada, não produzir relatório com `top nacional`; teste de ponta a ponta. |
| CRV-09 | Fonte OK com dados faltantes e resultado insuficiente | Asserção de que `OK` de fonte não significa `COMPLETE` de pesquisa; complementar com dataset com métricas ausentes e fontes heterogêneas. |
| CRV-10 | Publicação de material sensível nos futuros PRs | Executar pré-checagem de conteúdo **antes** de enviar ao GitHub; só fixtures fictícias. Gate global descrito no PR #18 não está instalado neste PR. |

## Não interferência

- Não modificar `src/`, `SKILL.md`, `main`, `validation/` nem PR #17 por causa desse checklist.
- A execução dos 46 testes anteriores foi evidência válida daquele commit; novos commits exigem nova verificação. Não converter CHECKLIST em `PASS`.
- Não usar dados do YouTube/Meta ou claims de autorização para reproduzir análises com material real.
- Não criar segundo `RESEARCH_ONLY`, `source_outcomes`, budget ledger ou owner de evidência.
- Ao publicar code fixes, registrar correção, teste específico, regressão e efeito sobre a baseline.

## Sequência de aceite

1. Auditoria inicial de exposição e controle pré-publicação (PR #18/security gate).
2. Ajustes CRV-01..CRV-09 com testes negativos e de ponta a ponta.
3. Verificação CI em HEAD da branch + inspeção de diff/segredos antes de cada publicação.
4. Avaliação de compatibilidade com a arquitetura, sem dar merge na skill canônica enquanto Gate 0 não for aceito.

**Status geral: REVIEW PENDING.**
