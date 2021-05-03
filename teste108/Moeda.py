def dobro(valor=0):
    valor = valor * 2
    return valor


def metade(valor=0):
    valor = valor / 2
    return valor


def acrecimo (valor=0, taxa=0):
    valor = valor + (valor * taxa/100)
    return valor


def desconto (valor=0, taxa=0):
    valor = valor - (valor * taxa/100)
    return valor


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:>8.2f}'.replace('.',',')