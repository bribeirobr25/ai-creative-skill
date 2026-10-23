# S0 · Consolidação da classificação textual e EXIF · 2026-10-23

**Status atual:** `S0_CLOSED_BY_OWNER_ATTESTATION_WITH_RESIDUAL_LIMITATIONS` (adendo §7). Os achados históricos abaixo preservam as limitações técnicas e a situação anterior ao encerramento administrativo.  
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

## 6. Verificação complementar de autoria em commits

Uma extensão posterior do auditor classificou a **posição** dos e-mails nas mensagens de commit sem emitir seus valores. O [job verificado com 74 testes PASS](https://github.com/bribeirobr25/ai-creative-skill/actions/runs/40007350647/job/120598524690) observou:

- **22 linhas de coautoria** (`Co-authored-by`) com endereço candidato, correspondendo a **um único endereço distinto**;
- nenhum alerta de e-mail de mensagem fora de trailers de coautoria nas regras aplicadas à execução;
- continua havendo **um endereço de autoria Git** para revisão independente.

Isso reclassifica as 22 ocorrências: **são atribuições técnicas repetidas de coautoria, não 22 documentos com e-mail pessoal**. Mesmo assim, a publicação do endereço no histórico é um fato que exige avaliar intenção e privacidade. Não remover coautoria nem alterar commits retroativamente sem aprovação e análise de impacto.

O check de diff do mesmo job retornou `0 BLOCK / 0 REVIEW` para as linhas novas examinadas. Esse número não apaga nem ignora os alertas históricos já classificados.

**O primeiro job de 73 testes citado no início continua sendo evidência do commit anterior. A evidência de execução mais recente desta revisão é o job de 74 testes acima.**

## 7. Encerramento da fase S0 por declaração do proprietário · 23/10/2026

**Decisão registrada:** `S0_CLOSED_BY_OWNER_ATTESTATION_WITH_RESIDUAL_LIMITATIONS`. O proprietário declarou que os materiais de mídia sob sua responsabilidade são **imagens/vídeos gerados com IA ou fotografias/vídeos captados por ele**, e que os **textos são de sua própria autoria**. Pediu expressamente o encerramento desta fase de revisão. Essa declaração é registrada como **atestação de proveniência/autoria do proprietário**, não como inspeção independente arquivo a arquivo nem parecer de licença.

**Tratamento:** a revisão aprofundada de autoria e proveniência das mídias/textos existentes deixa de ser bloqueio **para encerrar a triagem S0 administrativa**. Não houve nova inspeção visual global nem leitura semântica dos valores EXIF. O histórico já documentado sobre links/branches, as limitações dos scanners e os resultados de CI permanecem preservados.

**Riscos residuais não certificados:** direitos de eventuais elementos de terceiros presentes em conteúdos gerados por IA ou nas gravações (pessoas, marcas, música etc.), termos das ferramentas utilizadas, dados privados acidentais em pixels/EXIF, histórico de acesso a links, endereço de autoria/coautoria em metadados Git e superfícies externas (forks/caches). A declaração de autoria **não equivale** a autorização para tornar público um e-mail pessoal. Esses riscos ficam registrados, mas a fase S0 não será mantida aberta indefinidamente apenas por falta de inspeção exaustiva.

**Separação de gates:** encerrar S0 **não aprova** a ADR-0003, não ativa o preflight antes do push, não libera automaticamente merge do PR #20, não altera `main`, não autoriza APIs/dados reais de Intelligence e não dispensa verificação de novas publicações. Se surgir evidência concreta de exposição, reabrir a investigação pontual e conter o risco na origem.

**Fonte da decisão:** manifestação expressa do proprietário nesta conversa, em 23/10/2026. Sem publicar URLs, imagens, e-mails ou metadados identificadores.
