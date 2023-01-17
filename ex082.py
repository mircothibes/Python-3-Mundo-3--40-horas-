'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um numero: ')))
    r = str(input('Voce deseja continuar? [S/N]: ')).strip().upper()[0]
    if r in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('/-/'*20)
print(f'Os numeros da lista digitada foram {num}')
print(f'Valore pares foram os {pares}')
print(f'Valores impares foram os {ímpares}')
print('/-/'*20)

