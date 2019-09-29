import requests

def weather_by_city(city_name):
    weather_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    
    params = {
        "key": "c319fbdb846845a58c8134926192809",
        "q": city_name,
        "format": "json",
        "num_of_days": "1",
        "lang": "ru"
    }
    try:
        result = requests.get(weather_url, params = params) # возвращает строку, которую необходимо преобразовать
        result.raise_for_status() # магия с обработкой ответных кодов от сервера
        weather = result.json() # получение "питоновского словаря"

        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0] # получение части json
                except(IndexError,TypeError):
                    return False
    except(requests.RequestException,ValueError):
        print('Сетевая ошибка')
        return False
    return False

if __name__ == "__main__":
    print(weather_by_city("Moscow, Russia")) # не получилось запустить из-за ConnectionError и TimeoutError :( пробовала и свой ключ и ключ Михаила из видео...

