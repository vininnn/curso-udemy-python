lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
    
print(lista)

lista2 = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(lista2)

lista3 = [
    [letra for letra in 'Vini']
    for execucao in range(3)
]

print(lista3)