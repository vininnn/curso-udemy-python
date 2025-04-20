# Operadores lógicos
# and (e) or (ou) not (não)
# not - usado para inverter expressões
# not True = False
# not False = True

print(not True)
print(not 0)

frase = input('Digite uma frase: ')

if not frase :
    print('Você não digitou nada!')
else :
    print(f'A sua frase é: {frase}')