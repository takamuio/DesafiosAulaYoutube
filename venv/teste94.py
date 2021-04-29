galera = []
pessoa = {}
soma_idade = media_idade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO ! Digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma_idade += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        opcao = str(input('Deseja continuar ? [S/N] ')).upper().strip()[0]
        if opcao in 'SN':
            break
        print('ERRO ! Digite apenas S ou N.')
    if opcao in 'N':
        break
print('=-'*20)
print(f'A) O grupo tem {len(galera)} pessoas')
media_idade = soma_idade / len(galera)
print(f'B) A media da idade é {media_idade:5.2f}')
print(f'C) As mulheres cadastradas foram ', end='')
for pessoas in galera:
    if pessoas['sexo'] in 'Ff':
        print(f'[{pessoas["nome"]}] ', end='')
print()
print(f'D) Lista das pessoas que estão acima da media: ', end='')
for pessoas in galera:
    if pessoas['idade'] >= media_idade:
        print(f'{pessoas["nome"]} com {pessoas["idade"]} anos.', end='')

