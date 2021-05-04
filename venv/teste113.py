def leia_int(msg):
    while True:
        try:
            numero = int(input(msg))
        except (TypeError, ValueError):
            print(f'\033[0;31mErro ! Digite um valor inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[0;31mErro ! Entrada de dados interrompido pelo usuario.\033[m')
            return 0
        else:
            return numero

def leia_float(msg):
    while True:
        try:
            numero = float(input(msg))
        except (TypeError, ValueError):
            print(f'\033[0;31mErro ! Digite um valor real valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[0;31mErro ! Entrada de dados interrompido pelo usuario.\033[m')
            return 0
        else:
            return numero


numero_inteiro = leia_int('Digite um numero inteiro: ')
numero_real = leia_float('Digite um numero real: ')
print(f'Você digitou Inteiro {numero_inteiro}, Real {numero_real}')
