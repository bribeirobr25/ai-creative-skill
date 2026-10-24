> **ARQUIVO HISTÓRICO, NÃO CANÔNICO.** Documento preservado para rastreabilidade da pesquisa; seus estados, procedimentos, links e permissões não constituem instruções atuais. Consulte [STATUS v0.3](../STATUS.md), [arquitetura atual proposta](../architecture-v0.3.md) e [matriz de aceitação](../acceptance-v0.3.md). Nenhum acesso a provedores ou merge é autorizado por este documento.

# YouTube · Matriz de permissão por operação · Revisão de fontes 2026-10-23

**Estado:** VERIFICAÇÃO DOCUMENTAL DE POLÍTICA PÚBLICA · NÃO É LICENÇA / NÃO É APROVAÇÃO DA API / NÃO É CONSULTORIA JURÍDICA.  
**Caso de uso informado:** ferramenta própria, single operator, não comercializada; as pesquisas podem ter finalidade pessoal ou eventualmente informar projetos criativos de marca. Não presumir venda da skill ou distribuição de produto SaaS.  
**Versão das fontes:** página de política adicional atualizada em 2026-09-14; quota em 2026-10-15. Verificar alterações antes de uma futura integração real.

## 1. O que a documentação oficial confirma

- [Guia geral de conformidade](https://developers.google.com/youtube/terms/developer-policies-guide): descreve uso permitido de métricas já disponibilizadas e exemplos de cálculos simples, além de advertir contra custom scores e rankings que não estejam no regime autorizado.
- [Política adicional de métricas derivadas e armazenamento](https://developers.google.com/youtube/terms/derived-metrics-policy): aprova **certas categorias** de scores, ratios, leaderboards, comparações históricas, classificação e análise sob emenda e aceite para Analytics & Reporting. O documento exemplifica "Creator Influence Score", leaderboard por crescimento e séries de 36 meses; a permissão não é inerente a qualquer chave.
- [Guia oficial, seção Additional policies](https://developers.google.com/youtube/terms/developer-policies-guide#additional_policies_for_derived_metrics_and_data_storage): ressalva que se aplica **apenas a desenvolvedores auditados e expressamente aprovados**, via processo padrão a partir de 2026-06-01.
- [Developer Policies](https://developers.google.com/youtube/terms/developer-policies): deveres gerais de retenção, dados não autorizados e direitos de audiovisual também valem para a ferramenta interna.
- [Quota Calculator](https://developers.google.com/youtube/data/determine_quota_cost): default de **100 chamadas/dia `search.list`**, quota separada de 10.000 units/day para outras operações, ressalvados limites e uso efetivo da conta. Cada página de busca consome chamada.

## 2. Policy matrix inicial (documental, não status de autorização do usuário)

| Operação proposta | Regime geral não aprovado | Regime analítico adicional aprovado | Implementação atual |
|---|---|---|---|
| Pesquisar e mostrar IDs, títulos/links e contadores fornecidos pela API | Potencialmente elegível conforme termos e finalidade; respeitar apresentação, atualização e atribuição | Também sujeito aos termos correspondentes | NÃO EXISTE |
| Ordenação por valor nativo declarado (`viewCount`) / visualização de métricas básicas | Guia geral lista ordenações/visões simples como exemplos aceitáveis, sem transformar em score proprietário | Elegível se aprovado; manter proveniência | NÃO EXISTE |
| Gerar `OUTLIER_RATIO`, scores próprios comparativos e leaderboards de canais | **Não presumir permitido**. Restrição de derived scores sem aprovação adicional | A política adicional prevê exemplos de métricas/leaderboards mediante aceite aprovado | SÓ COM DADOS SINTÉTICOS |
| Agrupar estatísticas de diversos canais, histórica e longitudinalmente | Restrito; política geral não constitui licença de agregação ampla | Pode ser permitido sob condições da emenda e do escopo aprovado | NÃO EXISTE |
| Persistir estatísticas de terceiros por mais de 30 dias | Não assumir; regra geral de `Non-Authorized Data` com refresh/deleção aplicável | Estatísticas e métricas derivadas elegíveis podem ter prazo de até 36 meses; outros metadados (nome/título/descrição/comentário) continuam sob 30 dias | NÃO EXISTE |
| Baixar, armazenar ou analisar localmente áudio/vídeo protegido | Não autorizado por acesso à Data API isoladamente | A emenda de métricas não concede licença de mídia audiovisual | NÃO EXISTE |
| Inferir país real da audiência por localização da busca ou origem do canal | Não fundamentado pela API pública | Também exige campo apropriado/escopo real de acesso | NÃO EXISTE |
| Pesquisa em apoio a decisões de marca, sem vender a ferramenta | Finalidade deve ser declarada e permanecer nos termos | Pode existir uso analítico aprovado; não assumir "pessoal = aprovado" | NÃO EXISTE |

## 3. Decisão prática sobre as próximas atividades

1. **Livre para desenvolvimento sem API:** testar métodos estatísticos próprios com fixtures sintéticas ou dados próprios/licenciados expressamente para derivação. O PR #19 usa somente `SYNTHETIC_FIXTURE`.
2. **Antes de chamar a API:** identificar credencial/projeto/escopos, termos aceitos, política aplicável, finalidade exata e acesso real. Não usar chaves de projetos aleatórios, nem contornar políticas via outra origem.
3. **Antes de derived analytics com YouTube data:** demonstrar a autorização analítica adicional ou restringir o produto à apresentação/uso geral permitido.
4. **Antes de armazenar:** autorização de retenção por classe de dado, prazo, delete, revogação, refresh, derivados/logs e atualização.
5. **Antes de ampliar escala:** medir a quota real, cobertura, custo operacional e incerteza do universo observado.

## 4. Correções ao roadmap

O primeiro gate operacional passa a ser **`SOURCE_PERMISSION_PREFLIGHT`**, não "YouTube outlier API integration". Não cancelar YouTube como possível fonte, mas separar analytics em sandbox sintética de consulta/armazenamento de dados reais. É possível experimentar a API apenas nas operações demonstravelmente permitidas, sob credencial própria e com observância dos termos aplicáveis.

As alternativas de fontes licenciadas, dados fornecidos voluntariamente e owner-authorized channels continuam possíveis, mas seus próprios contratos também exigem revisão; um revendedor não pode magicamente sublicenciar direitos que não possui.

**Estado:** `DOCUMENTED_ONLY / NOT_APPROVED / NO_API_CALL`; documento de pesquisa, sem alteração em source skill/runtime.
