from teste115 import Interface
from teste115 import Validacoes


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')    # r = Read(ler)     t = Text(arquivo texto)
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')   # w = Write(escrever)
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso !')


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        Interface.cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastro_pessoa(arq, nome_pessoa='<Desconhecido>', idade_pessoa=0):
    try:
        a = open(arq, 'at') # a = Append(Adicionar)
    except:
        print('Erro ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome_pessoa};{idade_pessoa}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome_pessoa} adicionado !')
            a.close()