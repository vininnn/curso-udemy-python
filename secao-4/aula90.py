import sys

# Generator expressions, Iterables e Iterators
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__

lista = [n for n in range(1000000)] # A lista já possui todos os seus valores armazenados 
generator = (n for n in range(1000000)) # O generator espera você 'usar' o valor para cria-lo

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))