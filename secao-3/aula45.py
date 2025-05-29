# Como funciona o for in
# Iterável -> str, range, etc
# Iterador -> quem sabe entregar um valor por vez
# next -> me entregue o próximo valor
# iter -> me entregue o seu iterador

texto = 'Vinicius' # iterável
iterador = iter(texto) # iterador __iter__

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
 
# for letra in texto:
#   print(letra)