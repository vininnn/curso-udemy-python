import json

CAMINHO_ARQUIVO = 'C:\\Documents\\Estudos\\Udemy\\curso-python\\secao-5\\aula127.json'

class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    
p1 = Pessoa('Vinicius', 'Herberts Dal Bem', 18)
p2 = Pessoa('Eduardo', 'Boaro Gouveia', 18)
p3 = Pessoa('Gustavo', 'Silveira Guedes', 17)
p4 = Pessoa('Lana Yuna', 'Oyama', 18)
bd = (vars(p1), vars(p2), vars(p3), vars(p4))

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)
