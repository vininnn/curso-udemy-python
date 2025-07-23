# Função lambda
# É uma função anônima (função sem nome)
# Deve ser contido em uma unica expressão (linha)

nomes = [
    {'nome': 'Vinicius', 'sobrenome': 'Herberts'},
    {'nome': 'Gustavo', 'sobrenome': 'Silveira'}, 
    {'nome': 'Eduardo', 'sobrenome': 'Boaro'},
    {'nome': 'Lana', 'sobrenome': 'Oyama'}
]

#def ordenar(lista):
#    return lista['nome']

nomes_em_ordem = sorted(nomes, key= lambda lista: lista['nome'])
sobrenomes_em_ordem = sorted(nomes, key= lambda lista: lista['sobrenome'])

nomes.sort(key= lambda lista: lista['nome'])

print(nomes)
print(nomes_em_ordem)
print(sobrenomes_em_ordem)
