"""

Домашнее задание 

CSV

* Создайте список словарей:
        [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]
* Запишите содержимое списка словарей в файл в формате csv

"""

import csv


user_list = [
            {'name': 'Миша', 'age': 25, 'job': 'Scientist'}, 
            {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
            {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
            {'name': 'Константин', 'age': 32, 'job': 'Mayor'},
            {'name': 'Кирилл', 'age': 37, 'job': 'Mayor'},
            {'name': 'Оля', 'age': 30, 'job': 'Manager'},
            {'name': 'Маша', 'age': 3, 'job': 'Child'},
            ]       

with open('export.csv', 'w', encoding='ANSI', newline='') as f:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in user_list:
        writer.writerow(user)
