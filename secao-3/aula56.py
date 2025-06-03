# split e join
# split - divide uma string
# join - une uma string

texto = 'Se você quer ir rápido, vá sozinho. Se você quer ir longe, vá com os outros'
lista_palavras = texto.split()
lista_frase = texto.split(',')
lista_oracao = texto.split('.')
print(lista_palavras)
print(lista_frase)
print(lista_oracao)

texto2 = '   Dia, tarde,    noite     '
lista_texto2 = texto2.split(',')

lista_texto2_corrigida = []
for i, frase in enumerate(lista_texto2):
    lista_texto2_corrigida.extend(lista_texto2[i].split())

print(lista_texto2)
print(lista_texto2_corrigida)

frases_unidas = '-'.join(lista_texto2_corrigida)
print(frases_unidas)

