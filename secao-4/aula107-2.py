# Somar listas
from itertools import zip_longest
lista1 = [1, 2, 3]
lista2 = [1.1, 2.2, 3.3, 4]

lista3 = []
def lista_maior(funcao):
    def wrapper(l1, l2):
        if len(l1) < len(l2):
            l1, l2 = l2, l1
        return funcao(l1, l2)
    return wrapper

@lista_maior
def somar_lista(l1, l2):
    for a, b in zip_longest(l1, l2, fillvalue=0):
        v = a + b
        lista3.append(v)
    
    return lista3

print(somar_lista(lista1, lista2))