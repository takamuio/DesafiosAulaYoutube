def area(larg, compr):
    calcular_area = larg * compr
    print(f'A area do um terreno de {larg} x {compr} é de {calcular_area}m²')


print('Controle de terrenos ')
print('=-'*20)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))

area(largura, comprimento)