# DQB-02 — Emendas e desvios registrados

Nenhuma emenda alterou briefing, materiais, rubrica, regra de decisão ou metodologias depois do congelamento
(`ec6e8f6`). Registros por ordem cronológica:

1. **Seleção de assets (antes do congelamento).** Duas séries candidatas foram descartadas depois de inspeção
   visual: tubos de tinta com marcas reais visíveis e cerâmicas de artistas reais identificados. Apresentá-las
   como produtos de marca fictícia seria indevido. Também foram excluídas fotos de um café real (logo de
   terceiros visível) e uma foto com teclado ao fundo.
2. **Instrumento de evidência (antes de qualquer entrega).** O teste em fixtures mostrou um falso negativo
   (o Tab ao sair do documento era contado como foco invisível); corrigido no commit `63be9b8`.
3. **Sem acesso de escrita ao GitHub.** O pedido de acesso foi negado na sessão; a branch foi construída
   localmente e entregue como bundle para publicação pelo proprietário.
4. **Concorrência.** Em cada lote, duas execuções A e duas B rodaram simultaneamente; o R1 do B1 rodou
   junto com o R0 do B2. A disputa de CPU afeta os tempos de relógio das duas condições.
5. **Isolamento.** t92 relatou que um arquivo temporário seu, fora de `$RUN`, foi sobrescrito por outro
   processo (o `/tmp` do host é compartilhado). O script foi recriado dentro de `$RUN`. Nenhum executor
   relatou leitura cruzada; isso não equivale a monitoramento de acesso.
6. **Contrabalanceamento dos pacotes.** A primeira geração sorteou A como X em 3 de 4 pares. Corrigido antes
   da distribuição para exatamente 2 de 4, com sorteio de quais pares (`build_review.py`).
7. **Tamanho do repositório.** As cópias das fotos e fontes dentro de cada site foram omitidas do Git por serem
   byte-idênticas a `shared/`; `tools/restore_assets.py` as restaura e verifica todos os arquivos contra o
   registro de congelamento (16/16 idênticos).
8. **Rótulos de tempo.** "Tempo ativo" é autorrelato dos executores; os tempos comparados no relatório são de
   relógio, das notificações de cada agente. Para t19, a notificação do R0 chegou depois do envio do R1; o R1 foi
   calculado pela diferença entre as notificações cumulativas.
