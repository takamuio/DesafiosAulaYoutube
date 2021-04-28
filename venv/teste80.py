valores = []
for contador in range(0,5):
    numero = int(input('Digite um valor: '))
    if contador == 0 or numero > valores[-1]:
        valores.append(numero)
        print('Adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao < len(valores):
            if numero <= valores[posicao]:
                valores.insert(posicao, numero)
                print(f'Adicionado na posição {posicao} da lista...')
                break
            posicao +=1
print('=-'*20)
print(f'Os valores em ordem foram: {valores}')
