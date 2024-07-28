from threading import Thread
from time import sleep
from datetime import datetime


def wite_words(word_count, file_name):
    with open(file_name, 'w+') as file:
        n = 1
        while n <= word_count:
            file.write(f'Какое-то слово № {n}\n')
            sleep(0.1)
            n += 1
    print(f'Завершилась запись в файл {file_name}')


time1_start = datetime.now()

wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

time1_end = datetime.now()
print(f'Время выполнения без потоков: {time1_end - time1_start}')

time2_start = datetime.now()

args_1 = (10, 'example5.txt')
args_2 = (30, 'example6.txt')
args_3 = (200, 'example7.txt')
args_4 = (100, 'example8.txt')

thr_1 = Thread(target=wite_words, args=args_1)
thr_2 = Thread(target=wite_words, args=args_2)
thr_3 = Thread(target=wite_words, args=args_3)
thr_4 = Thread(target=wite_words, args=args_4)

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

time2_end = datetime.now()
print(f'Время выполнения с потоками: {time2_end - time2_start}')
