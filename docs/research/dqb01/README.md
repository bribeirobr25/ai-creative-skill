# DQB-01 — Design Excellence Benchmark

**Em execução: preparação congelada e preflight concluído. Websites A/B ainda não
produzidos; não há vencedor nem comprovação de qualidade profissional.**

O usuário autorizou incorporar a revisão metodológica e iniciar o trabalho local
sem gerações pagas. O protocolo foi fixado no commit `881ca0b` antes das implementações.
Branch independente `research/design-excellence-dqb01`, baseada diretamente em main
`39a0bfa39270ea4b685b0f862e7dbf647cf81d77`. PRs anteriores permanecem inalterados.

## Documentos para o time

- [Missão revisada](missao-revisada.md)
- [Protocolo e critérios de decisão](protocolo.md)
- [Briefing NOMA, conteúdo e liberdade criativa](briefing.md)
- [Procedimento e ficha de avaliação humana](avaliacao-humana.md)
- [Higgsfield: workflow, custos e limites de comparação](higgsfield-preflight.md)
- [Inputs e reprodução](../../../validation/dqb01/README.md)
- [Resultado do preflight](../../../validation/dqb01/results/preflight-checks.json)

## O que já foi executado

1. Verificação do baseline remoto e do PR #10: continua aberto/draft, head `553e76c`,
   sem revisão registrada no momento da consulta.
2. Recuperação das conclusões locais dos estudos anteriores, sem repetir seus testes.
3. Inspeção do pacote website-builder Higgsfield 2.2.1 e metadados das ferramentas.
   A existência da skill foi confirmada; sua equivalência com o workflow do vídeo
   histórico não foi estabelecida.
4. Seleção e inspeção de fotografias licenciadas; exclusão prévia de uma foto
   com marca de terceiros visível. Três imagens comuns, com crédito e hash.
5. Congelamento dos inputs. **14 verificações de preflight passaram**:
   integridade dos sete inputs, decodificação/dimensões das três imagens,
   igualdade das cópias dos dois documentos, escopo de alterações e base independente.
   Esses checks não avaliam estética nem funcionamento de um website.
6. Cotação sem geração: uma imagem `gpt_image_2_5`, 3:2, custa 0,25 crédito nas
   configurações consultadas. Total do workflow C continua desconhecido.

## Execução pendente

A comparação A/B foi desenhada para sessões isoladas. As regras do host exigem
autorização explícita para delegar; a pergunta ao usuário está pendente.
Não substituir silenciosamente por duas versões escritas pelo mesmo coordenador,
que já conhece a metodologia e os achados anteriores. Isso invalidaria a alegação
de baseline independente.

Com autorização: dois executores, configuração herdada igual, sem histórico e sem
override de modelo, input comum, B com metodologia integrada. Congelar primeira
entrega, inspecionar, entregar feedback simétrico e preservar revisão separada.
Sem autorização: eventual execução pelo coordenador será somente piloto exploratório,
com essa limitação registrada, e não estimativa controlada do valor agregado.

C nativo: **NOT_RUN**, por incompatibilidade do fluxo documentado com geração paga/
deploy público e equivalência não estabelecida. Revisores: **AWAITING_HUMAN_REVIEW**,
zero respostas, fichas preparadas. Não há alegação de benchmark concluído.

## Hipótese a testar

A metodologia pode organizar escopo e proteger fidelidade sem elevar, por si só,
a maturidade visual. O experimento deve poder mostrar ganho, empate ou regressão.
Não estamos testando uma suposta superioridade predeterminada de B ou Higgsfield.
Nenhuma alteração canônica é recomendada como comprovada nesta etapa.

## Referências históricas

- [Issue #8](https://github.com/bribeirobr25/ai-creative-skill/issues/8)
- [PR #9](https://github.com/bribeirobr25/ai-creative-skill/pull/9)
- [PR #10](https://github.com/bribeirobr25/ai-creative-skill/pull/10)
- Relatório Higgsfield já entregue: snapshot local consultado; não houve nova
  consulta ao Drive nesta etapa. O relatório histórico não mede este briefing.
- [Licença das fotos](https://www.pexels.com/license/) e fontes específicas em
  [credits.json](../../../validation/dqb01/shared/assets/credits.json).
