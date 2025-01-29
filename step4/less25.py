class Fruit:
    """Создайте класс Fruit, который имеет:
1. метод __init__, который устанавливает значения атрибутов name и price: название и цена фрукта
2. Методы сравнения. Здесь вы сами решаете, какие магические методы реализовывать.
Главное, чтобы фрукты могли сравниваться с числами и другими фруктами по цене. Смотрите тесты ниже в коде."""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __lt__(self, other):
        if isinstance(other, Fruit):
            if self.price < other.price:
                return True
            else:
                return False
        elif isinstance(other, float):
            if self.price < other:
                return True
            else:
                return False
        else:
            return TypeError

    def __le__(self, other):
        if isinstance(other, Fruit):
            if self.price <= other.price:
                return True
            else:
                return False
        elif isinstance(other, float):
            if self.price <= other:
                return True
            else:
                return False
        else:
            return TypeError

    def __gt__(self, other):
        if isinstance(other, Fruit):
            if self.price > other.price:
                return True
            else:
                return False
        elif isinstance(other, float):
            if self.price > other:
                return True
            else:
                return False
        else:
            return TypeError

    def __ge__(self, other):
        if isinstance(other, Fruit):
            if self.price >= other.price:
                return True
            else:
                return False
        elif isinstance(other, float):
            if self.price >= other:
                return True
            else:
                return False
        else:
            return TypeError

    def __eq__(self, other):
        if isinstance(other, Fruit):
            if self.price == other.price:
                return True
            else:
                return False
        elif isinstance(other, float):
            if self.price == other:
                return True
            else:
                return False
        else:
            return TypeError

    def __ne__(self, other):
        if isinstance(other, Fruit):
            if self.price != other.price:
                return True
            else:
                return False
        elif isinstance(other, float):
            if self.price != other:
                return True
            else:
                return False
        else:
            return TypeError





apple = Fruit("Apple", 0.5)
orange = Fruit("Orange", 1)
banana = Fruit("Banana", 1.6)
lime = Fruit("Lime", 1.0)
print(banana < 1.2)
print(lime < orange)
assert (banana > 1.2) is True
assert (banana >= 1.2) is True
assert (banana == 1.2) is False
assert (banana != 1.2) is True
assert (banana < 1.2) is False
assert (banana <= 1.2) is False

assert (apple > orange) is False
assert (apple >= orange) is False
assert (apple == orange) is False
assert (apple != orange) is True
assert (apple < orange) is True
assert (apple <= orange) is True

assert (orange == lime) is True
assert (orange != lime) is False
assert (orange > lime) is False
assert (orange < lime) is False
assert (orange <= lime) is True
assert (orange >= lime) is True
print('Good')
