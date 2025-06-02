lista = ['Vinicius', 'Eduardo', 'Gustavo']
lista_enumerada = enumerate(lista)

for item in lista_enumerada:
    print(item)

print('O que tem na lista enumerada: ', lista_enumerada)
# Nesse caso o iterador já foi usado, então ele esgota

# O ideal seria no caso, colocar o enumerate dentro do for
# Aqui ainda tem desempacotamento
for indice, nome in enumerate(lista):
    print(indice, nome)  

# for item in enumerate(lista):
#    indice, nome = item
#    print(indice, nome) 

# for tupla_enumerada in enumerate(lista):
#     for valor in tupla_enumerada:
#        print(valor)