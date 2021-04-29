aluno = {}
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Média do aluno {aluno["nome"]}: '))
if aluno["media"] >= 7:
    aluno['situacao'] = 'APROVADO'
elif 5 <= aluno["media"] < 7:
    aluno['situacao'] = 'RECUPERAÇÂO'
else:
    aluno['situacao'] = 'REPROVADO'
print('=-'*20)
for key, valor in aluno.items():
    print(f'  - {key} é igual {valor}')