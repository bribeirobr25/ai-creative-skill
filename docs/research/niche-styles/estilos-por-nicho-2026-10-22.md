# Nichos travam o esqueleto e liberam a pele

Em quase todos os nichos analisados, quem decide a conversão é um esqueleto de UI previsível. Ele tem um widget de transação visível já na primeira tela (ligar, agendar, reservar, cotar, doar, comprar), com as provas de confiança encostadas nele. O estilo visual funciona como uma "pele" que pode variar dentro de uma distância que cada setor tolera. A evidência a favor da convenção é forte e coerente. Julgamentos estéticos acontecem em **17–50 ms**, e designs simples e prototípicos vencem ([Google Research](https://research.google/blog/users-love-simple-and-familiar-designs-why-websites-need-to-make-a-great-first-impression/)). Em 2025, maior prototipicidade melhorou de forma significativa a atitude dos usuários em relação a bancos ([IDEAS/RePEc](https://ideas.repec.org/a/spr/elmark/v35y2025i1d10.1007_s12525-025-00777-9.html)). E **52% dos PDPs desktop** de e-commerce ainda são "medíocres" ou piores ([Baymard](https://baymard.com/research-articles/current-state-ecommerce-product-page-ux)). Já a evidência a favor do design distintivo vem de prêmios, cases e opinião de agência. **Não encontramos nenhum dado público de conversão que compare estilos visuais.** A consequência para a skill: a distância do protótipo deve ser pequena em finanças, saúde, jurídico, ofícios de emergência e ONGs, média em hospitalidade, beleza, educação e SaaS, e grande em portfólios, agências, arte contemporânea, festivais e DTC de alimentos, onde o próprio site é amostra do trabalho. O relatório traz **47 cartões** no mesmo formato, organizados em sete famílias. Cada cartão mapeia o protótipo e três direções (segura, expressiva e ousada) nos eixos do catálogo: `aesthetic`, `layout`, `surface`, `motion`, `type` e `color`. A saturação é concreta em três clusters: o "Linear dark" do SaaS, o roxo com orbes da IA e o bento de seis blocos iguais. Construtores de IA tendem a reproduzi-los. Os construtores atuais perguntam o setor e decidem o estilo por um eixo separado de "personalidade", e nenhum publica uma tabela setor→estilo. Os mapeamentos estilo-por-nicho daqui são síntese, quase nenhum exemplo foi aberto ao vivo, várias estatísticas vêm de fornecedores e a cobertura é fortemente EUA/Reino Unido.

## Leia cada cartão com dez campos fixos e cinco marcadores

Todos os cartões seguem a mesma ordem de campos: **Objetivo e conversão**, **Estrutura e mobile**, **Regras de UI/UX com evidência**, **Estilo típico (eixos)**, **Segura · expressiva · ousada**, **Evitar**, **Confiança**, **Imagem** e **Exemplos**. Um décimo campo, **Variantes**, aparece só quando subnichos divergem. As três direções têm definição fixa. **Segura** é a prototípica do nicho. **Expressiva** diferencia sem tocar no esqueleto de conversão. **Ousada** é memorável e sempre vem com a troca declarada. No campo de eixos, os nomes de estilo seguem o catálogo: as 12 estéticas (Minimalist, Swiss, Editorial, Brutalist, Neo-brutalist, Retro, Y2K, Maximalist, Organic, Luxury, Collage, Dark/tech) e as candidatas (Flat/Material, Typographic-led, Illustrative, Scandinavian/Japandi, Wabi-sabi, Art Deco, Memphis, Cyberpunk, Retrofuturism), com Bento como `layout`, Glass/Neu/Clay/aurora/grain como `surface` e Kinetic/Immersive como `motion`.

Os marcadores são cinco:

- **[F]** é um fato com fonte citada na mesma frase. Fica implícito sempre que há citação.
- **[S]** é síntese dos pesquisadores. **Todos os mapeamentos de estilo, as estruturas de página sugeridas e a matriz cruzada são [S], salvo citação explícita.**
- **[NV]** marca um exemplo nomeado por fonte mas não aberto ao vivo nesta pesquisa. **Todo exemplo é [NV] por padrão.** A única página buscada diretamente foi a da BOXT, em outubro de 2026. Os tokens de Graza e Gumroad vêm de extração de terceiros.
- **[O]** é observação de conhecimento prévio dos pesquisadores, sem fonte nesta pesquisa. Precisa ser verificada antes de qualquer uso.
- **[ANT]** marca evidência anterior a 2023. **[VEND]** marca estatística de fornecedor ou de segunda mão sem estudo primário verificável. **[✝]** marca site extinto ou redirecionado, que não deve ser usado.

Todos os cartões herdam o contrato base do catálogo e só registram riscos específicos. O contrato inclui contraste WCAG 2.2 AA de 4.5:1 para texto ([W3C](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)), controle de pausa para qualquer movimento automático acima de 5 s, o que abrange marquees, vídeo em loop e carrosséis ([W3C](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)), honra a `prefers-reduced-motion` ([W3C](https://www.w3.org/WAI/WCAG21/Understanding/animation-from-interactions.html)), alvos de toque de no mínimo 24×24 px (44 px recomendados) e foco que nunca fique escondido sob header sticky ([W3C](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html)).

## A prototipicidade vence a primeira impressão, e ninguém mediu o ganho da diferenciação

A evidência mais sólida sobre convenção é antiga, mas consistente. Tuch et al. (2012) mostraram 119 screenshots reais e viram que complexidade visual e prototipicidade afetavam a nota estética em **50 ms**. Com 17 ms as duas ainda pesavam, mas a prototipicidade pesava menos e crescia com o tempo de exposição. A combinação de **baixa complexidade com alta prototipicidade** foi a mais atraente **[ANT]** ([edoc Unibas](https://edoc.unibas.ch/21676)). O resumo do Google é direto: um site desconhecido foi considerado mais feio mesmo sendo simples, e "designs que contradizem o que os usuários esperam de um site podem prejudicar a primeira impressão" ([Google Research](https://research.google/blog/users-love-simple-and-familiar-designs-why-websites-need-to-make-a-great-first-impression/)). O ponto decisivo para uma skill por nicho é que **a prototipicidade é definida por categoria**. O dataset de Miniukovich & Figl (2023) mediu tipicidade, aderência ao exemplar e semelhança de família em cerca de **3.150 homepages**, separadas em bancos, e-commerce e universidades ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10823051)). O experimento de Figl et al. (2025) com sites de bancos comerciais concluiu que "maior prototipicidade melhora significativamente as atitudes" em relação ao banco, inclusive como empregador. Nesse estudo, prototipicidade engloba navegação, esquema de cor e organização do layout ([CBS](https://research.cbs.dk/da/publications/the-danger-of-not-being-typical-the-positive-effect-of-webpage-pr/)). As correlações entre prototipicidade e confiança do artigo companheiro de 2023 não foram obtidas.

A credibilidade segue a mesma lógica. No estudo de Fogg et al., com 2.684 participantes, o "visual do site" foi o fator mais citado, presente em **46.1%** dos comentários **[ANT]** ([Consumer Reports](https://advocacy.consumerreports.org/research/how-do-people-evaluate-a-web-sites-credibility)). A NN/g resume quatro fatores de confiança: qualidade de design, transparência antecipada (contato, custos), conteúdo completo e atual, e conexão com o resto da web. No mesmo trabalho, usuários confiaram mais em avaliações de terceiros do que em depoimentos publicados no próprio site **[ANT]** ([NN/g](https://nngroup.com/articles/trustworthy-design/)). A Lei de Jakob dá a razão comportamental: as pessoas passam a maior parte do tempo em outros sites e esperam que o seu funcione igual ([NN/g](https://www.nngroup.com/videos/jakobs-law-internet-ux/)). Em e-commerce, isso vira vantagem medida. O Baymard classifica **52% dos PDPs desktop e 62% dos mobile** como "medíocres" ou piores, e **58% das listagens desktop e 78% das mobile** como "ruins" a "medíocres" ([Baymard](https://baymard.com/research-articles/current-state-product-list-and-filtering)). Seguir a convenção bem executada já coloca um site acima da média.

A convergência visual também foi medida. Goree et al. (Indiana, 2020) analisaram cerca de 200 mil imagens arquivadas de 10 mil sites. As diferenças médias de cor e layout atingiram o pico em 2008–2010 e caíram até 2016, e as **diferenças de layout recuaram mais de 30%**. Os sites que usavam bibliotecas compartilhadas, como Bootstrap, ficaram mais parecidos entre si **[ANT]** ([Big Think](https://bigthink.com/technology-innovation/all-websites-look-the-same)). Ninguém replicou a medição na era dos construtores de IA. Mesmo assim, as fontes de 2025–2026 descrevem a saturação em clusters: "quase todo site de SaaS parece igual" ([LogRocket](https://blog.logrocket.com/ux-design/linear-design)), a marca de IA roxa "se desgasta mais rápido" porque IA não tem equivalente físico ([Indie Hackers](https://www.indiehackers.com/post/the-ai-purple-problem-why-every-ai-brand-looks-the-same-6cb0aa2a02)) e o bento se espalhou "sem considerar se servia ao produto" ([BuildMVPFast](https://www.buildmvpfast.com/blog/bento-grid-helps-vs-hurts-conversion-2026)). O problema dos sites gerados por IA que convergem para o mesmo gradiente roxo aparece em fontes que só foram lidas como snippet ([prg.sh](https://scour.ing/@emschwartz/p/https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website)).

O lado da diferenciação tem argumento de marca, mas nenhum número de conversão. Os vencedores da Awwwards em e-commerce de 2024–2026 incluem marcas de comida com sites maximalistas e cheios de movimento ([Awwwards](https://www.awwwards.com/websites/winner_category_ecommerce/)), mas a conversão de sites premiados não é pública. A Numiko elogia o visual "deliberadamente retrô e brutalista" da Nottingham Contemporary como prova de que o não convencional pode ser usável, e isso é opinião de curador ([Numiko](https://numiko.com/insights/best-museum-and-gallery-websites-2026)). Na odontologia, um "conceito de marca único" é citado como superior ao "polimento genérico", mas a frase vem de um listicle de agência ([Krishaweb](https://www.krishaweb.com/blog/best-dental-website-designs/)). Em instituições, os dados apontam para o lado oposto: estilo "gimmicky", com cara de anúncio, fez usuários ignorarem seções, e foto de banco deixou escolas genéricas **[ANT]** ([NN/g](https://www.nngroup.com/articles/university-sites/)). A posição defensável é **"estrutura convencional, pele distintiva"**: manter IA, posição de CTA e padrões de formulário típicos do nicho e deixar a personalidade da marca escolher a distância estilística. Essa distância varia por família:

| Distância tolerada do protótipo **[S]** | Nichos | Alavancas seguras de diferenciação |
|---|---|---|
| **Baixa** (só tipo, cor e foto) | finanças, seguros, jurídico, notários, patrimônio, clínicas, odonto, terapia, ofícios de emergência, ONGs, universidades | uma cor de marca saturada, serif editorial, fotografia dirigida, ilustração própria, movimento sutil |
| **Média** (estética muda, esqueleto fica) | e-commerce de moda/beleza/casa, SaaS, apps, hotéis, restaurantes, imóveis, fitness, salões, contabilidade, educação | Editorial, Organic, Retro, Typographic-led, Kinetic só no headline, Bento com tile âncora |
| **Alta** (o site é a amostra) | portfólios, agências, arte contemporânea, festivais e conferências de design, DTC de alimentos, streetwear, barbearias, criadores indie | Neo-brutalist, Maximalist, Collage, Y2K, Immersive, Brutalist, sempre com o fluxo de compra/contato padrão |

## E-commerce mantém o PDP convencional mesmo sob a casca mais ousada

Os cinco subnichos convertem do mesmo jeito: "adicionar ao carrinho" a partir do PDP. O que muda é a dúvida que a UI precisa resolver antes do clique. Na moda é o caimento, na beleza é o tom, no DTC de alimentos são sabor, quantidade e valor da assinatura, no artesanal é a autenticidade, e na casa são o tamanho físico e a entrega. O esqueleto é comum a todos: hero, tiles de categoria, grade de coleção, prova social e faixa editorial. No PDP desktop, a galeria fica à esquerda e o buy box à direita; no mobile, tudo empilha em galeria com swipe, buy box e acordeões **[S]**. A cesta média é abandonada em **70.22%** dos casos. Os motivos mais citados são custo extra (**40%**), entrega lenta (20%), desconfiança com o cartão (19%), cadastro obrigatório (18%), checkout longo (17%) e custo total escondido (12%). O checkout médio dos EUA tem 14.88 campos, quando o ideal fica em 7–8 ([Baymard](https://baymard.com/lists/cart-abandonment-rate)).

Algumas regras valem para todo e-commerce, qualquer que seja o estilo, e cada uma é violada por uma fatia grande do mercado:

- tamanho e tom em botões ou chips, não em dropdown (57% erram);
- variantes agrupadas no card da listagem, com swatches (42% erram);
- três ou mais miniaturas por item (80% erram);
- barra de filtros aplicados (20% erram);
- os cinco filtros essenciais: preço, avaliação, cor, tamanho e marca (51% erram) ([Baymard](https://baymard.com/research-articles/current-state-product-list-and-filtering));
- política de devolução no conteúdo do PDP, já que 60% dos compradores procuram por ela ali (44% erram);
- estimativa de custo total perto do botão de compra (67% erram) ([Baymard](https://baymard.com/research-articles/current-state-ecommerce-product-page-ux)).

Os sites premiados mantêm PDP e carrinho convencionais sob uma casca expressiva **[S]**. Por isso, nesta família a liberdade estilística vale para home, coleção e campanha, e não para os controles de compra.

### A1. Moda e acessórios

**Objetivo e conversão.** O visitante quer saber se a peça serve. A conversão é escolher o tamanho e adicionar à sacola. As ações secundárias são wishlist e "complete o look". Até 95% dos usuários consultam avaliações antes de comprar, e 90% dos sites de vestuário erram pelo menos um de cinco fundamentos ([Baymard](https://baymard.com/research-articles/apparel-5-best-practices)).

**Estrutura e mobile.** O hero é uma campanha em full-bleed, recortada em 4:5 ou 9:16 no mobile. O mega-menu vai de gênero para categoria e traz um tile editorial. A grade usa 4 colunas no desktop e 2 no mobile, com cards em retrato 2:3 ou 3:4, troca de imagem no hover e swatches sob a foto. No PDP desktop, a galeria empilhada fica à esquerda e o buy box sticky à direita. No mobile, o PDP tem carrossel com swipe, botões de tamanho, link para o guia de medidas, barra sticky de "adicionar" e acordeões de detalhes, tecido e entrega **[S]**.

**Regras de UI/UX com evidência.** Tamanhos devem aparecer como botões com estoque por tamanho. O guia de medidas fica junto ao seletor, em cm e polegadas, com as medidas do modelo. Um subscore agregado de caimento, numa barra de "pequeno" a "grande", funcionou bem nos testes. O carrossel de fotos de clientes deve percorrer todas as avaliações, e 90% dos sites de vestuário não fazem isso. Manequim e modelo virtual foram mal recebidos, e o recorte no fundo branco não mostra caimento ([Baymard](https://baymard.com/research-articles/apparel-5-best-practices)). **42%** dos usuários tentam julgar o tamanho pela foto, e 23% dos sites não têm imagem do produto em uma pessoa ([Baymard](https://baymard.com/research-articles/current-state-ecommerce-product-page-ux)).

**Estilo típico (eixos).** `aesthetic` Minimalist + Swiss · `layout` full-bleed hero + grade densa · `surface` flat · `motion` micro (troca no hover) · `type` grotesk neutra · `color` light, monocromático + um acento para promoções · radius 0–4px · complexidade média, prototipicidade alta **[S]**.

**Segura · expressiva · ousada.** *Segura:* Minimalist/Swiss, fundo branco, grotesk e cantos retos. *Expressiva:* Editorial, com layouts de revista e serif grande na home e no lookbook, mantendo o PDP padrão. *Ousada:* Kinetic typography e Immersive scroll em páginas de drop e campanha, ou Neo-brutalist para marca indie. A troca é performance mais pesada e o risco de esconder o produto, então PDP e carrinho continuam convencionais **[S]**.

**Evitar.** Brutalist cru em moda de luxo, porque parece inacabado para ticket alto. Scroll-jacking ou cursor customizado na listagem e no PDP. Seletores de variante escondidos e CTA com pouco contraste **[S]**.

**Confiança.** Estrelas com contagem sob o título, histograma de notas, barra de caimento, altura e tamanho do modelo, linha "troca fácil" sob o CTA, ícones de pagamento e badges de material e sustentabilidade **[S]**.

**Imagem.** Dominam fotos no modelo e de lifestyle. Acessórios usam packshot em cinza claro ou off-white. A peça nunca deve aparecer só recortada ([Baymard](https://baymard.com/research-articles/apparel-5-best-practices)).

**Exemplos.** Vencedores da Awwwards em e-commerce: Polène (nov. 2024, Luxury/Editorial minimal **[S]**), P448 (SOTD out. 2024), UND NY (SOTD jul. 2024), Hopaal (mai. 2024) e Coutumes (set. 2026). Drop Edition tem nicho não confirmado. A classificação de nicho e de estilo é dos pesquisadores ([Awwwards](https://www.awwwards.com/websites/winner_category_ecommerce/)).

**Variantes.** *Luxo:* Luxury/Editorial, 2–3 colunas, ritmo lento, serif. *Fast fashion:* grade densa de 4–6 colunas, barra promocional, vermelho de liquidação e quick-add. *Streetwear e drops:* Neo-brutalist ou Dark, contagem regressiva e Kinetic. *Sustentável:* Organic/Minimalist com paleta terrosa e blocos de transparência **[S]**.

### A2. Beleza e cosméticos

**Objetivo e conversão.** O visitante quer saber se o tom combina com a pele. A conversão é escolher tom ou tamanho e adicionar à sacola. As ações secundárias são shade finder ou quiz, amostra ou kit, e assinatura para itens de reposição **[S]**.

**Estrutura e mobile.** O hero mostra packshot sobre fundo tingido ou close de modelo, com faixa promocional rotativa. O mega-menu organiza por categoria (pele, maquiagem, cabelo, perfume) e tem um segundo eixo por "preocupação" ou tipo de pele. A grade usa 3–4 colunas no desktop e 2 no mobile, com cards 1:1 ou 4:5, linha de avaliação, contagem de tons e quick-add. No PDP, os tons aparecem como chips redondos com o nome do tom e imagens aplicadas em várias peles. Há acordeões de ingredientes, modo de uso e resultados, slider de antes e depois, cross-sell de "rotina" e toggle de assinatura **[S]**.

**Regras de UI/UX com evidência.** Mostrar preço por unidade quando o produto tem vários tamanhos: 81% dos PDPs e 67% das listagens não mostram ([Baymard](https://baymard.com/research-articles/current-state-ecommerce-product-page-ux)). Imagens em pessoas pesam mais em vestuário, acessórios e cosméticos. As 105 diretrizes de PDP específicas de beleza do Baymard são pagas e não foram verificadas ([Baymard](https://baymard.com/research/health-and-beauty)).

**Estilo típico (eixos).** `aesthetic` Minimalist · `layout` grade + PDP padrão · `surface` flat com gradientes suaves · `motion` médio (zoom no hover, vídeo em loop) · `type` sans limpa com serif elegante pontual · `color` light, pastel ou tons de pele · radius 8–24px **[S]**.

**Segura · expressiva · ousada.** *Segura:* Minimalist pastel. *Expressiva:* Organic para clean beauty, Luxury para prestige, ou renders 3D "jelly" em Claymorphism. *Ousada:* Maximalist ou Y2K para maquiagem colorida voltada à Gen-Z. A troca é hierarquia mais fraca e perda de precisão de cor nos swatches, e glass só entra na navegação **[S]**.

**Evitar.** Dark/tech e Cyberpunk, porque tons de pele e precisão de cor sofrem em UI escura e fundos com dominante de cor distorcem os swatches. Glassmorphism pesado sobre imagem de produto, pela mesma razão **[S]**.

**Confiança.** Tags de tipo de pele e preocupação, badges clean, vegano e cruelty-free, tiles com estatística de resultado clínico, antes e depois, entrada para o shade finder, selos de prêmio e lista completa de ingredientes **[S]**.

**Imagem.** Macro de textura (swatch, esfregaço, gota), renders translúcidos "dewy" e modelos com diversidade de tons de pele **[S]**.

**Exemplos.** Gielly Green, de cabelo, entrou na Awwwards em jan. 2026 ([Awwwards](https://www.awwwards.com/websites/winner_category_ecommerce/)). O benchmark do Baymard inclui Glow Recipe (pastel, vizinho de Clay **[S]**), Ilia (Organic clean **[S]**), Kiehl's, MAC, e.l.f., Sephora, Ulta e Chanel (Luxury **[S]**) ([Baymard](https://baymard.com/research/health-and-beauty)).

**Variantes.** *Varejo de massa:* Flat/Material denso e promocional. *Prestige:* Luxury. *Clean/indie:* Organic, botânico, serif, paleta terrosa. *Cor Gen-Z:* Maximalist, Y2K ou Clay. *Dermocosmético:* Swiss/Minimalist em branco e azul, com iconografia científica **[S]**.

### A3. Alimentos e bebidas DTC

**Objetivo e conversão.** O visitante quer entender sabor, quantidade e o valor da assinatura. A conversão é adicionar um kit ou assinar, com toggle entre compra única e assinatura. As ações secundárias são montar uma caixa, achar uma loja física e comprar no atacado. Muitos compradores voltam para repor **[S]**.

**Estrutura e mobile.** O hero mostra packshot em campo de cor saturada, com display grande e stickers. A navegação é rasa: Shop, Bundles, Subscribe, Recipes, Find in store. A grade é de 3, 2 ou 1 coluna, com cards quadrados e packshot contido. No PDP ficam o toggle com a % economizada, o seletor de tamanho com preço unitário, ícones de ingredientes, acordeão nutricional e uma faixa de receitas **[S]**. Os temas Shopify do nicho trazem quick add, cart drawer, carrinho sticky, barra de frete grátis, escalas de sabor, verificador de idade, localizador de lojas, pré-venda e retirada ([GetSiteControl](https://getsitecontrol.com/blog/shopify-themes-for-food-products/)).

**Regras de UI/UX com evidência.** Mostrar preço por unidade, que 81% dos PDPs omitem. Oferecer opção de presente no PDP, que 78% não oferecem ([Baymard](https://baymard.com/research-articles/current-state-ecommerce-product-page-ux)). Bebida alcoólica exige verificação de idade ([GetSiteControl](https://getsitecontrol.com/blog/shopify-themes-for-food-products/)).

**Estilo típico (eixos).** Graza é o protótipo documentado, com tokens extraídos por terceiros e não oficiais ([WebDesignHot](https://www.webdesignhot.com/design.md/graza/)):

- canvas creme `#f6e6d9`, texto oliva `#3c422e` e CTA chartreuse `#d1e030`;
- GT Alpina Typewriter no display e Apercu nos rótulos;
- botões quase pill de 32px e cards de 20px, com profundidade dada por borda de 2px em vez de sombra, objetos "sticker" e hover saltitante de 150–320ms;
- largura máxima de 1280px, coluna de texto de 720px e grade de 3, 2 ou 1 coluna.

Nos eixos: `aesthetic` Neo-brutalist-lite + Retro + Illustrative · `layout` blocos de cor alternando com seções creme · `surface` flat com borda · `motion` micro saltitante + marquee · `type` display com caráter · `color` vivid, derivada da embalagem **[S]**.

**Segura · expressiva · ousada.** *Segura:* o próprio "DTC sticker", que já é o protótipo entre marcas desafiantes, ou o Minimalist creme dos presets Local e Taste. *Expressiva:* Retro (anos 70, diner), Illustrative e acentos Memphis. *Ousada:* Maximalist com Immersive scroll em 3D, no estilo dos premiados SPYLT, Bored Cow e Bucks Sauce. A troca é peso e demora até chegar ao produto, então o PDP continua convencional **[S]**.

**Evitar.** Neumorphism, porque os controles ficam com pouco contraste. Minimalismo Swiss estéril, que não abre o apetite e se descola da embalagem **[S]**.

**Confiança.** Ícones de certificação (orgânico, vegano, sem glúten, não-OGM), tabela nutricional, faixa de origem, badge de economia na assinatura, "à venda em X lojas" e logos de imprensa **[S]**. Os temas destacam trust badges, imprensa e contador de estoque ([GetSiteControl](https://getsitecontrol.com/blog/shopify-themes-for-food-products/)).

**Imagem.** Packshot em modo "contain" sobre creme, lifestyle em full-bleed "cover", ingredientes ilustrados e paleta guiada pela embalagem ([WebDesignHot](https://www.webdesignhot.com/design.md/graza/)).

**Exemplos.** Graza (graza.co), Bucks Sauce (SOTD jul. 2026), SPYLT (SOTD mar. 2025), Bored Cow (SOTD abr. 2024), Bombon (set. 2025) e Rey Del Istmo (set. 2025). Crescente Sicily tem nicho não confirmado ([Awwwards](https://www.awwwards.com/websites/winner_category_ecommerce/)).

**Variantes.** *Desafiante de bens de consumo:* cor forte, Neo-brutalist/Retro. *Artesanal/gourmet:* Editorial/Organic, sóbrio, serif, foto escura e moody. *Mercado/catálogo grande:* Flat denso, guiado por busca, como os temas Canopy e Cornerstone ([GetSiteControl](https://getsitecontrol.com/blog/shopify-themes-for-food-products/)). *Café, chá e vinho:* Minimalist-Editorial com storytelling de origem e verificação de idade **[S]**.

### A4. Artesanal e pequenos makers

**Objetivo e conversão.** O visitante quer autenticidade e peça única. A conversão é adicionar ao carrinho, muitas vezes de estoque único ou limitado. As ações secundárias são encomenda ou comissão, newsletter de lançamentos e seguir o maker **[S]**.

**Estrutura e mobile.** O hero mostra lifestyle ou processo (mãos, oficina), ou é dividido com a apresentação do maker. A navegação é mínima: Shop, About, Journal, Custom. A grade tem 3 colunas com bastante respiro e fotos em luz natural, 1:1 ou 4:5. No PDP entram macro de detalhe, marcador "peça única / restam X", bloco de materiais e processo, prazo de produção, nota de encomenda e faixa com a história do maker **[S]**.

**Regras de UI/UX com evidência.** Valem as regras gerais de e-commerce. O Baymard não tem vertical de artesanal, e não há dado público sobre os objetivos desse visitante. Ainda assim, 89% dos sites não deixam o visitante salvar itens sem conta, o que pesa em lançamentos de estoque curto ([Baymard](https://baymard.com/research-articles/current-state-ecommerce-product-page-ux)).

**Estilo típico (eixos).** `aesthetic` Organic + Minimalist (ou Scandinavian) · `layout` grade arejada · `surface` papel ou grain leve · `motion` baixo · `type` serif humanista nos títulos, sans no corpo, acento manuscrito · `color` light quente (bege, argila, sálvia) · densidade baixa, quase sempre template de Squarespace ou Shopify **[S]**.

**Segura · expressiva · ousada.** *Segura:* Organic/Minimalist. *Expressiva:* Editorial em formato de diário, Illustrative ou Retro leve. *Ousada:* Collage/scrapbook, que reforça o "feito à mão". A troca é ordem de leitura confusa, peso dos recortes e risco de PDP bagunçado **[S]**.

**Evitar.** Dark/tech, Cyberpunk e Retrofuturism, que contradizem a narrativa artesanal. WebGL ou Immersive pesado, porque estoura a hospedagem de um pequeno maker e ofusca o produto **[S]**.

**Confiança.** Retrato e assinatura do maker, badge "feito à mão em [lugar]", galeria de processo, nota de unicidade, indicador de prazo, formulário direto de contato ou encomenda e contador de lote pequeno **[S]**.

**Imagem.** Luz natural, mãos, oficina e macro de material **[S]**.

**Exemplos.** Nenhum site real foi verificado. Os builders têm templates do nicho: Wix "The Craft Edit" ([Wix](https://www.wix.com/marketplace/template/54d81ab4-d790-4572-9cc6-d74588178a7c)), Dorik "Handmade – Home Decor" ([Dorik](https://fr.dorik.com/template/handmade-home-decor-website-template)) e Pixpa "Manifest" ([Pixpa](https://www.pixpa.com/templates/details/manifest)). Nenhum foi analisado. Os temas Shopify Craft, Studio e Refresh são **[O]**.

**Variantes.** *Maker solo em template:* Minimalist/Organic. *Estúdio orientado a design:* Editorial/Scandinavian. *Perfil de marketplace:* densidade de grade estilo Etsy **[S]**.

### A5. Casa, móveis e decoração

**Objetivo e conversão.** O visitante precisa resolver tamanho, material e entrega de item volumoso. A conversão é escolher material, acabamento e tamanho e adicionar ao carrinho. As ações secundárias são pedir amostras de tecido, consultar a entrega, achar um showroom e salvar num quadro. As jornadas são longas e cheias de retornos. 21% dos compradores dependem de salvar itens, mas 89% dos sites não deixam visitante salvar ([Baymard](https://baymard.com/research-articles/current-state-ecommerce-product-page-ux)).

**Estrutura e mobile.** O hero é uma cena de ambiente em 16:9 ou 3:2. O mega-menu organiza por cômodo e por tipo, com tiles de imagem. A grade tem 3–4 colunas de cards 4:3 ou quadrados, com swatches de acabamento e a linha "envia em X semanas". A galeria do PDP mistura silhueta, ambientes, imagem em escala com dimensões, close de material e 360°. O seletor de tecido usa swatches de imagem, o CTA de amostras grátis fica visível, a estimativa de entrega e montagem fica perto do buy box e o diagrama de dimensões fica ao lado da tabela técnica **[S]**.

**Regras de UI/UX com evidência.** Cada variação de tamanho precisa de uma imagem "Dimensions" com texto legível no mobile sem zoom, ao lado das dimensões em texto. Com dimensões só em texto, quase todos os participantes se perderam e muitos abandonaram ([Baymard](https://baymard.com/research-articles/dimensions-measurements-product-size-image)). 37% dos sites não têm imagem "em escala" ([Baymard](https://baymard.com/research-articles/current-state-ecommerce-product-page-ux)). O Baymard recomenda tirar a prioridade do AR "ver no ambiente" e listar conteúdo e quantidade nos kits. Só os títulos dessas diretrizes são públicos ([Baymard](https://baymard.com/research-articles/furniture-and-home-decor-benchmark-2025)).

**Estilo típico (eixos).** `aesthetic` Scandinavian/Japandi ou Minimalist · `layout` ambiente em full-bleed + grade · `surface` flat · `motion` baixo a médio · `type` sans refinada ou serif elegante · `color` light, neutros quentes (aveia, areia, pedra, nogueira) · radius pequeno **[S]**.

**Segura · expressiva · ousada.** *Segura:* Scandinavian/Minimalist. *Expressiva:* Editorial com histórias de ambiente, ou Bento para a visão de categorias. *Ousada:* Art Deco para vintage e luxo, ou Immersive scroll na coleção-herói. A troca é performance e distância do protótipo calmo **[S]**.

**Evitar.** Y2K e Memphis em móveis mainstream, que destoam do contexto calmo e aspiracional **[S]**.

**Confiança.** Estimador de data de entrega, opções de entrega com montagem, CTA de amostras grátis, garantia, período de teste (colchões, sofás), localizador de showroom, linha de parcelamento e diagrama de dimensões **[S]**. O diagrama aumenta a confiança mesmo de quem entende os termos ([Baymard](https://baymard.com/research-articles/dimensions-measurements-product-size-image)).

**Imagem.** Ambientes amplos, silhueta, close de material e o item em escala ao lado de uma pessoa **[S]**.

**Exemplos.** CANCAN Furnishings (Awwwards, out. 2025) e Monolith NYC (SOTD dez. 2024, nicho não confirmado) ([Awwwards](https://www.awwwards.com/websites/winner_category_ecommerce/)). O benchmark do Baymard inclui Castlery e Article (Scandinavian **[S]**), Perigold (Luxury/Editorial **[S]**), Parachute (Japandi/Organic **[S]**), Caraway e Our Place (DTC em blocos de cor **[S]**), CB2, West Elm, IKEA e Wayfair ([Baymard](https://baymard.com/research/houseware-and-furnishings)).

**Variantes.** *Massa:* Flat, promocional, denso. *DTC de utilidades domésticas:* família de produtos numa cor só, blocos de cor ou Bento, mais perto do DTC de alimentos. *Design/premium:* Japandi/Scandinavian. *Luxo/vintage:* Editorial/Art Deco **[S]**.

## Ofícios locais vendem pelo telefone fixo no topo, não pela estética

Quem procura um encanador geralmente está com pressa, no celular e buscando perto de casa. A ação principal é ligar. Agendar ou cotar vem em segundo lugar, e mensagem por texto ou WhatsApp em terceiro. O estudo Google/Ipsos é velho, mas é o melhor dado disponível: **70%** dos usuários de busca mobile já tinham usado click-to-call, **47%** procurariam outra marca se não houvesse telefone, e em serviços domésticos **66%** se diziam "muito propensos" a ligar **[ANT]** ([Think with Google](https://www.thinkwithgoogle.com/_qs/documents/1454/click-to-call_research-studies_hz2ytgv.pdf)). A outra metade da história é o agendamento online. A WebFX repete, de segunda mão, que quase 70% dos clientes de serviços domésticos agendam online **[VEND]** ([WebFX](https://www.webfx.com/blog/home-services/website-design-handbook/)).

O **esqueleto-base de ofícios** é este **[S]**:

1. Barra utilitária com aviso 24/7 ou oferta, número de licença e telefone.
2. Header sticky com logo, 4–6 itens, link de telefone e CTA preenchido.
3. Hero com H1 que nomeia serviço e cidade, linha de credenciais, dois CTAs (Ligar + Cotar/Agendar), badge de avaliação e foto real da equipe ou da van.
4. Faixa de selos.
5. Grade de serviços.
6. 3–4 diferenciais.
7. Antes e depois.
8. Carrossel de avaliações com logo da plataforma.
9. Processo em 3–4 passos.
10. Preços ou "a partir de".
11. Área atendida com mapa ou chips de cidades.
12. FAQ.
13. Faixa final de CTA.
14. Rodapé com nome, endereço, telefone e horário.

As páginas internas são uma por serviço e uma por cidade, no mesmo template. No mobile, uma barra inferior fixa com 2–3 botões de largura igual resolve a conversão: "Ligar" preenchido, "Cotar" ou "Agendar", e WhatsApp onde ele domina, como no Brasil, em boa parte da Europa, na Índia e na América Latina **[S]**.

A evidência dura é toda de áreas vizinhas. A NN/g recomenda header sticky só quando tem função, alvos de pelo menos 1 cm, texto de cerca de 16pt, fundo opaco e nunca translúcido, e uma proporção conteúdo:chrome perto de 13:1, em vez de 2:1 ([NN/g](https://www.nngroup.com/articles/sticky-headers/)). O Baymard viu 42% dos participantes digitarem o nome completo no campo "Nome", o que favorece um campo único ([Baymard](https://baymard.com/blog/checkout-flow-average-form-fields)). As agências recomendam formulários de 4–5 campos com validação inline ([Redefine Web](https://redefineweb.com/blog/home-service-web-design-best-practices/)). A afirmação de que o telefone no canto superior direito "converte mais" cita um "eye-tracking" sem nome e fica como não verificada. Os templates de marketplace parecem mais "desenhados" que os sites reais de alta conversão, que são mais densos e usam foto da própria van **[S]**.

### B1. Emergência: encanadores, eletricistas, aquecimento/HVAC (e telhados/faz-tudo)

**Objetivo e conversão.** O visitante quer ajuda agora, e a conversão é ligar. A segunda é cotar ou agendar, e a terceira é mensagem ou WhatsApp **[S]**. Os playbooks de HVAC de 2026 pedem caminhos óbvios de "ligar, agendar ou mandar mensagem" e um formulário de cotação no topo das páginas de venda ([Hook Agency](https://hookagency.com/hvac-websites/)).

**Estrutura e mobile.** Usa o esqueleto-base, com barra de emergência e botão de ligar sticky. Os padrões reais vistos em 20 sites de encanamento (ago. 2026) são estes ([UENI](https://ueni.com/blog/plumber-websites/)):

- barra de emergência no topo com botão sticky de "Ligar" (Helpers United, CW Plumbing);
- número da licença numa barra fina acima do menu (Quartz);
- oferta de financiamento na barra e "Monthly Payments" no menu (Platinum);
- telefone e cidade como pílulas clicáveis sob o subtítulo;
- barra escura de contato que agrupa telefone, WhatsApp, formulário e agendamento.

**Regras de UI/UX com evidência.** Seguir as regras de sticky header da NN/g ([NN/g](https://www.nngroup.com/articles/sticky-headers/)). O telefone deve ser um link `tel:` com cara de botão e também aparecer como texto, porque há quem disque de outro aparelho **[S]**. Pop-ups, modais de desconto e bolhas de chat que cobrem a barra inferior são o antipadrão mais comum **[S]**. "Nada sobrepõe o conteúdo" é citado como mérito ([UENI](https://ueni.com/blog/plumber-websites/)). Depois do formulário, uma página de confirmação explica os próximos passos ([Redefine Web](https://redefineweb.com/blog/home-service-web-design-best-practices/)).

**Estilo típico (eixos).** `aesthetic` Flat/Material "corporativo-local" · `layout` hero com foto real + grade de cards de serviço · `surface` flat · `motion` mínimo (fade-up, carrossel de avaliações) · `type` grotesk ou geométrica em bold 700–800 (tipo Montserrat, Poppins, Inter, Barlow), com caixa alta nos botões · `color` light, navy ou azul royal com um acento de segurança (laranja `#F97316`, vermelho `#DC2626` ou amarelo `#FACC15`) só em CTAs e badges · radius 6–12px, CTA em pill · densidade alta, CTA a cada 1–2 seções **[S]**. As paletas observadas confirmam o padrão: navy, cinza e azul na Bob's AC, azul e laranja na Thelen, e o vermelho e branco da Smock descrito como contraste aos "tons frios típicos de HVAC" ([Hook Agency](https://hookagency.com/hvac-websites/)). Vermelho e azul sinalizam aquecimento e refrigeração ([WebFX](https://www.webfx.com/blog/home-services/website-design-handbook/)).

**Segura · expressiva · ousada.** *Segura:* Flat/Material em navy com laranja. *Expressiva:* personagem Illustrative, como os mascotes da Bob's AC ou o urso da Kuma, "legível em tamanho pequeno". Também funciona uma cor única contrária à categoria (Smock) ou a van com letreiro como hero (In-Line) ([UENI](https://ueni.com/blog/plumber-websites/)). *Ousada:* Typographic-led ou Neo-brutalist leve, com bordas grossas, botões robustos e alto contraste, para uma marca desafiante. A troca é que não há exemplo vivo verificado em 2024–26, e contraste e alvos de toque precisam ficar intactos **[S]**.

**Evitar.** Glassmorphism, porque a translucidez sobre foto derruba o contraste do telefone, e a NN/g desaconselha header translúcido ([NN/g](https://www.nngroup.com/articles/sticky-headers/)). Neumorphism, que deixa o "Ligar" sem affordance. Immersive, Kinetic e 3D pesado, que atrasam o CTA para quem tem pressa. Y2K, Memphis e Collage, que parecem pouco sérios para gás e eletricidade. Swiss ou Minimalist sem CTA visível, que parecem site de agência. Foto de banco genérica **[S]**.

**Confiança.** Os componentes vêm de WebFX ([WebFX](https://www.webfx.com/blog/home-services/website-design-handbook/)), Redefine Web e UENI ([UENI](https://ueni.com/blog/plumber-websites/)):

- badge Google ou Trustpilot com estrelas e contagem, no hero e no header;
- faixa de credenciais (licença nº, segurado, bonded, Gas Safe, NICEIC ou Meisterbetrieb);
- logos de associações;
- selo de garantia;
- pílula de disponibilidade ("24/7", "chegada média em 60 min");
- cards da equipe e foto da frota;
- avaliação com serviço e bairro;
- badge de financiamento;
- par antes/depois com legenda.

**Imagem.** O dono ao lado da van, a equipe diante de duas vans, a van com letreiro como hero ou uma interação real com cliente ([UENI](https://ueni.com/blog/plumber-websites/)). Todas as fontes de agência recomendam foto real, mas nenhuma dá números ([Redefine Web](https://redefineweb.com/blog/home-service-web-design-best-practices/)).

**Exemplos.** Jacobs Heating (protótipo de HVAC), Thelen Mechanical (azul e laranja), Genz-Ryan (agendamento em todas as páginas) e Bob's AC (mascotes) ([Hook Agency](https://hookagency.com/hvac-websites/)). O rebrand da J Blanton Plumbing (jan. 2025) usou um "sistema de cor ousado" e o personagem "J", porque chamadas de encanador acontecem em momentos de estresse. A fonte não diz cores nem fontes ([Reel Chicago](https://reelchicago.com/article/j-blanton-plumbing-partners-with-geletka-in-a-bold-new-brand-identity/)).

**Variantes.** *Telhados e faz-tudo:* mesma família, mais escura e industrial, com carvão e amarelo ou laranja de segurança, sans condensada e CTAs Ligar + Cotar. Nenhuma fonte trata telhados especificamente, então é inferência **[S]**. *Empresa familiar antiga:* Retro de tradição, com logo em brasão ou escudo, script com sans condensada, creme com vermelho e navy e van ilustrada **[S]**.

### B2. Pintores e decoradores

**Objetivo e conversão.** O visitante quer ver resultado e pedir orçamento. A conversão é cotar **[S]**.

**Estrutura e mobile.** Usa o esqueleto-base com peso maior na galeria de antes e depois, organizada por tipo de serviço ([WebFX](https://www.webfx.com/blog/home-services/website-design-handbook/)), e um formulário de orçamento com cômodos ou m² e prazo **[S]**.

**Regras de UI/UX com evidência.** Nenhuma fonte trata o design de sites de pintura. Valem as regras gerais de formulários curtos e de prova acima da dobra ([Redefine Web](https://redefineweb.com/blog/home-service-web-design-best-practices/)). Também não há evidência comparando slider arrastável com pares lado a lado.

**Estilo típico (eixos).** `aesthetic` Flat/Material mais leve · `layout` grade de projetos · `surface` flat · `motion` mínimo · `type` grotesk · `color` light com acentos de swatch de cor **[S]**.

**Segura · expressiva · ousada.** *Segura:* Flat leve. *Expressiva:* Editorial, com projeto em destaque e paleta de amostras de tinta. *Ousada:* Neo-brutalist em blocos de cor saturada. A troca é parecer marca de tinta, e não prestador local **[S]**.

**Evitar.** Glass, Neumorphism e Immersive, pelas mesmas razões de B1 **[S]**.

**Confiança.** Badge de avaliação, garantia de acabamento, seguro e antes/depois com legenda do serviço **[S]**.

**Imagem.** Antes e depois reais, com o mesmo enquadramento **[S]**.

**Exemplos.** Nenhum verificado (lacuna).

### B3. Limpeza residencial e comercial

**Objetivo e conversão.** O cliente quer um serviço recorrente, e a conversão é agendar. Os exemplos incluem CEP dentro do CTA de agendamento (Midtown Chimney Sweeps), chat ao vivo (King of Maids) e estimativa instantânea (Maid First) ([htmlburger](https://htmlburger.com/blog/cleaning-websites-examples/)).

**Estrutura e mobile.** Usa o esqueleto-base com pacotes ou planos e toggle de frequência **[S]**. Os templates Wix do nicho já trazem agendamento e "planos de assinatura" ([Wix](https://www.wix.com/website/templates/html/industrial/services-maintenance/2)).

**Regras de UI/UX com evidência.** O primeiro passo deve ser de baixo esforço, como tipo de serviço ou CEP, e não nome e e-mail **[S]**. A tese de que formulários em etapas "convertem até 300% mais" vem de quem vende a ferramenta e usa dados de 2014–2016 sem tamanho de amostra **[VEND][ANT]** ([Venture Harbour](https://ventureharbour.com/multi-step-lead-forms-get-300-conversions/)).

**Estilo típico (eixos).** `aesthetic` Flat amigável · `layout` cards arredondados · `surface` flat · `motion` sutil · `type` sans arredondada · `color` light, azul claro, teal ou verde, com acento laranja ou pastel ([htmlburger](https://htmlburger.com/blog/cleaning-websites-examples/)) **[S]**.

**Segura · expressiva · ousada.** *Segura:* Flat amigável. *Expressiva:* Illustrative com containers arredondados e animação sutil, como a More Hands, vizinha do Claymorphism. *Ousada:* uma marca-personagem como a Men In Kilts, com fotos da equipe de kilt e cores casadas com a imagem. A troca é que isso depende de um conceito de marca real e não se gera do nada **[S]**.

**Evitar.** Dark/tech, porque luz e "limpo" importam. Glass e pop-ups sobre o CTA **[S]**.

**Confiança.** Avaliações Google, trust badges, garantia de satisfação e ícones próprios ([htmlburger](https://htmlburger.com/blog/cleaning-websites-examples/)).

**Imagem.** Equipe real e ambientes claros. Ilustração em marcas amigáveis **[S]**.

**Exemplos.** Men In Kilts, Luxe Cleaning Co (Luxury/Minimal), More Hands, Molly Maid (branco com pastel), Pretty Cleaning Services, A Pristine Carpet Clean (AU) e Height Cleaning (NZ) ([htmlburger](https://htmlburger.com/blog/cleaning-websites-examples/)).

**Variantes.** *Padrão:* Flat amigável. *Eco:* Organic/Scandinavian em sálvia e creme. A fonte só cita eco como tendência, sem exemplo. *Luxo:* Minimalist/Luxury, com imóveis de alto padrão, vídeo e sans espaçada **[S]**.

### B4. Jardinagem e paisagismo

**Objetivo e conversão.** Na manutenção, o cliente quer planos e agendamento. No paisagismo de design, quer pedir uma consulta depois de ver o portfólio **[S]**. A The Grounds Guys usa um botão de "estimativa rápida" ([WebFX](https://www.webfx.com/blog/home-services/website-design-handbook/)).

**Estrutura e mobile.** No design premium, a estrutura é ([idstudio](https://idstudio.co.uk/insights/web-design/landscape-garden-web-design/)):

- layout de vitrine em que o trabalho é o foco, com drone, time-lapse e imagem de página inteira;
- antes e depois lado a lado;
- páginas de projeto com objetivo, estilo, desafios, área, orçamento, prazo e depoimento;
- estimador de preço, tour 360° e agendamento como opcionais.

**Regras de UI/UX com evidência.** Fotografia profissional é o que tem mais impacto, e prêmios como BALI e TrustMark devem aparecer com destaque ([idstudio](https://idstudio.co.uk/insights/web-design/landscape-garden-web-design/)).

**Estilo típico (eixos).** *Manutenção:* `aesthetic` Flat · `color` verde fresco, como o template Wix "fresh, green" ([Wix](https://www.wix.com/website/templates/html/industrial/services-maintenance/2)). *Design:* `aesthetic` Organic/Editorial · `layout` full-bleed · `type` serif elegante para tradição ou sans moderna para contemporâneo · `color` tirada da paisagem, com verdes suaves e marrons terrosos ([idstudio](https://idstudio.co.uk/insights/web-design/landscape-garden-web-design/)).

**Segura · expressiva · ousada.** *Segura:* Flat verde para manutenção, ou Organic minimal para design. *Expressiva:* Editorial/Luxury, com full-bleed e serif. *Ousada:* Immersive scroll com drone e time-lapse. A troca é o peso do vídeo no celular e a consulta empurrada para baixo **[S]**.

**Evitar.** Glass sobre foto e foto de banco **[S]**.

**Confiança.** Selos de prêmio e associação, estudos de caso com orçamento e prazo, e depoimentos ([idstudio](https://idstudio.co.uk/insights/web-design/landscape-garden-web-design/)).

**Imagem.** Fotografia profissional, drone, mudança de estação **[S]**.

**Exemplos.** Rosebank Landscaping (Organic/Minimal) e Kinross House (Luxury/Editorial de tradição), ambos cases da idstudio ([idstudio](https://idstudio.co.uk/insights/web-design/landscape-garden-web-design/)).

### B5. Mudanças

**Objetivo e conversão.** O visitante quer uma cotação, idealmente em etapas: cômodos, origem e destino, data **[S]**.

**Estrutura e mobile.** Usa o esqueleto-base com uma calculadora de cotação em várias etapas no hero, cuja primeira etapa é um toque (tamanho do imóvel) **[S]**.

**Regras de UI/UX com evidência.** Não há fonte de design para mudanças. A evidência de formulário em etapas é de fornecedor e antiga **[VEND][ANT]** ([Venture Harbour](https://ventureharbour.com/multi-step-lead-forms-get-300-conversions/)).

**Estilo típico (eixos).** `aesthetic` Flat · `type` grotesk bold · `color` uma cor de marca saturada **[S]**.

**Segura · expressiva · ousada.** *Segura:* Flat com calculadora. *Expressiva:* marca desafiante com cor única, tipografia grande e ilustração flat. *Ousada:* Neo-brutalist. A troca é a confiança de quem vai entregar os próprios bens **[S]**.

**Evitar.** Immersive e Kinetic, que atrasam a cotação **[S]**.

**Confiança.** Seguro de carga, avaliações, preço fixo e frota real **[S]**.

**Imagem.** Equipe e caminhões reais **[S]**.

**Exemplos.** Nenhum verificado. O getbellhop.com, antes uma marca de mudança conhecida pelo visual ousado, redireciona hoje para uma página de domínio à venda **[✝]**.

### B6. Oficinas mecânicas

**Objetivo e conversão.** A conversão é agendar, com telefone e agendamento acima da dobra, muitas vezes repetidos no menu ([FreshySites](https://freshysites.com/blog/top-auto-repair-websites/)).

**Estrutura e mobile.** Usa o esqueleto-base, mais estes padrões ([FreshySites](https://freshysites.com/blog/top-auto-repair-websites/)):

- blocos de cupom para os serviços mais pedidos (Barkley Tire);
- formulário sobre foto da oficina em escala de cinza (Galson);
- cards de unidade no hero para redes (Community Tire Pros);
- cotação por mensagem de texto para mecânico móvel (Bumper Buddies).

**Regras de UI/UX com evidência.** Garantias e orçamento grátis acima da dobra (Pioneer). Certificações e anos de casa em destaque (Galson) ([FreshySites](https://freshysites.com/blog/top-auto-repair-websites/)).

**Estilo típico (eixos).** `aesthetic` Flat/Material de alto contraste · `type` sans condensada · `color` vermelho, preto, azul, laranja e amarelo, com preto/branco/vermelho recorrente e alguns heróis escuros ([FreshySites](https://freshysites.com/blog/top-auto-repair-websites/)).

**Segura · expressiva · ousada.** *Segura:* Flat em vermelho e preto. *Expressiva:* Illustrative familiar, como o banner de bairro ilustrado com fita teal da Christian Brothers, ou verde para especialista em híbridos (Savage Hybrid). *Ousada:* Dark/Luxury para performance e premium (West Coast Tire Pros) ou Retro para restauração de clássicos (Cathedral Automotive). A troca é que Dark só convence no segmento premium ([FreshySites](https://freshysites.com/blog/top-auto-repair-websites/)).

**Evitar.** Minimalist sem CTA e glass sobre foto de carro **[S]**.

**Confiança.** Badge ASE, avaliações Google embutidas no design (Eliot's), certificações e garantias ([FreshySites](https://freshysites.com/blog/top-auto-repair-websites/)).

**Imagem.** Fachada, carros no elevador e técnicos ([FreshySites](https://freshysites.com/blog/top-auto-repair-websites/)).

**Exemplos.** Cathedral Automotive (Retro), West Coast Tire Pros (Dark premium) e Christian Brothers Automotive (Illustrative) ([FreshySites](https://freshysites.com/blog/top-auto-repair-websites/)).

**Variantes.** *Mainstream:* Flat de alto contraste com Agendar. *Clássicos e performance:* Retro ou Dark/Luxury com Contato **[S]**.

### B7. Instaladores produtizados: caldeiras, solar, bombas de calor

**Objetivo e conversão.** O visitante quer um preço fixo sem visita técnica. A conversão é entrar no funil de cotação **[S]**.

**Estrutura e mobile.** A página da BOXT foi buscada em outubro de 2026 e é o único exemplo verificado diretamente ([BOXT](https://www.boxt.co.uk/)):

- hero "Get a fixed price in minutes", com o CTA principal levando a um app de cotação em etapas e o secundário "falar com vendas";
- mega-menu por produto, com botão de cotação e preço inicial em cada coluna;
- cards "Installed from £X" com dois CTAs;
- "How it works" em 3 passos numerados.

**Regras de UI/UX com evidência.** Funciona como e-commerce. Mostrar preço "a partir de" e o custo total cedo segue a lógica que o Baymard mede no varejo ([Baymard](https://baymard.com/lists/cart-abandonment-rate)).

**Estilo típico (eixos).** `aesthetic` Flat em grade de cards de e-commerce · `layout` cards de produto · `type` grotesk bold · `color` uma cor de marca saturada **[S]**.

**Segura · expressiva · ousada.** *Segura:* grade de e-commerce. *Expressiva:* marca desafiante com tipo grande e ilustração flat ou personagens 3D. *Ousada:* Clay ou 3D lúdico. A troca é parecer startup de consumo num serviço regulado de gás **[S]**.

**Evitar.** Esconder o preço atrás de formulário **[S]**.

**Confiança.** Trustpilot, "UK's most trusted", promessa de cobrir orçamento equivalente em £50, logos Gas Safe e Refcom, aviso FCA de financiamento no rodapé e bullets de garantia no hero ([BOXT](https://www.boxt.co.uk/)).

**Imagem.** Produto em packshot e instalador real **[S]**. O template Wix de solar usa "imagens grandes e vívidas" ([Wix](https://www.wix.com/website/templates/html/industrial/services-maintenance/2)).

**Exemplos.** BOXT (verificado em out. 2026).

## Produtos digitais saturaram o visual Linear e o roxo, mas não o esqueleto

Cada nicho digital tem um CTA dominante, e a página deve girar em torno dele. No SaaS é "Comece grátis", com "Agende uma demo" como secundário. Na IA é "Experimente", muitas vezes uma caixa de prompt no próprio hero. Em apps é o download, com badges das lojas e QR code. Em cursos é a matrícula numa página de vendas sem navegação. Em bens digitais é comprar e baixar. Em agências é "Começar um projeto", depois que o visitante viu os trabalhos. SaaS e IA convergem para o mesmo esqueleto: hero tipográfico centralizado com screenshot ou vídeo da UI, parede de logos, seções bento ou alternadas, métricas e depoimentos, preços em 3–4 planos com tabela comparativa, FAQ, faixa final de CTA e mega-rodapé **[S]**. A evidência mais forte é a da NN/g sobre transparência em B2B, e ela vale para todo o grupo ([NN/g](https://www.nngroup.com/articles/b2b-trust-from-b2c/)):

- compradores B2B esperam usabilidade de B2C;
- temem vendedores insistentes e querem informação suficiente para montar a lista curta sem falar com vendas;
- trial sem cartão;
- e-mail e telefone visíveis;
- formulário que explique por que pede cada campo.

As galerias de referência confirmam o minimalismo como linha de base. A Lapa Ninja tem **7.511** páginas, e a tag "Minimal" aparece em **3.051** delas, cerca de 41%. "Gradient" tem 464, "Retro Style" 102, "Bento Grid" 75 e "Course" só 39 ([Lapa Ninja](https://www.lapa.ninja/)). O problema do grupo é a saturação. Há marcadores genéricos que, combinados, fazem um site parecer template **[S]**:

- fundo quase preto com brilho radial roxo ou azul atrás do hero;
- badge em pill de anúncio acima do H1;
- H1 com texto em gradiente;
- só Inter ou Geist;
- marquee de logos em cinza;
- bento de seis blocos iguais;
- ícone ✦ de IA;
- cards de vidro;
- três planos com fita roxa de "Popular".

### C1. SaaS e software B2B

**Objetivo e conversão.** No PLG, a conversão é "Comece grátis" com "Fale com vendas" em ghost button. No enterprise, "Agende uma demo" é a principal **[S]**. Screenshots, vídeos e demos ao vivo ajudam quem não pode instalar software sem aprovação ([NN/g](https://www.nngroup.com/articles/b2b-trust-from-b2c/)).

**Estrutura e mobile.** O menu traz Produto ▾, Soluções ▾, Preços, Docs, Clientes, Login e o CTA. O hero tem H1 de até 10 palavras, dois CTAs e a UI real. Depois vêm logos, 3 propostas de valor, bento com um tile âncora grande, deep-dives alternados, integrações, métricas, cases, faixa de segurança, preços, FAQ, CTA e mega-rodapé com changelog, docs e status. As docs usam três colunas com busca ⌘K **[S][O]**. No mobile, a tabela comparativa vira acordeão por plano ou seletor com swipe, e páginas longas ganham barra inferior de CTA **[S]**.

**Regras de UI/UX com evidência.** Esconder preço acrescenta um passo, faz o produto parecer caro e a empresa parecer que esconde algo ([NN/g](https://www.nngroup.com/articles/b2b-trust-from-b2c/)). Quando não dá para cravar o preço, mostre exemplos de cenários típicos e deixe o configurador como opção **[ANT]** ([NN/g](https://www.nngroup.com/articles/show-prices-for-common-scenarios/)). Tabelas comparativas pedem ícones claros de ✓ e ✗, sem texto apagado para recurso indisponível ([NN/g](https://www.nngroup.com/articles/b2b-trust-from-b2c/)). As convenções de página de preços chegam com números que circulam, mas a própria fonte trata como "direcionais" e de segunda mão **[VEND]** ([m3ter](https://www.m3ter.com/blog/15-data-driven-pricing-page-optimizations)):

- destacar o plano "Mais popular": +16–30%;
- limitar a 3–4 planos: +15–25%;
- toggle já em anual: +20–30%.

O bento atrapalha quando fica acima da dobra, quando os tiles têm o mesmo tamanho, quando cada tile tem CTA próprio ou quando vira coluna longa no mobile. Isso é opinião sem A/B ([BuildMVPFast](https://www.buildmvpfast.com/blog/bento-grid-helps-vs-hurts-conversion-2026)). O dark mode estilo Linear é "mais escolha estética do que vantagem provada" ([LogRocket](https://blog.logrocket.com/ux-design/linear-design)). Uma UI densa, guiada por teclado, serve a devs e PMs e não deve ser copiada para outros públicos ([925studios](https://www.925studios.co/blog/linear-design-breakdown-saas-ui-2026)).

**Estilo típico (eixos).** `aesthetic` Minimalist + Dark/tech ("Linear/Vercel") ou a variante clara "shadcn/Tailwind" (Flat) · `layout` hero centralizado + bento abaixo + seções alternadas · `surface` aurora/gradient glow, fundo com grid de linhas, glass sutil · `motion` micro + scroll-reveal · `type` grotesk (Inter/Geist) · `color` dark ou zinc claro, cor reservada para status, um acento (muitas vezes roxo), escala de 4px ([925studios](https://www.925studios.co/blog/linear-design-breakdown-saas-ui-2026)). O rótulo "shadcn/Tailwind" é dos pesquisadores: branco, cinzas zinc, bordas de 1px, cards de 8–12px de radius e badges em pill **[S]**.

**Segura · expressiva · ousada.** *Segura:* Minimalist claro estilo shadcn, com UI real e bento de tile âncora. *Expressiva:* uma única cor de marca saturada, sem gradiente. A Raycast manteve a cor, abandonou o gradiente e ganhou identidade ([LogRocket](https://blog.logrocket.com/ux-design/linear-design)). Outra saída é o Editorial claro com o gradiente transformado em arte de marca, como a onda da Stripe **[O]**. *Ousada:* Illustrative + Retro, como o desktop de sistema operacional com mascote ouriço da PostHog **[O]**, ou Neo-brutalist. A troca é parecer menos "enterprise", o que exige um comprador tolerante **[S]**.

**Evitar.** Neumorphism, Claymorphism, Maximalist e Cyberpunk, porque prejudicam a legibilidade para o comprador B2B **[S]**. Somar os marcadores genéricos: o GitHub de 2025 ganhou mais cor e glassmorphism "e ficou pior por isso" ([LogRocket](https://blog.logrocket.com/ux-design/linear-design)).

**Confiança.** Depoimentos com nome, cargo e empresa, de preferência no arco "dúvida → confiança". Cases de setores variados. Escritórios, equipe e valores visíveis ([NN/g](https://www.nngroup.com/articles/b2b-trust-from-b2c/)). Parede de 5–8 logos monocromáticos com rótulo. Faixa de métricas com algarismos tabulares. Faixa de segurança (SOC 2, ISO 27001, GDPR, HIPAA) com link para um Trust Center **[S]**. Não há evidência da NN/g sobre paredes de logos.

**Imagem.** UI real em moldura de navegador ou vídeo. Arte abstrata só como assinatura de marca **[S]**.

**Exemplos.** Linear, Raycast, GitHub, Stripe e Wise são citados como exemplares do estilo Linear ([LogRocket](https://blog.logrocket.com/ux-design/linear-design)). Vercel, Stripe, Ramp e Notion adotaram bento em 2023–24 ([BuildMVPFast](https://www.buildmvpfast.com/blog/bento-grid-helps-vs-hurts-conversion-2026)). Attio, PostHog e Resend são **[O]**.

### C2. Ferramentas de IA e startups de IA

**Objetivo e conversão.** O visitante quer experimentar, e o input é o hero. Lovable, bolt.new e v0 usam a caixa de prompt como elemento principal **[O]**. Outras opções são demo interativa, player de áudio, slider de antes e depois ou galeria de resultados **[S]**.

**Estrutura e mobile.** Esqueleto de SaaS, mais prompt ou demo no hero, bloco de comparação de modelos e benchmarks, abas de API com trechos de código e preço por uso ou créditos **[S]**.

**Regras de UI/UX com evidência.** Comentaristas recomendam mostrar output e fluxo reais em vez de visual abstrato. Um deles diz que a SocialPost.ai converteu melhor depois da troca, o que é anedota. Outro sugere um teste de recordação de cinco segundos: esconder o hero e perguntar se as pessoas sabem dizer o que o produto faz ([Indie Hackers](https://www.indiehackers.com/post/the-ai-purple-problem-why-every-ai-brand-looks-the-same-6cb0aa2a02)).

**Estilo típico (eixos).** `aesthetic` Dark/tech · `surface` aurora/gradiente roxo-azul, orbes, brilho, blur, glass · `motion` "digitação" cinética nas demos · `layout` bento · `type` grotesk · `color` dark com roxo entre o azul de "confiança" e o rosa de "energia". Gemini, Microsoft 365 Copilot e os materiais de negócio da OpenAI são citados ([Indie Hackers](https://www.indiehackers.com/post/the-ai-purple-problem-why-every-ai-brand-looks-the-same-6cb0aa2a02)).

**Segura · expressiva · ousada.** *Segura:* o protótipo Dark/tech, mas com o gradiente contido e output real no hero em vez de orbes. *Expressiva:* Minimalist claro com demo interativa, como o áudio da ElevenLabs **[O]**, ou Editorial/Organic quente, com creme, serif e ilustração à mão, numa linha anti-roxo como a da Anthropic **[O]**. Também serve o Typographic-led monocromático. *Ousada:* Retrofuturism ou pixel em gradiente laranja, como a Mistral **[O]**. A troca é parecer menos "tech" e a legibilidade de fontes pixel **[S]**. A fonte recomenda fundo claro, calor, especificidade e linguagem simples ([Indie Hackers](https://www.indiehackers.com/post/the-ai-purple-problem-why-every-ai-brand-looks-the-same-6cb0aa2a02)).

**Evitar.** O clichê de orbe roxo com ícone ✦, robôs e glass sobre o output **[S]**. A marca de IA roxa "se desgasta mais rápido" ([Indie Hackers](https://www.indiehackers.com/post/the-ai-purple-problem-why-every-ai-brand-looks-the-same-6cb0aa2a02)).

**Confiança.** Faixa de segurança, benchmarks, galeria de outputs, documentação de API e logos de clientes **[S]**.

**Imagem.** Outputs reais e screenshots de fluxo **[S]**.

**Exemplos.** Gemini, Copilot e OpenAI aparecem citados pelo gradiente ([Indie Hackers](https://www.indiehackers.com/post/the-ai-purple-problem-why-every-ai-brand-looks-the-same-6cb0aa2a02)). Anthropic/Claude, OpenAI (site), Lovable, Cursor, ElevenLabs, Mistral, Runway e Perplexity são todos **[O]**.

### C3. Apps móveis (landing pages de app)

**Objetivo e conversão.** A conversão é o download: badges das lojas mais QR code no desktop e, no Safari do iOS, o Smart App Banner nativo em vez de intersticial próprio. A documentação da Apple não pôde ser lida **[O]**.

**Estrutura e mobile.** Uma contagem promocional de 15 páginas de app achou CTA acima da dobra em 15/15 e mockup de dispositivo em 14/15. A mesma fonte afirma, sem dar fonte, que 5–10% de visita→download é "a média" **[VEND]** ([The Swift Kit](https://theswiftk.it.com/blog/best-app-landing-page-examples-2026)). Os tipos de hero vistos são:

- ilustração com mockup (Headspace);
- mascote com mockup (Duolingo);
- dados ao vivo no fundo (Flighty);
- foto em full-bleed feita com o app (Halide);
- screenshot anotado (Things 3);
- vídeo mudo de 10–15 s (Loom).

A pilha sugerida é hero com badges, faixa de nota e downloads, 3–5 recursos com screenshot, widgets, avaliações da loja, plano Pro e badges repetidos no fim **[S]**.

**Regras de UI/UX com evidência.** Vídeo de hero mudo, com legenda e menos de 3 MB. O "~2× de conversão" atribuído a ele não tem fonte **[VEND]** ([The Swift Kit](https://theswiftk.it.com/blog/best-app-landing-page-examples-2026)).

**Estilo típico (eixos).** `aesthetic` Flat/Material limpo · `layout` mockups de dispositivo · `surface` gradientes suaves · `motion` baixo · `type` grotesk · `color` light. Apps de consumo puxam para Illustrative ou mascote, e ferramentas pro para Dark com render 3D do dispositivo, como a Fantastical ([The Swift Kit](https://theswiftk.it.com/blog/best-app-landing-page-examples-2026)).

**Segura · expressiva · ousada.** *Segura:* Flat com mockup. *Expressiva:* produto como hero (dados ao vivo da Flighty, foto real da Halide) ou Illustrative com mascote. *Ousada:* Claymorphism ou ícones 3D para público infantil e fintech amigável, ou Y2K para social Gen-Z. A troca é contraste e peso **[S]**.

**Evitar.** Immersive scroll pesado que empurra os badges para baixo. Brutalist **[S]**.

**Confiança.** "65 milhões de usuários" sob o hero (Headspace), "Apple Design Award" (Flighty), certificações antes dos screenshots (1Password), galeria de telas iniciais de usuários (Widgetsmith) e "Shot on Halide" ([The Swift Kit](https://theswiftk.it.com/blog/best-app-landing-page-examples-2026)).

**Imagem.** Screenshots reais em mockup, ou o output do app em full-bleed **[S]**.

**Exemplos.** Flighty, Things 3, Headspace, Duolingo, Fantastical, Halide e 1Password ([The Swift Kit](https://theswiftk.it.com/blog/best-app-landing-page-examples-2026)). Opal é **[O]**. O Apollo for Reddit aparece na lista mas fechou em 2023 **[✝]**.

### C4. Cursos online, coaches e negócios de criadores

**Objetivo e conversão.** A conversão é matricular ou comprar. A página de vendas não deve ter navegação, e "o único link deve levar ao checkout". Texto curto, abaixo de 500 palavras, serve para público que já conhece o criador ou curso simples. Texto longo serve para curso complexo ou premium ([Kajabi](https://www.kajabi.com/blog/how-to-create-an-amazing-sales-page-today)).

**Estrutura e mobile.** A ordem do Kajabi é promessa, bullets de benefício, vídeo, história, dados de credibilidade, depoimentos com nome e foto, prova de resultado, oferta com ancoragem de valor, garantia, CTA e bio do instrutor ([Kajabi](https://www.kajabi.com/blog/how-to-create-an-amazing-sales-page-today)). A síntese acrescenta o que o Kajabi não cobre: bloco "é para você / não é para você", currículo em acordeão (módulos → aulas → duração), bônus, planos com parcelamento, FAQ e barra sticky de "Matricular" no mobile **[S]**.

**Regras de UI/UX com evidência.** Depoimentos com nome e foto, de preferência em vídeo. Janela de garantia longa o bastante para experimentar e curta demais para terminar o curso ([Kajabi](https://www.kajabi.com/blog/how-to-create-an-amazing-sales-page-today)). Num teste atribuído ao Basecamp, tirar a navegação da página de preços teria dado +11–20% no checkout. O dado é de segunda mão **[VEND]** ([m3ter](https://www.m3ter.com/blog/15-data-driven-pricing-page-optimizations)).

**Estilo típico (eixos).** `aesthetic` Minimalist pessoal e quente, ou Organic · `layout` coluna narrativa única · `surface` flat, pastel "tipo Notion" · `motion` baixo · `type` sans quente com serif pontual · `color` light pastel · retrato grande do instrutor **[S]**. Essa linha vem de observação: nenhuma fonte documenta o estilo visual de cursos.

**Segura · expressiva · ousada.** *Segura:* Minimalist quente com o rosto em destaque. *Expressiva:* Editorial com serif para coaches premium, ou Illustrative com rabiscos. *Ousada:* Dark/Luxury cinematográfico como o MasterClass **[O]**, Neo-brutalist indie ou Collage/Retro para professores de artes. A troca é parecer produção cara ou nichada demais **[S]**.

**Evitar.** O visual Dark/tech de SaaS, que fica impessoal, e Cyberpunk **[S]**. Scroll-jacking que atrasa o CTA.

**Confiança.** Colagem de prints de DMs e resultados, grade de vídeo-depoimentos, selo de garantia, números de credibilidade e bio do instrutor ([Kajabi](https://www.kajabi.com/blog/how-to-create-an-amazing-sales-page-today)).

**Imagem.** Rosto do criador e prints reais de resultados **[S]**.

**Exemplos.** MasterClass, Maven, Domestika, aliabdaal.com, justinwelsh.me e Coursera, todos **[O]**. O buildspace.so, referência de criador neo-brutal e retrô, fechou em 2024 **[✝][O]**. A maior parte desse design é feita dentro de plataformas como Kajabi, Teachable, Podia e Stan, o que explica a pouca presença em galerias **[S]**.

### C5. Downloads digitais, templates e marketplaces de bens digitais

**Objetivo e conversão.** A conversão é comprar e baixar. O botão mostra o preço, pode haver campo de "pague quanto quiser", e o checkout é em overlay ou página única, começando pelo e-mail, com Apple Pay, Google Pay ou Link e entrega instantânea **[S]**.

**Estrutura e mobile.** *Criador solo:* capa grande ou galeria de prévia (ou demo ao vivo), lista "o que vem incluído" (formatos, páginas, compatibilidade com Figma, Notion ou Framer), preço com botão sticky no mobile, licença pessoal ou comercial, avaliações, card do criador e produtos relacionados. *Marketplace:* header com busca, chips de categoria, grade de cards (miniatura, título, criador, preço, nota) e filtros laterais **[S]**.

**Regras de UI/UX com evidência.** Não há dado primário sobre checkout em overlay versus redirecionamento (lacuna).

**Estilo típico (eixos).** `aesthetic` Minimalist em grade de marketplace · `layout` grade de cards. A assinatura do criador indie é o Neo-brutalist do Gumroad ([webdesignhot](https://www.webdesignhot.com/api/design-md/gumroad.md)):

- canvas creme `#f4f4f0` e cards brancos;
- rosa `#ff90e8`;
- borda preta de 1px em quase tudo e sombra dura deslocada de 4px, sem blur;
- preço em monoespaçada tabular;
- radius de 8px nos botões e 12px nos cards.

O catálogo anterior já registrou que o Gumroad aparece hoje sem `box-shadow`, então esses tokens precisam ser conferidos ao vivo.

**Segura · expressiva · ousada.** *Segura:* grade Minimalist. *Expressiva:* Neo-brutalist na linhagem do Gumroad, ou prévias em Bento. *Ousada:* Retro, Y2K ou Maximalist para criadores de templates de nicho, ou hero com prévia interativa ao vivo. A troca é que a moldura compete com o produto **[S]**.

**Evitar.** Glassmorphism sobre as prévias, porque atrapalha a leitura do próprio produto **[S]**.

**Confiança.** Contagem de vendas ("2.341 vendidos"), nota, lista de avaliações, card do criador e, junto ao botão, "download imediato" e política de reembolso **[S]**.

**Imagem.** Prévias reais do arquivo em uso **[S]**.

**Exemplos.** Gumroad ([webdesignhot](https://www.webdesignhot.com/api/design-md/gumroad.md)). Framer Marketplace (estilo **[O]**), Creative Market, UI8, Notion Templates e Envato Elements são **[O]**. Lemon Squeezy é **[O]**, foi comprada pela Stripe em 2024 e precisa de checagem de status.

### C6. Agências criativas e digitais

**Objetivo e conversão.** O visitante navega pelos trabalhos e depois clica em "Começar um projeto", que leva a um formulário qualificador (orçamento, prazo, serviços) ou a um calendário **[S]**.

**Estrutura e mobile.** Os padrões vistos em 12 agências são ([Krishaweb](https://www.krishaweb.com/blog/best-creative-agency-websites.txt)):

- home como fluxo de portfólio rolando (Instrument);
- home guiada por movimento (Fantasy, Hello Monday);
- site contido e autoritário, com projetos selecionados (Wolff Olins);
- arquivo filtrável por sócio, disciplina ou cliente (Pentagram);
- cases com briefing, processo e restrições (Area 17);
- foco numa só disciplina (Koto);
- hero com ponto de vista (Huge).

A pilha sugerida é hero tipográfico grande ou showreel, grade de trabalhos com prévia em vídeo no hover, lista de serviços, logos, processo, prêmios, equipe e um rodapé "Vamos conversar" com o e-mail em tipo grande **[S]**.

**Regras de UI/UX com evidência.** Cases enquadrados por resultado de negócio (Huge) ([Krishaweb](https://www.krishaweb.com/blog/best-creative-agency-websites.txt)). Valem o contrato de movimento do catálogo e a `prefers-reduced-motion` ([W3C](https://www.w3.org/WAI/WCAG21/Understanding/animation-from-interactions.html)).

**Estilo típico (eixos).** `aesthetic` Typographic-led + Swiss + Editorial · `layout` grade de trabalhos ou fluxo · `surface` flat · `motion` Kinetic typography + Immersive (WebGL, smooth scroll) · `type` display ou grotesk expressiva · `color` monocromático com acento **[S]**.

**Segura · expressiva · ousada.** Aqui a diferenciação é esperada. O site genérico é o template de agência do Webflow ou Framer: sans grande no hero, marquee de serviços e grade de trabalhos **[S]**. *Segura:* Swiss/Typographic com arquivo de trabalhos (Pentagram, Koto). *Expressiva:* fluxo Editorial com Kinetic (Instrument). *Ousada:* Immersive em WebGL (Locomotive **[O]**), Brutalist ou Maximalist. A troca é performance e risco vestibular, aceitável porque o site é a amostra **[S]**.

**Evitar.** O visual de template de SaaS, que diz "não somos criativos" **[S]**.

**Confiança.** Faixa de prêmios (Awwwards, FWA, Cannes, D&AD, Webby), imprensa, logos de clientes e retratos da equipe com nome **[S]**. Também cases por resultado ([Krishaweb](https://www.krishaweb.com/blog/best-creative-agency-websites.txt)).

**Imagem.** O trabalho em si, de preferência em vídeo **[S]**.

**Exemplos.** hugeinc.com, instrument.com, fantasy.co, wolffolins.com, area17.com, hellomonday.com, ideo.com, pentagram.com, wearecollins.com e koto.studio ([Krishaweb](https://www.krishaweb.com/blog/best-creative-agency-websites.txt)). A lista inclui a Ueno, que fechou depois de ser comprada pelo Twitter em 2021, então a atualidade da fonte é questionável **[✝]**. Consultorias B2B estão em D5.

## Finanças e serviços profissionais aceitam ousadia no tipo e na cor, nunca na clareza

Os seis nichos compartilham o mesmo esqueleto em 2025–2026 **[S]**:

1. Barra utilitária com telefone ou login.
2. Hero que responde quem, o quê e por quê.
3. Faixa de prova (logos, notas, selos, números).
4. Cards de serviço ou de área de atuação.
5. Pessoas.
6. Depoimentos e resultados.
7. Faixa de CTA repetida.
8. Rodapé com avisos legais.

O que varia é a mídia do hero e um módulo específico de cada nicho: calculadora em fintech, widget de cotação em seguros, bios e resultados em advocacia, central de insights em consultoria, escada de serviços em contabilidade e linha do processo em patrimônio.

A tolerância a estilo é assimétrica. As fontes de 2026 pedem que finanças troquem a estética "startup chamativa" por algo "mais maduro, calmo e tranquilizador". Uma cor "um pouco viva demais" pode minar a confiança, e excesso de 3D ou de animação "pode criar dúvida" ([Digidop](https://www.digidop.com/blog/2026-design-trends-for-finance-websites)). Ao mesmo tempo, a principal agência de design jurídico recomenda, para 2026, modo escuro de alto contraste, tipografia superdimensionada e recortes de retrato não convencionais ([PaperStreet](https://www.paperstreet.com/blog/2026-law-firm-website-design-trends/)). A leitura **[S]**: expressividade em tipografia, acento de cor, direção de arte e movimento sutil é aceita. Em clareza da informação, legibilidade, transparência e performance, não.

Os templates contam a mesma história em duas eras. O ThemeForest representa 2015–2020, com temas de advocacia tradicionais e heroes em slider. O Framer e o Webflow representam 2023–2026, com editorial minimalista, visual de SaaS e um acento só ([ThemeForest](https://themeforest.net/category/wordpress?term=law)). Ações de acessibilidade digital na Justiça federal dos EUA somaram 3.117 em 2025, 27% a mais que no ano anterior **[VEND]** ([Webtonic](https://www.webtonic.io/blog/best-web-design-ui-ux-agencies-for-wealth-management)).

### D1. Fintech, neobancos e investimento

**Objetivo e conversão.** A conversão é abrir conta ou baixar o app. A ação secundária é uma calculadora ou simulador, como o da Wise para estimar economia na hora ([Blend B2B](https://www.blendb2b.com/blog/best-fintech-website-examples)). Os robo-advisors franceses usam simuladores como ferramenta de conversão: Goodvest por tipo de aplicação, Ramify por objetivo e Yomoni para aposentadoria com dados fiscais ([Digidop](https://www.digidop.com/blog/2026-design-trends-for-finance-websites)).

**Estrutura e mobile.** Hero com mockup do app ou do cartão, QR no desktop e badges das lojas no mobile. Grade de recursos (o bento é inferido, nenhuma fonte o cita em finanças), calculadora ou conversor de câmbio, tabela de planos, seção de segurança, nota do app e logos de imprensa **[S]**. A UI de dados inclui tabelas comparativas (Ramify, Yomoni), gráfico de desempenho de sete anos (Nalo), barras e donuts (Pink Chip) e composição de fundo em círculo (Valhyr) ([Digidop](https://www.digidop.com/blog/2026-design-trends-for-finance-websites)).

**Regras de UI/UX com evidência.** Mostrar taxas e preços ou valores "a partir de", sem trancar o conteúdo principal atrás de login. Formulários curtos, ou em etapas com indicador de progresso. Prova de terceiros verificável em vez de depoimento anônimo ([NN/g](https://nngroup.com/articles/trustworthy-design/)). Movimento contido ([Digidop](https://www.digidop.com/blog/2026-design-trends-for-finance-websites)).

**Estilo típico (eixos).** A onda de 2021–2023 combinava Flat/Material, mesh gradients e ilustração 3D ou clay. Os exemplos eram os gradientes da Stripe, o clay 3D da Revolut, as formas 3D com lima da Wise, o cinza minimalista da Mercury e os hologramas do Cash App **[ANT]** ([BRIX](https://brixagency.com/inspiration/fintech-website-designs-for-inspiration/)). A direção atual é de neutros maduros com um acento neon. A identidade da Robinhood de outubro de 2024 usa preto, branco e neutros com o amarelo-esverdeado "Robin Neon", fotografia nítida e madura e um design "sem distrações" ([Robinhood](https://robinhood.com/us/en/newsroom/a-new-visual-identity)). Nos eixos: `aesthetic` Minimalist/Flat · `surface` flat, com gradiente cada vez menor · `motion` sutil · `type` grotesk · `color` neutros + uma cor de marca **[S]**.

**Segura · expressiva · ousada.** *Segura:* Minimalist claro com uma cor de marca, UI real e calculadora. *Expressiva:* uma cor saturada única com headline tipográfico grande, como o verde da Wise com globo ilustrado ([Digidop](https://www.digidop.com/blog/2026-design-trends-for-finance-websites)), ou Dark com luxury minimal, como a Robinhood. *Ousada:* Clay ou 3D, Kinetic, glass, para fintech jovem ou cripto. A troca é a dúvida que o excesso de 3D e de animação gera ([Digidop](https://www.digidop.com/blog/2026-design-trends-for-finance-websites)). Fintech neo-brutalista para Gen-Z e cripto existe na anedota, mas não foi verificada.

**Evitar.** Cor viva demais, 3D e animação em excesso, efeitos de cursor chamativos, texto de pouco contraste e scroll-jacking no mobile **[S]**.

**Confiança.** Os componentes vêm de [Digidop](https://www.digidop.com/blog/2026-design-trends-for-finance-websites), salvo onde indicado:

- cards de avaliação estilo Trustpilot (Yomoni);
- selos como "Best Retirement Plan 2025" (Ramify) e "Customer Service of the Year 2025" (Shine);
- logos de parceiros e seguradoras;
- pop-up regulatório (Diretiva UE 2014/65) e aviso bancário no fluxo (Revolut);
- retratos de assessores no menu (Ramify) e manifesto assinado pelo CEO;
- bloco de segurança com criptografia, proteção de depósitos, nome e número do regulador **[S]**.

**Imagem.** Mockup de app ou cartão, vídeo do produto (Ramp), fotografia madura e ilustração técnica ([Blend B2B](https://www.blendb2b.com/blog/best-fintech-website-examples); [Robinhood](https://robinhood.com/us/en/newsroom/a-new-visual-identity)).

**Exemplos.** Wise, Stripe, Revolut, Ramp e Algorand (stats ao vivo por API e alternância claro/escuro) ([Blend B2B](https://www.blendb2b.com/blog/best-fintech-website-examples)). Robinhood ([Robinhood](https://robinhood.com/us/en/newsroom/a-new-visual-identity)). Ramify, Qonto, Shine, Yomoni e Nalo, sem URL na fonte ([Digidop](https://www.digidop.com/blog/2026-design-trends-for-finance-websites)).

**Variantes.** *Fintech de consumo:* Flat com ilustração. *Investimento e trading:* Dark/tech migrando para luxury minimal. *Fintech B2B:* Minimalist/Swiss com UI de produto, glass sutil inferido e demos de produto imersivas, como Ramp e Stripe. *Cripto:* a maior tolerância do grupo **[S]**.

### D2. Contadores, impostos e escrituração

**Objetivo e conversão.** A conversão é "Agendar consulta", "Pedir orçamento" ou "Ligar de volta". As conversões utilitárias são o portal do cliente para envio seguro de arquivos e o link "Pagar fatura" ([Assembly](https://assembly.com/blog/accounting-firm-websites)). A Nth Degree troca o formulário de contato por um questionário atrás de um botão "Começar". A Fusion tem três CTAs: Preços, Ligar de volta e Chat ([Zarla](https://www.zarla.com/guides/accounting-website-examples)).

**Estrutura e mobile.** Os padrões observados são ([Zarla](https://www.zarla.com/guides/accounting-website-examples)):

- serviços em cards ou em escada, de gerente financeiro a CFO fracionado (Little Fish);
- dois cards de produto e preço, "só software" e "contadores + software", com banner de £10/mês (Crunch);
- checklist "Jeito errado × nosso jeito" (Appletree);
- barra de podcast ou imprensa;
- formulário de cotação no hero (template Zarla).

Os links de portal e de pagamento vão na barra utilitária **[S]**.

**Regras de UI/UX com evidência.** Transparência antecipada de custos e contato, sem conteúdo trancado ([NN/g](https://nngroup.com/articles/trustworthy-design/)). Preço por pacote ou "a partir de" onde o mercado aceita **[S]**.

**Estilo típico (eixos).** `aesthetic` Flat corporativo · `layout` hero com foto + faixa de prova · `type` sans · `color` azul/navy ou verde, foto com cara de banco. O hero com martelo de juiz e documento fiscal da Four Brothers é o clichê ([Assembly](https://assembly.com/blog/accounting-firm-websites)).

**Segura · expressiva · ousada.** *Segura:* Flat corporativo com faixa de prova. *Expressiva:* Editorial de boutique, com serif e neutros quentes. Exemplos são o verde e creme com serif da Appletree, o blush e creme com script da Little Fish, o branco generoso com filetes finos e ghost buttons da ProVision, e o fundo com folhagem da Long Term CPA ([Zarla](https://www.zarla.com/guides/accounting-website-examples); [Assembly](https://assembly.com/blog/accounting-firm-websites)). Acentos ilustrados, grade de serviços em Bento e tipo cinético restrito ao headline também cabem aqui **[S]**. *Ousada:* visual de SaaS em magenta e navy (Crunch), verde e amarelo "não corporativos" (EC Accounting) ou preto e branco com gráfico que segue o cursor (template Sophia Hoffman). A troca é perder clientes conservadores **[S]**.

**Evitar.** Fotos de martelo e aperto de mão, hero em slider automático e conteúdo atrás de formulário **[S]**.

**Confiança.** Parede de selos com ICAEW, parceiros de software e "Google 4.7 de 195 avaliações" (Fusion). Selos Forbes (Little Fish). Faixa "27 anos · AICPA · 1.400 clientes". Faixa de confidencialidade e "US$ 40M+ resolvidos" ([Zarla](https://www.zarla.com/guides/accounting-website-examples)). Logos de Xero e QuickBooks **[S]**.

**Imagem.** Equipe real e telas do software **[S]**.

**Exemplos.** crunch.co.uk, littlefishaccounting.com, appletreebusiness.com, fusionaccountants.co.uk, theorbitgroup.com.au e provisionwealth.com ([Zarla](https://www.zarla.com/guides/accounting-website-examples)). longterm.work e bakertilly.com ([Assembly](https://assembly.com/blog/accounting-firm-websites)).

**Variantes.** A Zarla já atribui paletas por subnicho, um padrão útil para a skill: creme com serif para o "estabelecido", hero escuro com formulário, roxo e lima para o "CPA de startup" e gradiente azul-roxo para "imposto cripto" ([Zarla](https://www.zarla.com/guides/accounting-website-examples)).

### D3. Seguros

**Objetivo e conversão.** A conversão é a cotação, com um input no hero e divulgação progressiva ([Azuro Digital](https://azurodigital.com/insurance-website-examples/)):

- a Hippo pede só o endereço;
- a Lemonade cota por um chatbot animado, a "Maya";
- a Ladder usa indicador de progresso e poucos campos;
- a Policygenius oferece várias entradas;
- a Oscar compara planos e leva ao portal do membro.

**Estrutura e mobile.** Campo de cotação no hero, "como funciona" em 3 passos, cards de cobertura por produto, estatística de rapidez no sinistro, notas (AM Best, Trustpilot) e FAQ em acordeão (seguradoras, territórios, elegibilidade, como na Park Shield) ([Azuro Digital](https://azurodigital.com/insurance-website-examples/)).

**Regras de UI/UX com evidência.** Formulários longos aumentam o custo de interação e reduzem a confiança ([NN/g](https://nngroup.com/articles/trustworthy-design/)). Não há estudo controlado comparando formulário no hero e botão de CTA (lacuna).

**Estilo típico (eixos).** *Incumbentes:* `aesthetic` Flat corporativo azul · imagem fotográfica. *Insurtech:* `aesthetic` Illustrative, vizinho do Corporate Memphis · `color` uma cor de marca viva · `type` sans amigável ([Azuro Digital](https://azurodigital.com/insurance-website-examples/)).

**Segura · expressiva · ousada.** *Segura:* Flat azul com foto. *Expressiva:* Minimalist pastel com fotos reais, como os azuis suaves e pessoas reais da Oscar ou os pastéis da Ladder. *Ousada:* Illustrative lúdico numa cor só, com chatbot, como o rosa da Lemonade, voltado a um público jovem. A troca é o tom e o risco de parecer datado ([Azuro Digital](https://azurodigital.com/insurance-website-examples/)). O Corporate Memphis perdeu força e virou paródia desde 2023 ([Wikipedia](https://en.wikipedia.org/wiki/Corporate_Memphis)), então a ilustração deve ser própria.

**Evitar.** Formulários longos no primeiro passo, Neo-brutalist, Y2K e baixo contraste **[S]**.

**Confiança.** Rating AM Best A- e limites de cobertura como números (Park Shield), notas acima de 4.5 (Kin) e prova social acima da dobra (Lemonade) ([Azuro Digital](https://azurodigital.com/insurance-website-examples/)).

**Imagem.** Ilustração própria, pessoas reais ou fotografia do bem segurado, como as fotos costeiras da Kin ([Azuro Digital](https://azurodigital.com/insurance-website-examples/)).

**Exemplos.** lemonade.com, hippo.com, hioscar.com, ladderlife.com, kin.com, nextinsurance.com e policygenius.com ([Azuro Digital](https://azurodigital.com/insurance-website-examples/)).

**Variantes.** *Incumbente ou corretor:* Flat corporativo. *Insurtech:* Illustrative ou pastel minimal **[S]**.

### D4. Escritórios de advocacia

**Objetivo e conversão.** A conversão é a consulta gratuita e a ligação. Os CTAs aparecem no header, no rodapé e na maior parte das seções, o telefone fica no header e mais de 60% do tráfego é mobile ([Knapsack](https://knapsackcreative.com/blog-industry/great-law-firm-website)). Numa pesquisa de cliente oculto com 500 escritórios dos EUA, só **40%** atenderam o telefone e 33% responderam o e-mail. Só 7% tinham chatbot, embora 51% dos potenciais clientes o vejam como bom ponto de partida. Quem falou com uma pessoa ao telefone teve mais de **três vezes** mais chance de recomendar o escritório ([2Civility](https://www.2civility.org/2024-clio-legal-trends-report-fixing-the-first-impression-problem-for-law-firms/)).

**Estrutura e mobile.** Cada área de atuação tem página própria com FAQ, tipos de caso e CTA específico ([Knapsack](https://knapsackcreative.com/blog-industry/great-law-firm-website)). As tendências de 2026 são ([PaperStreet](https://www.paperstreet.com/blog/2026-law-firm-website-design-trends/)):

- grids editoriais com assimetria e margens largas;
- áreas de atuação em cards;
- seções de altura total;
- filetes finos;
- navegação mínima com mega-menu;
- páginas de advogado com retrato grande e respiro editorial, em vez de diretório.

A Burges Salmon cortou cerca de metade das páginas, organizou o conteúdo pelo ponto de vista do cliente, reforçou a hierarquia tipográfica e a busca e adotou retratos pouco retocados ([Illustrate Digital](https://illustrate.digital/projects/burges-salmon/)). No mobile, uma barra sticky de ligação **[S]**.

**Regras de UI/UX com evidência.** Telefone visível e opção de retorno. Agendamento online, formulário de intake e mensagem de texto ([2Civility](https://www.2civility.org/2024-clio-legal-trends-report-fixing-the-first-impression-problem-for-law-firms/)). Carregar em menos de 3 s e ter botões fáceis de tocar ([Knapsack](https://knapsackcreative.com/blog-industry/great-law-firm-website)).

**Estilo típico (eixos).** O protótipo tradicional é `aesthetic` Luxury-lite ou vizinho do Art Deco · `color` navy, bordô e dourado · `type` serif · imagem de martelo, colunas ou skyline · hero em slider. É o que vendem os temas mais populares: "Attorney" com 4,7 mil vendas, "Law Office" com 1,7 mil e "Wize Law" com 1,3 mil ([ThemeForest](https://themeforest.net/category/wordpress?term=law)). A tendência de 2026 é Editorial, Typographic-led e paleta reduzida com um acento ([PaperStreet](https://www.paperstreet.com/blog/2026-law-firm-website-design-trends/)).

**Segura · expressiva · ousada.** *Segura:* Editorial claro com serif e um acento, como a paleta reduzida da Tressler, que é o protótipo atual da era Framer/Webflow. O protótipo tradicional em Luxury-lite (navy, bordô, dourado) fica como alternativa para quem pede sinais de tradição **[S]**. *Expressiva:* Typographic-led com tipo superdimensionado (Gerson, GRW) e retratos com recorte não convencional (Drake, Riddle). *Ousada:* Dark de alto contraste (Velkei, Roy Black). A troca é o contraste dos cinzas secundários e um tom menos institucional para clientes mais velhos ([PaperStreet](https://www.paperstreet.com/blog/2026-law-firm-website-design-trends/)).

**Evitar.** Fotos de martelo, aperto de mão e skyline, que estão perdendo espaço para fotografia dirigida ([PaperStreet](https://www.paperstreet.com/blog/2026-law-firm-website-design-trends/)). Slider automático como hero. Neo-brutalism, Y2K, Claymorphism, Corporate Memphis e Collage, com exceção de escritórios de danos pessoais ou boutiques tech com público jovem **[S]**.

**Confiança.** Selos da ordem e de certificações. Depoimentos com nome e foto ([Knapsack](https://knapsackcreative.com/blog-industry/great-law-firm-website)). Resultados de casos em cards de estatística, onde a regulação permitir. Avaliações de terceiros **[S]**.

**Imagem.** Retratos dirigidos e pouco retocados, e fotografia de arquivo coerente ([Illustrate Digital](https://illustrate.digital/projects/burges-salmon/)).

**Exemplos.** zemskyfamilylaw.com, leakeandersson.com, gersonlaw.com, grwpc.com, velkeilaw.com, royblack.com, tresslerllp.com, zimmreed.com, drakelegal.com, riddlepllc.com e omlaw.com ([PaperStreet](https://www.paperstreet.com/blog/2026-law-firm-website-design-trends/)). Burges Salmon tem URL inferida ([Illustrate Digital](https://illustrate.digital/projects/burges-salmon/)).

**Variantes.** *Escritório grande:* arquitetura de informação enxuta e busca forte. *Danos pessoais e consumidor:* telefone em primeiro lugar, mais denso. *Boutique:* Editorial ou Typographic **[S]**.

### D5. Consultorias e consultores

**Objetivo e conversão.** A conversão é contato, RFP ou download de estudo, e o conteúdo é a principal ferramenta de conversão ([HubSpot](https://blog.hubspot.com/website/consulting-website-examples)):

- o quiz de duas perguntas da Bain devolve três opções de serviço sem formulário;
- a Innosight rotula recursos para download por tipo;
- a IBM Consulting tem um índice na home que leva ao contato.

**Estrutura e mobile.** Hero de declaração, matriz de capacidades × setores, cases (desafio, abordagem, impacto em números), central de insights com filtros, pessoas e escritórios **[S]**. Os exemplos incluem o headline em duas colunas com arte original da McKinsey, o hero escuro com amarelo da EY, as três estatísticas de impacto da Yardstick e os cinco tiles de recursos da ERM no lugar de um carrossel ([HubSpot](https://blog.hubspot.com/website/consulting-website-examples)).

**Regras de UI/UX com evidência.** Escritórios, funcionários e valores visíveis aumentam a credibilidade ([NN/g](https://www.nngroup.com/articles/b2b-trust-from-b2c/)). Não trancar o conteúdo principal ([NN/g](https://nngroup.com/articles/trustworthy-design/)).

**Estilo típico (eixos).** `aesthetic` Editorial + Swiss minimal · `layout` declaração + grade de insights · `surface` flat · arte original · `type` grotesk ou serif editorial · `color` neutros com um acento. As Big Four são mais ousadas e cinéticas: cores fortes da Accenture, vídeo com headlines deslizantes da Booz Allen, parallax da Cognizant ([Seahawk](https://seahawkmedia.com/design/consulting-website-design-examples/)).

**Segura · expressiva · ousada.** *Segura:* Editorial/Swiss com arte original (McKinsey, PwC). *Expressiva:* Typographic-led de boutique, como as palavras em cursivo e roxo da Peoplism, o quebra-cabeça que se completa no scroll e os números claros sobre preto ([HubSpot](https://blog.hubspot.com/website/consulting-website-examples)). *Ousada:* arte cinética que reage ao usuário (Heidrick & Struggles). A troca é que WebGL pesado esconde a substância **[S]**.

**Evitar.** WebGL pesado sobre o conteúdo, conteúdo trancado e a estética de agência criativa numa consultoria de gestão **[S]**.

**Confiança.** Contadores animados e logos (RHR), estatísticas de impacto, cases nomeados, pessoas e escritórios ([HubSpot](https://blog.hubspot.com/website/consulting-website-examples)).

**Imagem.** Arte original e retratos, em vez de fotos de reunião de banco de imagens **[S]**.

**Exemplos.** mckinsey.com, bain.com, ey.com, innosight.com, peoplism.com, yardstickmanagement.com, rhrinternational.com e heidrick.com ([HubSpot](https://blog.hubspot.com/website/consulting-website-examples)). Não foram encontrados sites de consultores solo (lacuna).

### D6. Gestores de patrimônio e assessores financeiros

**Objetivo e conversão.** A conversão é agendar reunião ou "strategy call". Segundo um fornecedor, 58.2% do tráfego é mobile, mas o desktop converte 4.8% contra 2.1% no mobile. A recomendação é desenhar a descoberta para o celular e o pedido de reunião para a tela grande **[VEND]** ([Webtonic](https://www.webtonic.io/blog/best-web-design-ui-ux-agencies-for-wealth-management)).

**Estrutura e mobile.** Hero com lifestyle ou retrato, segmentos "quem atendemos" (executivos, empresários, aposentados), linha do processo (Descobrir → Planejar → Implementar → Revisar), equipe, bloco de transparência de taxas, agendador em etapas e login do cliente na barra utilitária **[S]**. As páginas de divulgação ADV, CRS e taxas entram no mapa do site, e vídeos têm transcrição ([Webtonic](https://www.webtonic.io/blog/best-web-design-ui-ux-agencies-for-wealth-management)).

**Regras de UI/UX com evidência.** Os números de performance são de fornecedor **[VEND]** ([Webtonic](https://www.webtonic.io/blog/best-web-design-ui-ux-agencies-for-wealth-management)): sites que passam em todos os Core Web Vitals teriam bounce 24% menor, e a Beacon Pointe teria dobrado a conversão ao reduzir o carregamento mobile de 12 s para 2 s.

**Estilo típico (eixos).** `aesthetic` Luxury · `color` verde escuro ou navy com dourado · `type` serif · `layout` muito branco e fotografia de lifestyle **[S]**. O arquétipo verde e dourado do private banking aparece na Peapack Private, conhecida só por snippet ([Peapack](https://www.peapackprivate.com/one-brand-one-website)).

**Segura · expressiva · ousada.** *Segura:* Luxury sóbrio. *Expressiva:* Editorial minimal. *Ousada:* UI com movimento sob medida (Trenith) ou a saída deliberada de paletas "apagadas e conservadoras" (case Parsons Capital) ([Webtonic](https://www.webtonic.io/blog/best-web-design-ui-ux-agencies-for-wealth-management)). A troca é afastar o cliente mais velho **[S]**.

**Evitar.** Os mesmos clichês de advocacia, além de Neo-brutalist, Y2K e Clay **[S]**.

**Confiança.** Divulgações ADV, Form CRS e de taxas, conformidade WCAG, cases nomeados, rankings como o CNBC FA 100 e integrações com custodiantes ([Webtonic](https://www.webtonic.io/blog/best-web-design-ui-ux-agencies-for-wealth-management)).

**Imagem.** Lifestyle e retratos reais dos assessores **[S]**.

**Exemplos.** É o conjunto mais fraco. Vector Wealth e Camarda vêm de uma lista de 2019 **[ANT]** ([WealthManagement.com](https://www.wealthmanagement.com/marketing/five-financial-advisor-web-design-examples-that-attract-and-convert)), e a Peapack Private só de snippet. Não há exemplos verificados de 2025–26.

### D7. Notários e cartórios

**Objetivo e conversão.** A conversão é agendar, com telefone ou WhatsApp, e o preço aparece logo ([Zarla](https://zarla.com/guides/notary-website-examples)):

- a onenotary.us tem "Notarize Now" como principal e "Business Plans" como secundário;
- a notablenotary.ca mostra US$ 34,99 no hero, com agendamento e WhatsApp;
- a pdxsigning.com informa uma faixa de US$ 25–125;
- a judithwinward.co.uk põe o telefone ao lado do título.

**Estrutura e mobile.** Cards de serviço com "saiba mais", gráfico de passos (onenotary), chips de confiança com nota, tempo de resposta e credencial, e heroes com imagem dividida ([Zarla](https://zarla.com/guides/notary-website-examples)).

**Regras de UI/UX com evidência.** Mostrar o preço logo segue a regra de transparência antecipada ([NN/g](https://nngroup.com/articles/trustworthy-design/)).

**Estilo típico (eixos).** `aesthetic` Flat institucional · `color` navy ou azul e branco, "estilo governo" · `type` sans ou serif sóbria. Uma minoria usa gradiente violeta de SaaS para notarização online, como a notarity ([Zarla](https://zarla.com/guides/notary-website-examples)).

**Segura · expressiva · ousada.** *Segura:* azul institucional. *Expressiva:* Organic calmo, como o verde em aguada da judithwinward ou os templates sálvia com dourado e ameixa com dourado antigo. *Ousada:* Flat de SaaS em gradiente violeta com mockups de celular, para notarização online. A troca é parecer um app e não um oficial público ([Zarla](https://zarla.com/guides/notary-website-examples)).

**Evitar.** Neo-brutalist, Y2K, Maximalist e Collage **[S]**.

**Confiança.** Faixa de ícones de conformidade (notarity), logos de clientes corporativos (onenotary) e credencial no headline (ironcladsigningco.com) ([Zarla](https://zarla.com/guides/notary-website-examples)).

**Imagem.** Retrato do profissional e escritório **[S]**.

**Exemplos.** onenotary.us, notarity.com, notablenotary.ca e judithwinward.co.uk ([Zarla](https://zarla.com/guides/notary-website-examples)).

**Variantes.** A amostra é de notary public dos EUA, Canadá e Reino Unido. O notariado latino, como o Notar alemão e o cartório brasileiro, não foi coberto e provavelmente pede um registro mais institucional **[S]**.

## Saúde, beleza e bem-estar giram em torno do botão de agendar, e o calor hospitaleiro diferencia

Em todos os nichos desta família, a conversão é agendar: uma consulta, uma avaliação gratuita, uma aula ou uma oferta de entrada. Os sites atuais mantêm essa ação visível em todas as páginas e oferecem um caminho de compromisso menor, como telefone, atendimento sem hora marcada, quiz ou ferramenta de match. A evidência vem de saúde e vale para toda a família. Num estudo com 1,33 milhão de respondentes da pesquisa de pacientes de clínicas gerais do Reino Unido, só **45.11%** sabiam que havia agendamento online e **15.61%** já tinham usado. Quem achava o site "muito fácil" tinha muito mais chance de agendar online (**OR 6.34**), e o uso caía depois dos 75 anos. Os dados são de 2018–2019 ([JMIR 2024](https://www.jmir.org/2024/1/e51931)). Nos EUA, 43% nunca agendaram online. 22% citam que o prestador não oferece, 17% que não há horário próximo e 7% que não sabem que tipo de consulta precisam ([Becker's](https://www.beckershospitalreview.com/innovation/why-patients-dont-use-online-scheduling)).

A NN/g mede um declínio de cerca de **0.8% ao ano** na capacidade de usar sites entre 25 e 60 anos. Recomenda texto e alvos grandes, alto contraste, aceitar vários formatos de entrada e tolerar erros **[ANT]** ([NN/g](https://www.nngroup.com/articles/usability-for-senior-citizens/)). Parallax e movimento disparado por interação podem causar tontura e náusea em pessoas com distúrbios vestibulares ([W3C](https://www.w3.org/WAI/WCAG21/Understanding/animation-from-interactions.html)). Para nichos de saúde, os padrões sintetizados são **[S]**:

- corpo de 16–18px;
- alvos de 44–48px;
- AA no mínimo;
- tap-to-call ao lado do "Agendar";
- formulários que aceitem telefone e data em formato livre e não exijam conta antes de escolher o horário;
- sem parallax nem vídeo com som em terapia e medicina.

Glass, Neumorphism e Claymorphism aparecem em kits de UI de apps de saúde, mas **não foram observados em nenhum site real de consultório** desta pesquisa. A predominância do Squarespace em terapia, pilates e unhas explica boa parte do protótipo "com cara de Squarespace" ([Colorlib](https://colorlib.com/wp/pilates-studio-website-examples/)).

### E1. Clínicas médicas e atenção primária

**Objetivo e conversão.** A conversão é "Agendar consulta" com o telefone ao lado. Clínicas com várias unidades acrescentam um buscador de unidade ou de médico **[S]**. Como 7% não sabem que tipo de consulta precisam, o fluxo pode começar pelo sintoma ou pela especialidade ([Becker's](https://www.beckershospitalreview.com/innovation/why-patients-dont-use-online-scheduling)).

**Estrutura e mobile.** A ordem sugerida é **[S]**:

1. Header com telefone e botão Agendar.
2. Hero com Agendar + Ligar e um chip de próximo horário ou horário de funcionamento.
3. Grade de serviços.
4. Médicos (foto, especialidade, credenciais, botão Agendar).
5. "O que esperar".
6. Avaliações e acreditações.
7. Convênios.
8. Mapa, horários e estacionamento.
9. FAQ.

No mobile, uma barra inferior com Ligar e Agendar. Os templates do Framer trazem perfis de médicos, FAQ, formulário de consulta e busca em destaque ([Framer](https://www.framer.com/blog/healthcare-website-design-examples/)). O conjunto padrão de recursos do Webflow inclui portal do paciente, teleconsulta e chat ([Webflow](https://webflow.com/templates/category/medical-websites)).

**Regras de UI/UX com evidência.** Deixar o agendamento visível e fácil de achar, manter o telefone e garantir horários online suficientes, inclusive urgentes ([JMIR 2024](https://www.jmir.org/2024/1/e51931)). Login e plataforma ineficaz afastam 3% e 8% dos pacientes ([Becker's](https://www.beckershospitalreview.com/innovation/why-patients-dont-use-online-scheduling)).

**Estilo típico (eixos).** `aesthetic` Flat/Material ou Minimalist "clínico" · `layout` grade de ícones · `surface` flat · `motion` mínimo · `type` sans · `color` branco com azul ou teal · foto de banco de médicos **[S]**. É um prior forte, mas ninguém o quantificou.

**Segura · expressiva · ousada.** *Segura:* Minimalist clínico. *Expressiva:* minimalismo hospitaleiro e editorial. O sistema da One Medical usa serif própria (One GT Super) com Ginto, fotografia íntima e bem fechada de pessoas juntas em vez do consultório, e ilustração editorial em tons terrosos e formas orgânicas. O tom pedido é "humano, ponderado, moderno e premium, mas acessível" ([One Medical](https://www.onemedical.com/brand-guidelines/)). Outra opção é o Scandinavian/Japandi calmo **[S]**. *Ousada:* um mundo de marca hospitaleiro completo, como o terracota, rosa e amarelo com formas curvas da Oula ([Hospitality Design](https://hospitalitydesign.com/projects/boutique-healthcare/121536)). A troca é a hipótese de que esse visual só convence quando a clínica física combina com ele **[S]**.

**Evitar.** Immersive, scroll-jacking, parallax, Kinetic, vídeo automático, paletas Dark/tech e efeitos glitch de Y2K, que aumentam a carga cognitiva de quem está ansioso ou é mais velho. Também neumorphism ou glass sobre foto **[S]**.

**Confiança.** Faixa de credenciais, card-resumo de avaliações (média, contagem, fonte e três citações recentes), logos de convênios, cards da equipe com foto real e acreditação **[S]**. Bios, depoimentos e credenciais se repetem nos templates ([Framer](https://www.framer.com/blog/healthcare-website-design-examples/)).

**Imagem.** Profissionais reais e pessoas juntas, em vez de espaços vazios ([One Medical](https://www.onemedical.com/brand-guidelines/)).

**Exemplos.** onemedical.com, parsleyhealth.com, asktia.com e oulahealth.com. Os três últimos foram descritos pelos interiores, em 2021 **[ANT]** ([Hospitality Design](https://hospitalitydesign.com/projects/boutique-healthcare/121536)). bupa.co.uk/dental é corporativo-clínico ([Krishaweb](https://www.krishaweb.com/blog/best-dental-website-designs/)). Templates de referência: APEX Clinic, MedExpert e Al-Medi ([Framer](https://www.framer.com/blog/healthcare-website-design-examples/)).

### E2. Odontologia e ortodontia

**Objetivo e conversão.** A conversão é Agendar, com linha de emergência e oferta para novo paciente. A Beehive deixa o formulário "a um clique" e o telefone sempre visível. A 1-800-DENTIST usa o telefone como CTA principal. A Diamond Braces abre com consulta gratuita ([Krishaweb](https://www.krishaweb.com/blog/best-dental-website-designs/)).

**Estrutura e mobile.** Os módulos-chave são ([Krishaweb](https://www.krishaweb.com/blog/best-dental-website-designs/)):

- perfis de dentista com foto, filosofia de atendimento e credenciais;
- galeria de antes e depois acessível da home;
- seção de emergência;
- preço e financiamento já no início;
- comparação de tratamentos (aparelho × Invisalign × alinhador);
- localizador de unidade para redes (Aspen Dental);
- página de tour pelo consultório.

**Regras de UI/UX com evidência.** Para pacientes ansiosos, equilibrar credibilidade clínica e calor, mostrando rostos e filosofia além de diplomas ([Krishaweb](https://www.krishaweb.com/blog/best-dental-website-designs/)).

**Estilo típico (eixos).** `aesthetic` Minimalist clínico · `layout` hero com foto de sorriso + slider de antes e depois · `color` branco e azul **[S]**.

**Segura · expressiva · ousada.** *Segura:* clínico. *Expressiva:* minimalismo hospitaleiro em pastel quente. A Tend usa paleta quente e apagada, formas arredondadas e referências de hotel-boutique para tornar a odontologia "quase sem fobia", e o site repete os tons do consultório ([SURFACE](https://surfacemag.com/articles/tends-design-first-approach-makes-dentistry-nearly-phobia-free/)). Também serve Bento na grade de serviços. *Ousada:* um conceito de marca lúdico e único, como a Beehive, citada como superior ao "polimento genérico". A troca é que isso é opinião de agência ([Krishaweb](https://www.krishaweb.com/blog/best-dental-website-designs/)).

**Evitar.** Neumorphism ou glass com pouco contraste, e Immersive **[S]**.

**Confiança.** Perfis, avaliações recentes como principal sinal local, antes e depois com nota de consentimento, preço e convênios, e comparações honestas de tratamento ([Krishaweb](https://www.krishaweb.com/blog/best-dental-website-designs/)).

**Imagem.** Equipe real, consultório real e sorrisos de pacientes com consentimento **[S]**.

**Exemplos.** hellotend.com ("quente, moderno, deliberadamente não clínico"), beehivedental.com, aspendental.com, diamondbraces.com, smilegeneration.com e 1800dentist.com ([Krishaweb](https://www.krishaweb.com/blog/best-dental-website-designs/)). A Tend tem um registro na Red Dot de ano não verificado ([Red Dot](https://red-dot.org/project/tend-49427)). A fonte cita a ferramenta de avaliação da Smile Direct Club como gancho, mas a empresa encerrou as operações no fim de 2023 **[O][✝]**.

### E3. Psicólogos, terapeutas e aconselhamento

**Objetivo e conversão.** Num conjunto de 29 sites de terapeutas, as conversões recorrentes foram ([Colorlib](https://colorlib.com/wp/therapist-websites/)):

- consulta gratuita de 15 minutos;
- banner de disponibilidade ("aceitando clientes", "agenda cheia", "sem fila de espera");
- valor da sessão "a um clique" ou na própria home;
- quiz ou ferramenta de match no lugar do formulário;
- layout de busca por tipo de atendimento, local e convênio;
- agendamento embutido via SimplePractice, Halaxy, Zencare ou Psychology Today.

**Estrutura e mobile.** Os tipos de hero são retrato único, foto da poltrona ou da sala real, sala de brinquedos real, retrato em meia tela, retrato recortado e headline em forma de pergunta. Os módulos incluem especialidades em checklist, páginas fixas de "Valores" e "Disponibilidade" no menu, valores por duração de sessão, logos de convênio e atendimento presencial e online ([Colorlib](https://colorlib.com/wp/therapist-websites/)).

**Regras de UI/UX com evidência.** Reduzir a incerteza com blocos "o que esperar", valores visíveis, status de disponibilidade e fotos da sala e do profissional reais. Checar contraste de sálvia sobre bege **[S]**. Não foi encontrado estudo revisado por pares sobre o design de sites de terapia (lacuna).

**Estilo típico (eixos).** `aesthetic` Organic ou Minimalist suave · `layout` coluna única com retrato · `surface` flat · `motion` nenhum · `type` serif ou script nos títulos · `color` light, sobre base branca ou creme com acentos apagados: sálvia `#9EACAD`, verde floresta `#355333` e `#0D352D`, e terracota `#894224` e `#E57B53` ([Colorlib](https://colorlib.com/wp/therapist-websites/)).

**Segura · expressiva · ousada.** *Segura:* Organic suave. *Expressiva:* Typographic-led em preto e branco, sem fotografia (miljabrecherdemuro.com). *Ousada:* Dark com um acento e tom irreverente, como o quase-preto com vermelho profundo da therapywithjoy.com, ou Maximalist culturalmente específico, como o roxo profundo com cravos-de-defunto da embracecorazon.com. A troca é falar só com um público muito definido ([Colorlib](https://colorlib.com/wp/therapist-websites/)).

**Evitar.** Immersive, parallax, Kinetic, vídeo automático, Dark/tech genérico, glitch e bege sobre bege com pouco contraste **[S]**.

**Confiança.** Logos de convênio, badge Zencare, banners de disponibilidade, valores claros incluindo a taxa de triagem, e atendimento online e presencial ([Colorlib](https://colorlib.com/wp/therapist-websites/)).

**Imagem.** Retrato real e consultório real ([Colorlib](https://colorlib.com/wp/therapist-websites/)).

**Exemplos.** jessicameiman.com (Minimalist), wholenesscollectivetherapy.com e jareebasgall.com (Organic), miljabrecherdemuro.com (Typographic), therapywithjoy.com (Dark), blwtherapy.com, deepeddypsychotherapy.com (busca) e embracecorazon.com ([Colorlib](https://colorlib.com/wp/therapist-websites/)).

### E4. Salões de cabelo, barbearias e nail studios

**Objetivo e conversão.** A conversão é "Agendar", com deep-link para Fresha, Vagaro ou Booksy, e informação sobre atendimento sem hora marcada **[S]**. Nas barbearias, a Imperium põe "Agendar" ao lado de "Sem hora marcada", a Legends combina Agendar com Loja e a Curbside Cuts promete agendamento "em 60 segundos" ([Zarla](https://www.zarla.com/guides/barbershop-website-examples)). Os nail studios dependem de motores externos (Zenoti, Vagaro, Fresha, Square, Boulevard, Meevo) e vendem assinaturas de US$ 59–99 por mês, vale-presente, fidelidade e press-ons ([Colorlib](https://colorlib.com/wp/nail-salon-website-examples/)).

**Estrutura e mobile.** Hero em full-bleed com Agendar, menu de serviços com preço e duração em abas, equipe com "agendar com fulano", grade estilo Instagram, avaliações, horário, mapa e vale-presente **[S]**. Nas barbearias, a cidade costuma estar no headline e os preços quase nunca aparecem: só a Ironside & Crowe mostra o menu com preços ([Zarla](https://www.zarla.com/guides/barbershop-website-examples)). Nos nail studios aparecem feeds do Instagram, marquees animados, marquee de avaliações, blocos de cor divididos, preços transparentes e localizador de unidades ([Colorlib](https://colorlib.com/wp/nail-salon-website-examples/)).

**Regras de UI/UX com evidência.** Marquees precisam de controle de pausa ([W3C](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)). O movimento nunca pode atrasar o botão Agendar **[S]**. Não há estudo sobre o efeito de mostrar preços em salões (lacuna).

**Estilo típico (eixos).** *Barbearias:* `aesthetic` Dark heritage/Retro · `color` preto, carvão ou navy com dourado ou latão · `type` serif ou script · brasões e neon ([Zarla](https://www.zarla.com/guides/barbershop-website-examples)). *Nail studios:* `aesthetic` Minimalist com muito branco · `color` pastel ou rosa e branco · grade de Instagram. O Squarespace está em 14 de 26 sites ([Colorlib](https://colorlib.com/wp/nail-salon-website-examples/)). *Salões de cabelo:* Luxury ou Editorial minimal, sem exemplos com fonte **[S]**.

**Segura · expressiva · ousada.** *Segura:* o protótipo de cada variante. *Expressiva:* Editorial em preto e branco com display serif, como a Paintbox (freight-display-pro) ou a Paint Nail Bar (Avenir, Didot, DIN Next) ([Colorlib](https://colorlib.com/wp/nail-salon-website-examples/)), ou marquee Kinetic. *Ousada:* Neo-brutalist em preto e amarelo ácido (Barber Barber) ([Zarla](https://www.zarla.com/guides/barbershop-website-examples)), gradientes pastel Y2K (NAF!), Maximalist tropical (Tropical Popical) ou Collage para salão de moda. A troca é afastar quem quer só um corte rápido **[S]**.

**Evitar.** Movimento sem fallback para reduced motion e botão de agendar escondido **[S]**.

**Confiança.** Selos de tempo de casa ("Celebrating 10 Years" da Master Barbers LA, "Traditional Family Barbers" da Gould) ([Zarla](https://www.zarla.com/guides/barbershop-website-examples)). Marquee de avaliações, reviews da Okendo e links para Yelp, Instagram e TikTok ([Colorlib](https://colorlib.com/wp/nail-salon-website-examples/)). Bloco de higiene e esterilização **[S]**.

**Imagem.** Cliente na cadeira, interior com neon e trabalho em close ([Zarla](https://www.zarla.com/guides/barbershop-website-examples)).

**Exemplos.** legends-barber.com (Dark), imperiumbarber.com (Dark-Retro), barberbarber.com (Neo-brutalist), backstagebarbershop.com (neon Retro) ([Zarla](https://www.zarla.com/guides/barbershop-website-examples)). paint-box.com, jinsoon.com, houseofnaf.com e amathesalon.com ([Colorlib](https://colorlib.com/wp/nail-salon-website-examples/)). Não há exemplos de salão de cabelo com fonte (lacuna).

**Variantes.** Barbearia, nail studio e salão de cabelo, como acima. Há barbearias claras fora do padrão: uma barbearia de navalha em creme com serif, um especialista em fade em azul vivo e uma barbearia infantil em laranja e menta ([Zarla](https://www.zarla.com/guides/barbershop-website-examples)).

### E5. Spas e clínicas estéticas (med spa)

**Objetivo e conversão.** Nas med spas, a ação principal é agendar uma consulta, quase sempre com uma alternativa de menor compromisso: consulta gratuita (Revive) ou o caminho "Not Ready to Book" (Tribeca). A unidade escolhida molda a navegação (Milk + Honey), e a Upkeep mantém o agendamento "visível e persistente" ([Workee](https://workee.ai/blog/best-medspa-websites)). Nos spas, um botão "Book" em destaque é a norma ([GlossGenius](https://glossgenius.com/blog/spa-websites)).

**Estrutura e mobile.** *Spas:* páginas de serviço com preço e duração, ofertas, políticas de atraso e cancelamento, e imagens e vídeos de natureza ([GlossGenius](https://glossgenius.com/blog/spa-websites)). *Med spas:* serviços agrupados por categoria ou preocupação para que um cardápio grande seja escaneável, navegação começando pela unidade, assinaturas, financiamento e antes e depois ([Workee](https://workee.ai/blog/best-medspa-websites)).

**Regras de UI/UX com evidência.** Mostrar as políticas antes da reserva ([GlossGenius](https://glossgenius.com/blog/spa-websites)). Não esconder preço nem agendamento atrás de animação pesada **[S]**.

**Estilo típico (eixos).** *Spa:* `aesthetic` Luxury + Organic · `color` neutros apagados · `type` serif delicada · vídeo de natureza. A Linnaean é descrita por "fontes delicadas, cores apagadas, ar elegante" ([GlossGenius](https://glossgenius.com/blog/spa-websites)). *Med spa:* `aesthetic` Luxury minimal · `color` branco, blush e bege · `type` serif · fotografia de modelo brilhante **[S]**.

**Segura · expressiva · ousada.** *Segura:* Luxury/Organic. *Expressiva:* Editorial com "compre por preocupação", Bento para a grade de tratamentos, texturas Wabi-sabi ou Japandi. *Ousada:* Immersive scroll com natureza, usado com parcimônia. A troca é o risco vestibular, o peso e o contraste de texto sobre bege **[S]**.

**Evitar.** Bege sobre bege e animação que esconde o preço **[S]**.

**Confiança.** Credenciais dos profissionais, financiamento, antes e depois ([Workee](https://workee.ai/blog/best-medspa-websites)), acordeão de políticas e avaliações em destaque ([GlossGenius](https://glossgenius.com/blog/spa-websites)). Os protocolos de COVID-19 da Forever Young são um sinal de higiene de outra época.

**Imagem.** Natureza, texturas e modelos com consentimento **[S]**.

**Exemplos.** linnaean.co.uk e refuge.com ([GlossGenius](https://glossgenius.com/blog/spa-websites)). milkandhoney.com ([Workee](https://workee.ai/blog/best-medspa-websites)).

### E6. Academias, fitness e personal trainers

**Objetivo e conversão.** A conversão é "Matricule-se", "Aula experimental" ou "Reserve uma aula", sempre com a grade de horários **[S]**. O redesign da Barry's tinha como objetivo simplificar a jornada de quem quer reservar uma aula na sua região e acrescentou loja Shopify. O case informa 17 mil pedidos por mês e ticket médio de US$ 133, sem base de comparação ([Barrel](https://www.barrelny.com/work/barrys)).

**Estrutura e mobile.** Hero em vídeo com aula experimental, tipos de aula, widget de horários (abas por dia, filtros por aula, coach e unidade), planos em 3 níveis, coaches, histórias de transformação, unidades e download do app **[S]**. Os padrões vistos são cards que entram animados no scroll (Buckler), vídeo e hover na home (Equinox) e menu com hover animado (Sebastian Lundberg) ([KIJO](https://kijo.london/blog/fitness-websites)). Widgets embutidos como Mindbody, Glofox e Momence dominam a UI da grade de horários **[S]**.

**Regras de UI/UX com evidência.** Não há dados sobre widgets de horário nem estudo de site escuro contra claro (lacuna). Movimento sempre com fallback ([W3C](https://www.w3.org/WAI/WCAG21/Understanding/animation-from-interactions.html)).

**Estilo típico (eixos).** `aesthetic` Dark bold · `layout` vídeo em full-bleed · `motion` médio · `type` sans condensada em caixa alta · `color` dark com acento neon ou vermelho **[S]**. No luxo, a paleta da Buckler é "escura e despojada" e a da Equinox "mínima e luxuosa" ([KIJO](https://kijo.london/blog/fitness-websites)).

**Segura · expressiva · ousada.** *Segura:* Dark bold. *Expressiva:* Luxury minimal (Equinox) ou Kinetic typography, já que o movimento é bem aceito neste nicho. *Ousada:* tipografia de impacto com toques de cor viva (Sebastian Lundberg) ou Neo-brutalist. A troca é contraste e foco ([KIJO](https://kijo.london/blog/fitness-websites)).

**Evitar.** Site só escuro com texto cinza fino, que falha no contraste, e movimento que atrasa o "Reserve" **[S]**.

**Confiança.** Números de resultado, transformações, credenciais dos coaches e avaliações **[S]**.

**Imagem.** Vídeo de treino real, coaches e o espaço **[S]**.

**Exemplos.** equinox.com, bucklerfit.com.br (Brasil) e sebastianlundberg.dk ([KIJO](https://kijo.london/blog/fitness-websites)). barrys.com ([Barrel](https://www.barrelny.com/work/barrys)).

**Variantes.** *Academia grande:* Dark bold. *Fitness boutique:* Dark ou cor de marca forte, com Editorial e Y2K pastel como diferenciação. *Personal trainer:* marca pessoal, ver G6 **[S]**.

### E7. Yoga e pilates

**Objetivo e conversão.** A conversão é a oferta de entrada com a grade de aulas: "Try a Free Week" na Yoga Pod e "7 Classes for $120" na GOOD Pilates. A Yoga on the Lane oferece dois caminhos, estúdio e online, cada um com seu Agendar. A Unplugged usa onboarding em 3 passos ([Zarla](https://www.zarla.com/guides/yoga-website-examples)). No pilates, a reserva fica "no centro", com fluxo para várias unidades (Pilates Republic) e botão fixo no header (Brighton Pilates) ([Colorlib](https://colorlib.com/wp/pilates-studio-website-examples/)).

**Estrutura e mobile.** Hero com foto calma e oferta de entrada, tipos de aula para iniciantes, grade semanal, fileira de professores no topo (Kind), planos de avulsa, pacote e ilimitado, fotos do estúdio e FAQ do que levar **[S]**. Marquees são frequentes, assim como blocos de imagem sobrepostos, vídeo no hero e loja ao lado da reserva ([Colorlib](https://colorlib.com/wp/pilates-studio-website-examples/)).

**Regras de UI/UX com evidência.** Marquees com controle de pausa ([W3C](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)) e contraste de sálvia sobre creme **[S]**.

**Estilo típico (eixos).** `aesthetic` Organic ou Minimalist terroso · `layout` grade de aulas · `motion` marquee · `type` serif ou script · `color` light em creme, sálvia e terracota. O Squarespace está em 19 de 26 sites de pilates ([Colorlib](https://colorlib.com/wp/pilates-studio-website-examples/)).

**Segura · expressiva · ousada.** *Segura:* Organic. *Expressiva:* Editorial (Be Kind), lima com damasco e lilás (Rebalance), ou Illustrative multicolorido em vez de foto (Yoga on the Lane). *Ousada:* Dark com cara de streetwear, como o preto e laranja com display grafitado da Y7 ([Zarla](https://www.zarla.com/guides/yoga-website-examples)), ou Y2K pastel com brilhos (Kink Pilates). A troca é falar com um público jovem e urbano específico **[S]**.

**Evitar.** Pouco contraste e marquee sem pausa **[S]**.

**Confiança.** Depoimentos com nome, imagens diversas e layout que começa pela equipe ([Zarla](https://www.zarla.com/guides/yoga-website-examples)).

**Imagem.** Estúdio real, luz natural e professores **[S]**.

**Exemplos.** y7-studio.com, kindcanberra.com.au e yogaonthelane.com ([Zarla](https://www.zarla.com/guides/yoga-website-examples)). thehouseofsculpt.com, rebalance.studio e kinkpilates.com ([Colorlib](https://colorlib.com/wp/pilates-studio-website-examples/)).

### E8. Fisioterapia e bem-estar holístico

**Objetivo e conversão.** A conversão é "Agendar avaliação", com um buscador por condição. Todos os exemplos de fisioterapia analisados oferecem agendamento online, e a Professional PT organiza o site em torno de "achar a unidade mais próxima" ([Seahawk](https://seahawkmedia.com/design/physical-therapist-websites/)).

**Estrutura e mobile.** Hero com Agendar, grade de condições tratadas (coluna, joelho, esporte, pós-operatório), abordagem, profissionais, resultados, convênios e unidades **[S]**. Exemplos: páginas detalhadas de tratamento com blog baseado em evidência (Cioffredi) e números de resultado (Therapydia) ([Seahawk](https://seahawkmedia.com/design/physical-therapist-websites/)).

**Regras de UI/UX com evidência.** Valem as mesmas regras de acessibilidade das clínicas ([NN/g](https://www.nngroup.com/articles/usability-for-senior-citizens/)).

**Estilo típico (eixos).** *Fisioterapia:* `aesthetic` Flat ou Minimal limpo · `color` azul, teal ou verde, com acentos esportivos ([Seahawk](https://seahawkmedia.com/design/physical-therapist-websites/)). *Holístico:* `aesthetic` Organic com tons terrosos, imagem botânica e formas suaves. O template "Healing" do Framer é descrito como "quente e acolhedor" ([Framer](https://www.framer.com/blog/healthcare-website-design-examples/)).

**Segura · expressiva · ousada.** *Segura:* Flat calmo. *Expressiva:* Scandinavian calmo, ou marca forte com sensação calma (RISE). *Ousada:* marca esportiva Dark para reabilitação esportiva (SPEAR). No holístico, as alternativas são Wabi-sabi, Japandi e Illustrative. A troca é afastar pacientes mais velhos **[S]**.

**Evitar.** O mesmo que em E1 **[S]**.

**Confiança.** Histórias de pacientes, números de resultado e conteúdo baseado em evidência ([Seahawk](https://seahawkmedia.com/design/physical-therapist-websites/)).

**Imagem.** Clínica e profissionais reais, e movimento em vez de maca **[S]**.

**Exemplos.** professionalpt.com, risephysicaltherapy.com, cioffredi.com e spearcenter.com ([Seahawk](https://seahawkmedia.com/design/physical-therapist-websites/)). essentialmvmt.com, de movimento holístico ([Colorlib](https://colorlib.com/wp/pilates-studio-website-examples/)). Não há exemplos documentados de acupuntura, naturopatia ou Ayurveda (lacuna).

## Hospitalidade, comida, viagem, imóveis e eventos precisam mostrar o widget de transação já

Cada nicho desta família tem um widget de "transação": a busca por datas e hóspedes no hotel, Reservar, Cardápio e Pedir no restaurante, o calendário com o mapa do ponto de encontro no tour, a busca com filtros e mapa na imobiliária e o formulário de consulta no espaço de eventos. A regra com mais evidência é mostrar esse widget de imediato. O Baymard viu **99%** dos participantes em OTAs, grandes redes e aluguel de imóvel inteiro procurarem a busca na home logo de cara. Ainda assim, **25%** dos sites de hospedagem não a tratam como conteúdo principal. Na IHG, 78% acharam a busca abaixo da dobra, e um participante da Marriott levou quase 30 s para encontrá-la ([Baymard](https://baymard.com/blog/travel-accommodations-booking-search)). No benchmark de 2026, que cobre Booking.com, Airbnb, Hyatt, Expedia, Esmé Hotel e outros, a nota vai de "ruim" a "razoável", e só um site chega a "razoável". As falhas comuns são busca fora do topo, preço pouco transparente, filtros ruins e avaliações fracas ([Baymard](https://baymard.com/research-articles/travel-accommodations-ux-benchmark-2026)).

Hotéis e espaços de eventos seguem um padrão: hero em foto ou vídeo full-bleed e depois seções alternadas de imagem e texto. Imóveis e OTAs seguem outro: busca → grade de cards → página de detalhe. Restaurantes ficam no meio: hero de atmosfera e, em seguida, blocos bem utilitários de cardápio, horário e endereço **[S]**. Estilos marcantes funcionam quando o caminho de reserva continua padrão e visível. A NobleDEN mostra o risco: o "Book Now" sozinho, debaixo de uma imagem animada grande, passou despercebido ([Baymard](https://baymard.com/blog/travel-accommodations-booking-search)).

### F1. Hotéis, hotéis-boutique, B&Bs e pousadas

**Objetivo e conversão.** A conversão é reservar. Redes e hotéis grandes precisam de uma barra de busca de largura total no hero. O boutique é diferente: **73%** começaram explorando a propriedade e só 27% quiseram ver disponibilidade primeiro. A solução é divulgação progressiva, com só Check-in, Check-out e Reservar visíveis, e o resto aparece ao clicar, como na The Nolitan ([Baymard](https://baymard.com/blog/travel-accommodations-booking-search)).

**Estrutura e mobile.** *Home:* hero (vídeo de até 15 s ou foto) com barra de datas, declaração de abertura, carrossel de quartos, seções de restaurante, spa e experiências, mapa do bairro, faixa de avaliações, imprensa e prêmios, ofertas e rodapé com reserva **[S]**. *Detalhe do quarto:* galeria de 6–15 imagens, ícones com área, cama, vista e ocupação, comodidades, planta para suítes e caixa sticky "Ver disponibilidade" **[S]**. *Mobile:* barra inferior sticky "Reservar" e seletor de datas em tela cheia **[S]**. A One&Only Cape Town mantém um widget flutuante de reserva visível durante o scroll ([HotelTechReport](https://hoteltechreport.com/news/hotel-website-designs)).

**Regras de UI/UX com evidência.** O módulo de busca deve ficar no alto, quase em largura total e com contraste forte sobre a imagem. O botão "Buscar" é vibrante, os inputs são grandes e os dropdowns aparecem inteiros. Cookies, avisos e chat não podem cobrir a busca ([Baymard](https://baymard.com/blog/travel-accommodations-booking-search)). O seletor de datas deve mostrar a disponibilidade com precisão ([Baymard](https://baymard.com/ecommerce-design-examples/date-picker)). Mostrar "a partir de €X/noite" e o total com taxas antes do passo final **[S]**.

**Estilo típico (eixos).** `aesthetic` Luxury + Editorial · `layout` full-bleed + split imagem-texto · `surface` flat · `motion` fades lentos, Immersive leve · `type` serif display de alto contraste com sans fina e navegação em caixa alta espaçada · `color` off-white, areia ou preto com um acento profundo (floresta, navy, oxblood) **[S]**. A orientação geral é design simples, layouts mínimos, imagens grandes, muito branco e fontes próprias ([htmlburger](https://htmlburger.com/blog/best-hotel-website-design/)).

**Segura · expressiva · ousada.** *Segura:* Luxury minimal, como a 7132 ou o Royal Savoy. *Expressiva:* Editorial de revista, como os blocos de imagem em quebra-cabeça da Casa Angelina, ou Organic/Japandi, como a Wolny Las. Bento entra na seção de experiências e Kinetic fica restrito ao headline do hero. *Ousada:* Maximalist (El Fenn), Retro kitsch (Austin Motel), tipografia em movimento (Wake Medellín) ou cursor customizado (Samsara Ubud). A troca é que preloaders e cursores atrasam a reserva, e cursor customizado não faz nada no toque ([HotelTechReport](https://hoteltechreport.com/news/hotel-website-designs); [htmlburger](https://htmlburger.com/blog/best-hotel-website-design/)).

**Evitar.** Preloader ou animação de entrada antes do conteúdo, exceto em marca de design topo de linha com botão de pular. Carrossel automático sem barra de reserva. Barra de datas em glass sobre foto movimentada. Neumorphism e Claymorphism. Pop-up na entrada, que deve vir atrasado e fácil de fechar **[S]**. O vídeo não pode deixar a página lenta ([HotelTechReport](https://hoteltechreport.com/news/hotel-website-designs)).

**Confiança.** A Vesper exibe os 100% no TripAdvisor na home, a 18 Micon Street põe logos de avaliações e imprensa ao lado das fotos e a Nobnocket Inn destaca prêmios ([HotelTechReport](https://hoteltechreport.com/news/hotel-website-designs)). Uma caixa de vantagens da reserva direta e avaliações com fonte e data **[S]**.

**Imagem.** Vídeo em câmera lenta, drone e a casa em várias horas do dia, como no B&B Portland's White House ([HotelTechReport](https://hoteltechreport.com/news/hotel-website-designs)).

**Exemplos.** oneandonlyresorts.com/cape-town, casangelina.com, el-fenn.com, austinmotel.com, 7132.com e samsaraubud.com ([HotelTechReport](https://hoteltechreport.com/news/hotel-website-designs)). royalsavoylausanne.com, wakemedellin.com e wolnylas.pl ([htmlburger](https://htmlburger.com/blog/best-hotel-website-design/)). Aman, The Hoxton e Ace Hotel são **[O]**. A lista da HotelTechReport começou em 2020, então alguns sites podem ter sido redesenhados.

**Variantes.** *Luxo e resort:* Luxury + Editorial. *Boutique e lifestyle:* Editorial com Retro ou Maximalist, como a El Fenn. *B&B e agriturismo:* Organic e caseiro, com fontes "deliberadamente informais" como no Colette's e o menu dedicado à região como na The Black Walnut. *Motel e hostel:* Retro, Mid-century, Y2K ou Neo-brutalist, como o retrô tropical da The Drifter e as fotos sépia com ilustração da Tourists. *Apart-hotel:* minimal chique, como a La Réserve ([HotelTechReport](https://hoteltechreport.com/news/hotel-website-designs)).

### F2. Aluguel de temporada (imóvel único ou pequeno portfólio)

**Objetivo e conversão.** A conversão é reservar datas. Em aluguel de imóvel inteiro, os participantes procuraram a busca já na home ([Baymard](https://baymard.com/blog/travel-accommodations-booking-search)).

**Estrutura e mobile.** Página de detalhe no padrão Airbnb **[S]**:

- galeria em mosaico (uma grande e quatro pequenas) e "Ver todas as fotos";
- dados-chave de hóspedes, quartos, camas e banheiros;
- comodidades;
- calendário inline com estadia mínima;
- card de preço sticky (coluna direita no desktop, barra inferior no mobile);
- mapa, regras da casa e avaliações.

**Regras de UI/UX com evidência.** Preço transparente e calendário que mostre a disponibilidade de verdade ([Baymard](https://baymard.com/ecommerce-design-examples/date-picker)). Banners não podem cobrir a busca no mobile, como aconteceu na Plum Guide ([Baymard](https://baymard.com/blog/travel-accommodations-booking-search)).

**Estilo típico (eixos).** `aesthetic` Minimalist ou Scandinavian com UI tipo OTA · `type` sans limpa · `color` neutros **[S]**.

**Segura · expressiva · ousada.** *Segura:* UI de OTA. *Expressiva:* Scandinavian/Organic com a história do anfitrião. *Ousada:* uma revista Editorial sobre a casa. A troca é empurrar o calendário para baixo **[S]**.

**Evitar.** Galeria sem "ver todas" e preço só no checkout **[S]**.

**Confiança.** Avaliações com fonte, regras claras e política de cancelamento junto do botão **[S]**.

**Imagem.** Todos os cômodos, sem esconder defeitos **[S]**.

**Exemplos.** Plum Guide (busca de largura total) e HomeToGo (no benchmark) ([Baymard](https://baymard.com/research-articles/travel-accommodations-ux-benchmark-2026)).

### F3. Restaurantes, cafés, padarias e bares

**Objetivo e conversão.** No restaurante, os botões do header são Reservar (via OpenTable, Resy, TheFork ou SevenRooms), Cardápio e Pedir, com horário e endereço na primeira tela ou no rodapé. No café, Cardápio, Retirada e Horário. No bar, Horário, Eventos, Reservar mesa e Locação **[S]**. Os sites de 2025 põem "Pedir" ou "Reservar" no menu ou na primeira seção: Socrate, The Fifth, Sushi Seki e Craft House ([UpMenu](https://www.upmenu.com/blog/best-restaurant-websites-design/)).

**Estrutura e mobile.** Hero de atmosfera com Reservar e Cardápio, história curta, pratos em destaque, cardápio em HTML com abas por serviço e ícones de dieta, horário e endereço com mapa, eventos privados, vale-presente, imprensa e Instagram **[S]**. Redes começam pelo seletor de unidade (Sushi Kushi). O Gramercy Tavern divide a home entre Bar e Salão ([UpMenu](https://www.upmenu.com/blog/best-restaurant-websites-design/)).

**Regras de UI/UX com evidência.** Nada de cardápio só em PDF. A NN/g diz que PDFs desorientam, atrapalham a leitura de varredura e são "subótimos" no celular, e aceita "um cardápio de uma página" apenas como PDF para imprimir **[ANT]** ([NN/g](https://www.nngroup.com/articles/avoid-pdf-for-on-screen-reading/)). Leitores de tela não interpretam a maioria dos PDFs, segundo um fornecedor com afirmações pouco citadas **[VEND]** ([JVF](https://jvf.com/why-restaurants-should-avoid-pdf-menus/)). A fonte de fornecedor diz que 77% dos clientes visitam o site antes de escolher e que cerca de 70% já desistiram por um site ruim, mas cita a pesquisa de segunda mão, sem verificação **[VEND]** ([UpMenu](https://www.upmenu.com/blog/best-restaurant-websites-design/)).

**Estilo típico (eixos).** *Alta gastronomia:* `aesthetic` Minimalist/Luxury, claro ou escuro, com serif elegante e um acento. *Casual e fast food:* `aesthetic` Flat de cor forte com botão "Pedir" grande. *Café e padaria:* `aesthetic` Organic + Illustrative em creme, kraft ou pastel, com tipo arredondado. *Bar:* `aesthetic` Dark + Retro ou Art Deco, com neon ou dourado **[S]**.

**Segura · expressiva · ousada.** *Segura:* o protótipo de cada variante. *Expressiva:* Minimalist de estética japonesa (A Single Pebble, branco e vermelho) ou Editorial com imprensa. *Ousada:* Neo-brutalist para fast food, Maximalist vibrante (as imagens caribenhas da Kokomo) ou Kinetic para bar. A troca é tirar o foco do cardápio ([UpMenu](https://www.upmenu.com/blog/best-restaurant-websites-design/)).

**Evitar.** Cardápio só em PDF, vídeo automático que deixa a página lenta e pop-up na entrada **[S]**. Uma estatística atribuída ao Google diz que 53% das visitas mobile são abandonadas acima de 3 s de carregamento. O dado é de segunda mão, por volta de 2016–2018 **[ANT][VEND]** ([JVF](https://jvf.com/why-restaurants-should-avoid-pdf-menus/)).

**Confiança.** Ranking do Yelp em destaque (Craft House), seção de imprensa (DANIEL, Adda, Kokomo) ([UpMenu](https://www.upmenu.com/blog/best-restaurant-websites-design/)), Michelin e guias, e notas do Google **[S]**.

**Imagem.** Pratos e salão reais, foto escura e moody na alta gastronomia **[S]**.

**Exemplos.** gramercytavern.com, danielnyc.com, jungsik.com, asinglepebble.com, thedeadrabbit.com, thefifthoc.com, thekebabshop.com e kokomonyc.com ([UpMenu](https://www.upmenu.com/blog/best-restaurant-websites-design/)). Noma, Tartine e Sweetgreen são **[O]**. Cafés e padarias ficaram sem exemplos, porque as listas específicas não foram lidas.

**Variantes.** Alta gastronomia, casual/fast food/rede, café/padaria e bar/coquetelaria, como no campo de estilo.

### F4. Agências de viagem, tours e experiências

**Objetivo e conversão.** No tour, a conversão é "Ver disponibilidade" num calendário com preço por data, junto com o mapa do ponto de encontro. Na agência de viagem sob medida, é um formulário "Comece a planejar" ou uma consulta **[S]**.

**Estrutura e mobile.** *Home:* busca por destino ou atividade, ou tiles de categoria, seguida de grade de tours em destaque. *Cards:* imagem, duração, tamanho do grupo, nota e preço "a partir de". *Detalhe:* galeria, destaques, roteiro dia a dia em acordeão, o que inclui e o que não inclui, mapa do ponto de encontro, calendário com preços, caixa sticky de reserva, avaliações e FAQ **[S]**.

**Regras de UI/UX com evidência.** O estudo do Baymard teve 1.700 h de testes e avaliou 7 sites em mais de 340 parâmetros. A página de detalhe do tour deve sempre trazer um mapa do ponto de partida, e o site deve linkar fontes de avaliação de terceiros, notas agregadas e prêmios ([Baymard](https://baymard.com/research-articles/tours-and-experiences-benchmark-2023)). Os usuários abriam o calendário para obter informação do tour, e calendários sem link para os detalhes forçavam desvios longos ([Baymard](https://baymard.com/ecommerce-design-examples/date-picker)).

**Estilo típico (eixos).** `aesthetic` Editorial de viagem + Flat/Material na grade de cards · `type` sans limpa com headlines bold · `color` guiada pela foto, com um acento de natureza ou aventura. Agências de luxo sob medida usam Editorial/Luxury com serif **[S]**.

**Segura · expressiva · ousada.** *Segura:* grade de cards com filtros. *Expressiva:* storytelling Editorial ou mapa ilustrado. *Ousada:* Immersive scroll de destino, no estilo dos sites de turismo Go Hawaii, Visit California, Discover Puerto Rico e Visit Philadelphia ([CyberOptik](https://www.cyberoptik.net/blog/best-travel-tourism-websites)). A troca é afastar a reserva do primeiro scroll **[S]**.

**Evitar.** Scroll-jacking em páginas de busca e calendário desconectado dos detalhes **[S]**.

**Confiança.** Avaliações de terceiros (Tripadvisor, Trustpilot, GetYourGuide), prêmios e endossos ([Baymard](https://baymard.com/research-articles/tours-and-experiences-benchmark-2023)). Certificações de sustentabilidade, licença de turismo e seguro **[S]**.

**Imagem.** Fotografia de destino e de grupos reais em atividade **[S]**.

**Exemplos.** Much Better Adventures, Take Walks, Ziptrek Ecotours, Wild Rover Tours e Extranomical Tours ([Baymard](https://baymard.com/research-articles/tours-and-experiences-benchmark-2023)). gohawaii.com e visitcalifornia.com ([CyberOptik](https://www.cyberoptik.net/blog/best-travel-tourism-websites)). GetYourGuide, Black Tomato e Intrepid são **[O]**.

### F5. Imobiliárias e corretores

**Objetivo e conversão.** A conversão começa numa barra de busca (toggle Comprar/Alugar, local, preço, quartos) e segue para a lista com mapa ao lado. Na página do imóvel, "Agendar visita" ou "Falar com o corretor" fica sticky **[S]**.

**Estrutura e mobile.** No desktop, resultados em lista e mapa lado a lado. No mobile, um toggle entre mapa e lista. Cards com carrossel de fotos, preço, quartos, banheiros, m², endereço, selo (Novo, Reduzido, Em negociação) e coração de favorito. Na página do imóvel, abas de galeria, planta, tour virtual e vídeo, grade de dados, mapa do bairro, classe energética onde se aplica (UE e Reino Unido), simulador de financiamento e card do corretor sticky **[S]**.

**Regras de UI/UX com evidência.** Compradores consideram "muito úteis" fotos (84%), plantas (55%), tours virtuais (43%) e vídeo (28%) **[ANT]** ([BoxBrownie/NAR 2022](https://www.boxbrownie.com/b/the-nar-report-that-helps-sell-homes-in-a-slowdown)). Numa amostra de mais de 25 mil anúncios de 2021, 94% não tinham tour virtual e 84% não tinham planta **[ANT]** ([Inman](https://inman.com/2021/07/08/vast-majority-of-real-estate-listings-lack-good-visuals-study)). As recomendações incluem filtros intuitivos, mapas interativos, comparação e design mobile-first ([Azuro Digital](https://azurodigital.com/real-estate-website-examples/)).

**Estilo típico (eixos).** *Portal ou agência:* `aesthetic` Swiss/Flat limpo · `type` sans neutra · `color` branco com um acento. *Agência de luxo:* `aesthetic` Luxury minimal ou Typographic-led · `color` preto, branco e pedra **[S]**.

**Segura · expressiva · ousada.** *Segura:* UI de listagem Flat. *Expressiva:* Luxury minimal com imagem em tela cheia e tours em vídeo (Altman Brothers) ou luxo limpo com tipografia refinada e filtros avançados (Fridman Group). *Ousada:* Typographic-led com "ar de galeria de arte" (Berdan) ou luxo imersivo em tons de terra (Caldera House). A troca é atrapalhar a busca ([Azuro Digital](https://azurodigital.com/real-estate-website-examples/)).

**Evitar.** Brutalist cru no luxo e scroll-jacking em páginas de listagem **[S]**.

**Confiança.** "Confiança se constrói com especificidade" ([Azuro Digital](https://azurodigital.com/real-estate-website-examples/)):

- números de vendas em destaque (Campion, os US$ 1,3 bi+ de Kumara Wilcoxon, os US$ 3 bi+ da Fridman);
- depoimentos;
- credenciais.

Um card do corretor com licença ou selo de verificado, telefone ou WhatsApp e tempo de resposta **[S]**.

**Imagem.** Fotografia profissional (HDR), planta e tour virtual ([Inman](https://inman.com/2021/07/08/vast-majority-of-real-estate-listings-lack-good-visuals-study)).

**Exemplos.** campionre.com, thealtmanbrothers.com, calderahouse.com, berdanrealestate.com e thefridmangroup.com ([Azuro Digital](https://azurodigital.com/real-estate-website-examples/)). Rightmove, Zillow, Idealista, Compass, Sotheby's e The Modern House são **[O]**.

### F6. Incorporadoras e lançamentos imobiliários

**Objetivo e conversão.** A conversão é "Registrar interesse", "Baixar o folder" ou "Agendar visita", sempre com um seletor de unidade **[S]**.

**Estrutura e mobile.** Landing do projeto com filme ou renders no hero, localização, tipos de unidade, implantação interativa ou seletor 3D do prédio com tabela de disponibilidade, áreas comuns, linha do tempo da obra, galeria, folder e formulário **[S]**. A Damac usa tours em Unreal Engine e filtros de unidade (andar, área, preço) que destacam as unidades num modelo 3D do prédio ([Azuro Digital](https://azurodigital.com/real-estate-website-examples/)).

**Regras de UI/UX com evidência.** Animações suaves e carregamento rápido sinalizam profissionalismo ([Azuro Digital](https://azurodigital.com/real-estate-website-examples/)). O seletor 3D precisa de uma alternativa em tabela **[S]**.

**Estilo típico (eixos).** `aesthetic` Luxury · `layout` hero de render · `motion` Immersive · `type` serif ou sans larga · `color` apagadas, guiadas pelos renders **[S]**.

**Segura · expressiva · ousada.** *Segura:* Luxury minimal com renders. *Expressiva:* storytelling Editorial de estilo de vida, como as "Stories" de Angela Andronache. *Ousada:* Dark/tech com Immersive 3D, como a Damac. A troca é performance e mobile ([Azuro Digital](https://azurodigital.com/real-estate-website-examples/)).

**Evitar.** Seletor 3D sem alternativa acessível e Brutalist cru **[S]**.

**Confiança.** Histórico da incorporadora, linha do tempo da obra e registro do empreendimento **[S]**.

**Imagem.** Renders, filme e fotos da obra **[S]**.

**Exemplos.** damacproperties.com ([Azuro Digital](https://azurodigital.com/real-estate-website-examples/)). O case da Berrow Projects não foi lido ([Solve](https://solve.co.uk/transformations/berrow-projects-website/)).

### F7. Espaços de eventos e serviços de casamento

**Objetivo e conversão.** A conversão é "Consulte sua data", "Pedir folder ou preços" ou "Agendar visita". Os sites de espaço giram em torno de "inquire", "schedule a tour" e "book a date", com muita foto e vídeo ([InsideOut](https://insideout.com/portfolio/wedding-venue-websites/)).

**Estrutura e mobile.** Filme no hero, espaços com capacidade por formato (sentado ou em pé), pacotes "a partir de" ou folder, galeria de casamentos reais, fornecedores indicados, hospedagem, FAQ, depoimentos e formulário com data, número de convidados e orçamento **[S]**.

**Regras de UI/UX com evidência.** Não há pesquisa de UX sobre sites de espaços de eventos, só portfólios de agência (lacuna).

**Estilo típico (eixos).** *Casamento:* `aesthetic` Editorial romântico + Luxury ou Organic · `type` script ou serif com sans · `color` blush, marfim, sálvia e dourado. *Espaço corporativo:* `aesthetic` Swiss/Flat · `layout` tabelas de capacidade e plantas · formulário de RFP **[S]**.

**Segura · expressiva · ousada.** *Segura:* Editorial romântico. *Expressiva:* Organic rústico (celeiro, campo) ou Art Deco (salão histórico). *Ousada:* Immersive com filme e scroll. A troca é o peso e o formulário ficar longe **[S]**.

**Evitar.** Brutalist cru e preço escondido atrás de várias etapas **[S]**.

**Confiança.** Depoimentos de clientes ([InsideOut](https://insideout.com/portfolio/wedding-venue-websites/)), imprensa de casamento do tipo "visto em" e galeria de casamentos reais **[S]**.

**Imagem.** Casamentos reais, o espaço vazio e montado, e o filme **[S]**.

**Exemplos.** hawkvalleyretreat.com, bentcreeknc.com, kellysresort.com e odessabythesea.com. São de um único portfólio de agência, então o estilo é homogêneo ([InsideOut](https://insideout.com/portfolio/wedding-venue-websites/)).

## Outros nichos: quanto mais o site é amostra do trabalho, maior a licença estética

O último grupo vai de nichos institucionais, que pedem prototipicidade alta, a nichos onde o visitante espera que o site seja a própria vitrine. No primeiro caso estão ONGs, universidades e museus na parte de planejar a visita. No segundo estão portfólios, arte contemporânea, festivais e conferências de design. Nenhum construtor tem categoria própria para museus. O mais próximo são "Arts & Culture", dentro de Nonprofits no Squarespace, e "Creative Arts" no Wix ([Squarespace](https://www.squarespace.com/templates); [Wix](https://www.wix.com/website/templates)).

### G1. ONGs, causas e instituições de caridade

**Objetivo e conversão.** A conversão é doar, de preferência de forma recorrente. Em 2025, **53%** das visitas a sites de ONGs vieram do celular, mas o desktop gerou 55% das transações e **70% da receita**. A doação média foi de US$ 145 no desktop e US$ 76 no mobile ([M+R Benchmarks](https://2025.mrbenchmarks.com/website-performance.html)).

**Estrutura e mobile.** Botão "Doar" sticky e de alto contraste, repetido como barra inferior no mobile. Hero com a missão e foto ou vídeo real. Faixa de impacto ("R$ X garante Y"), programas ou histórias em cards, prova (transparência financeira, avaliações, parceiros), voluntariado e newsletter, e rodapé com o registro legal **[S]**. Os padrões de 2026 são vídeo no hero, movimento com propósito, doação ligada ao resultado e navegação simples mesmo em escala ([Numiko](https://numiko.com/insights/the-best-non-profit-websites-2026)).

**Regras de UI/UX com evidência.** Na CaringBridge, trocar 3 valores sugeridos por 6 começando mais baixo levou a conversão de **0.96% para 2.0%** (n=4.159, 98.7% de confiança), sem queda significativa no valor médio **[ANT]** ([NextAfter](https://www.nextafter.com/?p=11643)). Deixar o formulário já na aba mensal, quando o pedido é mensal, levou de 0 para 4 doações recorrentes, numa amostra pequena (n=406) ([NextAfter](https://www.nextafter.com/?p=49869)). Sobre as carteiras digitais: 76% das ONGs oferecem PayPal, 47% Apple Pay e 40% Google Pay ([M+R Benchmarks](https://2025.mrbenchmarks.com/website-performance.html)). Em 2009, só 43% punham a missão na home e em 17% dos casos o usuário não achava onde doar **[ANT]** ([NonprofitPro/NN/g](https://www.nonprofitpro.com/article/nielsen-norman-group-releases-new-study-nonprofit-web-sites-estimates-organizations-could-double-online-donations-405368/)). Do conjunto sai uma especificação de formulário **[S]**:

- toggle entre doação única e mensal, já posicionado conforme o pedido;
- 4–6 valores começando baixo, cada um com uma linha de impacto;
- campo "outro valor";
- carteiras digitais no topo;
- formulário embutido na página.

**Estilo típico (eixos).** `aesthetic` Editorial documental sobre base Minimalist · `layout` hero com foto ou vídeo + cards de história · `motion` com propósito · `type` sans humanista ou serif · `color` light com um acento forte de marca **[S]**.

**Segura · expressiva · ousada.** *Segura:* Editorial documental. *Expressiva:* Kinetic ou Immersive a serviço da história, como o zoom no scroll da palavra "solution" na Farm Africa e o scroll em tela dividida da Obama Foundation, ou Illustrative para causas de crianças e comunidade. *Ousada:* identidade Neo-brutalist de campanha para grupos ativistas, como a Surfers Against Sewage, que tem mapa interativo da qualidade da água. A troca é afastar doadores mais velhos, que respondem pela maior parte da receita no desktop ([Numiko](https://numiko.com/insights/the-best-non-profit-websites-2026)) **[S]**.

**Evitar.** Luxury, que sugere dinheiro de doador gasto em aparência. Glass e Neumorphism nos formulários. Dark/tech pesado **[S]**.

**Confiança.** Explicar para onde vai o dinheiro: em 2009, só 4% diziam isso na home **[ANT]** ([NonprofitPro/NN/g](https://www.nonprofitpro.com/article/nielsen-norman-group-releases-new-study-nonprofit-web-sites-estimates-organizations-could-double-online-donations-405368/)). Valores com contexto, transparência financeira, selos de avaliação e registro legal **[S]**.

**Imagem.** Fotografia e vídeo reais dos beneficiários, com consentimento ([Numiko](https://numiko.com/insights/the-best-non-profit-websites-2026)).

**Exemplos.** childrenssociety.org.uk, wateraid.org/uk, obama.org, sas.org.uk, solar-aid.org (holofote que segue o cursor), ageofunion.com, farmafrica.org e edenprojects.org ([Numiko](https://numiko.com/insights/the-best-non-profit-websites-2026)).

### G2. Educação: escolas, universidades e escolas de idiomas

**Objetivo e conversão.** A conversão é "Fale conosco", "Agende uma visita", "Inscreva-se", "Faça o teste de nível" ou "Aula grátis". Nos testes da NN/g, **48%** dos usuários não perceberam que a universidade oferecia o curso que procuravam, mesmo existindo **[ANT]** ([NN/g](https://www.nngroup.com/articles/university-sites/)).

**Estrutura e mobile.** Hero com foto ou vídeo real do campus ou da turma, CTA principal (aula grátis, teste de nível ou visita) e secundário (folder). Buscador de cursos com filtros (idioma, nível CEFR A1–C2, formato, intensidade, data de início). Cards de curso com preço, horário e nível, acreditações, depoimentos, corpo docente, módulo de prazos e FAQ. No mobile, barra inferior sticky, no padrão da UT Austin **[S]**. As tendências de 2026 são imagem real em vez de banco, navegação por tipo de usuário e CTAs de inscrição e visita cedo e repetidos ([Freshy](https://freshysites.com/web-design-development/best-college-and-university-websites/)).

**Regras de UI/UX com evidência.** Identificar a instituição em todas as páginas, usar imagem autêntica, ter uma página "Sobre" com lista de fatos escaneável e prazos fáceis de achar, e não usar estilo "gimmicky" com cara de anúncio nem rótulos vagos **[ANT]** ([NN/g](https://www.nngroup.com/articles/university-sites/)). Páginas de professores convencem futuros alunos ([NN/g](https://www.nngroup.com/videos/university-faculty-pages/)). A Brown adia o autoplay do vídeo até o scroll para ganhar performance no mobile ([Freshy](https://freshysites.com/web-design-development/best-college-and-university-websites/)).

**Estilo típico (eixos).** *Universidade:* `aesthetic` Editorial institucional · `type` serif com sans · foto real. *Escola de idiomas:* `aesthetic` Flat/Material ou Minimalist amigável · `color` acentos vivos **[S]**.

**Segura · expressiva · ousada.** *Segura:* institucional ou Flat amigável. *Expressiva:* Typographic-led minimal com cara de galeria para escolas de arte, como a RISD, "minimalista, com ar de galeria e muito branco" ([Freshy](https://freshysites.com/web-design-development/best-college-and-university-websites/)), Illustrative para público infantil, ou Bento estilo SaaS para plataformas online como Lingoda e EF. *Ousada:* imersão em vídeo de tela cheia (Johns Hopkins). Brutalist ou Y2K só para escola de arte. A troca é performance e a clareza institucional **[S]**.

**Evitar.** Estilo de anúncio, slider de foto de banco e Brutalist ou Y2K fora de escola de arte **[S]**.

**Confiança.** Rankings e números, dados de empregabilidade **[ANT]** ([NN/g](https://www.nngroup.com/articles/university-sites/)), selos de acreditação, teste de nivelamento CEFR gratuito ([Colorlib](https://colorlib.com/wp/language-school-website-examples/)) e depoimentos em vídeo **[S]**.

**Imagem.** Alunos e professores reais, sem filtro, como na Penn ([Freshy](https://freshysites.com/web-design-development/best-college-and-university-websites/)).

**Exemplos.** risd.edu, jhu.edu, upenn.edu, admissions.utexas.edu, goshen.edu e brown.edu ([Freshy](https://freshysites.com/web-design-development/best-college-and-university-websites/)). lingoda.com ("estilo SaaS moderno", trial de 7 dias grátis), ef.edu (fontes variáveis próprias, CTA de folder sticky), kaplaninternational.com, enforex.com, jplinguistics.com e ltl-school.com ([Colorlib](https://colorlib.com/wp/language-school-website-examples/)).

**Variantes.** Universidade, escola de idiomas, escola infantil e plataforma online, conforme o campo de estilo **[S]**.

### G3. Museus, galerias e instituições culturais

**Objetivo e conversão.** Cerca de metade das visitas ao site serve para planejar a ida: **50%** no Indianapolis Museum of Art (n=4.074) e **47%** em 15 museus holandeses (cerca de 41 mil respostas). Comprar algo fica em 2.7–4% **[ANT]** ([Ecsite](https://www.ecsite.eu/sites/default/files/spokes5_website_motivations.pdf)).

**Estrutura e mobile.** Um utilitário de visita persistente, com horário do dia e status aberto/fechado, botão de ingressos e endereço. Hero com a exposição principal no tema de cor dela. Grade "Em cartaz" filtrável, conteúdo "Planeje sua visita", entradas para o acervo, sócio, loja e newsletter. O ingresso segue data → horário → tipo com seletor de quantidade **[S]**. As tendências de 2026 são indicadores de aberto/fechado ao vivo (Baltic, Guggenheim Bilbao), acervos centrados no objeto, cor por exposição (Nordiska, British Museum, Van Gogh), busca forte em escala (V&A) e coleções salvas sem login (MIT Museum, Cooper Hewitt) ([Numiko](https://numiko.com/insights/best-museum-and-gallery-websites-2026)).

**Regras de UI/UX com evidência.** O utilitário de visita fica acima da dobra, porque é o motivo de metade das visitas ([Ecsite](https://www.ecsite.eu/sites/default/files/spokes5_website_motivations.pdf)). Não há estudo sobre o funil de ingressos em museus (lacuna).

**Estilo típico (eixos).** `aesthetic` Minimalist/Swiss · `layout` imagem grande com grade · `type` contida · `color` preto e branco com acento por exposição **[S]**. O Rijksmuseum é "a arte primeiro, simples mas marcante" e a National Gallery é "discreta e calma" ([Numiko](https://numiko.com/insights/best-museum-and-gallery-websites-2026)).

**Segura · expressiva · ousada.** *Segura:* Minimalist/Swiss. *Expressiva:* Editorial para acervos contados como história, ou Kinetic, como a animação tipográfica de carregamento da Baltic. *Ousada:* scroll horizontal com paleta que muda (Van Gogh Museum) ou Brutalist "deliberadamente retrô" com microinterações (Nottingham Contemporary). A troca é que isso só funciona quando a logística de visita continua usável ([Numiko](https://numiko.com/insights/best-museum-and-gallery-websites-2026)).

**Evitar.** Glass, Neumorphism e Claymorphism, que competem com as obras. Maximalism pesado, que esconde a logística **[S]**. A Numiko desenhou o British Museum e o Science Museum e diz isso na própria lista, o que é viés de curadoria.

**Confiança.** Indicador "em exibição" (V&A), status ao vivo e preços claros ([Numiko](https://numiko.com/insights/best-museum-and-gallery-websites-2026)).

**Imagem.** As obras em alta resolução **[S]**.

**Exemplos.** rijksmuseum.nl, vangoghmuseum.nl, nationalgallery.org.uk, nottinghamcontemporary.org, guggenheim-bilbao.eus (Webby 2023), baltic.art, mitmuseum.mit.edu e vam.ac.uk ([Numiko](https://numiko.com/insights/best-museum-and-gallery-websites-2026)).

### G4. Portfólios criativos: fotógrafos, designers e ilustradores

**Objetivo e conversão.** A conversão é contato, encomenda, contratação ou agendamento, e o trabalho é a própria interface ([Framer](https://www.framer.com/blog/photography-portfolio-websites/)).

**Estrutura e mobile.** Nome ou logo e menu de 3–5 itens. A home é uma grade de trabalhos: masonry para fotógrafos, cases grandes para designers. A página de projeto é full-bleed para foto, e para design segue o template de case com contexto, papel, processo e resultado. Página "Sobre" com retrato, clientes e imprensa, e formulário com campo de data para eventos **[S]**. Os padrões vistos incluem alternar visualização P/M/G (Justin Bettman), carrossel horizontal com índice por cor (Ausra Babiedaite) e home em tela dividida (Samuel Angibaud) ([Framer](https://www.framer.com/blog/photography-portfolio-websites/)).

**Regras de UI/UX com evidência.** Imagens em torno de 2400–2560×1600 px, navegação enxuta, estilo do site alinhado ao olhar do fotógrafo, logos de clientes, autorretrato com bio e pelo menos 15–25 das melhores imagens ([Framer](https://www.framer.com/blog/photography-portfolio-websites/)). Em portfólios de UX, 3–5 cases detalhados e escaneáveis, porque recrutadores "muito raramente" leem palavra por palavra. A base é uma pesquisa com 204 profissionais **[ANT]** ([NN/g](https://www.nngroup.com/articles/ux-design-portfolios/)).

**Estilo típico (eixos).** `aesthetic` Minimalist · `layout` grade de trabalhos · `color` branco de galeria ou quase-preto · `type` pequena · muito branco **[S]**.

**Segura · expressiva · ousada.** *Segura:* Minimalist de galeria. *Expressiva:* Typographic-led ou Swiss para designers gráficos, e Editorial para fotojornalismo. *Ousada:* Kinetic e Immersive para motion e 3D. Collage, Maximalist ou Illustrative para ilustradores. Brutalist ou Neo-brutalist para designers experimentais. A troca é aceitável porque o visitante espera ver o estilo do autor **[S]**.

**Evitar.** Estilos que competem com o trabalho, como Glass, Claymorphism, bento carregado para fotógrafos e molduras coloridas em volta das fotos **[S]**.

**Confiança.** Logos de clientes e publicações, retrato e bio ([Framer](https://www.framer.com/blog/photography-portfolio-websites/)).

**Imagem.** O próprio trabalho, sem moldura **[S]**.

**Exemplos.** A matéria do Framer cita Justin Bettman, Dao for Design, Hannah Miles, Ausra Babiedaite, Samuel Angibaud, Keith Greenbaum e Christopher Ireland, mas sem URLs e sem confirmação de que estão no ar ([Framer](https://www.framer.com/blog/photography-portfolio-websites/)).

### G5. Arquitetos e designers de interiores

**Objetivo e conversão.** O visitante quer explorar projetos e depois contatar ou contratar o escritório ([Webflow](https://webflow.com/blog/best-architecture-websites)).

**Estrutura e mobile.** Header mínimo, hero em full-bleed de um projeto-assinatura, índice de projetos com alternância grade/lista e filtros por tipologia, página de projeto com sequência de imagens grandes e tabela de dados (local, ano, área, status, colaboradores), página do estúdio com processo e prêmios, e contato com mapa. Designers de interiores acrescentam antes e depois, mood boards, níveis de serviço e formulário com orçamento e prazo **[S]**.

**Regras de UI/UX com evidência.** Galeria interativa por tipologia, só as páginas necessárias, menu sempre no mesmo lugar, mobile-first, e layouts que "espelham a linguagem arquitetônica" do escritório ([Webflow](https://webflow.com/blog/best-architecture-websites)).

**Estilo típico (eixos).** `aesthetic` Minimalist/Swiss · `layout` grid · `color` monocromático · `type` sans fina · muito branco ([Webflow](https://webflow.com/blog/best-architecture-websites)) **[S]**.

**Segura · expressiva · ousada.** *Segura:* Minimalist/Swiss. *Expressiva:* Editorial com histórias de projeto em formato de revista, Luxury com serif e neutros quentes para residencial de alto padrão, ou Organic para práticas biofílicas. *Ousada:* Brutalist com a honestidade do concreto, para estúdios de vanguarda, ou Immersive/3D para estúdios de visualização. A troca é perder clientes residenciais conservadores **[S]**.

**Evitar.** Claymorphism, Y2K e Maximalism. Glass só como ligação conceitual deliberada, como no tema de vidro do ArchUnion, nunca como padrão ([Webflow](https://webflow.com/blog/best-architecture-websites)) **[S]**.

**Confiança.** Prêmios e imprensa, equipe e dados técnicos de cada projeto **[S]**.

**Imagem.** Fotografia de arquitetura profissional em tela cheia ([Webflow](https://webflow.com/blog/best-architecture-websites)).

**Exemplos.** reloadarchitecture.com, blackboxarch.com, fcarchitect.co.nz, garytoddarchitecture.co.nz, archunion.art e smp-arch.com. Vários itens da lista são sites de vitrine *.webflow.io, não escritórios confirmados ([Webflow](https://webflow.com/blog/best-architecture-websites)). Não há exemplos reais de designers de interiores com detalhes (lacuna).

### G6. Marcas pessoais, palestrantes e autores

**Objetivo e conversão.** As conversões são "Contrate para palestra", "Compre o livro", "Assine a newsletter ou baixe o material" e "Compre o curso ou ingresso" ([talks.co](https://talks.co/p/public-speaker-website)).

**Estrutura e mobile.** A estrutura comum, segundo uma revisão de 27 sites, é ([talks.co](https://talks.co/p/public-speaker-website)):

- foto, nome, tagline e expertise acima da dobra;
- temas, bio, livros e contato no menu;
- logos de clientes e de mídia, depoimentos;
- vídeo de palestra;
- CTA de contratação no header;
- material gratuito;
- página para organizadores de eventos.

A síntese acrescenta um kit de mídia (fotos, bio, rider técnico) e um formulário com data, local, público e orçamento **[S]**.

**Regras de UI/UX com evidência.** Design simples quando o conteúdo é denso, ousado quando o estilo de palestra é enérgico ([talks.co](https://talks.co/p/public-speaker-website)).

**Estilo típico (eixos).** `aesthetic` Editorial (layout de revista, serif display, foto grande) ou marketing pessoal ousado (acento de alto contraste, tipo grande) **[S]**.

**Segura · expressiva · ousada.** *Segura:* Editorial. *Expressiva:* Typographic-led minimal para líderes de pensamento, ou Organic suave para bem-estar e espiritualidade, como o "sereno e minimalista" de Eckhart Tolle. *Ousada:* Dark com tipografia forte (Ken Hughes), "ousado e de alta energia" (Tony Robbins), ou Retro/Illustrative ajustado ao gênero de quem escreve ficção. A troca é que o estilo precisa casar com a pessoa ([talks.co](https://talks.co/p/public-speaker-website)) **[S]**.

**Evitar.** Bento genérico de SaaS e Glass, que fazem a pessoa parecer um software. Maximalism que esconde o CTA de contratação **[S]**.

**Confiança.** Faixa "visto em" e "palestrou em", depoimentos e vídeo ([talks.co](https://talks.co/p/public-speaker-website)).

**Imagem.** Retrato grande, recortado ou em full-bleed, e fotos em palco **[S]**.

**Exemplos.** simonsinek.com, jaybaer.com, tonyrobbins.com, melrobbins.com, brenebrown.com, eckharttolle.com, stevenbartlett.com, kenhughes.info e garyvaynerchuk.com. As datas de captura não são informadas ([talks.co](https://talks.co/p/public-speaker-website)).

### G7. Eventos, conferências e festivais

**Objetivo e conversão.** A conversão é comprar ingresso ou se inscrever. As metas secundárias são ver palestrantes ou line-up, conferir a programação, patrocinar e resolver a logística ([htmlburger](https://htmlburger.com/blog/conference-websites/)).

**Estrutura e mobile.** Hero com nome, data, cidade, contagem regressiva e "Comprar ingresso", sticky no header e como barra inferior no mobile. Faixa de números, grade de palestrantes com hierarquia de headliners e agenda com abas por dia e filtros de trilha ou palco ("adicionar ao calendário", "minha agenda"). Cards de ingresso com estado de esgotado e badge de early-bird, vídeo da edição anterior, patrocinadores por cota, mapa e FAQ. Festivais acrescentam uma grade palco × horário com swipe horizontal **[S]**. A Ticket Fairy recomenda line-up com os headliners separados visualmente, programação com acordeões, ingressos "na frente e no centro" com CTAs de alto contraste, checkout curto, mídia pesada longe do caminho de compra e mapa interativo do evento ([Ticket Fairy](https://www.ticketfairy.com/blog/2025/02/11/how-to-build-a-music-festival-website-the-perfect-guide/)).

**Regras de UI/UX com evidência.** Comprimir as imagens para aguentar os picos da abertura de vendas e personalizar o template o bastante para "não parecer um clone genérico" ([Ticket Fairy](https://www.ticketfairy.com/blog/2025/02/11/how-to-build-a-music-festival-website-the-perfect-guide/)). Responder logo as perguntas-chave, repetir os CTAs e usar interatividade com propósito ([htmlburger](https://htmlburger.com/blog/conference-websites/)).

**Estilo típico (eixos).** Cada edição é uma campanha, então este é o nicho com mais licença **[S]**:

- *Conferência de tecnologia:* Dark/tech com gradiente ou Neo-brutalist, e Bento no "por que participar".
- *Conferência de design:* Kinetic, Immersive e Swiss.
- *Festival de música:* Maximalist, Collage, Retro, Y2K ou Illustrative, guiados pelo pôster.
- *Evento acadêmico ou de associação:* Flat minimal.

**Segura · expressiva · ousada.** *Segura:* Flat ou Dark/tech com agenda clara. *Expressiva:* a identidade de campanha da edição, como o vermelho animado do Circles ou as formas geométricas vibrantes do Red Hat Summit, que tem um quiz para montar a agenda pessoal. *Ousada:* o hero com som ambiente e muita interação da Awwwards Conference. A troca é performance no pico de vendas ([htmlburger](https://htmlburger.com/blog/conference-websites/)).

**Evitar.** WebGL pesado ou vídeo automático no caminho do ingresso, e Glass de pouco contraste em CTAs e programação **[S]**.

**Confiança.** Citação de imprensa no hero (Web Summit), números de escala (Ai4), lembrete de urgência nos CTAs (WaysConf) e uma carta "convença seu chefe" para baixar (Inbound) ([htmlburger](https://htmlburger.com/blog/conference-websites/)).

**Imagem.** Vídeo e galeria de edições anteriores, e retratos dos palestrantes **[S]**.

**Exemplos.** conference.awwwards.com, websummit.com, redhat.com/en/summit, ai4.io/vegas, waysconf.com, circlesconference.com, dublintechsummit.tech e inbound.com. Vários são edições de 2021–2024 **[ANT]** ([htmlburger](https://htmlburger.com/blog/conference-websites/)).

**Variantes.** Tecnologia, design, música, acadêmico e casamento (ver F7), como no campo de estilo.

## A matriz cruzada põe os 47 nichos contra o catálogo inteiro

As duas tabelas condensam os cartões para a etapa de recomendação. Todas as células são síntese **[S]** a partir das notas e dos cartões. Nenhuma vem de um estudo que compare estilos dentro de um nicho. A legenda é:

- **T**: típico, o protótipo do nicho e a direção "segura".
- **t**: típico de um subnicho (luxo, eco, clássico etc.).
- **✓**: funciona, ou seja, diferencia sem ferir a confiança.
- **!**: arriscado ou ousado, aceitável só com guardrails ou num subnicho, com a troca declarada no cartão.
- **✗**: evitar.
- **–**: sem sinal nas fontes.

As colunas de estética usam estas abreviações: Min (Minimalist), Swi (Swiss), Edi (Editorial), Fla (Flat/Material), Typ (Typographic-led), Ill (Illustrative), Org (Organic), Sca (Scandinavian/Japandi), Lux (Luxury), Ret (Retro), Bru (Brutalist), NeoB (Neo-brutalist), Y2K, Max (Maximalist), Col (Collage) e Dark (Dark/tech).

| Nicho | Min | Swi | Edi | Fla | Typ | Ill | Org | Sca | Lux | Ret | Bru | NeoB | Y2K | Max | Col | Dark |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A1 Moda | T | T | ✓ | t | ✓ | – | t | – | t | – | ✗ | t | ! | – | – | ! |
| A2 Beleza | T | t | – | t | – | – | t | – | t | – | – | – | ! | ! | – | ✗ |
| A3 Alimentos DTC | t | ✗ | t | t | ✓ | T | t | – | – | T | – | T | – | ! | ! | – |
| A4 Artesanal | T | – | ✓ | – | – | ✓ | T | t | – | ✓ | – | – | – | – | ! | ✗ |
| A5 Casa/móveis | T | – | ✓ | t | – | – | t | T | t | – | ✗ | – | ✗ | – | – | – |
| B1 Emergência | ! | ! | – | T | ! | ✓ | – | – | – | t | – | ! | ✗ | ✗ | ✗ | ! |
| B2 Pintores | – | – | ✓ | T | – | – | – | – | – | – | – | ! | – | – | – | – |
| B3 Limpeza | t | – | – | T | – | ✓ | t | t | t | – | – | – | – | – | – | ✗ |
| B4 Jardinagem | ✓ | – | t | T | – | – | t | – | t | – | – | – | – | – | – | – |
| B5 Mudanças | – | – | – | T | ✓ | ✓ | – | – | – | – | – | ! | – | – | – | – |
| B6 Oficinas | ! | – | – | T | – | ✓ | – | – | ! | t | – | – | – | – | – | t |
| B7 Instaladores | ✓ | – | – | T | ✓ | ✓ | – | – | – | – | – | – | – | – | – | – |
| C1 SaaS | T | ✓ | ✓ | T | ✓ | ! | – | – | – | ! | – | ! | – | ✗ | – | T |
| C2 IA | ✓ | – | ✓ | – | ✓ | ✓ | ✓ | – | – | ! | – | – | – | – | – | T |
| C3 Apps | ✓ | – | – | T | – | t | – | – | – | – | ✗ | – | ! | – | – | t |
| C4 Cursos | T | – | ✓ | t | – | ✓ | T | – | ! | ! | – | ! | – | – | ! | ✗ |
| C5 Bens digitais | T | – | – | – | – | – | – | – | – | ! | – | ✓ | ! | ! | – | t |
| C6 Agências | ✓ | T | T | ! | T | ✓ | – | – | – | ! | ! | ! | – | ! | ✓ | ✓ |
| D1 Fintech | T | ✓ | ✓ | T | ✓ | t | – | – | ✓ | – | ✗ | ! | ✗ | ✗ | ✗ | t |
| D2 Contadores | ✓ | – | ✓ | T | – | ✓ | ✓ | – | – | – | ✗ | ✗ | ✗ | ✗ | ✗ | ! |
| D3 Seguros | ✓ | – | – | T | – | t | – | – | – | – | ✗ | ✗ | ✗ | ✗ | ✗ | – |
| D4 Advocacia | ✓ | ✓ | T | – | ✓ | – | – | – | t | – | ✗ | ✗ | ✗ | ✗ | ✗ | ! |
| D5 Consultorias | ✓ | T | T | – | ✓ | – | – | – | ✓ | – | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ |
| D6 Patrimônio | ✓ | – | ✓ | – | – | – | – | – | T | – | ✗ | ✗ | ✗ | ✗ | ✗ | – |
| D7 Notários | ✓ | – | – | T | – | – | ✓ | – | – | – | ✗ | ✗ | ✗ | ✗ | ✗ | – |
| E1 Clínicas | T | – | ✓ | T | – | ✓ | ✓ | ✓ | – | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| E2 Odontologia | T | – | – | T | – | ! | ✓ | – | – | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| E3 Terapia | T | ✓ | – | – | ✓ | – | T | – | – | – | – | – | ✗ | ! | – | ! |
| E4 Salões/barbearias/unhas | T | – | ✓ | – | – | – | – | – | t | t | – | ! | ! | ! | ! | t |
| E5 Spas/estética | ✓ | – | ✓ | – | – | – | T | ✓ | T | – | – | – | – | – | – | – |
| E6 Academias | – | – | ✓ | – | ! | – | – | – | ✓ | – | – | ! | ! | – | – | T |
| E7 Yoga/pilates | T | – | ✓ | – | – | ✓ | T | – | – | – | – | – | ! | – | – | ! |
| E8 Fisio/holístico | T | – | – | T | – | ✓ | t | ✓ | – | ✗ | ✗ | – | ✗ | ✗ | ✗ | ! |
| F1 Hotéis | t | – | T | – | – | t | t | t | T | t | ✗ | ! | ! | ! | – | – |
| F2 Aluguel temporada | T | – | ! | t | – | – | ✓ | T | – | – | – | – | – | – | – | – |
| F3 Restaurantes/bares | T | – | ✓ | t | – | t | t | ✓ | t | t | – | ! | – | ! | – | t |
| F4 Viagem/tours | ✓ | – | T | T | – | ✓ | – | – | t | – | – | – | – | – | – | – |
| F5 Imobiliárias | ✓ | T | ✓ | T | ! | – | – | – | t | – | ✗ | – | – | – | – | – |
| F6 Incorporadoras | ✓ | – | ✓ | – | – | – | – | – | T | – | ✗ | – | – | – | – | ! |
| F7 Espaços/casamentos | ✓ | t | T | t | – | – | t | – | T | – | ✗ | – | – | – | – | – |
| G1 ONGs | T | – | T | – | ✓ | ✓ | – | – | ✗ | – | – | ! | – | – | – | ✗ |
| G2 Educação | ✓ | ✓ | T | T | ✓ | ✓ | – | – | – | – | ! | – | ! | – | – | – |
| G3 Museus | T | T | ✓ | – | ✓ | – | – | – | – | ! | ! | – | – | ✗ | – | – |
| G4 Portfólios | T | ✓ | ✓ | – | ✓ | ! | – | – | – | – | ! | ! | – | ! | ! | t |
| G5 Arquitetos/interiores | T | T | ✓ | – | – | – | ✓ | – | ✓ | – | ! | – | ✗ | ✗ | – | – |
| G6 Marcas pessoais | ✓ | – | T | – | ✓ | ! | ✓ | – | – | ! | – | – | – | ✗ | – | ! |
| G7 Eventos/festivais | ✓ | t | – | t | ✓ | t | – | – | – | t | – | t | t | t | t | t |

A segunda tabela cobre os modificadores de `layout`, `surface` e `motion`, mais duas candidatas de nicho.

| Nicho | Bento | Glass | Neu | Clay | Kinetic | Immersive | Art Deco | Cyberpunk/Retrofuturism |
|---|---|---|---|---|---|---|---|---|
| A1 Moda | – | – | – | – | ! | ! | – | – |
| A2 Beleza | – | ! | – | ✓ | – | – | – | ✗ |
| A3 Alimentos DTC | – | – | ✗ | – | ✓ | ! | – | – |
| A4 Artesanal | – | – | – | – | – | ✗ | – | ✗ |
| A5 Casa/móveis | ✓ | – | – | – | – | ! | ! | – |
| B1 Emergência | ✓ | ✗ | ✗ | – | ✗ | ✗ | – | – |
| B2 Pintores | – | ✗ | ✗ | – | – | ✗ | – | – |
| B3 Limpeza | – | ✗ | ✗ | ✓ | – | – | – | – |
| B4 Jardinagem | – | ✗ | – | – | – | ! | – | – |
| B5 Mudanças | – | – | – | – | ✗ | ✗ | – | – |
| B6 Oficinas | – | ✗ | – | – | – | – | – | – |
| B7 Instaladores | ✓ | – | – | ! | – | – | – | – |
| C1 SaaS | T | ! | ✗ | ✗ | – | ! | – | ✗ |
| C2 IA | t | T | – | – | ✓ | – | – | ! |
| C3 Apps | – | – | – | ! | – | ✗ | – | – |
| C4 Cursos | – | – | – | – | – | ✗ | – | ✗ |
| C5 Bens digitais | ✓ | ✗ | – | – | – | – | – | – |
| C6 Agências | – | – | – | – | T | T | – | – |
| D1 Fintech | ✓ | ! | ✗ | ! | ! | ! | – | ! |
| D2 Contadores | ✓ | – | ✗ | – | ! | ✗ | – | – |
| D3 Seguros | – | – | ✗ | ! | – | ✗ | – | – |
| D4 Advocacia | ✓ | – | ✗ | ✗ | ✗ | ! | t | – |
| D5 Consultorias | ✓ | – | – | – | ! | ! | – | – |
| D6 Patrimônio | – | – | ✗ | ✗ | – | ! | – | – |
| D7 Notários | – | – | ✗ | ✗ | – | – | – | – |
| E1 Clínicas | – | ✗ | ✗ | – | ✗ | ✗ | – | ✗ |
| E2 Odontologia | ✓ | ✗ | ✗ | – | ✗ | ✗ | – | ✗ |
| E3 Terapia | – | – | – | – | ✗ | ✗ | – | ✗ |
| E4 Salões/barbearias/unhas | – | – | – | – | ✓ | – | – | – |
| E5 Spas/estética | ✓ | – | – | – | – | ! | – | – |
| E6 Academias | – | – | – | – | ✓ | – | – | – |
| E7 Yoga/pilates | – | – | – | – | ✓ | – | – | – |
| E8 Fisio/holístico | – | ✗ | ✗ | – | ✗ | ✗ | – | ✗ |
| F1 Hotéis | ✓ | ✗ | ✗ | ✗ | ✓ | t | – | – |
| F2 Aluguel temporada | – | ✗ | ✗ | – | – | – | – | – |
| F3 Restaurantes/bares | – | ✗ | ✗ | ✗ | ! | ! | t | – |
| F4 Viagem/tours | – | – | – | – | – | ! | – | – |
| F5 Imobiliárias | – | – | – | – | – | ! | – | – |
| F6 Incorporadoras | – | – | – | – | – | ! | – | – |
| F7 Espaços/casamentos | – | – | – | – | – | ! | ✓ | – |
| G1 ONGs | – | ✗ | ✗ | – | ✓ | ! | – | – |
| G2 Educação | ✓ | – | – | – | – | ! | – | – |
| G3 Museus | – | ✗ | ✗ | ✗ | ✓ | ! | – | – |
| G4 Portfólios | ✗ | ✗ | – | ✗ | ! | ! | – | – |
| G5 Arquitetos/interiores | – | ! | – | ✗ | – | ! | – | – |
| G6 Marcas pessoais | ✗ | ✗ | – | – | ! | – | – | – |
| G7 Eventos/festivais | t | ✗ | – | – | t | ! | – | ! |

A leitura cruzada mostra três padrões. Primeiro, as colunas **Bru, NeoB, Y2K, Max e Col** ficam quase inteiras em ✗ nas famílias D e E e passam para ! ou t nas famílias C (agências, bens digitais) e G (portfólios, festivais). Esse é o gradiente de distância tolerada em forma de tabela. Segundo, **Glass e Neu** quase nunca são positivos. Glass só aparece como típico na IA, onde já é clichê, e como risco em beleza, fintech e arquitetura conceitual. Isso confirma a regra do catálogo de usar glass só na navegação ([Apple WWDC25](https://developer.apple.com/fr/videos/play/wwdc2025/219/)). Terceiro, **Immersive** é "!" em quase toda parte e só é típico em agências e hotéis de luxo. Mesmo nesses casos, o Baymard mostra que a reserva some sob a animação ([Baymard](https://baymard.com/blog/travel-accommodations-booking-search)).

## Construtores de IA perguntam o setor e decidem o estilo por "personalidade"

Os construtores de IA mais usados perguntam o tipo de negócio primeiro, mas o estilo visual vem de outro input ou de ajustes posteriores na conversa:

- **Squarespace Blueprint** é o mais explícito. O onboarding pede o tipo de negócio e o objetivo do site. Depois vêm o título e uma de **sete personalidades** (Professional, Playful, Sophisticated, Friendly, Bold, Quirky, Innovative), 9 tipos de seção para a home, 6 tipos de página (About, Contact, Shop, Services, Appointments, Course), 4 paletas por personalidade e 2 pares de fontes por personalidade, 14 no total. Cores e fontes só podem ser mudadas depois, no editor ([Website Builder Expert](https://www.websitebuilderexpert.com/?p=123850)).
- **Wix** faz de 4 a 5 perguntas: nome, tipo de conteúdo, objetivos e diferencial, e para lojas também público e produtos. O estilo vem depois, de um dos mais de 2.000 templates ou de um tema gerado e ajustado por chat ("pastel", "neon pink"), com botões "Generate new theme" e "Shuffle colors" ([Website Builder Expert](https://www.websitebuilderexpert.com/website-builders/how-use-wix-ai/)).
- **Durable** pede tipo de negócio, nome e local e gera o site em cerca de 30 segundos, "selecionando um template adequado". A lógica por setor não é documentada ([TechRadar](https://www.techradar.com/pro/software-services/durable)). Os controles posteriores são paleta, cantos, fontes e shuffle ([Durable](https://help.durable.com/en/articles/15199763-designing-your-site-colors-fonts-and-corners)).
- **Framer AI** parte de um prompt livre e não descreve presets por setor ([Framer](https://www.framer.com/solutions/ai-website-builder/)).
- **Relume** mostra os 3 melhores conceitos com descrições curtas ([Relume](https://resources.relume.io/resources/docs/concept-creation-using-the-relume-style-guide-builder)).
- **v0, Lovable e Bolt** caem no "visual shadcn" quando ninguém customiza ([Anna Arteeva](https://annaarteeva.substack.com/p/design-systems-lovable-bolt-v0-and)).
- Os inputs e padrões do **Hostinger** e do **10Web** não foram verificados.

**Nenhum fornecedor publica uma tabela setor→paleta→fonte→estilo.** O mais perto disso é a Zarla, que atribui paletas por subnicho nas próprias guias. Em contabilidade: creme com serif para o estabelecido, roxo e lima para o CPA de startup e gradiente azul-roxo para imposto cripto. Em notários: navy meia-noite com ciano, sálvia com dourado e ameixa com dourado antigo ([Zarla](https://www.zarla.com/guides/accounting-website-examples); [Zarla](https://zarla.com/guides/notary-website-examples)).

Os marketplaces confirmam o setor como principal modelo mental, e todos o organizam em dois níveis:

- O **Framer** tem 10 grupos com 4 subcategorias cada, de Portfolio, Software, Agency e Ecommerce até Services, Health, Publishing, Real Estate, Hospitality e Events ([Framer](https://www.framer.com/marketplace/templates/)).
- O **Squarespace** separa 10 grupos de "Solutions", com 6 subtipos cada, de um eixo de tipo de produto: lojas, portfólios, agendamento, doações e lançamentos limitados ([Squarespace](https://www.squarespace.com/templates)).
- O **Wix** tem 15 indústrias ([Wix](https://www.wix.com/website/templates)).
- O **Shopify** tem 1.343 temas, 20 filtros de indústria e um filtro de tamanho de catálogo com contagens visíveis: 27 temas para um produto, 102 para poucos, 885 para alguns e 329 para muitos ([Shopify](https://themes.shopify.com/themes)).
- O **ThemeForest** tem mais de 24.900 templates HTML ([ThemeForest](https://themeforest.net/category/site-templates)), e o **Webflow**, mais de 7.000 ([Webflow](https://webflow.com/templates)).

Nenhum mostra contagem por categoria, então não dá para montar um ranking de demanda.

O padrão do mercado tem dois eixos. **O setor define páginas, seções e imagem. A personalidade define paleta, par tipográfico e tom.** Os cartões deste relatório mostram que falta um terceiro eixo que os construtores ignoram: **o subnicho ou faixa de preço**, que muda o protótipo dentro do mesmo setor. Luxo e fast fashion, emergência e paisagismo de design, incumbente e insurtech, barbearia e nail studio são exemplos. O filtro de tamanho de catálogo do Shopify é o único caso desse eixo exposto ao usuário. A tabela abaixo projeta o vocabulário de personalidade do Squarespace nos estilos do catálogo. É útil como ponte, mas é síntese, não dado de fornecedor **[S]**.

| Personalidade | Estéticas do catálogo | Modificadores coerentes | Nichos onde cabe sem atrito |
|---|---|---|---|
| Professional | Swiss, Minimalist, Flat/Material | Bento com tile âncora, motion micro | finanças, advocacia, SaaS B2B, clínicas, consultorias |
| Sophisticated | Luxury, Editorial, Art Deco | serif editorial, fades lentos | hotéis, patrimônio, moda de luxo, arquitetura, casamentos |
| Friendly | Organic, Flat arredondado, Illustrative | radius grande, paleta quente | limpeza, odontologia, terapia, ONGs, escolas de idiomas |
| Playful | Illustrative, Clay, Neo-brutalist leve | micro saltitante | DTC de alimentos, apps de consumo, público infantil |
| Bold | Typographic-led, Neo-brutalist, Dark | Kinetic só no headline | academias, streetwear, conferências tech, palestrantes |
| Quirky | Collage, Maximalist, Y2K, Retro | marquee com pausa | festivais, barbearias ousadas, makers, criadores indie |
| Innovative | Dark/tech, Retrofuturism, Swiss | aurora contida, Bento | SaaS, IA, fintech, apps pro |

Essa tabela só vale quando cruzada com a matriz. "Bold" numa clínica deve cair em tipografia e cor fortes sobre o esqueleto clínico, nunca em Neo-brutalist, porque a coluna NeoB de E1 é ✗.

## O registro de incertezas deve viajar junto com cada recomendação

| Item | Situação | Implicação para a skill |
|---|---|---|
| Exemplos de sites | Só a BOXT foi buscada ao vivo (out. 2026). Os demais vêm de roundups de 2024–2026 e podem ter sido redesenhados. Os tokens de Graza e Gumroad são de extração de terceiros, e o Gumroad pode ter perdido o `box-shadow` | conferir com screenshot antes de usar como referência |
| Exemplos **[O]** | PostHog, Anthropic, Mistral, Lovable, Cursor, ElevenLabs, MasterClass, Maven, Aman, Noma, Rightmove e outros: conhecimento prévio sem fonte | nunca citar sem checar |
| Sites extintos **[✝]** | getbellhop.com, buildspace.so, Ueno, Apollo for Reddit. A Smile Direct Club deve estar encerrada **[O]** | excluir das listas |
| Evidência antiga **[ANT]** | Google/Ipsos 2013 (click-to-call), NN/g 2006, 2009, 2014/16 e 2019, Fogg 2002, Tuch 2012, motivações de museus 2012–13, NextAfter 2015, NAR 2022, BoxBrownie 2021, BRIX 2023, lista de advisors 2019 | tratar como direção, não como benchmark atual |
| Estatísticas de fornecedor **[VEND]** | ganhos de página de preços (m3ter), conversão mobile × desktop de patrimônio (Webtonic), 77%/70% de restaurantes (UpMenu), 5–10% de download de app e "2× com vídeo" (Swift Kit), "300%" de formulário em etapas (Venture Harbour), 53% de abandono acima de 3 s | não exibir como fato ao usuário final |
| Conteúdo pago | diretrizes do Baymard para beleza, furniture, datas e quartos. Relatório B2B da NN/g | só os títulos e resumos públicos foram usados |
| Mapeamentos de estilo | protótipos e matriz são síntese. Não há censo quantitativo de paleta, serif ou radius por nicho, e "clínico branco e azul" é prior forte mas não medido | tratar a matriz como prior ajustável |
| Bento e glass em finanças | inferidos da prática de SaaS, sem nenhuma fonte de finanças | marcar como hipótese |
| Conversão de design distintivo | nenhum dado público em nenhum nicho, nem para sites premiados | não prometer ganho de conversão por estilo |
| Correlação prototipicidade–confiança | os valores do artigo IJHCS 2023 não foram obtidos. Não há réplica da medição de homogeneização na era da IA | pesquisa futura |
| Cobertura geográfica | fortemente EUA, Reino Unido e Austrália. Quase nada de Alemanha/DACH, Brasil, Japão, Coreia ou América Latina (exceções: Buckler no Brasil, Fuoripista na Itália, Sebastian Lundberg na Dinamarca, Ramify/Qonto/Yomoni na França, Damac nos Emirados). WhatsApp, Meisterbetrieb, classe energética da UE e notariado latino são extrapolações | validar convenções locais antes de lançar em mercados não anglófonos |
| Nichos sem fonte de design | pintores, telhados, mudanças, limpeza eco, salões de cabelo, holístico (acupuntura, naturopatia, Ayurveda), designers de interiores reais, consultores solo, cafés e padarias | cartões finos; priorizar pesquisa |
| Templates de marketplace | listas de temas do Shopify por nicho não verificadas (robots bloqueou). Galerias do Squarespace, Godly, Land-book e Siteinspire por nicho não lidas | não citar nomes de temas como prova |
| Seleção dos exemplos | roundups de agência escolhem sites "bonitos". A Numiko desenhou alguns dos museus que lista, e a InsideOut é um portfólio próprio | os exemplos mostram boa prática curada, não o típico do mercado |

## Conclusão

A primeira decisão da skill não é escolher o estilo, e sim definir o **widget de transação** e onde ele fica: telefone, agendamento, busca por datas, cotação, doação ou carrinho. Em todas as sete famílias, a evidência mais dura (Baymard, NN/g, JMIR, M+R, Clio) é sobre esse widget e as provas ao lado dele, e quase nada é sobre estética. A unidade certa de recomendação também é mais fina do que "setor". É **setor × subnicho ou faixa de preço**, porque o protótipo muda mais entre emergência e paisagismo de design, ou entre fast fashion e luxo, do que entre setores vizinhos. Os construtores de mercado ainda não expõem esse terceiro eixo, e os cartões mostram que ele separa as recomendações.

A segunda implicação é que, nos nichos saturados, "segura" não pode significar "copiar o protótipo inteiro". Em SaaS e IA, o protótipo literal (fundo escuro, brilho roxo, bento de seis blocos, glass) é exatamente o clichê que as fontes de 2025–2026 criticam e que geradores baseados em shadcn reproduzem por padrão. Para esses nichos, a direção segura deve ser **estrutura prototípica com pele não clichê**: UI real, uma cor de marca e tile âncora. Fora dos nichos em que o site é amostra do trabalho, a ousadia deve vir da direção de arte, e não da arquitetura da informação. Como não existe dado de conversão para design distintivo, a skill deve justificar as direções expressiva e ousada pela adequação à marca e pela convenção do setor, nunca por promessa de desempenho. Essa lacuna é também a melhor oportunidade de medição que este trabalho deixa em aberto.
