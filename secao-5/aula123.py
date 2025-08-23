# Escopo da classe

class Animal:
    def __init__(self, nome):
        self.nome = nome

    variavel = 'Texto'
    print(variavel)

    def comendo(self, alimento):
        print(f'O {self.nome} está comendo {alimento}')

leao = Animal('Leão')
print(leao.nome)
leao.comendo('carne')