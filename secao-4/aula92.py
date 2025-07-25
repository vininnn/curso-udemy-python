# yield from

def gen1():
    yield 1
    yield 2
    yield 'Fim generator 1'

def gen2():
    yield 4
    yield 5
    yield 'Fim generator 2'

def gen3(gen):
    yield from gen
    yield 10
    yield 'Fim generator 3'

g1 = gen3(gen1())
g2 = gen3(gen2())

for n in g1:
    print(n)
for n in g2:
    print(n)