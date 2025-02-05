class Date:
    def __init__(self, dd, mm, yy):
        self._dd = dd
        self._mm = mm
        self._yy = yy

    @property
    def dd(self):
        return str(self._dd).zfill(2)

    @property
    def mm(self):
        return str(self._mm).zfill(2)

    @property
    def yy(self):
        return str(self._yy).zfill(4)


class DateUSA(Date):
    def format(self):
        return f'{self.mm}/{self.dd}/{self.yy}'

    def isoformat(self):
        return f'{self.yy}-{self.mm}-{self.dd}'


class DateEurope(DateUSA):
    def format(self):
        return f'{self.dd}/{self.mm}/{self.yy}'


dates = [
    DateUSA(1, 2, 2024),
    DateUSA(2, 2, 2024),
    DateEurope(20, 9, 2024),
    DateEurope(17, 12, 2024),
    DateUSA(3, 2, 2022),
    DateEurope(14, 3, 2001),
]
for d in dates:
    print(d.format())
    print(d.isoformat())
    print('-' * 10)