# Delta da v0.1 para v0.2 · execução concreta

## P0 implementado nesta branch

| Problema real dos pilotos | Mudança no candidato | Evidência / limite |
|---|---|---|
| Campos e estados divergentes | JSON Schema 2020-12 + enum único e validação cruzada | Della e diBoaS reclassificados em novos registros; os originais continuam NÃO conformes |
| Agente consultou spec e declarou método executado | `execution_mode`, `methods[].state`, `activation_evidence`; gate rejeita declaração WEB_MODULE_EXECUTED sem prova/instalação | Teste unitário; **integração a host não executada** |
| Preview morreu entre sessões | start/health/status/restart/stop + pid/token + arquivo de ownership | Preview real via HTTP, reiniciado após stop; não persistência entre hosts |
| QA textual sem evidência por requisito | `checks[]`: check_id, modo, resultado, arquivo, hash, viewport, data | 12 verificações/caso: 3 STATIC PASS, 9 NOT_TESTED; navegador bloqueado |
| Divergências nos nomes de W1/W3 | `BRIEF_RECOVERED` e `DIRECTION_PROVISIONAL` como vocabulário único | v0.1 preservada; não realizar migração silenciosa |

## P1 parcialmente implementado

- Cada asset da nova migração contém `origin`, `approval`, `rights`, `use_scope`. Isso não concede licença nem transforma `LEGACY` em `APPROVED`.
- Formulários: `NONE`, `LOCAL_CALCULATION`, `EXTERNAL_SUBMISSION`, `MOCK_INPUT`, com regra de não tratar cálculo local como captura real de lead.
- Revisão: algoritmo `snapshot/compare` detecta alteração de regiões protegidas e CSS/JS compartilhado. Simulação Della hero-only passa na checagem **estática**. Não substitui navegador, aprovação de usuário nem controle visual.

## Próximos gates (não concluídos)

- **G2 Host + navegador:** executar site com screenshots desktop e mobile, comportamento de CTA/teclado e reduced motion quando suportado, evidência ligada ao build hash.
- **G2 Router real:** request sem colar prompt inteiro deve ser interpretado pelo host/agente carregando a capacidade, build efetivo e preview; o CLI `route` não é suficiente.
- **G4 Revision:** usuário aprova regiões e solicita alteração; executar e comparar código, imagens e comportamento na mesma viewport; preservar CSS compartilhado.
- **G3 Generalização:** novo serviço/creator com poucos ativos canônicos, sessão limpa e Sites opcional.
- **G5 Criatividade:** comparação com mesmo contexto/ferramentas e avaliação humana cega. Sem métricas reais de conversão ou publicação implícita.

## Segurança e alcance

- Preview local está ligado a `127.0.0.1` e serve somente pasta do site; caminhos iniciados por `.` são bloqueados. O helper usa apenas uma porta livre, não encerra servidor não identificado.
- `URL` pode não ser acessível em navegador gerenciado mesmo com HTTP local saudável. HTTP 200 é pré-requisito, não prova de interação.
- Dados confidenciais, fontes, chaves e ativos de terceiro não devem ser introduzidos no pacote. O helper não executa deploy, não cria pagamentos nem conecta formulários.
- O campo de autorização de publicação só pode ser definido a partir de aprovação humana verificável. Em offline validation, `PREVIEW_ACCEPTED` é bloqueado conservadoramente.
