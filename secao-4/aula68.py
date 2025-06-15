# Escopo da função
# Local onde o código pode atingir
# Escopo global significa que o código pode atingir todo o programa
# Escopo local significa que o código pode atingir apenas nomes do mesmo local

# x global
x = 1

def funcao():
    # Esse é o x da 'funcao' não o global
    x = 10

    # A 'funcao' não pode alncaçar o y da 'outra_funcao'
    def outra_funcao():
        y = 2
        print(x, y)
        
    outra_funcao()
    print(x)

funcao()
print(x)

def outra_outra_funcao():
    # Agora eu posso acessar o x global
    global x
    x = 10

outra_outra_funcao()
print(x)