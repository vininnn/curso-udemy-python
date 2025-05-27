frase = input('Digite a frase a ser analisada: ').upper()

i = 0
quant_rep = 0
letra = frase[i]
while i < len(frase):
    if (letra != ' ') and (quant_rep < frase.count(frase[i])):
        letra = frase[i]
        quant_rep = frase.count(frase[i])

    i += 1

print(f'A letra que mais repetiu foi "{letra}" com {quant_rep} repetições!')
