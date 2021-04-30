from time import sleep
from random import randint


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for contador in range(0,5):
        num = randint(1,10)
        numeros.append(num)
        print(f'{num} ', end='')
        sleep(0.5)
    print('pronto !')
def somapar():
    soma = 0
    for contador in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {numeros}, temos {soma}')


numeros = []
sorteia()
somapar()
