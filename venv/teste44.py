valor_produto = int(input('Digite o valor do produto: '))
opcao_pagamento = int(input('Escolha a forma de pagamento: \n'
                            '[ 1 ] À vista Dinheiro/Cheque \n'
                            '[ 2 ] À vista Cartão \n'
                            '[ 3 ] Até 2x no cartão \n'
                            '[ 4 ] 3x + no cartão \n'
                            ''))
if opcao_pagamento == 1:
    print('O produto vai receber 10% de desconto !')
    total = valor_produto * 0.9
elif opcao_pagamento == 2:
    print('O produto vai receber 5% de desconto !')
    total = valor_produto * 0.95
elif opcao_pagamento == 3:
    total = valor_produto
    parcela = total / 2
    print('Sua compra sera parcelada em 2x de R$ {:.2f}'.format(parcela))
elif opcao_pagamento == 4:
    total = valor_produto * 1.2
    parcela = int(input('Quantas parcelas ?'))
    parcela_juros = total / parcela
    print('Sua compra sera parcelada em {}x de R$ {:.2f} COM JUROS'.format(parcela, parcela_juros))
else:
    total = valor_produto
    print('Opção de pagamento invalido !')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(valor_produto, total))