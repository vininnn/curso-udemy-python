# Excecções Orientadas a Objetos

class MyError(Exception):
    ...

def levantar():
    excecao = MyError("Mensagem de erro")
    excecao.add_note("Errou")
    raise excecao

try:
    levantar()
except MyError as erro:
    print(erro.__class__.__name__)
    print(erro)

    levantar()