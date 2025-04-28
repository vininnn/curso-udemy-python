# Introdução ao try / except
# try -> tentar executar o código
# except -> ocorreu algum erro ao tentar executar

numero = input('Digite o número que você quer dobrar: ')

try :
    numero_float = float(numero)
    print(f'O dobro de {numero_float} é {numero_float * 2}')
except :
    print('Você não digitou um número!')

#if numero.isdigit() :
#    numero_float = float(numero)
#    print(f'O dobro de {numero_float} é {numero_float * 2}')
#else :
#    print('Você não digitou um número!')
    

