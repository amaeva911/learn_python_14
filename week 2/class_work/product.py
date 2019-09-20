class Product:
    def __init__(self, name, price, discount=0, stock=0, max_discount=20):
        self.name = name.strip()
        if len(self.name) < 2:
            raise ValueError('Название товара должно быть 2 символа или более')
        self.price = abs(float(price))
        self.stock = abs(int(stock))
        self.discount = abs(float(discount))
        self.max_discount = abs(float(max_discount))
        if self.max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if self.discount > self.max_discount:
            self.discount = self.max_discount

    def discounted(self):
        return self.price - self.price * self.discount / 100

    def sell(self, items_count=1):
        if items_count > self.stock:
            raise ValueError('Недостаточно товара на складе')
        # Здесь мы можем как-то взаимодействовать с учетной/бухгалтерской системой
        self.stock -= items_count
    
    def __repr__(self):
        return f'<Product name: {self.name}, price: {self.price}, stock: {self.stock}>'

    def get_color(self):
        raise NotImplementedError # прописывается в родителе, когда нужна явная реализация в каждом потомке

# product1 = Product('Клещи', 123, stock=10)
# product1.sell(3)
# print(product1)

class Phone(Product):
    def __init__(self, name, price, color, discount=0, stock=0, max_discount=20):
        super().__init__(name, price, discount, stock, max_discount)
        self.color = color

    def __repr__(self):
        return f'<Phone name: {self.name}, price: {self.price}, stock: {self.stock}>'

    def get_color(self):
        return f'Цвет телефона: {self.color}'

# my_phone = Phone('Samsung', 10000, 'green', 12)
# print(my_phone)
# print(my_phone.color)

# print(my_phone.get_color())

class Sofa(Product):
    def __init__(self, name, price, color, texture, discount=0, stock=0, max_discount=20):
        super().__init__(name, price, discount, stock, max_discount)
        self.color = color
        self.texture = texture

    def __repr__(self):
        return f'<Sofa name: {self.name}, price: {self.price}, stock: {self.stock}>'

    def get_color(self):
        return f'Цвет дивана: {self.color}, материал: {self.texture}'

    def get_size(self):
        pass # означает, что метод будет реализован позже

my_sofa = Sofa('Аскона', 12000, 'голубой', 'кожа')
# print(my_sofa)
# print(my_sofa.color)
# print(my_sofa.texture)

print(my_sofa.get_color())

