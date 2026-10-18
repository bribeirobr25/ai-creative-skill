# AI Creative Skill · Media Upscale v0.3 · CANDIDATE EXPERIMENTAL

**Data:** 18/10/2026. **Escopo:** extensão isolada para teste; V2.4 e `00_ACTIVE` não modificados. **Nenhum consumo de créditos/API**.

## O que foi concretamente desenvolvido

1. Conservadas as rotas reais `IMAGE_UPSCALE` (Pillow Lanczos e Real-ESRGAN SRVGG) e `VIDEO_UPSCALE` (FFmpeg/Lanczos) da v0.2.
2. Registrada e **implementada** a rota `local.realesrgan.srvgg.video.v0.3` em `runtime/media_upscale_v03.py`, que executa super-resolução neural quadro a quadro por PyTorch + modelo oficial Real-ESRGAN, no dispositivo expressamente selecionado (`cpu`, `mps` ou `cuda`) se disponível.
3. Comportamento **provider-agnostic** para estas rotas **locais**, sem API ou ferramenta remota; outros provedores continuam apenas registros/mock. Não houve implementação de adapters comerciais nesta rodada.
4. Cotação e registro de custo incremental de fornecedor zero (computação/energia total **não mensurada**), hash de fonte/pesos/receita/registro, execução idempotente, erro `UNKNOWN` fail-closed, QA de áudio decodificado, FPS, quadros, duração, geometria e integridade de decodificação.
5. Teste em **trecho derivado de vídeo real Della** com 12 quadros de movimento, 24fps, áudio: **96×170 → 192×340**, 0,5 segundos, usando Real-ESRGAN WDN (`dn=0`) combinado com 65% Lanczos e 35% neural. Resultado técnico `PASS`, qualidade editorial **UNVERIFIED**. O vídeo foi reduzido para testar portabilidade CPU e **não** representa a qualidade em 480p→1080p nem 4K.
6. Testes de imagem em três conteúdos: produto, rosto/personagem e imagem editorial/storyboard, todos com baseline Lanczos e neural conservador. QA técnico `PASS`; **fidelidade visual não aprovada**.
7. **61/61 testes** na suite combinada de extensão v0.2, código v0.1 e v0.3, incluindo conservação de áudio, bloqueio de gasto, limite de device, estado desconhecido, adulteração, fonte preservada, fingerprint portátil e regressões.

## Executar (Python local)

Requisitos: Python 3.11+ compatível com dependências, FFmpeg/FFprobe, Pillow, NumPy, PyTorch; os pesos oficiais estão inclusos e **não** são baixados automaticamente.

```bash
python runtime/media_upscale_v03.py routes
python runtime/media_upscale_v03.py quote --kind VIDEO --route local.realesrgan.srvgg.video.v0.3 --source fixtures/v03/della_03A_short_480source_downscaled_96x170_0p5s.mp4 --width 192 --height 340 --device cpu --blend 0.35
python runtime/media_upscale_v03.py run --kind VIDEO --route local.realesrgan.srvgg.video.v0.3 --source fixtures/v03/della_03A_short_480source_downscaled_96x170_0p5s.mp4 --width 192 --height 340 --device cpu --blend 0.35 --output-dir outputs/minha_execucao
PYTHONPATH=runtime pytest -q tests/test_media_v02.py tests/test_media_v03.py upstream/video_upscale_provider_neutral_mvp_v0_1/tests/test_upscale.py
```

**Cuidado:** o retorno `TECHNICAL_QA_PASS` jamais deve ser promovido a `FIDELITY_PASS` ou a master de produção. A amostra curta usa redução prévia do 480p original, somente para provar a execução em CPU. Para processamento em resolução original, usar GPU/dispositivo apropriado e QA editorial com imagens reais da bolsa/etiqueta/personagens.

## Evidência anterior do Work

O Work executou Real-ESRGAN em Apple M1 MPS por 5 segundos (120 quadros, 480x854→1080x1922) e seu perfil D híbrido permaneceu `PARTIAL_VERIFIED` devido a pele/etiqueta. A rota v0.3 reproduz o mecanismo de **processamento local por quadro**, mas não reproduz automaticamente o output exato do Work, principalmente devido a modelo/pesos, dispositivo, blend, versões e fluxo de codificação.

## Artefatos

- `runtime/media_upscale_v03.py` e `runtime/media_upscale_v02.py`: executor, regras e importação das rotas anteriores.
- `registry/provider_capabilities_v0.3.json`: novos limites por rota, sem teto global único.
- `fixtures/v03/`: trechos derivados de mídias reais do usuário, com documentação de origem.
- `outputs/v03/`: resultados locais de teste, sem publicação comercial.
- `evidence/v03/`: matriz de imagens, QA e logs de testes.
- `docs/06_ARCHITECTURE_AND_QA_DELTA_v0.3.md`: análise das decisões e lacunas.
- `docs/07_VALIDATION_NEXT_GATE_v0.3.md`: requisitos para possível promoção.
- `MANIFEST_v0.3.json`: SHA-256 e bytes dos arquivos entregues.

Nenhuma instalação na V2.4 ou `00_ACTIVE` foi realizada.
