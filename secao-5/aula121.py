# Métodos de instâncias de classes Python

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def imprimir(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.imprimir()


