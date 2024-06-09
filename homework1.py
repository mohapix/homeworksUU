class Car:
    price = 1000000

    def horse_powers(self):
        return self.horse_power


class Nissan(Car):
    price = 1100000
    horse_power = 110

    def horse_powers(self):
        return None


class Kia(Car):
    price = 1200000
    horse_power = 120

    def horse_powers(self):
        return False


car1 = Nissan()
car2 = Kia()

print(car1.horse_powers())
print(car2.horse_powers())
