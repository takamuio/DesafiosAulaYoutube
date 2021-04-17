altura = float(input('Digite a altura de uma parede: '))
largura = float(input('Digite a largura de uma parede: '))
area = altura * largura
tinta = area / 2
print('Você vai usar {:.2f} Lt de tintas para {:.2f} m²'.format(tinta, area))
