# Auditoria de aprendizados · 21–22/10/2026

O que aprendemos com o DQB-03, o pacote de fotos da Della, a revisão das fotos geradas e o teste dos 18 estilos, organizado para entrar na AI Creative Skill. A pesquisa sobre estilos de web design é um trabalho separado e não está aqui. Cada afirmação aponta para a evidência; o que é dedução vem marcado como **(inferência)**.

## 1. Resumo

- **Foto de produto pede um caminho próprio na skill.** O executor da skill venceu a escrita manual numa avaliação cega (36 × 29 de 45). Mesmo assim, ele teve de decidir sozinho o dono da tarefa, a lista de fotos, o recorte das referências e o fundo comum, porque a skill não cobre isso. O perfil `PRODUCT_CONTENT` continua adiado.
- **Referência limpa é o fator que mais pesa na fidelidade.** Recortar cada referência para mostrar uma única bolsa, sem marcas de terceiros nem adereços, foi o maior ganho do pacote da skill. Hoje a skill só permite esse recorte; não o exige.
- **O GPT Image erra em dois pontos previsíveis:**
  - Desvia o desenho do tecido em close, foto aberta, foto com várias bolsas e cena de uso. O bordado da Azul virou margarida em 5 imagens.
  - Deforma etiquetas pequenas. "EST. 2023" saiu errado em 11 de 11 etiquetas de coleção e em 3 de 25 etiquetas de foto individual, sempre onde a etiqueta aparece pequena.
- **A correção que funciona para etiqueta é a montagem com a etiqueta real**, não gerar de novo. Ela corrigiu as 14 etiquetas sem gastar créditos. A skill já prevê isso para logotipos, mas não para a etiqueta costurada no produto.
- **Pedir alternativas ao mesmo agente não cria diversidade.** No DQB-03, B não mudou a direção escolhida. No teste de estilos, a Croissant abriu as 18 páginas, e a mesma foto do café abriu entre 13 e 15 delas. A escolha da imagem principal e da direção precisa vir de fora do agente: do dono, de um estilo dado ou de uma regra.
- **A skill executa bem um estilo dado.** Os 18 estilos ficaram reconhecíveis e funcionais: 17 passaram em 88 de 88 verificações, e o 18º teve um falso positivo. Mas o catálogo de estilos foi escrito pela coordenação, não pela skill.
- **Os passos de fechamento da skill são fáceis de pular.** Só 1 de 18 executores gerou e validou o registro de entrega, e nenhum usou o servidor de prévia. A autoverificação também deixou passar um defeito visível (imagens colapsadas no s06), que só o verificador comum pegou.
- **Dois erros de material de entrada vieram da coordenação, não da skill:** o prendedor descrito como "flor aplicada" e o forro da Croissant descrito como "com bolinhas". Os fatos do briefing precisam ser conferidos contra as fotos antes de serem entregues aos executores.

## 2. Fontes de evidência

| Estudo | Data | O que testou | Onde está |
|---|---|---|---|
| DQB-03 | 21/10 | Método atual (A) × "divergir e escolher" (B); 8 execuções e 16 sites; teste de campo do runtime 2.6 | Branch de pesquisa DQB-03 (protocolo, relatório, emendas, métricas); capturas da Della no Drive |
| Prompts de fotos, skill × manual | 21/10 | Pacote escrito pela skill em execução isolada × escrito pela coordenação; avaliação cega com 9 critérios | `docs/research/photoshoot-prompts-skill-vs-manual-2026-10-21.md`; pacotes no Drive e na pasta do dono |
| Pacote de fotos v2 | 21/10 | Correções do avaliador aplicadas ao pacote da skill | Pasta do dono (`della-photoshoot-v2.zip`) |
| Revisão das fotos geradas | 22/10 | 26 imagens aprovadas mais 1 de coleção, comparadas às fotos reais com as etiquetas ampliadas | `QA_REVISAO_CONTRA_FOTOS_REAIS.md`, na pasta do dono |
| Troca de etiqueta | 22/10 | Montagem da etiqueta real em 14 etiquetas de 5 imagens | Arquivos `_ETIQUETA-REAL` na pasta do dono |
| Teste dos 18 estilos | 22/10 | Um site por estilo, mesmo briefing e mesmas fotos, executores isolados com a candidata 2.6 | `SITES_ESTILOS_2026-10-21/` na pasta do dono (sites, capturas, `_execution.md`, `_checks.json`) |
| PR #17 (runtime 2.6) | 21/10 | Router, QA e verificações a 320 px nos 16 sites do DQB-03 | PR #17 e seção 6 do relatório do DQB-03 |

## 3. Achados por área

### (a) Fotos de produto a partir da foto real

**F-A1 · Não há dono para foto de produto.**
- **O que aconteceu:** o executor registrou que `PRODUCT_CONTENT` está adiado (Arquitetura §5.2) e que nem Ads, nem Organic, nem Web são donos desse trabalho. Ele decidiu sozinho as lacunas 1, 3 e 5 do rastro.
- **Por que importa:** cada execução vai improvisar escopo, lista de fotos e regras.
- **Mudança proposta:** criar o perfil de trabalho `PRODUCT_CONTENT` (novo arquivo) e a rota no `SKILL.md`, seção "Product / marketplace identity".
- **Prioridade:** P1.
- **Como validar:** repetir o pacote da Della com o perfil novo e comparar com a nota de 36/45.

**F-A2 · O recorte das referências decide a fidelidade.**
- **O que aconteceu:** a avaliação cega deu 2 contra 4 no critério de referências. O pacote manual enviava fotos sem recorte, com marcas de terceiros, indicadores de tela do celular e o prendedor sobre a bolsa.
- **Mudança proposta:**
  - Route Compilation §7.2: tornar o recorte obrigatório quando a rota não aceita referência parcial (o GPT Image, por exemplo). Cada recorte mostra um único produto e declara seu papel e o que não pode passar adiante.
  - Image Direction §10: apontar para essa regra.
- **Prioridade:** P0.
- **Como validar:** checklist do manifesto de referências: nenhuma marca de terceiro e um produto por referência.

**F-A3 · O desenho do tecido se perde em alguns tipos de foto.**
- **O que aconteceu:**
  - O bordado da Azul virou "margaridas em grade de losangos" em AZ-D1, AZ-O1, AZ-E1, AZ-E2 e, provavelmente, AZ-L1.
  - A Branca sofreu o mesmo desvio na C-H1.
  - A C-H1 também inventou listras azuis na Ursinho.
  - O packshot e a foto de destaque da Azul saíram corretos.
- **Por que importa:** o close de tecido é justamente a foto que prova o produto.
- **Mudança proposta:**
  - QA Realism: verificação do desenho do tecido com zoom, nos tipos close, aberta, coleção e uso.
  - Image Direction §10.1: depois que um packshot fiel for aprovado, ele pode servir de referência de tecido para as fotos seguintes. As fotos reais continuam sendo a autoridade, e a origem fica registrada.
- **Prioridade:** P0 para a verificação; P1 para a regra de referência.
- **Como validar:** gerar de novo AZ-D1 com a AZ-P1 anexada e comparar o motivo com AZ-02.

**F-A4 · Etiqueta pequena sai deformada; etiqueta grande sai certa.**
- **O que aconteceu:**
  - Nas fotos individuais, 22 de 25 etiquetas ampliadas estavam corretas. Os 3 erros estão nas cenas de uso, onde a etiqueta tem cerca de 60 a 100 px.
  - Nas fotos de coleção, 11 de 11 etiquetas estavam deformadas.
  - A montagem perspectiva com a etiqueta real corrigiu todas as 14 etiquetas erradas. Ela troca só o miolo e preserva a borda e a luz da imagem gerada.
- **Mudança proposta:**
  - Image Direction §9.1: estender a regra a "marca aplicada no produto" (etiqueta tecida). Etiqueta prevista abaixo de cerca de 120 px vai para montagem controlada a partir de foto real. **(O limite de 120 px é inferência a partir dos casos.)**
  - Localized Repair: a montagem passa a ser o reparo padrão de etiqueta.
- **Prioridade:** P0 para a regra; P2 para transformar a montagem em script da skill.
- **Como validar:** ampliar todas as etiquetas a 3× e conferir o texto letra a letra.

**F-A5 · Faltam regras de série.**
- **O que aconteceu:** o executor teve de criar sozinho a lista de fotos (hero, packshot, detalhe, aberta, uso, coleção, feito à mão) e um fundo greige comum para os packshots. O fundo comum funcionou: os cinco packshots formaram uma série. Já a Croissant, num render de fundo branco, destoou nos 18 sites.
- **Mudança proposta:** no perfil `PRODUCT_CONTENT`, criar uma lista padrão de fotos para loja e uma regra de cenário comum para a grade, incluindo o modelo que já tem fotos boas (gerar o `CR-P1`).
- **Prioridade:** P1.

**F-A6 · Pacote que o dono roda fora.**
- **O que aconteceu:** sem créditos no Higgsfield, o caminho real foi um pacote de prompts para o GPT do dono.
  - O README da v2 dizia que as fotos podiam ficar como conhecimento do GPT. Pelo que sabemos, elas precisam ir anexadas a cada mensagem; isso foi corrigido.
  - O pacote manual pedia formatos 4:5 e 16:9, que não são tamanhos nativos do GPT Image.
- **Mudança proposta:** receita de rota "pacote executado pelo dono" no Route Recipe Spec. Inclui referências anexadas por mensagem, tamanhos nativos do modelo, blocos prontos para colar, um único reparo e registro de execução.
- **Prioridade:** P1.

**F-A7 · O que o briefing declara precisa bater com as fotos.**
- **O que aconteceu:**
  - Forro da Croissant: o briefing dizia "com bolinhas", mas as fotos reais mostram creme liso com pintas naturais do tecido.
  - O prendedor de cabelo foi descrito como "flor aplicada" em `credits.json`.
  - As duas informações chegaram aos executores. Um site legendou o prendedor como "flor aplicada" e só corrigiu na segunda rodada.
- **Mudança proposta:** Image Direction §5.1 e §10.3: o que a fonte declara e a foto contradiz vira conflito obrigatório, não fato.
- **Prioridade:** P1.

### (b) Método de website

**F-B1 · A escolha precisa vir de fora do agente.**
- **O que aconteceu no DQB-03:** B seguiu o passo de divergir sem custar mais (9,6 contra 10,5 min no R0). Mesmo assim, as alternativas se repetiram, e a direção escolhida foi a mesma de A. A fonte Fraunces apareceu em 8 de 8 sites e o fundo creme em 8 de 8.
- **O que aconteceu no teste de estilos:** com o estilo dado como entrada, os 18 sites ficaram claramente diferentes.
- **Mudança proposta:** no perfil Web v0.2, passo 3 do fluxo rápido, a direção vem de um estilo escolhido ou aprovado pelo dono, com uma recomendação da skill. O passo "divergir e escolher" não é adotado.
- **Prioridade:** P0. Depende da pesquisa de estilos.
- **Como validar:** benchmark com escolha pelo dono contra A.

**F-B2 · A imagem principal converge.**
- **O que aconteceu:**
  - Em 18 de 18 sites, a abertura usa a Croissant.
  - A mesma foto do café é a maior imagem do topo em 13 de 18 (medição automática). Na inspeção visual das capturas, aparece em cerca de 15.
  - No DQB-03, a imagem principal foi a mesma em 4 de 4 sites por marca.
  - Esses números corrigem os "17 de 18" que informei antes, que estavam superestimados.
- **Por que importa:** é uma decisão de marca que fica implícita. **(Inferência:** o briefing "liderado pela Croissant" puxa a escolha.)
- **Mudança proposta:** no perfil Web, a escolha da imagem principal vira decisão registrada, com justificativa e pelo menos uma alternativa mostrada ao dono.
- **Prioridade:** P1.

**F-B3 · Preferências do dono contra o estilo.**
- **O que aconteceu:** a regra "o estilo vence" foi aplicada em 4 sites:
  - Brutalista: cantos retos.
  - Suíço: 4 px de raio e controles quadrados.
  - Editorial: botão principal discreto.
  - Claymorphism: um sulco no lugar da linha.
  - Os outros 14 acomodaram todas as preferências.
- **Mudança proposta:** criar um perfil de preferências do dono como entrada do perfil Web, com regra de conflito explícita e registro no relatório de entrega.
- **Prioridade:** P1.

**F-B4 · O registro de entrega e a prévia são pulados.**
- **O que aconteceu:** 1 de 18 executores gerou `web_delivery.json` e validou. Os outros 17 relataram que pularam esse passo, e nenhum iniciou o servidor de prévia, porque `file://` bastava. No DQB-03 também não houve registro formal.
- **Por que importa:** a evidência fica heterogênea, e o critério "não declarar prévia sem abrir" fica sem prova.
- **Mudança proposta:** perfil Web, passos 6 a 8, e `creative_web.py`. Criar um registro mínimo obrigatório, gerado pelo script a partir da execução do QA, e aceitar `file://` aberto no navegador como prévia local válida.
- **Prioridade:** P0.
- **Como validar:** 18 de 18 registros válidos numa nova rodada.

**F-B5 · Peso das imagens.**
- **O que aconteceu:** os sites ficaram com cerca de 9 a 10 MB, porque a regra "não editar pixels" impediu versões menores das fotos. Um executor usou mesclagem por CSS para aproximar o fundo branco da Croissant ao greige, o que é uma alteração visual.
- **Mudança proposta:** no perfil Web, passo 4, distinguir edição de produto (proibida) de versão derivada para web (redimensionar e comprimir, permitido com origem registrada). Filtros de cor sobre fotos de produto passam a ser declarados.
- **Prioridade:** P2.

**F-B6 · O catálogo de estilos não existe na skill.**
- **O que aconteceu:** os 18 cartões de estilo foram escritos pela coordenação.
- **Mudança proposta:** criar uma referência nova de catálogo de estilos, com recomendação a partir da entrada. Ver a pesquisa separada.
- **Prioridade:** P1.

### (c) QA e evidência

**F-C1 · A autoverificação não basta.**
- **O que aconteceu:** no s06, os 62 testes do próprio executor passaram, mas o verificador comum achou as fotos dos modelos colapsadas na página inicial.
- **Por que importa:** o `images_rendered` do runtime 2.6 só reprova imagem que falhou ao carregar, não imagem com altura zero. **(Inferência:** o QA do runtime também deixaria passar esse defeito.)
- **Mudança proposta:** `qa.py`: verificação de imagem visível colapsada ou minúscula (área ou altura mínima), ignorando logotipos.
- **Prioridade:** P0.
- **Como validar:** rodar sobre o s06 antes da correção, que deve reprovar.

**F-C2 · Falsos positivos de texto.**
- **O que aconteceu:** o s13 falhou em "título preservado" porque um SVG decorativo dentro do `h1` quebra o `innerText`. Na tela, o título está correto.
- **Mudança proposta:** normalizar o texto (espaços e quebras) antes de comparar a cópia. Registrar a regra no QA.
- **Prioridade:** P1.

**F-C3 · Artefatos de captura.**
- **O que aconteceu:**
  - Em captura de página inteira, a navegação fixa aparece no meio da página. Isso foi relatado por 6 executores.
  - Imagens com carregamento tardio saem em branco. Dois executores tiraram o carregamento tardio só por causa da captura.
- **Mudança proposta:** o perfil Web já manda rolar a página antes de julgar as imagens. Acrescentar:
  - capturas por tela, não só de página inteira;
  - não mudar o site só para servir à captura.
- **Prioridade:** P2.

**F-C4 · Pré-carregamento de fonte com `crossorigin` gera erro de console em `file://`.**
- **O que aconteceu:** no s05, a fonte carregou mesmo assim. As fontes locais funcionaram nos 18 sites. O s02 converteu a fonte para base64 sem necessidade.
- **Mudança proposta:** nota técnica no perfil Web: não usar `crossorigin` em pré-carregamento local, e fontes locais funcionam em `file://`.
- **Prioridade:** P2.

**F-C5 · O verificador comum precisou de emendas.**
- **O que aconteceu:** emendas E1 a E3 (menu móvel e logotipos, tolerância das miniaturas, rolagem das capturas). Depois delas, 16 de 16 sites passaram no DQB-03, e 17 de 18 mais um falso positivo no teste de estilos.
- **Mudança proposta:** portar as verificações genéricas para `qa.py`: menu recolhido, imagem colapsada e captura por estado. As verificações do briefing ficam como modelo para `data-testid`.
- **Prioridade:** P1.

### (d) Runtime 2.6 (PR #17)

**F-D1 · As mudanças funcionaram no campo.**
- **O que aconteceu:**
  - O QA da V2.5 marcaria de 6 a 23 âncoras "quebradas" por site, todas falsas. O 2.6 marca 0.
  - O router da V2.5 recusava o pedido real; o 2.6 envia para `WEB_PREVIEW`.
  - As verificações de 320 px e de imagens rodaram nos 16 sites, sem caminhos absolutos na evidência.
  - Nenhuma regressão foi encontrada.
- **Mudança proposta:** fazer o merge do #17 junto com F-C1, F-C2 e F-B4.
- **Prioridade:** P0.

### (e) Governança e processo de pesquisa

**F-E1 · O que funcionou.** Protocolo congelado, IDs neutros, executores isolados, hashes, emendas registradas e verificador comum tornaram a comparação legível. Esse modelo deve virar o guia de benchmark no Implementation Validation Plan. **P1.**

**F-E2 · Privacidade.**
- Repositório público, autor noreply, caminhos redigidos.
- Material da Della fica fora do GitHub (só no Drive e na pasta do dono).
- Push de tag e force push são bloqueados neste ambiente; as tags são criadas pelo dono.
- Mudança proposta: documentar como checklist de pesquisa. **P1.**

**F-E3 · Material de entrada da coordenação.** Os dois erros do F-A7 nasceram na coordenação. Mudança proposta: conferir os fatos do briefing contra as fotos antes de congelar o protocolo. **P1.**

**F-E4 · Branches pendentes.** PR #17 aberto; branch de pesquisa do DQB-03 sem PR; branch experimental de B. O combinado é fazer um merge único no fim. **P0** (organizacional).

## 4. Lacunas da skill

| Lacuna | O que existe hoje |
|---|---|
| Perfil de foto de produto (`PRODUCT_CONTENT`) | Listado como adiado (Arquitetura §5.2) |
| Lista padrão de fotos para loja | Nada |
| Receita de "pacote executado pelo dono" | Nada; a Route Recipe Spec só cobre execução pela skill |
| Recorte obrigatório das referências | Só permitido (Route Compilation §7.2) |
| Fundo comum para série de packshots | Nada; §10.1 trata só de continuidade de estilo |
| Asset aprovado como referência de tecido | §10.1 permite como estilo, não como detalhe de produto |
| Montagem determinística de etiqueta pequena | §9.1 cobre logotipo plano, não etiqueta costurada |
| Verificação do desenho do tecido com zoom | Nada específico no QA Realism |
| Catálogo de estilos e recomendação | Nada |
| Escolha da direção pelo dono | O passo 3 do perfil Web é "uma direção provisória" do agente |
| Decisão registrada sobre a imagem principal | Nada |
| Registro de entrega que não pode ser pulado | Existe esquema e script, mas são opcionais na prática |
| Imagem colapsada no QA do runtime | Só imagem quebrada |
| Versões derivadas de imagem para web | Nada; "não editar pixels" foi lido como "não redimensionar" |

## 5. Backlog proposto

| # | Item | Área | Prioridade | Esforço | Depende de | Versão |
|---|---|---|---|---|---|---|
| 1 | Merge do runtime 2.6 (#17) | d | P0 | S | itens 2 a 4 | 2.6 |
| 2 | Verificação de imagem colapsada em `qa.py` (F-C1) | c | P0 | S | – | 2.6 |
| 3 | Normalização de texto no QA (F-C2) | c | P1 | S | – | 2.6 |
| 4 | Registro de entrega mínimo gerado pelo script; `file://` aceito como prévia (F-B4) | b | P0 | M | – | 2.6 |
| 5 | Notas técnicas do perfil Web: captura, `crossorigin`, rolagem (F-C3, F-C4) | b, c | P2 | S | – | 2.6 |
| 6 | Recorte obrigatório de referências (F-A2) | a | P0 | S | – | 2.6 (texto) |
| 7 | Regra de etiqueta pequena por montagem (F-A4) | a | P0 | S | – | 2.6 (texto) |
| 8 | Conflito entre fato declarado e foto (F-A7, F-E3) | a, e | P1 | S | – | 2.6 |
| 9 | Perfil `PRODUCT_CONTENT` com lista de fotos e série de packshots (F-A1, F-A5) | a | P1 | L | 6, 7 | 2.7 |
| 10 | Receita de pacote executado pelo dono (F-A6) | a | P1 | M | 9 | 2.7 |
| 11 | Verificação de tecido com zoom e asset aprovado como referência de tecido (F-A3) | a | P0/P1 | M | 9 | 2.7 |
| 12 | Catálogo de estilos v1 (F-B6) | b | P1 | L | pesquisa de estilos | 2.7 |
| 13 | Escolha da direção pelo dono com recomendação (F-B1) e decisão sobre imagem principal (F-B2) | b | P0/P1 | M | 12 | 2.7 |
| 14 | Perfil de preferências do dono com regra de conflito (F-B3) | b | P1 | S | 13 | 2.7 |
| 15 | Portar verificações genéricas do verificador comum para `qa.py` (F-C5) | c | P1 | M | 2 | 2.7 |
| 16 | Versões derivadas de imagem para web (F-B5) | b | P2 | S | – | 2.7 |
| 17 | Guia de benchmark e checklist de privacidade (F-E1, F-E2) | e | P1 | M | – | 2.7 |
| 18 | Script de montagem de etiqueta na skill (F-A4) | a | P2 | M | 7 | 3.0 |
| 19 | Recomendação automática de estilo avaliada por benchmark | b | P2 | L | 12, 13 | 3.0 |

**Com o PR #17 (2.6), entram os itens 1 a 8.** São correções de runtime pequenas e testáveis, mais regras de texto que nasceram de evidência direta. **Depois (2.7 em diante)** vêm os itens que pedem desenho novo: perfil de produto, catálogo e escolha de estilo, porte do verificador comum. Os branches de pesquisa (DQB-03 e comparação de prompts) entram como documentação no mesmo merge, sem material da Della.

## 6. Perguntas para o dono

1. **Aviso de IA no site:** as fotos de produto geradas por IA levam aviso? Está em aberto desde o pacote v2.
2. **Montagem de etiqueta:** a troca pela etiqueta real pode virar prática padrão da skill para material de marca?
3. **Forro da Croissant:** confirma que é creme liso? O briefing original dizia "com bolinhas".
4. **Preferências visuais:** valem como padrão para todos os seus projetos ou só para a Della?
5. **Recomendação de estilo:** a skill deve mostrar um estilo recomendado ou dois a três para você escolher?
6. **Versionamento:** fazemos agora o merge da 2.6 com os itens 1 a 8 e deixamos o resto para a 2.7?
