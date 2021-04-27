from random import randint
numero = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os valores sorteados foram: ', end='')
for c in numero:
    print(f'{c} ', end='')
print(f'\nO menor é {max(numero)}')
print(f'O maior é {min(numero)}')