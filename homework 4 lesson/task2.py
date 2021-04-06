print('Please enter integer positive numbers')
n = 0
count = 0
summa = 0
composition = 1
average = 0
max_n = 0
index_max_n = 0
count_chet = 0
count_nechet = 0
max_2 = 0
count_max = 1

while True:
    n = int(input())
    if n == 0:
        break
    count += 1
    summa += n
    composition *= n
    average = summa / count
    if n % 2 == 0:
        count_chet += 1
    else:
        count_nechet += 1
    if n == max_n:
        count_max += 1
    elif max_n > n > max_2:
        max_2 = n
    elif n > max_n:
        max_2 = max_n
        max_n = n
        index_max_n = count
print('count', count)
print('summa', summa)
print('composition', composition)
print('average', average)
print('max_n', max_n)
print('count_chet', count_chet)
print('count_nechet', count_nechet)
print('max_2', max_2)
print('count_max', count_max)
print('index_max_n', index_max_n)

