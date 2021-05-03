def fatorial(numero, show=False):
    '''
    -> Calcula o fatorial de um numero
    :param numero: O numero a ser calculado.
    :param show: (Opicional) Mostra ou não o conta.
    :return: O valor fatorial do numero.
    '''
    f = 1
    for contador in range(numero, 0, -1):
        if show:
            print(contador, end='')
            if contador > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= contador
    return f



print(fatorial(5, True))
#help(fatorial)
