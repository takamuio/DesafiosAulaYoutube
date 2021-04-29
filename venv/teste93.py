jogador = {}
gols = []
jogador['nome'] = str(input('Nome jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for contador in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {contador+1}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('=-'*20)
print(jogador)
print('=-'*20)
for keys, valores in jogador.items():
    print(f'O campo [{keys}] tem o valor {valores}')
print('=-'*20)
print(f'O jogador {jogador["nome"]} jogou {len(gols)} partidas.')
for indice, valores in enumerate(jogador['gols']):
    print(f'{"=>":>6} Na partida {indice+1}, fez {valores} gols')
print(f'foi um total de {jogador["total"]} gols')