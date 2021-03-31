a = input('Please enter a number with 2 decimal digits:')
b = list(str(a).split('.'))
print('decimal part is', int(b[1]))
c = int(b[1]) // 10
print('first digit after point is', c)


