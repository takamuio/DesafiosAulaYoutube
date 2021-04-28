valores = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = soma_coluna = maior =0
tamanho_lista = range (0,3)

for linha in tamanho_lista:
    for coluna in tamanho_lista:
        valores[linha][coluna] = (int(input(f'Digite o valor em [{linha},{coluna}]: ')))
print('=-'*20)
for linha in tamanho_lista:
    for coluna in tamanho_lista:
        print(f'[{valores[linha][coluna]:^5}]', end='')
        if valores[linha][coluna] % 2 == 0:
            soma_par += valores[linha][coluna]
    print()
print('=-'*20)
print(f'A soma dos valores pares é {soma_par}')
for linha in tamanho_lista:
    soma_coluna += valores[linha][2]
print(f'A soma dos valores da terceira coluna é {soma_coluna}')
for coluna in tamanho_lista:
    if valores[1][coluna] > maior:
        maior = valores[1][coluna]
print(f'O maior valor da segunda linha é {maior}')