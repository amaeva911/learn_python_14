"""

Задание №1

Дата и время 

* Напечатайте в консоль даты: вчера, сегодня, месяц назад
    
"""

from datetime import date, datetime, timedelta


yesterday = datetime.strftime(datetime.now() - timedelta(1), '%d.%m.%Y')
print(f'Вчера {yesterday}')

today = datetime.now().strftime('%d.%m.%Y')
print(f'Сегодня {today}')

month_ago_30 = datetime.strftime(datetime.now() - timedelta(30), '%d.%m.%Y')
month_ago_31 = datetime.strftime(datetime.now() - timedelta(31), '%d.%m.%Y')
print(f'Месяц назад {month_ago_31} - {month_ago_30}')


