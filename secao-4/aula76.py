# Dicionatios em python dictionary
# Dicionarios são estruturas do tipo par de chave e valor
# Criar dict() ou {}
# Tipo mutável

#pessoa = dict(nome= 'Vinicius', sobrenome= 'Herberts Dal Bem')
pessoa = {'nome': 'Vinicius',
           'sobrenome': 'Herberts',
           'idade': 18,
           'altura': 1.8,
           'endereço': [
               {'rua_1': 'tal tal', 'numero': 123},
               {'rua_2': 'tal tal tal', 'numero': 456}
            ]}

for chave in pessoa:
    print(f'{chave}: {pessoa[chave]}')