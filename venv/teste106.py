from time import sleep
cores = ('\033[m',          # 0 - sem cor
         '\033[0;30;41m',   # 1 - vermelho
         '\033[0;30;42m',   # 2 - verde
         '\033[0;30;43m',   # 3 - amarelo
         '\033[0;30;44m',   # 4 - azul
         '\033[0;30;45m',   # 5 - roxo
         '\033[7;30m')      # 6 - branco


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(cores[5], end='')
    help(com)
    print(cores[0], end='')
    sleep(2)


def titulo(msg, cor= 0):
    tamanho = len(msg) + 4
    print(cores[cor], end='')
    print('~'* tamanho)
    print(f'  {msg}')
    print('~'* tamanho)
    print(cores[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('Systema de AJUDA PyHelp', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Obrigado', 1)