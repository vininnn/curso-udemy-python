import copy

produtos = [
    {'nome': 'Pão Melão', 'preco': 17.00},
    {'nome': 'Pão Francês', 'preco': 14.00},
    {'nome': 'Pão Integral', 'preco': 24.00},
    {'nome': 'Pão de Batata', 'preco': 16.40}
]

novos_produtos = copy.deepcopy(produtos)
for produto in novos_produtos:
    produto['preco'] = round(produto['preco'] * 1.1, 2)

produtos_ordem_nome = sorted(copy.deepcopy(novos_produtos), key= lambda lista: lista['nome'])
produtos_ordem_preco = sorted(copy.deepcopy(novos_produtos), key= lambda lista: lista['preco'])

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordem_nome, sep='\n')
print()
print(*produtos_ordem_preco, sep='\n')