# Operadores in e not in
# strings são iteráveis
# 0 1 2 3 4 5 6 7
# V i n i c i u s
# -8-7-6-5-4-3-1

nome = 'Vinicius'

print(nome[4])

print('Vin' in nome)
print('vin' in nome)
print('Vin' not in nome)
print('vin' not in nome)

nome = input('Digite o seu nome: ')
procurar = input('O que deseja procurar em seu nome? ')

if procurar in nome :
    print(f'Em seu nome há "{procurar}"!')
else :
    print(f'Em seu nome não há "{procurar}"!')




