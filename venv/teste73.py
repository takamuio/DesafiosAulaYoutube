brasileirao = ('Flamengo', 'Internacional', 'Atlético MG', 'São Paulo', 'Fluminence', 'Grêmio', 'Palmeiras', 'Santos',
               'Athletico Paranaense', 'Red Bull Bragantino', 'Ceará', 'Corinthians', 'Atlético GO', 'Bahia', 'Sport',
               'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')

print(f'Lista completa na ordem de classificação: {brasileirao}')
print('=-'*10)
print(f'Os 5 primeiros colocados são: {brasileirao[0:5]}')
print('=-'*10)
print(f'Os ultimos 4 colocados são: {brasileirao[-4:]}')
print('=-'*10)
print(f'A lista em ordem alfabetica: {sorted(brasileirao)}')
print('=-'*10)
print(f'O Grêmio esta na {brasileirao.index("Grêmio")+1}ª posição')