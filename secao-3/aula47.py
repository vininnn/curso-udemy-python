import os

# Palavra a ser descoberta
palavra_secreta = 'python'.upper()

# Letras descobertas/ quantidade de tentativas
letras_descobertas = ''
qtd_tentativa = 0

while True:
    tentativa = input('Digite uma letra: ').upper()

    if len(tentativa) > 1:
        print('Digite apenas uma letra!')
        continue
    elif not tentativa.isalpha():
        print('Digite uma letra válida!')
        continue

    qtd_tentativa += 1 

    if tentativa in palavra_secreta:
        letras_descobertas += tentativa

    palavra_formada = ''
    for tentativa in palavra_secreta:
        if tentativa in letras_descobertas:
            palavra_formada += tentativa
        else:
            palavra_formada += '*'
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Parabéns! Você completou a palavra!')
        print(f'A palavra secreta era: {palavra_secreta}')
        print(f'Tentativas: {qtd_tentativa}')
        break
