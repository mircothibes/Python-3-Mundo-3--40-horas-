def aumentar(preço, taxa):
    resposta = preço + (preço * taxa / 100)
    return resposta

def diminuir(preço, taxa):
    resposta = preço - (preço * taxa / 100)
    return resposta

def dobro(preço):
    resposta = preço * 2
    return resposta

def metade(preço):
    resposta = preço / 2
    return resposta
