# Conversão de tipos
# Type converison, typecasting, coercion
# É o ato de converter um tipo em outro
# Tipos imutáveis e primitivos:
# str, int, float, bool

print(1 + 1)
print('a' + 'b')
#print(1 + '1') O python não suporta operações entre str e int/float sem que um dado seja convertido

print(int('1'), type(int('1')))
print(float('1') + 1)
print(bool('')) # str vazia/ 0 é false
print(str(15) + 'b')
