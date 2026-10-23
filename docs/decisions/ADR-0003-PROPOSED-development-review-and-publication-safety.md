# ADR-0003-PROPOSED · Revisão contínua e proteção do repositório público

**Data:** 2026-10-23  
**Status:** PROPOSTA, NÃO CANÔNICA, NÃO APROVADA PARA MERGE  
**Aplicação pretendida:** transversal à AI Creative Skill, em consonância com ADR-0001 e ADR-0002.

## Contexto e aprendizado

As revisões independentes dos PRs #18 e #19 encontraram inconsistências de estados, cobertura, snapshots, limites, documentação e significado dos testes. Também mostraram risco de publicar URLs de acesso, dados de projetos e informações sensíveis num repositório público. Esses aprendizados não devem ficar apenas numa memória de sessão ou checklist específico de Intelligence.

## Decisão proposta

Adotar o ciclo **PLAN → IMPLEMENT → VERIFY → REVIEW → LEARN** para mudanças materiais:

1. **Plan:** recuperar baseline e owners canônicos, definir escopo/autorização, superfícies protegidas, fontes/direitos, riscos e critérios de aceite.
2. **Implement:** mudanças pequenas em branch dedicada e vinculadas ao responsável. Não alterar PR #17 de Web Experience sem coordenação com a sessão que o conduz.
3. **Verify:** testes positivos e negativos, metamórficos e fault injection quando relevantes, revisão de direitos, custos, segurança e host. Simulações Monte Carlo complementam os testes determinísticos, com premissas documentadas, nunca como “prova de mercado”.
4. **Review:** revisão independente do diff, dos contratos, da evidência real de testes, dos efeitos colaterais e das informações que serão publicadas; registrar PASS, FAIL, BLOCKED, NOT_RUN e UNVERIFIED conforme a execução.
5. **Learn:** persistir defeito, causa, correção, teste preventivo, alcance do aprendizado e limites de generalização. Nunca converter improvisação criativa em licença para alterar fatos, cânone, direitos, autorização, métricas ou custo.

## Classificação antes de publicar

| Classe | Critério |
|---|---|
| PUBLIC_OK | Código próprio, fixtures totalmente fictícias, documentação genérica e referências públicas autorizadas |
| REVIEW_REQUIRED | URLs de Drive/Docs, nomes de clientes em contexto privado, arquivos de fornecedor, IDs de projeto, screenshots, transcrições, caminhos privados, materiais sem licença de redistribuição esclarecida |
| NEVER_PUBLIC | API keys, tokens, cookies, credenciais, URLs assinadas de acesso, secrets, mídia/cânone privado de clientes, dados pessoais confidenciais e dumps de contas |

Um nome de marca ou URL de Drive não é necessariamente segredo por si só: é preciso classificar escopo e permissões. Contudo, remover um segredo do snapshot atual não elimina automaticamente cópias em commits, forks, caches e logs.

## Novo controle preventivo

- Antes de qualquer escrita no GitHub, inspecionar **todo o conteúdo** a publicar. Para commits locais, revisar diff staged; para GitHub connector, realizar preflight antes da chamada.
- Usar um guard estático de linhas adicionadas e arquivos suspeitos como camada auxiliar; não expor o valor do segredo em logs.
- No CI, verificar diffs da branch e executar testes de falso positivo/negativo. **CI após push não previne a primeira publicação**; exigir preflight local/manual antes do push.
- Analisar arquivos binários, URLs estáveis e documentação sensível manualmente; um scanner regex não certifica segurança completa.
- Antes de merge, revisar resultados, status da fonte, direitos, segurança, regressões e autorização. Nunca promover release porque os testes existentes ficaram verdes.

## Tratamento de exposição real

Não republicar conteúdo comprometido. Para credencial ou URL que concede acesso, revogar/rotacionar na origem antes de tratar histórico; investigar impacto em acessos/logs, forks/caches e registrar somente status e categoria em documentos públicos. Detalhes e dados privados ficam fora do Git público.

## Aplicação aos trabalhos atuais

- PR #17: permanecer sob a sessão Claude Code de website.
- PR #18: revisar contratos e privacidade; documentação de Intelligence continua Draft.
- PR #19: revisar semântica de busca vazia, seleção de snapshots, filtros repetidos, limites antecipados, escopo nacional, testes e Monte Carlo, preservando o isolamento sintético.
- Novos projetos: aplicar o mesmo gate de segurança, aprendizado, QA e revisão independentemente da capacidade.

## Limites desta proposta

A ADR não autoriza alteração da main, instalação da skill, chamada paga, compartilhamento de dados reais, remoção de histórico ou acesso a material privado. Uma ferramenta de varredura é apenas defesa em profundidade, não declaração de que o repositório foi auditado integralmente.

**Critério de promoção:** aprovação explícita do proprietário, revisão de conflitos com as ADRs existentes e testes de segurança do guard.
