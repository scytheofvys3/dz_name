# === DZ 43 Потоки на классах ===
import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        #threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)
        self.bot = 100
        self.sleep_day = 0

    def fight(self, name, power):
        while True:
            self.bot -= self.power
            self.sleep_day += 1
            print(f'{self.name} Сражается {self.sleep_day} день/дня, осталось {self.bot} воинов!')
            time.sleep(1.1)
            if self.bot <= 0:
                print(f'{self.name} одержал победу спустя {self.sleep_day} дней/дня!')
                break
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





