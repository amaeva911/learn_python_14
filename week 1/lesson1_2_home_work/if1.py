"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main(age):
    if age<=0:
        return "Вы еще не родились"
    elif age>0 and age<=6:
        return "Вы ходите в детский сад"
    elif age>6 and age<=17:
        return "Вы ходите в школу"
    elif age>17 and age<=23:
        return "Вероятно вы студент вуза"
    elif age>23 and age<=65:
        return "Вероятно вы работаете"
    else:
        return "Вероятно вы пенсионер"


status = main(int(input('Сколько вам лет? ')))
print(status)
