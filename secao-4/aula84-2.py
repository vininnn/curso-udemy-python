# Mapeamento e Filtro de dados em list comprehension
produtos = [
    {'nome': 'produto1', 'preco': 10},
    {'nome': 'produto2', 'preco': 20},
    {'nome': 'produto3', 'preco': 30}
]

produtos_atualizados = [
    {**produto, 'preco': produto['preco'] * 1.1}
    if produto['preco'] > 20 else {**produto} # if a esquerda do for é mapeamento
    for produto in produtos
    if produto['preco'] > 10 # if a direita do for é filtro
]

print(*produtos_atualizados, sep='\n')

