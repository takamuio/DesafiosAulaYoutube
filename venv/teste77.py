palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
for contador in palavras:
    print(f'\nNa palavra {contador.upper()} temos as vogais: ', end='')
    for letra in contador:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
