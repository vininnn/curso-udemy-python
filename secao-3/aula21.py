# Operadores lógicos
# and (e) or (ou) not (não)
# and - todas as condições precisam ser verdadeiras
# Se qualquer condição ser falsa, a expressão inteira não será satisfeita, ou seja, terá o valor False
# print(True and True and True and False) = False
# Representações de falsy = 0, 0.0, '', false
# Também a o dado None, ele é a representação de um não-valor

entrada = input('Digite [E] para entrar: ')
senha_digitada = input('Insira a senha correta: ')
senha_correta = '1234'

if entrada == 'E' and senha_digitada == senha_correta :
    print('Você entrou!')
else :
    print('Você não entrou!')

