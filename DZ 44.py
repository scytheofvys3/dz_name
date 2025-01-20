# === DZ 44 Блокировки и обработка ошибок ===
from random import randint
import threading
from time import sleep

class Bank():
    def __init__(self):
        self.balance = int(0)
        self.lock = threading.Lock()

    def deposit(self):
        x = 0
        while x < 100:
            refill = randint(50, 500)
            self.balance += refill
            print(f'Пополнение {refill}. Баланс {self.balance}')
            sleep(0.002)
            if self.balance >= 500 and self.lock.locked() == True:
                self.lock.release()
                #x += 1
            x += 1

    def take(self):
        x = 0
        while x < 100:
            refill = randint(50, 500)
            print(f'Запрос на {refill}')
            if refill <= self.balance:
                self.balance -= refill
                print(f'Снятие: {refill}. Баланс: {self.balance}')
                sleep(0.002)
                x += 1
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
                #break
                #x += 1

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')



