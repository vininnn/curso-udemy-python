# Retorno de funções
# Depois que a função retorna algum valor, ela se encerra

def soma(x, y):
    print('Executando função')
    return(x + y)
    

variavel_soma = soma(1, 2)
variavel_soma2 = soma(2, 4)
print(variavel_soma)
print(variavel_soma2)
print(variavel_soma + variavel_soma2)