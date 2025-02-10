class Shape:
    pass


class Polygon(Shape):
    pass


class Triangle(Polygon):
    pass


class Rectangle(Polygon):
    pass


class Square(Rectangle):
    pass


class Ellipse(Shape):
    pass


class Circle(Ellipse):
    pass


# Скопируйте реализацию классов из предыдущей задачи

shapes = [
    Polygon(), Triangle(), Ellipse(), Polygon(), Triangle(), Ellipse(), Polygon(), Square(), Polygon(), Circle(),
    Shape(), Polygon(), Triangle(), Circle(), Ellipse(), Shape(), Circle(), Rectangle(), Circle(), Circle(),
    Square(), Square(), Circle(), Rectangle(), Rectangle(), Polygon(), Polygon(), Polygon(), Square(), Square(),
    Rectangle(), Square(), Rectangle(), Polygon(), Circle(), Triangle(), Rectangle(), Shape(), Rectangle(),
    Polygon(), Polygon(), Ellipse(), Square(), Circle(), Shape(), Polygon(), Ellipse(), Triangle(), Square(),
    Polygon(), Triangle(), Circle(), Rectangle(), Rectangle(), Ellipse(), Triangle(), Rectangle(), Polygon(),
    Shape(), Circle(), Rectangle(), Polygon(), Triangle(), Circle(), Polygon(), Rectangle(), Polygon(), Square(),
    Triangle(), Circle(), Ellipse(), Circle(), Shape(), Circle(), Triangle(), Ellipse(), Square(), Circle(),
    Triangle(), Polygon(), Square(), Polygon(), Circle(), Ellipse(), Polygon(), Shape(), Triangle(), Rectangle(),
    Circle(), Square(), Triangle(), Triangle(), Ellipse(), Square(), Circle(), Rectangle(), Ellipse(), Shape(),
    Triangle(), Ellipse(), Circle(), Shape(), Polygon(), Polygon(), Ellipse(), Rectangle(), Square(), Shape(),
    Circle(), Triangle(), Circle(), Circle(), Circle(), Triangle(), Ellipse(), Polygon(), Circle(), Ellipse(),
    Rectangle(), Circle(), Shape(), Polygon(), Polygon(), Triangle(), Rectangle(), Polygon(), Shape(), Circle(),
    Shape(), Circle(), Triangle(), Ellipse(), Square(), Circle(), Triangle(), Ellipse(), Square(), Circle(),
]
cnt_shape, cnt_square, cnt_polygon = 0, 0, 0
for shape in shapes:
    if isinstance(shape, Circle): cnt_shape += 1
    if isinstance(shape, Rectangle): cnt_square += 1
    if isinstance(shape, Polygon): cnt_polygon += 1
print(cnt_shape)
print(cnt_square)
print(cnt_polygon)