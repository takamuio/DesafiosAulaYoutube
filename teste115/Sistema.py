from teste115 import Interface
from teste115 import Validacoes
from teste115 import Arquivo
from time import sleep

arq = 'listapessoas.txt'

if not Arquivo.arquivo_existe(arq):
    Arquivo.criar_arquivo(arq)

while True:
    respota = Interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do programa'])
    if respota == 1:
        Arquivo.ler_arquivo(arq)
    elif respota == 2:
        Interface.cabecalho('NOVO CADASTRO')
        nome = Validacoes.leia_str('Nome:')
        idade = Validacoes.leia_int('Idade: ')
        Arquivo.cadastro_pessoa(arq, nome, idade)
    elif respota == 3:
        Interface.cabecalho('Saindo do sistema')
        break
    else:
        print(f'\033[0;31mErro ! Opção invalida.\033[m')
    sleep(1.5)
