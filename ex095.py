'''Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    totalpartidas = int(input(f'Quantas partidas {jogador["nome"]}? '))
    partidas.clear()
    for c in range(0, totalpartidas):
        partidas.append(int(input(f'Quantos gols na {c}ª partida? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        r = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if r in 'SN':
            break
        print('ERRO - Responda apenas S ou N')
    if r in 'Nn':
        break
print('='*20)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3}º ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Qual jogador você deseja ver os dados? (999(SAIR)): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Jogador exite jogado com codigo {busca}')
    else:
        print(f'---Dados do jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'     No jogo {i} fez {g} gols.')
print('-' * 40)
print('-----FIM-----')
