import Moeda

preco = float(input('Digite o precço: R$ '))
print(f'A metade de {Moeda.moeda(preco)} é {Moeda.metade(preco, True)}')
print(f'O dobro de {Moeda.moeda(preco)} é {Moeda.dobro(preco, True)}')
print(f'Aumentando 10% temos {Moeda.acrecimo(preco, 10, True)}')
print(f'Reduzindo 13% temos {Moeda.desconto(preco, 13, True)}')