> **ARQUIVO HISTÓRICO, NÃO CANÔNICO.** Documento preservado para rastreabilidade da pesquisa; seus estados, procedimentos, links e permissões não constituem instruções atuais. Consulte [STATUS v0.3](../STATUS.md), [arquitetura atual proposta](../architecture-v0.3.md) e [matriz de aceitação](../acceptance-v0.3.md). Nenhum acesso a provedores ou merge é autorizado por este documento.

# Correção de escopo de uso pessoal e política YouTube 2026 · 23/10/2026

**Estado:** ESCLARECIMENTO POSTERIOR À AUDITORIA · PROPOSTA DE CLASSIFICAÇÃO · NÃO CANÔNICO · SEM ACESSO APROVADO  
**Contexto:** o proprietário esclareceu que a AI Creative Skill e a camada Intelligence são de **uso próprio/pessoal**, não serão vendidas nem disponibilizadas como um serviço concorrente de vidIQ ou Orthogonal. O esclarecimento deve orientar a avaliação de produto, segurança, distribuição e contratos.

## 1. Correção necessária à auditoria anterior

A [auditoria forense](forensic-audit-2026-10-23.md) tratou de forma excessivamente restritiva a possibilidade de criar métricas e rankings com dados da YouTube API. A política básica de desenvolvedores impõe restrições relevantes, **mas existe uma política adicional publicada em 2026 para casos analíticos aprovados**. Portanto:

- A existência de uma API pública **não autoriza automaticamente** uma fórmula de outlier, métricas derivadas, histórico ou cópia de audiovisual.
- A ausência de comercialização da skill **não determina por si só** autorização para todas as operações da API. Os contratos e políticas continuam aplicáveis mesmo para um único usuário.
- **Não é correto classificar definitivamente a capacidade como proibida ou inviável.** O YouTube passou a prever, mediante auditoria/aprovação do caso de uso de Analytics & Reporting, cálculos adicionais, scores/ratios, comparações/leaderboards e armazenamento de certas estatísticas por até 36 meses.
- **Também não é correto tratar essa política adicional como uma autorização já obtida.** Elegibilidade e aprovação para este projeto não foram verificadas. Antes da aprovação, respeitar as regras gerais.

## 2. Evidência oficial atual verificada

1. YouTube [Developer Policies](https://developers.google.com/youtube/terms/developer-policies): políticas gerais de API data, armazenamento e métricas derivadas.
2. YouTube [Developer Policies Guide](https://developers.google.com/youtube/terms/developer-policies-guide), seção **Additional policies for derived metrics and data storage**, atualizada em 2026-09-14: aplicável apenas a desenvolvedores auditados que solicitaram e receberam aprovação explícita para caso analítico, por meio do pedido padrão de extensão de quota, desde 2026-06-01.
3. YouTube [Additional policies for derived metrics and data storage](https://developers.google.com/youtube/terms/derived-metrics-policy): entre os exemplos permitidos **sob a alteração aprovada**, aparecem scores/ratios de canais, dashboards/leaderboards, sentimento e identificação/categorização; dados estatísticos e métricas derivadas podem permanecer por até 36 meses, enquanto títulos/nomes/descrições/comentários continuam sujeitos a atualização/exclusão de 30 dias.
4. YouTube [Formulário de conformidade/extensão](https://support.google.com/youtube/contact/yt_api_form): caminho oficial para consulta/solicitação; condições exatas e resultado dependem da revisão do YouTube.

As referências acima descrevem **permissões condicionadas**, e não autorização pessoal concedida.

## 3. Como classificar o caso de uso de forma correta

Registrar como **`PRIVATE_SINGLE_OPERATOR_TOOL / NOT_OFFERED_FOR_SALE`**, rótulo *de requisitos de produto*, não enum jurídico nem categoria canônica da skill.

Distinguir claramente:
- **Uso pessoal de pesquisa/estudo sem distribuição**: operação interna de um único proprietário, sem oferecimento de produto/serviço.
- **Uso interno profissional/comercial eventual**: a mesma ferramenta pode subsidiar publicidade, conteúdos, análise de concorrentes e decisões de uma marca própria, mesmo sem ser vendida. Classificar por **finalidade da consulta concreta**, não pelo preço do software.
- **Redistribuição/oferta de software ou relatórios a terceiros**: não pretendida pelo proprietário, não ampliar escopo por inferência.

Não pressupor que se esteja atendendo a clientes externos, vendendo dados, monetizando um painel ou criando um produto SaaS. Também não inferir que toda consulta à API é automaticamente `NONCOMMERCIAL` apenas porque o software não está à venda.

## 4. Modificações no planejamento recomendadas (não implementadas)

| Item | Correção |
|---|---|
| P0 YouTube derived metrics | Mudar de “proibição absoluta” para **permissão conforme política geral, ou conforme aprovação analítica 2026 quando obtida**. Sem autorização especial, não executar usos reservados ao regime aprovado. |
| Escolha de fonte | Manter YouTube como **candidato viável condicionado**, não descartar a priori; explorar em paralelo datasets expressamente licenciados ou dados próprios quando cabível. |
| Modelos de performance | Desenvolver fórmulas e testar com **fixtures sintéticas/offline**, sem API real ou dados sujeitos a restrições até resolver autorização pertinente. |
| Dados históricos | Planejar retenção por classe de dados e regime de autorização. Até 36 meses **somente** quando aplicável a aprovação e categorias cobertas; 30 dias para demais campos referidos, conforme política. |
| Acesso/custo | Não presumir necessidade de assinatura vidIQ ou Orthogonal; tampouco presumir que acesso grátis cobre grandes volumes. |
| Gate 0 | Reclassificar o bloqueio principal como `AUTHORIZATION_AND_SCOPE_UNRESOLVED`, não “impossibilidade técnica/legal absoluta”. Manter implementação da rota restrita bloqueada até confirmação. |
| Arquitetura | Preservar um motor nativo sem MCP obrigatório, com Policy Gate por fonte, operação, finalidade, campo e transformação. |

## 5. Próximo gate adequado

1. Documentar o caso de uso **pessoal/single-operator** e separar eventual pesquisa que subsidie atividades de marca de pesquisa estritamente privada.
2. Verificar os termos gerais, os limites de uso no regime não aprovado e a elegibilidade/aprovação do **Analytics & Reporting** para o proprietário e a ferramenta.
3. Especificar `ALLOWED / CONDITIONAL_APPROVAL / UNKNOWN / BLOCKED` como classificações *propostas* por ação de API, sem criar enum canônico sem o Growth Rule.
4. Manter os 35 testes, testes adversariais e Monte Carlo; adicionar teste de **escopo/estado da aprovação analítica** e de aplicação correta de regras de 30 dias/36 meses.
5. Só após validação de direitos/escopo seguir para protótipo com as operações comprovadamente permitidas.

**Decisão deste adendo:** corrigir a premissa excessivamente ampla da auditoria; manter o PR #18 em Draft, sem declarar Gate 0 aprovado, sem liberar automaticamente a coleta/análise ou modificar `main`, `SKILL.md` ou fontes normativas.
