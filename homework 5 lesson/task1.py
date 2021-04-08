chislo = int(input('vvedite chislo do 1000:'))


def checker():
    n = 2
    if chislo in (1, 2):
        res = 'prostoe'
    else:
        while n < chislo:
            if chislo % n != 0:
                res = 'prostoe'
            else:
                res = 'ne prostoe'
                break
            n += 1
    print(res)


checker()

