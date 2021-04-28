valores = []
while True:
    numero = int(input('Digite um valor: '))
    if numero not in valores:
        valores.append(numero)
        print('Valor adicionado.')
    else:
        print('Valor duplicado, não adicionado.')
    opcao = ' '
    while opcao not in 'NnSs':
        opcao = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    if opcao in 'Nn':
        break
print('=-'*20)
valores.sort()
print(f'Você digitou: {valores}')
