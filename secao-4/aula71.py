# Argumentos não nomeados - args
# *args (empacotamento/desempacotamento)

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args):
    total = 0
    for num in args:
        total += num
    return total

numeros = 1, 2, 3, 4, 5, 6

print(soma(*numeros)) 
print(sum(numeros))