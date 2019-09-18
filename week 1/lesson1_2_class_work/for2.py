import random

"""

Классное задание №1

Цикл for

Создать список из десяти целых чисел.
Вывести на экран каждое число, увеличенное на 1.
    
"""


def random_list():

    Start = 0
    Stop = 99   
    limit = 10

    random_list = [random.randint(Start, Stop) for item in range(limit)]

    print(random_list)
    return random_list


def raise_to_one_list(list):
    for item in list:
        print(item+1)

raise_to_one_list(random_list())