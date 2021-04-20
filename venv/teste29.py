velocidade = int(input('Que velocidade seu carro esta ?'))
if velocidade <= 80:
    print('Você esta dentro da velocidade !')
else:
    print('Você foi multado !')
    multa = (velocidade - 80) * 7.00
    print('Valor da multa é: R$ {:.2f}'.format(multa))