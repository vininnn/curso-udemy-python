# Interpoalção de strings
# s - string
# d ou i - inteiro
# f - float
# x ou X - hexadecimal (123456789ABCDEF)

# É uma forma antiga de formatação, 'formatação estilo C'
# Ultrapassada, atualmente recomenda-se usar f-strings mesmo

nome = 'Vinicius'
item = 'chocolate'
preco = 10.968
preco_int = int(preco)
interpolacao = 'O %s comprou o %s por R$%.2f' % (nome, item, preco)
print(interpolacao)
print('O hexadecimal de %i é %08x' % (preco_int, preco_int)) 
