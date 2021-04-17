#sortear ordem de apresentaçao de 4 alunos e mostrar qual é a ordem
import random
n1 = input('primeiro aluno: ')
n2 = input('segundo aluno: ')
n3 = input('terceiro aluno: ')
n4 = input('quarto aluno: ')
alunos = [n1, n2, n3, n4]
random.shuffle(alunos)
print('A ordem de apresentação vai ser: \n'
      '', alunos)
