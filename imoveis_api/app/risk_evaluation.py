def avaliar_risco(valor_imovel, pontuacao_credito, renda_comprador):
    if valor_imovel > 10_000_000 or valor_imovel < 100_000:
        return "Reprovada"
    if pontuacao_credito < 500:
        return "Reprovada"
    if valor_imovel > 0.3 * renda_comprador:
        return "Reprovada"
    return "Aprovada"
