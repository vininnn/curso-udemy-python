# Imutáveis que vimos: str, int, float, bool
# Sendo imutável, você só pode alterar o valor, mudando de variável

string = 'Vinicius'
# string[3] = 'ABC'
# print(string)
# Você não pode fazer uma atribuição de itens em tipos built-in

outra_string = f'ABC{string[3:]}'
print(outra_string)

# Método de String 
str1 = 'abc'
str2 = 'ABC'

print(str1.capitalize())
print(str1.upper())
print(str2.lower())
