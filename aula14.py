a = 'A'
b = 'B'
c = 1.1

formato_1 = 'a={} b={} c={:.3f}'.format(a, b, c)

resultado ='a={} b={} c={}'
formato_2 = resultado.format(a, b, c)

formato_3 = 'c={} b={} a={}'.format(c, b, a)
formato_4 = 'c={2} b={1} a={0}'.format(a, b, c)
formato_5 = 'c={2} b={1} a={0} a={0} a/={1} e {2}'.format(a, b, c)

formato_6 = 'a={primeiro} b={b} c={numero}'.format(primeiro=a, b=b, numero=c)


print(formato_1)
print(formato_2)
print(formato_3)
print(formato_4)
print(formato_5)
print(formato_6)
