comandos = ['listar', 'refazer', 'desfazer']
lista_de_tarefas = []
lista_refazer = []

def tarefas():
    print('Tarefas:')
    print(*lista_de_tarefas, sep='\n')
    print()

while True:
    print('Comandos: listar, refazer, desfazer')
    entrada = str(input('Digite um comando ou tarefa! ')).lower()
    print()

    if entrada in comandos:

        if entrada == 'listar':
            tarefas()

        elif entrada == 'refazer':
            if not lista_refazer:
                print('Não há nada para refazer!')
            else:
                refazer = lista_refazer.pop()
                lista_de_tarefas.append(refazer)
            tarefas()
            
        else:
            if not lista_de_tarefas:
               print('Não há nada para desfazer!')
            else:
                desfazer = lista_de_tarefas.pop()
                lista_refazer.append(desfazer)
            tarefas()
    else:
        lista_de_tarefas.append(entrada)
        tarefas()
