class Student:
    def __init__(self, name, marks=None):
        self.name = name
        self._course = 1
        self._marks = marks or []

    def __getitem__(self, item):
        return self.__dict__[item]


student = Student(name="Kevin", marks=[5, 4, 3])
print(student['marks'])