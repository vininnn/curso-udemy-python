# try, except, else e finally

try:
    a = 10
    b = 2
    c = a / b
    print(a[1000])
except ZeroDivisionError:
    print('Erro de divisão por zero!')
except NameError:
    print('Variável não definida!')
except (TypeError, IndexError) as error:
    print('Mensagem:', error)
    print('Nome:', error.__class__.__name__)
except Exception: # except de maior hierarquia
    print('Erro desconhecido')