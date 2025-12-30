# Enum -> Enumerador
# Conjunto de nomes simbólicos que representam um valor único
# enum.Enum é uma superclasse para enumerações, apesar de poder ser usadas normalmente

import enum

# Direcoes =  enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA']) 

class Direcoes(enum.Enum):
    ESQUERDA = 1
    DIREITA = 2

print(Direcoes(1), Direcoes['Esquerda'], Direcoes.ESQUERDA)
print(Direcoes(1).name, Direcoes.ESQUERDA.value)

def mover(direcao):
    print(f'Movendo para {direcao}')

mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
