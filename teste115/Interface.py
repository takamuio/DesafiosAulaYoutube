from teste115 import Validacoes


def linha(tamanho = 42):
    return '-' * tamanho


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    contador = 1
    for item in lista:
        print(f'[ {contador} ] - {item}')
        contador += 1
    print(linha())
    opcao = Validacoes.leia_int('Sua opção: ')
    return opcao





