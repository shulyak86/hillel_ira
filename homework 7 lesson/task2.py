a = input('vvedite temperaturu: ')
b = input('vvedite shkalu (C, K, F): ')


def isx_c():
    print(a, 'C', '\n',
        int(a)+273, 'K', '\n',
        int(a)*1.8, 'F')


def isx_k():
    print(a, 'K', '\n',
        int(a) - 273, 'C', '\n',
        int((int(a)-273) * 1.8), 'F')


def isx_F():
    print(a, 'F', '\n',
        int((int(a) + 459)*5/9), 'K', '\n',
        int(int(a) / 1.8), 'C')


def calculator():
    if b.lower() == 'c':
        isx_c()
    elif b.lower() == 'k':
        isx_k()
    elif b.lower() == 'f':
        isx_F()
    else:
        print('ne znau shkalu')



calculator()
