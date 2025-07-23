# kwargs - keywords arguments (argumentos nomeados)

pessoa = {
    'nome': 'Vinicius',
    'sobrenome': 'Herberts'
}

dados_pessoa = {
    'idade': 18,
    'altura': 1.8
}

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)

def mostrar_argumentos_nomeados(*args, **kwargs):
    print('Valores não nomeados:', args)
    print('Valores nomeados:', kwargs)
    
    for chave, valor in kwargs.items():
        print(chave, valor)

mostrar_argumentos_nomeados('Bom dia', 123, nome='Vinicius', idade=18)

argumentos = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3
}

mostrar_argumentos_nomeados(argumentos, **argumentos)