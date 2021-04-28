valores = [[], []]
for contador in range(1, 8):
    numero = int(input(f'Digite o {contador}° numero: '))
    if numero % 2 == 0:
        valores[0].append(numero)
    else:
        valores[1].append(numero)
valores[0].sort()
valores[1].sort()
print('=-'*20)
print(f'Lista dos pares: {valores[0]}')
print(f'Lista dos impares: {valores[1]}')