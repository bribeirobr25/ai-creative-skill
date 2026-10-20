# Briefing fixo — NOMA / Objetos de todos os dias

NOMA é uma marca **fictícia** de acessórios para este estudo. Não se afirma que
exista comercialmente nem que o nome esteja disponível para registro.

## Público e objetivo

Adultos 28–45, urbanos, interessados em acessórios discretos, expressão pessoal e
informação clara antes da compra. A visita deve apresentar o universo da marca,
permitir comparar duas bolsas, entender um produto e simular sua inclusão no carrinho.
Português do Brasil, preços demonstrativos em euros.

Tom: seguro, sóbrio, tátil, contemporâneo. Não transformar “premium” em ostentação,
depoimentos inventados, escassez artificial, slogans vagos ou animação obrigatória.
Buscamos uma experiência comercial visualmente madura, não um dashboard.

## Identidade obrigatória e liberdade

Nome NOMA; assinatura “Objetos de todos os dias”.
Paleta-base: tinta `#252A28`, papel `#F3F1EB`, verde `#43594B`.
Tons neutros auxiliares permitidos; contraste deve funcionar. Cores das fotografias
permanecem intactas. Fontes disponíveis no sistema; combinação livre.
Wordmark tipográfico permitido; sem símbolo que reproduza marca existente.

Livres: estrutura editorial, proporções, grade, escala tipográfica, distribuição
das imagens, componentes e transições discretas. Não há layout de referência.
Não exigir hero gigante, serifas, cards, bordas arredondadas ou scroll animado.

## Conteúdo comum obrigatório

Hero: “Para levar o que importa.”
Texto: “Duas formas de acompanhar a cidade. Uma coleção de linhas simples, texturas presentes e espaço para o essencial.”
Ação principal: “Explorar coleção”.

Seção editorial: “Menos excesso. Mais presença.”
Texto: “Uma dobra, uma linha, um gesto. A coleção aproxima formas cotidianas de um olhar atento ao detalhe.”
Usar a foto editorial como detalhe ilustrativo; ela NÃO mostra Arco ou Trama.

| ID | Nome | Preço | Cor | Medidas demonstrativas | Descrição |
|---|---|---|---|---|---|
| arco | Arco | €180 | Caramelo | 24 × 17 × 8 cm | Silhueta compacta, aba frontal e alça para acompanhar seus movimentos. |
| trama | Trama | €240 | Castanho | 32 × 23 × 12 cm | Volume estruturado, alças de mão e espaço para organizar o cotidiano. |

Especificações são dados fictícios do protótipo; não alegar certificações, origem,
composição do material, sustentabilidade, garantia, entrega ou fabricação artesanal.
Imagens são referências licenciadas, não fotografias de produtos reais NOMA.
Aviso visível no footer e carrinho: “Protótipo demonstrativo. Marca, produtos e preços fictícios. Não realiza vendas.”
Informação adicional de fotos: “Fotografias ilustrativas licenciadas do Pexels.”
Créditos detalhados podem estar em painel/página acessível.

## Experiências e comportamento

1. Homepage editorial com proposta, coleção e conteúdo editorial.
2. Catálogo com os dois produtos, nomes/preços e filtro de faixa de preço:
   “Todos” e “Até €200”, retornando somente Arco no segundo caso.
3. Página/rota de produto para cada item, imagem, descrição, cor, medidas e adicionar.
4. Carrinho demonstrativo: nome, preço unitário, quantidade inteira 1–9, subtotal,
   remoção e vazio. Valor nunca negativo/NaN; nenhuma cobrança ou dados pessoais.
5. Navegação ida/volta por URLs ou hash; homepage, coleção e carrinho acessíveis.
   Mobile pode usar menu ou links visíveis, sem inventar controle inoperante.
6. Teclado, foco visível, rótulos acessíveis, texto alternativo e reduced motion.
7. Sem chamadas de rede externas, analytics, pagamento, cadastro ou “checkout” falso.
   Sem login, backend, envio de formulário ou botões decorativos sem destino.

## Materiais

- `assets/arco.jpg`: foto integral do item Arco.
- `assets/trama.jpg`: foto integral do item Trama.
- `assets/editorial.jpg`: detalhe genérico, não foto alternativa de qualquer SKU.
- `assets/credits.json`: origem e licença de cada fotografia.

Nenhuma mudança de pixels; enquadrar via CSS, sem distorcer proporções. Não substituir
por ilustração geométrica. A biblioteca limitada, sem lifestyle ou múltiplos ângulos,
é uma limitação explícita do piloto e não pode ser atribuída à skill.

## Entrega do executor

Diretório `r0/` navegável com `index.html` e recursos locais; `execution.md` fora do
site com início/fim, decisões, arquivos de orientação lidos, limitações e verificações
realizadas. Não incluir a condição experimental nas páginas. Não publicar.
Não olhar a condição concorrente. Encerrar a primeira entrega e aguardar o feedback
único para `r1/`; nunca sobrescrever `r0/`.
