'''Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:
escreva(‘Olá, Mundo!’) Saída:
Olá, Mundo!'''

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa Principal
escreva('Marcos V T Kemer')
escreva('Thais S  Rosar')
escreva('Olivia Rosar Kemer')
escreva('Betina Rosar Kemer')

