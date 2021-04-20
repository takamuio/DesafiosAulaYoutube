numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite um numero: '))
numero3 = int(input('Digite um numero: '))
maior = numero1
if (numero2 > maior):
    maior = numero2
if (numero3 > maior):
    maior = numero3
print('{} é o maior numero'.format(maior))

menor = numero1
if (numero2 < menor):
    menor = numero2
if (numero3 < menor):
    menor = numero3
print('{} é o menor numero'.format(menor))
