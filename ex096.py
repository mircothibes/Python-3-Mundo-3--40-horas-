'''Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.'''

def area(largura, comprimento):
    a = largura * comprimento
    print(f'A area de um terreno {largura} x {comprimento} é de {a:.2f}m2')

# PROGRAMA PRINCIPAL
print('Controle de terrenos')
print('=' * 20)
l = float(input('Largura (metros): '))
c = float(input('Comprimento (metros): '))
area(l, c)
