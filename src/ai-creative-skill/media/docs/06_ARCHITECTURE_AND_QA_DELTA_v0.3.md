# Architecture Delta · Media Upscale v0.3 · Isolado

## Estratégia adotada
- Reutilizou `MediaRequest`, `run_image`, `neural_image`, `run_video`, `video_backend_v02`, SHAs e status de forma incremental. Não foi construída orquestração paralela para cloud.
- Acrescentou rota **local de vídeo neural** com `preflight_video_neural` → `neural_quote` → `run_neural_video` → inspeção técnica e ledger.
- Modelo `realesr-general-wdn-x4v3` (SRVGG, x4), WDN-only, conservador 35% sobre Lanczos. **Não é automaticamente o perfil D idêntico ao Work**, pois o Work processou 480p integral em MPS e esta rodada CPU usa fonte reduzida.
- O canal é local: nenhum URL/API key/credencial/transferência. Sem consentimento para cobranças. 0 de tarifa do provedor não equivale a custo operacional zero.
- Registro por capacidade: vídeo neural `EXECUTABLE_EXPERIMENTAL`, `quality_status=TECHNICAL_ONLY_VISUAL_REVIEW_REQUIRED`, no device CPU máximo 12 frames e fonte 128×128 (por área de pixels); devices GPU limites distintos. 5s max geral de candidata, não capacidade universal.
- Fonte e saída não podem se sobrescrever. Hash da fonte, pesos, implementação, ambiente de rota e parâmetros compõem o fingerprint. Em estado `UNKNOWN` ou artefato adulterado, a rota não é reenviada automaticamente.
- Audio copiado do arquivo original e comparado por PCM decodificado; frames verificados com FFprobe e decodificação integral; sem frame interpolation. FFmpeg transcodifica vídeo H.264, não possui método de super-resolução por si só.

## QA multi-tipo de imagem

| Classe | Entrada | Processamento | Evidência | Limite |
|---|---|---|---|---|
| Produto físico | Croissant real, recorte 96×120 | Lanczos e neural 35%, 192×240 | QA técnico PASS; painel comparativo | textura/estampa/etiqueta não certificadas |
| Personagem/rosto | Frame do comercial real, 96×120 | Lanczos e neural 35%, 192×240 | QA técnico PASS; painel comparativo | identidade/microtextura não certificadas |
| Editorial/storyboard | Trecho do storyboard Della aprovado, 96×120 | Lanczos e neural 35%, 192×240 | QA técnico PASS; painel comparativo | lettering/cor/layout final não certificados |
| Microtexto/etiqueta | Crop real Della 192×192, v0.2 | Lanczos e neural experimental | Evidência v0.2 preservada | texto pequeno não restaurado fielmente |
| Transparência | fixture alpha, v0.2 | Lanczos RGBA | regressão PASS | neural alpha ainda rejeitada |

Não há nota de melhoria perceptual baseada apenas em PSNR, Laplaciano, SSIM, tamanho do MP4, ou na posição do neural no painel. A política é preservar como hipótese até revisão humana e, para letras e marca, comparação canônica.

## Integração futura na V2.4
- Não adicionar novo Work Profile apenas para upscale. `MEDIA_UPSCALE` como operação de Media Postproduction, com rotas `IMAGE_UPSCALE` e `VIDEO_UPSCALE` no Provider Registry.
- Mapear novos tipos de request/quote/QA aos contratos existentes de `Execution Route Recipe`, `Route Compilation` e `QA_EVIDENCE_RIGHTS`, sem reimplementar política financeira geral nem escolher default obrigatório.
- `local.realesrgan.srvgg.video.v0.3` pode entrar como **rota candidata testada em CPU curto** somente com `quality_status=UNVERIFIED`, sem classificação `production_default`.
- Verificar adaptação real ao pacote e ativação em host limpo antes de promoção.

## Limitações reais
- Teste CPU curto não certifica reprodução dos cinco segundos em 480p integral; o Work executou MPS, mas essa modalidade não foi repetida neste runtime.
- Processamento neural é frame-by-frame, sem janela temporal, com risco de flicker em detalhes.
- Proteção de duplicação é de processo single-host via `flock`, não um serviço transacional distribuído.
- Mac/Windows podem precisar outro mecanismo de lock; dispositivo MPS não disponível neste container.
- Não há licença comercial atestada para todos os pesos de outros modelos; código Real-ESRGAN BSD-3-Clause, direitos dos materiais Della dependem do projeto.
- Não há vídeo 4K neural nem imagem 4K neural validada, apesar de registro flexível de dimensões.
- Não há endpoint pago/REST/MCP implantado nesta extensão; mocks permanecem mocks.
