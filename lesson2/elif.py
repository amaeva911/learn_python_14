def work_for_age(age):
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


status = work_for_age(int(input('Сколько вам лет? ')))
print(status)