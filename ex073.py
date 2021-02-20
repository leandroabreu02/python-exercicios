# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol,
# na ordem de colocação. Depois mostre:
# A) apenas os 5 primeiros colocados:
# B) os últimos 4 colocados da tabela:
# C) uma lista com os times em ordem alfabética
# D) em que posição na tabela está o time do corinthians
times = ('Internacional', 'Flamengo', 'São Paulo', 'Atlético-MG', 'Fluminense', 'Palmeiras', 'Grêmio', 'Santos', 'Athletico-PR', 'Corinthians', 'Bragantino', 'Ceará SC', 'Atlético-GO', 'Sport Recife', 'Fortaleza', 'Bahia', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')
print(f'Os 5 primeiros são: {times[0:5]}')
print(f'Os 4 últimos são: {times[16:20]}')
print(f'Times em ordem alfabética: {sorted(times)}')


# for pos, 'Corinthians' in enumerate(times) :
#   print(f'O Corinthians está na {pos}ª colocação!')




