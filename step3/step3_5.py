class File:
    def __init__(self, name, in_trash=False, is_deleted=False):
        self.name = name
        self.in_trash = in_trash
        self.is_deleted = is_deleted

    def restore_from_trash(self):
        print(f'Файл {self.name} восстановлен из корзины')
        self.in_trash = False

    def remove(self):
        print(f'Файл {self.name} был удален')
        self.is_deleted = True

    def read(self):
        """печатает фразу «ErrorReadFileDeleted({name})», если атрибут is_deleted истинен, и выходит из метода;
печатает фразу «ErrorReadFileTrashed({name})», если атрибут in_trash истинен, и выходит из метода;
печатает фразу «Прочитали все содержимое файла {self.name}», если файл не удален и не в корзине;"""
        if self.is_deleted:
            print(f'ErrorReadFileDeleted({self.name})')
            return
        elif self.in_trash:
            print(f'ErrorReadFileTrashed({self.name})')
            return
        else:
            print(f'Прочитали все содержимое файла {self.name}')

    def write(self, content):
        """печатает фразу «ErrorWriteFileDeleted({name})», если атрибут is_deleted истинен, и выходит из метода;
печатает фразу «ErrorWriteFileTrashed({name})», если атрибут in_trash истинен, и выходит из метода;
печатает фразу «Записали значение {content} в файл {self.name}», если файл не удален и не в корзине."""
        if self.is_deleted:
            print(f'ErrorWriteFileDeleted({self.name})')
            return
        elif self.in_trash:
            print(f'ErrorWriteFileTrashed({self.name})')
            return
        else:
            print(f'Записали значение {content} в файл {self.name}')

class Trash:
    content = []

    @staticmethod
    def add(file):
        if isinstance(file, File):
            Trash.content.append(file)
            file.in_trash = True
        else:
            print('В корзину можно добавлять только файл')

    @staticmethod
    def clear():
        print('Очищаем корзину')
        for file in Trash.content:
            file.remove()
        Trash.content = []
        print('Корзина пуста')

    @staticmethod
    def restore():
        print('Восстанавливаем файлы из корзины')
        for file in Trash.content:
            file.restore_from_trash()
        Trash.content = []
        print('Корзина пуста')


f1 = File('puppies.jpg')
f2 = File('cat.jpg')
f3 = File('xxx.doc')
passwords = File('pass.txt')

for file in [f1, f2, f3, passwords]:
    assert file.is_deleted is False
    assert file.in_trash is False

f3.read()
f3.remove()
assert f3.is_deleted is True
f3.read()
f3.write('hello')

assert Trash.content == []

Trash.add(f2)
Trash.add(passwords)
Trash.add(f3)

f1.read()
Trash.add(f1)
f1.read()

for file in [f1, f2, f3, passwords]:
    assert file.in_trash is True

for f in [f2, passwords, f3, f1]:
    assert f in Trash.content

Trash.restore()
assert Trash.content == [], 'После восстановления корзина должна была очиститься'

Trash.add(passwords)
Trash.add(f2)
Trash.add('hello')
Trash.add(f1)

for f in [passwords, f2, f1]:
    assert f in Trash.content


Trash.clear()

for file in [passwords, f2, f1]:
    assert file.is_deleted is True

assert Trash.content == [], 'После удаления файлов корзина должна была очиститься'

f1.read()