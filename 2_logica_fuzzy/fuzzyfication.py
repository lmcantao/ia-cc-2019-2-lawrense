def get_result_fuzzyfication(dinheiro, pessoa):

    if dinheiro <= 30:
        pouco = 1
        razoavel = 0
        adequado = 0
    elif dinheiro > 30 and dinheiro < 50:
        pouco = (50 - dinheiro) / 20
        razoavel = (dinheiro - 30) / 20
        adequado = 0
    elif dinheiro == 50:
        pouco = 0
        razoavel = 1
        adequado = 0
    elif dinheiro > 50 and dinheiro < 70:
        pouco = 0
        razoavel = (70 - dinheiro) / 20
        adequado = (dinheiro - 50) / 20
    elif dinheiro >= 70:
        pouco = 0
        razoavel = 0
        adequado = 1

    if pessoa <= 30:
        insuficiente = 1
        satisfatorio = 0
    elif pessoa > 30 and pessoa < 70:
        insuficiente = (70 - pessoa) / 40
        satisfatorio = (pessoa - 30) / 40
    elif pessoa >= 70:
        insuficiente = 0
        satisfatorio = 1

    print(pouco,razoavel,adequado,insuficiente,satisfatorio)

    return pouco,razoavel,adequado,insuficiente,satisfatorio