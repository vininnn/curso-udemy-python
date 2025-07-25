# raise - lançando excessões (erros)

a = 10
b = 0
if b == 0:
    raise ValueError('Erro de divisão por zero')
else:
    print(a / b)