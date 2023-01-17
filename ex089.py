'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário
 possa mostrar as notas de cada aluno individualmente.'''

ficha = list()

while True:
    nome = str(input('Nome: ')).strip().upper()[0:]
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
print('-='*20)
print(ficha)
print(f'{"No":<4}{"Nome":<10}{"Media":>8}')
print('-='*20)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.2f}')
while True:
    print('-='*20)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Final')
        break
    if opc <= len(ficha) - 1:
        print(f'Nota de {ficha[opc][0]} sao {ficha[opc][1]}')
print('Arrivederti')