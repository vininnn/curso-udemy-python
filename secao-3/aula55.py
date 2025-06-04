# Imprecisão de número flutuante
# Double precision floating-format IEEE 754
import decimal

a = 0.7
b = 0.1
c = a + b
print(c)
print(f'{c:.1f}')
print(round(c, 2))
a2 = decimal.Decimal(0.7)
b2 = decimal.Decimal(0.1)
c2 = a2 + b2
print(c2)

