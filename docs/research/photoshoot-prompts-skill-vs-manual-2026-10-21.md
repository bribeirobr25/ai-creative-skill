# Prompts de photoshooting: skill × manual (21/10/2026)

**Pergunta:** a AI Creative Skill escreve um pacote de prompts melhor do que o coordenador escrevendo direto?

**Caso:** sessão de fotos das necessaires da Della Berlin (marca real) a partir das fotos reais, para o proprietário
rodar no GPT Image por um GPT customizado. Material da marca fica fora deste repositório; aqui só o método e os achados.

## Desenho

- **Manual (v1):** escrito pelo coordenador com o contexto da conversa e os documentos da marca, sem carregar a skill.
- **Skill:** executor isolado, só com `src/ai-creative-skill/` (candidata `web-runtime-2.6-v1`, `0f7089a`), as mesmas
  fotos e os mesmos fatos da marca, sem ver a v1. Começou no `SKILL.md` e registrou o rastro (`skill-trace`).
- **Avaliação:** revisor independente, cego (pacotes X/Y), rubrica de 9 critérios aplicada antes de qualquer imagem,
  conferindo os fatos contra as fotos. Chave revelada só depois: X = manual, Y = skill.

## Resultado

| Critério (1–5) | Manual | Skill |
|---|---:|---:|
| Fidelidade ao produto | 3 | 4 |
| Seleção e papel das referências | 2 | 4 |
| Proteção contra invenção | 3 | 4 |
| Direção fotográfica | 4 | 4 |
| Adequação ao site | 4 | 4 |
| Adequação ao GPT Image | 3 | 4 |
| Uso pelo proprietário | 3 | 4 |
| Marca | 4 | 4 |
| Controle de risco | 3 | 4 |
| **Total** | **29** | **36** |

**Principais diferenças:** a skill recortou as referências para uma bolsa por imagem (sem cosméticos de marca,
adereços e ícones de tela), declarou o papel e as exclusões de cada referência, usou tamanhos nativos do modelo e
blocos de prompt autocontidos com checklist P0/P1/P2, limite de um reparo e registro de execução. A versão manual
inventou fatos (tecido "algodão", forros), tinha erros de modelo de texto (bolsa "sobre dois limões") e mandou fotos
com marcas de terceiros. A manual foi mais curta e manteve uma série visual única na grade.

**Erros da skill:** cor do bordado de um modelo (descrito tom sobre tom; é branco sobre azul), dois recortes de
referência ruins, foto de "feito à mão" gerada quando havia fotos reais, repetição excessiva (≈ 20 mil palavras).

## Lacunas da skill (decididas pelo executor, viram backlog)

1. Sem Work Profile para fotografia de produto/e-commerce (`PRODUCT_CONTENT` está adiado).
2. Sem taxonomia de fotos de produto para site/loja (hero, packshot, detalhe, aberto, uso, coleção).
3. Sem receita de rota para "pacote que o proprietário roda fora" (GPT customizado, sem API).
4. Recorte de referências permitido (Route Compilation §7.2) mas não prescrito quando o modelo não aceita referência
   parcial; o executor decidiu recortar e isso foi o maior ganho.
5. Sem regra para um fundo comum na grade de produtos (série visual).

## Leitura

O método Image Direction (verdade do produto, prontidão e papel das referências, modos de texto, rubrica de aceite)
melhora o resultado de forma mensurável mesmo antes de gerar imagens. O teste definitivo é gerar as mesmas fotos com
os dois pacotes; isso depende do proprietário rodar no GPT Image. Um pacote v2 com as correções do revisor foi entregue.
Também se confirmou um erro de material de entrada do coordenador no DQB-03 (descrição de um adereço como detalhe do
produto em `credits.json`), registrado nas emendas do DQB-03.
