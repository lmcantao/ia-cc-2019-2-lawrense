import fuzzyfication

def get_risco(dinheiro, pessoa):
    (pouco, razoavel, adequado, insuficiente, satisfatorio) = fuzzyfication.get_result_fuzzyfication(dinheiro, pessoa)

    r_alto = max(max(pouco, insuficiente), min(pouco, satisfatorio))
    r_medio = min(razoavel, satisfatorio)
    r_baixo = min(adequado, satisfatorio)

    print(r_alto, r_medio, r_baixo)

    return r_alto, r_medio, r_baixo