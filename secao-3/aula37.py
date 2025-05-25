contador = 0

while contador <= 20:
    contador += 1

    if (contador > 8) and (contador < 12):
        continue

    print(contador)

    if contador == 16:
        break

print('Acabou!')