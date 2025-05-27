# Calculadora com While

while True:
    try:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        num_valido = True
    except:
        print('Algum dos números digitados são inválidos! Tente novamente!')
        continue

    while True:
        operador = input('Digite o operador(+, -, *, /): ')
        op_permitidos = '+-*/'

        if operador in op_permitidos:
            break
        print('O operador digitado é inválido! Tente novamente!')

    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    else:
        if num2 == 0:
            print('Erro por divisão de 0!')
            continue
        resultado = num1 / num2   

    print(f'Resultado: {resultado}') 

    sair = input('Deseja sair? [S]sim ').upper().startswith('S')

    if sair is True:
        break

print('Fim do programa!')