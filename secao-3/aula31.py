# flag (bandeira) -> usado apra marcar um local
# none -> não valor
# is e is not = é e não é (tipo, valor, identidade)
# id -> identidade

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')

print(passou_no_if, passou_no_if is None) # is seria igual usar ==, mas para None normalmente se usa is
print(passou_no_if, passou_no_if is not None)