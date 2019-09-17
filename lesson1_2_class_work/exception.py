"""

Классная работа №1

Работа по видео и слайдам
    
"""


def cut_cake(people):
    try:
        z = 1 / people
        print(f'Каждый получит {z} пирога')
    except ZeroDivisionError:
        print('Не надо делить на ноль')
    except TypeError:
        print('Программа принимает число')


cut_cake(4)
cut_cake(0)
cut_cake('0')