# Métodos úteis de dicionários
# get - obtém um chave
# pop - apaga um item com uma chave específica
# popitem - apaga o último item adicionado
# update - atualiza um dicionário com outro

pessoa = {'Nome': 'Vinicius', 'Idade': 18, 'Altura': 1.8}

print(pessoa.get('Sobrenome', 'Não cadastrado'))
print(pessoa)

nome = pessoa.pop('Nome')
print(nome)
print(pessoa)

ultima_chave = pessoa.popitem()
print(ultima_chave)
print(pessoa)

lista = [['Nome', 'Gustavo'], ['Idade', 17]]
pessoa.update(lista)
print(pessoa)
