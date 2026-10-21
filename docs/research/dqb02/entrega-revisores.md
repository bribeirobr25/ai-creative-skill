# DQB-02 — Como distribuir os pacotes aos revisores

**Envie os pacotes antes de compartilhar este repositório, o PR ou o relatório.** O relatório revela
condições e hipóteses; um revisor que o leia deixa de ser cego.

## Pacotes

- **Obrigatório:** `dqb02-pacotes-R0.zip`, com quatro pares (`B1-par1`, `B1-par2`, `B2-par1`, `B2-par2`).
  Cada pasta tem `index.html` (instruções, formulário e capturas) e os dois sites navegáveis `site-X/` e `site-Y/`.
- **Opcional, depois do R0:** `dqb02-pacotes-R1.zip`, mesma estrutura, para as versões revisadas.
- Os pacotes podem ser regenerados com `validation/dqb02/tools/build_review.py`; as chaves X/Y ficam só com a coordenação.

## Instruções para cada revisor

1. Descompactar e abrir `B1-par1/index.html` no navegador (funciona sem internet).
2. Usar os dois sites (X e Y) no desktop e numa janela estreita ou no celular, completando as tarefas do site.
3. Preencher, por dimensão, preferência (X, Y ou empate), notas 1–5 e justificativa citando uma tela.
4. Clicar em "Baixar respostas (JSON)" e enviar o arquivo à coordenação. Repetir para os outros três pares.
5. Responder sozinho, sem conversar com outros revisores e sem ler relatórios do estudo.

## Perfil

Pelo menos dois revisores independentes; idealmente um com experiência profissional em UI/design visual.
O proprietário do projeto pode revisar, mas já leu discussões sobre os resultados: isso deve ser marcado
como exposição prévia no formulário.

## Depois das respostas

Aplicar a regra de decisão congelada em `protocolo.md`, usando apenas os pares R0. Divergência entre revisores
conta como empate. Publicar as respostas brutas no armazenamento privado e somente agregados anonimizados no Git.
