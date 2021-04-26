import math
print('=-'*10)
print('==== Banco Takka ====')
print('=-'*10)
cedula = 50
total_cedula = 0
sacar = int(input('Qual valor a sacar ? R$ '))
total = sacar
while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
print('=-'*10)
print('Muito obrigado, volte sempre')
