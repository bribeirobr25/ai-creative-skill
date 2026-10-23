# S0 · Links históricos, caminhos reutilizados e revisão privada · 23/10/2026

**Estado:** TRIAGEM AUTOMATIZADA APROFUNDADA / CLASSIFICAÇÃO PRIVADA PENDENTE / NÃO APROVADO PARA MERGE.  
**Base:** branch de proposta do [PR #20](https://github.com/bribeirobr25/ai-creative-skill/pull/20).  
**Norma vigente:** ADR-0001. ADR-0003 permanece proposta.  
**Evidência:** GitHub Actions, `scan-publication-diff`, varredura de todas as heads públicas presentes ao executar o CI; resultados e números devem ser associados ao commit específico.

## 1. O que foi melhorado

- O scanner não depende mais do primeiro caminho que o comando `git rev-list --objects` escolhe para um blob. **Todas as árvores de commits alcançáveis** são percorridas, para preservar os diferentes caminhos em que o mesmo conteúdo foi utilizado.
- O auditor de links agora classifica formatos (pasta, arquivo, documento), sem mostrar URL, ID ou token. Uma mesma versão pode conter mais de um formato.
- Foi adicionada uma **ferramenta local e privada** `security/private_triage.py`, fora do workflow público: coleta as URLs/paths históricos apenas num JSON dentro de diretório temporário exclusivo com permissões restritivas. Ela **recusa execução no CI**, evita gravar dentro do clone Git e não imprime conteúdos no terminal. O arquivo **nunca deve ser enviado para GitHub, chat, CI, Drive compartilhado ou anexado a PR**.
- A ferramenta de triagem privada **não altera permissões do Google Drive nem prova se links concedem acesso**. A conferência das ACLs/permissões precisa ocorrer na origem sob conta autorizada do proprietário, respeitando o escopo da revisão.

## 2. Resultado agregado de classificação (evidência prévia do CI)

| Métrica | Observação |
|---|---|
| Branches públicas com HEADs conferidas | 21 |
| Versões de blob alcançáveis após correção de aliases | 887 na primeira execução desse novo algoritmo; número cresce com novos commits |
| Versões de conteúdo com vários caminhos | 104 na primeira execução |
| Aliases caminho × blob | 1.014 na primeira execução |
| Referências a Drive/Docs em blobs | 4 |
| Link genérico compartilhável | 1 |
| Formatos de link Drive observados nos blobs | 3 folder, 1 file, 1 document, com possível sobreposição |
| Padrões credenciais `BLOCK` detectados | 0 nas regras implementadas |
| Texto/binários | JPEG/EXIF e demais binários ainda requerem classificação manual de conteúdo e direitos |

Essas contagens **não são quantidades de recursos distintos verificados**. O auditor pode encontrar várias referências num blob ou a mesma referência em versões diferentes. O verificador não confirmou permissões dos documentos no Drive. Não afirmar “sem vazamento” nem “exposto” sem análise privada.

## 3. Caminho seguro para a revisão humana

Apenas num clone local e por operador autorizado:

```sh
git fetch --all --tags
python security/private_triage.py
```

**Não rodar em GitHub Actions.** O utilitário utiliza diretório temporário privado, não modifica os arquivos do projeto, não faz chamadas de rede para Google Drive e impede saída acidental no repositório. A revisão de cada URL deve ser feita em uma sessão privada da conta proprietária, checando se é exemplo, público intencional, compartilhado por link, restrito ou revogado. Classificar **sem reproduzir IDs** em comentários públicos.

Possíveis decisões internas:
- `NON_SENSITIVE_REFERENCE`: referência pública e intencional;
- `PRIVATE_BUT_NOT_ACCESS_GRANTING`: link sem acesso concedido, ainda avaliar conveniência de exposição de ID/estrutura;
- `ACCESS_GRANTING_UNINTENDED`: acesso indevido confirmado, exige contenção na fonte;
- `UNKNOWN_PERMISSIONS`: falta de autorização/metadados para confirmar compartilhamento.

Se uma credencial/URL de acesso válida tiver sido publicada, deve ser revogada/rotacionada na origem antes de tratar o histórico. Não reescrever histórico ou revogar acesso legítimo sem identificar o recurso e seus dependentes.

## 4. Critérios ainda pendentes

- Conferir permissões reais dos links sob conta proprietária. A simples detecção da URL não comprova exposição.
- Examinar visualmente as imagens/capturas relevantes, além das tags EXIF.
- Verificar metadados completos e autorização de imagem/marca/cliente para arquivos selecionados.
- Classificar possível endereço de autoria Git, conforme preferência de privacidade do proprietário.
- Avaliar riscos de histórico não alcançável, forks, mirrors e caches fora do checkout.
- Aprovar/instalar o gate antes de publicação. CI pós-push não substitui pré-publicação.

**Situação:** S0 automatizado ampliado, **S0 manual ainda aberto**. Não alterar `main`, PR #17, credenciais, permissões ou documentação canônica por inferência automática.

## 5. CI de verificação mais recente (23/10/2026, 16:02 UTC)

No [job de segurança do PR #20](https://github.com/bribeirobr25/ai-creative-skill/actions/runs/39983440088/job/120516374436), o HEAD testado apresentou **58 testes PASS**, `0 BLOCK / 0 REVIEW` **no diff novo**, 21 branch heads verificadas, 895 versões de blob histórico, 1.022 aliases de caminho, 104 blobs reutilizados em múltiplos caminhos e 628 blobs textuais inspecionados. Os alertas históricos de links permaneceram em **quatro referências a Drive/Docs e um link genérico compartilhável**, sem identificação pública dos recursos. Nenhuma análise de ACL do Google Drive nem inspeção visual de mídia foi concluída.

O utilitário local é opt-in e deve gerar conteúdo confidencial apenas no computador do responsável, fora do repositório. **Não foi executado neste ambiente**, e a avaliação privada S0 permanece aberta.
