# Operadores
# União de conjuntos - union - todos os valores 
# Interseção - intersection - valores que ambos possuem
# Diferença - difference - valores que só o set da esquerda possui
# Diferença simétrica - symmetric_difference - valores únicos de ambos 

s1 = {1, 2, 3}
s2 = {3, 4, 5}

s3 = s1.union(s2) # s1 | s2
s4 = s1.intersection(s2) # s1 & s2
s5 = s1.difference(s2) # s1 - s2
s6 = s1.symmetric_difference(s2) # s1 ^ s2
print(s3)
print(s4)
print(s5)
print(s6)
