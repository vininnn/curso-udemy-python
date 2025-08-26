class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = []

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante.append(fabricante)

    def __str__(self):
        fabricantes = ", ".join(str(f) for f in self._fabricante)
        return f'{self.nome} | {self.motor} | {fabricantes}'


class Motor:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f'{self.nome}'


class Fabricante:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f'{self.nome}'


c1 = Carro('Palio')
c2 = Carro('Challenger')
m1 = Motor('V12')
f1 = Fabricante('Volkswagen')
f2 = Fabricante('Dodge')
f3 = Fabricante('Genérica')

c1.motor = m1
c1.fabricante = f1
c1.fabricante = f3

c2.motor = m1
c2.fabricante = f2
c2.fabricante = f3

print(c1)
print(c2)