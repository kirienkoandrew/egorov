class Quadrilateral:
    def __init__(self, height, width=None):
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value=None):
        if value:
            self.__width = value
        else:
            self.__width = self.height

    def __bool__(self):
        return self.width == self.height

    def __str__(self):
        if bool(self):
            return f'Квадрат размером {self.height}х{self.width}'
        else:
            return f'Прямоугольник размером {self.height}х{self.width}'

q1 = Quadrilateral(10)
print(q1)
print(bool(q1))
print(isinstance(q1, Quadrilateral))

q2 = Quadrilateral(3, 5)
print(q2)
print(bool(q2))

q3 = Quadrilateral(4, 7)
print(q3)
print(bool(q3))