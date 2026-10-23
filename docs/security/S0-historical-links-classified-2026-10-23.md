# S0 · Classificação dos links históricos e permissões atuais · 2026-10-23

**Status:** `LINK_TRIAGE_COMPLETED_FOR_FOUND_CANDIDATES / GLOBAL_S0_MANUAL_REVIEW_OPEN`.  
**PR:** [#20](https://github.com/bribeirobr25/ai-creative-skill/pull/20).  
**Evidência de CI:** varredura de refs atuais do repositório público, com preservação de todos os aliases de caminhos; [job de auditoria e testes](https://github.com/bribeirobr25/ai-creative-skill/actions/runs/39984767026). Revisões reais foram realizadas por leituras autorizadas, sem logs de URLs ou IDs.

## 1. Descoberta: correspondências não significam recursos diferentes

A revisão inicial identificara quatro ocorrências de strings com formato de Drive/Docs. O auditor atualizado contabilizou **três strings distintas** em versões históricas de blobs. Elas foram classificadas sem divulgar seu conteúdo:

| Registro anonimizado | Tipo | Classificação comprovada | Limitação |
|---|---|---|---|
| L-01 | Referência a pasta do Drive da importação inicial da skill | **Recurso identificável e acessível pela conta conectada.** Consulta `get_file_metadata` obteve `shared=false`, lista de permissões retornada contendo somente `user`, sem permissão `anyone` ou `domain` no metadata consultado | Confirma **estado atual**, não a ACL histórica nem se a publicação do ID era intencional |
| L-02 | URL de arquivo do Drive em versão antiga de teste do guard | **Fixture incompleta**, terminando no prefixo do ID sem identificador de recurso | Não representa recurso verificável; não fazer consulta de permissão |
| L-03 | URL de Google Docs em versão antiga de teste do guard | **Fixture incompleta**, terminando no prefixo do ID sem identificador de recurso | Não representa recurso verificável; não fazer consulta de permissão |

As duas referências incompletas foram confirmadas pela leitura da versão inicial do arquivo de testes no próprio GitHub, sem emitir seus valores. Referências posteriormente recompostas por concatenação não deixam strings completas diretamente visíveis no código, mas o histórico permanece acessível.

O indicador público `LINK_INCOMPLETE_OR_PLACEHOLDER_IDENTIFIER` agrega categorias **por blob**, e por isso pode contar as duas fixtures presentes no mesmo blob apenas uma vez. Isso não é evidência de um quarto recurso.

## 2. Links genéricos de compartilhamento/download

O auditor encontrou **três strings distintas**, todas classificadas no bucket de hostname **GitHub público**; zero em Google Storage e zero em hosts desconhecidos. Não foi encontrado indicador de token/signed query nos exemplos inspecionados. A categoria antiga `REVIEW:SHAREABLE_STORAGE_LINK=1` é **por blob**, não por URL.

**Veredito de privacidade para esta classe:** referências a downloads públicos do GitHub, não evidência de que arquivos privados do Drive estejam sendo compartilhados. O conteúdo, licença e confiabilidade dos downloads são outra questão, fora desta verificação de link.

## 3. Medidas tomadas e não tomadas

- **Executado:** detecção de strings distintas, confirmação do exemplo incompleto via commit histórico, leitura de permissão atual de L-01 pela conexão Drive autorizada, separação de links genéricos por domínio e inclusão de testes.
- **Não executado:** exposição dos links/IDs em PR, alteração de ACL, revogação, reescrita do histórico Git, inspeção visual de mídia, consulta de histórico de permissões do Drive, análise de acesso por terceiros no passado.
- **Decisão:** os alertas de texto acima estão **classificados até o limite da evidência**. Não há confirmação de link que conceda acesso público indevido no estado atual consultado.

## 4. Pendências para encerrar a auditoria S0 geral

1. Avaliar privadamente se o ID de L-01 deveria constar em histórico público, mesmo com permissão restrita, e decidir se vale intervenção. Não alterar histórico sem necessidade comprovada.
2. Inspecionar imagens/binários e valores EXIF quando autorizados; a análise atual só registrou presença de tags e classes de URLs de metadados.
3. Confirmar se o endereço de autoria Git não-noreply está de acordo com a preferência de privacidade do proprietário.
4. Rever forks/caches/commits não alcançáveis e controles locais de pré-publicação; a ADR-0003 permanece **PROPOSED**.

**Resultado:** risco de compartilhamento **por esses links** reduzido e classificado. Não concluir `WHOLE_REPO_CONFIDENTIALITY_CERTIFIED`.
