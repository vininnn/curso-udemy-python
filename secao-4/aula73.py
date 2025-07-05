# High order functions
# Funções de primeira classe

def saudacao(mensagem, nome):
    print(f'{mensagem} {nome}!')

def executar_funcao(funcao, *args):
    return funcao(*args)

executar_funcao(saudacao, 'Bom dia', 'Vinicius')