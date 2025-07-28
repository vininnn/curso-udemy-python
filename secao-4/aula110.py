# groupby - agrupando valores (itertools)
from itertools import groupby

alunos = [
    {'nome': 'Vinicius', 'nota': 'A'},
    {'nome': 'Felipe', 'nota': 'B'},
    {'nome': 'Eduardo', 'nota': 'A'},
    {'nome': 'Cecília', 'nota': 'C'},
    {'nome': 'Lana', 'nota': 'D'},
    {'nome': 'Lucas', 'nota': 'A'},
    {'nome': 'Gabriela', 'nota': 'B'},
    {'nome': 'Gustavo', 'nota': 'A'},
    {'nome': 'Pedro', 'nota': 'C'},
]

def ordenar(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordenar)
grupos = groupby(alunos_agrupados, key=ordenar)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)