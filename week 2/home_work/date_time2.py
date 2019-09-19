"""

Задание №2

Дата и время 

* Превратите строку "01/01/17 12:10:03.234567" в объект datetime
    
"""

from datetime import date, datetime, timedelta


date_string = "01/01/17 12:10:03.234567"
date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')

print(f'Преобразованная дата: {date_dt}')



