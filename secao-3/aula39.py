# Iterando strings com while

nome = input('Qual é o seu nome? ')
novo_nome = '*'

indice = 0
while indice < len(nome):
    novo_nome += nome[indice] + '*'
    indice += 1

print(f'O seu novo nome é {novo_nome}')