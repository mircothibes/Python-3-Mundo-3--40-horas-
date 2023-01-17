'''Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto
NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''
import datetime

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'com {idade} anos: Não Pode votar ainda!'
    elif 16 <= idade < 18 or idade > 65:
        return f'com {idade} anos : O voto é opcional!'
    else:
        return f'Com {idade} anos : O voto é valido!'



#programa principal
nasc = int(input('Digite o ano de nascimento: '))
print(voto(nasc))
