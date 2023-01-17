'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

num = list()
while True:
    n = int(input('Digite um numero: '))
    if n not in num:
        num.append(n)
        print('Valor Adcionado!!!')
    else:
        print('Valor Duplicado - Este valor não sera adicionado!!!')
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if r in 'N':
        break
print('Final!')
print('-'*20)
num.sort()
print(f'Você digitou os valores em ordem crescente e ficoou assim: {num}')

