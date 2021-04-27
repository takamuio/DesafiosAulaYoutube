numeros = (int(input('Digite um numero: ')), int(input('Digite mais um numero: ')), int(input('Digite outro numero: ')),
           int(input('Digite o ultimo numero: ')))
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
else:
    print('O numero 3 não foi digitado em nenhuma posição !')
print(f'Os valores pares digitados foram ', end='')
for contador in numeros:
    if contador % 2 == 0:
        print(contador, end=' ')