qtd_dezena = 2
qtd_unidade = 10

dezena = 0
while dezena <= qtd_dezena:
    unidade = 0
    while unidade < qtd_unidade:
        print(dezena,'', unidade)
        unidade += 1
    dezena += 1

print('Acabou!')