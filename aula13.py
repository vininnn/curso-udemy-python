nome = 'Vinicius Herberts Dal Bem'
peso_kg = 78.5
altura_metro = 1.84
imc = peso_kg / altura_metro ** 2

# Formatação de string
# f-strings
texto_1 = f'A altura de {nome} é {altura_metro} metros.'
texto_2 = f'O peso de {nome} é {peso_kg} Kg.'
texto_3 = f'O IMC de {nome} é {imc:.2f}' 

print(texto_1)
print(texto_2)
print(texto_3)
