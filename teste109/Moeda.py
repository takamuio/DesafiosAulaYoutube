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