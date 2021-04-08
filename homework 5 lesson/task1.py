chislo = int(input('vvedite chislo do 1000:'))
n = 2
while n < chislo:
    if chislo % n != 0:
        res = 'prostoe'
    else:
        res = 'ne prostoe'
        break
    n += 1
print(res)

