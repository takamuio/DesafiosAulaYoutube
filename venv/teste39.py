from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input('Digite seu ano de nascimento: '))
calcular_idade = ano_atual - ano_nascimento

print('Quem nasceu em {} tem {} anos em {}'.format(ano_nascimento, calcular_idade, ano_atual))

if calcular_idade < 18:
    saldo = 18 - calcular_idade
    ano = ano_atual + saldo
    print('Você ainda vai ter que se alistar em {} anos !'.format(saldo))
    print('Seu alistamento será em {}'.format(ano))
elif calcular_idade == 18:
    print('Esta na hora de se alistar !')
elif calcular_idade > 18:
    saldo = calcular_idade - 18
    ano = ano_atual - saldo
    print('Ja passou {} anos do seu alistamento !'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano))
