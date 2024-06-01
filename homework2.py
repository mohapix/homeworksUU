class House:

    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors += floors
        print(self.numberOfFloors)


my_house = House()
my_house.setNewNumberOfFloors(4)
