t1 = int(input('Digite o valor de uma linha: '))
t2 = int(input('Digite o valor de uma linha: '))
t3 = int(input('Digite o valor de uma linha: '))
if ((t1 + t2) > t3) and ((t1 + t3) > t2) and ((t2 + t3) > t1):
    print('Estas linhas formam um triangulo !')
else:
    print('Estas linhas não formam um triangulo !')