# Multiplicar os valores recebidos
def multiplicar(*args):
    total = 1
    for num in args:
        total *= num

    return total

lista_numeros = []
print('Digite os números que deseja multiplicar. Digite [s] para calcular:')
while True:
    numeros_para_multiplicar = input()
    try:
        lista_numeros.append(int(numeros_para_multiplicar))
    except ValueError:
        if numeros_para_multiplicar.lower() != 's':
            print('Digite um valor válido!')
        else:
            if len(lista_numeros) >= 2:
                break
            print('Digite pelo menos dois números!')

resultado = multiplicar(*lista_numeros)
print(resultado)


# Ímpar ou par
def impar_par(numero):
    if (numero % 2) == 0:
        return 'Par'
    return 'Ímpar'

while True:
    try:
        numero = int(input('Número para verificar: '))
        break
    except ValueError:
        print('Digite um número!')

print(impar_par(numero))