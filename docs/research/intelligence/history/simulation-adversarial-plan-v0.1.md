# Plano de resiliência, simulações e testes adversariais · v0.1

**Data:** 2026-10-23  
**Estado:** PROPOSTA / NÃO EXECUTADO / NÃO CANÔNICO / SEM APROVAÇÃO DE PRODUTO  
**Integração:** [arquitetura v0.1](architecture-preimplementation-v0.1.md), [matriz INT-01..INT-26](acceptance-and-validation-v0.1.md), [revisão da liberdade criativa e resiliência](design-review-creative-latitude-resilience-v0.1.md).  
**Proveniência de método:** reaproveita `validation/methodology/design.md`, `validation/methodology/economics.md`, `validation/harness.py`, `validation/generators/pairwise.py` e `validation/simulations/economics.py`. A simulação anterior de 36 mil execuções é sobre economia hipotética de rotas e **não** cobre automaticamente os novos conectores de inteligência.

## 1. Objetivos e fronteiras

Avaliar invariantes, confiabilidade, segurança, custos, cobertura, comportamento em falhas, robustez do ranking, preservação da intenção do usuário e uso saudável da latitude criativa. Nunca confundir:
- **propriedade determinística** demonstrada por teste vs **evidência empírica** de um serviço externo;
- **simulação estocástica** com distribuições supostas vs **probabilidade real calibrada**;
- **sucesso técnico** vs **interpretação correta** vs **preferência criativa humana**;
- **maior diversidade** vs **mais ideias úteis**;
- **falha de fonte** vs **ausência genuína de conteúdo**;
- **medida de dispersão** vs **incerteza epistêmica sobre cobertura e licença**.

Os testes devem maximizar aprendizado por custo, não número de loops. Cada família possui hipótese, oracle/asserts, nível de evidência, owner e gate de saída.

## 2. Pirâmide de validação

| Camada | Técnica | Quando | Exigência |
|---|---|---|---|
| P0 | Fixtures sintéticas e invariantes de contratos | Gate 1 | Teste determinístico, sem acesso externo |
| P1 | Metamorfismo, property-based/fuzzing com seed, pairwise/t-wise | Gate 1 | Oracles consistentes, shrink/reprodução do contraexemplo |
| P2 | Fault injection, state machine e concorrência | Gate 1/2 | Falhas explícitas sem custos/estados impossíveis |
| P3 | Monte Carlo + sensitivity + cenários extremos | Após P0–P2 e contrato estável | Dados sintéticos, parâmetros publicados, nenhuma afirmação de mercado |
| P4 | Canaries reais autorizados (YouTube/Meta) | Gate 1/2 | Evidência de API, preço, termos, cobertura e qualidade da amostra |
| P5 | Comparações criativas humanas e ablações | Gate 3/5, se aplicável | Avaliação independente, padrões de relevância, não apenas contagem de outputs |

**Importante:** `Monte Carlo` é complemento, não substituto de condições-limite construídas intencionalmente. Eventos raros de segurança precisam oracles exatos, testes exaustivos em subdomínios pequenos ou injeção focada. Amostragem aleatória pode não atingi-los.

## 3. Invariantes não negociáveis

**INV-01 Authority:** consulta paga sem aprovação/reserva é bloqueada; um `creative_risk_level` experimental não desbloqueia gasto.

**INV-02 Evidence:** fatos de origem e valores não podem ser inventados; `UNKNOWN` não vira zero; um erro de API não vira `NO_RESULTS`.

**INV-03 Identity:** produto, anunciante, conta, anúncio e publicação possuem IDs/escopo; duplicata não é confirmação independente; similar ≠ mesmo fabricante.

**INV-04 Metric semantics:** tempo, fuso, janela, denominador, tipo de conteúdo e significado de geografia devem ser compatíveis; ausência de histórico não produz velocidade medida.

**INV-05 Licensing/retention:** dado não licenciado para persistência não é gravado; revogação/expiração invalida cache e derivados na extensão suportada.

**INV-06 Isolation:** isolamento de projeto, credenciais, conteúdo privado, approved canon e usuários.

**INV-07 Bounded autonomy:** pesquisa não dispara criação/pagamento/publicação; exploração não altera filtros `PRESERVE`/exclusões.

**INV-08 Accounting:** no máximo uma reserva efetiva por tentativa lógica; `confirmed_spend + open_reservations <= authorized_cap` e sem double-billing por retry.

**INV-09 Recovery:** timeout após submissão de request pago = reconciliação/UNKNOWN, não replay cego; em consultas grátis, retry só se idempotente e admissível.

**INV-10 Reporting:** as afirmações públicas refletem população elegível e cobertura observada; nenhuma classificação “top Alemanha” sem universo defensável.

## 4. Matriz inicial de stress cases

| ID | Cenário | Oráculo |
|---|---|---|
| RES-01 | API `RATE_LIMITED` enquanto página seguinte já teria resultados | Relatório PARTIAL, paginação e lacuna explícitas; sem `NO_RESULTS` |
| RES-02 | 401/403, mudança de permissão, licença revogada durante run | Interromper uso inadmissível, controlar cache, estado rastreável |
| RES-03 | Schema drift, nulls, listas ausentes, tipos inesperados | `SCHEMA_DRIFT` ou erro classificado, não rankings fabricados |
| RES-04 | 2 regiões homônimas, creator DE com audiência no BR, idioma PT | Preservar base geográfica, não inferir audiência |
| RES-05 | Conteúdo duplicado/repost; anúncio traduzido e variação real | Dedup idempotente mantendo publicações/métricas independentes |
| RES-06 | Cortes em virada UTC, fuso Europe/Berlin, DST, janela com limites abertos | Janela consistente, sem contagem duplicada/omissão silenciosa |
| RES-07 | Like ou view contador decresce por correção; zero baseline | Delta negativo não vira crescimento positivo; intervalos inválidos sinalizados |
| RES-08 | Série irregular, gaps longos e missing-not-at-random | Não alegar VPH preciso nem tendência representativa |
| RES-09 | Falha de fonte A, fonte B livre mas com região/métrica diferente | Não substituir A silenciosamente nem apresentar equivalência falsa |
| RES-10 | Pico de viralização de um criador grande mascara outliers pequenos | Normalização/elegibilidade por coorte; outliers e views totais separados |
| RES-11 | Alta taxa de anúncios com métricas indisponíveis | Persistência é sinal distinto de engajamento; score respeita missing |
| RES-12 | Processos concorrentes consultam/quebram cache e reserva | Estado sem duplicata e sem limite de gasto ultrapassado |
| RES-13 | Timeout após possível cobrança, retorno duplicado ou fora de ordem | Uma tentativa lógica, reconciliação sem repetição paga |
| RES-14 | TTL de dados expira no meio do relatório | Marcar stale/desabilitar uso não autorizado; nada de relatório “atual” fictício |
| RES-15 | Texto de anúncio/comentário contém instruções para agente | Não executar prompt injection; conteúdo continua dado |
| RES-16 | Pesquisa exata solicita só Nubank; exploração tenta bancos concorrentes | Não ampliar sem finalidade/autoridade; `PRESERVE` vence |
| RES-17 | Pesquisa aberta: “ideias novas de conteúdo para bolsas” | Permitir hipóteses úteis realmente diversas dentro de budget/escopo |
| RES-18 | Dez “conceitos diferentes” com mesmo hook, mesma premissa | Detectar mode collapse qualitativamente; sem forçar variação inútil |
| RES-19 | Usuário solicita “só pesquisa, sem campanha” | Stop após relatório; sem produção paga |
| RES-20 | Host sem Python, sem rede ou DB indisponível | Limitação explícita e alternativa permitida; sem fingir que executou |
| RES-21 | Consulta gratuita responde com latência extrema e 30% páginas ausentes | Estouro de time budget gera PARTIAL e causa visível |
| RES-22 | Entradas malformadas, UUID duplicado, caracteres Unicode adversariais | Rejeitar/normalizar sem corromper identidade nem emitir comandos |
| RES-23 | Fallback muda ordenação ou score de conjunto parcial | Destacar instabilidade e cobertura; ranking nunca absolutizado |
| RES-24 | Resultados históricos sob nova versão do algoritmo | Preservar versão, inputs e não reescrever evidência passada |

Cada item deve ser registrado em `validation/scenarios/register.json` **somente na futura branch de implementação**, com fixtures sintéticas, risco, procedimento e evidência. Nenhum caso é considerado executado por estar listado.

## 5. Monte Carlo: desenho proposto

**Finalidade:** investigar limites e efeitos de incertezas operacionais (não “prever viralização verdadeira”). A simulação deve ocorrer em ambiente offline, sem criar token de API, credencial, rede ou consumo de serviço. Começar pequena e escalar quando houver perguntas concretas.

### 5.1 Variáveis aleatórias candidatas

- `source_availability`, `rate_limit_event`, `latency_seconds`, `api_error_class`;
- `collection_coverage`, `pagination_completion`, `null_metric_ratio`, `stale_ratio`;
- `duplicate_fraction`, `false_merge_fraction`, `false_split_fraction`;
- `sampling_bias` e fração do universo inobservável;
- `source_price_per_call`, `requests_per_report`, `retries` com limite;
- `baseline_sample_size` e assimetria de distribuição de visualizações;
- `rights_expiry_event`, `storage_permission` e `auth_revocation`.

**Distribuições propostas para testes, não fatos reais:** Bernoulli (disponibilidade), beta-binomial (taxas com heterogeneidade), lognormal/gama (latência e custos assimétricos), misturas com caudas pesadas (views), cenários discretos para política e revogação. Não estimar distribuição a partir de intuição e chamá-la calibrada.

### 5.2 Dependências e cenários correlacionados

Evitar pressupor independência entre falhas: limite de quota e latência podem piorar juntos; fontes vendendo o mesmo dataset não são evidências independentes; uma mudança de política pode afetar múltiplos conectores; campanhas grandes influenciam vários rankings. Modelar **cenários correlacionados**, incluindo choque comum e seleção missing-not-at-random. Testes de pior caso devem acompanhar médias.

### 5.3 Saídas recomendadas

- Fração simulada de relatórios completos, parciais ou bloqueados sob as suposições.
- Falhas graves por invariante: objetivo **zero** em toda amostra e em testes determinísticos; qualquer violação → FAIL.
- Custo por relatório útil e por observação válida (simulado, não faturamento real).
- Tempo de resposta p50/p95/p99 e timeout rate nas condições simuladas.
- Rank stability: Kendall tau / Jaccard top-k ou equivalentes quando as populações observadas diferem, com comparabilidade verificada.
- Precision/recall de entity matching **contra ground truth sintético construído**, não contra mercado real.
- Taxa de evidência insuficiente corretamente classificada.
- Para exploração: número de hipóteses materialmente distintas **aceitas por humanos**, não somente variedade lexical.

Registrar valores e parâmetros de entrada, seed, código/hash, amostragem, sensibilidades, variação de cenários, eventos raros forçados e limites de validade. Se falhas graves não aparecerem numa amostra, não se pode alegar risco zero; a falta de eventos tem limite estatístico e depende das hipóteses. **Intervalo de simulação ≠ intervalo de confiança de performance real.**

### 5.4 Estratégias comparadas em sensibilidade (sem vencedora antecipada)

- `one_source_only`: pesquisa somente na fonte principal elegível;
- `eligible_fallback`: fallback quando existe fonte autorizada com semântica compatível;
- `bounded_divergence`: uma consulta principal + até duas trilhas exploratórias autorizadas;
- `strict_exact`: apenas entidade/categoria exata solicitada.

Comparar os quatro eixos: cobertura, custo, latência, precisão/identidade e utilidade humana. Identificar o custo de novas hipóteses úteis vs sobrepesquisa. Não selecionar `bounded_divergence` automaticamente por gerar mais itens.

### 5.5 Reprodutibilidade e tamanho da amostra

Começar com **seeds fixas** e um conjunto pequeno de casos para depuração (por exemplo 100–500) e, quando necessário, um lote mais amplo ilustrativo (por exemplo 2.000–10.000 por cenário) com memória/custo monitorados. Esses tamanhos são *sugestões de engenharia*, não garantias de significância ou cobertura.

Para comparação de estratégias, usar *common random numbers* / ensaios pareados quando tecnicamente significativos, além de vários seeds. Testar condições-limite separadamente; fuzzing com shrink/reprodução. Anexar sumários compactos JSON, nunca dados privados, e não cometer resultados de sensores/mercados com direitos incertos.

## 6. Como testar a criatividade sem engessá-la

Os testes são para proteger a **decisão**, não prescrever o conteúdo criativo.

### 6.1 Quatro canários com controles

**CR-01 Exact fidelity:** pesquisa exata com zero espaço de exploração. PASS exige nenhuma troca de marca/mercado/período/objetivo; criatividade não é requisito.

**CR-02 Bounded discovery:** consulta aberta com variedade permitida. PASS exige pelo menos uma hipótese extra com conexão contextual clara quando evidência suporta; a IA pode retornar nenhuma se não houver oportunidade relevante. Custo deve permanecer no envelope.

**CR-03 Divergence vs baseline:** mesmo briefing, fontes e budget; comparar sem divergência e com exploração limitada. Avaliação cega por humanos usando relevância, distinção conceitual, evidência e valor, reportando casos em que a exploração não ajudou. Sem objetivo universal de “mais é melhor”.

**CR-04 Canon-protected creative transfer:** pesquisa vira briefing Ads/Organic; criativo pode explorar hooks, narrativa e estética, mas não inventar produto, material, claim, resultado ou autoridade. Sem geração real por padrão.

**Ablation:** quando resultado melhorar/piorar, variar **uma dimensão por vez** (novas palavras de busca, expansão de mercado autorizada, interpretação alternativa, revisão contraditória) mantendo dados/modelo/brief fixos. Um teste não separa todas as causas, e a primeira impressão do agente não substitui julgamento independente.

### 6.2 Antipadrões que devem reprovar

- Quantificar “criatividade” só por entropia lexical, temperatura ou número de variantes.
- Tornar criatividade uma obrigação para pesquisas exatas, reparos, datas e métricas.
- Confundir um modelo imprevisível com um sistema resiliente.
- Aceitar uma história plausível sem evidência porque gerou uma boa campanha.
- Bloquear ideias distintas com templates excessivamente rígidos.
- Promover um achado da simulação para regra de método sem teste de mundo real.

## 7. Etapas e custo de execução

| Quando | Trabalho | Custo externo esperado |
|---|---|---|
| **Design Gate 0** | Documento, matriz, revisão de ownership, exemplos e orçamento | Zero |
| **Dev Gate 1** | P0–P2 em fixtures, property-based, metamorphic, failure tests | Zero de APIs, custo local |
| **Dev Gate 1.5** | P3 Monte Carlo e sensitivity em offline, assim que contratos e oracles estabilizarem | Zero de APIs, custo computacional local |
| **Dev Gate 2** | Canaries autorizados em API e comparação com verdade observada | Depende da fonte/quotas |
| **Integration Gate 3** | CR-01..CR-04, transferência Research→Creative e QA humano | Evitar geração paga; só se aprovada |
| **Release Gate 5** | Regressão ampla, CI, host canary, avaliação editorial/direitos | Dependente de escopo e autorização |

**Gates para avançar:**
- Primeiro validar algoritmos e oracles contra casos conhecidos e negativos.
- Não rodar 10 mil simulações para mascarar uma falha determinística não corrigida.
- Não executar canaries pagos sem aprovação/reserva previstas no contrato atual.
- Não promover método/feature a produção por PASS técnico ou estatística sintética.
- Rodar cenários de exploração apenas em tarefas cuja latitude criativa foi legitimamente aberta.

## 8. Evidência de teste: registro mínimo proposto

~~~yaml
test_id: RES-11
category: MONTE_CARLO_OR_FAULT
scenario_version: v0.1
implementation_commit: UNKNOWN
execution_performed: false
source_kind: SYNTHETIC
seed: null
assumptions_ref: null
oracle_ref: INV-02
sample_size: null
tested_surface: NONE_YET
observed_results: null
violations: null
coverage_limits: "Planejado; não executado"
human_review: NOT_RUN
production_approval: UNVERIFIED
~~~

**Nenhum número deste plano é resultado observado da nova capacidade.** `NOT_RUN` permanece até haver código, fixtures, execução comprovada, outputs e interpretação. Reutilizar vocabulário canônico de resultado; os exemplos não estabelecem segundo schema normativo.

## 9. Pendências para implementação

- Implementar adapters de coleta com interfaces injetáveis e *fake clients* para simular falhas sem rede.
- Adotar teste property-based apenas com dependência justificada; integração ao harness e CI existentes.
- Definir políticas de retenção, quotas, latência e gastos por fonte **antes** de testes reais e histórico.
- Calibrar distribuições com dados reais autorizados quando possível; documentar limites de generalização.
- Preservar distinção entre performance medível de vídeos, estimativa de alcance, public ad persistence, creative interpretation e viabilidade comercial.
- Verificar originalidade de métodos, licença de dependências e estado de validação por gate.

**Este plano não implementa os testes e não autoriza execuções externas.**
