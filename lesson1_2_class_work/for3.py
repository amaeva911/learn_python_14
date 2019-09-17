"""

Классное задание №2

Цикл for

Ввести с клавиатуры строку.
Вывести эту же строку вертикально: по одному символу на строку консоли.
    
"""


def vertical_string_convertion():
    user_string = input('Ведите первоначальную строку: ')
    for letter in user_string:
        print(letter.upper())


vertical_string_convertion()