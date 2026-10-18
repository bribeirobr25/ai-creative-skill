# AI Creative Skill · V2.5 — instalação

**Escolha apenas um formato:**

- `AI_Creative_Skill_V2.5_Agent_Skill.zip`: para hosts compatíveis com Agent Skills; o ZIP deve conter a pasta `ai-creative-skill/` e seu `SKILL.md`.
- `AI_Creative_Skill_V2.5_OpenAI_Portable_Plugin.zip`: para hosts que aceitam plugins no formato `plugin.json` + `skills/ai-creative-skill/`. Não contém uma conta ou tool/connector Higgsfield/fal/Runway. A disponibilidade real dos plugins e instalação varia por host.

**V2.5 inclui** as famílias V2.4 preservadas, `WEB_EXPERIENCE` e `MEDIA_UPSCALE`. Para websites, a skill instrui um agente com ferramentas de desenvolvimento a construir e inspecionar uma página. Os helpers web são validadores, roteadores determinísticos e preview local, não um gerador autônomo de sites. Para imagem/vídeo, inclui executor Pillow/FFmpeg e suporte opcional experimental Real-ESRGAN com PyTorch/pesos fornecidos pelo usuário.

**Dependências opcionais conforme função:** Python 3.11+; web QA: `jsonschema`, `beautifulsoup4` e navegador compatível; imagens: `Pillow`, `numpy`; vídeo: `ffmpeg`/`ffprobe`; neural: `torch`, checkpoints verificados e hardware/tempo suficientes. Instalação da skill não instala essas dependências nem descarrega pesos automaticamente. As rotas pagos externos estão apenas documentadas/mock.

**Comandos (na pasta `ai-creative-skill` extraída):**

```bash
python scripts/creative_web.py route 'crie uma landing para meu produto'
python scripts/creative_web.py preview start /caminho/para/site/dist
python scripts/creative_web.py preview status /caminho/para/site/dist
python scripts/creative_web.py preview restart /caminho/para/site/dist
python scripts/creative_web.py preview stop /caminho/para/site/dist
python scripts/creative_media.py routes
python scripts/creative_media.py quote --kind IMAGE --route local.pillow.lanczos.image.v0.2 --source /caminho/foto.png --width 2000 --height 2000
```

Atenção: para uma foto não quadrada use dimensões de destino com mesma proporção; o comando acima é apenas ilustrativo para imagem quadrada.

**Não publicar sem autorização.** `PREVIEW_DRAFT` não significa `PREVIEW_ACCEPTED` nem `LIVE_VERIFIED`. Super-resolução neural preservando letras, rostos e produtos ainda requer revisão humana.

**Versão e auditoria:** `references/AI_Creative_Skill_V2.5_Integration_Manifest.md`, `references/AI_Creative_Skill_Release_Gates_v2.5.md`, `MANIFEST_SHA256.json`. Sem migração automática do 00_ACTIVE ou dos arquivos canônicos do usuário.
