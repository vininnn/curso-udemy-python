# Dictionary comprehension e set comprehension

produto = {
    'nome': 'agua',
    'preco': 1.99,
    'categoria': 'alimento'
}

novo_produto = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != 'categoria'
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor b')
]

dc = {
    chave: valor
    for chave, valor in lista
}

print(novo_produto)
print(dc)