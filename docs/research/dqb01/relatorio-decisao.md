# DQB-01 — Relatório de decisão

Data: 20/10/2026. Estado: **piloto A/B executado; AWAITING_HUMAN_REVIEW**.

Foram construídos quatro websites locais navegáveis: A e B, cada qual com primeira entrega R0 e uma revisão R1. O coordenador inspecionou capturas e estados reais, aplicou os mesmos testes funcionais e mediu posições de conteúdo no navegador. Esta análise é exploratória, não cega e não independente. Não há notas humanas, aprovação profissional ou vencedor geral. C, o workflow nativo Higgsfield, não foi executado. Sua qualidade não pode ser ordenada por este piloto.

## Execução e evidência

O protocolo/briefing/assets foram congelados em `881ca0b`, antes de A/B. Dois executores sem histórico herdado receberam o mesmo briefing, rubrica, três fotos, fontes do sistema e instruções Sites. A não recebeu AI Creative Skill. B recebeu adicionalmente a metodologia main `39a0bfa`, aplicada manualmente (`MANUAL_SPEC_GUIDED`). Não foi um teste de ativação automática da skill instalada.

Configuração de modelo herdada igual, sem override; versão exata de backend, seed e consumo de tokens não foram expostos/verificados. Os contextos foram isolados por instrução, não por sandbox de filesystem. Os registros não relatam leitura cruzada; isso não equivale a monitoramento completo de acesso.

| Condição | Primeira entrega UTC | Decorrido R0 | Única revisão UTC | Decorrido R1 |
|---|---|---:|---|---:|
| A | 21:00:14–21:07:36 | 7m22s | 21:10:01–21:13:46 | 3m45s |
| B | 21:00:24–21:07:57 | 7m33s | 21:10:19–21:14:30 | 4m11s |

São intervalos informados pelos executores, não instrumentação de trabalho contínuo. Limites: 20 minutos R0 e 12 R1, ambos respeitados. A soma é 11m07s para A e 11m44s para B; os 37 segundos de diferença não estimam custo causal da skill. O coordenador deu até três observações específicas por condição, sob a mesma política. A revisão inclui direção externa; não mede apenas autoaperfeiçoamento.

Verificações comuns: **100/100 em R0 e 100/100 em R1**, abrangendo as duas condições nos formatos 1440×900 e 390×844. Além disso, quatro checks de overflow da homepage por rodada passaram em 320 e 768 px. Catálogo, filtro, produto Arco, carrinho, quantidade/subtotal, remoção, navegação, recursos e erros foram exercitados. O check comum de teclado usa foco programático e Enter; os executores registraram sequências complementares de Tab/teclado. Não somar esses conjuntos como se fossem uma única cobertura independente. Os executores também verificaram Trama e outras rotas nas larguras adicionais. Sem testes de leitor de tela, Safari/Firefox, conversão ou certificação WCAG.

A primeira execução do adaptador reportou seis falhas falsas de texto: quatro em A e duas em B. Quebras de linha não eram normalizadas. O adaptador foi corrigido e executado sobre os mesmos sites R0, sem editar as entregas. As saídas iniciais foram preservadas. B R0 também teve falha de dependência no validador nativo; B R1 passou após receber ambiente existente com a dependência. Esse sucesso é validação estrutural do registro, não avaliação estética. As falhas históricas não foram apagadas nem reclassificadas retroativamente.

Os hashes confirmam R0 intacto, fotos idênticas em todos os sites e cópias de avaliação equivalentes. Há quatro pacotes neutros X/Y, ordem de mapeamento e de viewport alternada, com formulário local. Seus oito testes de interface passaram. **Zero respostas humanas.** Nenhum teste automatizado foi contado como revisor.

## 1. Qual abordagem entregou o melhor resultado observado?

Não há vencedor geral demonstrado. A R0 já entregou identidade consistente com serifa, produto protagonista e catálogo com preço visível na primeira tela desktop. B R0 tinha linguagem sem serifa consistente, mas headline mais dominante e catálogo com nomes/preços abaixo da primeira tela. Em R1, B ficou mais eficiente para apresentar a coleção e comparar informações; A reforçou a composição editorial e a clareza dos controles do carrinho. As preferências estéticas continuam abertas.

| Dimensão | Observação concreta em R1 | Interpretação permitida |
|---|---|---|
| Direção de arte | A: título transversal e volumes desiguais; B: duas peças numeradas como abertura | Duas decisões mais específicas, sem prova de identidade excepcional |
| Tipografia | A combina serifa expressiva com dados sem serifa; B reduz o título e mantém dados sans | Linguagens coerentes; serifa não é sinônimo de luxo ou superioridade |
| Composição | A dá mais escala a Trama; B integra apresentação e coleção, removendo a repetição inicial de Arco | A favorece impacto individual; B economiza repetição e favorece comparação |
| Imagens | Mesmas fotos e silhuetas visíveis; fundos fotográficos diferentes persistem | Não há ganho atribuível a melhor geração de assets |
| Componentes | B repete número/nome/preço; A mantém títulos e reorganiza resumo/controles | Melhor consistência local, sem vencedor geral |
| UI/interações | Filtro, navegação, quantidade e remoção funcionam; A separa quantidade de remover | Passes confirmam tarefas, não sofisticação percebida |
| Responsividade | Ambos antecipam nome/preço e ação na página de produto mobile | Ganho de hierarquia observável em ambos |
| Clareza/usabilidade | B antecipa preços no catálogo; A explicita total do item; ambos declaram simulação | Hipóteses de menor esforço, ainda sem tempos de usuários |
| Fidelidade | Texto obrigatório, fotos, valores e especificações preservados | Sem regressão observada; nenhuma compra real é prometida |

## 2. O que explica as diferenças?

As mudanças rastreáveis são ordem de conteúdo, proporção das fotos, escala tipográfica, distribuição de espaço e repetição de componentes. Não são melhorias do modelo de imagem. A usa maior produto isolado e mais espaço; B reúne os dois produtos na abertura e antecipa informações. Em ambos, deslocar nome/preço acima da foto e reduzir sua altura no mobile aproximou identificação e ação.

| Medida no navegador, em px a partir do topo | A R0 → R1 | B R0 → R1 |
|---|---:|---:|
| Topo de “Adicionar ao carrinho”, 390 px | 898 → 678 | 876 → 682 |
| Topo do preço Arco no catálogo, 1440 px | 840 → 853 | 964 → 362 |
| Topo do preço Arco no catálogo, 390 px | 738 → 699 | 713 → 396 |

Fontes: `layout-r0.json` e `layout-r1.json`. Valores arredondados, Chromium/DPR 1. Ambos passaram a mostrar a ação inteira dentro dos 844 px neste produto. Isso não estabelece regra universal de colocar tudo acima da dobra, ganho de conversão ou pontuação estética. A revisão de A não melhorou toda métrica: o preço do catálogo desktop desceu cerca de 13 px, coerente com a escolha de composição.

## 3. Qual é o valor agregado mensurável da AI Creative Skill?

**Ganho estético incremental não demonstrado.** A e B tiveram a mesma quantidade de passes comuns. B deixou rastros adicionais de método, decisões, revisão localizada e registro Web validado; isso é evidência de processo, não de estética. O catálogo B R1 tornou dados e descrições mais precoces que A, mas houve feedback específico justamente sobre esse problema. Não é possível atribuir a diferença apenas à skill, separando amostragem, escolhas do executor e intervenção externa.

## 4. Onde o design continua genérico ou pouco acabado?

R0 de ambos partiu de uma fórmula familiar: wordmark, texto à esquerda/foto à direita, dois cards e bloco editorial verde. R1 se diferencia mais, mas ainda usa fotografia de catálogo sem produção visual própria, tipografia do sistema, marca textual simples e narrativa breve. A mantém repetição de Arco na homepage; B tem apresentação mais direta de catálogo, menos imersiva. Os fundos fotográficos não formam uma campanha uniforme. Essas limitações ajudam a explicar a distância percebida para uma marca madura; não autorizam chamar qualquer minimalismo de amador. Também não provam que uma geração paga resolveria direção de arte.

## 5. Quais mudanças podem elevar o acabamento?

Testar uma decisão visual ligada ao briefing, propagada entre páginas, seguida de inspeção da hierarquia real em desktop/mobile. Aqui, “duas formas” motivou o par numerado em B; a relação entre volumes motivou A. Ambas as revisões foram possíveis com os mesmos assets. A candidata é tornar verificável a intenção criativa já registrada no método, não exigir mais seções, animações ou prompts extensos.

Assets mais uniformes e imagens de contexto são outra hipótese, separada do ganho da skill. Este piloto os fixou deliberadamente e não testa essa hipótese.

## 6. Como demonstrar reprodução?

Primeiro obter duas avaliações reais, com razões por dimensão e viewport, preservando desacordos e empate. Aplicar o critério congelado para “profissional”. Depois testar a mudança candidata em briefing ainda não visto, de outra categoria, sem impor serifa, numeração ou a mesma composição. Manter inputs, recursos e revisão equivalentes; repetir execuções independentes para observar variabilidade.

O critério do protocolo requer vantagem justificada em pelo menos duas dimensões, sem regressão crítica, antes de tratar uma mudança como candidata sustentada para a etapa seguinte. Esse limiar ainda não foi atingido por revisão humana.

## 7. O que depende de pessoas ou de recursos pagos?

Pessoas: maturidade profissional, preferência, facilidade percebida, tarefas sem orientação e possíveis conflitos entre aparência e uso. Os pacotes estão prontos; os revisores não foram contatados nem simulados.

Higgsfield: o pacote website-builder 2.2.1 inspecionado documenta geração de materiais e deploy; não é equivalente a executar Claude + workflow histórico do vídeo. A cotação consultada, sem geração, foi 0,25 crédito para **uma** imagem gpt_image_2_5 3:2. O total do website é desconhecido. Nenhum job pago, upload de mídia privada ou deploy foi executado. C permanece `NOT_RUN_NATIVE_WORKFLOW`. Uma comparação competitiva futura deve explicitar as diferenças de modelo, assets, tempo, ferramenta e publicação. Não é necessário pagar para obter as avaliações humanas ou realizar outro teste local com assets existentes.

## 8. Qual é a próxima mudança concreta no produto?

Propor ao time um teste pequeno dentro do **WEB_DIRECTION/WEB_EDIT existentes**: no registro de direção, explicitar uma decisão de composição ligada à marca e um efeito esperado na hierarquia; na revisão, confrontar intenção e tela real em homepage, produto e catálogo. Registrar uma concessão e corrigir apenas as superfícies afetadas. Usar campos existentes de decisão/evidência antes de considerar alterações de contrato. Não criar novo profile, router ou harness.

Isso é uma **hipótese de melhoria**, ainda não uma alteração canônica recomendada como comprovada. O PR contém pesquisa e protótipos, não modifica a skill instalada nem contratos canônicos. Antes de integrar, revisar neutralidade dos pacotes, proveniência manual de B, feedback não cego, limites da amostra e evidências. Não divulgar “qualidade profissional validada” ou “superior ao Higgsfield”.

## Evidências e limites de interpretação

- [Galeria navegável](galeria.html): screenshots equivalentes, sem pontuação automática.
- [Resultados R0](../../../validation/dqb01/results/r0-reviewed/results.json) e [R1](../../../validation/dqb01/results/r1-reviewed/results.json).
- [Métricas R0](../../../validation/dqb01/results/layout-r0.json) e [R1](../../../validation/dqb01/results/layout-r1.json).
- [Integridade](../../../validation/dqb01/results/delivery-integrity.json), [autorização](../../../validation/dqb01/results/execution-authorization.json) e [feedback](revision-feedback.md).
- [Registros dos executores](../../../validation/dqb01/results/executor-records/): autorrelatos, caminhos do host normalizados; não avaliações independentes.
- [Procedimento para revisores](entrega-revisores.md) e [teste dos pacotes](../../../validation/dqb01/results/reviewer-packet-ui.json).

É um único caso com briefing detalhado e baseline Sites forte, biblioteca limitada, contextos isolados por instrução, coordenador não cego, uma revisão com achados adaptados e um navegador. Essas condições restringem causalidade e generalização. A observação anterior do usuário de que o Higgsfield parece melhor em Della/diBoaS é uma motivação válida para investigar; não foi convertida artificialmente em resultado deste novo briefing. As etapas gratuitas viáveis foram executadas; o benchmark de qualidade permanece aberto até receber evidência humana.
