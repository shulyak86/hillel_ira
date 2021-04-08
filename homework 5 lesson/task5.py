a = int(input('vvedite storonu kvadrata: '))
t = []


def square():
    per = a * 4
    t.append(per)
    kvad = a ** 2
    t.append(kvad)
    diag = a * 2 ** (1 / 2)
    t.append(round(diag))
    tp = tuple(t)
    print(tp)


square()
