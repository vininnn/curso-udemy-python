# isinstance() - função que checa se um objeto é de determiando tipo

lista = [
    'a', 1, 1.1, True, ['lista',], ('tupla',), {'dicionario': 'dict',}, {0, 1}
]

for i in lista:
    if isinstance(i, str):
        print(i, 'é uma string')
    if isinstance(i, int):
        print(i, 'é um inteiro')
    if isinstance(i, float):
        print(i, 'é um float')
    if isinstance(i, bool):
        print(i, 'é um booleano')
    if isinstance(i, list):
        print(i, 'é uma lista')
    if isinstance(i, tuple):
        print(i, 'é uma tupla')
    if isinstance(i, dict):
        print(i, 'é um dicionário')
    if isinstance(i, set):
        print(i, 'é um set')