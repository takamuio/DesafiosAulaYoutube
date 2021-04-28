exprecao = str(input('Digite uma expreção numerica: '))
lista = []
for simbolo in exprecao:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expreção esta correta !')
else:
    print('Sua expreção esta incorreta !')
