valores = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        valores[l][c] = (int(input(f'Digite o valor em [{l},{c}]: ')))
print('=-'*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{valores[l][c]:^5}]', end='')
    print()

