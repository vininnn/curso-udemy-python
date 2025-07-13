# Métodos úteis de dicionários
# copy - retorna uma cópia rasa (shallow copy)

d1 = {'valor1': 1, 'valor2': 2, 'lista1': [0, 1, 2]}

d2 = d1
d2['valor1'] = 0

print(d1)

# shallow copy não copia valores mutáveis (listas ou dicionários)
# Ou seja, quando eu alterar um valor mutável, ele altera de todas as listas associadas
# Caso realmente queira fazer a cópia de mutáveis, é necessário importar o módulo copy e usar copy.deepcopy
d3 = d2.copy()
d3['valor1'] = 3
d3['lista1'][2] = 15

print(d2)
print(d3)