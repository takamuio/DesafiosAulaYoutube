valores = []
while True:
    numero = int(input('Digite um valor: '))
    valores.append(numero)
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    if opcao in 'Nn':
        break
valores_impares = []
valores_pares = []
for valor in range(0, len(valores)):
    if valor % 2 == 0:
        valores_pares.append(valor)
    else:
        valores_impares.append(valor)
print(f'Lista completa: {valores}')
print(f'Lista dos pares: {valores_pares}')
print(f'Lista dos impares: {valores_impares}')
