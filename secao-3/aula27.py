# Fatiamento de strings
# Fatiamento [i:f:p](inicio, fim, passo) [::] 
# A funcão len retorna a quantidade de caractere da string

variavel = 'Olá, mundo'
print(variavel[0:3])
print(variavel[5:])
print(len(variavel))
print(variavel[0:(len(variavel)):1])
print(variavel[0:(len(variavel)):2])
print(variavel[::-1])
print(variavel[::-2])