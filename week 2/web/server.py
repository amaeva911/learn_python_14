# server.py

from flask import Flask
from weather import weather_by_city

app = Flask(__name__) #создаем переменную app, которая будет flask приложением 

# flack испльзует пути, мы должны привезать функцию-обработчик к пути на сайт
# используем для этого декоратор 

@app.route('/')
# наша функция, которая идет за декоратором
def index():

    ### это вызов функции погоды (которая пока дает TimeoutError...)
    weather = weather_by_city('Kaluga,Russia')
    #return 'Привет!'
    if weather:
        return f'Погода:{weather['temp_C']}, ощущается как {weather['FeelsLikeC']}' #!!! тут ошибка, не находит параметры, хоть и не должны заходить в эту ветку при сбоях
    else: 
        return 'Сервис погоды временно недоступен'
# запускаем сервер
if __name__ == '__main__': # если этот файл запускается напрямую
    app.run(debug = True) # app.run() запускаем приложение // app.run(debug = True) - включение дебаг-режима

