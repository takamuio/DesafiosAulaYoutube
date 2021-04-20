distancia = int(input('Qual a distancia da viagem ?'))
if distancia <= 200:
    passagem = distancia * 0.5
    print('Sua passagem custa: R$ {:.2f}'.format(passagem))
else:
    passagem = distancia * 0.45
    print('Sua passagem custa: R$ {:.2f}'.format(passagem))