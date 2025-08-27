# Herança simples
# Ligação entre classes

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def mostrar_dados(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    ...

class Aluno(Pessoa):
    ...

c1 = Cliente('Vinicius', 'Herberts')
a1 = Aluno('Gustavo', 'Silveira')

c1.mostrar_dados()
a1.mostrar_dados()