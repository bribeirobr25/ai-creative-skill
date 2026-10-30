# AI Creative Skill · MEDIA_UPSCALE v0.2 · EXPERIMENTAL

Data: 2026-10-18. Estado: **CANDIDATE ISOLADA, NÃO INTEGRADA À V2.4 NEM AO 00_ACTIVE.**

## Objetivo e resultados

A extensão acrescenta `IMAGE_UPSCALE`, negocia as dimensões por capacidade específica da rota e registra formalmente a rota neural do vídeo executada pelo Work na Della. Reutiliza o MVP v0.1 para execução de vídeo via FFmpeg, sem criar uma nova orquestração para produção.

**Implementado e executado neste ambiente:**
- Imagem real Della Croissant **1200×1600 → 2400×3200 e 2880×3840**, PIL/Lanczos, PNG, com QA técnico aprovado.
- Crops Della **128×128 → 512×512** e etiqueta **192×192 → 768×768**, Real-ESRGAN SRVGG local em CPU, modelo WDN `dn=0`, 35% resultado neural / 65% Lanczos. QA técnico aprovado; **qualidade visual/etiqueta não aprovada**.
- Vídeo sintético real do MVP v0.1, FFmpeg, 24 FPS e áudio original: execução v0.2 pequena e reutilização idempotente verificadas.
- `IMAGE` 6144×8192 (8K aproximado) e `VIDEO` 2160×3844 e 7680×4320: **cotações/preflight aceitos**, não provas de render neural nessas dimensões.
- 41 testes automatizados aprovados: 26 novos + 15 regressões do MVP v0.1.

**Registrado, mas não implementado de modo genérico neste pacote:**
- `local.realesrgan.srvgg.mps.video.v0.2`: Work executou 5s reais da Della num Mac M1, 1080×1922, 24 FPS, resultado visual `PARTIAL_VERIFIED`. O pacote v0.2 registra origem/limites e não afirma que este host possa executar esse backend. Fonte: <private-archive://media-evidence/realesrgan-mps-video-v0.2>.
- Vídeo neural em 4K, imagem neural em 4K e 8K, QA temporal integral, reconhecimento exato do lettering: **não validados**.

## Execução sem APIs e sem custos por inferência

No diretório extraído:

```bash
python runtime/media_upscale_v02.py routes
python runtime/media_upscale_v02.py quote --source fixtures/della_croissant_real_studio_SOURCE.jpg --width 2400 --height 3200
python runtime/media_upscale_v02.py run --source fixtures/della_croissant_real_studio_SOURCE.jpg --width 2400 --height 3200 --output-dir outputs/minha_execucao
python runtime/media_upscale_v02.py run --source fixtures/della_label_192px_crop.png --width 768 --height 768 --route local.realesrgan.srvgg.image.v0.2 --device cpu --blend 0.35 --output-dir outputs/meu_neural
```

Requisitos testados aqui: Python, Pillow, numpy, pytest; rota neural local usa PyTorch + dois pesos oficiais incluídos. Rota vídeo requer FFmpeg/ffprobe e H.264 libx264. A versão do Python, hardware e bibliotecas do host precisam ser confirmados em cada execução; GPU Metal/MPS foi validada **no Work anterior**, não neste runtime.

## Estrutura

- `runtime/media_upscale_v02.py`: contrato de entrada/cotação, seleção por rota, QA e ledger de imagem, execução local de imagem.
- `runtime/video_backend_v02.py`: cópia evoluída do executor FFmpeg anterior, com limite de pixels derivado do Registry. Usada por `run_video`.
- `runtime/srvgg_arch.py`: SRVGG da origem Real-ESRGAN (BSD-3-Clause, licença em `runtime/LICENSE_RealESRGAN`).
- `registry/provider_capabilities_v0.2.json`: capacidades por rota, estados de verificação, limites de pixels e requisitos.
- `models/`: pesos oficiais do Work, SHA-256 no manifesto. Não há download implícito de pesos em runtime.
- `tests/` + `upstream/`: testes novos e regressões da V0.1.
- `evidence/`, `outputs/`, `fixtures/`: provas técnicas, comparações, fonte Della e resultados.
- `docs/`: contratos, gaps, riscos, gates para futura integração.

## Limites/segurança

- Saídas jamais sobrescrevem a fonte e passam por fingerprint/hash com fail-closed para `UNKNOWN` ou artefato adulterado.
- Sem URL arbitrária, sem upload a terceiros, sem assinatura, sem rede dentro da execução, sem compra de créditos.
- `cash_incremental=0` significa tarifa de provedor nula; energia, computação, armazenamento e tempo **não** foram precificados.
- A imagem é orientada conforme EXIF antes do processamento, ICC é preservado quando presente e EXIF é omitido da derivada por privacidade.
- `TECHNICAL_QA_PASS` **não certifica** textura real, marca, microtexto, rosto ou fidelidade comercial. Original Della e referências devem prevalecer.
- Nenhuma variante é `production_default`; sem promoção à V2.4 ou `00_ACTIVE`.
