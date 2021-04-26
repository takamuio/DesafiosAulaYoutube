while True:
    numero = int(input('Quer ver a tabuada de qual valor ? '))
    if numero < 0:
        break
    for c in range (1, 11):
        print(f'{numero} X {c} = {numero * c}')
    print('-='*10)
print('Tabuada Finalizada')