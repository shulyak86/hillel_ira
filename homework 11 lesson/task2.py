def hide_email():
    a = input('enter your email, please: ')
    mid_sign = a.index('@')
    b = a[:mid_sign - 3] + '***@***' + a[mid_sign + 3:]
    return b


print(hide_email())
