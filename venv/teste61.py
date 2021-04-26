primeiro = int(input('Digite o termo: '))
razao = int(input('Digite a razao: '))
termo = primeiro
contador = 1
while contador <= 10:
    print('{}'.format(termo), end=' -> ')
    contador += 1
    termo += razao

