class Building:
    total = 0

    def __init__(self):
        Building.total += 1


for i in range(0, 40):
    print(Building(), Building.total)
