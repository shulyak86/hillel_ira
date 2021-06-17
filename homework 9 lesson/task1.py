import csv
import argparse
import sys

brand = 'TOYOTA'
color = 'BLACK'
year = '2010'
fuel = 'gas'
# reg_num = None


def flag_saving(row):
    dict_args = {key: value for key, value in args_dict.items() if value}
    #del dict_args['--o']
    if not dict_args:
        sys.exit(0)
    save_flag = False
    map_dict = {'brand': 'BRAND',
                'color': 'COLOR',
                'year': 'MAKE_YEAR',
                'fuel': 'FUEL',
                'reg_num': 'N_REG_NEW'}
    for key, value in dict_args.items():
        if row[map_dict[key]] == value:
            save_flag = True
        else:
            save_flag = False
    return save_flag


def open_file():
    result = []
    with open('tz_opendata_z01012021_po01042021.csv', encoding='UTF-8') as file:
        file_reader = csv.DictReader(file, ('D_REG', 'BRAND', 'COLOR', 'MAKE_YEAR', 'FUEL', 'N_REG_NEW'), delimiter=';')
        for row in file_reader:
            if flag_saving(row):
                result.append(row)



def saving_file(result):
    with open("new_file.csv", 'w', encoding='UTF-8') as w_file:
        #fieldnames = ('D_REG', 'BRAND', 'COLOR', 'MAKE_YEAR', 'FUEL', 'NEW_REG_NEW')
        writer = csv.writer(w_file, delimiter=";")
        writer.writerows(result)


def naming_file():
    dict_args = {'brand': brand, 'color': color, 'year': year, 'fuel': fuel, }
    if brand in dict_args['brand']:
        name1 = f"brand-{str(dict_args['brand'])}-color-{str(dict_args['color'])}-year-{str(dict_args['year'])}-fuel-{str(dict_args['fuel'])}"
    else:
        name1 = "new_file"
    return name1


name = naming_file()
print(name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='choosing_a_car')
    #parser.add_argument('--o', type=str, default='tz_opendata_z01012021_po01042021.csv')
    parser.add_argument('--brand', type=str, default='')
    parser.add_argument('--color', type=str, default='')
    parser.add_argument('--year', type=str, default='')
    parser.add_argument('--fuel', type=str, default='')
    parser.add_argument('--reg_num', type=str, default='', nargs='?')
    args = parser.parse_args()
    args_dict = vars(parser.parse_args())
    open_file()
    saving_file()

