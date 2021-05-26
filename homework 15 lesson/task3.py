import re


def password_check():
    '''
    function that check password for length 8symb at last, a-z, A-Z, 0-9, ($)(@)(-)(+)(=)
    :return: ans is string if password is OK, or tuple of constraints not fulfilled if the password needs to be improved
    '''
    a = input('Enter your password: ')
    patt = [['a-z'], ['A-Z'], ['0-9'], '[($)(@)(-)(+)(=)]']
    ans = 'Password is OK'
    i = 0
    while i < 4:
        if not re.search(rf"{patt[i]}", a):
            ans = []
            ans.append(f'not enough  {patt[i]} ')
        i += 1
    if len(a) < 8:
        ans.append('Too short password, 8 or more symbols needed ')
    print(ans)
    return ans


password_check()
