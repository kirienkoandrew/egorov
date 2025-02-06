class Building:
    def __init__(self, floors):
        self.floors = {}
        for k in range(floors):
            self.floors[k] = None

    def __str__(self):
        res = ''
        for k, v in self.floors.items():
            res += f'{k}: {v}, '
        return res

    def __len__(self):
        return len(self.floors)

    def __setitem__(self, key, value):
        if key <= len(self.floors):
            self.floors[key] = value

    def __getitem__(self, item):
        if item in self.floors:
            return self.floors[item]

    def __delitem__(self, key):
        if key in self.floors:
            self.floors.pop(key)


iron_building = Building(22)  # Создаем здание с 22 этажами
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp Industries'
iron_building[2] = 'Stark Industries'
print(iron_building[2])
del iron_building[2]
print(iron_building[2])