''' Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''
todaspessoas = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input("Nome: ")).strip().upper()
    while True:
        pessoa['sexo'] = str(input("Sexo [M/F]: ")).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO!Por Favor digite apenas M ou F')
    pessoa['idade'] = int(input("Idade: "))
    soma += pessoa['idade']
    todaspessoas.append(pessoa.copy())
    while True:
        r = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if r in 'SN':
            break
        print('ERRO - Responda apenas S ou N.')
    if r == 'N':
        break
print('=-' * 20)
print(f'A) Ao todo temos {len(todaspessoas)} pessoas cadastradas')
media = soma / len(todaspessoas)
print(f'B) A media de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram => ', end='')
for p in todaspessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} - ', end=' ')
print()
print('D) Lista de pessoas que estão acima da media: ')
for p in todaspessoas:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('=-'*20)
print('=====FINALIZADO=====')

