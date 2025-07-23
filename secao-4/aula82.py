def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def criar_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

print(
    executa(
        lambda x, y: x + y, 2, 3
    ),
    executa(
        soma, 2, 3
    ),
    soma(2, 3)
)

duplicar = criar_multiplicador(2)
tripicar = executa(
    lambda m: lambda n: n * m, 3
)

print(duplicar(2))
print(tripicar(2))
