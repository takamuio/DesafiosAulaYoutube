from math import factorial
numero = int(input('Digite um numero inteiro: '))
f = factorial(numero)
print('O fator do numero {} é {}'.format(numero,f))

#usando while

contador = numero
fator = 1
print('Calculando {}! = '.format(numero), end='')
while contador > 0:
    print('{}'.format(contador), end='')
    if contador > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    fator *= contador
    contador -= 1
print('{}'.format(fator))
