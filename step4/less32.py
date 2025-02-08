import time
time.time()


class Timer:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args):
        start = time.time()
        print(f'start at {start}')
        self.func()
        end = time.time()
        print(f'end at {end}')
        print(end - start)
@Timer
def calculate():
    for i in range(10000000):
        2 ** 100

calculate()
