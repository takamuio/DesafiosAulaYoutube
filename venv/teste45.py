from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
maquina = randint(0,2)

jogador = int(input('Suas opções: \n'
                    '[ 0 ] Pedra \n'
                    '[ 1 ] Papel \n'
                    '[ 2 ] Tesoura \n'
                    ''))
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po !')

print('-=' * 15)
print('O computador escolheu {}'.format(itens[maquina]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-=' * 15)

if maquina == 0:
    if jogador == 0:
        print('Deu empate.')
    elif jogador == 1:
        print('Você ganhou !')
    elif jogador == 2:
        print('Você perdeu !')
    else:
        ('jogada invalida !')
elif maquina == 1:
    if jogador == 0:
        print('Você pedeu !')
    elif jogador == 1:
        print('Deu empate.')
    elif jogador == 2:
        print('Você ganhou !')
    else:
        ('jogada invalida !')
elif maquina == 2:
    if jogador == 0:
        print('Você ganhou !')
    elif jogador == 1:
        print('Você pedeu !')
    elif jogador == 2:
        print('Deu empate.')
    else:
        ('jogada invalida !')