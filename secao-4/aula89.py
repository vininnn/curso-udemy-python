# dir, hasattr, getattr
# has attribute
# get attribute

nome = 'Vinicius'
metodo = 'upper'

if hasattr(nome, metodo):
    print('Possui o método upper()')
    # print(nome.metodo()) não funcionaria, por isso deve pegar o metodo com o getattr
    print(getattr(nome, metodo)())
else:
    print('Não existe o método:', metodo)