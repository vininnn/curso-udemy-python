lista = [1, 2, 3, 4]
lista.insert(0, 0)
lista.insert(5, 5)
print(lista)

# Cuidados para se ter com insert
lista.insert(100, 6)
print(lista)
# Não há uma real adição no local 100 da lista, gera um erro
# print(lista[100])
print(lista[6])