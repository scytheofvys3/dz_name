# === DZ 39 Итераторы ===

class StepValueError(ValueError):
    def __init__(self, message):
        self.message = message

class Iterator:

    def __init__(self, start, stop, step=1):
        if not isinstance(start, int):
            raise ValueError('Нужно целое число в start')
        self.start = start
        if not isinstance(stop, int):
            raise ValueError('Нужно целое число в stop ')
        self.stop = stop
        if step == 0:
            raise StepValueError("Шаг не может быть равен нулю")
        self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        print(f'{self.pointer}', end=' ')
        return self

    def __next__(self):
        if self.step < 0:
            self.pointer += self.step
            if self.pointer < self.stop:
                print('')
                raise StopIteration()
        elif self.start > self.stop:
            self.pointer -= self.step
            if self.pointer < self.stop:
                print('')
                raise StopIteration()
        else:
            self.pointer += self.step
            if self.pointer > self.stop:
                print('')
                raise StopIteration()
        # if self.start > self.stop:
        #     self.pointer -= self.step
        #     if self.pointer < self.stop:
        #         raise StopIteration()
        # if self.start < self.stop:
        #     self.pointer += self.step
        #     if self.pointer > self.stop:
        #         raise StopIteration()
        return self.pointer

        # if self.step < -0:
        #     self.pointer += self.step
        #     if self.pointer < self.stop:
        #         raise StopIteration()
        # if self.step > 0:
        #     self.pointer -= self.step
        #     if self.pointer >= self.stop:
        #         raise StopIteration()
        # return self.pointer
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError as exc:
    print(f'Шаг указан неверно: {exc}')
except ValueError as exc:
    print(f'{exc}')

try:
    iter1 = Iterator(100.1, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError as exc:
    print(f'Шаг указан неверно: {exc}')
except ValueError as exc:
    print(f'{exc}')

try:
    iter1 = Iterator(100, 200.1, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError as exc:
    print(f'Шаг указан неверно: {exc}')
except ValueError as exc:
    print(f'{exc}')


iter2 = Iterator(-50, 1)
iter3 = Iterator(6, 105, 2)
iter4 = Iterator(56, 1, -2)
iter5 = Iterator(120, 10)

# iter2 = Iterator(-5, 1)
# iter3 = Iterator(6, 15, 2)
# iter4 = Iterator(5, 1, -1)
# iter5 = Iterator(10, 1)

for i in iter2:
    print(f'{i}',end=' ')
    # print(' ')
for i in iter3:
    print(f'{i}',end=' ')
    # print(' ')
for i in iter4:
    print(f'{i}',end=' ')
    # print(' ')
for i in iter5:
    print(f'{i}',end=' ')
    # print(' ')
# я три часа делал это. ахаха)
