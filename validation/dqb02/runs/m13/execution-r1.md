# Execução m13 · R1 (autorrevisão, sem feedback externo)

- **Início:** 2026-10-21T00:16:06Z
- **Fim:** 2026-10-21T00:22Z (aprox.)
- **Tempo ativo:** ~6 min
- **Base:** cópia de `r0/` em `r1/` (diff vazio confirmado antes das edições). `r0/` não foi alterado.
- **Rota do método:** `WEB_EDIT` com alteração na menor superfície possível (Work Profile Web v0.2, passo 7). Registro em `web-delivery-r1.json`, com `WEB_REVISION`; `creative_web.py validate` → `ok: true`.

## Revisão

Revisei as capturas do R0 (home, fornada, detalhe, encomenda vazia e com resumo, créditos) em 1440, 390 e 768, contra a rubrica e o passo 7 do método: ponto focal, hierarquia, proeminência do produto, CTA visível. Classifiquei cada achado como defeito objetivo, falha de direção ou preferência estética.

### Problemas encontrados

1. **Defeito visual pequeno.** No detalhe, a caixa "Quantidade / Adicionar" tinha uma faixa vazia embaixo (`.added` com `min-height` reservada), visível em 1440 e 390. O cartão parecia inacabado.
2. **Defeito visual pequeno.** Em 390px, a legenda do hero quebrava "Foto ilustrativa" em duas linhas, desalinhada da legenda à esquerda.
3. **Defeito de acessibilidade.** O link "Encomenda" no nav tinha um `aria-label` no span do contador. Leitores de tela podem ignorar esse rótulo e anunciar só "Encomenda 0".
4. **Higiene.** CSS `.toast` sem uso (o elemento tinha sido removido no R0).

### Avaliados e mantidos (preferência estética, não defeito)

- O arco recorta o topo das fotos: é o tradeoff declarado na direção, e o produto continua centrado.
- No mobile, o destaque da home é um carrossel horizontal com o card seguinte aparecendo parcialmente: isso indica que há rolagem lateral, e o link "Ver os cinco itens" vem logo abaixo.
- O hero em 390px mostra o CTA principal na primeira tela.

Não vi falha de direção nem problema de fidelidade.

## Correções em r1

| Arquivo | Mudança |
|---|---|
| `styles.css` | `.added` sem altura quando vazio; quando preenchido, ganha margem e divisória tracejada (mesma linguagem do "ticket"). |
| `styles.css` | `.figcap` com `flex-wrap` e `white-space:nowrap` em "Foto ilustrativa". |
| `styles.css` | Regras `.toast` removidas. |
| `index.html` | Contador do nav com `aria-hidden="true"` e um `span.visually-hidden` ", N itens". |
| `app.js` | `updateCount()` atualiza o texto oculto em vez do `aria-label`. |

## Preservado

Tudo o mais é idêntico ao R0:
- direção visual, paleta, tipografia, wordmark e layouts;
- textos e avisos obrigatórios;
- rotas, data-testids e lógica da encomenda;
- assets, fontes e créditos.

## Regressões e verificações

- **QA funcional completa** (`work/qa_r1.py`, igual a `work/qa.py`, apontando para `r1/`): 84 asserções em 1440×900, 390×844 e 768×1024 mais teclado e reduced motion. Resultados em `evidence-r1/functional-results.json`.
  - Na 1ª execução houve uma falha isolada, "tablet filter todos 5". Repeti duas vezes em r1 (84/84 nas duas) e duas vezes em r0 (84/84).
  - Conclusão: falha intermitente de tempo do script (espera de 200ms após o clique no filtro), não regressão. O código dos filtros não foi alterado no R1.
- **Verificação específica:**
  - Nome acessível do link: "Encomenda 0 , 0 itens". Depois de adicionar, o texto oculto passa a ", 1 item".
  - Mensagem de confirmação dentro da caixa, com divisória (`evidence-r1/mobile-detail-added.png`).
  - Legenda do hero em duas linhas íntegras (`evidence-r1/mobile-home-fold.png`).
- **Sem overflow** horizontal, **sem erros** de console e **sem requisições externas** (incluídos na QA).
- **Auditoria estática do método** sobre cópia: mesmo falso positivo de âncoras por hash do R0 (`evidence-r1/static-audit-on-copy/`).
- **Veredito do registro:** `PARTIAL`, pelo mesmo motivo do R0.

## Limitações (inalteradas)

- Só Chromium headless.
- Sem leitor de tela real.
- Sem revisão humana.
- Contraste não medido automaticamente.
