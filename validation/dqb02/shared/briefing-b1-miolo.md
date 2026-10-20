# Briefing fixo B1 — Miolo / Fornada de sábado

Miolo é uma micro-padaria **fictícia**, criada para este estudo. Não existe
comercialmente e o nome não foi verificado para registro.

## Contexto, público e objetivo

Miolo assa somente uma vez por semana: a massa é preparada na sexta à noite e as
encomendas são retiradas no sábado de manhã, num bairro residencial fictício
chamado Vale. Público: vizinhos de 25 a 55 anos que planejam o café da manhã ou o
lanche do fim de semana e querem saber o que haverá na fornada e encomendar antes.

A visita deve: apresentar a padaria e seu funcionamento; permitir ver e filtrar a
fornada; abrir cada produto; montar uma encomenda demonstrativa com horário de
retirada; revisar um resumo. Idioma: português do Brasil. Preços demonstrativos em euros.

Tom: caloroso, honesto, simples e preciso. Sem escassez artificial ("últimas
unidades"), contagens regressivas, depoimentos, avaliações, prêmios ou slogans vagos.

## Identidade: o que é fixo e o que é livre

Fixos: nome **Miolo**; assinatura **"Fornada de sábado, encomendada na sexta."**

Livres e deliberadamente em aberto: paleta, tipografia (fontes do pacote comum ou
do sistema), wordmark tipográfico, grade, escala, composição, ritmo, tratamento e
enquadramento das fotos via CSS, componentes, microinterações e transições discretas.
Não há layout de referência obrigatório. Nenhum símbolo deve imitar marca existente.

## Conteúdo obrigatório

Hero, título: "O pão de sábado começa na sexta."
Texto: "Encomende até sexta, 18h. Retire no sábado entre 8h e 12h, ainda morno."
Ação principal: "Ver a fornada".

Como funciona (três passos, com estas palavras-chave): Escolha até sexta, 18h ·
Assamos na madrugada de sábado · Retire entre 8h e 12h.

| ID | Nome | Categoria | Preço | Unidade | Descrição | Fotos disponíveis |
|---|---|---|---|---|---|---|
| no-cardamomo | Nó de cardamomo | Doce | €2,80 | unidade | Massa enriquecida, enrolada em nó, com açúcar e cardamomo. | 4 fotos de nós de cardamomo |
| muffin-baunilha | Muffin de baunilha | Doce | €2,50 | unidade | Massa simples de baunilha, assada em forminha de papel. | 4 fotos de muffins |
| torta-morango | Torta de morango | Doce | €24,00 | inteira, 8 fatias | Base amanteigada coberta de morangos. | 3 fotos da torta na forma |
| bolo-maca | Bolo de maçã | Doce | €4,20 | fatia | Bolo de maçã com canela. | 2 fotos de fatia **com sorvete** |
| scone-queijo | Scone de queijo | Salgado | €3,00 | unidade | Scone salgado com queijo. | 1 foto |

**Atenção à fidelidade:** a foto do bolo de maçã mostra uma bola de sorvete; o
sorvete **não** acompanha o produto e isso deve ficar claro ao lado da foto ou da
descrição. Não alegar ingredientes, origem, orgânico, artesanal, sem glúten,
benefícios, prazos de validade ou informações nutricionais. Exibir no detalhe de
cada produto: "Informações sobre alérgenos não disponíveis neste protótipo."

Aviso visível no rodapé e na encomenda: "Protótipo demonstrativo. Marca, produtos e
preços fictícios. Nenhuma encomenda é enviada." Informação de fotos: "Fotografias
ilustrativas de terceiros, sob licenças CC0, CC BY 4.0 e CC BY-SA 4.0 (créditos)."
Os créditos completos de `assets/credits.json` devem estar acessíveis numa página
ou painel, com autor, licença e link de cada foto usada.

## Experiências e comportamento obrigatórios

1. Homepage com proposta, como funciona e destaque da fornada.
2. Fornada (catálogo) com os cinco produtos, nomes e preços, e filtro
   "Todos" / "Doces" / "Salgados". "Salgados" deve retornar somente o scone.
3. Página ou rota de detalhe para cada produto: foto, descrição, preço, unidade,
   aviso de alérgenos, seletor de quantidade e "Adicionar à encomenda".
4. Encomenda demonstrativa: nome, preço unitário, quantidade inteira 1–12, subtotal,
   remover item, estado vazio, escolha obrigatória de um entre quatro horários de
   retirada (08:00–09:00, 09:00–10:00, 10:00–11:00, 11:00–12:00) e um botão
   "Revisar encomenda" que mostra um resumo local. Sem envio, pagamento, conta ou
   dados pessoais. Valor nunca negativo ou NaN.
5. Navegação de ida e volta por URL/hash; homepage, fornada e encomenda acessíveis
   em desktop e mobile, sem controles decorativos sem destino.
6. Teclado, foco visível, rótulos acessíveis, texto alternativo e `prefers-reduced-motion`.
7. Nenhuma chamada de rede externa: nada de CDN, analytics ou fontes remotas.

## Instrumentação obrigatória (invisível ao usuário)

Atributos `data-testid` nos elementos funcionais, com apresentação livre:
`nav-home`, `nav-catalog`, `nav-order`, `filter-all`, `filter-sweet`,
`filter-savory`, `product-no-cardamomo`, `product-muffin-baunilha`,
`product-torta-morango`, `product-bolo-maca`, `product-scone-queijo` (links/cartões
que abrem o detalhe), `add-order` (no detalhe), `order-quantity` (input numérico ou
select, um por linha), `order-remove`, `order-subtotal` (contém o valor total),
`order-empty`, `pickup-slot` (radio/select dos horários), `order-review` (botão) e
`order-summary` (resumo exibido após revisar).

Resultado esperado de referência: dois "Nó de cardamomo" = **€5,60**.

## Materiais

- `assets/`: 14 fotografias e `credits.json` com autor, licença, fonte e SHA-256.
  Usar sem alterar pixels; enquadrar via CSS sem distorcer proporções. Não é obrigatório
  usar todas. Não substituir por ilustrações que finjam ser produto.
- `fonts/`: pacote comum de seis famílias OFL locais (`fonts.css`); uso opcional.
- `references/`: pacote comum de referências visuais (capturas e descrições neutras).
