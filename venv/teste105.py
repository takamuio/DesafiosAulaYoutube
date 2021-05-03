def notas(* valores, situacao=False):
    '''
    -> Função para analizar notas e situações de varios alunos.
    :param valores: Uma ou mais notas de alunos (aceita X notas).
    :param situacao: (Opicional) Pode ou não mostrar situação da turma em relação a média.
    :return: Dicionario com varias informações da turma.
    '''
    turma = {}
    turma['total'] = len(valores)
    turma['maior'] = max(valores)
    turma['menor'] = min(valores)
    turma['media'] = sum(valores)/len(valores)
    if situacao:
        if turma['media'] >= 7:
            turma['situacao'] = 'Boa'
        elif turma['media'] >= 5:
            turma['situacao'] = 'Razoável'
        else:
            turma['situacao'] = 'Ruim'
    return turma


resposta = notas(5.5, 2.5, 9.5, 10, 7.6, situacao=True)
print(resposta)
#help(notas)