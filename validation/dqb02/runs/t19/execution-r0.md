# Execução t19 · R0

- Início (UTC): 2026-10-21T00:12:52Z
- Fim (UTC): 2026-10-21T00:29Z (aprox.); trabalho ativo de cerca de 16–17 min, abaixo do limite de 30 min.
- Entrega: `/tmp/dqb/runs/t19/r0/index.html` (abrir via file://). Rotas por hash: `#/`, `#/horarios`, `#/sessao/{aberta|nascer-sol|privativa}`, `#/planejar`, `#/regras`, `#/creditos`.

## Arquivos do método efetivamente lidos
- `ai-creative-skill/SKILL.md`: inteiro.
- `references/AI_Creative_Skill_Work_Profile_Web_Experience_v0.2.md`: inteiro (rota WEB_PREVIEW, fluxo FAST de 8 passos).
- `references/AI_Creative_Skill_V2.5_Integration_Manifest.md`: inteiro.
- `references/AI_Creative_Skill_Release_Gates_v2.5.md`: inteiro.
- `references/AI_Creative_Skill_Deliverable_Completeness_Catalog_Pre-v0.1-V2.4-CANDIDATE.md`: inteiro. Nenhum dos contratos de domínio dele se aplica a um website.
- `web/README_PTBR.md` e `web/docs/DELTA_AND_GATES.md`: inteiros.
- `web/schemas/web_delivery_v0.2.schema.json`: estrutura lida por script (campos, enums, `$defs.check`).
- `web/runtime/validate.py`: linhas 1–120 (regras de validação, REQUIRED_FAST_CHECKS, build_hash).
- `references/AI_Creative_Skill_Method_Typography_Layout_Pre-v0.8.md`: só as primeiras ~40 linhas (status e gatilho). O gatilho é voltado para criativos e legendas, então não segui adiante.
- Não lidos: Current Design Manifest, Architecture Spec, Runtime Activation, Execution Contracts, Specialist Method System e os demais métodos. O SKILL.md manda carregá-los só quando forem relevantes (execução externa, sobreposição de rotas ou estado persistente), e nenhum desses casos ocorreu aqui.

## Decisões de direção (WEB_DIRECTION)
- Ideia visual específica, "tábuas e água": as ripas horizontais do píer viram o sistema de réguas do site. O título do hero é dividido em três "pranchas" com filetes, com recuo crescente, e "Mergulhe." aparece em itálico na cor da brasa. A mesma régua se repete nos passos, na programação, nas fichas de fatos e no recibo do planejador.
- Paleta: ardósia, tirada do céu nublado das fotos; papel de bétula; brasa (laranja da lenha) como único acento, usado no CTA, no foco e nos números.
- Tipografia: Fraunces (títulos e wordmark, com SOFT e opsz), Instrument Sans (texto) e IBM Plex Mono (horários, rótulos, cálculo).
- Wordmark: "Tábua" em Fraunces mais um símbolo SVG próprio (duas tábuas sobre uma onda).
- Decisão de composição: o título ocupa a metade esquerda, sobre um gradiente escuro, e a escada de banho fica visível à direita, como prova do "mar logo ali".
- Consequência observável: no desktop, o texto e a escada dividem a tela. No celular, o crop desloca para a escada e o título fica sobre a água, com a navegação fixa no rodapé da tela (Início, Horários, Planejar, Regras).
- Tradeoff: o hero escuro e dramático sacrifica parte do "acolhedor". Compensei com o fundo claro de bétula no resto do site.
- Referência: de `editorial-brand-led` aceitei apenas a hierarquia "título serifado grande sobre fundo escuro". Não herdei layout, navegação nem logotipo. As demais referências não foram usadas.
- Fotos usadas, sem alterar pixels, só com object-fit/object-position: bathing-ladder (hero), jetty-and-water-2 (faixa), bench-2 (aberta), abyfjorden-estuary-2 (nascer do sol), jetties-1 (privativa).
- Créditos: rota `#/creditos` gerada a partir de `credits-data.js`, cópia literal dos campos de `assets/credits.json` (para funcionar em file:// sem fetch), mais um link direto para `assets/credits.json`.

## Verificações realizadas (Playwright/Chromium, file://, 1440×900, 390×844, 768×1024)
- Planejador nas três viewports: aberta×3 = €54; nascer×2 = €44; privativa×4 = €120; nascer×8 = €176; privativa×1 = €120. Aberta×9, privativa×7, 0, −2, vazio e 2.5 mostram `plan-error` e o total "—", sem nenhum valor numérico.
- Filtro "Nascer do sol": exatamente 2 slots (Sáb 07:00 e Dom 07:00, data-session=nascer-sol). "Todas" mostra 16 slots.
- Navegação: `session-privativa` abre `#/sessao/privativa` e o botão voltar retorna a `#/horarios`. As rotas atualizam `aria-current` e o título da página.
- Sem overflow horizontal (scrollWidth ≤ viewport) em home, horários e planejar nas três larguras.
- Teclado: a ordem do Tab é skip-link → marca → nav → CTA, com outline sólido visível. Enter funciona no filtro e as setas funcionam nos radios.
- Com `reduced_motion=reduce`, a duração das animações cai para ~0.
- Todas as imagens têm alt e nenhuma está quebrada. Zero requisições externas. Zero erros de JS.
- Defeitos encontrados e corrigidos durante o QA:
  1. A caixa visual cobria o input do radio. Corrigido com z-index.
  2. No celular, a navegação ficava sobreposta ao topo, porque o backdrop-filter do header criava um containing block para o nav fixo. Corrigido.
  3. As imagens com lazy load não carregavam na captura full-page. Removido o lazy.
  4. A assinatura vertical no hero ficava ilegível. Virou o eyebrow do hero.
  5. O texto da faixa ficava ilegível sobre as tábuas. Ganhou um painel escuro.
  6. A foto da privativa repetia a do hero. Trocada.
- O registro `web-delivery-r0.json` passou no validador do método (`runtime.validate.check`, sem erros). Evidências estão em `evidence-r0/` (capturas e `qa-results.json`).
- A auditoria estática do método (`creative_web.py audit`) não foi executada: ela exige diretório de saída dentro de `r0/`, e optei por não gravar evidência no site.

## Limitações conhecidas
- Todo o QA é autoavaliação do agente, não revisão humana independente. Não houve leitor de tela real nem dispositivo físico.
- No celular, o valor estimado fica abaixo do formulário e exige rolagem depois de escolher sessão e pessoas.
- A instrumentação `plan-session` está em radios: os três inputs têm o mesmo data-testid.
- Os testids `session-*` aparecem várias vezes por página (cards na home e nos horários, links "outras sessões").
- Execução no modo MANUAL_SPEC_GUIDED: o método foi lido e aplicado manualmente, sem ativação automática de módulo.
