inp = input('Please enter an number of the year:')
ostatok = int(inp) % 4
#typ_ostatok = type(ostatok)
ostatok_ot_100 = int(inp) % 4
if not ostatok and ostatok_ot_100 !=0:
    print(ostatok)
    print(ostatok_ot_100)
    print('Yes')
#typ_ostatok_ot_100 = type(ostatok_ot_100)
else:
    print(ostatok)
    print(ostatok_ot_100)
    print('No')


