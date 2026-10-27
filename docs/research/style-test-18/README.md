# Teste dos 18 estilos · Della Berlin (21–22/10/2026)

**Pergunta:** a skill (candidata 2.6, `0f7089a`) executa um estilo visual dado como entrada, de forma reconhecível e funcional?

## Desenho

- Um briefing (marca real, lista de interesse, seis modelos, sem preço) e o mesmo conjunto de 39 imagens (photoshoot v02 aprovado pelo dono, renders e editoriais da Croissant, fotos de produção, ilustração). Briefing registrado só por hash: `8fe28fe532bcb30e9577f8dc7a139514254bcb17376075d05d4e989558d0911b`. Fotos e sites ficam com o dono, fora do repositório.
- 18 execuções isoladas, uma por estilo, com `STYLE.md` gerado de `../style-catalog/cartoes-estilo-teste-18-v0.json` (sha256 `e424b1efb242634577578d223805f66c08b725efd36d1619dab6b2de9e96aa79`), as instruções em `executor-instructions.md`, um pool de 30 famílias OFL e a skill copiada para a pasta da execução. Preferências visuais do dono incluídas, com a regra "o estilo vence em conflito".
- Mesmo coletor do DQB-03 (`validation/dqb03/tools/check_site.py`, 88 verificações funcionais e de fidelidade) em todas. Uma rodada de correção apenas quando o coletor achou defeito.

## Resultado

| Execução | Estilo | Coletor | Maior imagem do topo (Croissant) |
|---|---|---|---|
| s01 | Minimalist | 88/88 | pedestal |
| s02 | Swiss / International Typographic Style | 88/88 | café |
| s03 | Editorial / Magazine | 88/88 | café |
| s04 | Brutalist | 88/88 | café |
| s05 | Neo-brutalist | 88/88 | café |
| s06 | Bento grid | 88/88 | café |
| s07 | Glassmorphism | 88/88 | café |
| s08 | Neumorphism (soft UI) | 88/88 | café |
| s09 | Claymorphism / soft 3D | 88/88 | making-of (maior imagem medida; visualmente café) |
| s10 | Retro / vintage | 88/88 | café |
| s11 | Y2K | 88/88 | café |
| s12 | Maximalist | 88/88 | café |
| s13 | Organic / natural | 86/88 (falso positivo, E4) | café |
| s14 | Luxury / elegant | 88/88 | pedestal |
| s15 | Dark / tech | 88/88 | pedestal |
| s16 | Kinetic typography | 88/88 | patisserie |
| s17 | Immersive / 3D scroll | 88/88 | café |
| s18 | Collage / scrapbook | 88/88 | café |

- **Estilos reconhecíveis e distintos** nas 18 aberturas (folhas comparativas com o dono).
- **Funcionamento:** 17 com 88/88; o s13 falhou 2 verificações por um artefato de extração de texto (SVG dentro do `h1`), corrigido no coletor (emenda E4 do DQB-03).
- **Rodadas de correção:** s06 (imagens dos modelos colapsadas na página inicial; os 62 testes do próprio executor passavam) e s05 (preload de fonte com `crossorigin` gerando erro de console em `file://`).
- **Conflitos estilo × preferências do dono:** 4 (Brutalista: cantos retos; Suíço: raio 4 px e controles quadrados; Editorial: botão principal discreto; Claymorphism: sulco no lugar da linha). Os outros 14 acomodaram tudo.
- **Convergência da imagem principal:** as 18 abrem com a Croissant; a mesma foto do café é a maior imagem do topo em 13 (medição automática).
- **Fechamento do método:** 1 de 18 gerou e validou o registro de entrega; nenhum iniciou o servidor de prévia (`file://` bastou). Origem dos itens 2–4 do backlog 2.6.
- **Peso:** sites de 9–10 MB, porque "não editar pixels" foi lido como "não redimensionar".

## Leitura

A skill executa bem um estilo dado; a escolha do estilo e da imagem principal precisa vir de fora do agente (dono ou catálogo). O catálogo usado aqui foi escrito pela coordenação e é anterior à pesquisa em `../style-catalog/`.
