n1 = 0
n2 = 1
contador = 2
print('=-'*12)
print('Sequancia de Fibonacci')
print('=-'*12)
tamanho = int(input('Quantos termos você quer ver ? '))
print('{} > {} >'.format(n1, n2), end='')
while contador != tamanho:
    n3 = n1 + n2
    print(' {} > '.format(n3), end='');
    n1 = n2
    n2 = n3
    contador += 1
print('FIM')
