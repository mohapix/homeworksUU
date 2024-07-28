from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies_left = 100
        days = 0
        while enemies_left > 0:
            sleep(1)
            enemies_left -= self.power
            days += 1
            print(f'{self.name} сражается {days} {days_str(days)}, осталось {enemies_left} воинов.')
        print(f'{self.name} одержал победу спустя {days} {days_str(days)}!')


def days_str(days):
    if 4 < days < 21:
        res = 'дней'
    elif str(days)[-1] == '1':
        res = 'день'
    else:
        res = 'дня'
    return res


threads = []
knights = [('Sir Lancelot', 10), ("Sir Galahad", 20), ]

for knight in knights:
    thread = Knight(*knight)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print('Все битвы закончились!')
