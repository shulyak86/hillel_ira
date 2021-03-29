tochka_puti = 0
v = input('Velocity: in(km/h), please')
t = input('Time: in(h), please')
tochka_puti = tochka_puti + int(v) * int(t)
if int(v)<0:
    print('Vasya! You run in opposite direction!')
elif tochka_puti > 100:
    print('Vasya pribyl')
else:
    print('Otmetka v puti', int(tochka_puti))
