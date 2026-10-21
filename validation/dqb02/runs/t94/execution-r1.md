# Execução t94 · R1 (autorrevisão)

- Início (UTC): 2026-10-21T00:29:06Z
- Fim (UTC): 2026-10-21T00:32Z (aprox.; último registro de relógio em 00:31:54Z)
- Tempo ativo: cerca de 3 a 4 minutos, dentro do limite de 15.
- `r1/` foi criado como cópia de `r0/`. `r0/` não foi modificado.
- Veredito: **CHANGED**, com correções pequenas. A direção, a estrutura, o comportamento e a instrumentação foram mantidos.

## Método aplicado na revisão

- Work Profile Web v0.2, passo 7, executado de fato com as ferramentas do método:
  - `scripts/creative_web.py preview start r1` subiu o preview: STARTED em http://127.0.0.1:58473/.
  - `audit` rodou contra esse preview e retornou status PARTIAL. As renderizações em 1440 e 390 deram PASS (BROWSER_OBSERVED).
  - `content_truth` ficou NOT_TESTED: o próprio método exige evidência humana.
  - `anchors_static` deu FAIL ADVISORY. É falso positivo: o checador trata rotas por hash (`#/horarios`) como ids de elemento, e a navegação foi confirmada no navegador.
  - O preview foi parado com `preview stop` (STOPPED).
- O `audit` exige que a pasta de saída fique dentro do site. Por isso os arquivos `.web_qa`, `.web-preview-owner.json` e `.web-preview.log` foram movidos para `evidence-r1/audit/` e `r1/` ficou só com os arquivos do site.
- Revisão pela rubrica: inspecionei capturas de telas não revisadas no R0 (detalhe de sessão em desktop, regras em desktop, planejador no mobile, faixa da assinatura e faixa final da home).
- Revisão de fidelidade: Typography & Layout §2 (autoridade do texto) e a regra do Work Profile de nunca inventar fatos.

## Problemas encontrados → correções (somente em `r1/app.js` e `r1/styles.css`)

1. **Fidelidade: textos não presentes no briefing.**
   - O título "Quatro passos, na ordem que o corpo pedir." soava levemente corporal/místico e contradizia o "nesta ordem" do briefing. Passou a "Quatro passos, no seu ritmo."
   - O detalhe de Nascer do sol dizia "com o mar ainda quieto", uma afirmação sobre o local sem base no briefing. Passou a "A primeira sessão do sábado e do domingo, às 07:00. Mesmo formato da Sessão aberta, em outro horário e com outro preço."
   - Removi a regra inventada "Chegue alguns minutos antes".
   - A Sessão aberta dizia "A sessão de todos os dias de funcionamento", o que é impreciso porque ela não acontece todos os dias com o mesmo horário. Passou a "Disponível de terça a domingo."
2. **Ambiguidade.** O rótulo "Aberta / Ter a Dom" na faixa de fatos podia ser confundido com a "Sessão aberta". Passou a "Funciona / Ter a Dom".
3. **Tipografia da assinatura.** "Calor de lenha. Mar logo / ali." quebrava no meio da frase no desktop. Agora são duas linhas deliberadas: "Calor de lenha." / "Mar logo ali." Também evitei a quebra do rótulo "A PARTIR DE" introduzida pela mudança.

## Preservado

- A direção visual (tábuas, paleta, tipografia, fotos e enquadramentos), todas as rotas, todos os `data-testid`, a lógica do planejador, o filtro, os avisos, os créditos e `index.html`, que tem o mesmo hash do r0.

## Regressões e verificações

- `evidence-r1/qa.py`, o mesmo script do R0 apontado para r1, rodou 51/51 PASS após a última alteração:
  - Rotas e navegação, incluindo o voltar do navegador.
  - Filtro: 16 horários em "Todas" e 2 em "Nascer do sol".
  - Planejador: €54, €44 e €120, e erros para 9 e 7 pessoas e para entradas inválidas.
  - Teclado, `alt`, avisos, movimento reduzido, nenhuma rede externa e nenhum erro de JS.
  - Nenhuma rolagem horizontal nos 3 tamanhos de tela.
- A faixa da assinatura foi conferida em 1440, 390 e 768 (`evidence-r1/r1-*-sig.png`), sem quebra indevida e sem estouro.
- Nenhuma regressão encontrada.
- Hashes finais:
  - `r1/app.js` a6bfa848…
  - `r1/styles.css` 15cb641f…
  - `r1/index.html` b33984ca…, igual ao r0.

## Limitações mantidas

- `content_truth` precisa de revisão humana. Não houve teste com leitor de tela nem em aparelho físico.
- O contraste não foi medido.
- Não há registro `web-delivery` validado pelo schema.
