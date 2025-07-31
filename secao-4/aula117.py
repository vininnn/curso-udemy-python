import json

pessoa = {
    'nome': 'Vinicius',
    'sobrenome': 'Herberts',
    'enderecos': [
        {'rua': 'R1', 'numero': 123},
        {'rua': 'R2', 'numero': 456},
    ],
    'altura': 1.8,
    'numeros_preferidos': (8, 9, 15),
    'dev': True,
    'nada': None,
}

caminho_arquivo = 'C:\\Documents\\Estudos\\Udemy\\curso-python\\secao-4\\'
caminho_arquivo += 'aula117.json'

with open(caminho_arquivo, 'w') as arquivo:
    json.dump(pessoa, arquivo)

with open(caminho_arquivo, 'r') as arquivo:
    pessoa = json.load(arquivo)

print(pessoa)
