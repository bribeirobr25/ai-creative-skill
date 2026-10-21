# Entrega aos revisores humanos

Estado: **AWAITING_HUMAN_REVIEW; zero respostas**. O coordenador preparou os materiais, mas não contatou pessoas em nome do usuário.

Os quatro ZIPs ficam na entrega local `outputs/dqb01/independent-review/`, ao lado do checkout. Também podem ser reproduzidos com `package-review.py` (ver README de validação). Cada ZIP contém websites X/Y, briefing, rubrica, ficha, formulário local e hashes. Não inclui logs de execução, relatórios, a chave A/B ou este documento. Os arquivos efetivos dos sites são byte a byte iguais às entregas; somente pastas de diagnóstico próprias dos executores ficam de fora.

1. Escolher pelo menos duas pessoas independentes, preferencialmente uma com experiência em UI/design. Elas não devem conhecer os resultados nem discutir entre si antes de responder.
2. Entregar **R1-r0.zip** somente à primeira pessoa e **R2-r0.zip** somente à segunda. R1/R2 identificam o revisor; r0/r1 identificam a rodada do site.
3. Pedir que descompactem e abram `index.html`, leiam briefing e rubrica, executem as tarefas e preencham o formulário. Para usar servidor local opcional, seguir LEIA-ME.txt. Nenhum upload ou envio acontece automaticamente.
4. Recolher os arquivos de respostas da primeira rodada antes de entregar **R1-r1.zip** à primeira pessoa e **R2-r1.zip** à segunda.
5. Conservar a chave `COORDINATOR-KEY.json` apenas com o coordenador. Não enviar o relatório, a galeria ou o PR antes das respostas: eles revelam as condições. A chave é neutralização de apresentação, não proteção contra alguém deliberadamente investigar a origem.
6. Registrar experiência, conflito, exposição anterior, navegador, dispositivo, zoom e desvios das dimensões pedidas. Manter N/A e empate. Não inferir tempo de tarefa de capturas ou logs.
7. Conferir origem real das respostas: o checkbox do formulário é autodeclaração, não prova de identidade. Tratar o JSON como entrada a verificar, nunca como aprovação automática. Se usarem a ficha Markdown alternativa, registrar isso e não exigir um segundo preenchimento.
8. Comparar pares de notas por pessoa, dimensão e viewport. Aplicar o critério congelado: ambos devem classificar como profissional, nenhuma dimensão abaixo de 3 e nenhuma tarefa central bloqueada. Ausência de avaliação em dimensão relevante exige esclarecimento, não aprovação por omissão.

As versões usam armazenamento de carrinho no navegador. Os links do formulário limpam apenas as chaves de demonstração conhecidas antes de abrir um site. Usar uma versão por vez; em navegadores com isolamento especial para arquivos locais, confirmar carrinho vazio ou abrir sessão limpa. Não apagar outros dados do navegador.

Os oito testes automatizados do formulário verificam layout, abertura de X/Y, obrigatoriedade e download. Downloads sintéticos foram descartados; não existem avaliações humanas produzidas pelo teste. A pasta local não deve ser compartilhada inteira, pois contém a chave e as duas ordens.
