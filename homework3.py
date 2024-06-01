class Building:

    def __init__(self, floors, type):
        self.numberOfFloors = floors
        self.buildingType = type

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


h1 = Building(10, 'Многоэтажный дом')
h2 = Building(10, 'Многоэтажный дом')
h3 = Building(9, 'Многоэтажный дом')
h4 = Building(10, 'Многоэтажное строение')
print(h1 == h2)
print(h2 == h3)
print(h1 == h4)
