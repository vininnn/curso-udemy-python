# Métodos úteis de dicionários
# len - quantas chaves
# keys - iterável com chaves
# values - iterável com valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe

pessoa = {'Nome': 'Vinicius', 'Idade': 18, 'Altura': 1.8}

print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
# Diferente do .get(), .setdefault() pode alterar o dicionário
print(pessoa.setdefault('Sobrenome', 'Não cadastrado'))
print(pessoa)
