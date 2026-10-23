# YouTube Analytics & Reporting · Processo de autorização e evidências · 2026-10-23

**Tipo:** checklist de pesquisa baseada em documentação oficial; NÃO é solicitação enviada, aceite, licença concedida ou extensão de quota.  
**Finalidade informada:** AI Creative Skill como ferramenta privada para um único operador, sem venda nem distribuição. Cada uso de dados (pesquisa pessoal, planejamento de conteúdo ou decisão relacionada à marca) deve ser descrito fielmente. Não afirmar uso exclusivamente sem fins comerciais se houver decisões comerciais reais.  
**Proibição operacional até aprovação:** não usar dados YouTube API para scores derivados/leaderboards e armazenamento ampliado que dependam de aceite especial.

## 1. Constatações verificadas em fontes oficiais

- [Guia de políticas de desenvolvedor](https://developers.google.com/youtube/terms/developer-policies-guide): a permissão adicional vale **somente para desenvolvedores auditados e expressamente aprovados**, mediante processo de compliance/quota, desde 01/06/2026.
- [Política adicional de métricas derivadas e armazenamento](https://developers.google.com/youtube/terms/derived-metrics-policy): admite certos scores/ratios, leaderboards, categorização, sentimento e outros analytics **sob emenda aceita e caso aprovado**. Scores próprios devem ser identificados como independentes, não como métricas oficiais.
- [Formulário oficial YouTube Data API Audit and Quota Extension](https://support.google.com/youtube/contact/yt_api_form): apresenta opções de inscrição **As an individual user**, categoria **Analytics & Reporting**, campo para número do projeto Google Cloud e confirmação explícita da emenda (se aprovada). Há também `Internal Company Tool`, mas isso descreve ferramenta para empregados de organização; **não marcar apenas por ser privada**.
- O formulário possui campos de **URL principal HTTPS**, **URL pública da política de privacidade**, evidências de produto/screenshots e, para ferramenta interna sem conta de demonstração, orientação para fornecer **screencast end-to-end**. A existência de projeto local sem site público pode exigir preparação adicional ou esclarecimento com YouTube; não inventar URL ou conformidade.
- A emenda, quando aplicável, permite retenção de certas estatísticas e métricas derivadas por **até 36 meses**. Títulos, nomes, descrições e comentários seguem limites de atualização/exclusão de 30 dias. Isso não autoriza cópia ou download de mídia audiovisual.

**Data de verificação:** 23/10/2026. Os textos podem mudar e o formulário pode variar conforme respostas/conta.

## 2. Procedimento proposto para o proprietário (sem enviar)

| Etapa | Ação | Pré-condição |
|---|---|---|
| A | Definir cliente e finalidade exata: offline read-only, pesquisa de vídeos/canais, comparação, scores próprios, eventual histórico; sem upload/publicação/scraping/mídia baixada | Uma descrição fiel do uso |
| B | Obter/criar um Google Cloud Project sob controle do proprietário, habilitar YouTube Data API se pertinente e anotar seu **Project Number** em armazenamento privado | Conta/projeto próprios; não colocar IDs ou credenciais no GitHub |
| C | Preparar demonstração real do cliente API sob ambiente controlado, com dados sintéticos ou fontes legitimamente autorizadas; registrar prints e screencast | Não alegar demonstração de integração API que não existe |
| D | Preparar URL de acesso HTTPS e política de privacidade pública se exigidas pelo formulário. Caso não exista site, identificar a limitação e consultar o canal oficial; não inventar endereço | Acesso de auditoria factível |
| E | Abrir [formulário de auditoria](https://support.google.com/youtube/contact/yt_api_form); selecionar modalidade pessoa física quando verdadeira, informar contato/projeto e categoria Analytics & Reporting | Não enviar antes de informações completas |
| F | Na seção sobre **derived metrics and data storage**, ler e aceitar conscientemente a emenda aplicável; descrever explicitamente o cálculo de outlier, eventual ranking e retenção pretendida, com controles | Não presumir deferimento nem existência de licença |
| G | Fornecer plano de volume/quota, uso dos métodos, funcionalidades e evidências exigidas; aguardar resposta formal | Só o YouTube decide elegibilidade/aprovação |
| H | Arquivar privadamente decisão/escopo/datas/restrições e converter em `SourcePolicyCapability` antes de liberar operações | Aprovação expressa verificável |

### Campos / documentos que não devemos inventar

- Nome civil e contatos da pessoa responsável; endereço e país.
- Google Cloud Project Number / identificadores técnicos e modalidade real do cliente.
- URL pública HTTPS do cliente, URL pública de Privacy Policy, documentação Terms of Service quando exigida.
- Telas reais de funcionalidade, política de privacidade, link de política, eventual fluxo OAuth e vídeo de demonstração.
- Estimativa **fundamentada** de volume de API/quotas, endpoints e periodicidade.
- Declaração precisa de finalidade e armazenamento: campos, duração, exclusão, refresh e opt-out.
- Aceite individual da emenda e pedido formal.

Esses itens são dados privados ou exigem preparação; **não** devem ser inseridos neste repositório público.

## 3. Texto-base em inglês para descrição do caso de uso (RASCUNHO, ajustar à realidade)

> I am developing a private, single-operator creative research tool for my own use. It is not offered, sold, or distributed as a software service. I want to use authorized YouTube Data API information to discover and compare videos and channels and to generate clearly labeled, independently computed analytics such as age-normalized view performance, engagement ratios, and channel/video trend reports. Any analysis intended to support my own content or brand-planning activities will be disclosed accurately as part of the use case. I will not present my analytics as YouTube-provided or YouTube-endorsed metrics. I will not download or store YouTube audiovisual content through the Data API. Processing, retention, access and deletion will follow the approved scope, including separate treatment of statistical versus descriptive data. I request an assessment of whether this use case qualifies for the additional analytics and derived-metrics policy.

Este texto é **proposta de preenchimento**, não descrição de uma implementação já existente. Não alegar existência de cliente API funcional, dashboard público, políticas publicadas ou auditoria concluída antes de realmente existir. Pode ser necessário fornecer projeto/URLs/telas para solicitar o regime adicional.

## 4. Três estados para o futuro policy gate

- `GENERAL_POLICY_ONLY`: apenas operações comprovadamente elegíveis sob regras gerais; nenhuma inferência de autorização adicional.
- `ANALYTICS_AMENDMENT_PENDING`: solicitação enviada, mas ainda sem aprovação; mesma restrição anterior.
- `ANALYTICS_AMENDMENT_APPROVED`: **somente** após comprovação, com escopo da aprovação, obrigações e prazo verificados. Revalidar antes de uso e registrar revogação.

Esses são rótulos de projeto propostos, **não enums canônicos**. Um clique no formulário ou check de aceite sem deferimento explícito não basta.

## 5. Relação com os PRs

- [PR #18](https://github.com/bribeirobr25/ai-creative-skill/pull/18): design e direitos, Gate 0 não aprovado.
- [PR #19](https://github.com/bribeirobr25/ai-creative-skill/pull/19): experimentos matemáticos e bridge de pesquisa **100% sintéticos**, não integração YouTube.
- **Nenhuma solicitação foi enviada ao YouTube.** Nenhum ID, segredo, endereço ou comprovante privado foi inserido no repositório.
