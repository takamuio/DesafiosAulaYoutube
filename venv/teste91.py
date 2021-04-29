from random import randint
from time import sleep
from operator import itemgetter
jogadas = {'jogador_1': randint(1,6),
           'jogador_2': randint(1,6),
           'jogador_3': randint(1,6),
           'jogador_4': randint(1,6)}
ranking = []
print(f'{"Preparando jogadas":^40}')
print('=-'*20)
sleep(1.5)
for key, valor in jogadas.items():
    print(f'O {key} tirou: {valor}')
    sleep(1)
print('=-'*20)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print(f'{" == Ranking dos jogadores ==":^40}')
for indece, valor in enumerate(ranking):
    print(f'O {indece+1}° lugar: {valor[0]} com {valor[1]}')
    sleep(1)