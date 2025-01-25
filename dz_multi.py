# === DZ 46 Многопроцессное программирование ===

import multiprocessing
import datetime
from os import cpu_count


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            all_data.append(line)
        print(f'{name} обрабатывается')
    return


filenames = [f'file {number}.txt' for number in range(1, 5)]

# Линейный вызов
# start_time = datetime.datetime.now()
# for i in filenames:
#     read_info(i)
# print(f'{datetime.datetime.now() - start_time}')


# Многопроцессный вызов
if __name__ == '__main__':
    with multiprocessing.Pool(processes=cpu_count()) as pool:
        start_time = datetime.datetime.now()
        pool.map(read_info, filenames)
        print(f'{datetime.datetime.now() - start_time}')

