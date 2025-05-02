# Ímpar ou par
entrada = input('Digite um número inteiro: ')

try:
    numero = int(entrada)
except:
    print('Você não digitou um número inteiro!')
else:   
    if numero % 2 == 0:
        tipo_numero = 'par'
    else:
        tipo_numero = 'ímpar'
    
    print(f'O número que você digitou ({numero}) é {tipo_numero}!')

# Mensagem para hora
entrada = input('Digite a hora atual: ')

try:
    hora = int(entrada)
except:
    print('Você não digitou uma hora válida!')
else:
    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora <= 17:
        print('Boa tarde!')
    elif hora < 24:
        print('Boa noite!')
    else: 
        print('Você não digitou uma hora válida!')

# Tamanho do nome
nome = input('Qual é o seu primerio nome? ')

if not nome.isalpha():
    print('Sintaxe de nome inválida!')
else:
    if len(nome) <= 4:
        print('O seu nome tem um tamanho curto!')
    elif len(nome) <= 6:
        print('O seu nome tem um tamanho intermediário!')
    else:
        print('O seu nome tem um tamanho grande!')

