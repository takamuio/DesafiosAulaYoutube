listagem = ('banana', 4.55, 'Arroz', 5.74, 'Chiclete', 0.50, 'Feijão', 8.12, 'Pão', 2, 'Frango', 12.34, 'batata', 6.98)

print('=-'*22)
print(f'{"Listagem de Preços":^40}')
print('=-'*22)

for contador in range(0, len(listagem)):
    if contador % 2 == 0:
        print(f'{listagem[contador]:.<28}', end='')
    if contador % 2 == 1:
        print(f'R$ {listagem[contador]:>7.2f}')

print('=-'*22)
