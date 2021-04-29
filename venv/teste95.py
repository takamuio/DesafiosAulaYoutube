time = []
jogador = {}
gols = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols.clear()
    for contador in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {contador+1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        opcao = str(input('Deseja continuar ? [S/N] ')).upper().strip()[0]
        if opcao in 'SN':
            break
        print('ERRO ! Digite apenas S ou N.')
    if opcao in 'N':
        break
print('=-'*20)
print('ID ', end='')
for i in jogador.keys():
    print(f'{i:<15} ', end='')
print()
print('=-'*20)
for keys, valores in enumerate(time):
    print(f'{keys:>3}  ', end='')
    for dados in valores.values():
        print(f'{str(dados):<15}', end='')
    print()
print('=-'*20)
while True:
    busca = int(input('Buscar jogador pela ID? [999 finaliza] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe jogador com ID {busca}')
    else:
        print(f' --- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]} ---')
        for indice, gol in enumerate(time[busca]["gols"]):
            print(f'   No jogo {indice+1} fez {gol} gols.')
    print('=-' * 20)
print('Programa finalizado')