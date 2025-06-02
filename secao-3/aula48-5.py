# Cuidado com dados mutáveis
# Copiando valor (imutável)
# Aponta para o mesmo valor na memória (mutável)

a = 'Vinicius'
b = a
print(b)
a = 'Eduardo'
print(b)

lista_a = ['Vinicius', 'Eduardo']
lista_b = lista_a
print(lista_b)

lista_a[0] = 'Gustavo'
print(lista_b)