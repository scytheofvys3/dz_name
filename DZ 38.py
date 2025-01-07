# === DZ 38 Создание функций на лету ===
from random import choice

# Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y:x[0]==y[0] ,first, second)))
# получается что индекс увеличивается с каждым проходом из-за map
# так как она проходит по всем элементам в последовательности

# Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, "w", encoding='utf-8') as file:
            # w перезапись
            # a добавление в конце
            file.write(str(f'{data_set}\n'))
    return write_everything

write = get_advanced_writer('example.txt')# на этом моменте у нас происходит замыкание
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
# здесь у нас write подставляет значение к функции которая возвращалась

# Класс как функция. Метод __call__
class MysticBall:
    def __init__(self, *words):
        self.words = list(words)

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())



