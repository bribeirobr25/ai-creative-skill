# Resultados de execução · 2026-10-18

- **Teste unitário:** 35/35 PASS; 0 chamadas pagas. Inclui bloqueio de status inválido, alias legado, prova falsa de QA browser, estado de autorização, duplicação de checks, paths fora da raiz, idempotência de preview, arquivo oculto, recuperação e regressão de regiões.
- **diBoaS ZIP v0.1:** HTML/CSS/JS/ativos presentes; novo registro v0.2 candidato cumpre schema. 12 checks: 3 PASS estáticos, 9 NOT_TESTED. Não se declara o ZIP anterior como conforme.
- **Della ZIP v0.1:** idem; 16 ativos de produto no pacote original. 12 checks: 3 PASS estáticos, 9 NOT_TESTED.
- **Preview local diBoaS:** `start` + `HEALTHY_OWNED` + `stop` confirmado. **Preview local Della:** `stop` + `restart` + `HEALTHY_OWNED` + `stop` confirmado. URL/porta são efêmeros.
- **Browser real:** Chromium Playwright com o binário do sistema retornou `net::ERR_BLOCKED_BY_ADMINISTRATOR` para `localhost`. Não houve captura de navegador nova. O arquivo JSON preserva esse bloqueio como evidência.
- **Edição Della (simulação):** substituição só da headline no hero em cópia; `collection`, `croissant`, `details`, `contact` byte-identical no HTML serializado pela comparação de regiões; CSS/JS não alterados. Uma mudança CSS compartilhada exige novo QA. **Não é uma revisão com regiões aprovadas pelo usuário.**
- **Portabilidade:** testes da extensão funcionam em cópia do diretório e não exigem dependência da skill Sites. Não foi feito clean-host real com contexto reduzido e prompt genuíno de construção.

## Escopo de aceitação

`P0_RUNTIME_IMPLEMENTED_WITH_BLOCKED_BROWSER_QA`, `P1_PARTIAL`, `INTEGRATION_NOT_PROVEN`, `NOT_PROMOTED`.

Não há atribuição causal de qualidade visual, aquisição, ativação ou conversão. Nenhum material de Della/diBoaS foi republicado neste pacote, exceto metadados de referência e relatórios sem arquivos de mídia.
