# R1 · Quality Gate: Media Reframe, profissional vs técnico

**2026-10-20 · Pesquisa/teste de qualidade; NÃO é certificação comercial, alteração da V2.5 ou release.**
**PR de trabalho:** #2 (draft); único código adicionado à branch é de pesquisa e ensaio sintético.

## 1. Resultado e critério epistemológico

Pillow e FFmpeg são tecnicamente capazes de reframe de qualidade profissional **sob condições de resolução, composição e exportação adequadas**. Não são garantia universal. Eles não criam detalhes ausentes por apenas fazer upscale ou resize. A aprovação exige separar:

- **TECHNICALLY_EXECUTED:** operação e testes técnicos reproduzidos;
- **PRODUCTION_CANDIDATE:** testado em material real/autorizado com QA editorial documentado;
- **PRODUCTION_APPROVED_FOR_SCOPE:** combinação exata de fonte, método, formato, campanha e destino aceita por humano. **Não alcançado neste R1.**

## 2. Teste gratuito realizado, sem mídia privada

Código: [r1_quality_benchmark.py](./r1_quality_benchmark.py). Fonte sintética 3840×2160, com texturas de alta frequência, microtexto, representação de produto e segundo sujeito propositalmente deslocado. Fontes de resolução mais baixa foram geradas por redução da mesma imagem 4K. Foi aplicado recorte 9:16 e saída 1080×1920. A referência é o mesmo recorte obtido a partir da fonte 4K, com geometria equivalente, **não um novo vídeo vertical filmado profissionalmente**.

Ambiente local: Pillow 12.3.0, NumPy 2.3.5, FFmpeg 7.1.5. Custos comerciais e APIs externas: **zero**.

| Fonte | Crop útil | Ampliação linear | PSNR geral vs 4K | PSNR ROI produto | PSNR ROI microtexto |
|---|---|---:|---:|---:|---:|
| 4K | 1215×2160 | 0,889× (redução) | Idêntico à referência | Idêntico | Idêntico |
| 1080p | 608×1080 | 1,778× | 33,018 dB | 28,033 dB | 24,043 dB |
| 720p | 405×720 | 2,667× | 29,556 dB | 24,617 dB | 21,180 dB |
| 480p | 270×480 | 4,000× | 27,614 dB | 22,707 dB | 20,246 dB |

**Interpretação:** perda progressiva confirmada, pior nas regiões protegidas com detalhe e microtexto. As métricas só valem para a referência sintética alinhada. A linha 4K é uma identidade de referência; seu PSNR infinito aparece como null no JSON. O script registra também um indicador **global SSIM-like não padronizado**, que jamais deve ser tratado como SSIM oficial, VMAF ou nota de aprovação.

**Composição de dois sujeitos:** não cabem no mesmo crop vertical; cenário detectado e alternativa pad exportada. A adequação editorial do pad segue não verificada.

**Vídeo sintético:** 48 quadros a 24 FPS, duração de 2 s, corte de cena e marcador em movimento, áudio AAC. Saída 360×640, quadro/FPS/duração iguais, **mesmo SHA-256 do áudio PCM decodificado** antes/depois. O crop segue trajetória **manual** condicionada à cena. Sem tracking automático, QA visual de rosto/produto real, jitter ou human review.

**Portabilidade:** os números acima foram observados localmente. O workflow separado [reframe-quality-r1.yml](../../../.github/workflows/reframe-quality-r1.yml) instala FFmpeg no CI da branch de pesquisa e anexa JSON sintético. Conferir o resultado do próprio workflow antes de alegar que passou no GitHub. Nenhuma mídia privada foi publicada.

## 3. Gates propostos para qualidade profissional

| Gate | Evidência necessária | Resultado quando falhar |
|---|---|---|
| Direitos e autoridade | Fonte autorizada, fingerprint, região protegida, nenhum upload sem consentimento | BLOCKED |
| Geometria e safe areas | Todas as caixas protegidas cobertas em todos os quadros; composição passa avaliação visual | CROP_BLOCKED, recomendar pad/master alternativo |
| Resolução útil | Crop_width/target_width e crop_height/target_height; registrar toda ampliação, nunca só o canvas final | QUALITY_REVIEW_REQUIRED |
| Identidade e produtos | Faces, roupas, rótulos, logo, textura e geometria lado a lado com master | FAILED_CREATIVE_QA |
| Métrica alinhada | PSNR, SSIM ou VMAF quando houver referência tecnicamente alinhada | Diagnóstico apenas, não aprovação isolada |
| Movimento e cortes | Rastreamento, drift, jitter, zoom/pan, cortes limpos, sujeitos íntegros | NEEDS_TEMPORAL_QA |
| Áudio e exportação | FPS e quadros, duração, codecs, orientação, espaço de cor e áudio (PCM fingerprint para stream copy) | FAILED_TECHNICAL_QA |
| Critério humano | Avaliação editorial por formato, produto, identidade e contexto publicitário | Sem aprovação: UNVERIFIED |

Fontes técnicas: [YouTube recommended upload encoding](https://support.google.com/youtube/answer/1722171) orienta FPS da fonte, H.264, BT.709 para SDR, AAC/Opus etc.; **não certifica qualidade do material original**. [Netflix VMAF FAQ](https://github.com/Netflix/vmaf/blob/master/resource/doc/faq.md) explica por que VMAF entre resoluções distintas ou o escore isolado não atesta qualidade perceptual universal. O [projeto VMAF](https://github.com/Netflix/vmaf) oferece modelos atuais; **VMAF não foi executado neste benchmark**.

Não estabelecer cutoff universal de PSNR ou VMAF sem calibrar subjetivamente por mídia/dispositivo/domínio. Média alta não compensa um rosto, produto ou logo que falhe em um único quadro crítico.

## 4. Decisão de roteamento (proposta, não instalada)

1. **4K com crop seguro, pixels nativos suficientes:** priorizar reframe local com parâmetros de exportação adequados; ainda NEEDS_HUMAN_REVIEW.
2. **Full HD para 9:16 a 1080 vertical:** precisa ampliar 1,778× no cenário considerado, logo QUALIDADE CONDICIONAL, nunca aprovação por resolução nominal.
3. **480p para 1080 vertical:** ampliar 4×; não vender como qualidade nativa profissional. Recomendar master vertical original, composição editorial ou outra rota explicitamente aceita.
4. **Dois sujeitos em extremidades:** se ambos não cabem, crop está bloqueado; pad ou novo master exigem escolha editorial.
5. **Smart crop/tracking:** continua candidato, não comprovado. Apenas posicionamento manual foi testado.
6. **Outpainting:** rota generativa distinta, ainda não homologada; custos, dados, identidade, pixels protegidos e consistência temporal exigem novos testes e aprovação separada.

O reframe é uma **operação independente** da arquitetura da skill: recebe fonte e restrições, executa apenas o necessário, avalia, entrega status e encerra. Não cria automaticamente master, outpainting, nova cena ou publicação.

## 5. Próximo gate aberto

Comparação comercial com **mídias reais e de uso autorizado**: produto com textura e texto pequeno, um/dois rostos, master 4K e variações Full HD/480p, cortes/movimento e áudio, referência profissional/nativa vertical, formatos 9:16/4:5/1:1, inspeção de quadros problemáticos, QA humano e registro de versão/custo/direitos. Nenhuma mídia Della/diBoaS será enviada a API externa sem aprovação.

**Nenhuma integração ao runtime principal, merge, release, ação paga, upload privado ou aprovação de produção está implícita.**
