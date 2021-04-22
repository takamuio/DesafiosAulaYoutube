t1 = int(input('Digite o valor da linha 1 do triangulo: '))
t2 = int(input('Digite o valor da linha 2 do triangulo: '))
t3 = int(input('Digite o valor da linha 3 do triangulo: '))

if t1 + t2 > t3 and t1 + t3 > t2 and t2 + t3 > t1:
    if t1 == t2 == t3:
        print('Estas linhas formam um triangulo equilátero')
    elif t1 == t2 != t3  or t1 == t3 != t2 or t3 == t2 != t1:
        print('Estas linhas formam um triangulo isósceles')
    elif t1 != t2 != t3 != t1:
        print('Estas linhas formam um triangulo escaleno')
else:
    print('Estas linhas não formam um triangulo !')