from UtilidadesCeV import Moeda
from UtilidadesCeV import Dado

preco = Dado.leia_dinheiro('Digite o preço: R$ ')
Moeda.resumo(preco, 20, 30)