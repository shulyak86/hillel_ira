a = int(input('vvedite A'))
b = int(input('vvedite B'))
if a < b:
    while a <= b:
        print(a)
        a += 1
elif a > b:
    while b <= a:
        print(b)
        b += 1
