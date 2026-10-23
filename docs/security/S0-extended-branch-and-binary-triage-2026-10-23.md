# S0 · Auditoria ampliada de branches e metadados · 2026-10-23

**Status:** TRIAGEM TÉCNICA AMPLIADA / REVISÃO MANUAL PRIVADA PENDENTE / NÃO CERTIFICADO  
**Owner:** PR #20, branch `proposal/reusable-development-security-gate-20261023`.  
**Evidência:** execução da tarefa `scan-publication-diff` no [GitHub Actions](https://github.com/bribeirobr25/ai-creative-skill/actions/runs/39948339311) referente ao commit de código de classificação, com resultados consultados diretamente no log. Números são de versões de objetos, não arquivos únicos, salvo indicação específica.

## 1. Correção de cobertura da auditoria

A versão anterior escaneava apenas refs já presentes no checkout. O workflow agora faz `git fetch` de todas as heads públicas no remoto, e `security/history_audit.py` exige correspondência de nome + SHA com o remoto (`git ls-remote --heads`) antes de entregar conclusão. Se alguma branch estiver faltando ou divergente, a auditoria falha.

**Branches públicas alcançadas e conferidas: 21.** Isso cobre os commits alcançáveis dessas heads no instante da execução, **não** blobs órfãos, históricos já reescritos, forks externos, caches, logs de terceiros ou branches excluídas antes da varredura.

## 2. Resultados observados na execução ampliada

| Categoria | Ocorrências/contagem | Interpretação correta |
|---|---:|---|
| Branch heads conferidas | 21 | Comparadas ao remoto atual |
| Blobs de texto analisados | 613 | Versões de conteúdos textuais UTF-8 dentro do limite |
| Blobs binários | 267 | Não receberam auditoria visual/semântica |
| Mensagens de commit | 148 | Metadados textuais alcançáveis |
| Padrões `BLOCK` reconhecidos | 0 | Não prova ausência absoluta de segredos |
| Referências a Google Drive/Docs | 4 | Resultados por blob-versão, não necessariamente quatro URLs diferentes |
| Link genérico compartilhável | 1 | Exige permissões e finalidade verificadas privadamente |
| Endereço de autoria para revisão | 1 | Não reproduzir endereço no GitHub |
| JPEGs | 256 | Versões de objetos, podem repetir uma mídia ao longo do histórico |
| JPEGs com marca EXIF | 30 | A presença de EXIF não prova exposição pessoal |
| JPEGs com tags EXIF potencialmente identificadoras | 27 | 27 caminhos distintos observados no conjunto examinado |
| URLs em namespace comum de metadados | 3 | Detectadas como namespaces padrões do tipo Adobe; não são por si só links privados |
| Tags de GPS apontadas pelo parser | 0 relatadas | **Não comprova ausência de localização ou outros metadados** |
| Outras categorias binárias | 11 | Requerem identificação/inspeção privada específica |

**Origem ampla dos cinco alertas de links:** três em versões de código/método-fonte, um em material de pesquisa e um em arquivos de teste. Essas categorias não divulgam caminhos, identificadores nem a URL encontrada. Elas não atestam a configuração atual de compartilhamento do Google Drive.

## 3. Prioridades de inspeção privada

**P0 imediato apenas se houver acesso indevido confirmado:** qualquer URL assinada/token ativo, pasta privada publicamente acessível por link ou arquivo com dados pessoais que não deveriam estar no repositório. Rotacionar/revogar **na origem**, sem publicar o valor nem reescrever histórico precipitadamente.

**P1 de classificação humana:**
1. Revisar o link compartilhável e os quatro achados de Drive/Docs com **conta proprietária**, checando se são exemplos, links de documentação pública ou recursos efetivamente compartilhados. Se houver permissões `anyoneWithLink`/públicas, confirmar intenção antes de alterar.
2. Revisar os **27 caminhos JPEG com tags potencialmente identificadoras**. Priorizar metadados de autor, descrição, copyright, câmera/serial, XMP e eventual inclusão de informações de projeto. O parser lê **IDs de tags, não valores**.
3. Revisar outros 11 objetos binários e mídia visual por rostos, credenciais em screenshots, QR codes, textos privados, direitos autorais e autorizações de projetos. Um scanner de assinatura não substitui análise visual.
4. Verificar se o e-mail Git commit author é um endereço que o proprietário aceita publicamente ou deseja substituir por noreply em futuros commits.

**P2 preventivo:** tornar a política de publicação da ADR-0003 efetiva somente após revisão e aceitação do proprietário, instalando preflight local ou outro mecanismo equivalente antes do primeiro push. CI pós-push é apenas segunda barreira.

## 4. Resultados que NÃO podemos afirmar

- Não afirmar `ALL_PUBLIC_REPO_FILES_SAFE`.
- Não concluir `DRIVE_LINKS_PRIVATE` ou `DRIVE_LINKS_PUBLIC` sem verificar permissões na origem.
- Não concluir `NO_PII_IN_IMAGES` só porque a inspeção de EXIF não identificou ponteiros GPS.
- Não tratar `27 caminhos EXIF` como 27 vazamentos.
- Não tratar `4 Drive matches` como quatro recursos distintos: são contagens de versões/arquivos no histórico.
- Não afirmar que o CI pós-push evita a primeira exposição de material recém-enviado.

## 5. Evidência técnica e próximos gates

A suíte do scanner executou **40 testes de controle sintético** com sucesso no commit de classificação (incluindo fetch de branch faltante, refs divergentes, metadados EXIF e URLs em namespace padrão). O guard do diff do próprio PR retornou `0 BLOCK / 0 REVIEW`. Esses PASS demonstram as invariantes testadas, **não** qualidade visual, privacidade real de links nem aceitação de norma.

**Saída:** `S0_AUTOMATED_HISTORY_COVERAGE_COMPLETE_FOR_CURRENT_PUBLIC_BRANCH_HEADS` e `S0_MANUAL_CLASSIFICATION_INCOMPLETE`. A ADR-0003 permanece **PROPOSED**. Não houve alteração de `main`, `src/` ou PR #17.

Registro anterior preservado: [resumo S0 inicial](S0-historical-audit-summary-2026-10-23.md), que tinha cobertura incompleta por não verificar todas as heads.
