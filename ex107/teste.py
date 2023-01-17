'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use
algumas dessas funções.'''

from ex107 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade do preço é {moeda(p)} é {(moeda.metade(p))}')
print(f'O dobro do preço é {moeda(p)} é {(moeda.dobro(p))}')
print(f'Aumentado 10% de {moeda(p)} fica {(moeda.aumentar(p, 10))}')
