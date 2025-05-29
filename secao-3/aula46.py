for i in range(10):
    if i == 2:
        print('Pulando esta seção...')
        continue

    if i == 8:
        print('Encerrando o programa...')
        break

    for j in range(1, 3):
        print(i, j)

else:
    print('O programa foi encerrado naturalmente...')

