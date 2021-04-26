contador = maior = menor = soma = 0
opcao = ''
while opcao != 'N':
    numero = int(input('Digite um numero: '))
    opcao = str(input('Quer contuinar [S/N] ?')).upper().strip()[0]
    soma += numero
    contador += 1
    if contador == 1:
            maior = menor = numero
    else:
        if numero > maior:
                maior = numero
        if numero < menor:
                menor = numero
media = soma / contador
print('Você digitou {} numeros e a media foi {:.1f}'.format(contador, media))
print('O menor numero foi {} e o maior foi {}'.format(menor, maior))