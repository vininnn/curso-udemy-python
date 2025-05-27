# While/else
# Se tiver algum break o else não funciona

i = 0
teste = True
while i < 10:
    print(i)
    i += 1
    while teste:
        break
    else:
        print('A variável "teste" é falsa')
else:
    print('O código foi completamente executado!')
print('Fora do while.')