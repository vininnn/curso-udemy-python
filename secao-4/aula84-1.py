# list comprehension

print(list(range(10)))

lista = []
for num in range(10):
    lista.append(num)
print(lista)

lista = [
    num * num
    for num in range(10)
]
print(lista)

