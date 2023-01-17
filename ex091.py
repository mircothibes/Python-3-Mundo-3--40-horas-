'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'player1': randint(1, 6),
        'player2': randint(1, 6),
        'player3': randint(1, 6),
        'player4': randint(1, 6)}
ranking = list()
print('VAlORES SORTEADOS')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(2)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('Ranking dos Jogadores')
for i, v in enumerate(ranking):
    print(f'{i+1}ª lugar: {v[0]} com {v[1]}')
    sleep(1)


