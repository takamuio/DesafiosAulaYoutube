valores = []
for contador in range(0,5):
    numero = int(input(f'Digite um numero na posição {contador}: '))
    valores.append(numero)
print('=-'*20)
print(f'Você digitou os valores: {valores}')
print(f'O maior numero é {max(valores)} nas posições: ', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}..', end='')
print()
print(f'O maior numero é {min(valores)} nas posições: ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}..', end='')
