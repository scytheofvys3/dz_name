# === DZ 37 Генераторные сборки ===

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
print(list(first_result))

second_result = (range(len(first[0])) == range(len(second[0])),
                 range(len(first[1])) == range(len(second[1])),
                 range(len(first[2])) == range(len(second[2]))
                 )
# second_result = (len(x) == len(y) or len(x) != len(y) for x in first for y in second if range(len(x)) == range(len(y)))
# тут получается что мы уходили во внутренний цикл и сравнения получались некорректным.
# получалось что внутренний цикл сравнивал свою переменную несколько раз из первого,
# а нам требовалось сравнить каждый элемент строго друг над другом так сказать
# долго думал зачем нам тут range пока не осенило)
print(list(second_result))

# first = ['Strings', 'Student', 'Computers']
# print(range(len(first[0])))
# print(range(len(second[0])))
# print(range(len(first[1])))
# print(range(len(second[1])))
# print(range(len(first[2])))
# print(range(len(second[2])))
