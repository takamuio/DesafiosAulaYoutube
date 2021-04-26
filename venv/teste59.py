from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
opcao = 0
while opcao != 5:
    print('==== Menu ====\n'
          '[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] Maior\n'
          '[4] Novos numeros\n'
          '[5] Sair do programa')
    opcao = int(input('Digite a opção: '))
    if opcao == 1:
        print('A soma do {} + {} = {}'.format(n1, n2, n1+n2))
    elif opcao == 2:
        print('A multiplicação de {} X {} = {}'.format(n1, n2, n1*n2))
    elif opcao == 3:
        if n1 > n2:
            print('O numero {} é maior que {}'.format(n1, n2))
        else:
            print('O numero {} é maior que {}'.format(n2, n1))
    elif opcao == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite um valor: '))

    else:
        print('Opção invalida, tente novamente !')
    print('=-=' * 10)
    sleep(1.5)
print('Programa finalizado !')
