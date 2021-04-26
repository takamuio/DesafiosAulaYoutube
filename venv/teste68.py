from random import randint
from time import  sleep
print('=== Par ou Impar ===')
diferenca = 0
vitorias = 0
while True:
    parimpar = ' '
    while parimpar not in 'PpIi':
        parimpar = str(input('Par ou Impar [P/I] ? ')).upper().strip()[0]
        escolha = int(input('Numero de 1 a 3: '))
        escolha_pc = randint(1, 3)
        diferenca = escolha + escolha_pc
        print('Par')
        sleep(1)
        print('Ou')
        sleep(1)
        print('Impar')
        print(f'Você escolheu {escolha} e a maquina {escolha_pc}. Total {diferenca}', end='')
        if diferenca % 2 == 0:
            print(' Deu PAR')
        else:
            print(' Deu IMPAR')
    if parimpar in 'Pp':
        if diferenca % 2 == 0:
            print('Você venceu !')
            vitorias += 1
        else:
            print('Você Perdeu !')
            break
    elif parimpar in 'Ii':
        if diferenca % 2 == 1:
            print('Você venceu !')
            vitorias += 1
        else:
            print('Você Perdeu !')
            break
    print('=-'*10)
    print('Vamos jogar novamente...')
    print('=-' * 10)

print(f'Você ganhou {vitorias} vezes')