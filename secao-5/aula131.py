# @property, getter - método para obter atributo
# Método que se comporta como atributo

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        return self.cor_tinta
    
c1 = Caneta('Azul')
print(c1.cor_tinta)
print(c1.cor)