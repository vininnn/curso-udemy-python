# Sets - conjuntos (matemática) em python (tipo set)
# Mutáveis porém só aceitam valores imutáevis dentro deles

#s1 = set('Vinicius')
#s1 = {'Vinicius'}
#s1 = set() # vazio
#s1 = {'Oi', 1, 2, 3} # com dados

# Seus valores sempre são únicos
# Não têm índices
# Não garantem ordem
# São iteráveis

l1 = [1, 2, 2, 3, 3, 33]
s1 = set(l1)
l2 = list(s1)
print(l2)

s1.add(4)
s1.add('Vini')
print(s1)

s1.update((1, 2, 3, 4, 5), range(8), 'Vini')
print(s1)

s1.discard(33)
s1.discard('Vini')
print(s1)
