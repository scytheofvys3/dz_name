# === DZ 45 Очереди для обмена данными между потоками ===

from random import randint
from time import sleep
import threading
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

    def __repr__(self):
        return f'{self.number}, {self.guest}'

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return f'{self.name}'

    def run(self):
        sleep(randint(3, 10))

class Cafe():
    def __init__(self, *args):
        self.queue = Queue()
        self.tables = [*args]

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')
        #while True:
        # if Table.guest is None:
        #     Table.table = self.queue.get(guests)
        #     Guest.start()
        #     print(f'{Guest.name} сел(-а) за стол номер {Table.number}')
        # else:
        #     self.queue.put(guests)
        #     print(f'{Guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.name} за текущим столом {table.number} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    if not self.queue.empty():
                        guest = self.queue.get()
                        table.guest = guest
                        guest.start()
                        print(f'{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
            sleep(0.5)

        # if self.queue.empty() is not None:
        #     if Guest.is_alive() == False:
        #         print(f'{Guest.name} за текущим столом {self.table} покушал(-а) и ушёл(ушла)')
        #         print(f'Стол номер {self.table} свободен')
        #         Table.guest = None
        # if self.queue.empty() and Table.guest == None:
        #     Table.guest = self.queue.get()
        #     print(f'{Guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {self.table}')
        #     Guest.start(guests)



# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()