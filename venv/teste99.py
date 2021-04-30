from time import sleep

def maior(* numeros):
    print('Analisando os varoles passados...')
    for contador in numeros:
        print(f'{contador} ', end='')
        sleep(0.3)
    print(f'Foram informados {len(numeros)} valores ao todo.')
    print(f'O maior valor informado foi {max(numeros)}')
    print('=-'*20)
    sleep(1)
print('=-'*20)
maior(9, 4, 6, 2, 12, 7)
maior(5, 1, 7)
maior(6)
maior()