# Próximo gate · Media Upscale v0.3

**Decisão:** `ACCEPTED_AS_ISOLATED_TECHNICAL_CANARY`, `NOT_PRODUCTION_READY`.

1. **Reprodutibilidade:** extrair o ZIP em ambiente limpo e executar três rotas (imagem convencional, imagem neural crop, vídeo neural de 0,5s) e 61 testes sem puxar recursos ocultos do host. Checar manifestos e licenças.
2. **Qualidade imagem:** revisão humana lado a lado de produto, rosto, conteúdo editorial, etiqueta; separar preferências de **fidelidade factual**. Se o ganho for imperceptível ou alterar marca, não promover rota neural.
3. **Vídeo no Work Mac/MPS:** testar o executor v0.3 ou adaptar a receita comprovada da v0.2 Work para 5s de 480p→1080p e comparar com D e Higgsfield, mesmos quadros, fotos reais canônicas, pele e etiqueta. Registrar hashes/custos/tempo.
4. **Critério temporal:** medir/revisar flicker em todas as cenas e transições; não presumir que preservação de FPS implica estabilidade de texturas.
5. **Resoluções por rota:** 1080p, 4K, 8K somente quando executáveis com hardware/custo aprovados; testes de compatibilidade 4K GPU, limiar de RAM, codec, fps, SAR e HQ; cotação isolada não é render.
6. **Compliance:** considerar proteção de dados e licenças antes de distribuição, evitar embutir mídias privadas Della no pacote público da skill; artefatos atuais são apenas pesquisa privada.
7. **Arquitetura e deploy:** revisão contra o Registry, Execution Route Recipe e QA da V2.4; rodar canário host independente; só então alterar branch candidata, nunca `00_ACTIVE` sem autorização.

**Não iniciar automaticamente jobs pagos, nem gerar novos vídeos completos da Della, nem promover modelo em produção por um único resultado bonito.**
