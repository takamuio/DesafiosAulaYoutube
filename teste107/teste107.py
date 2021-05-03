import Moeda

preco = float(input('Digite o preço: R$ '))
print(f'A metade de {preco} é {Moeda.metade(preco)}')
print(f'o dobro de {preco} é {Moeda.dobro(preco)}')
print(f'Aumentando 10% temos {Moeda.acrecimo(preco, 10)}')
print(f'Reduzindo 13% temos {Moeda.desconto(preco, 13)}')