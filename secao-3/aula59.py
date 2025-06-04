# Desempacotamento em chamadas de métodos de função

string = 'ABCD'
lista = ['Vinicius', 'Eduardo', (1, 2, 3, 4), 'Gustavo']
tuplas = 'Python', 'é', 'uma', 'linguagem'

a, b, *_ = string
print(a, b)
p, *_, u = lista
print(p, u)

for nome in lista:
    print(nome, end=' ')

print(*lista)
print(*string)