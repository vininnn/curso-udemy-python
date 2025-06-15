# Introdução ás funções (def)
# São trechos de códigos usados para replicar uma determinada ação ao longo do programa
# Elas recebem valores para parâmetros (argumentos) e retornam um valor específico
# Por padrão retornam None

# def imprimir(texto, numero):
#     print(texto, numero)

# imprimir('Hello World', 1)
# imprimir('Olá Mundo', 2)

def saudacao(texto='Sem saudação'):
    print(texto)

saudacao('Bom dia')
saudacao('Boa tarde')
saudacao('Boa noite')
saudacao()

