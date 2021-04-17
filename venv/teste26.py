frase = str(input('Digite uma frase: ')).lower().strip()
print('existe {} A na frase'.format(frase.lower().count('a')))
print('O primeiro A esta na posição {}'.format(frase.find('a')+1))
print('O ultimo A esta na posição {}'.format(frase.rfind('a')+1))