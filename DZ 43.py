# === DZ 43 Потоки на классах ===
import threading
import time

class Knight(threading.Thread):
    __HP_BOT = 100
    __DAY = 0
    def __init__(self, name, power):
        super().__init__()
        #threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)


    def fight(self, name, power):
        while True:
            self.__HP_BOT -= self.power
            self.__DAY += 1
            print(f'{self.name} Сражается {self.__DAY} день/дня, осталось {self.__HP_BOT} воинов!')
            time.sleep(1.1)
            if self.__HP_BOT <= 0:
                return f'{self.name} одержал победу спустя {self.__DAY} дней/дня!'
            # else:
            #     print(f'{self.name} одержал победу спустя {self.sleep_day} дней')
            #     break

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.fight(self.name, self.power)
        # first_knight.join()
        # second_knight.join()
        #print(f'Все битвы окончены. Воцарился мир!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print(f'Все битвы окончены. Воцарился мир!')





