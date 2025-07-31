# Problema dos parâmetros mutáveis em funções Python
def adiciona_clientes(nome, lista=None): # Não deixar lista=[]
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('Vinicius')
adiciona_clientes('Gustavo', cliente1)
adiciona_clientes('Eduardo', cliente1)
cliente1.append('Lana')

cliente2 = adiciona_clientes('Felipe')
adiciona_clientes('Pedro', cliente2)

cliente3 = adiciona_clientes('Gabriela')
adiciona_clientes('Cecília', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)