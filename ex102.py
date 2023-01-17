'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show,
que será um valor lógico (opcional) indicando se será mostrado
 ou não na tela o processo de cálculo do fatorial.'''

def fatorial(numero, show=False):
    """
    Calcula o Fatorial de um numero!
    :param numero: o numero a ser calculado
    :param show: é opcional, pode mostar ou não a conta
    :return: o valor fatorial de um numero
    """
    f = 1
    for c in range(numero, 0, - 1):
        print(c, end='')
        if c > 1:
            print(' x ', end='')
        else:
            print(' = ', end='')
        f *= c
    return f


#programa principal
print(fatorial(15, show=True))

#help(fatorial)


