# S0 · Consolidação da classificação textual e EXIF · 2026-10-23

**Status:** `S0_TEXTUAL_CANDIDATES_CLASSIFIED_TO_AVAILABLE_EVIDENCE / S0_MEDIA_RIGHTS_AND_AUTHOR_PRIVACY_OPEN`  
**Origem:** análise de 21 refs públicas atuais no PR #20. **Não é certificação geral de privacidade ou direitos.**  
**CI verificado:** [GitHub Actions, 73 testes PASS](https://github.com/bribeirobr25/ai-creative-skill/actions/runs/40006660415/job/120596191692). Três checks do HEAD do commit executado passaram.  
**Nota:** todo registro público usa somente categorias, contagens e links para documentos de método; nenhum endereço privado, e-mail pessoal, URL, valor EXIF ou ID de arquivo é reproduzido.

## 1. Reconciliação de alertas de links

Conforme [classificação histórica anterior](S0-historical-links-classified-2026-10-23.md):

| Classe | Resultado apoiado por evidência | Risco remanescente |
|---|---|---|
| Uma referência real a pasta do Google Drive na importação | Recurso identificado pela conexão autorizada; estado consultado `shared=false` e permissões somente de tipo `user`; nenhuma permissão `anyone` ou `domain` no retorno | Estado atual não atesta ACL antiga; publicação do ID pode não ser desejada, mesmo sem conceder acesso |
| Duas referências de Drive/Docs em arquivos antigos de teste | URLs de fixture incompletas, sem identificador de recurso | Nenhuma permissão real para verificar; não tratar como vazamento |
| Três URLs genéricas de download/compartilhamento | Host classificado como GitHub público, sem query token ou URL assinada observada | Direitos de conteúdo e eventual insegurança de download são análise distinta |
| Quatro matches Drive/Docs do histórico | Correspondem a três strings distintas, com repetição de uma referência | Contagens de blob não são contagens de recursos distintos |

**Conclusão limitada:** nenhum desses candidatos demonstrou compartilhamento público indevido na verificação disponível. Não houve alterações de permissões, credenciais ou histórico.

## 2. EXIF: revisão adicional de conteúdo sem emissão de valores

O scanner anterior via tags `Artist`, `Copyright` e `ImageDescription` em 27 versões de JPEG; 30 versões tinham algum EXIF. Ele foi estendido com um parser **limitado** a TIFF IFD e valores textuais ASCII/UNDEFINED dos campos selecionados. O parser não envia nem registra o texto: somente flags fixas de presença, e-mail/URL/número longo, truncamento/indeterminação.

**Resultado no CI do commit verificado:**
- `BINARY_EXIF_IDENTIFYING_VALUE_PRESENT: 27` (valores não vazios em 27 versões);
- não houve emissão de `BINARY_EXIF_EMAIL_LIKE_VALUE_NEEDS_REVIEW`, `BINARY_EXIF_URL_LIKE_VALUE_NEEDS_REVIEW` ou `BINARY_EXIF_LONG_NUMBER_LIKE_VALUE_NEEDS_REVIEW` nas versões examinadas;
- as tags de identificação existem e os valores **não foram publicados nem semanticamente aprovados**.

Isso **não** demonstra ausência de nomes de pessoas, créditos comerciais privados, descrições confidenciais, XMP, strings codificadas, EXIF fora do trecho amostrado, detalhes visuais nas imagens ou direitos autorais insuficientes. A inspeção visual anterior abrangeu **três** screenshots apenas.

## 3. E-mails em mensagens de commit: repetições separadas de identidades

A nova regra do guard marca e-mails candidatos de conteúdo, exceto domínios reservados de documentação e remetentes automáticos com `noreply`. Na inspeção do histórico alcançável:

| Evidência | Resultado |
|---|---:|
| Mensagens de commit com e-mail candidato | 22 |
| **Endereços candidatos distintos** nessas mensagens | **1** |
| Endereços de autoria Git fora da lista de `noreply` a revisar | 1 |

Não foram divulgados os endereços nem seus domínios. As 22 ocorrências não representam 22 identidades ou 22 vazamentos independentes. **É necessária decisão de privacidade do proprietário** quanto ao uso de e-mails públicos no histórico; não reescrever commits ou substituir atribuição sem necessidade fundamentada.

## 4. Segurança de novas publicações

- `publication_guard.py` sinaliza padrões de segredo (BLOCK), links do Drive e e-mails pessoais prováveis (REVIEW) sem imprimir o conteúdo nem nomes de arquivos sensíveis.
- A suíte passou **73 testes offline** no job citado. Diferenças do PR não emitiram bloqueios/avisos nesse commit.
- A auditoria verifica as heads públicas atuais do origin, percorre versões alcançáveis e conserva aliases de caminhos. Ela não alcança forks/caches, objetos órfãos ou servidores externos.
- `private_triage.py` continua disponível para avaliação sob controle do proprietário local, **não é executado em CI** e não foi usado para publicar links privados.

## 5. Status de fechamento e próxima decisão

| Item S0 | Estado |
|---|---|
| Links históricos encontrados pelo auditor | **Classificados com limite de evidência** |
| Pasta real Drive, permissão atual | **Restrita no metadata consultado** |
| Detecção de tokens padrões em blobs textuais | **0 padrões reconhecidos**, não garantia absoluta |
| EXIF: campos e classes de valor | **Triagem automatizada concluída**; sem aprovação semântica |
| E-mails de autoria/commit | **Um candidato único em mensagens e um de autoria a revisar**, sem aprovação do usuário |
| Inspeção visual completa, direitos de mídias | **PENDENTE** |
| Privacidade e conteúdo em forks/caches/objetos órfãos | **NÃO VERIFICADO** |
| Segurança preventiva obrigatória na `main` | **NÃO INSTALADA**; PR #20 permanece Draft |

**Decisão operacional:** não bloquear desenvolvimento matemático sintético do PR #19 por questões de mídia não relacionadas, mas manter o PR #20 em Draft e a promoção da ADR-0003 pendente até revisão de risco residual, pré-publicação local e decisão do proprietário. PR #17 permanece sob sua sessão responsável.

**Nenhuma exposição crítica foi confirmada pelos candidatos avaliados.** Isso é uma conclusão circunscrita, não a declaração de que o repositório inteiro está livre de informações sensíveis.
