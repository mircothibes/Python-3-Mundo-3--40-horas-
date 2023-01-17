'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

valores = []
while True:
    valores.append(int(input('Digite um numero: ')))
    r = str(input('Voce deseja continuar? [S/N]: ')).strip().upper()[0]
    if r not in 'S':
        break
print(f'Voce digitou {len(valores)} numeros')
valores.sort(reverse=True)
print(f'A lista em ordem decrescente {valores}')
print(f'O valor 5 aparece {valores.count(5)} vez')
