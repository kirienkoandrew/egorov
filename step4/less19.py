class GroceryItem:
    """Создайте класс GroceryItem, который имеет следующие методы:

метод __init__, который устанавливает значения атрибутов name, price и quantity: название товара, его цену и количество

магический метод __str__, который возвращает строковое представление товара в следующем виде:
Name: {name}
Price: {price}
Quantity: {quantity}
магический метод __repr__, который возвращает однозначное строковое представление объекта
GroceryItem({name}, {price}, {quantity})"""
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'''Name: {self.name}
Price: {self.price}
Quantity: {self.quantity}'''

    def __repr__(self):
        return f'GroceryItem({self.name}, {self.price}, {self.quantity})'