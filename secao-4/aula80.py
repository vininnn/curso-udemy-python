def primeira_repeticao(lista):
    repetidos = set()
    for num in lista:
        if lista.count(num) >= 2:
            repetidos.add(num)

    if not repetidos:
        return -1
    else:
        repeticao = {}
        for num in repetidos:
            repeticao[num] = []

        for num in repetidos:
            for j in range(len(lista)):
                if lista[j] == num:
                    repeticao[num].append(j)

        for num in repetidos:
            del repeticao[num][0]

        primeira_rep = len(lista)
        for num in repetidos:
            if repeticao[num][0] < primeira_rep:
                primeira_rep = repeticao[num][0]
                valor = num

        return valor

primeiras_repeticoes = []
cnjt_listas = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
]

for listas in cnjt_listas:
    primeiras_repeticoes.append(primeira_repeticao(listas))

print(primeiras_repeticoes)
