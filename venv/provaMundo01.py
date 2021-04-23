solucao = ['a','b','c'],\
          ['d','e','f'],\
          ['g','h','i']

soma = ''
for c in range(0,len(solucao)):
    n = solucao[c][c]
    soma += n
print(soma)
