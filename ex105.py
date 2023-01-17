''' Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)'''

def notas(* n, sit=False):
    """
    -> Função para analisar notas e situação de alunos.
    :param n: uma ou mais notas dos alunos (aceita uma variavel),
    :param sit: valor opcional, indicando se deve ou adicionar a situação.
    :return: dicionario com várias informações da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'PÉSSIMO'
    return r

#programa principal
resposta = notas(5.5, 2.5, 8.5, sit=True)
print(resposta)
#help(notas)

