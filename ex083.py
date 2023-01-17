'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''
simbolo = ''
p = []
exp = str(input('Digite uma expressão: ')).strip()
for simbolo in exp:
    if simbolo == '(':
        p.append('(')
    elif simbolo == ')':
        if len(p) > 0:
            p.pop()
        else:
            p.append(')')
            break
if len(p) == 0:
    print('Sua expressão está valida!!!')
else:
    print('Sua expressão está errada!!!')

