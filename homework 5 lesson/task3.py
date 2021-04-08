a = int(input('vvedite storonu a: '))
b = int(input('vvedite storonu b: '))
fig = input('esli kvadrat - vvedite Y, esli treug - vvedite N ')

kvadrat = a * b
treug = a * b / 2
if fig == 'Y':
    print('plowad prjamougolnika: ', kvadrat)
elif fig == 'N':
    print('plowad treugolnika: ', treug)
else:
    print('vy ne to vveli!')
