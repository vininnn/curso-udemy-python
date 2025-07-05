#def duplicar(numero):
#    return numero * 2
#def triplicar(numero):
#    return numero * 3
#def quadruplicar(numero):
#    return numero * 4

def criar_multiplicador(multiplicar):
    def multiplicador(numero):
        return numero * multiplicar
    return multiplicador

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

numero = int(input('Digite um número: '))

print('Número duplicado:', duplicar(numero))
print('Número triplicado:', triplicar(numero))
print('Número quadruplicado:', quadruplicar(numero))