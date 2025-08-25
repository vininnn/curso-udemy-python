# Encapsulamento e modificadores de acesso
# public, protected, private
# _ = protected, __ = private

class Acess:
    def __init__(self):
        self.public = 'Isso é público'
        self._protected = 'Isso é protegido'
        self.__private = 'Isso é privado'

    def metodo_publico(self):
        print('Método público')

    def _metodo_protected(self):
        print('Método protegido')

    def __metodo_private(self):
        print('Método privado')

a = Acess()
print(a.public)
print(a._protected)
print(a.public)

