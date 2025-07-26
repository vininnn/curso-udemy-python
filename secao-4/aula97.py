# Modularização
# O python só reocnhece arquivos abaixo do __main__
# Dai precisaria acessar por meio do sys.path
import aula97m

print('Este módulo se chama:', __name__)
print(aula97m.a)