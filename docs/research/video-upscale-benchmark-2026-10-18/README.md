# Video upscale 480p → 1080p · Benchmark comercial vs. gratuito

**Data:** 2026-10-18
**Tipo:** documento de pesquisa. Não é implementação aprovada, mudança de canon nem certificação de qualidade.
**Relação com o canon:** traz evidência para `MEDIA_UPSCALE · Specialist Method v0.3` (`src/ai-creative-skill/references/AI_Creative_Skill_Method_Media_Upscale_v0.3.md`, seção *Known execution evidence and limits*) e para a linha **Upscale** da *Higgsfield Exit Coverage Matrix* (§16 de `AI_Media_Provider_Registry_v0.12.md`). As propostas de atualização estão na seção 9. Nada em `src/` foi alterado.
**Mídia:** nenhum vídeo, quadro ou recorte do projeto foi versionado aqui, porque este repositório é público. A mídia fica no armazenamento privado do projeto.

---

## 1. Pergunta

1. Um vídeo de IA gerado em 480p (9:16) deve ser ampliado para 1080p ou para 4K antes de ir para Reels, TikTok, Shorts ou LinkedIn?
2. O upscale comercial feito pelo Higgsfield ("Edit Video → Upscale") tem qualidade boa e fiel ao produto?
3. Uma ferramenta **gratuita** consegue chegar a uma qualidade próxima, igual ou superior?
4. Quanto custa cada caminho, e em que situação vale a pena revisitar a opção gratuita, local ou com GPU alugada na nuvem?

## 2. Material de teste

Anúncio lifestyle de produto: nécessaire de tecido (musselina com estampa de croissant, laço e etiqueta costurada com a marca), com uma persona num café.

| Medida | Fonte | Upscale Higgsfield |
|---|---:|---:|
| Quadro | 480 × 854 | **1078 × 1918** (não é exatamente 1080 × 1920) |
| Duração / FPS / quadros | 30,050 s / 24 / 721 | 30,050 s / 24 / 721 |
| Vídeo | H.264 High, ~1,19 Mbps | HEVC Main (`hevc_nvenc`), ~12,6 Mbps |
| Tamanho | 5,48 MB | 48,4 MB |
| Áudio | AAC LC ~254 kbps | idêntico (PCM correlação 1,0000, RMS 0) |

Dados técnicos vindos da auditoria de 2026-10-17 (FFprobe, FFmpeg, OpenCV, SSIM). Sem interpolação de FPS. SSIM médio ~0,945 após reduzir o upscale à resolução da fonte, o que indica preservação da cena, não qualidade estética.

## 3. Identificação do provider (lacuna anterior resolvida)

A auditoria de 2026-10-17 não conseguiu atribuir o motor, porque o campo "Select model" ficou em escolha automática. O histórico de jobs no Higgsfield (via MCP, `show_generations`) mostra:

```text
model: topaz_video
enhancement.model: slp-2.5        # Topaz Starlight Precise 2.5 (difusão)
width/height (fonte): 480 x 854
output_width/output_height: 1920 x 1080 (orientação invertida no registro; arquivo real 1078x1918)
frame_interpolation: null
input_video.type: video_job        # gerado no próprio Higgsfield (cinematic_studio_video_4_0)
custo informado pelo usuário: 39 créditos (30 s, 1080p)
```

**Conclusão:** a opção "Upscale" com modelo automático executou **Topaz Video, Starlight Precise 2.5**. A documentação da API Topaz marca esse modelo como *Deprecated*, então pode existir uma versão mais nova. **Lição de processo:** sempre registrar o modelo pelo histórico do job, porque a interface com seleção automática não mostra qual foi usado.

## 4. Benchmark gratuito: método

- **Host:** container Linux na nuvem, 2 vCPU, 7 GB RAM, **sem GPU**. PyTorch 2.14 CPU.
- **Rotas comparadas** (todas com saída exata de 1080 × 1920, Lanczos no ajuste final):
  - `Lanczos`: interpolação convencional, sem IA (controle).
  - `Real-ESRGAN realesr-general-x4v3` (SRVGGNetCompact, o mesmo tipo de rede da rota canônica `local.realesrgan.srvgg.*`).
  - `Real-ESRGAN RealESRGAN_x2plus` (RRDBNet ×2).
  - `Real-ESRGAN RealESRGAN_x4plus` (RRDBNet ×4).
  - `Topaz slp-2.5` (resultado do Higgsfield, redimensionado de 1078 × 1918 para 1080 × 1920 para alinhar os recortes).
- **Quadros:** 8,5 s (rosto em plano médio) e 13,8 s (produto em primeiro plano com etiqueta). Etiqueta do Topaz também em 12,5 / 13,2 / 13,8 / 14,5 / 15,2 s, para verificar estabilidade temporal.
- **Recortes:** rosto, olhos, tecido e etiqueta, lado a lado (`compare_crops.py`).
- Scripts nesta pasta: `sr_benchmark.py` (imagem ou vídeo, três modelos) e `compare_crops.py`. Os pesos não estão versionados (veja o docstring).

### Tempo de processamento (CPU, 2 vCPU, quadro 480 × 854)

| Modelo | s/quadro | Vídeo de 721 quadros |
|---|---:|---:|
| realesr-general-x4v3 | ~10 | ~2 h |
| RealESRGAN_x2plus | ~30 | ~6 h |
| RealESRGAN_x4plus | ~150 | ~30 h |

Inviável em CPU para produção. Em Apple Silicon (MPS) ou numa GPU NVIDIA, cai para frações de segundo ou poucos segundos por quadro. O canon registra um piloto Real-ESRGAN em Apple M1/MPS com 5 s, 480 × 854 → 1080 × 1922.

## 5. Resultados de fidelidade

| Região | Lanczos | Real-ESRGAN (3 modelos) | Topaz slp-2.5 |
|---|---|---|---|
| **Tecido** (produto) | macio, sem detalhe | **falha**: a musselina vira superfície lisa com linhas de grade desenhadas por cima (pior no x4plus) | preserva a textura amassada da musselina; é o melhor resultado |
| **Rosto / pele** | macio | pele lisa e "plástica", bordas nítidas, aspecto de IA | poros, cílios e sardas reconstruídos; aspecto fotográfico. **Atenção:** acrescenta sardas que mal aparecem na fonte, então conferir com a referência canônica da persona |
| **Etiqueta: palavra da marca** | legível | legível | legível e correta |
| **Etiqueta: linha da cidade** | ilegível (o formato lembra a palavra correta) | ilegível ou garbled | **texto nítido e errado** ("EBOLIN", "ESBLIN", "EABLIN") |
| **Etiqueta: estabilidade temporal** | estável | não medido em vídeo | **tremula**: a palavra inventada muda entre quadros |

**Causa raiz da etiqueta:** o gerador de vídeo já não renderizou a palavra correta em 480p. O upscaler de difusão apenas transformou o ruído em letras nítidas, e o resultado muda de quadro para quadro. Isso confirma a regra do canon: *"Upscaled text that looks clearer but is wrong fails brand authenticity."*

**Status sugerido para o master Topaz:** `TECHNICAL_QA_PASS` e fidelidade `PARTIAL` (etiqueta reprovada, pele a conferir). Fica `INTERNAL_PREVIEW_ONLY` até a etiqueta ser corrigida na finalização.

## 6. Custos

### Higgsfield (rota usada)

- Plano informado pelo usuário: **US$129/mês por 3.000 créditos**, ou ≈ **US$0,043/crédito**.
- Upscale 1080p de 30 s: 39 créditos ≈ **US$1,68** (≈ US$3,35 por minuto).
- 4K a partir da mesma fonte: 99 créditos ≈ **US$4,26**. Não recomendado (veja a seção 8).
- Custo real versus custo de oportunidade: se sobram créditos no fim do mês, o custo marginal do upscale é zero. Ele só pesa quando os créditos acabam antes do fim do mês.

### Topaz direto (estimativa)

A página da API (Starlight Precise 2.5) informa **26,0417 quadros por crédito em 1080p** e 11,9179 em 4K. Para 721 quadros, são ≈ **27,7 créditos**.

| Compra de créditos Topaz | US$/crédito | Custo deste vídeo |
|---|---:|---:|
| Assinatura 80/mês (US$9,99) | 0,125 | ≈ 3,46 |
| Assinatura 400/mês (US$39,99) | 0,100 | ≈ 2,77 |
| Assinatura 1.400/mês (US$99,99) | 0,071 | ≈ 1,97 |
| Assinatura 3.000/mês (US$199,99) | 0,066 | ≈ 1,83 |
| Assinatura 9.000/mês (US$499,99) | 0,055 | ≈ 1,52 |
| Pacote avulso 400 (US$78) | 0,195 | ≈ 5,40 |

**Ressalvas:** os créditos da API podem não equivaler aos créditos de cloud render do app. O custo varia com modelo, resolução e fps, e a Topaz recomenda conferir o orçamento no app. Preços consultados em 2026-10-18.

**Conclusão de custo:** para o volume atual, o Higgsfield sai igual ou mais barato. O Topaz direto só fica mais barato no plano de US$499/mês com uso total. A vantagem do Topaz direto não é preço: é ter controle explícito do modelo e um orçamento antes de renderizar.

## 7. Opções gratuitas e quando revisitar

| Opção | Tipo | Qualidade esperada | Requisito | Status |
|---|---|---|---|---|
| Real-ESRGAN (general-x4v3 / x2plus / x4plus) | GAN, quadro a quadro | abaixo do Topaz: textura de tecido destruída, pele plástica | CPU (lento) ou Apple MPS / NVIDIA | **testado** (quadros) |
| Upscayl (app Mac/Win/Linux) | interface para os mesmos modelos Real-ESRGAN (ncnn/Vulkan) | igual ao Real-ESRGAN | roda bem num Mac Apple Silicon | não testado; deve dar o mesmo resultado |
| **SeedVR2** (ByteDance Seed, Apache 2.0, nativo no ComfyUI) | difusão one-step para vídeo, variantes 3B e 7B (FP16/FP8/INT8) | **promessa** na mesma classe do Topaz Starlight | GPU NVIDIA com VRAM alta. A documentação não dá números exatos; o troubleshooting cita RTX 3090. Não roda de forma prática num MacBook Air | **não testado** |

### Por que o SeedVR2 não foi adotado agora

1. **Qualidade não comprovada** neste material: tecido, pele e principalmente o comportamento com texto na etiqueta (difusão tende a inventar letras, como o Topaz).
2. **Hardware:** o laptop do usuário não tem GPU suficiente, e este container não tem GPU.
3. **Custo real de alugar GPU:** o custo por hora de uma GPU alugada não foi pesquisado nesta sessão. A estimativa é que fique na mesma ordem de grandeza de um upscale no Higgsfield. O custo dominante é o **tempo de configuração e iteração** (ComfyUI, download de modelos, ajuste de parâmetros, novas rodadas), que hoje vale mais que a diferença de US$1–2 por vídeo.

### Gatilhos para revisitar

- Volume passar de **dezenas de vídeos por mês**, ou vídeos longos (minutos), em que o crédito por quadro pesa.
- Necessidade de sair do Higgsfield (linha *Upscale* da Exit Matrix).
- Acesso a uma GPU NVIDIA própria ou de baixo custo.
- Surgir uma versão do SeedVR2, ou de outro modelo aberto, que rode bem em Apple Silicon.

### Roteiro para um teste com GPU alugada (quando revisitar)

1. Alugar uma instância NVIDIA com VRAM alta (classe RTX 3090/4090 ou superior) e template de ComfyUI.
2. Instalar o SeedVR2 nativo do ComfyUI (ou `numz/ComfyUI-SeedVR2_VideoUpscaler`). Começar com **3B FP8**; comparar com 7B se a VRAM permitir.
3. Rodar **o mesmo clipe de 30 s** (480 × 854, 24 fps), alvo exato 1080 × 1920, sem interpolação.
4. Cronometrar o tempo total (setup + render) e anotar o custo/hora real.
5. Fazer a QA da seção 5 com `compare_crops.py`: tecido, rosto, etiqueta em 5 instantes. Comparar com Topaz slp-2.5.
6. Opcional no mesmo host: Real-ESRGAN em GPU, para medir a velocidade real e ter o vídeo completo.
7. Registrar o resultado aqui e atualizar o status da Exit Matrix só se passar no benchmark do projeto.

## 8. Recomendações operacionais

1. **Fonte 480p: upscale para 1080p, não para 4K.** De 480p para 4K é um fator de 4,5×, o que aumenta a alucinação, e Reels, TikTok e LinkedIn entregam em torno de 1080p. Exceção: no YouTube Shorts, o envio em 4K dá bitrate melhor. Nesse caso, faça o upscale de IA para 1080p e depois Lanczos sem IA para 2160 × 3840.
2. **Usar o Topaz slp-2.5 via Higgsfield** para material com textura de produto. Não usar Real-ESRGAN gratuito em vídeo de produto têxtil.
3. **Corrigir texto e etiqueta na finalização, não no upscale.** Fazer tracking da etiqueta e sobrepor a foto real autorizada, ou aplicar um desfoque leve só nela. Nenhum upscaler testado recupera texto pequeno correto.
4. **Gerar em resolução nativa maior** (720p/1080p) quando possível, e usar image-to-video com a foto real do produto como quadro inicial, para reduzir texto inventado na origem.
5. **Conferir a pele e as sardas da persona** contra a referência canônica após o upscale.
6. **Registrar sempre** modelo, versão, preset e créditos de cada job pelo histórico do provider.
7. Na reexportação, normalizar 1078 × 1918 para exatamente 1080 × 1920.

## 9. Propostas de atualização do canon (não aplicadas)

Ficam sujeitas à autoridade de mudança de canon (ADR-0001). Não aplicadas neste commit.

**`AI_Creative_Skill_Method_Media_Upscale_v0.3.md`, seção *Known execution evidence and limits*:** substituir *"exact provider/model variant and genuine label fidelity remain unverified"* por evidência equivalente a:

> 2026-10-18 benchmark: Higgsfield "Upscale" (auto model) executed Topaz Video Starlight Precise 2.5 (`slp-2.5`) for 30 s 480x854→1078x1918, 24 fps, audio identical. Textile and skin texture clearly superior to Real-ESRGAN (general-x4v3, x2plus, x4plus), which flattened muslin texture and produced plastic skin. Label secondary text FAILED: rendered sharp but wrong and temporally unstable (different invented words across frames). Result: TECHNICAL_QA_PASS, fidelity PARTIAL. See `docs/research/video-upscale-benchmark-2026-10-18/`.

**`AI_Media_Provider_Registry_v0.12.md`, §16, linha Upscale:**

| Capability | Higgsfield baseline | Alternative candidates | Current alternative evidence | Exit-ready |
|---|---|---|---|---|
| Upscale | empirical baseline = Topaz Starlight Precise 2.5 via Higgsfield | Topaz direct; SeedVR2 (open, GPU); Real-ESRGAN (open) | Real-ESRGAN: EMPIRICAL_FAIL on textile/skin fidelity (stills); Topaz direct: DOCUMENTED, priced, untested; SeedVR2: DOCUMENTED, untested | no |

## 10. Pendências

- [ ] A/B controlado no Higgsfield com modelo explícito (ByteDance `aigc` Pro, FLUX.3 Precise, Topaz) no mesmo clipe, para comparar com o resultado automático.
- [ ] Teste SeedVR2 em GPU alugada (roteiro da seção 7).
- [ ] Orçamento real do Topaz no app para o mesmo clipe, para confirmar a equivalência de créditos.
- [ ] Workflow de correção de etiqueta por tracking e sobreposição, documentado como rota de finalização.

## Fontes

- Auditoria técnica de 2026-10-17 (privada, armazenamento do projeto).
- Histórico de jobs do Higgsfield via MCP (`show_generations`), consultado em 2026-10-18.
- [Topaz Labs – Cloud Render (preços de créditos)](https://www.topazlabs.com/cloud-render)
- [Topaz Developer – Starlight Precise 2.5](https://developer.topazlabs.com/video-models/starlight/starlight-precise-2.5)
- [Magic Hour – Topaz Video pricing](https://magichour.ai/blog/topaz-video-ai-pricing) (terceiro; planos e créditos incluídos)
- [ComfyUI – SeedVR2](https://docs.comfy.org/tutorials/utility/seedvr2.md)
- [numz/ComfyUI-SeedVR2_VideoUpscaler](https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler)
- [xinntao/Real-ESRGAN (releases dos pesos)](https://github.com/xinntao/Real-ESRGAN/releases)
