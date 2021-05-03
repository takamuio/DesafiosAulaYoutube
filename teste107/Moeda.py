def dobro(valor):
    valor = valor * 2
    return valor


def metade(valor):
    valor = valor / 2
    return valor


def acrecimo (valor, taxa):
    valor = valor + (valor * taxa/100)
    return valor


def desconto (valor, taxa):
    valor = valor - (valor * taxa/100)
    return valor