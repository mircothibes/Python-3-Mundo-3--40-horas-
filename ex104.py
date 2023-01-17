'''Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante ‘a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt(‘Digite um n: ‘)'''

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\33[1;31mERRO - Digite o numero valido\33[m')
        if ok:
            break
    return valor

#programa principal
numero = leiaInt('Digite um numero quaquer: ')
print(f'Voce acabou de digitar o numero {numero}!!!')