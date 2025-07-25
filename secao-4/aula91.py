# Generator functions
def generator(n=0, maximum=8):
    while True:
        yield n
        n += 1

        if n > maximum:
            return

gen = generator()
for i in gen:
    print(i)