import random
numero = random.randint(0,5)
print('Pensei em um numero de 0 a 5. Tente acertar !')
escolha = int(input('Escolhi o numero : '))
if numero == escolha:
    print('Você acertou !')
else:
    print('Você errou !')
print('O numero que eu pensei foi {}'.format(numero))