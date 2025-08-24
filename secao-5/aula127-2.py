from aula127_1  import CAMINHO_ARQUIVO, Pessoa
import json

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    dados = json.load(arquivo)
    p1 = Pessoa(**dados[0])
    p2 = Pessoa(**dados[1])
    p3 = Pessoa(**dados[2])
    p4 = Pessoa(**dados[3])

print(p1.nome)
print(p2.nome)
print(p3.nome)
print(p4.nome)