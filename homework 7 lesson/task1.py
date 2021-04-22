def split_stroka(funk):
    def wrapper():
        s = funk().split()
        print(s)
    return wrapper


@split_stroka
def funk():
    a = input('vvedite stroku ')
    print(a)
    return a


funk()
