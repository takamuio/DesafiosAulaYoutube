numero = int(input('Digite um numero: '))
opcao = int(input('Escolha qual sera a base de conversão: \n'
                  '[ 1 ] binario \n'
                  '[ 2 ] octal \n'
                  '[ 3 ] hexadecimal \n'
                  ''))

if opcao == 1:
    print('O numero {} em BINARIO é {}'.format(numero, bin(numero)))
elif opcao == 2:
    print('o numero {} em OCTAL é {}'.format(numero, oct(numero)))
elif opcao == 3:
    print('O numero {} em HEXADECIMAL é {}'.format(numero, hex(numero)))
else:
    print('Opçao não valida ! \n'
          'Tente novamente')