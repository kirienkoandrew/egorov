class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def deposit(self, value):
        self.balance += value

    def is_money_enough(self, value):
        return self.balance >= value

    def payment(self, value):
        if self.is_money_enough(value):
            self.balance -= value
            return True
        else:
            print('Не хватает средств на балансе. Пополните счет')
            return False

class Cart:
    def __init__(self, user, goods=None, total=0):
        self.user = user
        if goods is None:
            self.goods = {}
        self.__total = total

    def add(self, product, quontity=1):
        self.goods[product] = self.goods.get(product, 0) + quontity
        self.__total += product.price * quontity


    def remove(self, product, quontity=1):
        if product.price > self.__total:
            self.__total = 0
        if self.goods[product] < quontity:
            self.__total -= product.price * self.goods[product]
            del self.goods[product]
        else:
            self.goods[product] -= quontity
            self.__total -= product.price * quontity

    @property
    def total(self):
        return self.__total

    def order(self):
        if User.payment(self.user, self.total):
            print('Заказ оплачен')
        else:
            print('Проблема с оплатой')

    def print_check(self):
        print('---Your check---')
        sorted_goods = sorted(self.goods, key=lambda x: x.name)
        for goods in sorted_goods:

            print(f'{goods.name} {goods.price} {self.goods[goods]} {self.goods[goods] * goods.price}')
        print(f'---Total: {self.total}---')

billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total) # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order() # Заказ оплачен
print(cart_billy.user.balance) # 20