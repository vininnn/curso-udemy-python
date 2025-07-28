# Unir listas

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'Rj']
uniao = []

def lista_menor(funcao):
    def wrapper(lista1, lista2):
        if len(lista1) > len(lista2):
            lista1, lista2 = lista2, lista1
        return funcao(lista1, lista2)
    return wrapper

@lista_menor
def unir_listas(lista1, lista2):
    uniao = list(zip(lista1, lista2))
    return uniao

#print(list(zip(lista1, lista2)))
#print(list(zip_longest(lista1, lista2)))
print(unir_listas(cidades, estados))