'''Adapte o código do desafio #107, criando uma função adicional chamada moeda()
que consiga mostrar os números como um valor monetário formatado.'''

from ex108 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade do preço é {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro do preço é {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentado 10% de {moeda.moeda(p)} fica {moeda.moeda(moeda.aumentar(p, 10))}')

