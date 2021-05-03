def dobro(valor=0, formatacao=False):
    resposta = valor * 2
    return resposta if not formatacao else moeda(resposta)


def metade(valor=0, formatacao=False):
    resposta = valor / 2
    return resposta if not formatacao else moeda(resposta)


def acrecimo (valor=0, taxa=0, formatacao=False):
    resposta = valor + (valor * taxa/100)
    return resposta if not formatacao else moeda(resposta)


def desconto (valor=0, taxa=0, formatacao=False):
    resposta = valor - (valor * taxa/100)
    return resposta if not formatacao else moeda(resposta)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:>8.2f}'.replace('.',',')


def resumo(valor=0, taxa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preco analisado: \t{moeda(valor)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Aumentando {taxa}%: \t{acrecimo(valor, taxa, True)}')
    print(f'Reduzindo {taxar}%: \t\t{desconto(valor, taxar, True)}')
    print('-' * 30)