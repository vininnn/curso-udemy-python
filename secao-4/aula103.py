# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# São açúcar sintáticos - sintactic sugar

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print('Você foi decorado')
        return resultado
    return interna

@criar_funcao # sintactic sugar
def inverte_string(string):
    return string[::-1]


def e_string(parametro):
    if not isinstance(parametro, str):
        raise TypeError('O parâmetro deve ser uma string')

invertida = inverte_string('123')
print(invertida)