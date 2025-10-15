class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == "side_a":
            if value <= 0:
                print("НЕ МОЖНА змінити сторону. Довжина сторони повинна бути більшою за 0")
            else:
                super().__setattr__(key, value)

        elif key == "angle_a":
            if not (0 < value < 180):
                print("НЕ МОЖНА змінити кут. Кут 'α' повинен бути не включно між 0 та 180° ")
            else:
                super().__setattr__(key, value)
                super().__setattr__("angle_b", 180 - value)

        else:
            super().__setattr__(key, value)

    def display_info(self):
        return f'Ромб: Сторона a: {self.side_a}, Кут α: {self.angle_a}°, Кут β: {self.angle_b}°'

r1= Rhombus(25, 179)
print(r1.display_info())

print("\nЗмінюю кут 'α' на валідне значення 150°:")
r1.angle_a = 150
print(r1.display_info())

print("\nЗмінюю кут 'α' на НЕ валідне значення 181°:")
r1.angle_a = 181
print(r1.display_info())

print("\nЗмінюю сторону 'а' на НЕ валідне значення -15:")
r1.side_a = -15
print(r1.display_info())

