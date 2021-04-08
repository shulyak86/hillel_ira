str = input('vvedite zelye chisla')
list = str.split()
n = 0
newlist = []
for x in list:
    if int(x) % 2 != 0:
        newlist.append(x)
    elif int(x) % 2 == 0:
        newlist.append('0')
        n += 1
print(newlist)
print('chetnyx bylo', n)
