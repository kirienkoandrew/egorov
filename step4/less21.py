class Hero:
    """Создайте класс Hero, который имеет следующие методы:

метод __len__, который возвращает количество атрибутов экземпляра

магический метод __str__, который возвращает строковое представление героя. Для этого нужно перечислить все атрибуты в алфавитном порядке на отдельной строке, напротив каждого атрибута указать его значение. Вот такой формат должен получится:
атрибут_1: значение_атрибут_1
атрибут_2: значение_атрибут_2
...
атрибут_N: значение_атрибут_N

Если у экземпляра нету атрибутов, необходимо вернуть пустую строку"""
    def __init__(self):
        pass

    def __len__(self):
        return len(self.__dict__)

    def __str__(self):
        res = []
        sorted_dict = dict(sorted(self.__dict__.items()))
        for k, v in sorted_dict.items():
            res.append(f'{k}: {v}')
        return '\n'.join(res)

hero = Hero()
assert len(hero) == 0
hero.health = 50
hero.damage = 10
assert len(hero) == 2
print(hero)
assert str(hero) == '''damage: 10
health: 50'''
hero.weapon = ['sword', ' bow']
hero.skill = 'Некромант'
assert str(hero) == '''damage: 10
health: 50
skill: Некромант
weapon: ['sword', ' bow']'''
print(hero)

villain = Hero()
assert str(villain) == ''
assert len(villain) == 0
villain.level = 15
villain.skill = 'Боец'
villain.armor = 25
assert len(villain) == 3
assert str(villain) == '''armor: 25
level: 15
skill: Боец'''
print(villain)