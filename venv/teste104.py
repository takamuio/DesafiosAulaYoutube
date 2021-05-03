def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        numero = str(input(msg))
        if numero.isnumeric():
            valor = int(numero)
            ok = True
        else:
            print(f'\033[0;31mErro ! Digite um valor inteiro valido.\033[m')
        if ok:
            break
    return valor


numero = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o numero {numero}')