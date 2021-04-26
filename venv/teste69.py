idade_menor = idade_maior = contador = 0
print('==== Cadastrar Pessoas ====')
while True:
    idade = int(input('Digite idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Digite sexo [M/F]: ')).upper().strip()[0]
    if idade >= 18:
        idade_maior += 1
    if sexo in 'Mm':
        contador += 1
    if sexo in 'Ff' and idade < 20:
        idade_menor += 1
    print('=-'*10)
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = str(input('Deseja continuar [S/N] ? ')).upper().strip()[0]
    print('=-' * 10)
    if opcao in 'Nn':
        break
print(f'Foram cadastrados {idade_maior} pessoas acima de 18 anos')
print(f'Foram cadastrados {contador} homens')
print(f'Foram cadastrados {idade_menor} mulheres abaixo de 20 anos')
