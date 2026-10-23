# Segurança de publicação e aprendizado contínuo · Proposta experimental

**Status:** candidato técnico, não aprovado na main.  
**Rastro:** [ADR-0003-PROPOSED](../docs/decisions/ADR-0003-PROPOSED-development-review-and-publication-safety.md). Complementa ADR-0001 (separação do Git público e material privado) e ADR-0002 (caminho mínimo por tarefa).

## O que este gate faz

O script `publication_guard.py` lê SOMENTE **linhas adicionadas num diff Git**, sem rede, sem pacotes externos e sem divulgar valores encontrados. Ele classifica:

- `BLOCK`: formatos reconhecíveis de chaves/tokens, bearer credentials, URLs com assinaturas de acesso, marcadores de private key e arquivos de credenciais como `.env` ou `.pem`.
- `REVIEW`: URLs de Google Drive/Docs (podem ser compartilhamentos legítimos ou privados), mídias e arquivos binários. Um alerta de Drive **não prova vazamento**.
- Saída sem o segredo, apresentando apenas regra e arquivo/posição de linha adicionada. Atenção: o próprio nome do arquivo pode carregar contexto sensível; usar nomes neutros desde a origem.

**Limites:** não procura exfiltração por base64 genérica/obfuscação, fotos com dados, texto confidencial sem marcadores, trechos em commits antigos, forks ou logs externos. A revisão humana continua obrigatória. O scanner CI funciona **depois do push**, por isso o uso local antes de publicar é indispensável.

## Rodar antes de um commit/push local

```sh
python security/publication_guard.py --staged
python -m unittest discover -s security -p 'test_*.py' -v
```

Opcionais, para revisão de branch e aviso estrito:

```sh
python security/publication_guard.py --range "origin/main...HEAD"
python security/publication_guard.py --staged --fail-on-warning
```

Na integração com GitHub connector, que não usa Git local, é obrigatório **inspecionar o conteúdo antes da ação de escrita**. Este guard não é automaticamente invocado pelo connector.

Exemplo de hook a ser instalado/manual: [pre-commit.example](pre-commit.example). Não sobrescrever hooks já existentes; integrar com o hook prévio, se necessário.

## Auditoria do histórico já testada

O novo [auditor de objetos Git alcançáveis](history_audit.py) percorre versões antigas de blobs textuais e mensagens de commit, agrega alertas sem mostrar valores, caminhos nem e-mails e marca mídia/binários para revisão separada.

O [resumo sanitizado da auditoria S0](../docs/security/S0-historical-audit-summary-2026-10-23.md) registra a primeira execução e suas limitações. A [auditoria ampliada de 21 branches e triagem binária](../docs/security/S0-extended-branch-and-binary-triage-2026-10-23.md) corrige a cobertura original, classifica metadados EXIF sem revelar valores e indica as revisões privadas ainda necessárias. Em execuções subsequentes, foram observadas referências de Drive/links compartilháveis e possível e-mail pessoal de autoria para **classificação privada**, nenhum padrão reconhecido `BLOCK`. Contagem por blob/versão não corresponde diretamente ao número de links únicos. Mídia não recebeu inspeção visual.

Para reproduzir localmente com os refs disponíveis:

```sh
git fetch --all --tags
python security/history_audit.py
```

Um retorno bem-sucedido não significa que o histórico foi limpo ou que permissões de URLs foram verificadas. O resultado resumido do CI não contém as URLs sensíveis. A análise de permissões reais e de conteúdo binário deve ser feita privadamente, antes de promover a ADR.

## Revisão privada dos links e materiais históricos

A [triagem S0 aprofundada](../docs/security/S0-local-private-link-review-2026-10-23.md) explica a diferença entre uma varredura pública com categorias sanitizadas e uma revisão efetiva de permissões na origem.

Num clone local controlado pelo proprietário, e **fora de qualquer CI ou terminal com logs compartilhados**, a ferramenta [private_triage.py](private_triage.py) pode gerar um JSON de revisão, protegido por permissões de arquivo e fora do repositório:

```sh
git fetch --no-tags --prune origin '+refs/heads/*:refs/remotes/origin/*'
python security/private_triage.py
```

O arquivo local contém URLs completas, caminhos históricos e candidatos de mídia: **NUNCA fazer upload, commit, anexar a PR ou compartilhar em chat**. A ferramenta se recusa a rodar no CI, impede destino dentro do Git e exige diretório com acesso restrito. Ela não consulta Google Drive, não altera ACLs e não comprova se um link realmente dá acesso.

Antes de uma conclusão de segurança, o proprietário deverá classificar os links diretamente na conta Google Drive, separar links públicos intencionais de compartilhamento indevido, verificar as mídias e avaliar o endereço de autoria Git. Se existir credencial/URL de acesso ativo publicada, priorizar revogação na origem.

O auditor [history_audit.py](history_audit.py) agora percorre **todas as árvores de commits alcançáveis** e conserva aliases de caminhos quando o mesmo blob foi reutilizado. Isso evita atribuir um link antigo a um único caminho arbitrário.

## Antes do merge

1. Conferir diff completo, não só scanner e tests.
2. Resolver qualquer `BLOCK` **antes de publicar** e quaisquer alertas já expostos com contenção apropriada.
3. Analisar manualmente `REVIEW`: ver URL/link em ambiente privado, permissões, finalidade e direitos, sem colar link/credencial em comentários públicos.
4. Revisar também commits anteriores, anexos binários, históricos e logs. Um commit removido do HEAD pode continuar acessível.
5. Verificar testes do **commit exato**, interferência com outras branches, autorização e licença; não interpretar CI verde como aprovação do projeto.

## Resposta a exposição

Se houver token/URL que concede acesso: **revogar/rotacionar primeiro na origem**, depois verificar histórico, forks/caches/logs, escopo e eventuais comunicações. Não publicar o valor do segredo nem materiais confidenciais no issue ou PR. Relatório detalhado de incidente fica em armazenamento privado.

## Cenários de regressão

Os testes usam exemplos construídos dinamicamente em memória. Verificam padrões bloqueantes, links para revisão, arquivos binários, conteúdos deletados, diff com vários arquivos, ausência de vazamento em stdout e diferenciação de falhas Git.

O workflow [publication-guard.yml](../.github/workflows/publication-guard.yml) testa estas regras e verifica o diff do PR. Quando e se for integrado à main, a política do repositório poderá exigir o check como condição de merge, após análise de falsos positivos e testes em PRs existentes.

**Este PR não substitui a auditoria inicial S0 do histórico público do repositório.** Essa auditoria deve ser tratada separadamente e relatada privadamente quando dados sensíveis forem encontrados.
