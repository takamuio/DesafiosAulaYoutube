sexo = input('Qual seu sexo: [F/M] ').strip().upper()[0]
while sexo not in 'FfMm':
    sexo = input('Opção invalida. Qual seu sexo: [F/M]').strip().upper()[0]
print('Você escolheu [{}]'.format(sexo))
print('Obrigado !')