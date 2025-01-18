# === DZ 42 Создание потоков ===
import threading
from time import sleep
from datetime import datetime

def wite_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(word_count + 1):
            sleep(0.1)
            file.write(f'Какое-то слово № <{i}>\n')
        print(f'Завершилась запись в файл <{file_name}>')

time_start = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
time_end = datetime.now() - time_start
print(f'Работа функции {time_end}')

# Вспомогательные потоки
start_time_thread = datetime.now()

thread = threading.Thread(target=wite_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=wite_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=wite_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=wite_words, args=(100, 'example8.txt'))

thread.start()
thread2.start()
thread3.start()
thread4.start()

thread.join()
thread2.join()
thread3.join()
thread4.join()

end_time_thread = datetime.now() - start_time_thread

print(f'Работа функции {end_time_thread}')
