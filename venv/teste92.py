from datetime import datetime
dicionario = {}
dicionario['nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano nascimento: '))
dicionario['idade'] = datetime.now().year - ano_nascimento
dicionario['carteira_trabalho'] = int(input('Carteira de trabalho (0 não tem): '))
if dicionario['carteira_trabalho'] != 0:
    ano_contratacao = 0
    ano_minimo_trabalho = ano_nascimento + 16
    while ano_contratacao < ano_minimo_trabalho:
        ano_contratacao = int(input('Ano da contratação: '))
        if ano_contratacao >= ano_minimo_trabalho:
            dicionario['contratacao'] = ano_contratacao
        else:
            print('Ano de contratação invalida !')
    calcular_aposentadoria = (dicionario['contratacao'] - ano_nascimento) + 35
    dicionario['aponsentadoria'] = calcular_aposentadoria
    dicionario['salario'] = float(input('Salário: '))
print('=-'*20)

for keys, valores in dicionario.items():
    print(f'{keys} tem o valor {valores}')
