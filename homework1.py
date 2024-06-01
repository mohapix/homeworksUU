class House:

    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
            return
        n = 1
        while n <= new_floor:
            print(n)
            n += 1


# elbrus = House('ЖК Эльбрус', 30)
# elbrus.go_to(int(input('Введите этаж: ')))
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
