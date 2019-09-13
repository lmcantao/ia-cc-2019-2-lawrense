import risco

def get_desfuzzyfication(dinheiro, pessoa):

    (r_alto, r_medio, r_baixo) = risco.get_risco(dinheiro, pessoa)

    qtd_baixo = 0
    qtd_medio = 0
    qtd_alto = 0

    valor_baixo = 0
    valor_medio = 0
    valor_alto = 0

    for x in range(0, 91, 5):
        if x <= 30:
            qtd_baixo = qtd_baixo + 1
            valor_baixo = valor_baixo + x
        elif x >= 40 and x <= 60:
            qtd_medio = qtd_medio + 1
            valor_medio = valor_medio + x
        elif x >= 70:
            qtd_alto = qtd_alto + 1
            valor_alto = valor_alto + x


    print(valor_baixo, valor_medio, valor_alto, qtd_baixo, qtd_medio, qtd_alto, valor_baixo * r_baixo + valor_medio * r_medio + valor_alto * r_baixo, qtd_baixo * r_baixo + qtd_medio * r_medio + qtd_alto * r_alto)

    resp = (valor_baixo * r_baixo + valor_medio * r_medio + valor_alto * r_alto) / (qtd_baixo * r_baixo + qtd_medio * r_medio + qtd_alto * r_alto)

    if resp <= 30:
        return "BAIXO RISCO"
    elif resp > 30 and resp < 40:
        return "MÉDIO_BAIXO RISCO"
    elif resp >= 40 and resp <= 60:
        return "MÉDIO RISCO"
    elif resp > 60 and resp < 70:
        return "MÉDIO_ALTO RISCO"
    elif resp >= 70:
        return "ALTO RISCO"
