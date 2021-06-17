import csv
import re
from collections import OrderedDict


def user_input():
    user_inp = 0
    chosen_par = input('choose param: "iata_code" or "country" or "name": ')
    if chosen_par == 'iata_code':
        chosen_value = input('please input iata_code: ')
        user_inp = [chosen_par, chosen_value]
        if len(user_inp[1]) != 3:
            raise NameError('"iata_code" should only contain 3 letters!!!')
        return user_inp
    elif chosen_par == 'country':
        chosen_value = input('please input country: ')
        user_inp = ['iso_country', chosen_value]
        return user_inp
    elif chosen_par == 'name':
        chosen_value = input('please input name of an airport: ')
        user_inp = [chosen_par, chosen_value]
        return user_inp
    else:
        print('Please choose an option in "iata_code" or "country" or "name", and then enter a value for this option')
        return user_inp


with open('cut_to_60strings_airports.csv', encoding='utf8', newline='') as File:
    reader = csv.DictReader(File)
    user_inp = user_input()
    # print(user_inp[0])
    for row in reader:
        if user_inp[0] in list(row.keys()) \
                and user_inp[1] in list(row.values()) \
                and user_inp[0] != 'name':
            with open('result_airport.csv', 'a', encoding='utf8', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(row.values())
        elif user_inp[0] in list(row.keys()) \
                and user_inp[0] == 'name' \
                and str(user_inp[1]).lower() in str(row['name'].lower()):
            # print(row.items())
            # print(row.keys())
            # print(row.values())
            with open('result_airport.csv', 'a', encoding='utf8', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(row.values())
