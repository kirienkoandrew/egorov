class SparseArray:
    """Ваша задача - реализовать разреженный массив на базе класса SparseArray.

Требования к классу SparseArray следующие:

     ➖ он должен хранить упорядоченную коллекцию целых чисел, в которой могут присутствовать разреженные области -  элементы массива, заполненные значением None. Индексация начинается с 0. В каком виде хранить значения, определяете вы;

    ➖ при создании SparseArray может передаваться произвольное количество аргументов;

    ➖ при обращении по индексу должен возвращать значение элемента. Если элемента с таким индексом не было, должно произойти расширение массива до текущего индекса, при этом все новые элементы заполняются значением None;

    ➖ при изменении элемента по индексу

array[10] = 100
новое значение должно сохраниться по указанному индексу. Если индекс выходит за границы текущих элементов, необходимо выполнить расширение массива до этого индекса. Промежуточные значения заполняются None;

    ➖ при удалении по индексу в данный элемент должно записаться значение None, размер массива не меняется. Если индекс удаляемого элемента вышел за границы, ничего делать не нужно.

    ➖ поддерживает работу с функцией len, которая возвращает количество элементов массива, включая разреженные элементы;

    ➖ имеет свойство values, которое возвращает все элементы массива в виде кортежа. Данное свойство должно быть с правом только на чтение.

Гарантируется, что индексы в тестовых данных будут использованы неотрицательные. И значения, передаваемые в SparseArray, будут являться только целыми числами."""
    def __init__(self, *args):
        self.array = [i for i in args]

    @property
    def values(self):
        return tuple(self.array)

    def __len__(self):
        return len(self.array)

    def __str__(self):
        return ' '.join(map(str, self.array))

    def __getitem__(self, item):
        if item > len(self.array) - 1:
            self.array.extend([None] * (item - len(self.array) + 1))
        else:
            return self.array[item]

    def __setitem__(self, key, value):
        if key > len(self.array) - 1:
            self.array.extend([None] * (key - len(self.array)))
            self.array.append(value)
        else:
            self.array[key] = value

    def __delitem__(self, key):
        if key <= len(self.array) - 1:
            self.array[key] = None

array = SparseArray(1, 2, 3)
print(array.values)
print(array[7])
print(array.values)
array[6] = 100
print(array.values)
array[10] = 200
print(array.values)
del array[1]
print(array.values)
print(len(array))