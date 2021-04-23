termo = int(input('Digite o termo: '))
razao = int(input('Digite a razao: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('Acabou')

