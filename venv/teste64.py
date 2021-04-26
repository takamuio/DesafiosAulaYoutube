soma = contador = numero = 0
while numero != 999:
    numero = int(input('Digite um numero [999 para parar]: '))
    if numero != 999:
        soma += numero
        contador += 1
print('Você digitou {} numeros e a soma deles é {}'.format(contador, soma))