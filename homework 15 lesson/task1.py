import re
import csv

a = input('Enter your vehicle number: ')
b = a[0:2]
a.replace('I', 'І', 2)

pattern = r'[A-Z, А-Я, І]{2}[0-9]{4}[A-Z, А-Я, І]{2}'
matches = re.search(pattern, a)
if not matches:
    print('No it\'s not a car number')
else:
    print('Yes, its number')
    with open('ua_auto.csv', encoding='utf8', newline='') as File:
        reader = csv.DictReader(File)
        for row in reader:
            if a[0:2] == row['Код 2004']:
                print('2004 encoding for ', row['Регіон'])
                break
            elif a[0:2] == row['Код 2013']:
                print('2013 encoding for ', row['Регіон'])
                break
            else:
                None




