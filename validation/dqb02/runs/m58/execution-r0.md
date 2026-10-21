# Execução m58 · R0 · Miolo

- Início (UTC): 2026-10-20T23:54:43Z
- Fim (UTC): 2026-10-21T00:04:33Z
- Tempo ativo aproximado: ~11 min (dentro do limite de 30 min)
- Entrega: `/tmp/dqb/runs/m58/r0/index.html` (abrir via file://, sem servidor; rotas por hash `#/`, `#/fornada`, `#/fornada/doces|salgados`, `#/produto/<id>`, `#/encomenda`, `#/creditos`)

## Arquivos do método lidos
- `ai-creative-skill/SKILL.md`: integral.
- `references/AI_Creative_Skill_V2.5_Integration_Manifest.md`: integral.
- `references/AI_Creative_Skill_Work_Profile_Web_Experience_v0.2.md`: integral (rota WEB_PREVIEW, fluxo FAST).
- `references/AI_Creative_Skill_Deliverable_Completeness_Catalog_Pre-v0.1-V2.4-CANDIDATE.md`: integral (não há contrato específico para web; usei apenas a sequência geral de autoverificação).
- `web/README_PTBR.md`, `web/docs/DELTA_AND_GATES.md`: integrais.
- `web/schemas/web_delivery_v0.2.schema.json`: integral.
- `web/runtime/validate.py`: integral (para alinhar o registro aos checks FAST exigidos e ao hash do build). `web/runtime/qa.py`: só o trecho da exceção / função audit (via traceback e grep).
- Não lidos: Current Design Manifest V2.4, Architecture Spec, Runtime Activation, Execution Contracts, Specialist Method System, Typography/Layout e Image Direction methods. Pelo SKILL.md, eles não eram exigidos para um WEB_PREVIEW FAST sem execução paga.

## WEB_BRIEF (resumo)
Padaria fictícia de fornada única. Ação principal: "Ver a fornada" → encomenda demonstrativa com horário. Verdade do produto: somente a tabela do briefing. UNKNOWN: alérgenos, ingredientes e origem. O sorvete do bolo de maçã não acompanha o produto. Cálculo apenas local (LOCAL_CALCULATION), sem envio.

## Decisões de direção (WEB_DIRECTION, provisória)
- Ideia: "bilhete da fornada". A semana vira uma linha do tempo (sexta → madrugada → sábado 8h–12h) e a encomenda é tratada como bilhete pontilhado.
- Paleta: papel de farinha (#f6efe3), casca (#8a4b1f), tinta (#2a1d14) e um vermelho-frutas só para avisos.
- Tipografia: Fraunces (wordmark e títulos, com itálico "sexta." em cor de casca), Instrument Sans (leitura), IBM Plex Mono (preços, horários e rótulos, como num bilhete).
- Hero com foto em arco (alusão a boca de forno) e etiqueta "Uma fornada por semana".
- Como funciona: três passos com as palavras-chave exatas, régua tracejada no desktop e vertical no mobile.
- Catálogo: os 2 primeiros cartões são largos em "Todos" para dar ritmo. Filtros em pílulas com contagem.
- Detalhe: galeria com miniaturas, preço e unidade em mono, aviso de alérgenos, stepper 1–12. No bolo de maçã há uma caixa de aviso sobre o sorvete, e o cartão do catálogo também avisa.
- Encomenda: select 1–12 por linha, remover, estado vazio com ícone SVG próprio, 4 horários em radio (obrigatórios), "Revisar encomenda" → resumo local escuro que recebe foco. Aviso de protótipo na encomenda, no resumo e no rodapé.
- Créditos: rota `#/creditos` com miniatura, título, autor, licença (link) e fonte das 14 fotos.
- Fotos sem alteração de pixels; enquadramento por object-fit/object-position.
- Persistência da encomenda em localStorage, só para conveniência e com try/catch.
- Movimento discreto (subida de 8px na troca de rota, hover nos cartões), zerado com prefers-reduced-motion.

## Verificações realizadas
1. `creative_web.py route --intent WEB_PREVIEW` → WEB_PREVIEW/FAST, build_required. Sem --intent, o pedido literal retornou "Ambiguous request" (limitação do roteador determinístico).
2. Playwright/Chromium (`evidence-r0/qa.py`, resultados em `evidence-r0/qa-results.json`): **42/42 PASS**. Cobertura:
   - textos obrigatórios exatos; 5 produtos; Salgados = só o scone; Doces = 4;
   - detalhe dos 5 produtos com aviso de alérgenos e add-order; aviso do sorvete;
   - estado vazio; 2 × Nó de cardamomo = **€5,60**; 12 = €33,60; opções 1–12;
   - revisão bloqueada sem horário; 4 horários; resumo com horário, total e aviso;
   - voltar/avançar do navegador; remover → vazio; sem NaN/negativo; 14 créditos;
   - foco visível via Tab; todas as imagens com alt; sem overflow horizontal em 1440, 390 e 768 (home, detalhe, encomenda);
   - reduced motion; nenhuma requisição externa; nenhum erro JS.
3. Revisão visual das capturas (`evidence-r0/*.png`) em 1440, 390 e 768. Três correções: (a) padding lateral perdido em detalhe e cabeçalhos (atalho `padding` sobrescrevia `.wrap`); (b) scroll-margin para o resumo e a âncora não ficarem sob o topo fixo; (c) o toast agora some ao trocar de rota. QA reexecutado depois das correções: 42/42.
4. `creative_web.py audit` numa cópia de r0 (exige saída dentro do site), resultado em `evidence-r0/static-audit/.qa/`: assets PASS, js_syntax PASS; "anchors_static" FAIL só porque o auditor estático trata rotas hash `#/...` como âncoras quebradas (no navegador elas funcionam). A cópia foi removida depois.
5. Registro `web-delivery-r0.json` (state PREVIEW_DRAFT, verdict PARTIAL, execution_mode MANUAL_SPEC_GUIDED) validado com `creative_web.py validate --site-dir`: **ok: true**.

## Limitações conhecidas
- Revisão estética feita pelo próprio executor; sem revisão humana, cega ou com leitor de tela (NOT_TESTED).
- Preview aberto por file://; o preview server do método não foi usado.
- O teste de teclado cobriu foco visível e navegação básica, não um percurso completo só com teclado.
- O total da encomenda só aparece no resumo e no bilhete; não há subtotal por categoria.
- A encomenda persiste em localStorage apenas neste navegador; não há envio, conta, pagamento nem dados pessoais.
- O verdict PARTIAL do registro é deliberado: não houve aprovação humana e o anchors_static do auditor é falso positivo.
