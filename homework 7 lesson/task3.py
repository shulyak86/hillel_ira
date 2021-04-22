def weather():
    import requests
    import datetime
    API_KEY = 'f9ada9efec6a3934dad5f30068fdcbb8'
    city_name = 'Odessa'
    cnt = 5
    request = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?', params={'q': city_name, 'cnt': cnt,
                                                                                               'appid': API_KEY})
    data = request.json()
    filename = datetime.datetime.now().strftime('%d-%m-%Y') + '-' + str(city_name) + ' ' + str(cnt) + 'days-forecast.txt'
    file = open(filename, 'w')
    file.write('date: \t\t day:\t night:\t feels like(day):\t feels like(night): \n')
    for data_list in data['list']:
        file.write(str(datetime.datetime.fromtimestamp(data_list['dt']).strftime('%d-%m-%Y')) + '\t')
        file.write(str(data_list['temp']['day']) + '\t')
        file.write(str(float(data_list['temp']['night'])) + '\t\t')
        file.write(str(data_list['feels_like']['day']) + '\t\t\t\t')
        file.write(str(data_list['feels_like']['night']) + '\n')
    file.close()


weather()

