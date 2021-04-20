salario = float(input('Digite seu salario: '))
if salario > 1250.00:
    aumento = salario * 1.1
    print('Seu salario com aumento fica: R$ {:.2f}'.format(aumento))
else:
    aumento = salario * 1.15
    print('Seu salario com aumento fica: R$ {:.2f}'.format(aumento))