# Método de classe + factories

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def pessoa_50_anos(cls, nome):
        return cls(nome, 50)
    
p1 = Pessoa.pessoa_50_anos('Vinicius')
print(p1.idade)