# server.py

from flask import Flask, render_template
from weather import weather_by_city

app = Flask(__name__) #создаем переменную app, которая будет flask приложением 

# flack испльзует пути, мы должны привезать функцию-обработчик к пути на сайт
# используем для этого декоратор 

@app.route('/')
# наша функция, которая идет за декоратором, называется view (подготовка данных для отображения и передача их в шаблон)
def index():
    page_title = 'Прогноз погоды'
    weather = weather_by_city('Kaluga,Russia')
    return render_template ('index.html', page_title = page_title, weather = weather)
# запускаем сервер
if __name__ == '__main__': # если этот файл запускается напрямую
    app.run(debug = True) # app.run() запускаем приложение // app.run(debug = True) - включение дебаг-режима

