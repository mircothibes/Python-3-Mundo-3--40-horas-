def aumentar(preço = 0, taxa = 0):
    resposta = preço + (preço * taxa / 100)
    return resposta

def diminuir(preço = 0, taxa = 0):
    resposta = preço - (preço * taxa / 100)
    return resposta

def dobro(preço = 0):
    resposta = preço * 2
    return resposta


def metade(preço):
    resposta = preço / 2
    return resposta

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')
