"""Перед вами вновь класс BankAccount

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return self.name
И еще имеется класс Numbers

class Numbers:
    def __init__(self, values: list):
        self._values = values
Ваша задача дописать классы BankAccount и Numbers таким образом, чтобы их экземпляры могли участвовать в операции
сложения с числами и c другими экземплярами классов BankAccount и Numbers"""
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return self.name

    def __radd__(self, other):
        return self.balance + other

class Numbers:
    def __init__(self, values: list):
        self._values = values

    def __radd__(self, other):
        return sum(self._values) + other

    def __add__(self, other):
        return sum(self._values) + other


lst = [
    BankAccount('Jack', 1000),
    Numbers([1, 2, 3, 4, 5]),
    BankAccount('Ivan', 30),
    7.5,
    Numbers([10, 20, 30, 40, 50]),
    BankAccount('Frank', 2000),
    10
]
print(sum(lst))