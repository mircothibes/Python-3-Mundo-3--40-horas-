'''Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep
def maior(* num):
    cont = maior = 0
    print('=-' * 20)
    print('Analisando os valores que foram passados...................')
    sleep(2)
    for valor in num:
        print(f'\33[1:34m{valor}\33[m', end='\n', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')

#Programa Principal
maior(2, 4, 6, 8)
maior(8, 12, 4, 3, 9)
maior(1, 5)
maior(6)
maior()

