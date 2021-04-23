from datetime import date
ano_atual = date.today().year
soma_menor = 0
soma_maior = 0
for pessoa in range(1, 8):
    ano_nascimento = int(input('Ano de nascimento da {}ª pessoa ?'.format(pessoa)))
    if ano_atual - ano_nascimento < 21:
        soma_menor += 1
    else:
        soma_maior += 1
print('Tem {} menor de idade \n'
      'Tem {} maior de idade'.format(soma_menor, soma_maior))
