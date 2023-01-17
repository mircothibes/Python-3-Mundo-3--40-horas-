'''Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''

times = ('Corintians', 'Palmeiras', 'Santos', 'Gremio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitoria', 'Coritiba', 'Avai', 'Ponte Preta',
         'Atletico-GO')
print(f'Os cinco primeiros times são {times[0:5]}')
print(f'Os quatro ultimos colocados são {times[16:20]}')
print(f'Os times em ordem alfabeitca ficam: {sorted(times)}')
print(f'O time Chapecoense está na {times.index("Chapecoense")}ª posição')


