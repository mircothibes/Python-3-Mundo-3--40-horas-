def aumentar(preço=0, taxa=0, formato=False):
    """
    ->calcula o aumento de um determinado preço,
    retotnando o resultado com sua formatação.
    :param preço: o preço a ser reajustado.
    :param taxa: qual é a porcentagem do aumento.
    :param formato: se quer a saida formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    """
    resposta = preço + (preço * taxa / 100)
    return resposta if format is False else moeda(resposta)

def diminuir(preço=0, taxa=0, formato=False):
    resposta = preço - (preço * taxa / 100)
    return resposta if format is False else moeda(resposta)

def dobro(preço=0, formato=False):
    resposta = preço * 2
    return resposta if format is False else moeda(resposta)


def metade(preço=0, formato=False):
    resposta = preço / 2
    return resposta if format is False else moeda(resposta)

def moeda(preço =0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')

def resumo(preço=0, taxaaumento=10, taxaredução=5):
    print('=' * 30)
    print('Resumo do valor'.center(30))
    print('=' * 30)
    print(f'Preço Analisado: \t{moeda(preço)}')
    print(f'O dobro do preço é \t{dobro(preço, True)}')
    print(f'Metado do preço é \t{metade(preço, True)}')
    print(f'{taxaaumento}% de aumento: \t{aumentar(preço, taxaaumento, True)}')
    print(f'{taxaredução}% de redução: \t{diminuir(preço, taxaredução, True)}')
    print('=' * 30)
