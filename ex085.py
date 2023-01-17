''' Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.'''

numeros = [[], []]
val = 0
for c in range(1, 8):
    val = int(input(f'Digite o {c}º numero: '))
    if val % 2 == 0:
        numeros[0].append(val)
    else:
        numeros[1].append(val)
print('=-'*20)
print(f'Todos os valores e suas respectiva lista -> {numeros} ')
numeros[0].sort()
numeros[1].sort()
print(f'Valore pares {numeros[0]}')
print(f'Valore impares {numeros[1]}')


