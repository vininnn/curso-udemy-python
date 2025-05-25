# Repetição
# While(enquanto)
# Executa uma ação enquanto uma condição for verdadeira

condicao = True

while condicao:
    nome = input('Qual é o seu nome? ')
    print(f'Seu nome é {nome}')

    sair = input('Quer sair? [s]sim ou [n]não ')
    if sair == 's':    
        break

print('Saiu do while!')