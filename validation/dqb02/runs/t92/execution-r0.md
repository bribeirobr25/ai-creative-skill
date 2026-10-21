# Execução t92 · R0 · Tábua

- Início: 2026-10-21T00:12:55Z
- Fim: 2026-10-21T00:24:53Z
- Tempo ativo: ~12 min (inclui leitura do método, implementação e QA no navegador)
- Entrega: `/tmp/dqb/runs/t92/r0/index.html` (rotas por hash; abrir via `file://`)

## Arquivos do método lidos

- `ai-creative-skill/SKILL.md`: integral. Roteamento para `WEB_PREVIEW`.
- `references/AI_Creative_Skill_Work_Profile_Web_Experience_v0.2.md`: integral. Fluxo FAST, WEB_DIRECTION (uma decisão de composição, uma consequência observável, um tradeoff), LOCAL_CALCULATION, QA em 1440/390 (+768).
- `references/AI_Creative_Skill_V2.5_Integration_Manifest.md`: integral.
- `references/AI_Creative_Skill_Deliverable_Completeness_Catalog_Pre-v0.1-V2.4-CANDIDATE.md`: integral. Nenhum dos contratos ali (persona, ideia, storyboard etc.) se aplica a um website; não há contrato de web no catálogo.
- `web/docs/DELTA_AND_GATES.md` e `web/README_PTBR.md`: integrais.
- `references/AI_Creative_Skill_Method_Typography_Layout_Pre-v0.8.md`: **parcial**, só as linhas 1–40 (status e gatilho). Não apliquei as seções seguintes.
- `references/AI_Creative_Skill_Specialist_Method_System_Pre-v0.14-V2.4-CANDIDATE.md`: **somente grep** por "web|landing|typograph" (linhas 144 e 679). Não foi lido.
- Não li: Architecture Spec, Runtime Activation, Execution Contracts, schema `web_delivery_v0.2.schema.json` nem `scripts/creative_web.py`. Não gerei registro `web-delivery-r0.json` e não rodei a validação do schema. O helper `preview start` não foi usado porque o site abre direto por `file://`, que é o que o briefing pede.

## WEB_BRIEF (resumo)

- Verdade: tudo vem de `briefing.md` (marca, local, horários e preços fictícios). Não inventei preço, dado, depoimento nem afirmação de saúde.
- Público: iniciantes, que precisam do ritual e das regras, e frequentadores, que querem os horários rápido.
- Ação principal: "Ver horários". A ação secundária é o planejador local (`LOCAL_CALCULATION`, sem envio).
- Direitos: as fotos são CC0 de outro local, usadas sem alterar pixels (hash SHA-256 conferido contra `credits.json`) e com crédito em `#/creditos`.

## WEB_DIRECTION

- Ideia: **calor de lenha × frio do mar**, com a tábua (a prancha) como unidade estrutural. O carvão, o ember (laranja-brasa) e a madeira dão o lado quente; o azul-ardósia dá o lado do mar. Faixas horizontais funcionam como "tábuas" no ritual, nos divisores, no wordmark SVG de três pranchas e na grade da programação.
- Decisão de composição: o hero é dividido em dois. À esquerda fica o painel quente (carvão com linhas de pranchas), com o título em três cores ("Aqueça" em brasa, "Mergulhe" em azul itálico, "Descanse" em creme). À direita fica a foto da escada que desce para o mar.
- Consequência observável: no desktop, título e CTA "Ver horários" aparecem acima da dobra lado a lado com a escada. No mobile, a foto vai para cima (38vh) e logo abaixo vêm título, CTA e assinatura, ainda acima da dobra.
- Tradeoff: o painel tipográfico ocupa 46% da largura do hero, então a foto aparece menor e mais recortada que num hero de tela cheia. Troquei imersão fotográfica por legibilidade e pela leitura imediata da proposta.
- Tipografia (pacote comum): Fraunces para títulos, Instrument Sans para o texto e IBM Plex Mono para horários e dados (números tabulares).
- Referências visuais de `references/`: não usei nenhuma. Não há layout de referência.
- Fotos usadas: `bathing-ladder` (hero e privativa), `bench-1` (aberta), `abyfjorden-estuary-2` (nascer do sol, luz baixa), `jetty-and-water-2`, `bench-2`, `pier-and-jetty-4` (lugar). As 19 aparecem em `#/creditos`.

## Estrutura

Rotas `#/`, `#/horarios` (filtro também em `?filtro=nascer-sol`), `#/sessao/{aberta|nascer-sol|privativa}`, `#/planejar` (aceita `?sessao=`), `#/regras` (regras e FAQ), `#/creditos`. Toda a instrumentação `data-testid` do briefing está presente. `plan-error` só existe no DOM quando há erro; nesse caso o total vira "—", sem valor em €.

## Verificações (Playwright/Chromium, `file://`, build final)

Script: `evidence-r0/qa_r0.py`. Resultados: `evidence-r0/qa-results.json`, **50/50 PASS**. Hashes do build: `evidence-r0/build-sha256.txt`.

- Sem overflow horizontal em 6 rotas × 1440×900, 390×844 e 768×1024.
- A programação mostra 16 horários. O filtro "Nascer do sol" deixa só 2, ambos `data-session="nascer-sol"` às 07:00 (Sáb/Dom), e "Todas" volta aos 16.
- Os links `session-*` abrem o detalhe certo. O botão voltar do navegador funciona, e `nav-home`, `nav-schedule` e `nav-plan` funcionam.
- Planejador:
  - Aberta×3 = €54; Nascer×2 = €44; Privativa×4 = €120; Nascer×8 = €176; Privativa×1 = €120.
  - Aberta×9, Privativa×7, 0, −2, vazio e 2,5 dão erro, sem total em € nem NaN.
  - Não há erro no estado inicial, e a pré-seleção por `?sessao=` funciona.
  - No mobile, €54 também confere.
- Teclado: o primeiro Tab vai para o link "Pular para o conteúdo" e o segundo para o wordmark. O contorno de foco é visível (solid).
- Todas as imagens têm alt e carregam. O aviso do rodapé (texto exato) e a menção CC0 estão presentes.
- Com `prefers-reduced-motion: reduce`, as transições caem para cerca de 0 s.
- Nenhuma requisição fora de `file://` e nenhum erro de console ou JS.
- Revisão visual das capturas (home desktop/mobile, horários desktop/mobile, planejador com erro, detalhe privativa, planejador mobile) gerou estas correções no mesmo build:
  1. Contorno de foco espúrio no `main` depois da navegação.
  2. Cartões de horário no mobile quebravam o nome em 3 linhas; passaram para layout empilhado.
  3. Legenda de tags com sublinhado de link.
  4. Foco do campo numérico do stepper recortado.

  A QA foi rodada de novo depois de cada correção.

## Limitações conhecidas

- A QA é automatizada e feita pelo próprio agente (SELF_REVIEW). Não houve revisão humana nem teste com leitor de tela ou em dispositivo físico.
- O registro `WEB_QA` no schema v0.2 não foi produzido nem validado. As evidências estão em JSON livre.
- A rota "Regras" some do menu do topo no mobile por falta de espaço. Ela continua acessível pelo rodapé e pelos links da home.
- O hero desktop tem `max-height: 860px`; em telas muito altas sobra área abaixo. Testei somente os três viewports citados.
- No mobile, a programação fica longa (cerca de 2.500 px). O filtro e a contagem ficam no topo, mas não há navegação por dia.
- O caminho temporário de scripts (scratchpad do host) foi compartilhado e sobrescrito por outro processo durante a execução. Por isso o script final de QA foi recriado e executado de dentro de `$RUN/evidence-r0/`. Os resultados finais vêm apenas dele.
