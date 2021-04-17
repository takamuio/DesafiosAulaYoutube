#escolher 1 de 4 alunos aleatoriamente
import random
n1 = input('primeiro aluno: ')
n2 = input('segundo aluno: ')
n3 = input('terceiro aluno: ')
n4 = input('quarto aluno: ')
alunos = [n1, n2, n3, n4]
escolher = random.choice(alunos)
print('O aluno escolhido foi: {}'.format(escolher))
