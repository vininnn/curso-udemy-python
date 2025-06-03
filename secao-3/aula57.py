# Listas dentro de listas

pessoas = [
    # 0           1  
    ['Vinicius', 'Gustavo'], # 0
    # 0
    ['Felipe', (0, 1, 2, 3, 4)], # 1
    # 0          1       2
    ['Eduardo', 'Lana', 'João'] # 2

]

print(pessoas)
print(pessoas[0])
print(pessoas[2][0])
print(pessoas[1][1][3])

for pessoa in pessoas:
    for nomes in pessoa:
        print(nomes)