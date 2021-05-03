import Moeda

preco = float(input('Digite o precço: R$ '))
print(f'A metade de {Moeda.moeda(preco)} é {Moeda.moeda(Moeda.metade(preco))}')
print(f'O dobro de {Moeda.moeda(preco)} é {Moeda.moeda(Moeda.dobro(preco))}')
print(f'Aumentando 10% temos {Moeda.moeda(Moeda.acrecimo(preco, 10))}')
print(f'Reduzindo 13% temos {Moeda.moeda(Moeda.desconto(preco, 13))}')