import random
numero = random.randint(0, 10)
escolha = contador = 0
print('Pensei em um numero de 0 a 10. Tente acertar !')
while numero != escolha:
    escolha = int(input('Qual seu palpite: '))
    contador += 1
    if numero == escolha:
        print('Você acertou !')
        print('O numero que eu pensei foi {}'.format(numero))
    else:
        if numero < escolha:
            print('Menos... tente novamente !')
        elif numero > escolha:
            print('Mais... tente novamente')

print('Você precisou de {} chances para acertar ! Parabens !'.format(contador))
