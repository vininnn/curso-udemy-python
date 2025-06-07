import re
import random
import os

print('Escolha uma oção:')
print('[0] Gerar um novo CPF.')
print('[1] Validar um CPF já existente.')
while True:    
    try:
        opcao = int(input())
        if opcao in (0, 1):
            break
        print('Opção inválida! Tente novamente.')
    except ValueError:
        print('Digite apenas números!')

os.system('cls')
cpf_base = []

# Gerador CPF
if opcao  == 0:
    for i in range(9):
        cpf_base.append(str(random.randint(0, 9)))

# Validador de CPF
else:
    print('Digite o seu CPF:')
    while True:

        entrada = re.sub(r'\D', '', input())

        if len(entrada) != 11:
            print('Um CPF deve conter 11 digitos! Tente novamente!')
        elif entrada == entrada[0] * len(entrada):
            print('Um CPF não pode ser sequencial! Tente novamente!')
        else:
            break

    cpf_base = list(entrada[:9])
    cpf_enviado = list(entrada)

# Calculando os digitos de validação
for i in range(2):
    indice = 10 + i
    soma_ponderada = 0

    for num in cpf_base:
        soma_ponderada += int(num) * indice
        indice -= 1

    resto_da_divisao = soma_ponderada % 11

    digito_validativo = 0 if resto_da_divisao < 2 else 11 - resto_da_divisao
    cpf_base.append(str(digito_validativo))
  
# Resultados
if opcao == 0:
    cpf_base.insert(3, '.')
    cpf_base.insert(7, '.')
    cpf_base.insert(11, '-')
    print('CPF gerado:', ''.join(cpf_base) )

else:
    os.system('cls')
    if cpf_base == cpf_enviado:
        print('O CPF enviado é válido!')
    else:
        print('O CPF enviado é inválido!')