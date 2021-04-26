import requests
from datetime import date, timedelta, datetime
import json
amount = input('vvedite summu, kotoruju xotite pomenjat: ')


def value_check():
    with open('symbols.json', 'r') as file:
        symbols = json.load(file)
        from_val = input('vvedite vashu valutu: ')
        to_val = input('vvedite gelaemuju valutu: ')
        if from_val in symbols['symbols'].keys():
            from_val
        else:
            from_val = 'USD'
        if to_val in symbols['symbols'].keys():
            to_val
        else:
            to_val = 'UAH'
    # print(symbols['symbols'].keys())
    return from_val, to_val


def date_check():
    today = date.today()
    start_date = datetime.strptime(input('vvedite den, v kotoryi xotite pomenjat (format year-month-day): '),
                                   '%Y-%m-%d').date()
    if start_date > today:
        start_date = datetime.now().strftime("%Y-%m-%d")
        return start_date
    else:
        while start_date < today:
            #start_date += timedelta(days=1)
            return start_date



def make_req():
    r = requests.get('https://api.exchangerate.host/convert',
                     params={'from': from_val, 'to': to_val, 'amount': amount, 'date': start_date})
    json_string = r.json()

    print(
        str(json_string['date']) + '\t' + str(json_string['query']['from']) + '\t\t\t' + str(json_string['query']['to'])
        + '\t\t' + str(json_string['query']['amount']) + '\t'
        + '\t' + str(json_string['info']['rate']) + '\t' + str(json_string['result']) + '\n')


#
#
#
from_val, to_val = value_check()
today = date.today()
start_date = date_check()
print('Date\t\tFrom\t\tTo\t\tAmount\tRate\t\t\tResult')
while start_date <= today:
    make_req()
    start_date += timedelta(days=1)
