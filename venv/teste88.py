from random import randint
from time import sleep
megasena = []
jogos = []
print('--'*20)
print(F'{"MEGA SENA":^40}')
print('--'*20)
quantidade_de_jogos = int(input('Quantos jogos serão feito ? '))
total_de_jogos = 1
while total_de_jogos <= quantidade_de_jogos:
    contador = 0
    while True:
        sortido = randint(1, 60)
        if sortido not in jogos:
            jogos.append(sortido)
            contador += 1
        if contador >= 6:
            break
    jogos.sort()
    megasena.append(jogos[:])
    jogos.clear()
    total_de_jogos += 1
for numeros, jogadas in enumerate(megasena):
    print(f'{numeros+1}° Jogo: {jogadas}')
    sleep(1.5)
print('Boa Sorte')