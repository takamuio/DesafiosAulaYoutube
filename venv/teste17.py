import math
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
print('O valor da hipotenusa desse triangulo retangulo é: {:.2f}'.format(math.hypot(cateto_oposto, cateto_adjacente)))
