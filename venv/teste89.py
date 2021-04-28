ficha = []
while True:
    nome = str(input('Nome: '))
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    ficha.append([nome ,[nota_1, nota_2], media])
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = str(input('Você quer continuar ? [S/N] ')).upper().strip()[0]
    if opcao in 'Nn':
        break
print('=-'*20)
print(f'{"N°":<4}{"NOME":<10}{"MÈDIA":>8}')
print('-'*26)
for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('=-'*20)

    mostrar_nota = int(input('Mostrar nota de qual aluno ? [999 interronpe] '))
    if mostrar_nota == 999:
        print('Saindo do sistema')
        break
    if mostrar_nota <= len(ficha) - 1:
        print(f'Notas de {ficha[mostrar_nota][0]} são {ficha[mostrar_nota][1]}')
