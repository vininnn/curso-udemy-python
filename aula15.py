# nome = input('Qual é o seu nome? ')
# print(f'O seu nome é {nome}')

# Essas maneira são um pouco controversas, principalmente a segunda, pois, se o usuário digitrar por exemplo 'a', o programa vai dar erro logo no inicio, não deixando brecha para corrigir posteriormente.

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

print(f'A soma dos número é {int(numero_1) + int(numero_2)}')

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))

print(f'A soma dos número é {numero_1 + numero_2}')

# Melhor abordagem:

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos número é {int_numero_1 + int_numero_2}')