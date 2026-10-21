> Executor self-report; host paths normalized for publication. Not an independent review.

# DQB-01 — condição A — registro de execução

## Primeira entrega (R0)

- Início UTC: 2026-10-20 21:00:14.
- Fim UTC: 2026-10-20 21:07:36 (fechamento do registro).
- Tempo decorrido aproximado: 7 minutos; trabalho ativo aproximado: 6 minutos, incluindo leitura, implementação, inspeção e QA. Limite de 20 minutos não esgotado.
- Modelo: configuração herdada, sem override; identificador exato de backend/seed/tokens não exposto e não inventado.
- Escopo: site local, buildless, sem geração paga, publicação, registro de Site, Git ou comunicação com executor concorrente.
- Entrega: `r0/index.html`, `r0/styles.css`, `r0/app.js`, `r0/assets/`; evidências em `r0/evidence/`.
- Estado: R0 concluído e congelado na entrega; aguardando única rodada de feedback. Avaliação humana: `AWAITING_HUMAN_REVIEW`.

## Arquivos de orientação efetivamente lidos

1. `shared/executor-common.md`
2. `shared/briefing.md`
3. `shared/protocolo.md`
4. `<HOST_USER>/.codex/plugins/cache/openai-curated-remote/sites/1.0.1/skills/sites/SKILL.md`
5. `<HOST_USER>/.codex/plugins/cache/openai-curated-remote/sites/1.0.1/skills/sites/references/preview/local.md`
6. `<HOST_USER>/.codex/plugins/cache/openai-curated-remote/sites/1.0.1/skills/sites/references/design/presentation-led.md`

Materiais consultados: `shared/assets/credits.json`, visualização dos três JPEGs fornecidos. Foram também lidos/inspecionados arquivos e capturas produzidos por esta execução dentro de R0. Nenhum acesso ao AI Creative Skill, fontes da intervenção, condição concorrente, histórico ou material Higgsfield. Nenhum desvio de acesso identificado.

## Decisões aplicadas

- Direção editorial sóbria: base papel, tinta e verde; Georgia para títulos e Arial para navegação e informações de compra; wordmark tipográfico próprio.
- Homepage com proposta e objeto concreto, apresentação comparável dos dois produtos, editorial separado e claramente ilustrativo.
- Catálogo com filtro explícito e URL própria para a faixa de preço; proporção das fotos ajustada após inspeção para manter nomes e preços visíveis em 1440 × 900.
- Páginas de produto com imagem única, dados demonstrativos e inclusão com confirmação/link para carrinho.
- Carrinho em sessão local, seletor nativo de 1 a 9, subtotal, remoção, vazio e aviso de demonstração; sem checkout.
- Navegação hash, créditos internos, foco visível, link para pular conteúdo, live region e respeito a reduced motion.
- Fotos copiadas sem alteração de bytes/pixels; apenas enquadramento CSS. Sem fontes ou recursos remotos.

## Verificações realizadas

- Sintaxe de JavaScript: passou.
- Chromium local via `file://`, DPR 1, em 1440 × 900, 390 × 844, 320 × 740 e 768 × 1024.
- Fluxos automatizados: catálogo; filtro Até €200 retorna só Arco; detalhe/medidas; adicionar Arco; quantidade 2 retorna €360; remover/estado vazio; Trama retorna €240; quantidade 9 retorna €2.160.
- Nas quatro dimensões: imagens carregadas, sem overflow horizontal nos estados verificados, sem erro de script e sem requisição HTTP/HTTPS da página.
- Em desktop e mobile: navegação por Tab/Enter, filtro, detalhe, adicionar, carrinho, quantidade por tecla numérica 2/Tab e remoção; foco sólido confirmado nos alvos registrados. Back/Forward, créditos e limite de nove unidades ao adicionar repetidamente também passaram.
- Capturas: homepage hero e full (1440/390), catálogo, Arco, carrinho preenchido/vazio nos quatro tamanhos; Trama em 1440/390. Inspeção visual própria, sem alegação de avaliação humana independente.
- Relatórios executáveis/resultados: `r0/evidence/verify.cjs`, `verification.json`, `keyboard.cjs`, `keyboard.json`.

## Falhas/retries e limites

1. A primeira inicialização do Chromium dentro do sandbox terminou em SIGTRAP/EPERM. Retry com permissão de execução externa ao sandbox foi aprovado automaticamente e permitiu QA local. Não foi falha do site.
2. Primeiro teste de filtro leu o DOM antes de concluir o evento hashchange. O teste foi corrigido para aguardar a remoção de Trama; passou. Captura de catálogo em 768 px inicialmente conservou altura anterior durante transição de rota; espera explícita pelo título e dois frames corrigiu a coleta.
3. Duas sequências de teclado por setas para o seletor nativo do Mac não produziram o valor 2 esperado e esgotaram a espera (30 s e 5 s). O teste final com tecla numérica 2 e Tab concluiu a tarefa em ambos os tamanhos. Não se afirma validação de todas as combinações de teclas/plataformas do controle nativo.
4. Biblioteca visual limitada aos três JPEGs e uma vista por produto; fundos e fotógrafos distintos. Não se extrapola essa limitação para capacidade de qualquer metodologia.
5. Verificação automatizada não constitui certificação WCAG, pesquisa de conversão ou julgamento independente de qualidade profissional. Sem teste em dispositivo físico ou leitor de tela.

Não há servidor de preview mantido: a entrega abre diretamente em navegador por `index.html` ou pode ser servida pelo coordenador como conteúdo estático.
