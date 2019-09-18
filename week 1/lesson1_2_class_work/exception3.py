"""

Классное задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию discounted(price, discount, max_discount=20)
из урока про функции так, чтобы она перехватывала исключения, 
когда переданы некорректные аргументы (например, строки вместо чисел).
    
"""

stock = [
		{'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 'discount': 25},
		{'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 10},
		{'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10},
        {'name': 'test1', 'stock': 18, 'price': '11111.0', 'discount': 10},
        {'name': 'test2', 'stock': 18, 'price': 11111.0, 'discount': '11'},
        {'name': 'test3', 'stock': 18, 'price': 'одинадцать тысяч ровно', 'discount': 10},
        {'name': 'test4', 'stock': 18, 'price': 11111.0, 'discount': 'нет скидок'},
]

def discounted(price, discount, max_discount=20, name=''):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount or "iphone" in name.lower() or not name:
            return price
        else:
            return price - (price * discount / 100)
    except ValueError:
        print('Ошибка ввода: Параметры price и discount должны быть числовыми')



for phone in stock:
    dis_phone = discounted(phone['price'], phone['discount'], name=phone['name'])
    print(dis_phone)
		
