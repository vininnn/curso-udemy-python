# @property, @setter

class Caneta:
    def __init__(self, cor):
        self._cor= cor # Variáveis que começam com _ ou __ são convencionados a apenas serem usados dentro da classe

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        self._cor = valor
    

c1 = Caneta('Azul')
print(c1.cor)
c1.cor = 'Rosa'
print(c1.cor)