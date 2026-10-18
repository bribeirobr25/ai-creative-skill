# AI Creative Skill · WEB_EXPERIENCE MVP v0.2 · CANDIDATE

**Estado:** experimental / isolado / **NÃO INSTALADO NA V2.4** / nenhum deployment ou custo autorizado. Data: 18/10/2026.

## Resultado desta iteração

- Contrato de entrega tipado: `schemas/web_delivery_v0.2.schema.json`, com 6 famílias canônicas do MVP v0.1 e enums de estado/veredito.
- Validação de artefatos reais e relações entre estados, evidências, versão do build e autorizações: `runtime/validate.py`.
- Pré-roteamento por intenção e entregável: `runtime/router.py`. **Não é um modelo semântico nem ativação automática de uma skill instalada.**
- `PreviewAdapter` local com start/status/restart/stop e identificação do processo: `runtime/preview.py`. Servidor loopback somente, sem persistência prometida, sem encerrar processos alheios.
- QA com diagnóstico estático e tentativa opcional de navegador: `runtime/qa.py`. Inspeção de código não é promovida a teste efetivo de UX.
- Controle de PRESERVE/VARY por hashes de regiões, com invalidação quando CSS/JS compartilhado muda: `runtime/revision.py`.
- Migração **explícita** dos ZIPs da Della e diBoaS para registros candidatos v0.2: `runtime/migrate.py`. **Não** corrige retroativamente a conformidade das entregas v0.1.
- 35 testes unitários negativos/positivos; dois pilotos reavaliados sem alterar as versões anteriores.

## Execução básica (Python 3.11+; `pip install jsonschema beautifulsoup4`)

Partindo da raiz deste pacote:

```sh
python -m unittest discover -s tests -v
python -m runtime.cli route "crie uma landing para meu produto"
python -m runtime.cli preview start /CAMINHO/DO/SITE/dist
python -m runtime.cli preview status /CAMINHO/DO/SITE/dist
python -m runtime.cli audit /CAMINHO/DO/SITE/dist --output /CAMINHO/DO/SITE/dist/.web_mvp_v02_qa --url http://127.0.0.1:PORTA/
python -m runtime.cli preview stop /CAMINHO/DO/SITE/dist
python -m runtime.cli validate evidence/Della_migrated_v02.json --site-dir /CAMINHO/DO/SITE/dist
```

**Nota:** o pacote não redistribui os ZIPs de website, fontes ou imagens dos usuários; arquivos `evidence/*_migrated_v02.json` referem-se aos respectivos diretórios extraídos dos arquivos originais no Drive. As evidências de QA vivem ao lado de cada preview, por hashes. Caminhos de evidência são locais e relativos ao site original, portanto não dão prova autônoma sem os originais.

## Limites comprovados

1. Chromium bloqueou a navegação em `http://127.0.0.1` neste ambiente com `ERR_BLOCKED_BY_ADMINISTRATOR`; o HTTP healthcheck foi positivo. O browser QA destes dois casos permanece `NOT_TESTED`, não PASS.
2. Não houve agente novo executando `WEB_EXPERIENCE` como módulo integrado. O router executado é determinístico e ainda exige um host/agente para produzir o HTML/CSS/JS.
3. Não houve teste em usuário real, dispositivo físico, leitor de tela ou comparação criativa cega.
4. A alteração localizada foi simulada numa cópia de código Della; **não foi uma edição solicitada ou aprovada pelo usuário**. Hash de HTML/CSS não certifica pixels nem comportamento de navegador.
5. Reabrir preview em host efêmero só é possível quando os arquivos e o ambiente persistem; nenhum link público foi criado.

## Integração futura

Manter a extensão isolada como Work Profile/capability candidate. Primeiro resolver o teste de navegador em host compatível, carregar `WEB_PREVIEW/WEB_EDIT` em sessão limpa via adaptador real e executar revisão humana localizada. A instalação/promoção de V2.4/`00_ACTIVE` exigirá aprovação separada.
