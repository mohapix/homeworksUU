import threading
import queue
import time


class Table:

    def __init__(self, number):
        self.number: int = number
        self.is_free: bool = True

    def __call__(self, customer):
        with customer.lock:
            self.is_free = False
            time.sleep(5)
            self.is_free = True


class Cafe:

    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables: list = tables
        self.customers_limit: int = 20

    def customer_arrival(self):
        n = 1
        while True:
            if n <= self.customers_limit:
                customer = Customer(n)
                print(f'Посетитель номер {n} прибыл.')
                self.serve_customer(customer)
                n += 1
            elif not self.queue.empty():
                self.serve_customer()

            if n > self.customers_limit and self.queue.empty() and all(table.is_free for table in self.tables):
                break

            time.sleep(1)

    def serve_customer(self, customer=None):
        if any(table.is_free for table in self.tables):
            if not self.queue.empty():
                if customer is not None:
                    self.queue.put(customer)
                    print(f'Посетитель номер {customer.number} ожидает свободный стол.')
                customer = self.queue.get()

            for table in self.tables:
                if table.is_free:
                    customer.table = table
                    customer.start()
                    break

        elif customer is not None:
            self.queue.put(customer)
            print(f'Посетитель номер {customer.number} ожидает свободный стол.')


class Customer(threading.Thread):

    def __init__(self, number):
        super().__init__()
        self.number: int = number
        self.lock = threading.Lock()
        self.table = None

    def run(self):
        print(f'Посетитель номер {self.number} сел за стол {self.table.number}.')
        self.table(self)
        print(f'Посетитель номер {self.number} покушал и ушёл.')


# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
