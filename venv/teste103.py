def ficha(nome = '<desconhecido>', gols = 0):
    print(f'O jogador {nome} fez {gols} gols no campeonato')



nome_jogador = str(input('Digite o nome do jogador: '))
quantidade_gols = str(input('Digite quantidade de gols: '))
if quantidade_gols.isnumeric():
    quantidade_gols = int(quantidade_gols)
else:
    quantidade_gols = 0
if nome_jogador.strip() == '':
    ficha(gols=quantidade_gols)
else:
    ficha(nome_jogador, quantidade_gols)