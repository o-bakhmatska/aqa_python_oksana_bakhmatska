# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
# Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
# Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
# Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side ** 2

    def perimeter(self):
        return 4 * self.__side


class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return round(math.pi, 2) * self.__radius ** 2

    def perimeter(self):
        return 2 * round(math.pi, 2) * self.__radius


shapes = [
    Square(5),
    Rectangle(4, 6),
    Circle(3)
]

for shape in shapes:
    print(f"{shape.__class__.__name__}:")
    print(f"  Area: {shape.area()}")
    print(f"  Perimeter: {shape.perimeter()}")


