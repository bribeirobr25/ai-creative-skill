# Briefing fixo B2 — Tábua / Sauna no píer

Tábua é uma sauna a lenha **fictícia**, sobre um píer, com acesso a banho de mar, numa
cidade costeira também fictícia chamada Enseada do Norte. Foi criada para este estudo,
não existe comercialmente e o nome não foi verificado para registro.

## Contexto, público e objetivo

Público: adultos de 25 a 60 anos da região, iniciantes e frequentadores habituais.
Os iniciantes precisam entender como funciona, o que levar e quais regras seguir; os
habituais querem ver os horários e planejar uma visita rapidamente.

A visita deve: transmitir a experiência e o lugar; explicar o ritual e as regras;
mostrar a programação semanal com filtro; abrir cada tipo de sessão; calcular
localmente o valor estimado de uma visita, sem reservar. Idioma: português do Brasil.
Preços demonstrativos em euros.

Tom: calmo, direto e acolhedor, sem misticismo. **Não fazer afirmações sobre saúde,
bem-estar, imunidade, desintoxicação ou benefícios terapêuticos.** Sem depoimentos,
avaliações, escassez artificial ou contagem de vagas.

## Identidade: o que é fixo e o que é livre

Fixos: nome **Tábua**; assinatura **"Calor de lenha. Mar logo ali."**

Livres e deliberadamente em aberto: paleta, tipografia (pacote comum ou sistema),
wordmark tipográfico, grade, escala, composição, ritmo, tratamento das fotos via CSS,
componentes, microinterações e transições discretas. Não há layout de referência.

## Conteúdo obrigatório

Hero, título: "Aqueça. Mergulhe. Descanse."
Texto: "Uma sauna a lenha sobre o píer, com escada direto para o mar."
Ação principal: "Ver horários".

Como funciona, nesta ordem: Aqueça na sauna (10 a 15 min) · Desça a escada para o
mar, se quiser · Descanse no deck · Repita no seu ritmo.

O que levar: toalha, roupa de banho, chinelo e garrafa de água.
Regras obrigatórias: maiores de 18 anos; banho de mar por conta e risco de cada
pessoa, sem salva-vidas no local; sem álcool; silêncio na sauna.

| ID | Sessão | Duração | Preço | Capacidade | Quando |
|---|---|---|---|---|---|
| aberta | Sessão aberta | 90 min | €18 por pessoa | até 8 pessoas | Ter–Sex 17:00 e 19:00 · Sáb 10:00, 14:00, 17:00 · Dom 10:00 |
| nascer-sol | Nascer do sol | 90 min | €22 por pessoa | até 8 pessoas | Sáb e Dom 07:00 |
| privativa | Sauna privativa | 2 h | €120 por grupo | 1 a 6 pessoas | Dom 15:00 · Qua 20:00 |

Segunda-feira: fechado. Não exibir número de vagas nem disponibilidade em tempo real:
"Programação ilustrativa; disponibilidade não verificada neste protótipo."

Aviso visível no rodapé e no planejador: "Protótipo demonstrativo. Marca, local,
horários e preços fictícios. Nada é reservado." Informação de fotos: "Fotografias
ilustrativas de outro local (domínio público, CC0); não retratam as instalações da
marca fictícia." Os créditos de `assets/credits.json` devem estar acessíveis.

## Experiências e comportamento obrigatórios

1. Homepage com proposta, como funciona, o que levar e acesso aos horários.
2. Programação semanal visível com filtro "Todas" / "Nascer do sol": o filtro "Nascer
   do sol" mostra somente as sessões de 07:00 de sábado e domingo.
3. Página ou rota de detalhe para cada tipo de sessão: duração, preço, capacidade,
   horários e regras relevantes.
4. Planejador de visita local: escolher o tipo de sessão e o número de pessoas e ver o
   valor estimado. Aberta e Nascer do sol: preço × pessoas, 1–8. Privativa: €120 fixos
   para 1–6. Fora do limite ou valor inválido: mensagem de erro clara e nenhum total
   enganoso. Sem envio, pagamento, conta ou dados pessoais. Valor nunca negativo ou NaN.
5. Página ou seção de regras e perguntas frequentes.
6. Navegação de ida e volta por URL/hash; homepage, horários e planejador acessíveis
   em desktop e mobile; sem controles decorativos sem destino.
7. Teclado, foco visível, rótulos acessíveis, texto alternativo e `prefers-reduced-motion`.
8. Nenhuma chamada de rede externa.

## Instrumentação obrigatória (invisível ao usuário)

`nav-home`, `nav-schedule`, `nav-plan`, `schedule-filter-all`,
`schedule-filter-sunrise`, `schedule-slot` (cada horário exibido na programação, com
o atributo `data-session` igual ao ID da sessão), `session-aberta`,
`session-nascer-sol`, `session-privativa` (links que abrem o detalhe), `plan-session`
(select ou radios), `plan-people` (input numérico), `plan-total` (valor estimado) e
`plan-error` (mensagem de erro, presente somente quando houver erro).

Resultados esperados de referência: Sessão aberta × 3 = **€54**; Nascer do sol × 2 =
**€44**; Privativa × 4 = **€120**; Sessão aberta × 9 → erro; Privativa × 7 → erro.

## Materiais

- `assets/`: 19 fotografias CC0 de um mesmo dia e local, e `credits.json`. Usar sem
  alterar pixels; enquadrar via CSS sem distorcer. Não é obrigatório usar todas.
- `fonts/`: pacote comum de seis famílias OFL locais (`fonts.css`); uso opcional.
- `references/`: pacote comum de referências visuais (capturas e descrições neutras).
