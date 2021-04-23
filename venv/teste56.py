soma_idade = 0
idade_mais_velho = 0
quantidade_feminono = 0
nome_mais_velho = ''
for c in range(1,5):
    print('---- {}ª PESSOA ----'.format(c))
    nome = str(input('Seu nome: '))
    idade = int(input('Sua idade: '))
    sexo = str(input('Seu sexo [M/F]: ')).strip()
    soma_idade += idade
    if sexo in 'Mm' and idade > idade_mais_velho:
        idade_mais_velho = idade
        nome_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        quantidade_feminono += 1

media_idade = soma_idade / 4
print('A media de idade do grupo é de {} anos'.format(media_idade))
print('O homem mais velho do grupo é {} com {} anos'.format(nome_mais_velho,idade_mais_velho))
print('Existem {} mulheres abaixo de 20 anos no grupo'.format(quantidade_feminono))