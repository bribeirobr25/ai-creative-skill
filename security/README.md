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
