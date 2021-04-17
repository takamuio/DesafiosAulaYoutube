nome_completo = input('Digite seu nome completo: ')
divisao_de_nome = nome_completo.split()
print('Seu primeiro nome é: {}'.format(divisao_de_nome[0].title()))
print('Seu ultimo nome é: {}'.format(divisao_de_nome[-1].title()))