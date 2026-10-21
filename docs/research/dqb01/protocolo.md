# Protocolo DQB-01, revisão 1

Preparado em 20/10/2026 antes das implementações. A revisão registrada no Git antes
do início é a referência congelada. O piloto não é pré-registrado em serviço
externo. Nenhum desfecho estético foi observado ao definir os critérios abaixo.

## Condições e validade

| Condição | Intervenção | Inferência permitida |
|---|---|---|
| A | Briefing comum e orientações gerais Sites, sem AI Creative Skill | Capacidade do agente nesse ambiente |
| B | Mesmo pacote + AI Creative Skill main `39a0bfa39270ea4b685b0f862e7dbf647cf81d77` | Diferença observada associada à aplicação manual da metodologia |
| C | Workflow nativo Higgsfield, somente se compatível com orçamento e autorização | Comparação competitiva; causal somente com condições realmente equivalentes |

A/B: mesma configuração de modelo herdada do host, sem override, sessões sem
histórico herdado; mesmas capacidades de ferramentas disponíveis e permissões.
Não há garantia de determinismo ou igualdade de amostragem. Registrar identificação
do modelo somente se exposta; não inventar versão de backend, seed ou tokens.
Os executores compartilham filesystem, mas recebem escopo explícito para não ler
o outro diretório. Isso é isolamento de contexto/instrução, não sandbox físico.
Registrar desvios de acesso. O coordenador não implementará A e B fingindo
independência. A execução isolada depende da autorização explícita para agentes.

Ambos recebem o mesmo briefing, rubrica e instrução de buscar acabamento profissional.
Nenhum recebe captura de Higgsfield, achados de execuções anteriores ou expectativa
de vencedor. Sites é orientação comum; A não significa “modelo sem skills”.
B aplica a versão integrada, não as propostas ainda não integradas de #9/#10.
Custos de leitura/aplicação da metodologia fazem parte do esforço de B.

## Unidade e recursos

- Um briefing, uma execução por condição; quatro experiências: homepage, catálogo,
  produto e carrinho demonstrativo. Dois produtos; sem pagamento/conta/backend.
- HTML/CSS/JS local, sem framework obrigatório, dependências ou chamadas externas.
  O navegador tem acesso somente à origem local durante a verificação.
- Mesmos três JPEGs licenciados e fontes do sistema. Nenhuma edição dos pixels,
  nova imagem ou geração; crop via CSS permitido, sem ocultar características
  essenciais. Wordmark em texto e ícones simples próprios permitidos.
- Inspeção principal em 1440×900 e 390×844, DPR 1; smoke adicional 320×740 e 768×1024.
- Primeira entrega: até 20 minutos de execução ativa por condição, com tempo
  decorrido registrado. Uma entrega completa; problemas conhecidos permanecem.
  Se houver limite/erro de ferramenta, registrar, sem compensação oculta.
- Revisão: mesmo prompt de autoavaliação pela rubrica e até três achados concretos
  do coordenador por condição, priorizados por bloqueio de tarefa, fidelidade e
  acabamento, nessa ordem. Até 12 minutos ativos. Sem copiar o concorrente.
  Mesma política, não necessariamente mesmas correções. Preservar feedback integral.
- Retries por falha de infraestrutura são registrados separadamente; não contam
  como nova proposta criativa. Reexecução completa muda o tamanho da amostra.

## Rubrica de qualidade

Notas ordinais 1–5, ou N/A justificado, por pessoa, viewport e versão. 2 e 4
representam níveis intermediários. Exigir referência a tela/estado e justificativa.
Não inferir qualidade a partir de número de elementos, animações ou tamanho de fonte.

| Dimensão | 1: insuficiente | 3: adequado | 5: acabamento excepcional para o briefing |
|---|---|---|---|
| Direção de arte/identidade | Decisões desconexas ou identidade indistinguível | Linguagem coerente, ainda intercambiável | Ideia visual específica e consistente em todas as experiências |
| Tipografia/hierarquia | Leitura difícil, pesos/escala sem função | Texto legível e hierarquia reconhecível | Escala, ritmo e quebras deliberados; expressão e leitura se reforçam |
| Composição/espaçamento | Alinhamentos, proporções ou densidade atrapalham | Estrutura equilibrada e compreensível | Ritmo entre telas/seções, espaço e enquadramento sustentam a narrativa |
| Imagens | Crops inadequados, tratamento incoerente ou produto confuso | Imagens claras e pertinentes | Integração cuidadosa com composição e conteúdo, dentro do material disponível |
| Componentes | Estados ou padrões inconsistentes | Padrões estáveis e estados essenciais | Família visual precisa; variações motivadas e detalhes resolvidos |
| UI/interações | Ornamento atrapalha ou controles parecem inacabados | Respostas claras e interação previsível | Feedback, transições e microdetalhes ajudam a tarefa com discrição |
| Responsividade | Conteúdo/ação perde legibilidade ou uso | Reorganização funcional em ambos os tamanhos | Composição deliberada por formato, preservando caráter e prioridades |
| Clareza/usabilidade | Proposta/tarefa ambígua, caminhos difíceis | Proposta entendida e tarefas concluíveis | Informação no momento certo, descoberta fácil e pouco esforço percebido |
| Fidelidade | Conteúdo obrigatório alterado ou afirmação inventada | Requisitos preservados | Requisitos e escolhas criativas se reforçam, sem promessas indevidas |

Esforço/custo/intervenções são medidas separadas, não uma décima nota estética.
Não somar passes técnicos à rubrica. Não publicar um ranking por média que esconda
desacordo; mostrar pares de notas e preferências por dimensão. Uma média descritiva,
se utilizada posteriormente, deve identificar N/A e não representar significância.

## Tarefas e evidência

Partir de estado limpo para cada avaliação. Sem dicas antes da primeira tentativa:

1. Explicar a proposta e identificar se há compra real.
2. Encontrar uma bolsa de até €200 e identificar preço e descrição.
3. Abrir Arco, ler medidas e adicionar uma unidade ao carrinho.
4. Alterar para duas unidades: subtotal esperado €360; remover e reconhecer vazio.
5. No mobile, usar navegação, voltar ao catálogo e repetir a ação principal.
6. Repetir a navegação principal por teclado; verificar foco visível e saída de modal,
   se houver. Não exigir modal quando outra solução adequada é usada.

Capturar homepage hero/full, catálogo, produto, carrinho preenchido/vazio e
navegação mobile. Evidência automatizada: carregamento local, erros de script,
imagens, overflow, caminhos, totais e controles. Não é certificação WCAG nem
estudo de conversão. Tempo e sucesso de humanos serão coletados separadamente
do tempo de automação.

## Avaliação humana e decisão

Dois revisores humanos independentes, idealmente incluindo experiência em UI/design.
Cada um recebe versões neutras X/Y com mapeamento inverso e a mesma rubrica.
Não revelar condição, relatório analítico ou hipótese de vencedor antes das respostas.
Primeira entrega e revisão são rodadas separadas; avaliar a primeira antes da final
evita contaminá-la pelo conhecimento da correção. Registrar familiaridade e conflitos.

Classificação global: protótipo, adequado, profissional, ou evidência insuficiente,
com exemplos. “Profissional” exige ambos julgarem assim, nenhuma dimensão abaixo de
3 e nenhuma tarefa central bloqueada; isso é um critério operacional deste piloto,
não definição universal de profissionalismo.

Uma melhoria merece teste seguinte se houver vantagem justificada em pelo menos
duas dimensões, sem regressão crítica de fidelidade/usabilidade, e decisão rastreável
na implementação. Não exigir vitória de B. Desacordo/empate/N/A permanecem explícitos.
Sem humanos: `AWAITING_HUMAN_REVIEW`; análise do coordenador é exploratória,
não cega e não independente. Não promover mudança canônica por essa análise.

Para falar em reprodução: aplicar a alteração candidata a outro briefing de outra
categoria mantendo o procedimento; preservar também resultado negativo. Este piloto
não autoriza anunciar superioridade populacional, causalidade forte ou ganho de vendas.

## Integridade

Preservar hashes dos inputs, versões R0/R1, timestamps, prompts, feedback e evidências.
Não editar R0 depois de entregá-lo; R1 é cópia separada. Registros são artefatos de
pesquisa; não criar novos enums de runtime, profiles ou harness. Reutilizar contratos
existentes quando aplicáveis. O branch independente não depende de PRs abertos.
O time pode revisar o protocolo durante a execução; qualquer mudança depois da
primeira entrega é identificada como emenda, sem reescrever a história.
