from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #listar o conteudo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #cadastrar pessoas
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('\33[1;34mSaindo do sistema.......Até logo!!!\33[m')
        break
    else:
        print('\33[7:31mDigite uma opção valida\33[m')
        sleep(2)

