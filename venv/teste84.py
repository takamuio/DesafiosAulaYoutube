pessoas = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        menor = maior = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = str(input('Deseja continuar ? [S/N] ')).upper().strip()[0]
    if opcao in 'Nn':
        break
print('=-'*20)
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'A lista completa {pessoas}')
print(f'O maior peso é {maior}Kg de ', end='')
for c in pessoas:
    if c[1] == maior:
        print(f'[{c[0]}]', end=' ')

print(f'\nO menor peso é {menor}KG de ',end='')
for c in pessoas:
    if c[1] == menor:
        print(f'[{c[0]}]', end=' ')
