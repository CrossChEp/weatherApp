import requests
def find(city):
        """
        Параметры:
            city - название города (строка)
        
        Возвращаемое значение:
            словарь - с ключами:
                icon_source - ссылка для скачивания иконки
                temp_real - температура на данный момент  
                temp_feels - температура "ощущается как" на данный момент
                description - описание погоды на данный момент

            пустой словарь - город не найден
        """
        callback = dict()
        key = '110e6871bbbfd9e712471e94efb92953'
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'q': city, 'type': 'like', 'units': 'metric', 'lang': 'ru', 'APPID': key}).json()
        if res['cod'] == '404' or 'weather' not in res.keys():
            return callback
        
        icon_id = res['weather'][0]['icon']
        callback['icon_source'] = f'http://openweathermap.org/img/wn/{icon_id}@2x.png'
        callback['temp_real'] = str(int(res['main']['temp'])) + '°C'
        callback['temp_feels'] = str(int(res['main']['feels_like'])) + '°C'
        callback['description'] = str(res['weather'][0]['description'])
        return callback
