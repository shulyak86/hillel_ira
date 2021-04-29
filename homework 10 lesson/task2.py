def palindromnost():
    a = input('vvedite vawe slovo: ')
    j = 0
    for i in range(len(a) // 2):
        if a[i] == a[-1 - j]:
            i += 1
            j += 1
            if i == len(a) // 2:
                print('vawe slovo palindrom')
            continue
        else:
            print('vawe slovo NE palindrom')
            break


palindromnost()
