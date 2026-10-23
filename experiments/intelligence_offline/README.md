# Intelligence offline canary · experimento isolado

**Estado:** EXPERIÊNCIA TÉCNICA EM BRANCH SEPARADA · NÃO CANÔNICA · SEM DADOS REAIS · SEM AUTORIZAÇÃO PARA RELEASE  
**Base:** `main` `fb7f794ca2c51c2752afde5f907bd2866c9d1f25`.  
**Ligação de pesquisa:** [PR #18](https://github.com/bribeirobr25/ai-creative-skill/pull/18), ainda Draft/Gate 0 pendente.

Este experimento testa **apenas lógica matemático-estatística e invariantes sobre dados artificiais**. Não usa a YouTube Data API, Meta, TikTok, vidIQ, Orthogonal, web scraping, APIs, credenciais, dados pessoais, imagens, vídeo, armazenamento persistente ou modelos de IA. Também não é parte do runtime da skill em `src/ai-creative-skill/`.

## S1 concluída: revisão técnica offline

A [revisão S1 consolidada](S1-technical-review-2026-10-23.md) documenta a correção de inconsistências de cobertura nacional, resultados com contagem de views desconhecida, colidência de IDs de evidência, identidade contraditória entre snapshots, comparações de formato e entrada estatística inválida. **68/68 testes sintéticos PASS** no [job do commit `5efb2ebe`](https://github.com/bribeirobr25/ai-creative-skill/actions/runs/40017781052/job/120634192975). S1 está encerrada **somente quanto à revisão técnica offline**. PR #19 continua Draft, e a cobertura de provedores/licenças, contrato executável e integrações permanecem pendentes.

A S0 de mídia/textos foi encerrada administrativamente por declaração do proprietário no PR #20. O guard ainda não foi promovido à `main` ou instalado como proteção pré-push obrigatória.

## Revisão cruzada antes de expandir

O [checklist de revisão](cross-review-checklist-2026-10-23.md) registra dez pontos trazidos pelo Claude Code e pelo planejamento de segurança: semântica de resultado vazio, snapshots, parâmetro de limite, ranking nacional, deduplicação e Monte Carlo. Esse checklist é o registro **histórico**: os reparos verificados na S1 constam no relatório acima; tarefas de integração, política e Monte Carlo operacional permanecem pendentes. A nova regra de **pré-publicação sem segredos** está detalhada no [roadmap do PR #18](https://github.com/bribeirobr25/ai-creative-skill/blob/proposal/intelligence-architecture-pre-v0-1-20261023/docs/research/intelligence/revised-roadmap-security-gate-2026-10-23.md) e ainda precisa de implementação técnica.

## Atualização: adaptador experimental de pesquisa

- `research_bridge.py`: converte fixtures sintéticas em um *envelope lógico* compatível com os campos documentados por `RESEARCH_EVIDENCE_SYNTHESIS`: `research_execution_id`, `query_plan`, `source_outcomes`, `coverage`, `evidence_clusters`, `counterevidence`, `freshness_verdicts`, `status` e `unknowns`. Métricas e ranking permanecem em extensão `intelligence`, com ligações por `evidence_id`.
- `test_research_bridge.py`: verifica estados de fonte `OK`, `NO_RESULTS`, `RATE_LIMITED`, `AUTH_FAILED`, vínculo de evidência, datas, métricas ausentes e não comparabilidade.
- **Importante:** o contrato de pesquisa atualmente é uma especificação em Markdown, **não um schema executável em produção**. A correspondência é a uma *fixture de pesquisa*, não a um runtime canônico implementado. Não persistimos resultados, não acessamos APIs e não autorizamos uso de dados reais.
- Uma fonte `OK` pode produzir pesquisa `PARTIAL` ou `INSUFFICIENT_EVIDENCE` quando faltam métricas para a pergunta. Um resultado de API não é automaticamente uma pesquisa completa.

## O que existe

- `engine.py`: entidades sintéticas, verificação de fonte, deduplicação por plataforma/publicação/instante, cálculo de outlier relativo à idade e baseline comparável, velocidade entre dois snapshots, classificação por contagem bruta de views da amostra, simulação offline de falha comum/correlacionada em dois conectores fictícios.
- `test_engine.py`: invariantes de entrada, permissão explícita para calcular métricas derivadas **somente com fixtures sintéticas**, dados ausentes, IDs, contadores negativos, tempos, duplicatas, baseline insuficiente, empates, ranking nacional não demonstrado e reprodutibilidade de simulação.
- `.github/workflows/intelligence-offline-experiment.yml` (na branch experimental): executar os testes sem dependências externas em PR.

## Executar localmente

```sh
python -m unittest discover -s experiments/intelligence_offline -p 'test_*.py' -v
python experiments/intelligence_offline/engine.py
```

Python 3.11+. Sem dependências adicionais. A segunda linha emite uma simulação sintética com seed fixa, retornando contagens de `COMPLETE/PARTIAL/BLOCKED` sob hipóteses **inventadas para teste**, nunca taxas observadas de plataformas.

## Invariantes e limitações

1. `source_kind != SYNTHETIC_FIXTURE` é recusado. O flag `derived_permission` apenas habilita testes matemáticos com dados fictícios; **não concede licença real**. O runtime real futuro deverá consultar política de operação e de finalidade de fonte antes de calcular.
2. Mesmo conteúdo com IDs de publicação distintos **não é deduplicado como mesma publicação**. Um mesmo ID/momento com atributos conflitantes falha. Um mesmo vídeo de baseline em dois momentos não conta como dois vídeos.
3. Outlier só para mesmo canal/plataforma/formato e vídeo de idade comparável; mínimo 3 exemplos; median zero/sem evidência retorna `InsufficientEvidence`. Não extrapola outlier de dataset para país.
4. Views por hora são diferença observada em horas, não total/idade; contadores em queda não viram crescimento positivo.
5. Ranking por `RAW_VIEW_COUNT` mantém explicitamente `OBSERVED_SAMPLE_ONLY` se população não foi verificada. `Top N nacional` sem cobertura é rejeitado.
6. Monte Carlo offline ilustra efeitos de indisponibilidade comum (correlação entre fontes). Não testa APIs, retries reais, limites de cota ou resiliência de host em produção; não estima confiabilidade real.
7. Não há implementação de `research_execution`, Evidence Record canônico, aprovação, Budget Ledger, registro de fontes, CLI de produção, storage, API, MCP, pesquisa semântica ou workflow criativo. Não interpretar o experimento como substituto dos contratos existentes.
8. Não armazenar saídas reais do provedor nesta branch. Não fazer merge como parte da skill sem revisão de Gate 0, permissões e validações adequadas.

## Gate de licenças e política YouTube

O [guia oficial](https://developers.google.com/youtube/terms/developer-policies-guide) descreve algumas operações e métricas simples permitidas sob políticas gerais, enquanto [a política adicional](https://developers.google.com/youtube/terms/derived-metrics-policy) permite scores e leaderboards sob alteração/aceite para caso analítico aprovado. Não presumir que uso pessoal da skill equivale à aprovação formal. [Quota oficial](https://developers.google.com/youtube/data/determine_quota_cost) e condições de armazenamento precisam ser verificadas **no momento do primeiro teste de integração com API real**.

**Estado de testes:** este README não afirma PASS. Consultar o CI do PR experimental. Não há chamadas externas.
