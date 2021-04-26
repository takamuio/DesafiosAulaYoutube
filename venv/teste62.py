primeiro = int(input('Digite o termo: '))
razao = int(input('Digite a razao: '))
termo = primeiro
contador = 1
total = 0
opcao = 10
while opcao != 0:
    total += opcao
    while contador <= total:
        print('{}'.format(termo), end=' -> ')
        contador += 1
        termo += razao
    print('Pausa')
    opcao = int(input('Quantos termos você quer mostrar a mais ?'))
print('Progressão finalizada com {} termos'.format(total))
