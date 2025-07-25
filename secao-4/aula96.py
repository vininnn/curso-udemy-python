# Módulos
# import nome_modulo
# Importa o módulo inteiro
import sys
print(sys.platform)

# from nome_modulo import objeto
# Importa partes do módulo
from sys import platform
print(platform)

# alias 1 - import nome_modulo as apelido
import sys as sistema
print(sistema.platform)
# alias 2 - from nome_modulo import objeto as apelido
from sys import platform as plataforma
print(plataforma)

# from nome_modulo import *
# Má prática - importa tudo, sem prefixo
from sys import *
print(platform)


