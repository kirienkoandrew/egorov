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
        else:
            print('Не хватает средств на балансе. Пополните счет')

u1 = User('andrew', 123)
print(u1.login)
print(u1.balance)
u1.deposit(100)
print(u1.__dict__)
u1._User__balance = 123123
print(u1.balance)
u1.payment(123)
print(u1.balance)
u1.payment(123123123)