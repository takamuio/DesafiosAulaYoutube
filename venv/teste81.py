valores = []
while True:
    numero = int(input('Digite um valor: '))
    valores.append(numero)
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    if opcao in 'Nn':
        break
print('=-'*10)
print(f'Foi adicionado {len(valores)} numeros')
valores.sort(reverse=True)
print(f'Lista ondenada de forma decrescente: \n'
      f'{valores}')
if 5 in valores:
    print('O valor 5 esta na lista !')
else:
    print('O valor 5 não esta na lista !')
