# Lista de compras
import os

lista = []
while True:
    print('Selecione uma opção:')
    opcao = input('[i]nserir [a]pagar [l]istar: ').lower()

    if opcao == 'i':
        os.system('cls')
        produto = input('Nome do produto: ')
        lista.append(produto)
        
    elif opcao == 'a':
        try:
            indice = int(input('Selecione o índice para apagar: '))
            del lista[indice]
        except (ValueError, IndexError):
            print('Não foi possível apagar esse índice!')
            
    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Não há nada para listar!')        
        else:
            for indice, nome in enumerate(lista):
                print(indice, nome)
            
    else:
        print('Selecione uma opção existente!')
    