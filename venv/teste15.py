dias = int(input('Quantos dias ficou alugado ?'))
km = float(input('Quantos Kms foi rodado ?'))
aluguel_dia = dias * 60
aluguel_km = km * 0.15
aluguel = aluguel_dia + aluguel_km
print('Você deve : {:.2f}'.format(aluguel))
