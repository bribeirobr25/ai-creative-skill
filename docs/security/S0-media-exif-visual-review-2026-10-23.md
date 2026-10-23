# S0 · EXIF, inspeção visual amostral e precauções de mídia · 23/10/2026

**Estado:** TRIAGEM BINÁRIA AMPLIADA / METADADOS COMPLETOS E REVISÃO VISUAL GLOBAL PENDENTES.  
**Branch:** PR #20, proposta não canônica. Nenhum arquivo de imagem ou permissão foi alterado.  
**Fonte:** auditor histórico nos 21 heads públicos alcançáveis, binários examinados por assinatura e tags EXIF sem revelar valores. [Evidência de execução e testes](https://github.com/bribeirobr25/ai-creative-skill/actions/runs/39994741760/job/120555222613) (associar resultados ao SHA efetivamente testado).

## 1. Categorias observadas

| Categoria | Ocorrências em versões históricas |
|---|---:|
| JPEG | 256 |
| JPEG com marca EXIF | 30 |
| JPEG com Artist | 27 |
| JPEG com Copyright | 27 |
| JPEG com ImageDescription | 27 |
| JPEG com GPS pointer reconhecido | Nenhum sinalizado pelo classificador atual |
| JPEG com CameraOwnerName/CameraSerial reconhecidos | Nenhum sinalizado pelo classificador atual |
| URLs em cabeçalho JPEG classificadas como namespaces padronizados | 3 |

As contagens são de blobs/versionamentos históricos, não indivíduos, imagens correntes ou segredos. Os 27 caminhos identificados até aqui não implicam 27 exposições distintas. O parser lê IDs de tags EXIF; **não interpreta nem publica os valores de autor, copyright e descrição**. As tags podem representar autoria de ferramentas, crédito legítimo, pessoas ou outra documentação.

## 2. Amostra visual efetivamente examinada

Foi possível abrir três imagens públicas via GitHub como base64 numa sessão de inspeção, sem copiá-las ao repositório ou gerar novos arquivos distribuídos. As amostras representam comparações de layout de sites/protótipos e **não mostraram, à primeira vista, chaves, e-mails, documentos privados ou dados pessoais diretamente visíveis**. Esta observação é restrita às três imagens examinadas.

**Não atribuir esse resultado aos demais arquivos:** fotografias ou screenshots podem revelar texto, rostos, direitos de imagem e informações comerciais sem que EXIF ou regex identifiquem.

## 3. Controle preventivo adicional

O exemplo `security/pre-commit.example` passou a utilizar a modalidade **estrita** (`--fail-on-warning`) do `publication_guard.py`: arquivos binários, referências de Drive e conteúdos suspeitos exigem decisão humana antes de um commit/push local. O workflow de PR registra avisos e não substitui o preflight.

Não apagar automaticamente campos `Artist` e `Copyright`: alguns podem ser atribuição necessária a direitos de uso. Antes de publicar material com metadados, resolver licenciamento, proveniência e finalidade, e escolher tratamento apropriado. Uma remoção cega de EXIF não substitui avaliação de privacidade e pode comprometer rastreabilidade de licença.

## 4. Itens ainda não encerrados

- Revisão **privada dos valores** EXIF de Artist/Copyright/Description em mídia relevante, sem publicar conteúdo sensível no relatório.
- Conferência de conteúdo visual dos arquivos fora da amostra, principalmente capturas com dados, logos/identidades de clientes, rostos, QR codes, identificadores ou tokens.
- Revisão de direitos de mídia e disponibilização pública dos conjuntos de pesquisa.
- Definir aceitação da ADR-0003 e instalação de gate local antes de liberar merge; o pre-commit fornecido é apenas exemplo, não hook instalado.

**Veredito:** a auditoria automatizada e a amostra visual reduzem incertezas, mas **S0 ainda não recebeu clearance geral**.
