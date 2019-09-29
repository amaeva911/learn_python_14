"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
school_scores = [
    {'school_class': '4a', 'scores': [3,4,4,2]}, 
    {'school_class': '4б', 'scores': [5,4,5,5,2,5]}, 
    {'school_class': '4в', 'scores': [2,3,5,3,3,3,3,2,1]}, 
    {'school_class': '4г', 'scores': [4,4,4,3,3,5]},
    {'school_class': '4д', 'scores': [5,4,2,5,3,5]},
    {'school_class': '4е', 'scores': [2,3,3,2,2,2,5,3,4]}
    ]

average_school_marks = 0

for scores in school_scores:
    average_class_score = sum(school_scores['scores'])/len(school_scores['scores'])
    print(average_class_score)
    counter = counter + len(school_scores['scores'])
    average_school_score = average_school_marks + sum(school_scores['scores'])

average_school_marks = average_school_score / counter

# def count_avarage_scores(scores):
#     """
#     Эта функция вызывается и выводит средний бал каждому классу и по школе
#     """
#     total_sum = 0 # общая сумма
#     total_score_count = 0 # количество оценок
#     count = 0 # позиция класса при переборе //пока не нашла как можно проще, вангую есть готовый метод, из всего, что попробовала - этот самый простой, но рукописный
    
#     school_class_count = len(school_scores) # подсчитываю и вывожу общее количество классов в школе, по которым есть оценки
#     print('------------')
#     print (f'Количество классов в школе: {school_class_count}')
#     print('------------')


#     for class_unit in school_scores: # цикл, перебивает словари списка (классы школы) по одному

#         class_scores_to_print = class_unit['scores'] # без этого не работает форматирование как оказалось
#         class_name_to_print = class_unit['school_class'] # аналогично

#         class_sum = sum(class_scores_to_print) # перебираю оценки класса и суммирую их
#         total_sum += class_sum # добавляю к общей сумме оценок

#         class_count = len(class_scores_to_print) # перебираю оценки класса и считаю их количество
#         total_score_count += class_count # добавляю к общему числу оценок

#         class_avarage_score = int(round(class_sum / class_count)) # считаю среднюю по классу, округляется по правилам арифметики и привожу к типу int

#         print (f'Класс: {class_name_to_print}, количество оценок: {class_count}, сумма оценок: {class_sum }, средняя оценка: {class_avarage_score}')

#         count += 1 # позиция + 1

#         if count == school_class_count: # использую данное условие для вывода данных по школе
#             print('------------')

#             total_school_avarage_score = int(round(total_sum / total_score_count)) # считаю общую среднюю по школе с использованием total переменных
#             print (f'Средняя оценка по школе: {total_school_avarage_score}')        

    
# count_avarage_scores(school_scores) 
