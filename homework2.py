class Vehicle:
    vehicle_type = None


class Car:
    price = 1000000

    def horse_powers(self):
        return self.horse_power


class Nissan(Car, Vehicle):
    vehicle_type = 'Nissan'
    price = 1100000
    horse_power = 110

    def horse_powers(self):
        return None


car1 = Nissan()
print(car1.vehicle_type, car1.price, car1.horse_powers())
