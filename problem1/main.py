# tulis solusi code disini
import math
class Shape:
    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

    def calculate_perimeter(self):
        return 4 * self.side


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def calculate_perimeter(self):
        return self.base + self.height + (self.base ** 2 + self.height ** 2) ** 0.5


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


def main():
    shapes = {
        "Persegi": Square(4),
        "Segitiga": Triangle(3, 4),
        "Persegi Panjang": Rectangle(7, 8)
    }

    for shape_name, shape in shapes.items():
        print(f"{shape_name} :")
        print(f"Luas : {shape.calculate_area()}")
        print(f"Keliling : {shape.calculate_perimeter()}")
        print()