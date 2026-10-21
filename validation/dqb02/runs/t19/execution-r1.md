# Execução t19 · R1 (revisão própria, sem feedback externo)

- Início (UTC): 2026-10-21T00:29:10Z
- Fim (UTC): 2026-10-21T00:31Z (aprox.); cerca de 2–3 min ativos, dentro do limite de 15 min.
- r1 é cópia de r0 com edições pontuais (WEB_EDIT de superfície mínima). r0 não foi alterado.

## Revisão (Work Profile Web v0.2, passo 7, e rubric.md)
Revisei pelas capturas de r0 (evidence-r0): homepage, horários com filtro, detalhe da privativa, planejador e erro, e regras, em 1440, 390 e 768.

## Problemas encontrados
1. **Clareza no celular (390×844), planejador.** O valor estimado fica abaixo do formulário, fora da primeira dobra. Depois de mudar sessão ou pessoas, o resultado não aparece sem rolar a página. Defeito de usabilidade na interação crítica da tarefa.
2. **Hierarquia na home (desktop), seção "O que levar".** O título usava o tamanho padrão do navegador, menor que o título vizinho "Quatro regras, sem exceção". A hierarquia das duas colunas ficava desequilibrada. Ajuste menor.

Considerei e mantive como estava:
- A repetição dos testids `session-*` e o grupo de radios `plan-session`. São coerentes com o briefing.
- A ilustração da sessão Nascer do sol. É foto de outro horário, mas está identificada como ilustrativa.

## Correções feitas em r1
- `app.js` e `styles.css`: adicionado o resumo "Valor estimado" logo abaixo do campo de pessoas, visível só em telas de até 860px. É `aria-hidden` (o `plan-total`, com `aria-live`, continua sendo a fonte acessível e instrumentada). Mostra o mesmo valor ou "—" em caso de erro.
- `styles.css`: `#bring-title` passou a 1.9rem, igual ao título das regras.

## Preservado
- Direção visual, paleta, tipografia, fotos e crops.
- Rotas, todo o conteúdo obrigatório, avisos, créditos e instrumentação.
- A lógica de cálculo e de erro não foi alterada.

## Verificações (Playwright/Chromium, file://, r1, evidências em evidence-r1/)
- Planejador nas três viewports: aberta×3 = €54, nascer×2 = €44, privativa×4 = €120. Aberta×9, privativa×7, 0, −2, vazio e 2.5 dão erro e total "—".
- Filtro "Nascer do sol": somente Sáb e Dom 07:00. "Todas" mostra 16 slots.
- Detalhe e voltar funcionam. Sem overflow horizontal.
- Teclado: Tab com foco visível, Enter no filtro, setas nos radios.
- `reduced_motion` OK. Imagens com alt e nenhuma quebrada.
- 0 requisições externas. 0 erros JS.
- Inspeção visual do planejador mobile (válido e erro) e do desktop: o resumo aparece sob o stepper no celular e fica oculto no desktop.
- Regressões: nenhuma observada.

## Limitações
- Revisão feita pelo próprio agente, sem avaliação humana nem leitor de tela.
- Nas capturas full-page de celular, a nav fixa aparece no meio da imagem; é artefato da captura.
- O registro `web-delivery-r0.json` não foi reemitido para r1.
