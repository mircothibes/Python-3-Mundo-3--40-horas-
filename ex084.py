'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
ltemp = []
lprin = []
maior = menor = 0
while True:
    ltemp.append(str(input('Nome: ')).strip())
    ltemp.append(float(input('Peso: ')))
    if len(lprin) == 0:
        maior = menor = ltemp[1]
    else:
        if ltemp[1] > maior:
            maior = ltemp[1]
        if ltemp[1] < menor:
            menor = ltemp[1]
    lprin.append(ltemp[:])
    ltemp.clear()
    r = str(input('Voce deseja continuar? [S/N]: ')).strip().upper()[0]
    if r in 'N':
        break
print('=-' *20)
print(f'Pessoas cadastradas {lprin} ')
print(f'Ao total foram cadastradas {len(lprin)} pessoas')
print(f'O maior peso foi de {maior}Kg')
print(f'O menor peso foi de {menor}Kg')
