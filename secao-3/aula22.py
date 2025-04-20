# Operadores lógicos
# and (e) or (ou) not (não)
# or - qualquer condição avaliada como verdadeira avalia a expressão como verdadeira
# A expressão é falsa apenas se todos as condições forem falsas
# print(True and True and True and False) = True

entrada = input('Digite [E] para entrar: ')
senha_digitada = input('Insira a senha correta: ')
senha_correta = '1234'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_correta :
    print('Você entrou!')
else :
    print('Você não entrou!')

palavra = input('Digite uma palavra (opcional): ') or 'Nada foi digitado'
print(palavra)

