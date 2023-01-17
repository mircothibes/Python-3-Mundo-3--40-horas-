'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o
(com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['CT'] = int(input('Carteira de Trabalho: (0 não tem): '))
if dados['CT'] != 0:
    dados['contraração'] = int(input('Ano de contraração: '))
    dados['salario'] = float(input('Salario: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contraração'] + 35) - datetime.now().year)
print('-=' * 20)
print(dados)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
