from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self):
        self.__sides = []
        self.__color = []
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, rgb):
        return all(isinstance(color, int) and 0 <= color <= 255 for color in rgb)

    def set_color(self, r, g, b):
        rgb = [r, g, b]
        if self.__is_valid_color(rgb):
            self.__color = [*rgb]

    def set_sides(self, *args):
        if self.__is_valid_sides(*args):
            self.__sides = [*args]
        elif not self.__sides:
            while len(self.__sides) < self.sides_count:
                self.__sides.append(1)
        if isinstance(self, Circle):
            self._set_radius()
        elif isinstance(self, Triangle):
            self._set_height()

    def __is_valid_sides(self, *args):
        sides = [*args]
        if len(sides) != self.sides_count:
            return False
        for side in sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    def __len__(self):
        return sum(self.__sides)

    def get_sides(self):
        return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, rgb, *args):
        super().__init__()
        self.__radius = 0
        self.set_sides(*args)
        self.set_color(*rgb)

    def _set_radius(self):
        self.__radius = round(self.get_sides()[0] / pi / 2, 2)

    def get_square(self):
        return round(self.__radius ** 2 * pi, 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, rgb, *args):
        super().__init__()
        self.__height = 0
        self.set_sides(*args)
        self.set_color(*rgb)

    def _set_height(self):
        self.__height = 2 * self.get_square() / self.get_sides()[2]

    def get_square(self):
        p = len(self) / 2
        a, b, c = self.get_sides()
        return round(sqrt(p * (p - a) * (p - b) * (p - c)), 2)


class Cube(Figure):
    sides_count = 12

    def __init__(self, rgb, *args):
        super().__init__()
        self.set_sides(*args)
        self.set_color(*rgb)

    def set_sides(self, *args):
        sides = []
        if len(args) == 1:
            side = args[0]
            while len(sides) < self.sides_count:
                sides.append(side)
        print('sides:', sides)
        super().set_sides(sides)

    def get_volume(self):
        pass


# circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
# triangle1 = Triangle((222, 35, 130), 10, 10, 10, 10)
print(cube1.get_sides())

# Проверка на изменение цветов:
# circle1.set_color(55, 66, 77)  # Изменится
# cube1.set_color(300, 70, 15)  # Не изменится
# print(circle1.get_color())
# print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
# circle1.set_sides(15)  # Изменится
# triangle1.set_sides(10, 10, 10)
print(cube1.get_sides())
# print(circle1.get_sides())
# print(triangle1.get_sides())

# Проверка периметра (круга), это и есть длина:
# print(len(circle1))
# print(len(cube1))
# print(len(triangle1))
# print(triangle1.get_square())

# Проверка объёма (куба):
# print(cube1.get_volume())
