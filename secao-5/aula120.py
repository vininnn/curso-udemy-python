# Introdução à classses
# Classes geram objetos(instâncias) que podem ter atributos e métodos
# Por conveção classes são escritas em PascalCase

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
p1 = Pessoa('Vinicius', 'Herberts')
p2 = Pessoa('Gustavo', 'Silveira')

print(p1.nome, p1.sobrenome)
print(p2.nome, p2.sobrenome)