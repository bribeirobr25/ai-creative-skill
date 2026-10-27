# Separe estilo, layout, superfície e movimento no catálogo

Um catálogo de estilos para uma skill de geração de sites não deve tratar os 18 nomes da lista como itens do mesmo nível. Doze são estéticas propriamente ditas: Minimalist, Swiss/International, Editorial, Brutalist, Neo-brutalist, Retro, Y2K, Maximalist, Organic, Luxury, Dark/tech e Collage. Três são tratamentos de superfície aplicados sobre uma estética (Glassmorphism, Neumorphism e Claymorphism). Bento grid é um padrão de layout. Kinetic typography e Immersive/3D scroll são padrões de movimento. Dark/tech mistura um modo de cor com uma estética. As galerias de referência já trabalham assim: a Awwwards separa categoria, tag, tecnologia, fonte e cor em facetas independentes ([Awwwards](https://www.awwwards.com/websites/)). Por isso o catálogo deve ter um cartão por estética, com o mesmo conjunto de campos, e trazer layout, superfície, movimento e modo de cor como modificadores que se combinam. As fontes oferecem números concretos para só parte dos estilos (neo-brutalismo, glass, neumorfismo, clay, bento e animações por rolagem). O restante dos valores de CSS foi sintetizado e aparece marcado assim neste relatório. As pesquisas de percepção pesam na decisão: julgamentos estéticos acontecem em 17–50 ms, e combinar baixa complexidade com alta prototipicidade vence a primeira impressão ([Google Research](https://research.google/blog/users-love-simple-and-familiar-designs-why-websites-need-to-make-a-great-first-impression/)). Estilos expressivos, portanto, exigem uma categoria de negócio que os aceite. Entre os construtores de sites com IA analisados, nenhum infere o estilo a partir de uma foto de produto, nem apresenta um catálogo de estilos com nome e justificativa. A prática mais bem documentada é apresentar três direções (segura, expressiva e ousada) e permitir misturar no nível dos tokens. Faltam na lista ao menos dez estéticas com sinal de uso em 2024–2026, com Flat/Material, o "padrão seguro", em primeiro lugar. Muitos sites de exemplo, licenças de fontes e afirmações sobre suporte de navegador ainda precisam de verificação, e o registro de incertezas no fim do relatório reúne esses pontos.

## Convenções de leitura e o contrato base que vale para todos os estilos

### Marcadores usados em todo o catálogo

Cada valor concreto deste relatório traz uma marca de procedência. **[F]** indica um fato ou valor com fonte, citada na mesma linha. **[S]** indica um valor sintetizado pelos pesquisadores: serve como padrão de partida, mas não vem de uma autoridade única. **[C]** indica um contraste calculado nesta pesquisa com a fórmula de luminância relativa da WCAG 2.x. **[NV]** indica um exemplo ou fato não verificado ao vivo; os sites de exemplo vieram de roundups e nenhum foi aberto, então podem ter sido redesenhados. **[LIC?]** indica uma licença de fonte que precisa ser confirmada no arquivo LICENSE/OFL.txt antes de empacotar. **[SUP?]** indica uma afirmação de suporte de navegador que deve ser rechecada no MDN ou no caniuse no momento do build.

Sobre fontes: todas as famílias sugeridas estão no Google Fonts, que distribui sob OFL ou Apache 2.0. As licenças não foram conferidas uma a uma, então toda a lista carrega **[LIC?]** implícito. Há quatro exceções já identificadas. **Ubuntu usa a Ubuntu Font Licence, não a OFL**. **Satoshi e General Sans** usam a Fontshare ITF FFL. **SF Pro** tem licença da Apple restrita às plataformas Apple. Os faces comerciais "icônicos" de alguns estilos, como Dinamo, Pangram Pangram e as display setentistas de marketplace, não são OFL. A licença OFL de **Geist e Geist Mono** não foi verificada.

### Contrato base de acessibilidade e performance (herdado por todos os cartões)

As regras abaixo valem para todos os estilos. Por isso os cartões tratam apenas dos riscos específicos de cada um.

**Contraste.** WCAG 2.2 AA exige 4.5:1 para texto normal e 3:1 para texto grande (≥24px regular ou ≥18.66px bold) **[F]** ([W3C 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)). Bordas de componentes, estados e gráficos com significado precisam de 3:1 **[F]** ([W3C 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)).

**Espaçamento de texto.** O conteúdo precisa resistir a line-height de 1.5×, espaçamento de parágrafo de 2×, letter-spacing de 0.12em e word-spacing de 0.16em **[F]** ([W3C 1.4.12](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html)). Na prática, cards e caixas de texto não podem ter altura fixa.

**Movimento.** Todo conteúdo que começa sozinho, dura mais de 5 s e aparece junto com outro conteúdo precisa de um controle de pausar, parar ou ocultar. Isso vale para marquees, vídeo em loop e carrosséis, e a regra é Nível A **[F]** ([W3C 2.2.2](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)). Nada pode piscar mais de três vezes por segundo **[F]** ([W3C 2.3.1](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html)). A SC 2.3.3 é AAA, mas honrar `prefers-reduced-motion` (técnicas C39/SCR40) é a linha de base esperada **[F]** ([W3C 2.3.3](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html)). Usuários com distúrbios vestibulares podem ter tontura, náusea e enxaqueca **[F]** ([web.dev](https://web.dev/articles/prefers-reduced-motion)).

**Foco e alvos de toque.** Novidades da WCAG 2.2: o foco não pode ficar totalmente escondido por um header sticky (2.4.11), e os alvos de toque precisam ter no mínimo 24×24 CSS px (2.5.8) **[F]** ([W3C 2.4.11](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html); [W3C 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)).

**Reflow.** Não pode haver rolagem bidimensional a 320 CSS px de largura **[F]** ([W3C 1.4.10](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)).

**Ordem de leitura.** A ordem programática tem de ser correta mesmo quando o CSS Grid posiciona os itens fora da ordem do DOM **[F]** ([W3C 1.3.2](https://www.w3.org/WAI/WCAG22/Understanding/meaningful-sequence.html)).

O contrato sintetizado para todo site gerado **[S]** é este:

- O movimento é escrito dentro de `@media (prefers-reduced-motion: no-preference)`, e o estado final visível é o padrão.
- No JS, `matchMedia('(prefers-reduced-motion: reduce)')` fica escutando `change`.
- Há um botão "Pausar animações" no site inteiro que grava `data-motion="off"` no `<html>` e persiste em localStorage. Ele cobre a 2.2.2 com um único controle.
- O foco usa `:focus-visible { outline: 3px solid; outline-offset: 3px }`.
- `scroll-padding-top` é igual à altura do header sticky.
- Os alvos de toque têm 44px recomendados.
- As imagens usam AVIF/WebP com `srcset`. A imagem de LCP leva `fetchpriority="high"`, as demais levam `loading="lazy"`, e toda mídia tem `width`/`height` ou `aspect-ratio`.
- As fontes são WOFF2 em subset, com `font-display: swap`, uma ou duas pré-carregadas e de preferência variáveis.
- Só `transform` e `opacity` são animados.

Os limiares de Core Web Vitals (LCP < 2.5 s, CLS < 0.1, INP < 200 ms) vêm de conhecimento geral e não foram conferidos nesta pesquisa **[NV]**.

```css
/* [S] gate padrão de movimento, reaproveitado por todos os estilos */
@media (prefers-reduced-motion: reduce){
  *,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;
    transition-duration:.01ms!important;scroll-behavior:auto!important}
}
```

```js
// [S] reveal com IntersectionObserver, desligado sob reduced motion; conteúdo visível sem JS (escopo .js .reveal)
const rm = matchMedia('(prefers-reduced-motion: reduce)');
if (!rm.matches) {
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
  }), { rootMargin: '0px 0px -10% 0px', threshold: 0.1 });
  document.querySelectorAll('.reveal').forEach(el => io.observe(el));
} else document.querySelectorAll('.reveal').forEach(el => el.classList.add('is-in'));
```

## Quatro eixos independentes substituem a lista plana de 18

### Galerias e pesquisa já separam as facetas

A Awwwards organiza a navegação em **Category** (setor ou tipo de site, como Fashion, Luxury, Startups ou Experimental), **Tag**, **Technology**, **Font** e **Color**. A faceta Tag mistura, num mesmo nível, estilo visual (Minimal, Flat Design, Retro, Illustration, Typography), layout (Horizontal Layout, Single page, Fullscreen) e interação (Parallax, Microinteractions, Transitions, Storytelling, 3D) **[F]** ([Awwwards](https://www.awwwards.com/websites/)). A Siteinspire usa quatro facetas: **Styles, Types, Subjects, Platforms**. Na data da pesquisa, a página inicial mostrava Typographic com **2.105** sites, Minimal com **847**, Grid Layout com **672** e Unusual Layout com **671** **[F]** ([Siteinspire](https://www.siteinspire.com/)). Esses números sugerem que tipografia e minimalismo dominam o design de "qualidade curada". Os relatórios de tendência também misturam os eixos. A lista de 2026 da Figma coloca no mesmo nível estilos (Neumorphism, Retrofuturism, Maximalism, Collage, Neo-brutalism), escolhas de cor e tipo (Vibrant palettes, Bold typography, Dark mode) e interação (Motion design, 3D/immersive) **[F]** ([Figma](https://www.figma.com/resource-library/web-design-trends/)).

A pesquisa acadêmica oferece eixos contínuos que ficam acima dos estilos. Lavie & Tractinsky separam a **estética clássica** (limpa, clara, organizada, simétrica) da **estética expressiva** (criativa, original, fascinante, com efeitos especiais) **[F]** ([Hobday, resumo de Lavie & Tractinsky](https://anthonyhobday.com/blog/20221005.html); artigo original de 2004). Tuch et al. (Google/Basel, 2012) apontam a **complexidade visual** e a **prototipicidade** (o quanto o site parece típico da sua categoria) como os dois fatores por trás dos julgamentos rápidos **[F]** ([Google Research](https://research.google/blog/users-love-simple-and-familiar-designs-why-websites-need-to-make-a-great-first-impression/)). Qualquer estilo do catálogo pode ser posicionado nesses dois eixos.

### Reclassificação dos 18 e esquema proposto

A tabela abaixo reclassifica os 18 nomes **[S]**. É a decisão estrutural mais importante do catálogo.

| Eixo | Itens da lista atual | Observação |
|---|---|---|
| `aesthetic` (escolha primária) | Minimalist, Swiss/International, Editorial, Brutalist, Neo-brutalist, Retro/vintage, Y2K, Maximalist, Organic/natural, Luxury/elegant, Collage/scrapbook, Dark/tech (parcial) | Editorial também implica um layout de revista; Retro e Organic são "estilos-mãe" com presets |
| `surface` (aplicada sobre a estética) | Glassmorphism, Neumorphism, Claymorphism | Também entram aqui: grain/noise, paper/texture, aurora/gradient mesh, duotone, Liquid Glass |
| `layout` | Bento grid | Também entram aqui: editorial grid, coluna narrativa única, split-screen, full-bleed hero, broken grid, index/table list, sidebar/docs |
| `motion` | Kinetic typography, Immersive/3D scroll | Também entram aqui: none, micro-interactions, scroll-reveal, parallax, page transitions |
| `color_mode` | Dark/tech (parcial) | Dark deve virar um toggle disponível em qualquer estética, mais uma estética "Tech/futurist" |

O esquema proposto para cada cartão tem oito facetas **[S]**:

1. `aesthetic`: uma estética primária e, opcionalmente, uma secundária.
2. `layout`.
3. `surface`.
4. `motion`.
5. `type_system`: grotesk, serif editorial, display/expressive, mono ou handwritten.
6. `color_mode` e caráter da paleta: muted, vivid, monochrome, pastel ou neon.
7. Dials mensuráveis: `complexity`, `prototypicality` e o eixo `classical↔expressive`.
8. Metadados de encaixe: setores, posicionamento de preço, tipo de conteúdo (photo-led, text-led ou app/SaaS), personalidade de marca, nível de risco de acessibilidade e custo de performance.

Esse desenho repete a lógica da Awwwards, que mantém Category, Tag e Technology separados. Ele também permite combinações como "Luxury + editorial grid + flat + reveal lento" sem multiplicar estilos quase duplicados.

### Regras de combinação entre eixos

As fontes justificam algumas restrições cruzadas que o catálogo deve codificar. A Apple recomenda glass apenas na camada de navegação, nunca na área de conteúdo e nunca glass sobre glass **[F]** ([Apple WWDC25](https://developer.apple.com/fr/videos/play/wwdc2025/219/)). Neumorphism deve ser usado "com parcimônia, principalmente como acento ao lado de outro sistema" **[F]** ([CSS-Tricks](https://css-tricks.com/?p=304931)). Bento é layout e se combina com qualquer estética, e "glass bento" e "soft bento" são combinações válidas **[S]**. Collage é muitas vezes uma *técnica* dentro do maximalismo, e Editorial absorve as duas como acento, por exemplo um "shell editorial + hero em collage" **[S]**.

Alguns estilos se sobrepõem, e o catálogo deve tratá-los como vizinhos com ponte explícita, não como duplicatas:

- O byooooob.com aparece como neo-brutalista na NN/g e como Y2K candy na Webflow, então N1 Candy e Y2 Candy são vizinhos **[F]** ([NN/g](https://www.nngroup.com/articles/neobrutalism/); [Webflow](https://webflow.com/blog/y2k-aesthetic)).
- O Frutiger Aero aparece tanto em Y2K quanto na categoria "Organic & atmospheric" do daisyUI **[F]** ([daisyUI](https://trends.daisyui.com/organic-atmospheric-ui/)).
- Luxury "dark opulent" e Dark/tech "luxury dark" descrevem a mesma direção.
- O minimalismo quente (Japandi) se sobrepõe ao Organic "earthy craft".

## Dezoito cartões com os mesmos onze campos

Todos os cartões seguem a mesma ordem de campos: (1) definição e traços-assinatura, (2) variantes, (3) layouts e padrões de página, (4) tipografia OFL, (5) cor, (6) componentes, (7) efeitos, movimento e configurações, (8) riscos de acessibilidade e performance, (9) encaixe de marca, (10) antipadrões e (11) exemplos e referências. A linha "Eixo" no topo de cada cartão situa o item na taxonomia acima.

---

### 1. Minimalist

**Eixo:** estética primária. Baixa complexidade, alta prototipicidade e risco baixo.

#### 1.1 Definição e traços-assinatura
Segundo a NN/g, o minimalismo existe para apresentar conteúdo e funções "de modo simples e direto", tirando o que não serve aos objetivos do usuário. Suas raízes estão na arte minimalista dos anos 1960, no "Less is more" de Mies van der Rohe, na razão dado-tinta de Tufte, no minimalismo de Carroll (1990) e na heurística de Nielsen de 1995. O Google foi pioneiro da abordagem na web nos anos 2000 **[F]** ([NN/g](https://www.nngroup.com/articles/roots-minimalism-web-design/)). A NN/g lista estes traços: texturas planas, paleta limitada (geralmente escala de cinza mais um acento), muito espaço negativo, pouco conteúdo e alta proporção de elementos significativos **[F]** (mesma fonte).

Para o gerador, os traços-assinatura **[S]** são cinco:

1. Um elemento dominante por viewport.
2. Pelo menos 40–50% do viewport vazio.
3. No máximo um neutro e um acento.
4. Uma família tipográfica em 2–3 pesos.
5. Nenhuma textura, gradiente ou sombra, ou no máximo uma elevação muito sutil.

O que separa os três estilos vizinhos: o minimalismo é *redução*, o Swiss é *sistema* e o Luxury é *contenção somada a artesania* **[S]**.

#### 1.2 Variantes
A NN/g alerta que o minimalismo extremo "nunca deve ser um produto final" e que a adesão rígida produz uma "densidade de informação desperdiçadoramente baixa" **[F]** ([NN/g](https://www.nngroup.com/articles/roots-minimalism-web-design/)). Isso justifica separar variantes por densidade. Os nomes da tabela são rótulos de catálogo **[S]**.

| Variante | Assinatura e valores-chave | Usar para |
|---|---|---|
| Stark / Mono | `#FFFFFF` ou off-black, tipo preto, zero ou um acento saturado, um sans | arquitetos, portfólios, estúdios, manifestos de tecnologia |
| Warm (Japandi/soft) | fundo `#F5F1EA`–`#EFE9DF`, cinzas quentes, acento terroso (clay, sage), humanist sans ou serif leve no título, radius 4–8px | wellness, cerâmica, interiores, skincare, padarias, hotéis boutique |
| Functional / product | cinzas neutros, um acento, componentes densos mas calmos, hairlines de 1px, sombras sutis | software, fintech, B2B |
| Typographic / text-only | sem imagens, o texto é o layout (nome grande, lista de projetos) | sites pessoais, escritores, consultores |

#### 1.3 Layouts e padrões de página
A NN/g mostra que o design flat/minimal funciona melhor com baixa densidade de informação, layout tradicional e elementos interativos que se destacam **[F]** ([NN/g](https://www.nngroup.com/articles/flat-ui-less-attention-cause-uncertainty/)). Também registra a navegação global escondida como tendência influenciada pelo minimalismo **[F]** ([NN/g](https://www.nngroup.com/articles/roots-minimalism-web-design/)). O estudo quantitativo da NN/g sobre menus hambúrguer não foi buscado e deve ser verificado antes de citar números **[NV]**.

Valores padrão **[S]**:

- **Gutter lateral:** `clamp(16px, 4vw, 48px)`.
- **Grid:** `repeat(12, minmax(0,1fr))` com gap de 24–32px no desktop e 16px no mobile.
- **Largura de texto:** medida de 60–68ch.
- **Container:** 1200–1280px (functional) ou 1040px (stark/typographic).
- **Hero:** (a) H1 de uma frase alinhado à esquerda no terço superior com um CTA, (b) produto centralizado em campo liso, ou (c) split 50/50.
- **Nav:** logo à esquerda e 3–5 links visíveis à direita. No mobile, um botão de texto "Menu" abre um overlay de tela cheia.
- **Grade de coleção:** 3, 2 e 1–2 colunas, imagens 4:5 ou 1:1, nome e preço pequenos abaixo, sem moldura de card.
- **Ritmo:** padding vertical `clamp(64px, 10vw, 160px)`, uma ideia por seção.

#### 1.4 Tipografia (OFL)
**[S]**:

- **Escala:** razão modular de 1.2 ou 1.25.
- **Corpo:** 16–18px, line-height 1.5–1.65.
- **Display:** line-height 1.05–1.15, tracking −0.01 a −0.02em.
- **Labels:** 12–14px, +0.02em.
- **Pesos e famílias:** 400/500 (+600), uma família.
- **Pares stark:** Inter sozinha (Inter Tight no display), Geist + Geist Mono **[LIC?]** ou Manrope.
- **Pares warm:** Instrument Serif + Instrument Sans, Fraunces + DM Sans ou Newsreader + Public Sans.

#### 1.5 Cor
A fonte define a paleta como escala de cinza mais um acento **[F]** ([NN/g](https://www.nngroup.com/articles/roots-minimalism-web-design/)). Os tokens **[S]** abaixo têm contrastes estimados que devem ser conferidos num checker:

| Variante | Tokens | Contraste estimado |
|---|---|---|
| Stark | `--bg:#FFFFFF; --fg:#111111; --muted:#6B6B6B`, acento opcional `#0047FF` | muted ≈5.3:1 |
| Warm | `--bg:#F5F1EA; --surface:#ECE6DC; --fg:#2B2622; --muted:#6E655C`, acento `#A0522D` ou `#6F7D5C` | muted ≈5:1 (verificar); sage como texto exige conferir 4.5:1 |

Texto cinza sobre branco precisa ser no mínimo `#767676` para chegar a 4.5:1. Os neutros fazem 90% do trabalho.

#### 1.6 Componentes
O dado mais forte aqui é empírico. Num estudo de eyetracking com 71 participantes, links e botões com sinalizadores fracos custaram **22% mais tempo de tarefa e 25% mais fixações**. No caso Brilliant Earth, 86% dos participantes da versão forte foram do título ao link-alvo, contra 50% da versão fraca **[F]** ([NN/g](https://www.nngroup.com/articles/flat-ui-less-attention-cause-uncertainty/)).

Componentes **[S]**:

- **Botão primário:** fundo `--fg` sólido, 44–48px de altura, padding `0 24px`, radius 0–6px (8px ou pill na variante warm).
- **Links:** sublinhados, com `text-underline-offset:.2em; text-decoration-thickness:1px`.
- **Cards:** sem borda nem sombra, ou com 1px `#E5E5E5` na variante functional.
- **Divisores:** raros, 1px `rgba(0,0,0,.08)`.
- **Ícones:** outline de 1.5px (Lucide ou Phosphor Light), 20–24px, sempre com rótulo.

#### 1.7 Efeitos, movimento e configurações
**[S]**: hover de 150–250ms só em cor e opacidade, com `--ease-std: cubic-bezier(.2,0,0,1)`. O reveal é opcional e usa o padrão do contrato base. Sticky header que muda no scroll deve usar IntersectionObserver sobre um sentinela, e não scroll listeners.

#### 1.8 Riscos de acessibilidade e performance
A NN/g mostra que o minimalismo só visual, que esconde elementos importantes, pode "aumentar a complexidade em vez de reduzi-la", e cita o Windows 8 como exemplo de alerta **[F]** ([NN/g](https://www.nngroup.com/articles/roots-minimalism-web-design/)). As correções **[S]** são manter a nav primária visível no desktop, sublinhar links e dar forma ou preenchimento aos botões. Performance é o ponto forte do estilo, que bate com folga os limiares de CWV.

#### 1.9 Encaixe de marca
A NN/g recomenda decidir se o minimalismo serve ao site, à marca e ao conteúdo **[F]** ([NN/g](https://www.nngroup.com/articles/roots-minimalism-web-design/)). **Bom encaixe [S]:** arquitetura, interiores, cerâmica, skincare, wellness, SaaS, portfólios, lançamentos de produto único e serviços de PMEs. **Encaixe ruim [S]:** grandes catálogos e marketplaces, notícias, portais de governo, varejo de desconto e marcas infantis.

#### 1.10 Antipadrões
**[S]**:

- O visual de "template vazio": H1 centralizado, foto de banco e três cards com ícones.
- Nav escondida no desktop.
- Texto cinza sobre cinza.
- Ícones sem rótulo.
- Espaço em branco sem hierarquia.
- Tudo no mesmo tamanho e peso.

#### 1.11 Exemplos e referências
Feed da Minimal Gallery, setembro–outubro de 2026 **[F]** ([Minimal Gallery](https://minimal.gallery/)): Union Boulangerie (candidata a warm), Odyssee Clinic, Flowlife, Spek, Unify (functional), How&How, GRNDWRK STUDIO e Grafik. A galeria não marca subvariantes, então o encaixe por variante foi palpite **[NV]**. linear.app e vercel.com são candidatos a functional minimal **[NV]**.

---

### 2. Swiss / International Typographic Style

**Eixo:** estética primária. Baixa complexidade, prototípico em setores culturais e técnicos, risco baixo.

#### 2.1 Definição e traços-assinatura
O estilo surgiu entre os anos 1930 e 1950 e se apoia na tipografia modernista dos anos 1920 (Construtivismo, De Stijl, Bauhaus) **[F]** ([Wikipedia](https://en.wikipedia.org/wiki/International_Typographic_Style)). Marcos históricos da mesma fonte:

- 1908: a Escola de Design de Basileia reformula o curso básico com técnicas de grid.
- 1918: Ernst Keller passa a lecionar em Zurique.
- Pioneiros: Max Bill e Théo Ballmer.
- Josef Müller-Brockmann buscava uma expressão objetiva e usava fotografias grandes.
- Rudolph de Harak levou o estilo aos EUA.
- 1959: a revista *Neue Grafik* espalha o estilo internacionalmente.

Características definidoras **[F]** (mesma fonte): estrutura em grid, layouts assimétricos, tipos sans-serif, texto alinhado à esquerda com margem direita irregular (flush-left/ragged-right), preferência por fotografia em vez de ilustração, e clareza e objetividade. As fontes de referência são Akzidenz-Grotesk, Univers e Helvetica.

Na tradução para a web, a Justinmind (2018) fala em grids matemáticos e cita Müller-Brockmann: "The grid system is an aid, not a guarantee". Menciona também leitura em F e em Z e o princípio "form follows function" **[F]** ([UX Planet](https://uxplanet.org/swiss-style-web-design-everything-you-need-to-know-2b128fd327b9)). A Tilda (2022) descreve o estilo como "quickly perceived, universal, efficient" e sugere grid modular de 3 ou 4 colunas **[F]** ([Tilda](https://blog-en.tilda.cc/tpost/zsxaujziu1-swiss-style-in-web-design)).

Seis traços-assinatura **[S]**:

1. Grid modular perceptível (12 colunas, com spans de 2/3/4/6).
2. Neo-grotesk sans, e só ele.
3. Flush-left em tudo.
4. Assimetria com o tipo grande funcionando como imagem.
5. Forte contraste de escala.
6. Campos chapados em branco, preto e vermelho, com fotografia objetiva.

#### 2.2 Variantes
Nenhuma fonte codifica variantes. Os rótulos da tabela são do catálogo **[S]**.

| Variante | Assinatura e valores-chave | Usar para |
|---|---|---|
| Classic Swiss (Zürich) | grid estrito de 12 colunas, neo-grotesk, branco/preto/vermelho, fotografia grande, seções como pôsteres | instituições culturais, exposições, arquitetura, eventos |
| Neo-Swiss / New Grotesk | Inter, Instrument Sans ou Geist; headlines enormes com tracking negativo; monocromático com um acento neon; metadados pequenos em mono | agências, estúdios, tech, conferências (a variante mais comum hoje) |
| Swiss-Brutalist / Visible-grid | linhas do grid expostas, rules de 1px, labels em mono, layouts de índice/tabela, pouca imagem | foundries, arquivos, ferramentas dev, publicações de arte |
| Editorial Swiss (Basel) | mais fotografia, texto em múltiplas colunas, legendas e índices, paleta um pouco mais quente | revistas, museus, marcas editoriais |

#### 2.3 Layouts e padrões de página
**[S]**:

- **Grid:** 12 colunas (ou modular de 6/4), gap 16–24px, todo texto começando numa linha de coluna.
- **Container:** 1440–1600px ou fluido em largura total.
- **Hero:** (a) headline enorme ocupando 8–12 colunas, com metadados nas colunas 1–3; (b) pôster com foto em largura total sobrepondo as linhas do grid; ou (c) índice em tabela de projetos (ano, cliente, categoria).
- **Nav:** links alinhados às colunas, muitas vezes numerados (01, 02…).
- **Grades de projeto:** spans assimétricos (7+5, 4+4+4, 8 com offset 4) e toggle entre lista e tabela.
- **Ritmo:** unidade de 8px, seções separadas por rules de 1px em vez de muito padding, padding de 48–96px.
- **Mobile:** grid de 4 colunas com gap 12–16px, mantendo flush-left e a numeração.

#### 2.4 Tipografia (OFL)
**[F]** A Justinmind sugere Montserrat, Open Sans, Lato e Helvetica. O texto é de 2018, e a Montserrat é geométrica, não neo-grotesk, então encaixa mal ([UX Planet](https://uxplanet.org/swiss-style-web-design-everything-you-need-to-know-2b128fd327b9)). A Tilda sugere Helvetica, Futura e Tilda Sans, com hierarquia bold title → subtitle → body ([Tilda](https://blog-en.tilda.cc/tpost/zsxaujziu1-swiss-style-in-web-design)).

**[S]**:

- **Escala:** razão de 1.333–1.5, ou uma escala de "salto" com corpo de 16–18px e display de 96–200px.
- **Line-height:** 1.4–1.5 no corpo e 0.9–1.0 no display.
- **Tracking do display:** −0.02 a −0.04em.
- **Labels:** 11–13px, frequentemente mono em caixa alta com +0.04em.
- **Pesos:** 400/500/700.
- **Equivalentes livres de Helvetica/Akzidenz:** Inter, Archivo, Schibsted Grotesk ou Instrument Sans. Arimo é métrica-compatível com Arial/Helvetica e serve de fallback.
- **Pares neo e brutalistas:** Space Grotesk ou Hanken Grotesk com IBM Plex Mono, JetBrains Mono ou Space Mono.

#### 2.5 Cor
Um template de exemplo usa branco, azul e preto **[F]** ([UX Planet](https://uxplanet.org/swiss-style-web-design-everything-you-need-to-know-2b128fd327b9)). Tokens **[S]**:

| Variante | Tokens | Observações |
|---|---|---|
| Classic | `--bg:#FFFFFF; --fg:#000000; --accent:#E30613` | contraste ≈4.9:1, a verificar; o hex do vermelho suíço vem de conhecimento geral; para texto vermelho pequeno, use `#C8000F` |
| Neo-Swiss | `--bg:#F2F2F0; --fg:#0A0A0A; --accent:#FF4F00` ou `#2B50FF` | neons como `#D4FF3F` só como preenchimento atrás de texto preto |

#### 2.6 Componentes
**[S]**:

- **Botão:** retângulo preto ou vermelho, radius 0, muitas vezes na largura da coluna.
- **Link:** texto com "→" e sublinhado no hover.
- **Sem cards:** o conteúdo fica em células do grid separadas por rules.
- **Rules:** 1px (denso) ou 2–4px (pôster), em preto.
- **Imagens:** full-bleed em 3:2 ou 4:3, alto contraste, P&B ou duotone. A fonte prefere fotografia por ser "mais objetiva" **[F]** ([UX Planet](https://uxplanet.org/swiss-style-web-design-everything-you-need-to-know-2b128fd327b9)).
- **Ícones:** quase nenhum, só setas, sinais de mais e números.

#### 2.7 Efeitos, movimento e configurações
**[S]**:

- Mudanças de estado instantâneas ou de 120–200ms.
- Inversão de linha no hover em listas de índice: `.row:hover{background:#000;color:#fff}`.
- Wipes com `clip-path` de 400–600ms usando `cubic-bezier(.65,0,.35,1)`.
- Marquee de texto (com gate e pausa).
- Labels com `mix-blend-mode: difference`.

#### 2.8 Riscos de acessibilidade e performance
**[S]**:

- Headlines gigantes estouram a 320px. A correção é `clamp()` com `overflow-wrap:anywhere` ou `hyphens:auto` (este exige `lang`).
- Não codificar significado só no vermelho.
- Mono com no mínimo 12px.
- Índices montados como `<table>` real.
- Scrim em texto sobre foto.

A performance é excelente.

#### 2.9 Encaixe de marca
**Bom [S]:** museus, galerias, festivais, arquitetura, estúdios, foundries, editoras, conferências, pesquisa, engenharia/tech e B2B suíço ou alemão. **Ruim [S]:** marcas de consumo românticas ou emocionais (casamentos, infantil), luxo heritage (exceto no modo editorial) e comida de conforto.

#### 2.10 Antipadrões
**[S]**:

- Fonte "tipo Helvetica" com 12 colunas e sem contraste de escala, que fica com cara de template Bootstrap.
- Texto centralizado.
- Gradientes, sombras ou cards arredondados.
- Assimetria aleatória, desligada das colunas.
- Vermelho em toda parte.

#### 2.11 Exemplos e referências
Siteinspire e Awwwards não retornaram listagens legíveis, então nenhum exemplo suíço de 2023–2026 foi verificado em galeria. Candidatos **[NV]**: Grilli Type (grillitype.com), Dinamo (abcdinamo.com), Museum für Gestaltung Zürich (museum-gestaltung.ch), Swiss Design Awards (swissdesignawards.ch) e Experimental Jetset (experimentaljetset.nl). Referências: [Wikipedia](https://en.wikipedia.org/wiki/International_Typographic_Style), [UX Planet (2018)](https://uxplanet.org/swiss-style-web-design-everything-you-need-to-know-2b128fd327b9) e [Tilda (2022)](https://blog-en.tilda.cc/tpost/zsxaujziu1-swiss-style-in-web-design).

---

### 3. Editorial / magazine

**Eixo:** estética primária que também implica um layout (editorial grid). Complexidade média e risco baixo.

#### 3.1 Definição e traços-assinatura
Não existe definição formal. A Subframe descreve o estilo como equilíbrio entre forma e função, com imagem e tipo liderando, tipografia forte ou elegante, fotografia marcante e paleta contida ou monocromática, às vezes com um acento ousado **[F]** ([Subframe](https://www.subframe.com/tips/editorial-website-design-examples)). Um texto de praticante de 2026 afirma que layouts editoriais estão substituindo o hero único. O padrão descrito é uma matéria principal, duas secundárias e 2–4 blocos menores acima da dobra, com a célula maior pelo menos **1.6×** a vizinha, porque "balanced grids read as feature tables" **[F]** ([Pravin Kumar](https://www.pravinkumar.co/blog/editorial-layouts-replace-hero-sections-webflow-2026)). As estatísticas de desempenho do mesmo artigo (NN/g 2026, Baymard 2025) não têm link e não puderam ser verificadas, então não entram aqui como evidência. A KOTA descreve neutros "warm, tactile" (tons de cogumelo, off-whites calcários) com grain e fotografia "candid camera roll" **[F]** ([KOTA](https://kota.co.uk/blog/branding-inspiration-brand-design-trends-for-2026)). A Figma afirma que "Typography is taking center stage in 2026" **[F]** ([Figma](https://www.figma.com/resource-library/web-design-trends/)).

Teste de reconhecimento **[S]**: headline grande em serif ou condensada, grid assimétrico de várias colunas, legendas e bylines em small caps ou mono, espaço em branco generoso, um acento e foto full-bleed. A linhagem Brody/Carson/Emigre, citada às vezes, está sem fonte aqui.

#### 3.2 Variantes
Rótulos de catálogo **[S]**:

| Variante | Assinatura e valores-chave | Usar para |
|---|---|---|
| Fashion/luxury magazine | Didone fina ou de alto contraste, fotografia grande, quase monocromático, fades lentos | moda, beleza, hospitalidade, galerias, DTC premium |
| Newspaper/broadsheet | grid denso de colunas com rules, masthead, datelines, serif no corpo, muitas manchetes por tela | mídia, newsletters, think tanks, hubs de conteúdo B2B |
| Indie/slow (tipo Kinfolk) | neutros quentes e grain, foto candid, serif humanista com small caps, leitura longa (coincide com os neutros da KOTA **[F]**) | lifestyle, comida, artesanato, wellness |
| Experimental / Swiss-editorial | headline grotesk, numerais enormes, labels rotacionadas, texto dentro da imagem | agências, arquitetura, estúdios, música |

#### 3.3 Layouts e padrões de página
Este é o estilo com mecânica de grid mais bem documentada. Rachel Andrew usa linhas nomeadas com sufixos `-start`/`-end`, que criam áreas implícitas (`content`, `full`, `start-half`…): os itens de breakout ocupam `full` e o texto fica em `content` **[F]** ([Smashing](https://www.smashingmagazine.com/2019/10/editorial-design-patterns-css-grid-subgrid-naming/)). O artigo é de 2019 e diz que subgrid só existia no Firefox Nightly. Essa informação está desatualizada: subgrid hoje está em todos os motores, segundo o MDN, que não foi relido nesta pesquisa **[SUP?]**.

Uma demo de 2026 usa grid estrito de 8 colunas e faz sobreposição por coordenadas de linha, sem `position:absolute`: `.page-one__photo{grid-column:1/8;grid-row:1/4;z-index:-1}`. A demo usa `columns` para texto denso, pesa menos de 5 KB e não tem JS **[F]** ([FreeFrontend](https://freefrontend.com/code/editorial-css-grid-magazine-layout-2026-03-31/)). O padrão de "front page" do texto de Pravin Kumar tem quatro colunas com áreas nomeadas a 1440px, duas no tablet (com a matéria principal ocupando as duas) e uma no mobile, ordenada por prioridade. Os cards terciários têm quatro campos (imagem, eyebrow, headline, link) e a página usa dois pesos, um acento e uma única proporção de recorte **[F]** ([Pravin Kumar](https://www.pravinkumar.co/blog/editorial-layouts-replace-hero-sections-webflow-2026)).

Valores **[S]**:

```css
/* [S] grid editorial de breakout (versão moderna do padrão Smashing) */
.page{--gutter:clamp(1rem,2.5vw,2rem);--measure:68ch;display:grid;column-gap:var(--gutter);
  grid-template-columns:[full-start] minmax(var(--gutter),1fr) [wide-start] minmax(0,12rem)
    [content-start] min(var(--measure),100% - 2*var(--gutter)) [content-end]
    minmax(0,12rem) [wide-end] minmax(var(--gutter),1fr) [full-end];}
.page>*{grid-column:content}.page>.wide{grid-column:wide}.page>.bleed{grid-column:full}
```

- **Front page:** 12 colunas, gutter de 24px, máximo de 1280–1440px, matéria principal em 7–8 colunas e coluna lateral em 4–5.
- **Artigo:** medida de 680–720px, imagens largas de 960–1100px e full-bleed em 100vw.
- **Commerce editorial:** fileiras 2-up alternando com 3- ou 4-up, e um tile de "story" a cada 6–8 produtos.
- **Nav:** masthead centralizado com barra de seções em caixa alta a 0.08em. O hambúrguer só aparece abaixo de 768px.
- **Ritmo:** feature, 3-up denso, imagem full-bleed com legenda, faixa de citação e linha de 2 colunas, separados por hairlines de 1px `currentColor` a 20–30%.

#### 3.4 Tipografia (OFL)
**[F]** Dois pesos no total ([Pravin Kumar](https://www.pravinkumar.co/blog/editorial-layouts-replace-hero-sections-webflow-2026)). Um diretório de pares lista Newsreader + Instrument Serif e Fraunces + Instrument Sans ([maxibestof](https://maxibestof.one/typefaces/newsreader/pairing/instrument-serif)).

Pares por variante **[S]**:

| Variante | Display | Texto | Meta |
|---|---|---|---|
| Fashion | Bodoni Moda ou Playfair Display (opsz) | Inter ou Instrument Sans | IBM Plex Mono |
| Newspaper | Libre Caslon Display/Text ou Newsreader | Source Serif 4 | Inter em small caps |
| Indie/slow | Fraunces (soft, opsz), Instrument Serif ou Gloock | Newsreader ou EB Garamond | DM Mono |
| Swiss-experimental | Inter Tight, Archivo (wide) ou Space Grotesk | Inter | JetBrains Mono |

Configuração **[S]**:

- **Escala:** razão de 1.333–1.5.
- **Corpo:** `clamp(1.0625rem, 0.95rem + 0.35vw, 1.25rem)`, line-height 1.5–1.65.
- **H1:** `clamp(2.75rem, 1rem + 6vw, 7.5rem)`, line-height 0.95–1.05, tracking −0.02 a −0.04em, peso 300–500 em Didones e 600–800 em grotesks.
- **Kicker:** 0.75–0.8125rem em caixa alta, com 0.08–0.14em.
- **Legendas:** 0.8125–0.875rem.
- **Recursos tipográficos:** `font-variant-numeric: oldstyle-nums`, e `text-wrap: balance` e `pretty` como progressive enhancement.

#### 3.5 Cor
**[F]** Paleta contida ou monocromática com um acento; a Cole Haan usa fundo amarelo ([Subframe](https://www.subframe.com/tips/editorial-website-design-examples)). Um acento em todo o layout ([Pravin Kumar](https://www.pravinkumar.co/blog/editorial-layouts-replace-hero-sections-webflow-2026)). Neutros de cogumelo, off-white calcário e neutros enferrujados ([KOTA](https://kota.co.uk/blog/branding-inspiration-brand-design-trends-for-2026)).

Tokens **[S]**:

| Variante | Tokens | Observações |
|---|---|---|
| Fashion | tinta `#111111`, papel `#FAFAF7`, legenda `#5C5C5C`, acento `#C8102E` | legenda ≈6.5:1 |
| Slow | papel `#F2EDE4`, tinta `#2B2622`, muted `#6B5F55`, ferrugem `#A4492B` | |
| Newspaper | jornal `#F4F1EA`, tinta `#1A1A1A`, rule a 25% | |

#### 3.6 Componentes
**[S]**:

- **Pull quote:** `<figure class="pullquote"><blockquote>…</blockquote><figcaption>`, na serif de display a 1.75–2.5rem e line-height 1.15, com rules de 2px acima e abaixo ou uma rule de 4px à esquerda. Não deve repetir o corpo; se repetir, a cópia leva `aria-hidden`.
- **Drop cap:** `initial-letter: 3 2`, com fallback `@supports not (initial-letter:1){float:left;font-size:4.2em;line-height:.8}` **[SUP?]**.
- **Figcaption:** 0.8125rem, com crédito em mono caixa alta.
- **Byline:** autor, `<time datetime>`, tempo de leitura e seção.
- **Kicker:** na cor de acento.
- **Hairline:** `border-block-start:1px solid color-mix(in srgb, currentColor 25%, transparent)`.
- **Sidenotes:** na margem direita no desktop, `<details>` no mobile.
- **Extras:** TOC e barra de progresso.

#### 3.7 Efeitos, movimento e configurações
**[S]**:

- Reveals de 12–24px em 500–700ms, com stagger de 60–80ms e `threshold:.15`.
- Imagens revelando de `clip-path: inset(0 0 100% 0)` para `inset(0)` em 800ms.
- Barra de progresso com `animation-timeline: scroll()` dentro de `@supports` **[SUP?]**.
- Grain como tile estático de 256×256 (10–20 KB) a 0.04–0.08 de opacidade, preferível a `feTurbulence` ao vivo em tela cheia.

#### 3.8 Riscos de acessibilidade e performance
O posicionamento por linhas do grid pode descolar a ordem visual da ordem do DOM (1.3.2), e caixas de altura fixa quebram sob a 1.4.12 **[F]** ([W3C 1.3.2](https://www.w3.org/WAI/WCAG22/Understanding/meaningful-sequence.html)). Correções **[S]**:

- Medida de no máximo 75ch e line-height ≥1.5.
- `<article>`, `<figure>` e `<time>` semânticos.
- Legenda não substitui alt.
- Legenda cinza com no mínimo 4.5:1.

#### 3.9 Encaixe de marca
**Bom [S]:** editoras, journals, moda e beleza, hospitalidade, arquitetura, galerias, DTC premium com histórias, consultorias com thought leadership e ONGs. **Com cuidado:** homepages de e-commerce, mantendo produtos acima da dobra ou um rail de produtos. A afirmação de "23% menos add-to-cart", atribuída à Baymard, não tem link e não está verificada **[NV]**. **Ruim [S]:** apps utilitários e varejo de desconto.

#### 3.10 Antipadrões
**[S]**:

- Layout de "revista" falsa preenchido com texto genérico.
- Pull quote repetindo o parágrafo anterior.
- Produtos escondidos abaixo de histórias longas.
- Legendas cinza-claro.

#### 3.11 Exemplos e referências
Da [Really Good Designs](https://reallygooddesigns.com/best-magazine-websites) **[F]** (sites não visitados **[NV]**): The New Yorker, WIRED, Exhibition Magazine, Assemble Papers, Hunger Magazine, Vessel Magazine, Scandinavian Mind e Rolling Stone. Para PMEs, as revistas independentes são análogos mais próximos. Outros candidatos **[NV]**: The Pudding, Kinfolk, Apartamento, It's Nice That e The Fabulist da Aesop.

---

### 4. Brutalist

**Eixo:** estética primária, com a variante "anti-design" na extremidade expressiva. Risco alto fora das categorias criativas, exceto a variante funcional.

#### 4.1 Definição e traços-assinatura
O termo ganhou força por volta de 2016 e é creditado a Pascal Deville, que criou o brutalistwebsites.com. Deville tomou o nome da arquitetura ("béton brut") e descreveu o estilo como "ruggedness and lack of concern to look comfortable or easy" **[F]** ([LogRocket](https://blog.logrocket.com/ux-design/web-brutalism/)). O daisyUI data o diretório de 2014 **[F]** ([daisyUI](https://trends.daisyui.com/trend/brutalism/)). A leitura proposta para o conflito é que o diretório nasceu em 2014 e a tendência virou mainstream por volta de 2016; o site primário não foi aberto. Alison Smithson usou "New Brutalism" em 1953, e na web o termo é "an analogy rather than a direct architectural method" **[F]** (daisyUI). Assinaturas: estrutura com cara de HTML cru, controles com aparência padrão, contraste duro, grid exposto, tipo enorme e pouco polimento **[F]** (daisyUI). Vitaly Friedman resume: "unconcerned aesthetics, not intentionally broken aesthetics" **[F]** ([Smashing](https://www.smashingmagazine.com/2020/01/split-personality-brutalist-web-development/)).

O manifesto de David Bryant Copeland traz sete regras **[F]** ([brutalist-web.design](https://brutalist-web.design/)):

1. O conteúdo é legível em todas as telas razoáveis.
2. Só links e botões respondem a cliques.
3. Links são sublinhados e botões parecem botões.
4. O botão voltar funciona.
5. O conteúdo é visto rolando a página.
6. Decoração só quando necessária.
7. "Performance is a feature."

#### 4.2 Variantes
O. O'Brien propõe dois tipos **[F]** ([Smashing](https://www.smashingmagazine.com/2020/01/split-personality-brutalist-web-development/)). O Tipo Um, "l'Internet Brut", usa HTML cru (Craigslist, Wikipedia, Old Reddit, Bloomberg). O Tipo Dois, "l'Internet Fou", é deliberadamente quebrado, com a usabilidade "an afterthought" ou "actively sabotaged" (Toiletpaper, jisooeom.com). Deville separa os praticantes em puristas, UX minimalists e anti-ists. A LogRocket fala em Functional, Jarring e Neu-brutalism **[F]** ([LogRocket](https://blog.logrocket.com/ux-design/web-brutalism/)).

| Variante **[S]** | Assinatura e valores-chave | Usar para |
|---|---|---|
| B1 Raw/HTML (functional) | fontes do sistema, links azuis sublinhados, uma coluna | manifestos, documentação, editoras indie, ferramentas dev |
| B2 Typographic/editorial | grotesk ou mono gigante, linhas do grid expostas, P&B com um acento | estúdios, instituições culturais, festivais, portfólios |
| B3 Anti-design/jarring | collage, sobreposições, faces em choque | arte, moda e música, quando conversão é secundária |

#### 4.3 Layouts e padrões de página
**[F]** O estilo expõe o fluxo do documento, o grid e a navegação. Usa blocos superdimensionados, saltos bruscos de escala e seções em largura total. As listas ficam "explicit rather than wrapped in cards", e as imagens mantêm proporções honestas e legendas visíveis ([daisyUI](https://trends.daisyui.com/trend/brutalism/)). Não há drop-downs ([LogRocket](https://blog.logrocket.com/ux-design/web-brutalism/)).

**[S]**:

- **Hero:** (a) wordmark de 12–20vw sangrando a borda, (b) `<h1>` simples com lista de links, ou (c) imagem full-bleed com bloco de legenda.
- **Grid:** 12 colunas desenhadas com rules de 1–2px, ou coluna única de 60–75ch.
- **Nav:** linha de links inline.
- **Coleções:** índice em tabela (nome | ano | categoria), ou grid com gap de 1px sobre fundo preto, em que o gap vira rule.
- **Mobile:** coluna única, links sempre visíveis e `clamp()` mais `overflow-wrap:anywhere` no display.

#### 4.4 Tipografia (OFL)
**[F]** Archivo Black, Space Mono, IBM Plex Mono, Work Sans e Courier Prime, ou sans/serif/mono do sistema "with blunt scale contrasts, underlined links" ([daisyUI](https://trends.daisyui.com/trend/brutalism/)). **[S]**:

- **Corpo:** 16–18px em `system-ui` ou mono.
- **Escala:** razão de 1.5–2.0, com display de 8–20vw dentro de `clamp()`.
- **Pesos:** só 400 e 700/900.
- **Display:** caixa alta com −0.03em.
- **Performance:** fontes do sistema não pesam nada.

#### 4.5 Cor
**[F]** Preto e branco com um acento utilitário duro (azul ou vermelho). As cores padrão de link e foco podem ser mantidas ([daisyUI](https://trends.daisyui.com/trend/brutalism/)). Tokens **[S]**: `--bg:#fff; --fg:#000; --link:#0000EE; --visited:#551A8B; --accent:#FF0000`.

#### 4.6 Componentes
**[F]** Radius `0` ou `0.25rem`, rules grossas, bordas expostas, controles nativos e mídia full-bleed ([daisyUI](https://trends.daisyui.com/trend/brutalism/)). "Hyperlinks are underlined and buttons look like buttons" ([brutalist-web.design](https://brutalist-web.design/)).

```css
/* [S] não testado nesta pesquisa */
body.raw{font:16px/1.5 system-ui,sans-serif;max-width:72ch;margin:2rem auto;padding:0 1rem}
.raw a{color:#0000EE;text-decoration:underline;text-underline-offset:.15em}.raw a:visited{color:#551A8B}
.b-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:2px;background:#000;border:2px solid #000}
.b-grid>*{background:#fff;padding:1rem}
.b-mega{font:900 clamp(3rem,14vw,14rem)/.85 "Archivo Black",sans-serif;text-transform:uppercase;letter-spacing:-.04em;overflow-wrap:anywhere}
```

#### 4.7 Efeitos, movimento e configurações
**[F]** "Immediate state changes, hard cuts, native scrolling, and occasional raw marquees". Transições decorativas suaves ficam de fora ([daisyUI](https://trends.daisyui.com/trend/brutalism/)). **[S]** Inversão instantânea no hover (`a:hover{background:#000;color:#fff}`) e, como easter egg, um toggle de "dev mode" que mostra o grid com `outline:1px solid red`.

#### 4.8 Riscos de acessibilidade e performance
**[F]** Críticos apontam que o brutalismo "jarring" carece de hierarquia e de jornada clara; por outro lado, tipo forte e alto contraste ajudam alguns usuários com baixa visão ([LogRocket](https://blog.logrocket.com/ux-design/web-brutalism/)). A opinião de que "a limitação radical pode aumentar conversões" não vem acompanhada de dados ([Smashing](https://www.smashingmagazine.com/2020/01/split-personality-brutalist-web-development/)). **[S]**:

- Manter os sublinhados.
- Texto rotacionado ou sobreposto preserva a ordem do DOM.
- Cursores customizados não escondem o ponteiro.
- Tabelas usam `<th scope>`.
- Testar reflow a 320px.

A variante B1 é a mais rápida e acessível do catálogo inteiro.

#### 4.9 Encaixe de marca
**[F]** Sites editoriais, portfólios de artistas, projetos culturais e marcas contraculturais ([daisyUI](https://trends.daisyui.com/trend/brutalism/)). **[S]** Livraria ou galeria independente pedem B2. Manifestos e ferramentas dev pedem B1. Escritório de advocacia, banco e clínica devem evitar o estilo, ou usar só um B1 tipográfico contido.

#### 4.10 Antipadrões
**[S]**:

- Misturar sombras suaves, gradientes ou radius grandes, o que deixa o site com cara de "corporativo inacabado".
- Esconder a nav em truques.
- Remover sublinhados.
- Tipo gigante que estoura no mobile.
- Usar a variante jarring em checkout ou formulários.

#### 4.11 Exemplos e referências
**[F]** (status ao vivo **[NV]**): Bloomberg, 56 Digital e Craigslist (funcionais). Twomuch.Studio e A2-Type (tipográficos) ([LogRocket](https://blog.logrocket.com/ux-design/web-brutalism/)). Théâtre Saint-Gervais (saintgervais.ch), Kane Robinson e Studio Push ([Bejamas](https://bejamas.com/insights/field-notes/neubrutalism-web-design-trend)). Drudge Report. Toiletpaper e Ji Soo Eom (arte). Diretório: brutalistwebsites.com. Manifesto: brutalist-web.design.

---

### 5. Neo-brutalist (neubrutalism)

**Eixo:** estética primária. Expressivo sobre UX convencional; risco médio a alto conforme o setor.

#### 5.1 Definição e traços-assinatura
A NN/g (abril de 2025) define o estilo como uma evolução do brutalismo, feita de "raw, unrefined elements" com cores fortes e formas simples, que combina o estilo brutalista com o design gráfico dos anos 1990 **[F]** ([NN/g](https://www.nngroup.com/articles/neobrutalism/)). A NN/g aponta cinco traços:

1. Alto contraste e cores vivas.
2. Linhas grossas e formas geométricas.
3. Sombras sólidas deslocadas.
4. Tipo forte e excêntrico como ponto focal.
5. Referências retrô, como botões estilo Windows 98 e mono.

O daisyUI chama o estilo também de "Neo Memphis" e resume: "wraps conventional UX in loud geometric blocks, dark outlines, hard offset shadows, flat color, and exaggerated type". O período vai do início dos anos 2020 até hoje **[F]** ([daisyUI](https://trends.daisyui.com/trend/neubrutalism/)). A Bejamas o lê como reação ao neumorfismo e ao glassmorphism, com pseudo-3D isométrico a 45° e ilustração cartunesca **[F]** ([Bejamas](https://bejamas.com/insights/field-notes/neubrutalism-web-design-trend)). Atribuir a popularização ao rebrand do Gumroad em 2021 é comum, mas não foi verificado **[NV]**.

Teste de reconhecimento **[S]**: todo card e todo botão têm borda preta de 2–4px e sombra preta sólida deslocada, com preenchimentos saturados sobre página off-white.

#### 5.2 Variantes
**[F]** Radius 0 (mais perto do brutalismo) ou 4–8px (comum em bibliotecas). Acima de cerca de 12px o estilo "reads as a different look" ([The Plus Addons](https://theplusaddons.com/blog/neo-brutalism-web-design/)). De 1 a 3 acentos ([daisyUI](https://trends.daisyui.com/trend/neubrutalism/)), ou 2–3 cores segundo a NN/g. Em fundo escuro, a sombra se inverte (`6px 6px 0 #fff`), como em feastables.com ([The Plus Addons](https://theplusaddons.com/blog/neo-brutalism-web-design/)).

| Variante **[S]** | Valores-chave | Usar para |
|---|---|---|
| N1 Candy | página off-white, 3 acentos, borda de 3px, sombra de 6px, radius 0–8px | ferramentas para criadores, marketing SaaS, startups de consumo |
| N2 Mono/limited | preto, branco e um acento amarelo ou lime | ferramentas dev B2B, um tom mais "sério" |
| N3 Soft/rounded | radius 8–12px (limite da fonte), fills pastel, borda de 2px | edtech, produtos infantis, comida |
| N4 Dark inverted | superfície escura, borda e sombra brancas | gaming, vida noturna |

#### 5.3 Layouts e padrões de página
**[F]** "Conventional navigation and task flow beneath an irregular modular grid", com controles grandes, sobreposições ocasionais, ilustração outline, motivos de papel milimetrado e fragmentos de janela de browser ([daisyUI](https://trends.daisyui.com/trend/neubrutalism/)). A NN/g recomenda 24–32px de padding em torno de formas densas e headlines com cerca de 2× o tamanho do corpo ([NN/g](https://www.nngroup.com/articles/neobrutalism/)). O card de referência tem padding de 24px ([The Plus Addons](https://theplusaddons.com/blog/neo-brutalism-web-design/)).

Estrutura de página **[S]**:

- **Hero:** headline enorme à esquerda, uma palavra marcada como marca-texto, dois CTAs com borda e uma "janela de browser" com borda; stickers rotacionados entre −3° e 6°.
- **Features:** bento de cards com borda e preenchimentos alternados.
- **Logos:** faixa com borda ou marquee.
- **Pricing:** três cards, o destacado com sombra maior.
- **FAQ:** `<details>` com borda.
- **Footer:** bloco preto invertido.
- **Mobile:** sombras de 6–8px caem para 3–4px, bordas para 2–3px, e os alvos ficam com 44px ou mais.

#### 5.4 Tipografia (OFL)
**[F]** Display: Syne e Archivo Black. Funcional e corpo: Space Grotesk, DM Sans e Space Mono ([daisyUI](https://trends.daisyui.com/trend/neubrutalism/)). Faces decorativas ou condensadas não servem para corpo ([NN/g](https://www.nngroup.com/articles/neobrutalism/)). **[S]**:

- **Corpo:** 16–18px, peso 400/500.
- **h1:** `clamp(2.5rem, 6vw + 1rem, 6rem)`, peso 700–800.
- **Line-height:** 1.0–1.1 no display e 1.5–1.6 no corpo.

#### 5.5 Cor
Esta é a paleta mais bem documentada do catálogo, com contrastes contra texto `#000` **[F]** ([The Plus Addons](https://theplusaddons.com/blog/neo-brutalism-web-design/)):

| Cor | Hex | Contraste com #000 |
|---|---|---|
| White card | `#FFFFFF` | 21:1 |
| Off-white page | `#FAF7F0` | 19.63:1 |
| Lime | `#C4F000` | 15.81:1 |
| Yellow | `#FFDE00` | 15.70:1 |
| Cyan | `#00E5FF` | 13.65:1 |
| Hot pink | `#FF69B4` | 7.93:1 |

A mesma fonte dá o azul de foco `#0044FF` e mostra que um par neumórfico (`#E0E0E0`/`#A3B1C6`) mede apenas **1.65:1**. A cor de página do daisyUI é `#f1f0eb` **[F]**. A NN/g avisa que pares como amarelo e ciano falham em legibilidade **[F]**. Regra **[S]**: texto sobre acentos é sempre `#000` ou `#111`, nunca branco sobre amarelo, lime ou ciano.

#### 5.6 Componentes
**[F]** Borda de 2–5px (o exemplo usa `4px solid #000`). Sombra dura sem blur, `6px 6px 0 #000`; o neobrutalism.dev usa `4px 4px 0 0 rgba(0,0,0,1)`. Radius 0–8px (o exemplo usa 6px) e padding de 24px. Estados do botão: no hover e no `:focus-visible`, `translate(3px,3px)` com sombra de 3px; no `:active`, `translate(6px,6px)` com sombra 0; transições de 80ms ou menos, até cerca de 100ms; foco `3px solid #0044FF` com offset de 3px ([The Plus Addons](https://theplusaddons.com/blog/neo-brutalism-web-design/)). A fonte tem uma incoerência interna: a figura de anatomia diz offset de 14px e o código diz 6px. O neobrutalism.dev é uma biblioteca de 64 componentes para React/Tailwind v4 ([neobrutalism.dev](https://www.neobrutalism.dev/)).

```css
/* [S] receita vanilla a partir dos valores [F] acima; não testada */
:root{--ink:#000;--bw:3px;--sh:6px;--r:6px}
.nb-btn{font:700 1rem/1 "Space Grotesk",system-ui;padding:.875rem 1.25rem;min-height:44px;background:#FFDE00;color:var(--ink);
  border:var(--bw) solid var(--ink);border-radius:var(--r);box-shadow:var(--sh) var(--sh) 0 var(--ink);transition:transform 80ms,box-shadow 80ms}
.nb-btn:hover{transform:translate(3px,3px);box-shadow:3px 3px 0 var(--ink)}
.nb-btn:active{transform:translate(var(--sh),var(--sh));box-shadow:0 0 0 var(--ink)}
.nb-btn:focus-visible{outline:3px solid #0044FF;outline-offset:3px}
.nb-card{background:#fff;border:var(--bw) solid var(--ink);border-radius:var(--r);box-shadow:8px 8px 0 var(--ink);padding:24px}
.nb-mark{background:#C4F000;padding:0 .2em;border:2px solid #000;box-decoration-break:clone}
@media (max-width:600px){:root{--sh:4px;--bw:2px}}
```

#### 5.7 Efeitos, movimento e configurações
**[F]** "Lift by increasing the hard shadow, press by translating into the shadow, with abrupt slides, stamps, or tilts" ([daisyUI](https://trends.daisyui.com/trend/neubrutalism/)). **[S]** Para o reveal de "carimbo", um IntersectionObserver adiciona `.in`, e a animação vai de `scale(1.15) rotate(-3deg); opacity:0` até o estado normal em 180ms, com `steps(3)` ou `cubic-bezier(.2,1.6,.4,1)`.

#### 5.8 Riscos de acessibilidade e performance
**[F]** A NN/g lista os riscos: o estilo pode sobrecarregar o usuário, pares de cor podem falhar, tipo decorativo no corpo prejudica a leitura, elementos interativos ficam difíceis de reconhecer e a hierarquia e os CTAs perdem força. As correções propostas são checker de contraste, 2–3 cores, corpo neutro, padding de 24–32px, pistas de interatividade e testes com usuários ([NN/g](https://www.nngroup.com/articles/neobrutalism/)). O alto contraste "can cause anxiety for others" ([Bejamas](https://bejamas.com/insights/field-notes/neubrutalism-web-design-trend)). **[S]**:

- A borda de 3px já ajuda a cumprir a 1.4.11.
- O "press" não pode ser a única pista de estado; use também `aria-pressed`.
- Stickers rotacionados ficam dentro de ±6°.

A performance é barata, porque sombras sem blur pintam pouco.

#### 5.9 Encaixe de marca
**[F]** Startups, produtos para criadores, portfólios, projetos culturais, marcas jovens e páginas de marketing expressivas ([daisyUI](https://trends.daisyui.com/trend/neubrutalism/)). Ruim para finanças, saúde e bancos ([Bejamas](https://bejamas.com/insights/field-notes/neubrutalism-web-design-trend)). **[S]** SaaS ou ferramenta de criador pede N1/N2. Café ou food truck pede N3.

#### 5.10 Antipadrões
**[S]**:

- Tudo com o mesmo peso visual (NN/g).
- Mais de três acentos.
- Branco sobre amarelo.
- Sombras com blur ou gradientes.
- Radius acima de 12px.
- Direções ou offsets de sombra inconsistentes.
- Uma "parede de caixas".

#### 5.11 Exemplos e referências
**[F]** (status ao vivo **[NV]**). A NN/g cita Gumroad, o refresh da Figma, o e-commerce da Tony's Chocolonely (feito pela Tinloof), 99percentoffsale.com, byooooob.com, cyanbanister.com, bieffeforniture.it, Dodonut, The API World, Sui Overflow 2025 e Halo Lab ([NN/g](https://www.nngroup.com/articles/neobrutalism/)). A Bejamas cita Gumroad, Figma, thegreatlake.fun, cleanwith.plus e Budapest Park. O feastables.com tem sombras duras confirmadas. A home do Gumroad servida atualmente **não tem `box-shadow`**, então talvez já não sirva de referência pura ([The Plus Addons](https://theplusaddons.com/blog/neo-brutalism-web-design/)). Guia: neubrutalism.co.

---

### 6. Bento grid

**Eixo:** layout, não estética. Combina com qualquer estética e qualquer superfície. Risco baixo a médio.

#### 6.1 Definição e traços-assinatura
Bento são "meticulously organized web layouts reminiscent of Japanese bento boxes". A Apple popularizou o padrão em infográficos promocionais, e o CSS Grid somado ao minimalismo impulsionou sua difusão **[F]** ([freeCodeCamp](https://www.freecodecamp.org/news/bento-grids-in-web-design/)). Princípios da mesma fonte:

- Agrupar conteúdo relacionado por célula.
- Variar os tamanhos para criar hierarquia, que também se constrói com cor, tipo e posição.
- Usar o centro como ponto focal.
- Limitar o grid a **≤ 9 caixas**.

A Mockuuups acrescenta compartimentos distintos, mídia mista, tamanhos variados, limites claros, tipo forte sobre paleta contida e hovers interativos **[F]** ([Mockuuups](https://mockuuups.studio/blog/post/best-bento-grid-design-examples/)). Checklist **[S]**:

1. Um grid de 4–12 colunas.
2. De 5 a 9 tiles com spans mistos (1×1, 2×1, 1×2, 2×2).
3. Gap uniforme.
4. Um radius compartilhado.
5. Um tile para cada ideia.
6. Um tile "herói" dominante.

#### 6.2 Variantes
**[F]** A StudioMeyer descreve duas configurações ([StudioMeyer](https://studiomeyer.io/en/blog/bento-grid-layouts)). Na *página de produto*, o hero ocupa 2×2, os features 1×1 e um destaque 2×1. No *dashboard*, uma linha de 4 KPIs, um gráfico de 3–4 colunas e widgets de 2 colunas. A Mockuuups nomeia outras quatro: storytelling (Apple.com), interativa (create.video), editorial mínima (literal.club), link-in-bio (bento.me) e case study (Koto) ([Mockuuups](https://mockuuups.studio/blog/post/best-bento-grid-design-examples/)).

| Variante **[S]** | Assinatura | Usar para |
|---|---|---|
| Product (Apple) | imagem grande, uma afirmação ou métrica por tile, fundo neutro claro ou escuro | lançamentos, tours de features de hardware e SaaS |
| Dashboard | tiles densos, KPIs primeiro, gráficos nos tiles largos | analytics, fintech, seções de resultados |
| Editorial/portfolio | tiles de foto, citação e social, uma cor por tile | agências, criadores, link-in-bio, páginas Sobre |

#### 6.3 Layouts e padrões de página
**[F]** Colunas: 4–6 no desktop (≥1024px), 2–3 no tablet (768–1023px) e 1–2 no mobile (<768px), sempre mobile-first. Gaps de **16–24px**, nunca abaixo de 16px. **Não mais de 1–2 tiles herói por altura de viewport** ([StudioMeyer](https://studiomeyer.io/en/blog/bento-grid-layouts)). Uma receita de tutorial usa `repeat(6,1fr)`, `gap:1.5vw` e `max-width:1500px` com `grid-template-areas`, passando a 4 colunas em 1000px e a 3 em 750px ([freeCodeCamp](https://www.freecodecamp.org/news/bento-grids-in-web-design/)).

Densidade **[S]**:

| Densidade | Gap | Radius do tile | Padding |
|---|---|---|---|
| Compact (dashboard) | 12–16px | 12–16px | 16–20px |
| Standard (SaaS) | 16–20px | 20–24px | 24–32px |
| Airy (Apple) | 20–24px | 24–32px | 32–48px |

Os cantos internos são concêntricos: radius interno igual ao externo menos o padding **[S]**.

```css
/* [S] receitas grid-template-areas */
.bento{display:grid;gap:var(--gap,20px);grid-template-columns:repeat(4,minmax(0,1fr));grid-auto-rows:minmax(180px,auto);max-width:1200px;margin-inline:auto;padding-inline:16px}
.bento--a{grid-template-areas:"hero hero a b" "hero hero c c" "d e e f"}          /* produto */
.bento--c{grid-template-areas:"k1 k2 k3 k4" "chart chart chart side" "chart chart chart side" "t1 t1 t2 t2"} /* dashboard */
@media (max-width:1023px){.bento{grid-template-columns:repeat(2,1fr)}.bento--a{grid-template-areas:"hero hero" "a b" "c c" "d e" "f f"}}
@media (max-width:640px){.bento{grid-template-columns:1fr;grid-template-areas:none}.bento>*{grid-area:auto!important}}
```

Recomposição no mobile **[S]**:

- O hero continua primeiro e em largura total.
- O 2×2 vira largura total em 4:3.
- Pares de métricas podem ficar 2-up a partir de 360px.
- Uma fileira com `scroll-snap` é alternativa para 4 ou mais tiles pequenos.

Esqueleto de página **[S]**: hero, depois bento de features (6–9 tiles), prova social, um segundo bento, pricing e CTA.

#### 6.4 Tipografia (OFL)
**[F]** Tipo forte sobre paleta contida ([Mockuuups](https://mockuuups.studio/blog/post/best-bento-grid-design-examples/)). **[S]**:

- **Fontes:** Inter (ou Inter Display), Geist **[LIC?]**, Manrope, Plus Jakarta Sans e DM Sans.
- **Números:** JetBrains Mono ou Geist Mono.
- **Editorial:** Instrument Serif ou Fraunces.
- **Título do tile:** 20–28px, peso 600.
- **Métrica:** 40–72px, peso 600–700, com −0.02em.
- **Label:** 13–14px, peso 500.

#### 6.5 Cor
**[S]** Página neutra (`#f5f5f7` no claro, `#0a0a0a` no escuro), tiles um passo mais claros ou mais escuros, e 1–2 tiles com a cor da marca ou um gradiente como acento.

#### 6.6 Componentes
**[S]** Um tile = `<li>` ou `<article>` com heading, dentro de `<ul>`. Para tornar o tile inteiro clicável, use um único `<a>` com `::after` esticado, sem links aninhados.

```css
.tile{border-radius:var(--r,24px);padding:clamp(20px,3vw,32px);background:var(--tile);overflow:hidden;position:relative;container-type:inline-size}
/* @container (min-width:420px) alterna empilhado/lado a lado para o tile funcionar em qualquer span */
```

#### 6.7 Efeitos, movimento e configurações
**[F]** Revelações no hover incentivam a exploração ([Mockuuups](https://mockuuups.studio/blog/post/best-bento-grid-design-examples/)). **[S]**:

- Lift de −3px em `.25s cubic-bezier(.2,.8,.2,1)`.
- Spotlight que segue o cursor, via `radial-gradient(400px circle at var(--mx) var(--my), rgb(255 255 255/.12), transparent 40%)`.
- Tilt de no máximo 6°, só com `(pointer:fine)` e sem reduced motion.
- Entrada com stagger de 40–60ms.
- Borda de gradiente animada com `@property` **[SUP?]**: as versões de suporte não foram verificadas.

#### 6.8 Riscos de acessibilidade e performance
**[F]** A ordem de tabulação tem de ser lógica e não pode contradizer a ordem visual ([StudioMeyer](https://studiomeyer.io/en/blog/bento-grid-layouts)). **[S]**:

- Escrever o DOM em ordem de prioridade e posicionar com `grid-template-areas`.
- Evitar `grid-auto-flow: dense` e `order` quando alteram a sequência significativa.
- Usar scrim sob texto sobre imagem.

#### 6.9 Encaixe de marca
**[F]** Revistas, educação e portfólios ([freeCodeCamp](https://www.freecodecamp.org/news/bento-grids-in-web-design/)). Páginas de produto e dashboards ([StudioMeyer](https://studiomeyer.io/en/blog/bento-grid-layouts)). Apresentações de marca e case studies ([Mockuuups](https://mockuuups.studio/blog/post/best-bento-grid-design-examples/)). **Bom [S]:** SaaS e devtools, hardware de consumo, fintech, eventos (agenda, palestrantes, local) e restaurantes (destaques do menu, horário, mapa). **Ruim [S]:** leitura longa, conteúdo jurídico ou governamental e landing de mensagem única.

#### 6.10 Antipadrões
**[F]** Mais de 9 caixas. Mais de 1–2 heróis por viewport. **[S]**:

- Tiles todos do mesmo tamanho (isso é card grid, não bento).
- Radius ou gaps diferentes entre tiles.
- Tiles de enchimento.
- Mais de cerca de 30% dos tiles com texto denso.

#### 6.11 Exemplos e referências
**[F]** (status ao vivo **[NV]**): Apple.com, literal.club, create.video, procreate.com, iconwerk.com, bento.me e o case WhatsApp da Koto ([Mockuuups](https://mockuuups.studio/blog/post/best-bento-grid-design-examples/)). Vercel, Linear, Spotify e Google Analytics são citados sem URL ([StudioMeyer](https://studiomeyer.io/en/blog/bento-grid-layouts)). Galeria: BentoGrids.com.

---

### 7. Glassmorphism (incluindo Apple Liquid Glass)

**Eixo:** superfície/material, aplicado à camada de navegação de outra estética. Risco de legibilidade alto.

#### 7.1 Definição e traços-assinatura
A NN/g define o estilo como "a visual-design style that uses varying levels of see-through translucency to create depth and separate foreground from background, resembling frosted glass". Ele é mais eficaz sobre gradientes ou fundos complexos e popular desde 2020. O Microsoft Fluent chama esse material de **Acrylic**. A NN/g identifica três alavancas: **opacidade** (exemplos de 90/60/30%), **blur** (a 30% de opacidade, 25px ainda deixa bordas distinguíveis e 100px funde o fundo) e **strokes/gradientes** **[F]** ([NN/g](https://www.nngroup.com/articles/glassmorphism/)). O Liquid Glass foi anunciado na WWDC em **9 de junho de 2025** como um material que "refracts and reflects" **[F]** ([Wikipedia](https://en.wikipedia.org/wiki/Liquid_Glass)). Seus traços **[F]** ([Apple WWDC25](https://developer.apple.com/fr/videos/play/wwdc2025/219/)):

- **Lensing**: a lente concentra a luz e o fundo continua nítido.
- **Adaptivity**: elementos pequenos alternam entre claro e escuro.
- **Espessura** proporcional ao tamanho.
- **Resposta à interação**.
- **Scroll-edge effects**.

Checklist **[S]**:

1. Preenchimento com α entre 0.1 e 0.6.
2. `backdrop-filter: blur()` com saturate.
3. Borda clara de 1px ou de gradiente.
4. Fundo vivo e controlado.
5. Sombra suave.
6. Grain opcional.

#### 7.2 Variantes
**[F]** A Apple separa Regular de Clear: o Clear precisa de uma camada de escurecimento e só serve sobre mídia rica com conteúdo forte por cima, e os dois **nunca se misturam**. A tinta deve ser seletiva, só em ações primárias ([Apple WWDC25](https://developer.apple.com/fr/videos/play/wwdc2025/219/)). Glass "acrylic" de blur alto vai sobre fundos desconhecidos; blur baixo só sobre fundos controlados ([NN/g](https://www.nngroup.com/articles/glassmorphism/)). O "liquid glass" na web via `backdrop-filter: url(#svgFilter)` com `feDisplacementMap` funciona **só em Chromium** ([LogRocket](https://blog.logrocket.com/how-create-liquid-glass-effects-css-and-svg/)) **[SUP?]**. A Apple aumentou a opacidade após o beta 1, o iOS 26.1 ganhou um toggle de transparência e a WWDC 2026 (iOS 27) reduziu a transparência padrão e adicionou um slider clear↔tinted ([Wikipedia](https://en.wikipedia.org/wiki/Liquid_Glass)). A própria Apple recuou na transparência.

| Variante **[S]** | Valores-chave | Usar para |
|---|---|---|
| Light frosted | painéis brancos com α 0.25–0.5 sobre gradientes pastel | wellness, beleza, apps de consumo |
| Dark glass | `rgb(255 255 255/.06–.12)` ou `rgb(15 15 20/.4–.6)` sobre blobs neon ou foto | crypto, Web3, IA, gaming, música |
| Liquid (web) | progressive enhancement, só em Chromium, só em controles flutuantes (nav pill, tab bar, CTA) | um acento; nunca em cards de conteúdo |

#### 7.3 Layouts e padrões de página
**[F]** Header sticky com `backdrop-filter: blur(16px)` e um filho de backdrop com altura estendida, para que o conteúdo logo abaixo também alimente o blur ([Josh W. Comeau](https://joshwcomeau.com/css/backdrop-filter)). Glass só na camada de navegação ([Apple](https://developer.apple.com/fr/videos/play/wwdc2025/219/)). Quando o designer controla o fundo, ele deve ser simples ([NN/g](https://www.nngroup.com/articles/glassmorphism/)). Esqueleto **[S]**:

- Fundo de gradient mesh ou blobs fixo (`position:fixed; z-index:-1`).
- Nav pill flutuante a 12–16px do topo, radius 999px.
- Hero com card ou CTA em glass.
- Cards de feature em glass, em 3 colunas.
- Plano de pricing destacado com tinta.
- Modais com camada de escurecimento.

#### 7.4 Tipografia (OFL)
**[S]**:

- **Fontes:** Inter, Outfit, Sora, Space Grotesk (tech/crypto) e Figtree.
- **Evitar:** Satoshi, General Sans e SF Pro, que não são OFL.
- **Corpo:** nunca abaixo de 16px, nunca peso 300 sobre glass, de preferência 500 ou mais.

#### 7.5 Cor
**[S]** O fundo leva 2–4 blobs saturados (`#7c3aed`, `#06b6d4`, `#f472b6`) com blur de 80–120px. O texto é `#fff` sobre glass escuro e `#0b0b10` sobre glass claro. A NN/g recomenda verificar o contraste em todo o componente, porque a translucidez coloca o texto sobre muitas cores **[F]** ([NN/g](https://www.nngroup.com/articles/glassmorphism/)).

#### 7.6 Componentes
**[F]** O web.dev dá três exemplos: `rgba(255,255,255,.3)` com `blur(.5rem)`; um modal com `blur(10px)` e `.5`; e `brightness(150%) saturate(150%) blur(1rem)`. O artigo também registra que `backdrop-filter` diferente de `none` cria um novo stacking context e que o fallback é `@supports not`, com imagem pré-borrada. O texto é de 2019 ([web.dev](https://web.dev/articles/backdrop-filter)).

Josh Comeau acrescenta ([Josh W. Comeau](https://joshwcomeau.com/css/backdrop-filter)):

- Um vidro mais grosso usa `hsl(0 0% 100% / .5–.6)`.
- A borda de vidro é um segundo elemento com `blur(12px) brightness(0.96)`.
- `border-radius` exige uma `<mask>` SVG.
- O suporte passa de **97% (caniuse, outubro de 2026)**.
- O Chromium só corrigiu o recorte com `overflow:hidden` no **Chrome 142** (outubro de 2025).
- No Firefox há um bug com `position: sticky` dentro de um ancestral com overflow e radius, corrigido no Nightly em setembro de 2026 **[SUP?]**.

A receita de Liquid Glass da LogRocket usa `backdrop-filter: url(#liquid-glass-button) brightness(150%)` e uma cadeia SVG `feGaussianBlur(1)` → `feImage` (mapa de deslocamento) → `feDisplacementMap scale=55` → `feColorMatrix saturate 50` → rim especular. Só funciona em Chromium ([LogRocket](https://blog.logrocket.com/how-create-liquid-glass-effects-css-and-svg/)).

```css
/* [S] tokens de glass: fundo sólido por padrão, vidro só dentro de @supports */
:root{--glass-bg:rgb(255 255 255/.18);--glass-bg-solid:rgb(248 248 252/.96);--glass-border:rgb(255 255 255/.35);
  --glass-blur:16px;--glass-sat:160%;--glass-shadow:0 8px 32px rgb(0 0 0/.18);--radius:20px}
.glass{background:var(--glass-bg-solid);border:1px solid var(--glass-border);border-radius:var(--radius);
  box-shadow:var(--glass-shadow),inset 0 1px 0 rgb(255 255 255/.45)}
@supports ((backdrop-filter:blur(1px)) or (-webkit-backdrop-filter:blur(1px))){
  .glass{background:var(--glass-bg);-webkit-backdrop-filter:blur(var(--glass-blur)) saturate(var(--glass-sat));
    backdrop-filter:blur(var(--glass-blur)) saturate(var(--glass-sat))}}
.glass--dark{--glass-bg:rgb(17 17 24/.45);--glass-bg-solid:rgb(17 17 24/.94);--glass-border:rgb(255 255 255/.12)}
@media (prefers-reduced-transparency:reduce){.glass{background:var(--glass-bg-solid);backdrop-filter:none;-webkit-backdrop-filter:none}}
@media (prefers-contrast:more){.glass{background:var(--glass-bg-solid);border-color:currentColor}}
```

Escadas de valores **[S]**:

- **Blur:** 8px em chips, 12–16px em cards e header, 20–24px em modais sobre foto, no máximo 32–40px e raramente.
- **Alpha:** glass claro de 0.15–0.35 sobre gradientes controlados e 0.5–0.7 sobre foto ou vídeo; glass escuro de 0.35–0.6.

`CSS.supports('backdrop-filter','url(#x)')` pode retornar true sem renderizar, então não serve como detecção confiável **[NV]**.

#### 7.7 Efeitos, movimento e configurações
**[F]** Controles do Liquid Glass que se transformam, pulsam ou borbulham distraem com o uso repetido, e controles flutuantes que somem prejudicam a previsibilidade ([NN/g](https://www.nngroup.com/articles/liquid-glass/)). **[S]**:

- Animar os blobs devagar (deriva de 20–40s), nunca o raio de blur.
- Congelar os blobs sob reduced motion.
- Não copiar para a web as abas que viram busca.

#### 7.8 Riscos de acessibilidade e performance
**[F]** A NN/g registra que, no iOS 26, texto sobre foto perde contraste, texto sobre texto fica ilegível, controles se fundem ao conteúdo, barras de busca claras passam despercebidas e os alvos ficam apertados ([NN/g](https://www.nngroup.com/articles/liquid-glass/)). Designers disseram à Wired que a transparência prejudica a leitura sob luz do sol ([Wikipedia](https://en.wikipedia.org/wiki/Liquid_Glass)). `prefers-reduced-transparency` tem disponibilidade limitada: Chrome/Edge 118+, Firefox 113 (talvez atrás de flag), Samsung 25 e **nenhum Safari**, segundo um espelho do MDN que pode estar atrasado ([w3cub](https://docs.w3cub.com/css/@media/prefers-reduced-transparency)) **[SUP?]**.

Correções **[S]**:

- Testar o contraste contra o pixel *pior* do fundo.
- Fundo sólido como padrão.
- Overrides para `prefers-reduced-transparency` e `prefers-contrast`, mais um toggle na página (necessário para usuários de Safari).
- `scroll-padding-top` para cumprir a 2.4.11.
- Nunca texto corrido sobre glass em cima de vídeo.

Performance **[S]**:

- No máximo 3–5 elementos com `backdrop-filter` visíveis ao mesmo tempo.
- Nada de camadas de blur em viewport inteira.
- Blur de no máximo 24px em superfícies grandes.
- No mobile, 8–12px ou fundo sólido.

#### 7.9 Encaixe de marca
**Bom [S]:** produtos de IA, dashboards de crypto/DeFi, música e streaming, gaming, beleza e wellness (glass claro) e widget de reserva de viagem sobre foto. **Ruim [S]:** formulários de saúde, governo, fluxos bancários, grades de produto de e-commerce (o vidro prejudica a fidelidade de cor) e tabelas densas.

#### 7.10 Antipadrões
**[F]** Glass na camada de conteúdo, glass sobre glass, Regular misturado com Clear e tinta em tudo ([Apple](https://developer.apple.com/fr/videos/play/wwdc2025/219/)). Texto sobre imagem movimentada, movimento decorativo, controles instáveis e alvos apertados ([NN/g](https://www.nngroup.com/articles/liquid-glass/)). **[S]**:

- Glass sem fundo colorido, que fica cinza.
- Texto branco sobre glass claro.
- Mais de uma camada de blur empilhada.
- Parágrafos longos sobre glass.
- `backdrop-filter` animado.

#### 7.11 Exemplos e referências
Sistemas de referência **[F]**: Fluent Acrylic, materiais do visionOS e Liquid Glass no OS 26. Roundups de sites com glass foram bloqueados por verificação anti-bot, então não há lista verificada. Candidatos **[NV]**: a nav global do apple.com, linear.app, raycast.com, vercel.com e stripe.com.

---

### 8. Neumorphism / Soft UI

**Eixo:** superfície, só como acento. O risco de acessibilidade é o mais alto do catálogo.

#### 8.1 Definição e traços-assinatura
É um estilo de GUI entre o skeuomorfismo e o flat, em que os elementos **têm a mesma cor do fundo** e se destacam apenas por sombras e luzes **[F]** ([Wikipedia](https://en.wikipedia.org/wiki/Neumorphism)). Origem segundo a Wikipedia: um mockup bancário de Alexander Plyuto no Dribbble, com o termo cunhado por **Jason Kelly em 2019**, e o HarmonyOS no Honor Vision TV (agosto de 2019) como proto-exemplo. A Webflow data o conceito de Plyuto de **2020**, o que é um conflito entre fontes ([Webflow](https://webflow.com/blog/neumorphism)). O declínio veio rápido: o macOS Big Sur (novembro de 2020) trouxe o estilo para o mainstream e as críticas junto, e em 2021 a maioria dos designers já tinha mudado de direção **[F]** (Webflow). A Wikipedia considera o Big Sur mais próximo do glassmorphism.

Checklist **[S]**:

1. Fundo monocromático de tom médio, nunca branco ou preto puro.
2. Preenchimento igual ao fundo.
3. Sombras pareadas, clara em cima à esquerda e escura embaixo à direita.
4. Radius grandes.
5. `inset` para estados pressionados.
6. Um acento mínimo.

#### 8.2 Variantes
**[F]** Direção da luz definida pelo sinal dos offsets. Superfícies **flat**, **convex** (gradiente claro→escuro), **concave** (invertido) e **pressed/inset**. A direção recomendada hoje é **híbrida**: usar o estilo "sparingly, mainly as an accent alongside another design system" ([CSS-Tricks](https://css-tricks.com/?p=304931)). O neumorfismo "shouldn't be the dominant style" ([OpenReplay](https://blog.openreplay.com/implementing-neumorphic-shadows/)).

| Variante **[S]** | Valores-chave | Usar para |
|---|---|---|
| Light soft UI | fundo ≈`#e0e5ec` | vitrines calmas de produto, smart home, áudio |
| Dark soft UI | fundo ≈`#2a2d32`, com a sombra "clara" só um pouco mais clara que o fundo | dashboards dark, players de música |
| Hybrid (padrão recomendado) | texto e botões flat de alto contraste, cards ou toggles neumórficos decorativos | qualquer uso real |

#### 8.3 Layouts e padrões de página
**[F]** O estilo pede padding e margem extras e funciona melhor em cards grandes e contêineres estáticos. Inputs, selects e barras de progresso devem ficar de fora ([CSS-Tricks](https://css-tricks.com/?p=304931)). **[S]** Esqueleto: uma única cor de fundo na página inteira, hero com dispositivo ou ilustração centralizada, 2–3 cards em relevo, uma demo de toggle e um CTA flat de alto contraste.

#### 8.4 Tipografia (OFL)
**[S]** Faces arredondadas: Nunito, Quicksand (só títulos), Poppins e Manrope. O texto é sempre flat, com pelo menos 4.5:1 (por exemplo, `#2d3436` sobre `#e0e5ec`), nunca em relevo.

#### 8.5 Cor
**[F]** Fundos perto do branco ou do preto puros dificultam o contraste das sombras ([CSS-Tricks](https://css-tricks.com/?p=304931)). Exemplos de fundo `#e0e0e0`/`#ebecf0`, com sombra clara `#fff` e escura `#babebc` ([OpenReplay](https://blog.openreplay.com/implementing-neumorphic-shadows/)). **[S]** Lightness HSL de 85–92% no tema claro ou 15–20% no escuro, saturação até 15%, e um acento (como `#6c5ce7`) só para estados ativo, ligado e foco.

#### 8.6 Componentes
**[F]** Duas sombras com offsets de sinais opostos; com luz no topo à esquerda, a sombra escura fica em `+h +v` e a clara em `−h −v`. O estado pressionado usa `inset`. Um leitor achou mais suave usar 4 sombras externas e 2 internas ([CSS-Tricks](https://css-tricks.com/?p=304931)). Valores fixos da OpenReplay **[F]** ([OpenReplay](https://blog.openreplay.com/implementing-neumorphic-shadows/)):

- Container: `-5px -5px 10px #fff, 5px 5px 10px #babebc`.
- Input inset: `inset 7px 2px 10px #babebc, inset -5px -5px 12px #fff`.
- Pressed: `inset 1px 1px 2px #babebc, inset -1px -1px 2px #fff`.
- Razão offset:blur de cerca de 0.5–0.6.

O gerador neumorphism.io produziria `20px 20px 60px #bebebe, -20px -20px 60px #ffffff` sobre `#e0e0e0` **[NV]**.

```css
/* [S] fórmula: d = 0.05–0.1 × tamanho do elemento (cards 8–20px, botões 4–6px), blur b = 2d */
:root{--bg:#e0e5ec;--hi:#ffffff;--lo:#a3b1c6;--d:10px;--b:20px}
.neu{background:var(--bg);border-radius:20px;box-shadow:calc(var(--d)*-1) calc(var(--d)*-1) var(--b) var(--hi),var(--d) var(--d) var(--b) var(--lo)}
.neu--convex{background:linear-gradient(145deg,color-mix(in srgb,var(--bg),#fff 12%),color-mix(in srgb,var(--bg),#000 8%))}
.neu--inset,.neu-btn[aria-pressed="true"]{box-shadow:inset var(--d) var(--d) var(--b) var(--lo),inset calc(var(--d)*-1) calc(var(--d)*-1) var(--b) var(--hi)}
[data-theme=dark]{--bg:#2a2d32;--hi:#363a40;--lo:#1e2024}
```

#### 8.7 Efeitos, movimento e configurações
**[F]** O pressionado é uma sombra inset no `:active` ([CSS-Tricks](https://css-tricks.com/?p=304931)). **[S]** Transição de `box-shadow .15s`. Em muitos elementos, em vez de animar sombras grandes, anime a opacidade de um pseudo-elemento que carrega a sombra.

#### 8.8 Riscos de acessibilidade e performance
**[F]** Os checkers de contraste ignoram sombras, os usuários não identificam o que é interativo, e controles com estado devem ser evitados ([CSS-Tricks](https://css-tricks.com/?p=304931)). As bordas se fundem ao fundo e o estado de foco difere pouco do normal ([UX Collective](https://uxdesign.cc/neumorphism-can-we-make-it-more-accessible-15be5fe2ef28)). Michal Malewicz, que popularizou o termo, sugere usar o estilo só em cards e nunca em controles essenciais ([Built In](https://builtin.com/design-ux/neumorphism-accessibility), 2020). O par neumórfico típico mede **1.65:1** ([The Plus Addons](https://theplusaddons.com/blog/neo-brutalism-web-design/)).

Correções **[S]**:

- Todo interativo ganha borda de 1px com pelo menos 3:1 (`#8a97ab` sobre `#e0e5ec`, a verificar).
- O pressionado vem com mudança de cor ou ícone e `aria-pressed`.
- Foco `outline:3px solid var(--accent)`.
- `forced-colors` ganha borda.

#### 8.9 Encaixe de marca
**Bom, só como acento [S]:** conceitos de smart home e IoT, vitrines de dispositivos de áudio, meditação, calculadoras e páginas de "gadget", experimentos de portfólio. **Ruim [S]:** formulários, checkout, dashboards com muitos estados, públicos com baixa visão e marcas de identidade vibrante (o estilo exige fundo monocromático) ([Wikipedia](https://en.wikipedia.org/wiki/Neumorphism)).

#### 8.10 Antipadrões
**[F]** Inputs, selects e barras de progresso neumórficos, o estilo como dominante e a hierarquia achatada ([CSS-Tricks](https://css-tricks.com/?p=304931); [OpenReplay](https://blog.openreplay.com/implementing-neumorphic-shadows/)). **[S]** Fundos `#fff` ou `#000` puros, texto em relevo e estado ou CTA indicados só por sombra.

#### 8.11 Exemplos e referências
**[F]** *Light and Day* (Webflow Showcase, com bordas de maior contraste), o conceito de Plyuto, os ícones do Big Sur ([Webflow](https://webflow.com/blog/neumorphism)) e o HarmonyOS ([Wikipedia](https://en.wikipedia.org/wiki/Neumorphism)). Sites de marca em produção são raros em 2025–2026, o que por si só indica que o estilo é nicho. O neumorphism.io e coleções do CodePen servem de referência visual.

---

### 9. Claymorphism / soft 3D

**Eixo:** superfície, com um ramo de ilustração 3D. Risco médio, com acessibilidade melhor que a do neumorfismo.

#### 9.1 Definição e traços-assinatura
Michal Malewicz publicou "Claymorphism in user interfaces" no UX Collective em **20 de dezembro de 2021**. Ele descreveu o estilo como algo que sai do mundo de UI "into the art space" e atende ao desejo de "an illusion of depth on our flat screens" **[F]** ([UX Collective](https://uxdesign.cc/claymorphism-in-user-interfaces-1757fabaa377)). O texto completo estava atrás de paywall. O daisyUI chama o claymorphism de "a contemporary interface label, not a historic art movement", com atribuição a Malewicz "commonly attributed" e difícil de provar **[F]** ([daisyUI](https://trends.daisyui.com/trend/claymorphism/)). A OpenReplay diz que o estilo surgiu no Dribbble/Behance em 2022 e o liga a UI de Web3 **[F]** ([OpenReplay](https://blog.openreplay.com/implementing-claymorphism-with-css/)), o que conflita um pouco com a data do artigo de Malewicz. A LogRocket fala em "reimagined neomorphism", com referências a bichos de pelúcia, balões e claymation **[F]** ([LogRocket](https://blog.logrocket.com/ux-design/what-is-claymorphism-web-design/)).

Traços-assinatura **[S]**:

1. Superfícies infladas com 3–4 sombras empilhadas.
2. Radius de 16–32px, cápsulas com 999px.
3. Duas a três famílias pastel sobre um off-white tingido.
4. Sans arredondado pesado.
5. Ícones e ilustrações 3D "de massinha".
6. Movimento elástico.

#### 9.2 Variantes
**[F]** A setproduct separa landing pages 3D ou ilustradas (Spline, Blender) do clay aplicado a componentes ([setproduct](https://preview.setproduct.com/blog/claymorphism-design-guide)). A LogRocket inclui ilustrações e avatares em clay ([LogRocket](https://blog.logrocket.com/ux-design/what-is-claymorphism-web-design/)). Os vizinhos no daisyUI são Kawaii UI, Frutiger Aero e Organic/Blob.

| Variante **[S]** | Valores-chave | Usar para |
|---|---|---|
| Clay UI | componentes feitos de sombra, radius 16–32px, densidade baixa a média | landings de app e SaaS, onboarding, infantil e educação, fintech amigável |
| 3D-illustration-led | UI flat ou levemente soft, com a arte de hero e features carregando o clay, radius 12–20px | marcas que querem personalidade com conteúdo mais denso |

#### 9.3 Layouts e padrões de página
**[F]** Clusters flutuantes centralizados de poucos módulos robustos, com densidade baixa a média e texto curto ([daisyUI](https://trends.daisyui.com/trend/claymorphism/)). Valores da setproduct ([setproduct](https://preview.setproduct.com/blog/claymorphism-design-guide)):

- Nav em pill flutuante.
- Padding de card de 24–28px.
- Gap mínimo de 16px entre elementos clay.
- Alvos de pelo menos **48×48**.
- Botões de 52–56px de altura.
- Escala de 8pt: 4/8/12/16/24/32/48.
- Elevação em três níveis: L0 flat, L1 card em repouso, L2 sheet flutuante (offset de 12px, blur de 32px).
- Nunca empilhar clay em três ou mais níveis.

Landing **[S]**:

- **Topo:** nav pill (`position:sticky; top:12px`), H1 centralizado de até 8 palavras, CTA coral com texto escuro mais um secundário lavanda, e objeto 3D ou três cards flutuando a ±3°.
- **Corpo:** bento de 4–6 cards pastel (`repeat(auto-fit,minmax(260px,1fr)); gap:24px`) e pricing com o card do meio em L2.
- **Fechamento:** FAQ em "poços" inset e faixa de CTA arredondada.

#### 9.4 Tipografia (OFL)
**[F]** A setproduct indica Quicksand, Nunito, Outfit e Fredoka ([setproduct](https://preview.setproduct.com/blog/claymorphism-design-guide)):

- Pesos 500 no corpo, 600 em labels e 700 em títulos.
- H1 de 28–32px e H2 de 22px (escala de app).
- Corpo de no mínimo 16px e legenda de 13px.
- Letter-spacing de 0.01em.
- Line-height de 1.4 no corpo e 1.2 nos títulos.
- **Evitar Inter e Helvetica.**

O daisyUI indica Fredoka, Baloo 2, Nunito, M PLUS Rounded 1c e Sniglet ([daisyUI](https://trends.daisyui.com/trend/claymorphism/)). **[S]** Para web: Fredoka 600–700 ou Baloo 2 800 com Nunito 400–600, H1 `clamp(2.25rem, 5vw + 1rem, 4rem)` (maior que a escala de app da fonte) e corpo de 1–1.125rem com line-height 1.5.

#### 9.5 Cor
**[F]** Paleta da setproduct ([setproduct](https://preview.setproduct.com/blog/claymorphism-design-guide)):

- Página `#F7F5FB` e sheet `#FFFFFF`.
- Lavanda `#B8A6FF`, céu `#9EC9F0`, menta `#7DD4A8`, pêssego `#FFB59E`, rosa `#F5B8D0` e limão `#F5D77A`.
- CTA coral `#FF7A6B`.
- Texto `#2E2A3F` (forte) e `#6B6580` (secundário).
- O matiz da sombra é a cor da superfície escurecida em cerca de 15%, nunca cinza.

**Contradição:** a setproduct afirma que branco sobre coral `#FF7A6B` atinge "at least 4.5". O cálculo dá **2.55:1, que falha**. Texto escuro `#2E2A3F` sobre o coral dá 5.43:1 e passa **[C]**.

Outros pares calculados **[C]**:

| Par | Contraste | Resultado |
|---|---|---|
| `#2E2A3F` sobre lavanda | 6.54 | passa |
| `#2E2A3F` sobre menta | 7.8 | passa |
| `#2E2A3F` sobre limão | 9.8 | passa |
| `#2E2A3F` sobre a página | 12.78 | passa |
| muted `#6B6580` sobre a página | 5.11 | passa |
| branco sobre lavanda | 2.11 | falha |

Regra: texto escuro sobre todos os pastéis.

#### 9.6 Componentes
**[F]** Receita da OpenReplay (radius 30px): `box-shadow: inset -0.6em -0.6em 1em rgba(165,79,29,.6), inset 0.4em 0.4em 0.5em rgba(245,230,221,.6), 0.8em 0.8em 2em rgba(165,79,29,.6)` ([OpenReplay](https://blog.openreplay.com/implementing-claymorphism-with-css/)). Valores da setproduct ([setproduct](https://preview.setproduct.com/blog/claymorphism-design-guide)):

- **Card em repouso:** `8px 8px 24px rgba(108,76,240,.35), inset -6px -6px 16px rgba(80,50,200,.25), inset 6px 6px 16px rgba(255,255,255,.55)`.
- **`:active`:** offsets reduzidos à metade.
- **Spec de 4 camadas:** sombra colorida 8/8/24 a .35, lift branco −8/−8/24 a .6, brilho inset 4/4/8 a .5 e profundidade inset −6/−6/12 a .30.
- **Inputs:** só inset.
- **Radius:** cards 28, botões 18, chips 999, inputs 16, tiles de ícone 20; nunca abaixo de 16px em interativos.

```css
/* [S] tokens clay construídos sobre os valores [F] da setproduct */
:root{--page:#F7F5FB;--ink:#2E2A3F;--lav:#B8A6FF;--mint:#7DD4A8;--cta:#FF7A6B;--r-card:28px;--r-btn:18px}
.clay{--h:108 76 240;border-radius:var(--r-card);background:var(--lav);color:var(--ink);
  box-shadow:8px 8px 24px rgb(var(--h)/.35),-8px -8px 24px rgb(255 255 255/.6),inset 4px 4px 8px rgb(255 255 255/.5),inset -6px -6px 12px rgb(var(--h)/.30)}
.clay-btn{--h:200 80 70;min-height:54px;padding:0 24px;border:0;border-radius:var(--r-btn);background:var(--cta);color:var(--ink);
  box-shadow:6px 6px 16px rgb(var(--h)/.35),inset 3px 3px 6px rgb(255 255 255/.5),inset -4px -4px 8px rgb(var(--h)/.3);transition:transform .14s ease,box-shadow .14s ease}
.clay-btn:hover{transform:translateY(-2px)}.clay-btn:active{transform:scale(.97)}
.clay-btn:focus-visible{outline:3px solid var(--ink);outline-offset:3px}
@media (forced-colors:active){.clay{border:2px solid CanvasText}}
```

#### 9.7 Efeitos, movimento e configurações
**[F]** Transições de 140ms, hover de −2px, press em `scale(.97)` com os offsets pela metade e um "springy bounce on release" sem valores ([setproduct](https://preview.setproduct.com/blog/claymorphism-design-guide)). Elevações flutuantes, um leve squash-and-stretch e um pulo suave no sucesso ([daisyUI](https://trends.daisyui.com/trend/claymorphism/)). **[S]**:

- `--ease-bounce: cubic-bezier(.34,1.56,.64,1)`.
- `--ease-spring: linear(0, .5 7%, 1.06 15%, 1.02 22%, .99 30%, 1 45%)` **[SUP?]**, porque o suporte a `linear()` não foi verificado; manter um fallback em cubic-bezier.
- Pop-in de 320ms.

#### 9.8 Riscos de acessibilidade e performance
**[F]** O clay tem menos problemas óbvios que o neumorfismo ([OpenReplay](https://blog.openreplay.com/implementing-claymorphism-with-css/)). A setproduct recomenda AA de 4.5:1, conferir cada par pastel e "don't rely on shadow alone to show state" ([setproduct](https://preview.setproduct.com/blog/claymorphism-design-guide)). **[S]**:

- Botões com preenchimento de pelo menos 3:1 contra a página, ou com borda de 2px.
- Estado com mudança de cor e `aria-pressed`.
- Borda em `forced-colors`.
- No mobile, 2 camadas de sombra em vez de 4.
- Render estático em AVIF/WebP em vez de embed de Spline ou WebGL.

#### 9.9 Encaixe de marca
**[F]** Onboarding, infantil e educação, fintech amigável e apps de poupança, landings 3D, estados vazios e celebrações. Evitar em tabelas densas, analytics, ferramentas enterprise e admin e leitura longa ([setproduct](https://preview.setproduct.com/blog/claymorphism-design-guide)). **Ruim [S]:** advocacia, infraestrutura B2B, ferramentas clínicas e luxo.

#### 9.10 Antipadrões
**[F]** Sombras cinza ou neutras, radius de botão abaixo de 16px, página `#FFF` pura, ausência do brilho inset em cima à esquerda, clay empilhado em três ou mais níveis, grotesks afiadas e vários CTAs saturados na mesma tela ([setproduct](https://preview.setproduct.com/blog/claymorphism-design-guide)). **[S]** Clay em todo elemento, clay junto com glass na mesma tela, pastel sobre pastel sem âncora escura e direções de luz inconsistentes nos assets 3D.

#### 9.11 Exemplos e referências
**[F]** Demo do daisyUI (trends.daisyui.com/claymorphism/demo/), template "Claylo" da setproduct e avatares 3D de Amrit Pal Singh ([LogRocket](https://blog.logrocket.com/ux-design/what-is-claymorphism-web-design/)). Nenhum site de produção de terceiros foi encontrado. Isso indica que o clay funciona como camada de acento (arte 3D, ícones, onboarding), e não como sistema para o site inteiro.

---

### 10. Retro / vintage

**Eixo:** estética-mãe com presets de era. O risco varia por era, e Mid-century é a mais segura.

#### 10.1 Definição e traços-assinatura
A HubSpot define sites retrô pelo "distinctly old-fashioned look and feel" que vem do tipo, da cor ou dos gráficos. Os recursos comuns são tipo vintage e letterpress, paletas de época, pixel art, halftone, layouts derivados de impressos e texturas de papel **[F]** ([HubSpot](https://blog.hubspot.com/website/retro-websites)). A Wix usa "newstalgia" para tons esmaecidos, estática de TV e referências a VCR **[F]** ([Wix Studio](https://www.wix.com/studio/blog/retro-web-design)). O daisyUI documenta as eras **[F]**:

- **Psychedelic:** de meados dos anos 1960 ao início dos 1970 ([daisyUI](https://trends.daisyui.com/trend/psychedelic-design/)).
- **Mid-century modern:** de meados dos anos 1940 ao fim dos 1960; o rótulo foi popularizado pelo livro de Cara Greenberg em 1984 ([daisyUI](https://trends.daisyui.com/trend/mid-century-modern/)).
- **Synthwave/Outrun:** uma reconstrução dos anos 1980 feita na internet a partir de meados dos 2000; "Outrun" vem do jogo da Sega de 1986 ([daisyUI](https://trends.daisyui.com/trend/synthwave-outrun/)).
- **Web 1.0/Webcore:** de 1991 ao fim dos anos 1990 ([daisyUI](https://trends.daisyui.com/trend/web-1-0-webcore/)).

Traços **[S]**:

1. Paleta específica da era.
2. Display de época com um tipo de leitura neutro.
3. Artefatos de impressão.
4. Recursos gráficos como sunbursts, faixas, selos e sombras duras.
5. Layouts de impresso ou de UI de época.
6. Nostalgia controlada no movimento.

Retro não deve ser modelado como um estilo único, porque as regras de paleta, tipo e forma se contradizem entre as eras **[S]**.

#### 10.2 Variantes
Radius com fonte no daisyUI **[F]**: psychedelic 1–2rem, MCM .25–1rem, synthwave .25–1rem e Web 1.0 0–.25rem. Os usos por era vêm das páginas do daisyUI citadas acima **[F]**.

| Variante | Assinatura e valores-chave | Usar para |
|---|---|---|
| 70s groovy / psychedelic | lettering distorcido, padrões caleidoscópicos, cor saturada, formas líquidas; pills | música, festivais, moda, bares, brechós, cafés |
| Mid-century modern | geometria limpa, cores quentes e esmaecidas, ilustração humanista, bumerangues e starbursts | móveis, arquitetura, hotéis, lojas de design, editorial |
| 80s synthwave | horizonte neon, grid em perspectiva, letreiro cromado, fundo escuro | games, música, automotivo, vida noturna, streaming |
| 90s Web 1.0 | tipo padrão do browser, links azuis, botões chanfrados, GIFs, contadores | sites pessoais, arte, comunidades dev, games, marcas irônicas |
| Print newstalgia **[S]** | letterpress, zine, halftone, papel rasgado | gráficas, livrarias, revistas, cervejarias artesanais |

Memphis, Vaporwave, Jet Age, Retro-Futurism e Halftone/Comic aparecem no índice do daisyUI e entram como candidatos na seção de estilos faltantes.

#### 10.3 Layouts e padrões de página
**[F]** O daisyUI descreve o layout de cada era:

- Psychedelic: composição radial ou espiral com centro forte; horários, preços e controles vão em campos sólidos e calmos.
- MCM: blocos modulares com assimetria relaxada.
- Synthwave: composição cinematográfica com horizonte baixo, e as ações ficam perto das bordas estáveis da tela.
- Web 1.0: fluxo visível do documento, molduras de tabela e nav lateral persistente.

Na prática, os exemplos da HubSpot incluem KLR (parallax), Bialetti (scrapbook animado), Ikony (grid de zine), Harvard Film Archive (livro-caixa), Bonjour Market (marquee) e Bonnie Hong (desktop anos 80 com rastro de cursor) **[F]** ([HubSpot](https://blog.hubspot.com/website/retro-websites)).

Plantas por era **[S]**:

- **70s:** hero com sunburst, headline groovy com sombra dura, selos circulares e faixas listradas como separadores.
- **MCM:** 12 colunas com blocos de cor.
- **Synthwave:** hero escuro com piso em perspectiva e disco de sol; conteúdo em painéis sólidos.
- **90s:** duas colunas com nav à esquerda de 180–200px e rodapé com selos.
- **Mobile, em todas as eras:** coluna única, com sunbursts e grids virando fundos estáticos.

#### 10.4 Tipografia (OFL)
Fontes por era **[F]**:

- Psychedelic: Shrikhand, Fascinate, Modak, Monoton e Yatra One, "only at large sizes".
- MCM: Josefin Sans, Libre Franklin, Fira Sans, League Spartan e Bitter.
- Synthwave: Orbitron, Audiowide, Monoton, Russo One e Bruno Ace SC.
- Web 1.0: Tinos, Arimo, Cousine, Comic Neue e VT323.

As display setentistas comerciais (Frunch, The Sooky 70s, Popsmile e outras) não têm licença declarada e **não servem para um pipeline só OFL** ([Fabrik Brands](https://fabrikbrands.com/best-70s-fonts-for-retro-design/)).

Pares e escalas **[S]**:

| Era | Display | Texto | Escala |
|---|---|---|---|
| 70s | Shrikhand, Modak ou Righteous | DM Sans ou Work Sans | H1 4–7rem, line-height 0.95–1.05, display só a partir de 32px |
| MCM | League Spartan ou Josefin Sans (caixa alta, 0.1em) | Libre Franklin ou Bitter | H1 3–5rem |
| Synthwave | Monoton, Orbitron ou Audiowide | Space Mono ou Rajdhani | títulos neon só a partir de 40px |
| 90s | Tinos, Comic Neue ou VT323 (banners) | Arimo ou Tinos 16px | h1 em 2em |

Righteous, Young Serif e DM Sans são sugestões sem fonte.

#### 10.5 Cor
Paletas por era **[F]**:

- MCM: mostarda, oliva, laranja queimado, teal, nogueira e creme.
- Psychedelic: complementares quase neon, equilibradas com bolsões escuros.
- Synthwave: azul-meia-noite, magenta elétrico, ciano, violeta e laranja-pôr-do-sol.
- Web 1.0: cores seguras de browser, links azuis e visitados roxos.

Nos exemplos da HubSpot aparecem mostarda com verde (KLR), pêssego sobre bordô (Bialetti) e vermelho, preto e branco de letterpress (Old Iron Press). Conjuntos com contraste calculado **[C]**:

| Era | Cores | Pares calculados |
|---|---|---|
| 70s | creme `#F6E8C9`, marrom `#3B2416`, laranja `#E36A2E`, mostarda `#E2A72E`, ferrugem `#A8432A` | marrom/creme 11.94; laranja/creme **2.72, só decorativo**; marrom/laranja 4.39, só texto grande; marrom/mostarda 6.76; branco/ferrugem 6.0 |
| MCM | creme `#F3EBDD`, carvão `#2A2826`, teal `#2F6F73`, laranja queimado `#C8642B` | carvão 12.4; teal/creme 4.87; branco/teal 5.77; laranja/creme **3.34, só texto grande ou UI** |
| Synthwave | navy `#0D0221`, texto `#F5F3FF`, magenta `#FF2A6D`, ciano `#05D9E8` | texto/navy 18.27; magenta/navy 5.54; **branco/magenta 3.62, falha no corpo**; ciano/navy 11.55 |
| 90s | `#FFFFFF`, link `#0000EE`, visitado `#551A8B`, prata `#C0C0C0` | link 9.4; visitado 11.01; preto/prata 11.54; link/prata 5.17 |

#### 10.6 Componentes
Vocabulário de formas **[F]**: bumerangues, losangos e starbursts (MCM); paisleys, espirais e bordas onduladas (psychedelic); botões chanfrados, bordas de tabela de 1px e `<hr>` (Web 1.0). O Paak House usa sombras longas e contornos grossos ([HubSpot](https://blog.hubspot.com/website/retro-websites)).

```css
/* [S] receitas; nenhuma fonte deu valores para halftone, sunburst ou grid synthwave */
.sunburst{background:repeating-conic-gradient(from 0deg at 50% 100%,#E2A72E 0 6deg,#F6E8C9 6deg 12deg)}
.offset{border:3px solid #3B2416;border-radius:16px;box-shadow:6px 6px 0 #3B2416}
.groovy{font-family:Shrikhand,serif;color:#F6E8C9;text-shadow:3px 3px 0 #E36A2E,6px 6px 0 #E2A72E,9px 9px 0 #A8432A}
.halftone{background:radial-gradient(circle,#3B2416 1.2px,transparent 1.6px) 0 0/8px 8px;opacity:.25}
.grid-floor{transform:perspective(300px) rotateX(60deg);transform-origin:bottom;
  background:linear-gradient(#FF2A6D 2px,transparent 2px) 0 0/100% 40px,linear-gradient(90deg,#FF2A6D 2px,transparent 2px) 0 0/40px 100%}
.neon{color:#F5F3FF;text-shadow:0 0 4px #fff,0 0 12px #FF2A6D,0 0 24px #FF2A6D}
.bevel{background:#C0C0C0;border:2px solid;border-color:#fff #404040 #404040 #fff;padding:4px 12px}
.scanlines::after{content:"";position:absolute;inset:0;pointer-events:none;background:repeating-linear-gradient(transparent 0 2px,rgb(0 0 0/.12) 2px 3px)}
```

#### 10.7 Efeitos, movimento e configurações
Movimento por era **[F]**:

- MCM: painéis deslizantes e motivos girando devagar.
- Psychedelic: morph, rotação, respiração e deriva "at slow tempos without obscuring the next action".
- Synthwave: o grid vem na direção do espectador e o neon pulsa.
- Web 1.0: GIFs, marquees e piscadas, "not the only way to convey information".

Recursos **[S]**:

- Marquee de 30s linear.
- Flicker em `steps(1)` mantido abaixo de 3 flashes por segundo.
- Selo girando devagar só quando o movimento está permitido.
- Pausa obrigatória para qualquer movimento que dure mais de 5 s.

#### 10.8 Riscos de acessibilidade e performance
**[F]** Psychedelic: texto prático em baixa densidade e silhuetas de palavra reconhecíveis. Web 1.0: nada de fundos "novidade" atrás do texto. A página de Synthwave não tem seção de acessibilidade. Correções **[S]**:

- Display só a partir de 32px.
- Núcleo sólido quase branco no neon.
- Fundos tileados de anos 90 só nas laterais.
- Nada de grain, halftone e scanlines ao mesmo tempo.
- Ruído pré-renderizado em tile de 128–256px.

#### 10.9 Encaixe de marca
Encaixes por era com fonte nas páginas do daisyUI estão na tabela 10.2 **[F]**. Encaixes ruins **[S]**: 70s em saúde, seguros e governo; synthwave em marcas familiares ou de wellness; 90s em checkout e marcas premium (exceto com ironia). O Mid-century é o retrô mais seguro para negócios.

#### 10.10 Antipadrões
**[S]**:

- Misturar eras sem intenção (groovy com neon synthwave e chanfros de anos 90).
- Display no corpo do texto.
- Excesso de textura.
- Nostalgia de fantasia que esconde o produto.

#### 10.11 Exemplos e referências
**[F]** (status ao vivo **[NV]**). Da HubSpot ([HubSpot](https://blog.hubspot.com/website/retro-websites)): paakhouse.org, accord.dk e tonik.com (70s); klr-interieur.com e bialettistory.com (MCM/vintage); oldironpress.com, ikony.tv, dunderville.se, mondoshop.com e heritagetype.com (impresso); bonniehong.com e music.zajno.com (anos 80/pixel). Da Wix ([Wix Studio](https://www.wix.com/studio/blog/retro-web-design)): themacmc.com, threeuncles.co.uk, strategyfolk.com.au, enigma.cc e treeptours.com. Snippets de synthwave em CSS: [Speckyboy](https://speckyboy.com/css-javascript-snippets-synthwave/).

---

### 11. Y2K

**Eixo:** estética primária. Frutiger Aero entra como subvariante. Risco alto fora dos públicos jovens.

#### 11.1 Definição e traços-assinatura
A Webflow descreve o Y2K como uma recriação da cultura da internet do fim dos anos 1990 e início dos 2000, "digital, spacey, and a little over the top", moldada por hip-hop, rave, embalagens de brinquedo e anúncios da era do iPod. As conexões lentas favoreciam tipo encorpado e gráficos simples **[F]** ([Webflow](https://webflow.com/blog/y2k-aesthetic)). O daisyUI situa o período entre meados dos anos 1990 e cerca de 2001, com revival a partir do fim dos anos 2010. As assinaturas são gradientes cromados, plástico translúcido, letras-bolha, lens flares e ícones brilhantes, e o uso atual do termo é "broader and less historically precise" **[F]** ([daisyUI](https://trends.daisyui.com/trend/y2k/)). O CARI lista entre os motivos "silver eyeshadow, shiny clothing, Oakleys, gradients, and blobby electronics" **[F]** ([CARI](https://cari.institute/aesthetics/y2k-aesthetic)). O Frutiger Aero cobre aproximadamente 2005–2013, teve o nome cunhado retroativamente em 2017 (crédito a Froyo Tam e Sofi Xian) e se caracteriza por azul-verde, gel brilhante, bolhas, água e céu **[F]** ([daisyUI](https://trends.daisyui.com/trend/frutiger-aero/)).

#### 11.2 Variantes
**[F]** A Webflow aponta seis direções: chrome/holográfico, gradientes multichrome, bolhas e blobs, glow neon no escuro, glitch e lo-fi. Aponta também quatro paletas: elétrica, candy, multichrome e monocromática editorial ([Webflow](https://webflow.com/blog/y2k-aesthetic)). A Wix aponta sete, entre elas retrofuturist gradients, pixel/retro-PC, low-fi purist e "analogue UX" ([Wix Studio](https://www.wix.com/studio/blog/y2k-design)). **Y2K Techno-Skeuomorphism** é inspirado em equipamentos de áudio futuristas: prata escovado, LCD azul e botões de transporte chanfrados ([daisyUI](https://trends.daisyui.com/trend/y2k-techno-skeuomorphism/)).

| Variante **[S]** | Assinatura | Usar para |
|---|---|---|
| Y1 Chrome / techno-futurist | prata, azul-gelo, tipo cromado, display techno | moda, música, campanhas |
| Y2 Candy / pastel bubblegum | rosa, aqua e lime; display arredondado; brilhos e stickers | beleza, moda, público jovem, criadores |
| Y3 Cyber / pixel / retro-PC | fundo escuro, neon, pixel, janelas de OS, glitch | música eletrônica, games |
| Y4 Frutiger Aero | céu, água e vidro em azul-verde; sans humanista arredondado | eco-tech, campanhas nostálgicas |
| Y5 Techno-skeuomorphic player | console com display, transporte e dials | música, ferramentas de áudio, games |

#### 11.3 Layouts e padrões de página
**[F]** "Layered, desktop-like compositions with compact device-style windows, floating bubbles, product cutouts", em densidade média, com a regra "Primary actions stay large, and chrome ornament must not crowd labels" ([daisyUI](https://trends.daisyui.com/trend/y2k/)). O cromado deve ficar como acento em cards de hero e CTAs, com os blobs atrás do conteúdo ([Webflow](https://webflow.com/blog/y2k-aesthetic)). **[S]**:

- **Hero:** headline cromado ou iridescente sobre gradient mesh, ou um hero de "desktop" com 2–3 janelas.
- **Cards:** brilhantes, com radius de 16–32px.
- **Nav:** pill brilhante, ou dock inferior só no desktop.
- **Mobile:** janelas empilhadas em cards de largura total e menos blobs.

#### 11.4 Tipografia (OFL)
**[F]** Fontes do daisyUI:

- Y2K: Audiowide, Michroma, Righteous, Syncopate e Zen Dots.
- Techno-skeuo: Share Tech Mono, Orbitron e Chakra Petch.
- Frutiger Aero: Ubuntu, Nunito Sans, Varela Round, Quicksand e M PLUS Rounded 1c.

O texto cromado usa `font-size: clamp(3rem,10vw,8rem); font-weight:800; letter-spacing:-0.02em`, com corpo de no mínimo 16px ([The Plus Addons](https://theplusaddons.com/blog/y2k-web-design.md)). **Ubuntu não é OFL** **[LIC?]**; substitua por Nunito Sans ou Varela Round. Opções pixel OFL **[S]**: VT323, Press Start 2P, Silkscreen e Pixelify Sans. Opções largas: Unbounded, Krona One e Monoton.

#### 11.5 Cor
**[F]** Prata, azul-gelo, rosa-choque, lime e branco ([daisyUI](https://trends.daisyui.com/trend/y2k/)). As paletas candy "need more negative space", e o texto deve ficar em cards de alto contraste ([Webflow](https://webflow.com/blog/y2k-aesthetic)). Paradas do cromado: `#f8f8f8, #b9c4cc, #5d6a75, #ffffff, #8e9aa5, #d8dee3, #6f7b86`. O tipo cromado é cinza médio e costuma falhar sobre fundo claro, e lime sobre ciano é "close to unreadable" ([The Plus Addons](https://theplusaddons.com/blog/y2k-web-design.md)).

Tokens **[S]**, todos a conferir:

- Y2K chrome: `--bg:#0b1020; --ice:#bfe6ff; --pink:#ff5fc8; --lime:#b6ff3d`.
- Y2K pastel: `--bg:#fff4fb; --pink:#ffb3e1; --aqua:#a8f0ff; --ink:#2a1440`.
- Frutiger Aero: `--sky:#3fa9f5; --aqua:#7fe0e6; --grass:#5cc84a; --ink:#0b2a3c`.

Cromado vai sobre navy ou preto, com `-webkit-text-stroke` escuro, e é tratado como texto grande.

#### 11.6 Componentes
**[F]** Radius de `1rem`–`2rem`. Bolhas, cápsulas, estrelas cromadas e janelas chanfradas ([daisyUI](https://trends.daisyui.com/trend/y2k/)). Receitas literais ([The Plus Addons](https://theplusaddons.com/blog/y2k-web-design.md)):

```css
/* [F] receitas literais da fonte */
.chrome{font-size:clamp(3rem,10vw,8rem);font-weight:800;letter-spacing:-0.02em;
  background:linear-gradient(180deg,#f8f8f8 0%,#b9c4cc 28%,#5d6a75 46%,#ffffff 52%,#8e9aa5 58%,#d8dee3 78%,#6f7b86 100%);
  background-clip:text;color:transparent;}
.sparkle{width:64px;aspect-ratio:1;background:linear-gradient(135deg,#b6ff3d,#00e5ff);
  clip-path:polygon(50% 0%,60% 40%,100% 50%,60% 60%,50% 100%,40% 60%,0% 50%,40% 40%);}
/* [S] gel/aqua pill */
.gel{border-radius:999px;padding:.8rem 1.6rem;color:#06223a;font-weight:700;border:1px solid #2b7bd6;
  background:linear-gradient(180deg,#e9f6ff 0%,#9fd3ff 49%,#5aa9f5 50%,#8fd0ff 100%);
  box-shadow:inset 0 1px 0 #fff,inset 0 -2px 6px rgba(0,60,140,.35),0 4px 10px rgba(0,80,180,.3)}
```

As bibliotecas 98.css e XP.css não tiveram licença nem estado de manutenção verificados **[LIC?]**.

#### 11.7 Efeitos, movimento e configurações
**[F]** Brilhos de carregamento, bolhas flutuantes, janelas que saltam, varreduras de lens flare e "springy device interactions" ([daisyUI](https://trends.daisyui.com/trend/y2k/)). O glitch deve ser "brief and targeted" ([Webflow](https://webflow.com/blog/y2k-aesthetic)). O Frutiger Aero é "optimistic rather than futuristic". **[S]**:

- Shine de 1.2s no hover.
- Bolhas flutuando em ciclos de 4–8s, com delays escalonados.
- Glitch em RGB-split com `steps()`, por menos de 600ms e uma vez só.
- Arrasto de janela opcional e acessível por teclado.

#### 11.8 Riscos de acessibilidade e performance
**[F]** Verificar o contraste de `background-clip:text`, usar o cromado só em títulos decorativos, manter texto real e não imagem de texto, e marcar brilhos com `aria-hidden` ([The Plus Addons](https://theplusaddons.com/blog/y2k-web-design.md)). **[S]**:

- Fallback sólido via `@supports not (background-clip:text)`.
- Painéis translúcidos com α de pelo menos 0.85 atrás de texto.
- Pixel fonts só em labels.
- No máximo 2–3 blobs, de preferência pré-borrados.
- MP4/WebM em vez de GIF.

#### 11.9 Encaixe de marca
**[F]** Moda, beleza, música, produtos sociais e marcas jovens ([daisyUI](https://trends.daisyui.com/trend/y2k/)). DTC de roupa sim, banco não ([Wix Studio](https://www.wix.com/studio/blog/y2k-design)). **[S]** Cosméticos e bolsas de maquiagem para Gen-Z pedem Y2 candy, com o cromado de Y1 como acento. Produtor musical ou noite de clube pedem Y3 ou Y5. App eco ou de wellness pede Y4.

#### 11.10 Antipadrões
**[S]**:

- Corpo de texto cromado ou em gradiente.
- Várias faces display ao mesmo tempo.
- Glitch contínuo.
- Texto dentro de imagem.
- Blobs e janelas que escondem o CTA.
- Natureza Frutiger misturada com neon cyber sem intenção.

#### 11.11 Exemplos e referências
**[F]** Da [Webflow](https://webflow.com/blog/y2k-aesthetic) (**[NV]**): digivalet-toffeenut.webflow.io, byooooob.com, pashaink.com, griffo.house, walrus.xyz, akari.lusion.co, portal.thenifty.com, com.manychat.com, poison.studio e unbias-by-sista.webflow.io. A Wix cita WebLabNY, SpaceHey, o site de Olivia Rodrigo, Starface, Public Domain e Digital Fatigue, sem URLs. Demos: trends.daisyui.com/y2k/demo/ e /frutiger-aero/demo/.

---

### 12. Maximalist

**Eixo:** estética primária, com Collage como técnica interna. Alta complexidade e risco alto.

#### 12.1 Definição e traços-assinatura
A Webflow descreve o maximalismo como a recusa da convenção em favor do excesso criativo: ele "embraces discord and incongruity", e "When you want to be loud, maximalism is here to express your creativity". A origem está nos pôsteres psicodélicos dos anos 1960 (Wes Wilson) **[F]** ([Webflow](https://webflow.com/blog/maximalism-web-design)). Traços apontados pela Webflow:

- Absurdo e easter eggs.
- Cor supersaturada que quebra as regras.
- Texturas em conflito.
- Repetição.
- Espaço preenchido, com margens empurradas para a borda.
- Camadas.
- Referências retrô.
- Múltiplas fontes.
- Discordância de escala.

A Envato fala em "brand maximalism": marcas que trocam o flat dos anos 2010 por algo "louder, funnier, stranger, and far more human", com tipos mistos, sticker-bomb e texturas de grain, glitch e halftone **[F]** ([Envato](https://author.envato.com/hub/trend-deep-dive-brand-maximalism/)). A Figma cita Spotify e Liquid Death **[F]** ([Figma](https://www.figma.com/resource-library/web-design-trends/)). Teste de reconhecimento **[S]**: quase nenhum fundo vazio, três ou mais matizes saturados, três ou mais tipos, padrões ou marquees repetidos e movimento lúdico no cursor.

#### 12.2 Variantes
**[F]** A Webflow só nomeia formalmente o maximalismo psicodélico, mas os exemplos dela implicam o retro/8-bit, o caos estilo Geocities e as personas absurdas. A Envato implica o maximalismo tech (Nothing), o heritage (Burberry, 2023) e o sticker-bomb.

| Variante **[S]** | Assinatura | Usar para |
|---|---|---|
| Pattern/ornament | papéis de parede, florais, bordas sobre bordas | interiores, moda, heritage |
| Typographic | tipo ocupando a tela, muitas famílias, marquees | agências, eventos, música |
| Retro/pixel/Y2K | sprites, widgets Geocities, gradientes brilhantes | games, moda Gen-Z, vida noturna |
| Brand/candy (CPG) | cores de marca saturadas, mascotes, stickers, CTAs repetidos | alimentos, bebidas, brinquedos |

#### 12.3 Layouts e padrões de página
**[F]** Preencher o espaço negativo, levar as margens até a borda, sobrepor camadas e compor fora de equilíbrio. A Curry Cafe repete os CTAs e o Y-N10 usa rolagem diagonal ([Webflow](https://webflow.com/blog/maximalism-web-design)). O Choreus usa slideshow full-bleed com tipo grande ([Jack Christian](https://jackchristian.com.au/blog/my-top-5-maximalist-websites/)). **[S]**:

- Blocos de cor em largura total, sem fundo branco.
- Faixas de marquee entre seções.
- Tipo enorme cruzando as linhas das colunas.
- CTA a cada 1–2 telas.
- Cards com borda de 3–4px e `6px 6px 0 #000`.
- No mobile, manter o color blocking e um único CTA primário visível.

#### 12.4 Tipografia (OFL)
**[F]** Múltiplas fontes, incluindo retrô e descasadas, mas com tipo claro sobre o visual agitado; a referência é a capa de *Wimmen's Comix* ([Webflow](https://webflow.com/blog/maximalism-web-design)). A Envato cita faces pixel (Nothing) e serifs decorativas (Burberry). **[S]**:

- **Condensadas:** Anton, Bebas Neue e Big Shoulders Display.
- **Expressivas:** Unbounded, Syne, Climate Crisis, Shrikhand, Bungee e Monoton.
- **Pixel:** Press Start 2P, VT323 e Silkscreen.
- **Corpo:** Inter, Rubik ou Space Grotesk.
- **Limite:** quatro famílias por página.
- **Display:** até 12–20vw em palavras do hero.
- **Variáveis:** Fraunces, Bricolage Grotesque, Unbounded e Syne cobrem várias "personalidades" em um só arquivo.

#### 12.5 Cor
**[F]** Paletas supersaturadas que quebram a teoria das cores, equilibradas com elementos contidos; Mack and Pouya usa rosa, amarelo e azul ([Webflow](https://webflow.com/blog/maximalism-web-design)). **[S]**:

- **Candy:** `#FF3EA5`, `#FFD400`, `#00C2FF`, `#7A2BFF` e `#00D27A`, com `#0B0B0B` para os "pratos" de texto.
- **Branco sobre `#FF3EA5`:** cerca de 3:1, então só texto grande; preto é mais seguro.
- **Amarelo `#FFD400`:** falha com branco.
- **Corpo de texto:** sempre sobre placas sólidas.
- **`prefers-contrast: more` e `forced-colors`:** removem padrões e texturas.

#### 12.6 Componentes
**[F]** Ilustrações excêntricas, animações sem propósito, easter eggs, CTAs piscando e contador de visitas no Dino's ([Webflow](https://webflow.com/blog/maximalism-web-design)). Cursor de borboleta em Ellen Porteus ([Jack Christian](https://jackchristian.com.au/blog/my-top-5-maximalist-websites/)). Sticker-bomb ([Envato](https://author.envato.com/hub/trend-deep-dive-brand-maximalism/)). **[S]**:

- Marquee com botão de pausa e a cópia duplicada em `aria-hidden`.
- Cluster de stickers decorativos.
- Bordas com `border-image` ou xadrez em `repeating-conic-gradient(#FFD400 0 25%, #FF3EA5 0 50%) 0 0/40px 40px`.
- Cards de sombra dura.
- Cursor-toy que nunca substitui o cursor de texto, desligado com `(pointer:coarse)` ou reduced motion.
- Easter eggs que nunca bloqueiam conteúdo.

#### 12.7 Efeitos, movimento e configurações
**[F]** Efeitos 3D borbulhantes com áudio no Slosh Seltzer e scroll animado no Choreus ([Jack Christian](https://jackchristian.com.au/blog/my-top-5-maximalist-websites/)). Nada pode piscar mais de 3 vezes por segundo ([W3C 2.3.1](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html)). **[S]**:

- Marquee de 30s linear.
- Hover elástico em `cubic-bezier(.34,1.56,.64,1)`.
- Cursor via requestAnimationFrame, só com `(pointer:fine) and (prefers-reduced-motion:no-preference)`.
- Piscada estilo Geocities a 1 Hz ou menos, sem flashes vermelhos.

#### 12.8 Riscos de acessibilidade e performance
**[F]** O artigo da Webflow não trata de acessibilidade ([Webflow](https://webflow.com/blog/maximalism-web-design)). **[S]**:

- Textura atrás de texto com opacidade de no máximo 0.08.
- 4.5:1 contra o pior pixel.
- Áudio desligado por padrão (WCAG 1.4.2).
- Nunca rolagem diagonal ou sequestrada.
- Fontes somando no máximo 150–200 KB.
- Limite de camadas com `mix-blend-mode` e `filter`.

#### 12.9 Encaixe de marca
**[F]** O maximalismo "isn't for every audience" e é polarizador ([Webflow](https://webflow.com/blog/maximalism-web-design)). Exemplos por setor: Meow Wolf (arte experiencial), BEHAVE (doces), Vintageria (moda vintage), Curry Cafe e Dino's (restaurantes). Na Envato: Liquid Death, Nothing, Burberry, Pepsi, Duolingo e Crocs. **[S]**:

| Encaixe | Setores |
|---|---|
| Bom | snacks e bebidas CPG, locais de entretenimento, festivais, games, streetwear, brinquedos, vida noturna, estúdios, música |
| Com cuidado | restaurantes (menu e horário precisam ser simples e rápidos) |
| Ruim | saúde, finanças, jurídico, enterprise, serviços públicos, públicos mais velhos |

#### 12.10 Antipadrões
**[S]**:

- Decoração que esconde CTA ou preço.
- Mais de quatro tipos.
- Marquee sem pausa.
- Rolagem diagonal.
- Áudio automático.
- Maximalismo sem sistema, com cores aleatórias por seção e sem tokens.
- Desktop simplesmente encolhido no mobile.

#### 12.11 Exemplos e referências
**[F]** (status ao vivo **[NV]**). Da [Webflow](https://webflow.com/blog/maximalism-web-design): meowwolf.com, eatbehave.com, pablitoplaneta.com, y-n10.com, vintageria.it, dinostomatopie.com, curry.cafe e thegeekdesigner.com. Da [Jack Christian](https://jackchristian.com.au/blog/my-top-5-maximalist-websites/): choreus.co, peststopboys.co.uk e sloshseltzer.com. liquiddeath.com. Candidatos **[NV]**: Fishwife, Omsom, Graza, Poolsuite e MSCHF.

---

### 13. Organic / natural

**Eixo:** estética-mãe com presets de humor. Complexidade baixa a média e risco médio.

#### 13.1 Definição e traços-assinatura
O daisyUI define "Organic / Blob Design" como silhuetas fluidas, curvas assimétricas, blobs suaves e layouts livres no lugar da geometria rígida. O estilo descende da arte biomórfica do início do século XX e foi revivido no fim dos anos 2010 **[F]** ([daisyUI](https://trends.daisyui.com/trend/organic-blob-design/), citando a [Tate](https://www.tate.org.uk/art/art-terms/b/biomorphic)). O biophilic design usa "organic shapes, botanical imagery, earthy colors, natural textures, and gentle motion". Suas raízes passam por Fromm, por *Biophilia* de E. O. Wilson (1984) e pelo trabalho de Kellert, e a fonte avisa que as telas "cannot reproduce all the spatial and sensory effects studied in architecture" **[F]** ([daisyUI](https://trends.daisyui.com/trend/biophilic-design/)). O wabi-sabi vem da cultura do chá (Sen no Rikyū, séculos XV e XVI) e, na versão comercial, muitas vezes se reduz a "a palette of beige ceramics" **[F]** ([daisyUI](https://trends.daisyui.com/trend/wabi-sabi/)). O daisyUI agrupa dez estilos em "Organic and atmospheric UI", entre eles Cottagecore, Solarpunk e Global Village Coffeehouse **[F]** ([daisyUI](https://trends.daisyui.com/organic-atmospheric-ui/)).

Traços **[S]**:

1. Blobs e pedras com bordas de seção onduladas.
2. Paleta terrosa ou botânica sobre creme.
3. Grain ou papel.
4. Serif suave ou sans humanista com entrelinha folgada.
5. Fotografia real de natureza e material.
6. Fades e derivas lentas.

#### 13.2 Variantes
Valores e usos **[F]** das páginas do daisyUI citadas acima; os nomes das variantes são **[S]**.

| Variante | Radius e texturas | Usar para |
|---|---|---|
| Wellness / biophilic | 0.75–1.5rem, `--noise:1`; folha, musgo, argila, casca, céu | spa, yoga, terapia, suplementos, clean beauty, hospitalidade |
| Earthy craft / wabi-sabi | 0–0.25rem, bordas irregulares, `--noise:1`; sem acentos saturados | cerâmica, café, padaria, slow fashion, loja artesanal |
| Botanical / cottagecore | 8–16px mais arcos **[S]**; florais, texturas feitas à mão, serif delicada | floricultura, chá, jardim, bolsas e cosméticos artesanais, comida em pequenos lotes |
| Playful blob | 1–2rem e blobs | SaaS acessível, ferramentas criativas, onboarding |

#### 13.3 Layouts e padrões de página
**[F]** As seções seguem um caminho solto e fluido, mas texto e controles mantêm "one dependable reading spine". O texto fica fora das curvas ([daisyUI](https://trends.daisyui.com/trend/organic-blob-design/)). O biophilic propõe um fluxo aberto inspirado em trilhas e clareiras ([daisyUI](https://trends.daisyui.com/trend/biophilic-design/)). O wabi-sabi pede assimetria quieta, margens irregulares e um único objeto por espaço. Em sites de wellness, a Heights usa uma nuvem flutuante no hero, a Vitl usa cards pastel e a Inessa usa paleta terrosa neutra ([Limely](https://www.limely.co.uk/blog/our-top-10-health-wellness-websites)).

**[S]**:

- **Hero:** foto full-bleed de natureza ou material, ou um split com imagem mascarada em blob sobrepondo a seção seguinte.
- **Transições:** divisor SVG ondulado.
- **Corpo:** fileiras alternadas com imagens em arco ou em forma de pedra.
- **Footer:** borda ondulada ou rasgada.
- **Ritmo:** `padding-block: clamp(4rem, 10vw, 8rem)`.
- **Produtos:** cards off-white sem sombra, imagem com topo em arco e nome em serif.
- **Mobile:** blobs decorativos somem abaixo de 480px.

#### 13.4 Tipografia (OFL)
Fontes por variante **[F]**:

- Blob: Fraunces, Gabarito, Varela Round, Quicksand e Urbanist ([daisyUI](https://trends.daisyui.com/trend/organic-blob-design/)).
- Biophilic: Fraunces, Lora, Alegreya, Nunito Sans e Cormorant Infant, em sentence case ([daisyUI](https://trends.daisyui.com/trend/biophilic-design/)).
- Wabi-sabi: Shippori Mincho, Zen Old Mincho, Sawarabi Mincho, Yuji Syuku e Noto Serif JP, "at modest scale" ([daisyUI](https://trends.daisyui.com/trend/wabi-sabi/)).

Pares e escalas **[S]**:

| Variante | Display | Texto | Escala |
|---|---|---|---|
| Wellness | Fraunces (eixos SOFT/WONK) 400–600 | Nunito Sans ou Lora | H1 `clamp(2.5rem, 6vw, 5rem)`, peso 400–500, line-height 1.6–1.7 |
| Earthy craft | Cormorant, Young Serif ou Shippori Mincho | Alegreya Sans ou Lora | H1 de até 3.5rem; small caps com 0.08em |
| Botanical | Fraunces itálica ou Cormorant itálica | Lora | uma palavra em itálico por headline |

#### 13.5 Cor
**[F]** Tons botânicos, de fruta ou minerais sobre creme ([daisyUI blob](https://trends.daisyui.com/trend/organic-blob-design/)). Folha, musgo, argila, casca, céu e mineral ([biophilic](https://trends.daisyui.com/trend/biophilic-design/)). Argila gasta, cinza, musgo, chá, linho e carvão, "no polished, high-saturation accents" ([wabi-sabi](https://trends.daisyui.com/trend/wabi-sabi/)).

Conjunto calculado **[C]**:

| Cor | Hex | Pares |
|---|---|---|
| Creme | `#F4EFE6` | fundo |
| Tinta | `#2B2A26` | sobre creme 12.54 |
| Musgo | `#4F6B3A` | texto sobre creme 5.24; branco sobre musgo 6.01 |
| Terracota | `#B5563A` | sobre creme **4.21, só texto grande**; branco sobre terracota 4.82 |
| Sálvia | `#A3B18A` | tinta sobre sálvia 6.3 |
| Muted | `#6E6A5E` | sobre creme 4.72 |

#### 13.6 Componentes
**[F]** Blobs, cards de pedra, ondas suaves e recortes circulares irregulares. Arcos de folha e divisores em forma de galho ([daisyUI](https://trends.daisyui.com/trend/biophilic-design/)). Grain feito em SVG com `feTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3" stitchTiles="stitch"`. Ele deve ser salvo como arquivo separado, porque a referência por `id` a partir do CSS não funciona, e mesclado com `multiply` e `isolation:isolate`. Blink e WebKit mesclam de formas um pouco diferentes **[F]** ([CSS-Tricks](https://css-tricks.com/grainy-gradients/)).

```css
/* [S] */
.blob{border-radius:63% 37% 54% 46% / 55% 48% 52% 45%;aspect-ratio:1;background:#A3B18A}
@media (prefers-reduced-motion:no-preference){.blob{animation:morph 18s ease-in-out infinite alternate}
  @keyframes morph{to{border-radius:40% 60% 35% 65% / 60% 35% 65% 40%}}}
.arch{border-radius:999px 999px 16px 16px;overflow:hidden}
.pebble{border-radius:46% 54% 43% 57% / 52% 44% 56% 48%;overflow:hidden}
.wave{display:block;width:100%;height:clamp(40px,6vw,80px);margin-bottom:-1px}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:100;background:url(/img/noise.svg);opacity:.08;mix-blend-mode:multiply}
.squiggle{text-decoration:underline wavy #B5563A;text-underline-offset:.25em;text-decoration-thickness:2px}
```

#### 13.7 Efeitos, movimento e configurações
**[F]** As silhuetas se transformam devagar ([blob](https://trends.daisyui.com/trend/organic-blob-design/)). O movimento sugere brisa, crescimento ou respiração, e "ambient effects should stop around focused tasks" ([biophilic](https://trends.daisyui.com/trend/biophilic-design/)). O wabi-sabi pede crossfades imperfeitos e evita a precisão de máquina ([wabi-sabi](https://trends.daisyui.com/trend/wabi-sabi/)). **[S]** `--ease-calm: cubic-bezier(.25,.1,.25,1)`, fades de 800ms e deriva de 12s.

#### 13.8 Riscos de acessibilidade e performance
**[F]** Os alvos interativos devem ter tamanho previsível, mesmo com formas irregulares ([daisyUI](https://trends.daisyui.com/trend/organic-blob-design/)). Há uma reclamação anedótica sobre o custo de performance do `feTurbulence` ([CSS-Tricks](https://css-tricks.com/grainy-gradients/)). **[S]**:

- Painel creme sólido, ou com pelo menos 85% de opacidade, atrás do texto.
- Grain com opacidade de 0.08–0.12, desligado em blocos de texto.
- Serifs itálicas finas só a partir de 24px.
- Botões retangulares ou em pill, com o blob atrás como decoração.
- Ruído pré-renderizado em tile de 128–256px (5–20 KB).

#### 13.9 Encaixe de marca
**[F]** Wellness, sustentabilidade, hospitalidade, saúde, lifestyle, artesanato, comida, slow living e comércio artesanal (as três páginas do daisyUI). **Ruim [S]:** trading de fintech, cibersegurança e ferramentas dev, com exceção do playful blob em SaaS acessível.

#### 13.10 Antipadrões
**[F]** "Generic leaf decoration" no lugar de plantas e materiais autênticos ([biophilic](https://trends.daisyui.com/trend/biophilic-design/)). A redução a "paleta de cerâmica bege" ([wabi-sabi](https://trends.daisyui.com/trend/wabi-sabi/)). **[S]**:

- Clip-art de folha.
- Grain em tudo.
- Blobs que cortam rostos ou produtos.
- Mais de 1–2 motivos de blob por viewport.
- Bege sobre bege.

#### 13.11 Exemplos e referências
**[F]** (status ao vivo **[NV]**). Da [Colorlib, outubro de 2026](https://colorlib.com/wp/skincare-brand-website-examples/): ahuaskin.co.nz, bodha.com, herbivorebotanicals.com, truebotanicals.com, tataharperskincare.com, saltandstone.com e farmacybeauty.com. Da [Limely](https://www.limely.co.uk/blog/our-top-10-health-wellness-websites): inessawellness.com, yourheights.com, dirteaworld.com e neomwellbeing.com.

---

### 14. Luxury / elegant

**Eixo:** estética primária, muitas vezes sobre uma estrutura minimalista ou suíça. Risco médio e dependente do setor.

#### 14.1 Definição e traços-assinatura
Não há fonte autoritativa que defina "luxury web design" como estilo. As definições disponíveis vêm de blogs de agências. A IIAD (2025) lista as pistas que fazem um site "parecer caro" **[F]** ([IIAD](https://www.iiad.edu.in/the-circle/why-some-websites-just-feel-expensive/)):

- Serifs clássicas (Dior, Rolex), em uma ou duas famílias.
- Títulos finos e espaçados ("quiet luxury" da Bottega Veneta).
- Espaço negativo generoso (Hermès).
- Paleta monocromática (Chanel) ou dark com dourado (Cartier).
- Imagem "film-like" e loops de vídeo ambiente (Burberry).
- Movimento lento, "revealing rather than reacting".
- Nav esparsa.
- CTAs discretos ("Request a Consultation" em vez de "Shop Now").
- Sinais de exclusividade ("Price Upon Request").

A KIJO acrescenta tipo sob medida ou minimalista, espaço em branco "deliberate and confident", rolagem suave e carregamento rápido **[F]** ([KIJO](https://kijo.london/blog/luxury-website-design)).

Traços **[S]**:

1. Display serif ou Didone de alto contraste, ou um sans refinado com tracking largo.
2. O máximo de espaço em branco e o ritmo vertical mais lento do catálogo.
3. Fotografia editorial full-bleed ou filme.
4. Marfim, osso e preto, com metálico opcional.
5. Movimento de 600–1200ms.
6. Labels pequenas em caixa alta com tracking largo e CTAs como link de texto.

#### 14.2 Variantes
**[F]** A IIAD distingue registros: quiet luxury (Bottega), monocromático (Chanel), gradientes suaves com paleta profunda (Rolls-Royce) e dark com dourado (Cartier). A Limely mostra um espectro: neutro calmo (Rêve En Vert), artesania (The Row), collage editorial (Abask), funcional (COS) e atmosférico (DeMellier) ([Limely](https://www.limely.co.uk/blog/top-10-minimalist-luxury-ecommerce-websites)).

| Variante **[S]** | Assinatura | Usar para |
|---|---|---|
| Quiet luxury | marfim e pedra, quase preto, sans refinado ou serif leve, quase sem movimento (The Row, Totême) | moda, couro, marcas minimalistas de alto padrão |
| Heritage maison | Didone ou Garamond, wordmark centralizado, P&B com dourado, capítulos de storytelling (Hermès, Chanel) | joalheria, relógios, champanhe |
| Dark opulent | preto, navy ou verde profundo com dourado ou champanhe, vídeo cinematográfico (Cartier dark) | automotivo, alta joalheria, destilados, imóveis premium |
| Editorial-fashion | grids em collage, serif grande, ritmo de revista (Abask) | concept stores, designers, beleza |
| Hospitality/wellness | paleta quente, serif com sans, paisagem full-bleed, CTA de reserva | hotéis, spas, residências (Aman é arquétipo **[NV]**) |

#### 14.3 Layouts e padrões de página
**[F]** Nav esparsa e conteúdo revelado aos poucos, "like a curated exhibition", com zoom 360° (Gucci) ([IIAD](https://www.iiad.edu.in/the-circle/why-some-websites-just-feel-expensive/)). As grades de produto são "simple" (The Row), "curated, uncluttered" (Totême) e "clear, structured" (COS) ([Limely](https://www.limely.co.uk/blog/top-10-minimalist-luxury-ecommerce-websites)). **[S]**:

- **Grid e texto:** 12 colunas, gap 20–32px, conteúdo até 1440px com heros em 100vw/100svh e textos estreitos de 36–48ch.
- **Hero:** (a) imagem ou vídeo full-bleed com wordmark pequeno e link "Discover", (b) split editorial de 7+4 colunas, ou (c) still de produto centralizado.
- **Nav:** wordmark centralizado; utilidades como texto em caixa alta ("Search", "Bag (2)"); transparente sobre o hero e sólida após o scroll.
- **Produtos:** de 2 a 4 colunas, em 3:4 ou 4:5 sobre `#F2F0EC`, com hover que troca para a segunda imagem e um tile editorial a cada 6–8 produtos.
- **Ritmo:** `clamp(96px, 14vw, 240px)`, o maior do catálogo.
- **Mobile:** `<picture>` com direção de arte.

#### 14.4 Tipografia (OFL)
**[F]** A Cedilla lista 13 Google Fonts OFL para luxo ([Cedilla](https://www.cedilla.studio/blog/free-luxury-fonts)):

- **Playfair Display:** tão usada que perde distinção.
- **EB Garamond.**
- **Cormorant / Cormorant Garamond.**
- **Bodoni Moda:** com uma advertência, "Don't use Bodoni at 12pt — it'll fall apart on screen".
- **Oranienbaum.**
- **Cinzel:** com Tenor Sans ou EB Garamond.
- **Italiana.**
- **Cardo.**
- **Forum:** hotéis e spas.
- **Marcellus.**
- **Tenor Sans.**
- **Della Respira.**

As regras da Cedilla são tracking de wordmark de **+50 a +200** (0.05–0.2em), um peso só (regular ou light) com hierarquia por tamanho e espaçamento, e uma serif com um sans limpo, nunca serif com serif.

**[S]**:

- **Escala:** razão de 1.25–1.333.
- **Corpo:** 16–18px (serif de 18–20px), line-height 1.6–1.75.
- **Display:** line-height 1.0–1.15.
- **Labels:** 11–13px em caixa alta, com 0.12–0.2em.
- **Pesos:** 300/400 e itálico.
- **Pares quiet:** Cormorant Garamond com Jost ou Tenor Sans.
- **Pares heritage:** Bodoni Moda (só a partir de 32px) com Inter ou Jost, ou Cinzel com EB Garamond.
- **Pares editorial:** Playfair Display ou Gilda Display com Work Sans, ou Italiana (só no hero) com Marcellus.
- **Evitar:** Playfair com Montserrat, que virou combinação de template.

#### 14.5 Cor
**[F]** Monocromático (Chanel), gradientes suaves com paletas profundas (Rolls-Royce) e preto com dourado (Cartier) ([IIAD](https://www.iiad.edu.in/the-circle/why-some-websites-just-feel-expensive/)). A Fendi usa fundo branco limpo ([Limely](https://www.limely.co.uk/blog/top-10-minimalist-luxury-ecommerce-websites)). **[S]**, com contrastes estimados a conferir:

| Variante | Tokens | Observações |
|---|---|---|
| Quiet | `--bg:#F7F4EF; --surface:#EDE8E0; --fg:#1A1A1A; --muted:#5E5A55` | |
| Dark opulent | `--bg:#0B0B0C; --fg:#F2EEE6; --muted:#A39E95; --gold:#C9A96E` | dourado ≈8:1 sobre o quase-preto; sobre marfim falha como texto, então use `#8A6D3B` ou só em rules e ícones |

Armadilha clássica: uma legenda "elegante" em `#B5AFA6` sobre `#F7F4EF` fica em cerca de 2:1 e reprova.

#### 14.6 Componentes
**[F]** Imagem "film-like" em vez de packshot simples, vistas 360°, vídeo ambiente e micro-interações refinadas no hover ([IIAD](https://www.iiad.edu.in/the-circle/why-some-websites-just-feel-expensive/)). **[S]**:

- **Botão:** outline de 1px ou preto sólido, radius 0, 48–52px de altura, 12–13px em caixa alta com 0.15em; ou um link sublinhado.
- **Cards:** sem moldura.
- **Hairlines:** 1px ou 0.5px (`scaleY(.5)`), em tom secundário ou dourado.
- **Imagens:** retrato em 3:4 ou 4:5, ou cinematográfico em 21:9, com grade de cor consistente.
- **Navegação:** rótulos de texto no lugar de ícones.

#### 14.7 Efeitos, movimento e configurações
**[F]** Animação lenta, suave e com propósito; fades suaves no scroll (a Apple é citada como referência) ([IIAD](https://www.iiad.edu.in/the-circle/why-some-websites-just-feel-expensive/)). Rolagem suave ([KIJO](https://kijo.london/blog/luxury-website-design)). **[S]**:

```css
:root{--ease-out:cubic-bezier(.22,1,.36,1)}
.lux .img{overflow:hidden}.lux .img img{transition:transform 1.4s var(--ease-out)}.lux .img:hover img{transform:scale(1.04)}
.lux .link{background:linear-gradient(currentColor,currentColor) 0 100%/0 1px no-repeat;transition:background-size .5s var(--ease-out)}
.lux .link:hover,.lux .link:focus-visible{background-size:100% 1px}
```

Hovers de 300–500ms, reveals de 800–1200ms e zoom de 1.03–1.05 ao longo de 1.2–1.6s. O vídeo de hero usa `<video autoplay muted loop playsinline poster>` com botão de pausa visível e não toca sob `reduce`. Bibliotecas de smooth scroll só entram se forem desligadas em reduced motion.

#### 14.8 Riscos de acessibilidade e performance
**[F]** Bodoni se desfaz em tamanhos pequenos ([Cedilla](https://www.cedilla.studio/blog/free-luxury-fonts)). Sites de luxo devem carregar "instantaneously" ([KIJO](https://kijo.london/blog/luxury-website-design)). **[S]**:

- Nenhum peso abaixo de 300 no corpo.
- Serif de corpo com pelo menos 18px.
- Labels com pelo menos 12px e tracking de no máximo 0.2em, para continuar compatível com a 1.4.12.
- Scrim `linear-gradient(to top, rgba(0,0,0,.55), transparent 60%)` sobre vídeo.
- Conteúdo "price upon request" alcançável por teclado.
- Vídeo de hero com no máximo 2–4 MB e `preload="none"` ou `metadata`.

#### 14.9 Encaixe de marca
**Bom [S]:** moda, couro, joalheria e relógios, perfumaria e beleza premium, hotéis boutique e spas, alta gastronomia, imóveis premium, automotivo e marcas artesanais. **Ruim [S]:** varejo de desconto, SaaS utilitário, serviços públicos e marketplaces com muitos SKUs e filtragem densa.

#### 14.10 Antipadrões
**[F]** "Shop Now" no lugar de CTAs de concierge ([IIAD](https://www.iiad.edu.in/the-circle/why-some-websites-just-feel-expensive/)). Playfair usada em excesso e serif com serif ([Cedilla](https://www.cedilla.studio/blog/free-luxury-fonts)). **[S]**:

- Gradiente dourado com script e preto, que vira "template de luxo" barato.
- Banners de urgência, pop-ups e contagens regressivas.
- Mega-menus.
- Fotografia inconsistente.
- Som automático.
- Easings rápidos e elásticos.

#### 14.11 Exemplos e referências
**[F]** (status ao vivo **[NV]**). Da [Limely 2026](https://www.limely.co.uk/blog/top-10-minimalist-luxury-ecommerce-websites): therow.com, aesop.com, toteme.com, chanel.com, fendi.com, abask.com, demellierlondon.com, reve-en-vert.com, cos.com e arket.com. Da [IIAD](https://www.iiad.edu.in/the-circle/why-some-websites-just-feel-expensive/): hermes.com. Da [KIJO](https://kijo.london/blog/luxury-website-design): espalifeatcorinthia.com e crownpavilions.com. Jacquemus e Aman foram citados de memória **[NV]**.

---

### 15. Dark / tech

**Eixo:** metade modo de cor, metade estética. O catálogo deve separar `color_mode: dark` (disponível para qualquer estética) da estética "Tech/futurist". Risco médio, e o principal problema é contraste.

#### 15.1 Definição e traços-assinatura
O visual dark SaaS é chamado de "Linear style" ou "Linear design", por causa da ferramenta Linear. Seu conteúdo é "straightforward and sequential, highlighting logical progression" **[F]** ([LogRocket](https://blog.logrocket.com/ux-design/linear-design)). Os traços listados pela fonte: modo dark (o autor admite "no real evidence it's better"), tipo forte, gradientes complexos, glassmorphism, monocromia de alto contraste, sombras suaves e linearidade estrita.

A fonte também registra como as referências mudaram. A Linear passou do monocromático azul (2024) para o preto e branco (2025). A Raycast trocou o gradiente por "noisy abstract visuals". O site do GitHub em 2025 foi criticado pelo excesso de glass. A recomendação de fundo é a cor da marca com 1–10% de luminosidade, porque o preto puro é "too black". A crítica central é que o estilo está saturado e os SaaS ficam todos parecidos **[F]** (mesma fonte).

O redesign da Linear (março de 2024) **[F]** ([Linear](https://linear.app/now/how-we-redesigned-the-linear-ui)):

- Trocou HSL por um gerador de temas em LCH, "perceptually uniform".
- Reduziu cada tema a 3 variáveis (base, acento e contraste) em vez de 98.
- Ganhou uma variável de contraste para temas de altíssimo contraste.
- Constrói a elevação com opacidades de preto e branco.
- Usa Inter Display nos títulos e Inter no resto.
- Tem theme-color `#08090a`.

#### 15.2 Variantes
Nenhuma fonte nomeia subvariantes **[S]**.

| Variante | Assinatura | Usar para |
|---|---|---|
| Precision dark (Linear/Vercel) | quase preto tingido pela marca, escada de cinzas, um acento, hairlines de 6–10% de branco, brilho radial no hero, screenshot em "janela" | dev tools, B2B SaaS, infra de IA, fintech |
| Cyber / neon / terminal | lime, ciano e magenta sobre preto; mono; scanlines; hero de prompt; glitch | segurança, crypto, gaming, hackathons |
| AI-lab soft dark / cinematic | carvão quente, display serif ou grotesk, orbs e auroras, imagem abstrata com ruído | empresas de modelos e laboratórios de IA |
| Luxury dark | ver o cartão 14, "Dark opulent" | bens físicos premium |

Regra de escolha **[S]**: ferramenta de uso diário pede precision. Público que se identifica com cultura hacker pede cyber. IA vendendo visão pede cinematic.

#### 15.3 Layouts e padrões de página
**[F]** CTAs mínimos e rolagem unidimensional ([LogRocket](https://blog.logrocket.com/ux-design/linear-design)). Estrutura **[S]**:

- **Página:** coluna central de 1100–1280px com hero (headline, sub, 1–2 CTAs e produto emoldurado), faixa de logos, bento, seções de aprofundamento, depoimentos ou métricas, pricing, CTA final e footer multicoluna.
- **Nav:** sticky de 56–64px, com `backdrop-filter: blur(12px)` sobre `rgb(8 9 10 / .7)` e borda inferior de 8% de branco.
- **Bento:** `repeat(6,1fr)`, virando 1 coluna abaixo de cerca de 720px.
- **Janela de produto:** radius de 12–16px, borda de 1px e brilho por trás.

#### 15.4 Tipografia (OFL)
**[F]** Inter Display e Inter na Linear ([Linear](https://linear.app/now/how-we-redesigned-the-linear-ui)). **[S]**:

- **Outras opções:** Geist e Geist Mono **[LIC?]**, Space Grotesk, IBM Plex Sans/Mono e JetBrains Mono.
- **Mono:** só em código, labels, eyebrows e métricas.
- **Títulos:** 48–80px com −0.02 a −0.04em.

#### 15.5 Cor
**[F]** Theme-color `#08090a`, a lógica de LCH e a marca com 1–10% de luminosidade ([Linear](https://linear.app/now/how-we-redesigned-the-linear-ui); [LogRocket](https://blog.logrocket.com/ux-design/linear-design)). Tokens **[S]**:

- **Fundos:** `--bg:#08090a; --surface:#111214; --surface-2:#18191c`.
- **Borda:** `--border:rgb(255 255 255/.08)`.
- **Texto:** `--text:#f2f3f5; --text-2:#a1a3a8`, com o texto secundário verificado em 4.5:1.
- **Acento:** um só, em OKLCH ou LCH.
- **Evitar** branco puro sobre preto puro em textos longos (halação); use off-white entre `#e6e6e6` e `#f2f2f2`.

#### 15.6 Componentes
**[S]**:

```css
/* fundo de grid com fade */
background-image:linear-gradient(rgb(255 255 255/.05) 1px,transparent 1px),linear-gradient(90deg,rgb(255 255 255/.05) 1px,transparent 1px);
background-size:64px 64px;mask-image:radial-gradient(ellipse at 50% 0%,#000 30%,transparent 75%);
/* borda de gradiente sem markup extra */
border:1px solid transparent;
background:linear-gradient(var(--surface),var(--surface)) padding-box,linear-gradient(135deg,rgb(255 255 255/.25),rgb(255 255 255/.02)) border-box;
```

Outros elementos:

- **Dot grid:** `radial-gradient(rgb(255 255 255/.08) 1px, transparent 1px) 0 0/24px 24px`.
- **Brilho do hero:** `radial-gradient(closest-side, oklch(70% .15 270 / .35), transparent)` em cerca de 800×400px com `blur(40px)`.
- **Spotlight no cursor:** com rAF.
- **Ruído:** de 3–6% para evitar banding.

#### 15.7 Efeitos, movimento e configurações
**[S]**:

- Hover de 150–300ms em ease-out.
- Reveals com `view()`, como no cartão 17.
- Borda animada com `@property --a` e `conic-gradient(from var(--a), …)`, que repinta a cada frame e não fica só no compositor; use em 1–2 elementos no máximo e desligue em reduced motion.

#### 15.8 Riscos de acessibilidade e performance
**[S]** O risco principal é o cinza secundário sobre o quase preto ficar abaixo de 4.5:1. Outros riscos:

- Ausência de light mode e de `prefers-color-scheme`.
- Screenshots de hero sem `width`/`height`, que causam CLS.
- Vários brilhos concorrentes.

Nenhuma fonte mediu o contraste de sites dark reais.

#### 15.9 Encaixe de marca
**Bom [S]:** dev tools, infra de IA/ML, SaaS, crypto/DeFi, cibersegurança, hardware gamer e ferramentas de áudio e criação. **Ruim [S]:** infantil, alimentação e hospitalidade (exceto luxury dark), saúde voltada ao paciente, governo, PMEs locais com público mais velho e sites de leitura longa.

#### 15.10 Antipadrões
**[F]** Copiar o template inteiro, que gera o problema de "todo SaaS igual", e glass em tudo, como na crítica ao GitHub em 2025 ([LogRocket](https://blog.logrocket.com/ux-design/linear-design)). **[S]**:

- Cinza de baixo contraste.
- Vários acentos com glow.
- Bordas animadas em todos os cards.
- Nenhum elemento distintivo. É preciso ao menos um: fundo tingido pela marca, tipo incomum ou visual próprio.

#### 15.11 Exemplos e referências
**[NV]**: linear.app (via o post da Linear), vercel.com, raycast.com (via a LogRocket), resend.com, cursor.com e supabase.com. Luxury dark: páginas de produto do rolex.com. Críticas não buscadas: [Anthony Hobday (2023)](https://anthonyhobday.com/blog/20230119.html) e [UX Collective/Bootcamp](https://bootcamp.uxdesign.cc/the-rise-of-linear-style-design-origins-trends-and-techniques-4fd96aab7646).

---

### 16. Kinetic typography

**Eixo:** padrão de movimento, aplicado a uma estética (Swiss, Editorial, Maximalist, Brutalist ou Dark). Risco de movimento alto.

#### 16.1 Definição e traços-assinatura
Tipografia cinética é "animated text where type is not displayed statically but brought to life through movement, transformation, or temporal sequencing". O próprio tipo é o objeto animado, o que separa a técnica de um simples fade-in **[F]** ([StudioMeyer](https://studiomeyer.io/en/blog/kinetische-typografie)). A fonte nomeia as técnicas: texto reativo ao scroll, split-text por linha, palavra ou caractere, morphing, animação de eixos de fontes variáveis e reveals por máscara ou clip. As fontes variáveis permitem animar peso e largura em hover, scroll e viewport, além de eixos customizados **[F]** ([FontLab](https://blog.fontlab.com/2026/03/10/variable-fonts-in-motion-and-ui/)). A Figma recomenda texto animado no scroll **[F]** ([Figma](https://www.figma.com/resource-library/web-design-trends/)).

Traços **[S]**:

1. Display enorme (10–20vw) como visual principal.
2. Poucas palavras.
3. Contraste forte.
4. Ritmo por stagger e repetição.
5. Grotesks ou condensadas.
6. Movimento que carrega significado.

#### 16.2 Variantes
Nomes **[S]**, construídos a partir da lista de técnicas da StudioMeyer.

| Variante | Assinatura | Usar para |
|---|---|---|
| Marquee/ticker | palavras enormes em loop, às vezes duas fileiras opostas ou velocidade ligada ao scroll | energia de marca, line-ups de eventos, agências, moda |
| Scroll-reactive | palavras que escalam, deslizam ou acendem com o scroll; headline que encolhe até virar nav | manifestos, heros |
| Variable-font axis | peso, largura ou eixos que "respiram" no hover, na proximidade do cursor ou no scroll | foundries, estúdios, música |
| Split-text reveal | linhas ou palavras subindo de uma máscara | a opção mais "corporativa": heros SaaS, portfólios, editorial |
| 3D/perspective (opcional) | letras girando, texto em cilindro | uso pontual |

#### 16.3 Layouts e padrões de página
**[S]**:

- Hero de tipo em viewport inteiro (12–18vw).
- Faixas de marquee como divisores.
- Seção de manifesto com palavras que acendem no scroll.
- Índice com títulos de linha reativos ao hover e uma imagem que segue o cursor.
- Wordmark gigante no footer.
- **Mobile:** `clamp(2.5rem, 12vw, 9rem)`, sem efeitos por caractere, no máximo um marquee e nada que dependa de hover.

#### 16.4 Tipografia (OFL)
Fontes variáveis do Google Fonts **[S][LIC?]**:

- Roboto Flex (wdth, wght, opsz, GRAD, XTRA).
- Recursive (MONO, CASL, slnt).
- Anybody (wdth 50–150).
- Big Shoulders Display.
- Fraunces (SOFT, WONK).
- Archivo (wdth).
- Bricolage Grotesque.
- Inter, Space Grotesk e Unbounded.

Os ícones comerciais do estilo (Dinamo, Pangram) não são OFL. **[F]** "A variable font is not automatically smaller": faça subset com glyphhanger ou pyftsubset ([StudioMeyer](https://studiomeyer.io/en/blog/kinetische-typografie)).

#### 16.5 Cor
**[S]** Contraste forte, em preto e branco ou com uma cor viva. Na frase que acende no scroll, o estado apagado precisa atender ao contraste ou ser tratado como texto decorativo duplicado. **[F]** Mantenha o contraste durante a animação ([StudioMeyer](https://studiomeyer.io/en/blog/kinetische-typografie)).

#### 16.6 Componentes
**[F]** O elemento `<marquee>` está proibido pela regra axe "marquee elements must not be used" ([Rocket Validator](https://rocketvalidator.com/accessibility-validation/marquee)).

```html
<!-- [S] marquee sem biblioteca -->
<div class="marquee" aria-label="Brand · Brand · Brand"><div class="track" aria-hidden="true"><span>…</span><span>…</span></div></div>
```
```css
.track{display:flex;width:max-content;animation:m 30s linear infinite}@keyframes m{to{transform:translateX(-50%)}}
.marquee:hover .track,.marquee.paused .track{animation-play-state:paused}
@media (prefers-reduced-motion:reduce){.track{animation:none}}
```

**[S]**:

- Velocidade de 40–80px/s.
- Fade nas bordas com `mask-image: linear-gradient(90deg, transparent, #000 10%, #000 90%, transparent)`.
- Botão de pausa visível, obrigatório pela 2.2.2.
- No split-text, `aria-label` no pai com spans `aria-hidden` e `Intl.Segmenter` para grafemas.

#### 16.7 Efeitos, movimento e configurações
**[F]** Números da StudioMeyer ([StudioMeyer](https://studiomeyer.io/en/blog/kinetische-typografie)):

- Stagger de **30–50ms por caractere** soa fluido; **100ms ou mais** soa dramático.
- Split por palavra serve para headlines de 3–8 palavras; split por caractere só para textos curtos.
- No máximo **2–3 elementos com split por página**.
- Anime só `transform` e `opacity`, nunca `font-size`, `width` ou `margin`.
- Pause o que estiver fora do viewport e use rAF.

```css
/* [S] split por palavra */
.w{display:inline-block;overflow:clip}
.w>span{display:inline-block;transform:translateY(110%);transition:transform .8s cubic-bezier(.2,.7,.2,1) calc(var(--i)*40ms)}
.in .w>span{transform:none}
/* [S] frase que "acende" no scroll — só cor, logo fora da definição de "motion" da WCAG */
.word{animation:lit linear both;animation-timeline:view();animation-range:cover 30% cover 50%}
```

As fontes variáveis usam `font-weight`, `font-stretch` e `font-style: oblique` para eixos registrados e `font-variation-settings` só para os customizados, com `transition: font-weight .4s`. Cada frame refaz o layout do texto, então limite o efeito a uma headline com largura reservada **[S]**. O suporte a `view()` está no cartão 17 **[SUP?]**.

#### 16.8 Riscos de acessibilidade e performance
**[F]** Sob reduced motion, volte para fades ou texto estático. Evite loops infinitos e autoplay, deixe pausar, não pisque acima de 3 Hz e garanta texto visível sem JS ([StudioMeyer](https://studiomeyer.io/en/blog/kinetische-typografie)). Mudanças de cor e opacidade não contam como "motion animation" na 2.3.3 ([W3C](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html)). **[S]** O split por caractere quebra leitores de tela e ligaduras, e spans injetados que mudam a quebra de linha depois do primeiro paint causam CLS.

#### 16.9 Encaixe de marca
**Bom [S]:** agências e estúdios, moda, música, festivais, esporte, foundries, DTC ousado e microsites de campanha. **Ruim [S]:** dashboards bancários, saúde, jurídico, leitura longa, serviços públicos e qualquer página em que o texto precise ser lido enquanto se move.

#### 16.10 Antipadrões
**[S]**:

- Animar o corpo do texto.
- Fazer split em todos os títulos.
- Marquee sem pausa.
- Texto crítico em `opacity:0` até o JS rodar.
- Reveals que se repetem a cada scroll.
- Vários loops ao mesmo tempo.
- Animar `font-size`.

#### 16.11 Exemplos e referências
A StudioMeyer cita Stripe pela animação sutil de texto e menciona páginas de produto da Apple e foundries como categorias. Candidatos **[NV]**: [Typewolf Site of the Day](https://www.typewolf.com/site-of-the-day), [coleção de tipografia da Awwwards](https://www.awwwards.com/websites/typography/), abcdinamo.com, pangrampangram.com e displaay.net.

---

### 17. Immersive / 3D scroll storytelling

**Eixo:** padrão de movimento e mídia, aplicado a uma estética (Luxury, Dark/tech, Editorial). Risco de movimento e performance alto.

#### 17.1 Definição e traços-assinatura
Sites imersivos transformam a barra de rolagem numa linha do tempo **[S]**. A Codrops descreve seções sticky de tamanhos diferentes criando empilhamento ou colapso, cartas empilhadas e animação das seções enquanto saem do viewport. A demo usa `position: sticky` com JS, e o artigo diz que as animações CSS guiadas por scroll "will very likely be able to replace them" **[F]** ([Codrops](https://tympanus.net/codrops/2024/01/31/on-scroll-animation-ideas-for-sticky-sections)).

A evidência mais importante é o estudo da NN/g sobre scrolljacking (2023) **[F]** ([NN/g](https://www.nngroup.com/articles/scrolljacking-101/)):

- A maioria dos participantes ficou ao menos levemente desorientada.
- Jacks longos foram lidos como bug.
- Movimento horizontal disparado por gesto vertical confundiu.
- Texto dentro do scrolljack causou os piores problemas.
- No mobile é pior.
- "Falsos finais" fizeram usuários achar que a página tinha acabado.

O scrolljacking pode ser aceitável se agregar valor funcional, for curto, ficar abaixo da dobra e for testado. A NN/g diz que "in most cases, not worth adding on mobile".

#### 17.2 Variantes
A W3C cita "parallax with a global off switch" como exemplo da 2.3.3 **[F]** ([W3C](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html)). Nomes **[S]**:

| Variante | Assinatura | Usar para |
|---|---|---|
| Parallax layers | camadas em velocidades diferentes; o custo mais baixo; totalmente removível | viagem, outdoor, hospitalidade, portfólios |
| Sticky scrollytelling | seção alta (300–500vh) com palco `sticky; top:0; height:100vh` e "passos" de texto em fluxo normal; nasceu no jornalismo de dados | explicadores de produto, relatórios anuais, ONGs, "como funciona"; **o melhor perfil de acessibilidade** |
| Scroll-scrubbed media / pseudo-3D | sequência de imagens em canvas ou vídeo controlado pelo scroll; pilhas de cards em CSS 3D | hardware, automotivo, lançamentos |
| WebGL worlds | Three.js/OGL, shaders, câmera em trajeto, com Lenis e GSAP | campanhas carro-chefe, estúdios, luxo, games; **fora do alvo "sem bibliotecas"** |

#### 17.3 Layouts e padrões de página
**[S]**:

- Hero fixado em tela cheia que diminui de escala e se integra à página.
- Capítulos com indicador de progresso.
- Cenas fixadas alternando com texto em fluxo normal, como a NN/g recomenda.
- Galeria horizontal curta com indicação visível de progresso.
- Máscara que se expande até full-bleed.
- CTA final em fluxo normal.
- Nav sticky e links "pular para capítulo" como rota de saída.
- **Mobile:** pins cerca de 50% menores, pôster no lugar de WebGL, horizontal virando `scroll-snap` nativo e `100svh`/`100dvh` no lugar de `100vh`.

#### 17.4 Tipografia (OFL)
Não há fonte específica. A tipografia vem da estética primária **[S]**. A regra que importa: manter o texto de leitura fora das cenas fixadas e animadas, ou duplicá-lo em fluxo normal, porque texto dentro de scrolljacks causou os problemas mais graves **[F]** ([NN/g](https://www.nngroup.com/articles/scrolljacking-101/)).

#### 17.5 Cor
Também vem da estética primária **[S]**. Texto sobre mídia em movimento precisa de scrim ou de placa sólida, porque o contraste muda a cada frame.

#### 17.6 Componentes
**[S]**: indicador de progresso (barra `scroll()` ou pontos de capítulo), skip links por capítulo com `scroll-margin-top`, pausa para vídeo em loop (2.2.2) e pôster estático para reduced motion.

#### 17.7 Efeitos, movimento e configurações
**[F]** Uma Scroll Progress Timeline mapeia a rolagem para 0–100%, e uma View Progress Timeline mapeia a passagem de um elemento pelo scroller, podendo "run off the main thread". Recursos disponíveis ([Chrome for Developers](https://developer.chrome.com/docs/css-ui/scroll-driven-animations)):

- Timelines nomeadas: `scroll-timeline: --name inline`, `view-timeline-name`, e `timeline-scope` no pai.
- Ranges: `cover`, `contain`, `entry`, `exit`, `entry-crossing` e `exit-crossing`.
- APIs JS: `ScrollTimeline` e `ViewTimeline`.

Suporte, segundo uma fonte secundária ([BuildMVPFast](https://www.buildmvpfast.com/blog/css-scroll-driven-animations-replace-js-2026)) **[SUP?]**:

- Chrome/Edge 115 (julho de 2023), confirmado pelo Chrome.
- Safari 26 (setembro de 2025), com versão threaded na 26.4 e correções na 26.5.
- Firefox ainda atrás de `layout.css.scroll-driven-animations.enabled` na versão 152 (junho de 2026), prioridade da Interop 2026.
- Cerca de 82.6% global no caniuse, sem status Baseline.

A mesma fonte recomenda que o estado final seja o padrão e que a animação só se aplique dentro de `@media (prefers-reduced-motion: no-preference) { @supports (animation-timeline: view()) {…} }`.

```html
<!-- [S] cena sticky -->
<section class="scene" style="height:400vh"><div class="stage" style="position:sticky;top:0;height:100svh;overflow:clip">…</div></section>
```

Técnicas **[S]**:

- **Progresso só com CSS:** `.scene{view-timeline:--scene block}` com `animation-range: contain 0% contain 100%`.
- **Fallback em JS:** `p = clamp(0,1,-rect.top/(rect.height-innerHeight))` em rAF, gravado em `--p`.
- **Sticky:** `overflow: clip` e não `hidden` nos ancestrais, porque `hidden` quebra o sticky.
- **Passos com IntersectionObserver:** `rootMargin:'-50% 0px -50% 0px'` e `stage.dataset.step = n`, robusto e acessível.
- **Parallax em CSS:** profundidade de 0.1–0.6.
- **3D em CSS:** `perspective` de 800–1200px soa natural, 300–600px é dramático e acima de 2000px é quase plano.
- **Pilha de cards:** `top: calc(10vh + var(--i)*24px)`, com escala de 0.9–0.95.
- **Máscara:** de `clip-path: inset(20% 30% round 24px)` para `inset(0)`.
- **Sequência de imagens:** 60–150 frames WebP, com teto de 1–2 MB por 100 frames no mobile.

| Biblioteca | Uso típico | Alternativa vanilla **[S]** |
|---|---|---|
| GSAP + ScrollTrigger/SplitText | timelines fixadas em várias etapas, scrub com easing | `view-timeline` + `timeline-scope`, IntersectionObserver com transições, padrão `--p` em rAF |
| Lenis | rolagem inercial, sincronia com WebGL | rolagem nativa e `scroll-behavior:smooth` só em âncoras; Lenis altera a rolagem nativa, que é o risco apontado pela NN/g |
| Three.js / OGL | modelos 3D reais, shaders | CSS 3D, sequências pré-renderizadas, vídeo, renders estáticos |

#### 17.8 Riscos de acessibilidade e performance
**[F]** Reações vestibulares incluem tontura, náusea e dor de cabeça, e "severe reactions may require bed rest". A rolagem controlada pelo usuário é permitida, mas o movimento não essencial adicionado a ela deve poder ser evitado ([W3C 2.3.3](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html)). Na 2.2.2, "começa automaticamente" inclui "scrolling an element into view" ([W3C 2.2.2](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)). **[S]**:

- Nunca alterar a velocidade ou a direção da rolagem nativa nem usar `preventDefault` no wheel.
- O que estiver fixado não pode prender o foco.
- `content-visibility:auto` com `contain-intrinsic-size`.
- Handlers de pointermove mínimos para proteger o INP.
- Nenhuma tarefa de main thread acima de 50ms.

#### 17.9 Encaixe de marca
**Bom [S]:** lançamentos de produto, hardware, automotivo, luxo, campanhas, relatórios anuais e de impacto, museus, jornalismo de dados e portfólios de estúdio. **Ruim [S]:** listagens de e-commerce, pricing e docs de SaaS, serviços locais, qualquer tarefa orientada a objetivo (a NN/g observa que esses usuários se irritam e saem) e páginas de SEO.

#### 17.10 Antipadrões
**[S]**, somados à NN/g:

- Sequestrar o wheel ou o toque.
- Snap travando todas as seções.
- Pins de mais de 3–4 viewports sem indicação de progresso.
- Texto importante dentro da animação.
- Hero 3D que baixa 5–10 MB antes do primeiro paint.
- Nenhum fallback.
- Scrollbar escondida.
- Busca na página e âncoras quebradas.

#### 17.11 Exemplos e referências
**[NV]**: igloo.inc (WebGL; teria sido Site of the Year da Awwwards em 2024, não verificado), lusion.co, bruno-simon.com, apple.com/airpods-pro (scroll-scrubbed), landonorris.com e pudding.cool (scrollytelling). Coleções de scrollytelling da Awwwards e o case Aten7 da Immersive Garden aparecem só em resultados de busca. Os vencedores do SOTY de 2024/2025 não foram verificados.

---

### 18. Collage / scrapbook

**Eixo:** estética primária e também técnica dentro do Maximalismo. Pode entrar como acento num shell editorial. Risco alto fora das categorias criativas.

#### 18.1 Definição e traços-assinatura
A Designmodo (publicado em 2013, atualizado em fevereiro de 2026) define o estilo scrapbook como a imitação do scrapbooking físico, com camadas de texturas, imagens e elementos decorativos num visual multicamada. Chama o estilo de "attention-grabbing" e difícil de executar **[F]** ([Designmodo](https://designmodo.com/scrapbook-website-design/)). Traços apontados pela Designmodo:

- Texturas de papel.
- Fundos irregulares.
- Camadas sobrepostas com separação clara.
- Sombras limpas.
- Lettering à mão e rabiscos.
- Etiquetas, selos e molduras envelhecidas.
- Recortes com cantos dobrados.
- Menus em forma de etiqueta.

"Scrapbooking is all about layering" **[F]** ([Alpha Efficiency](https://alphaefficiency.com/scrapbook-style-web-design)). A Figma inclui no estilo "sticker graphics, torn textures, cutout photos, and hand-drawn fonts" **[F]** ([Figma](https://www.figma.com/resource-library/web-design-trends/)). A KOTA o chama de "controlled chaos", com tipo, imagem, fita e grampos como elementos de composição, mais perto de pôsteres de protesto e zines, e aceitável "provided the infrastructure stays calm" **[F]** ([KOTA](https://kota.co.uk/blog/branding-inspiration-brand-design-trends-for-2026)). Teste de reconhecimento **[S]**: bordas e textura de papel visíveis, rotação de ±1–8°, fita ou stickers, recortes com sombra, toques de letra à mão e elementos invadindo os limites das seções.

#### 18.2 Variantes
**[F]** A Alpha Efficiency fala em três modos de produção: tradicional (materiais físicos), digital (Figma/Canva) e híbrido. O post do Medium descreve um "hybrid style" com cantoneiras sobre layout limpo ([Medium](https://shariqkhan74.medium.com/scrapbook-layering-in-website-design-trends-techniques-and-best-practices-18f19b5a3bcd)). A KOTA liga o collage ao revival dos zines e à textura riso, com desregistro e sobreimpressão.

| Variante **[S]** | Assinatura | Usar para |
|---|---|---|
| Analog scrapbook | papel kraft ou creme, washi tape, polaroids, letra à mão, grampos | infantil, família, padarias, artesanato, casamentos, blogs |
| Digital/editorial collage | fundo limpo, recortes sem fundo, formas chapadas, halftone (layout tipo Ghia, segundo a KOTA) | bebidas e beleza DTC, campanhas, portfólios |
| Punk/zine | grain de fotocópia, letras de "carta de resgate", bordas rasgadas, P&B com uma cor | música, eventos, bares, streetwear, ativismo |
| Riso/print | 2–3 tintas spot, `mix-blend-mode: multiply`, offsets de desregistro | estúdios, editoras, ilustradores |

#### 18.3 Layouts e padrões de página
**[F]** Menus em forma de etiqueta. No exemplo Putzengel, cada seção fica em sua própria camada para manter a clareza ([Designmodo](https://designmodo.com/scrapbook-website-design/)). **[S]**:

- **Grid:** 12 colunas com `grid-template-areas`; as peças ocupam células sobrepostas com `z-index` explícito e rotação via `--r`.
- **Hero:** headline central num cartão de papel cercado por 3–7 recortes e stickers. No DOM, a ordem é headline, CTA e depois as decorações em `aria-hidden`.
- **Produtos:** grade de polaroids com rotações alternadas (−2°, 1.5°, −1°, 2.5°) que se endireitam e sobem no hover.
- **Mobile:** uma ou duas sobreposições, rotação de ±1–2° (ou 0 em cards com texto) e alguns stickers ocultos abaixo de 600px.

#### 18.4 Tipografia (OFL)
**[F]** Fontes manuscritas ou retrô usadas como elemento de design, em títulos e citações ([Alpha Efficiency](https://alphaefficiency.com/scrapbook-style-web-design); [Medium](https://shariqkhan74.medium.com/scrapbook-layering-in-website-design-trends-techniques-and-best-practices-18f19b5a3bcd)). **[S]**:

- **Estrutura:** Archivo Black, Anton ou DM Serif Display.
- **Corpo:** Inter ou Work Sans.
- **Acentos manuscritos:** Caveat, Permanent Marker ou Gochi Hand.
- **Máquina de escrever:** Special Elite ou Courier Prime.
- **UI amigável:** Rubik ou Bricolage Grotesque.
- **Regras:** manuscrita só a partir de 1.25rem e em frases de até 8 palavras; letras de "carta de resgate" só em títulos decorativos, com um único nome acessível (texto real com `aria-label`, ou SVG com `<title>`).

#### 18.5 Cor
**[F]** O SOTD "Collage" da Awwwards (2017, prática antiga) usava apenas `#000` e `#FFF`, então collage não precisa ser colorido ([Awwwards](https://www.awwwards.com/sites/collage)). **[S]**:

- **Analog:** kraft `#C8A97E` só como fundo, creme `#FFF8E7`, fita `#F4E3A1` a cerca de 70%, vermelho de marcador `#D7263D` e tinta `#1E1E1E`.
- **Riso:** rosa flúor `#FF48B0`, azul `#0078BF` e amarelo `#FFE800` em multiply sobre `#FBF8F1`.

O texto fica sempre em cartões creme.

#### 18.6 Componentes
**[F]** Técnicas de papel em CSS (dev.to, 2021) ([dev.to](https://dev.to/s_aitchison/3-experiments-with-css-paper-effects-2o56)):

- A dobra é um `::after` com dois gradientes lineares.
- A fita é semitransparente (`opacity:.5`), com borda pontilhada nas pontas para parecer serrilhada.
- O alfinete é feito de gradientes.
- O papel de destacar usa `skew`.
- Os links ficam numa lista semântica, com `rem` para escalar.
- A autora não resolveu as bordas rasgadas.

Cantoneiras ([Medium](https://shariqkhan74.medium.com/scrapbook-layering-in-website-design-trends-techniques-and-best-practices-18f19b5a3bcd)) e fita com grampos ([KOTA](https://kota.co.uk/blog/branding-inspiration-brand-design-trends-for-2026)) completam o vocabulário. **[S]**:

- **Fita:** `::before` de 90×28px, `rgb(244 227 161/.7)` com `rotate:-4deg` e pontas em zigue-zague via `clip-path`.
- **Polaroid:** moldura branca com padding de 12px e 40px embaixo, sombra `0 1px 2px rgb(0 0 0/.15), 0 8px 20px rgb(0 0 0/.12)`.
- **Sticker:** contorno branco de 4–6px e hover em `scale(1.06) rotate(-3deg)`.
- **Borda rasgada:** `clip-path: polygon()` com 20–40 pontos, ou `mask-image`, reutilizada.
- **Doodles:** SVG com `stroke-dashoffset`, já desenhados sob reduced motion.
- **Recorte:** WebP/AVIF com alpha, `drop-shadow(0 6px 10px rgb(0 0 0/.25))` e contorno via `feMorphology dilate`.

#### 18.7 Efeitos, movimento e configurações
**[F]** O SOTD de 2017 usava WebGL, PixiJS, GSAP e jQuery, com notas de 8.00 em Animations e 7.38 em Accessibility no Dev Award. É prática antiga e desnecessária para um build estático ([Awwwards](https://www.awwwards.com/sites/collage)).

```css
/* [S] */
.collage{display:grid;grid-template-columns:repeat(12,1fr);grid-auto-rows:minmax(4rem,auto)}
.piece{grid-column:var(--c);grid-row:var(--rw);rotate:var(--r,0deg);z-index:var(--z,1);transition:rotate .3s,translate .3s}
.piece:hover,.piece:focus-within{rotate:0deg;translate:0 -4px}
@media (max-width:600px){.piece{grid-column:1/-1;grid-row:auto;rotate:calc(var(--r,0deg)*.3)}}
```

Outras técnicas **[S]**:

- **Borda áspera:** `feTurbulence baseFrequency="0.04" numOctaves="2"` alimentando um `feDisplacementMap scale="6–12"`, aplicado ao fundo do cartão e nunca ao texto.
- **Riso:** duas cópias em multiply, a segunda com `translate(2px,-1px)`.
- **Halftone:** `radial-gradient(circle,#000 1px,transparent 1.5px) 0 0/6px 6px`.
- **Grain:** opacidade de 0.10–0.18.

#### 18.8 Riscos de acessibilidade e performance
**[F]** As fontes de tendência não dão orientação de acessibilidade ([Alpha Efficiency](https://alphaefficiency.com/scrapbook-style-web-design)). Um scrapbook mal organizado "will look messy and heavy" ([Designmodo](https://designmodo.com/scrapbook-website-design/)). As sobreposições e as barras sticky podem violar a 2.4.11, e elementos rotacionados que transbordam violam a 1.4.10 ([W3C 2.4.11](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html); [W3C 1.4.10](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)). **[S]**:

- Rotação de no máximo ±3° em elementos com mais de algumas palavras; nunca rotacionar corpo de texto ou formulários.
- Testar zoom a 200% e 400%.
- Elevar o `z-index` no `:focus-within`.
- Decorações com `aria-hidden` e `alt=""`.
- Stickers com significado ("Novo", "−20%") também como texto real.
- Evitar `order` e `grid-auto-flow: dense`.
- Recortes em WebP/AVIF com alpha, nunca PNGs de vários MB.
- `aspect-ratio` reservado.

#### 18.9 Encaixe de marca
**[F]** Moda e beleza, agências criativas, artistas e músicos, marcas DIY, alimentos e bebidas, marcas retrô ([Alpha Efficiency](https://alphaefficiency.com/scrapbook-style-web-design)). Boutiques, blogs pessoais e eventos ([Medium](https://shariqkhan74.medium.com/scrapbook-layering-in-website-design-trends-techniques-and-best-practices-18f19b5a3bcd)). Lifestyle e portfólios ([Figma](https://www.figma.com/resource-library/web-design-trends/)). **[S]**:

| Encaixe | Setores |
|---|---|
| Bom | padarias e cafés, artesanato e produtos feitos à mão (como uma marca de bolsas artesanais), infantil e família, música e eventos, bares, zines, ilustradores, beleza Gen-Z, bebidas sem álcool |
| Com cuidado | agências e portfólios (podem parecer amadores) |
| Ruim | finanças, jurídico, saúde, B2B SaaS, governo |

#### 18.10 Antipadrões
**[S]**:

- Tudo rotacionado, o que achata a hierarquia.
- Corpo de texto sobre textura.
- Stickers de clip-art genéricos.
- Collage de desktop encolhido até ficar ilegível.
- Decoração escondendo CTA ou preço.

#### 18.11 Exemplos e referências
Não foi possível verificar 4–6 sites de collage *ao vivo e recentes (2023–2026)*. Os resultados apontaram para shots no Dribbble, um SOTD de 2017 e uma lista com origem em 2013. **[F]** (status **[NV]**):

- collagecrafting.com (Awwwards, 2017).
- restaurant-lemoderne.fr, brokedesign.com e snowboard-zezula.cz/bern (lista da Designmodo, de idade incerta).
- O layout da Ghia, só via Dribbble ([KOTA](https://kota.co.uk/blog/branding-inspiration-brand-design-trends-for-2026)).
- tylerupchurch.com.
- ellenporteus.com, entre collage e maximalismo.
- La Palatine, citada pela Figma sem URL e não encontrada.

Candidatos **[NV]**: as páginas do Spotify Wrapped e ghia.com.

---

## Tabela de encaixe e risco cobre os dezoito de uma vez

A tabela abaixo condensa o catálogo para a etapa de recomendação. Os níveis de risco de primeira impressão seguem a lógica da pesquisa de complexidade e prototipicidade ([Google Research](https://research.google/blog/users-love-simple-and-familiar-designs-why-websites-need-to-make-a-great-first-impression/)), mas a atribuição estilo a estilo é uma síntese **[S]**. Nenhum estudo de 2023–2026 compara confiança entre estilos modernos nomeados.

| # | Estilo | Eixo | Risco de 1ª impressão/confiança | Risco de acessibilidade principal | Custo de performance | Melhor encaixe | Encaixe ruim |
|---|---|---|---|---|---|---|---|
| 1 | Minimalist | estética | baixo | sinalizadores fracos, nav escondida, cinza claro | muito baixo | arquitetura, wellness, SaaS, produto único | catálogos grandes, notícias, varejo de desconto |
| 2 | Swiss | estética | baixo | headline estourando a 320px, significado só no vermelho | muito baixo | cultura, arquitetura, foundries, B2B técnico | romântico, infantil, heritage luxury |
| 3 | Editorial | estética + layout | baixo | ordem DOM/visual, legendas claras | baixo a médio (imagens) | editoras, moda, hospitalidade, thought leadership | apps utilitários, varejo de desconto |
| 4 | Brutalist | estética | alto (B1 baixo) | hierarquia fraca na variante jarring | mínimo | arte, cultura, manifestos, dev | checkout, finanças, saúde |
| 5 | Neo-brutalist | estética | médio a alto | pares de cor, CTA perdido | baixo | startups, criadores, jovem, DTC | finanças, saúde, bancos |
| 6 | Bento | layout | baixo a médio | ordem de tab vs visual | baixo | SaaS, hardware, dashboards, link-in-bio | leitura longa, mensagem única |
| 7 | Glassmorphism | superfície | médio | contraste sobre fundo variável, 2.4.11 | **alto** (`backdrop-filter`) | IA, crypto, música, beleza (só nav) | formulários, bancos, grades de produto |
| 8 | Neumorphism | superfície (acento) | médio | **contraste não-textual (1.65:1), estado invisível** | baixo a médio | IoT, áudio, meditação (acento) | formulários, checkout, baixa visão |
| 9 | Claymorphism | superfície | médio | texto branco sobre pastel, borda só de sombra | médio (sombras e 3D) | onboarding, infantil, fintech amigável | dados densos, jurídico, luxo |
| 10 | Retro | estética-mãe | médio (MCM baixo) | display no corpo, flicker, texturas | baixo a médio | música, comida, móveis, impresso | saúde, seguros, governo |
| 11 | Y2K | estética | alto | texto cromado, neon sobre neon, glitch | médio a alto (blobs) | moda, beleza, música, Gen-Z | bancos, B2B sério |
| 12 | Maximalist | estética | alto | texto sobre padrão, marquees, flashes | médio a alto | CPG, entretenimento, festivais | saúde, finanças, público mais velho |
| 13 | Organic | estética-mãe | médio | texto sobre grain e foto, tons terrosos médios | baixo a médio | wellness, clean beauty, artesanal | trading, segurança, dev tools |
| 14 | Luxury | estética | médio | serifs finas, cinza "elegante", vídeo sem pausa | médio (vídeo) | moda, joias, hotéis, imóveis | desconto, SaaS utilitário |
| 15 | Dark/tech | modo de cor + estética | médio | cinza secundário < 4.5:1 | baixo a médio | dev tools, IA, SaaS, crypto | infantil, saúde, PME local |
| 16 | Kinetic type | movimento | alto | 2.2.2, vestibular, leitores de tela no split | médio (layout em fontes variáveis) | agências, moda, eventos | jurídico, saúde, leitura |
| 17 | Immersive scroll | movimento + mídia | alto | scrolljacking, vestibular, foco preso | **alto** (WebGL, sequências) | lançamentos, luxo, relatórios | e-commerce, docs, serviços locais |
| 18 | Collage | estética/técnica | alto | ordem de leitura, texto rotacionado, 2.4.11 | médio (recortes) | artesanal, comida, música, jovem | finanças, jurídico, saúde |

A leitura transversal da tabela: os riscos se concentram em três famílias com mecanismos diferentes. As **superfícies translúcidas e de sombra** (glass, neu) falham em contraste e em estado. As **estéticas de alta expressividade** (brutalist jarring, maximalist, Y2K, collage) falham em hierarquia e em ordem de leitura. Os **padrões de movimento** (kinetic, immersive) falham nas regras vestibulares e de pausa. Isso sustenta a proposta de que cada cartão carregue *guardrails* próprios além do contrato base.

## Quinze candidatos preenchem lacunas de tendência e de "padrão seguro"

### O que as fontes de 2025–2026 nomeiam e a lista não tem

A Figma cita **Retrofuturism** (visões vintage do futuro com neon, cromado e pixel) como tendência de 2026 **[F]** ([Figma](https://www.figma.com/resource-library/web-design-trends/)). A Envato registra, nas buscas internas do seu marketplace, "neon lights" **+200% em 4 semanas**, "distorted" +45% em 12 semanas e gráficos "experimental" com textura +61%. São contagens internas, não dados de mercado **[F]** ([Campaign Brief](https://campaignbrief.com/?p=305818)). A Adobe Express (dezembro de 2025) nomeia design tátil com "puffy, soft textures and hyper-realistic objects", "exaggerated, playful letters", imagem surreal e absurda, design orgânico e imperfeito, layouts livres de zine, sabor local e cultural, collage e layouts maximalistas **[F]** ([Adobe](https://www.adobe.com/express/learn/blog/design-trends-2026)). Flat Design segue como tag permanente na Awwwards **[F]** ([Awwwards](https://www.awwwards.com/websites/)). O **Corporate Memphis** (Alegria) se popularizou depois que o Facebook o adotou em 2017. Em 2023 já tinha perdido popularidade e virado alvo de paródia **[F]** ([Wikipedia](https://en.wikipedia.org/wiki/Corporate_Memphis)). O índice do daisyUI cataloga ainda Memphis, Vaporwave, Jet Age, Retro-Futurism, Halftone/Comic, Cybercore, Seapunk, Solarpunk e Cottagecore **[F]** ([daisyUI](https://trends.daisyui.com/)).

### Candidatos por eixo

As definições usam vocabulário padrão de design **[S]**. Nenhuma fonte primária foi consultada para definir Japandi, Swiss-punk ou Aurora UI.

| Candidato | Definição | Sinal 2024–26 | Eixo | Prioridade **[S]** |
|---|---|---|---|---|
| Flat / Material | cores sólidas, formas simples; o Material acrescenta elevação de "papel" e regras de movimento | tag Flat Design permanente na Awwwards | estética de base | **alta**, é o padrão seguro que falta |
| Typographic-led / Swiss-punk | o tipo é o visual principal; Swiss-punk quebra o grid suíço | "Typographic" é a maior categoria da Siteinspire (2.105); "exaggerated letters" na Adobe | estética | alta |
| Illustrative / hand-drawn | ilustração própria ou rabiscos lideram; letra à mão | "organic and imperfect" e doodles na Adobe | estética | alta |
| Cyberpunk / neon | fundo escuro, magenta e ciano, glitch, HUD, mono | picos de busca por neon (Envato), retrofuturism (Figma) | estética (pode absorver o Dark "cyber") | alta |
| Retrofuturism | o futuro visto do passado: cromado, neon, curvas de era espacial | tendência de 2026 (Figma, Envato) | estética, distinta de Y2K e Retro | alta |
| Scandinavian / Japandi | neutros claros, madeira, sans suave, minimalismo quente | interiores, móveis, wellness | estética (ou variante do Minimalist warm) | média |
| Japanese / Wabi-sabi | assimetria, imperfeição, texturas naturais, às vezes tipo vertical | "organic and imperfect" na Adobe | estética (ou variante do Organic) | média |
| Art Deco | simetria, preto e dourado, ornamento geométrico escalonado, serifs de alto contraste | hospitalidade, bares, eventos | estética (ou variante do Luxury) | média |
| Bauhaus / geometric | cores primárias, círculos, quadrados e triângulos, sans | nicho estável em arte e cultura | estética | média |
| Memphis (anos 1980) | brilhantes em choque, rabiscos, confete, terrazzo | marcas lúdicas, eventos | estética (ou preset do Retro) | média |
| Skeuomorphism / tactile | materiais reais (couro, metal, papel) | "hyper-realistic objects" na Adobe | estética + superfície | média |
| Anti-design / chaotic | quebra deliberada de grids, distorção | "Chaos packaging" (Envato); "anti-design" (Figma) | extremo expressivo do Brutalist | baixa como entrada própria |
| Liquid Glass | material translúcido refrativo e dinâmico (Apple, 2025) | alta visibilidade, ressalvas fortes da NN/g | superfície (evolução do glass) | subvariante do Glass |
| Aurora / gradient mesh, Grainy gradients, Duotone, Monochrome | fundos e tratamentos | comuns em IA e SaaS | superfície ou paleta | modificadores |
| Corporate Memphis | figuras planas com membros elásticos | em queda e parodiado desde 2023 | ilustração | **só como antipadrão "datado"** |

Também devem entrar como modificadores, e não como estilos, o **3D/WebGL product** (padrão de mídia), **Surreal/absurdist** (direção de imagem), **Cultural/heritage-local** (modificador de estilo), **Zine/freeform** (vizinho do Collage) e **Gamified UI** (interação), todos com sinal na Adobe ou na Figma **[S]**. Não há dado quantitativo de prevalência entre galerias para nenhum candidato.

## Recomendar a partir de uma foto ou frase tem evidência indireta

### Primeiras impressões favorecem o simples e o típico da categoria

A evidência sobre como as pessoas julgam um site é antiga, mas consistente. Lindgaard et al. (2006) mostraram que o apelo visual é julgado com cerca de **50 ms** de exposição, e que essas notas instantâneas concordam com as obtidas depois de mais tempo olhando **[F]** ([Nature News](https://www.nature.com/news/2006/060109/full/news060109-13.html)). Tuch et al. (Google, 2012) reduziram a janela para **17–50 ms**. No mesmo estudo, sites muito complexos foram considerados menos bonitos mesmo quando familiares, e sites pouco prototípicos foram considerados mais feios mesmo quando simples **[F]** ([Google Research](https://research.google/blog/users-love-simple-and-familiar-designs-why-websites-need-to-make-a-great-first-impression/)). No estudo de Fogg et al. (2002), com 2.684 participantes, **46.1%** dos comentários sobre credibilidade mencionavam o visual do site **[F]** ([ClickZ](https://clickz.com/study-for-site-cred-looks-matter/56564/)). Reinecke & Gajos analisaram 2.4 milhões de avaliações de cerca de 40 mil pessoas e encontraram variação de preferência por gênero, escolaridade e país: mulheres gostaram mais de sites coloridos, maior escolaridade reduziu a preferência por cor e russos preferiram menos complexidade **[F]** ([Reinecke & Gajos, CHI 2014](https://eecs.harvard.edu/~kgajos/papers/2014/reinecke14visual.shtml)).

A implicação para a skill é direta. A aceitabilidade de um estilo depende da convenção do setor. Um recomendador deveria aumentar o peso da prototipicidade em categorias sensíveis a confiança, como finanças, saúde, jurídico e B2B, e reduzi-lo nas categorias criativas **[S]**. Falta, porém, evidência recente: nenhum estudo revisado por pares de 2023–2026 compara confiança entre estilos nomeados (brutalist contra minimal, por exemplo).

### Agências traduzem palavras em direções, não em layouts completos

A prática documentada de agência começa pelas palavras. Os *style tiles* de Samantha Warren (2012) coletam adjetivos com perguntas de metáfora ("que veículo seria o site?") e pares de diferencial semântico ("moderno vs. antiquado"), agrupam os temas recorrentes e apresentam **três tiles**. No caso do Washington Examiner, os três partiam de "clean", "strong" e "friendly", e os stakeholders combinaram elementos num tile final **[F]** ([A List Apart](https://alistapart.com/article/style-tiles-and-how-they-work)). O mesmo texto avisa que mood boards são vagos demais para um sistema web e que apresentar várias telas completas leva o cliente a montar um "Frankencomp". O framework de personalidade de marca de Aaker (1997) tem cinco dimensões: Sincerity, Excitement, Competence, Sophistication e Ruggedness **[F]** ([Aaker 1997](https://gwern.net/doc/economics/1997-aaker.pdf)). A distinção clássico↔expressivo de Lavie & Tractinsky funciona como ponte validada entre adjetivos e visual **[F]** ([Hobday](https://anthonyhobday.com/blog/20221005.html)). Não foi encontrado nenhum mapeamento publicado e validado das dimensões de Aaker para estilos web específicos.

### Construtores de IA pedem negócio, não estilo, e nenhum lê a foto do produto

Os construtores atuais pedem informação sobre o negócio e o propósito, geram um design e oferecem botões de shuffle ou regenerar:

- **Wix:** faz 4–5 perguntas sobre propósito e conteúdo, sem pergunta de estilo. Descreve o tema em palavras, oferece "Generate new theme" e "Shuffle these colors" e guarda só os cinco designs anteriores **[F]** ([Website Builder Expert](https://www.websitebuilderexpert.com/website-builders/how-use-wix-ai/)).
- **Squarespace Blueprint AI:** é o único com um passo explícito de estilo. O usuário escolhe uma de **sete personalidades** (Professional, Playful, Sophisticated, Friendly, Bold, Quirky, Innovative), cada uma com **quatro paletas e dois pares de fontes** (14 no total) e preview ao vivo **[F]** ([Website Builder Expert](https://www.websitebuilderexpert.com/website-builders/squarespace-blueprint-ai/)).
- **Durable:** oferece Palette (presets ou a partir da cor da marca), **Corners** (de reto a arredondado), Fonts e **Shuffle**, que remixa sem mexer no layout **[F]** ([Durable](https://help.durable.com/en/articles/15199763-designing-your-site-colors-fonts-and-corners)).
- **Relume:** gera conceitos depois do sitemap e do wireframe, com "surprise me", shuffle com travas e um modo **Pitch Concepts** que mostra os **3 melhores conceitos** com descrições curtas **[F]** ([Relume](https://resources.relume.io/resources/docs/concept-creation-using-the-relume-style-guide-builder)).
- **Framer AI** (2023): define o estilo só pelo prompt, com adjetivos de "vibe" **[F]** ([DesignProject](https://designproject.io/blog/better-framer-ai-prompts/)).
- **v0, Lovable e Bolt:** não têm presets, e o padrão React + Tailwind + shadcn/ui produz o "visual shadcn" quando ninguém customiza **[F]** ([Anna Arteeva](https://annaarteeva.substack.com/p/design-systems-lovable-bolt-v0-and)). As funções de 2026 de Lovable e v0 não foram verificadas.

Nenhum desses construtores infere estilo a partir de uma **foto de produto**, e nenhum expõe **estilos nomeados com justificativa**. Essas são as duas brechas de diferenciação **[S]**.

### Opções de mecânica de escolha, sem plano de implementação

As opções abaixo são alternativas que a evidência sustenta. São descritas como opções de produto, e o plano de implementação fica para depois **[S]**.

**Opção A: sinais → dials → ranking.** A ideia é extrair sinais do input mínimo:

- Da foto: paleta dominante, material e textura, clima de luz, categoria e faixa de preço implícita.
- Da frase: adjetivos e tom.
- Da ideia de marca: público, categoria e posicionamento.

Esses sinais são projetados num pequeno conjunto de dials: dimensão de Aaker (ou personalidade estilo Squarespace), clássico↔expressivo, complexidade, prototipicidade, temperatura (frio/tech↔quente/orgânico), faixa de preço e tipo de conteúdo. Cada cartão do catálogo é pontuado contra os dials, com penalidade de convenção setorial. A vantagem é usar o que a pesquisa de primeira impressão mede. A desvantagem é que nenhum mapeamento validado de adjetivo para estilo existe, então os pesos começam arbitrários.

**Opção B: três direções explicadas.** É a tradução direta de Warren (três tiles) e da Relume (top 3): uma direção **segura/prototípica**, uma **expressiva fiel à marca** e uma **ousada**. Cada uma vira um cartão tipo style tile com paleta, par tipográfico, uma amostra de UI e um recorte de hero usando a foto do próprio usuário, mais uma frase de justificativa ligada aos adjetivos extraídos. A direção ousada leva uma nota explícita de troca, como "memorável, mas menos convencional para fintech". É a opção com mais respaldo de prática e a que melhor atende o "deixar o usuário escolher".

**Opção C: seletor de personalidade.** Copia o Squarespace: o usuário escolhe uma de 5–7 personalidades e cada uma abre um subconjunto do catálogo. É barato e previsível, mas joga fora o sinal da foto e reduz o catálogo a poucos rótulos.

**Opção D: galeria livre do catálogo.** O usuário navega pelos 18 (ou mais) cartões com nome e escolhe. É transparente, mas devolve ao usuário o trabalho de decidir sem orientação e esbarra no fato de que o público leigo não conhece os nomes dos estilos.

**Opção E: mistura no nível dos tokens, como camada sobre qualquer outra.** Travar o tipo e embaralhar a paleta, ou travar o layout e trocar a superfície, como fazem a Relume e a Durable, em vez de misturar telas inteiras. Isso evita o "Frankencomp" que Warren descreve e casa naturalmente com a taxonomia multieixo.

Um mapeamento heurístico entre as dimensões de Aaker e os estilos **[S]**, útil para qualquer uma das opções:

| Dimensão de Aaker | Estilos sugeridos |
|---|---|
| Sincerity | Organic, Scandinavian, Illustrative |
| Excitement | Maximalist, Neo-brutalist, Y2K, Kinetic |
| Competence | Swiss, Minimal, Flat/Material, Bento |
| Sophistication | Luxury, Editorial, Art Deco, Monochrome |
| Ruggedness | Brutalist, Retro workwear, dark com textura |

Heurísticas de conteúdo **[S]**:

- Marcas guiadas por foto de produto pedem estilos de pouca moldura (Minimal, Luxury, Editorial), que deixam a imagem trabalhar.
- Sites com muito texto pedem Editorial ou Swiss.
- App e SaaS pedem Flat, Bento ou Dark.
- Glass e neumorfismo só entram como superfície secundária com baixa densidade.

## Registro de incertezas a resolver antes de publicar o catálogo

| Item | Situação | Ação |
|---|---|---|
| Sites de exemplo de todos os cartões | nenhum aberto ao vivo; vieram de roundups de 2024–2026 | conferir com screenshot; o Gumroad já aparece sem `box-shadow` |
| Exemplos Swiss e Collage | nenhum verificado em galeria; Collage sem exemplo ao vivo de 2023–2026 | navegar por tags na Awwwards, Godly e Siteinspire num browser real |
| Licenças de fontes | nenhuma conferida individualmente; Ubuntu não é OFL; Geist não verificada; Satoshi, General Sans e SF Pro fora; display setentistas comerciais sem licença declarada | ler o OFL.txt/LICENSE de cada família no build |
| Scroll-driven animations | Firefox atrás de flag na 152 segundo fonte secundária; versões do Safari não cruzadas com o MDN | checar MDN/caniuse; manter progressive enhancement |
| `prefers-reduced-transparency` | sem Safari, segundo um espelho do MDN que pode estar defasado | checar o MDN; manter o toggle na página |
| `backdrop-filter: url()` (Liquid Glass web) | só Chromium; `CSS.supports` não é confiável | tratar como enhancement opcional |
| `@property`, `linear()`, `initial-letter`, subgrid | versões de suporte não verificadas nesta pesquisa | checar no build |
| Bugs de backdrop-filter | correção do Chrome 142 e bug do Firefox sticky (Nightly, setembro de 2026) relatados só pelo Josh Comeau | reconferir |
| Datas de origem | brutalismo 2014 vs 2016; neumorfismo (Plyuto) 2019 vs 2020; claymorphism 2021 vs 2022 | manter as duas datas no cartão |
| Valores contraditórios | setproduct: branco sobre coral "≥4.5" (calculado 2.55); The Plus Addons: offset de 14px na figura vs 6px no código | usar os valores calculados e os do código |
| Estatísticas de editorial | números atribuídos a NN/g 2026 e Baymard 2025 sem link | não usar |
| Contrastes estimados (cartões 1, 2, 14) | estimativas dos pesquisadores, diferentes dos valores **[C]** | rodar checker antes de fixar tokens |
| Core Web Vitals | limiares citados de conhecimento geral | conferir no web.dev |
| neumorphism.io | algoritmo do gerador não confirmado | não citar como fonte |

## Conclusão

A decisão de arquitetura pesa mais do que qualquer valor de CSS deste relatório. Ao tratar superfícies (glass, neu, clay), layout (bento) e movimento (kinetic, immersive) como modificadores com regras próprias de combinação, o catálogo deixa de ter 18 itens que se sobrepõem. Passa a ter cerca de 12 estéticas, mais as candidatas, sobre as quais se aplicam modificadores conhecidos. Cada modificador carrega o próprio guardrail: glass só na camada de navegação, neumorfismo só como acento, movimento sempre opt-in e pausável. Essa estrutura também resolve um problema silencioso de qualidade. A distribuição desigual de evidência fica visível: os estilos com números de fonte são justamente os mais "técnicos" (neo-brutalismo, glass, neumorfismo, clay, bento e scroll-driven), enquanto os mais "culturais" (Swiss, Luxury, Editorial e Collage) dependem de valores sintetizados e de exemplos não verificados. O próximo passo de pesquisa com melhor retorno é medir tokens reais de sites verificados nesses quatro estilos.

Quanto à recomendação, a vantagem da skill está menos em adivinhar o estilo certo e mais em explicar por que três direções servem àquela marca. A pesquisa de primeira impressão justifica sempre oferecer uma direção prototípica para o setor. A prática de agência justifica oferecer três opções, em vez de uma ou de dez. E a ausência, no mercado, de construtores que leiam a foto do produto ou nomeiem estilos indica que dar nome aos estilos e justificar a escolha já diferencia o produto, mesmo antes de qualquer ganho na precisão do ranking.
