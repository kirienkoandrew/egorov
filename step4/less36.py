"""Перед вами класс BankAccount

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return self.name

Ваша задача дописать его таким образом, чтобы его экземпляры могли участвовать в операции сортировки списка,
в котором могут находиться только числа и другие экземпляры класса BankAccount"""
from functools import total_ordering

@total_ordering
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.balance == other

    def __lt__(self, other):
        return self.balance < other


values = [BankAccount('Petrovich', 400), 500, BankAccount('Andrey', 200), 100, BankAccount('Zina', 150)]
values.sort()
print(*values)
