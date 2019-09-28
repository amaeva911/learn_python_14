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
    result = requests.get(weather_url, params = params) # возвращает строку, которую необходимо преобразовать
    weather = result.json() # получение питоновского словаря

    if 'data' in weather:
       if 'currean_condition' in weather['data']:
           try:
               return weather['data']['current_condition'][0]
           except(IndexError, TypeError, ConnectionError, TimeoutError):
               return False
    return False

    #return weather

if __name__ == "__main__":
    print(weather_by_city("Moscow, Russia")) # не получилось запустить из-за ConnectionError и TimeoutError :( пробовала и свой ключ и ключ Михаила из видео...

