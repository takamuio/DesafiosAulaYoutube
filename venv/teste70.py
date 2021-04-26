total = menor = contador = contador_mil = 0
nome_menor = ''
print('=-'*10)
print('=== Mercado do Zé ===')
print('=-'*10)
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preco do produto: '))
    total += preco
    contador += 1
    if contador == 1:
        menor = preco
    if preco < menor:
        menor = preco
        nome_menor = nome
    if preco > 1000:
        contador_mil += 1
    print('=-'*10)
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = str(input('Deseja continuar [S/N] ? ')).upper().strip()[0]
    print('=-' * 10)
    if opcao in 'Nn':
        print('==== Fim do Programa ====')
        break
print(f'O total gasto é R$ {total:.2f}')
print(f'Existem {contador_mil} produdos acima de R$ 1000.00')
print(f'O produto de menor custo é {nome_menor} por R$ {menor:.2f}')
