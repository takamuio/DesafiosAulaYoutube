valor_da_casa = float(input('Valor da casa: R$ '))
salario = float(input('Salario do comprador: R$ '))
anos = int(input('Quantos anos de financiamento ?'))

prestacao = valor_da_casa / (anos * 12)

print('Para pagar uma casa de R$ {:.2f} em {} anos \n'
      'A prestação sera R$ {:.2f}'.format(valor_da_casa, anos, prestacao))

if (salario * 0.3) > prestacao:
    print('Seu financiamento foi aprovado !')

else:
    print('Seu financiamento não foi aprovado')
    print('A parcela seria maior que 30% seu salario !')
