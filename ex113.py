'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação
 de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\33[7;31mERRO: favor digitar um numero inteiro valido!\33[m')
            continue
        except (KeyboardInterrupt):
            print('\n\33[1;31mEntada de erro interrompida pela usuario!\33[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\33[7;31mERRO: favor digitar um numero inteiro valido!\33[m')
            continue
        except (KeyboardInterrupt):
            print('\n\33[1;31mEntada de erro interrompida pela usuario!\33[m')
            return 0
        else:
            return n


#programa principal
n1 = leiaInt('Digite um valor inteiro: ')
n2 = leiaFloat('Digite um valor real: ')
print(f'Valor inteiro digitado foi {n1} e o real foi {n2}')
