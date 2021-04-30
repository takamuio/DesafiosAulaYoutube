from time import sleep

def linha():
    print('=-'*20)
def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} ao {fim} em {passo}')
    if passo < 0:
        passo = - passo
    elif passo == 0:
        passo = 1
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += passo
        print()
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= passo
        print()
        linha()
linha()
contador(1, 10, 1)
linha()
contador(10, 0, 2)
print('Você escolhe a contagem')
escolhe_inicio = int(input('Começa em: '))
escolhe_fim = int(input('Termina em: '))
escolhe_passo = int(input('Pula de quantos em quantos: '))
contador(escolhe_inicio, escolhe_fim+1, escolhe_passo)