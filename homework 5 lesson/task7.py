from datetime import datetime, date

den = int(input('vvedite den: '))
month = int(input('vvedite mecjaz: '))
year = int(input('vvedite god (format 1967): '))
try:
    print(date(year, month, den))
except:
    print('wrong date')
