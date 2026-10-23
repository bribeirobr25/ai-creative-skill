# Revisão cruzada aplicada · Intelligence synthetic canary · 2026-10-23

**Status:** parte das observações implementada e testada; restantes pendentes. Tudo sintético, sem dados de terceiros, integração canônica, gastos ou novas permissões.  
**Origem:** revisão independente de Claude Code após os PRs #18 e #19 e plano de segurança do PR #20.  
**CI verificado:** 56 testes unitários offline concluídos em PR #19 no commit de código verificado. Os checks normativos existentes de V2.5/boundary são separados e não certificam integração.

## Resolução por achado

| Achado | Status | Mudança / evidência |
|---|---|---|
| Descrição do PR desatualizada | CORRIGIDO NA DESCRIÇÃO ATUAL | Atualizar arquivos/test count a partir do diff e CI; não presumir número pela narrativa antiga |
| NO_RESULTS versus INSUFFICIENT_EVIDENCE | CORRIGIDO NO EXPERIMENTO | Busca negativa pode encerrar a pergunta de existência somente com finalidade e escopo verificados explicitamente. Ranking sem itens permanece insuficiente. Fonte e trabalho possuem estados distintos |
| derived_permission booleano | CONFINADO AO EXPERIMENTO | Somente entradas SYNTHETIC_FIXTURE aceitas. Um Policy Gate real não foi implementado; bloqueio de uso em dados externos continua |
| Monte Carlo com duas fontes e probabilidades fixas | PENDENTE EXPANSÃO | 2.000 cenários sintéticos são teste de reprodutibilidade, não previsão nem stress completo. Quotas, latência, retry, custos, falhas correlacionadas extras seguem no plano |
| Duplicação do filtro de coorte do outlier | CORRIGIDO | Uma passada agrupa observações por publicação; uma publicação = uma unidade de baseline |
| Dois snapshots do mesmo vídeo geram falha | CORRIGIDO NA HIPÓTESE DO CANÁRIO | Escolha de medição com idade mais próxima, tie-break determinístico; inconsistência de identidade real continua bloqueante |
| limit verificado somente após catch | CORRIGIDO | Verificação type/interval no início; bool e limites inválidos são rejeitados |
| requested_national_top não atravessa o bridge | CORRIGIDO | Flag propagada ao cálculo; sem cobertura elegível, relatório devolve INSUFFICIENT_EVIDENCE e não transforma amostra em ranking nacional |
| Fonte OK mas conclusão insuficiente | CORRIGIDO | Dados ausentes e amostras heterogêneas não concluem pesquisa como COMPLETE automaticamente |
| Dados privados/publicação | PR #20 PROPOSTO, NÃO INTEGRADO | Gate e ADR-0003-PROPOSED com 23 testes de segurança, separado do canário e da main. Auditoria histórica completa ainda não foi executada |

## Itens ainda em aberto

1. Uma revisão mais profunda da seleção de snapshots (censura, intervalos, comparabilidade temporal, mudanças de identidade de canal e múltiplos formatos).
2. Contrato de elegibilidade estatística, amostragem não aleatória, distribuição com caudas longas, viés de busca e ranking cross-platform.
3. Monte Carlo além da sanidade matemática: limites de APIs, correlação de falhas, idempotência/retry, latência, custo, política de dados e falhas raras forçadas.
4. Gate de segurança privado e histórico de commits: scanner proposto não cobre retroativamente qualquer exposição.
5. Interface `research_execution` é uma fixture alinhada a **Markdown metodológico**, não um parser/schema canônico runtime instalado.
6. Política específica de YouTube ou outro fornecedor antes de qualquer uso de dados reais e métricas derivadas.

## Critério de progressão

O PR #19 permanece Draft. Nenhuma aprovação de release, acesso a YouTube, cobrança, produção, canon ou merge decorre de 56 testes sintéticos. Os aprendizados são reaproveitados sob a ADR-0003 **proposta**, com limites por capacidade e aceitação independente.
