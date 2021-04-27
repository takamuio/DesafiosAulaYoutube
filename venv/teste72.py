contagem = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
            'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('Digite um numero de 0 a 20: '))
    if numero <= 20 and numero >= 0:
        break
    print('Numero invalido! ')
print(f'Você digitou o numero {contagem[numero]}', end=' ')