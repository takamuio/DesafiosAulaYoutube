numero = int(input('Digite um numero inteiro: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='' )
    print('{} '.format(c), end='')
print('\n\033[mo numero {} foi divisivel {} vezes'.format(numero, total))
if total == 2:
    print('Ele é PRIMO')
else:
    print('Ele NÂO é primo')
