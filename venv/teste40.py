n1 = float(input('Digite a N1 do aluno: '))
n2 = float(input('Digite a N2 do aluno: '))
n3 = float(input('Digite a N3 do aluno: '))

media = (n1 + n2 + n3) / 3

if media <= 5.0:
    print('Sua média foi: {:.1f}'.format(media))
    print('REPROVADO')
elif media > 5.0 or media <= 6.9:
    print('Sua média foi: {:.1f}'.format(media))
    print('RECUPERAÇÃO')
else:
    print('Sua média foi: {:.1f}'.format(media))
    print('APROVADO')