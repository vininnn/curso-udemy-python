# Interpoalção de strings
# s - string
# d ou i - inteiro
# f - float
# .<número de digitos>f
# x ou X - hexadecimal (123456789ABCDEF)
# (Caractere)(><^)(Quantidade)
# > - esquerda
# < - direita
# ^ - centro
# = - força o caracetere adicionado aparecer antes de qualquer sinal
# Sinal - + ou -
# Ex: 0>-100,.1f
# Conversion flags - !r, !s, !a

variavel = 'ABC'

print(f'{variavel}')
print(f'{variavel: >8}')
print(f'{variavel:0<8}')
print(f'{variavel:0^8}')
print(f'{1000.987654321:.2f}')
print(f'{1000.987654321:,.2f}')
print(f'{1000.987654321:+,.2f}')
print(f'{-1000.987654321:,.2f}')
print(f'{-1000.987654321:0>12,.2f}')
print(f'{-1000.987654321:0=12,.2f}')
print(f'{variavel!a}')