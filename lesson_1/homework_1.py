# task 01 == Виправте синтаксичні помилки
print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03 == Вставте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
bananas = apples * 4
print("Яблук:", apples, "Бананів:", bananas)

# task 05 == виправте назви змінних
side_1 = 1
side_2 = 2
side_3 = 3
side_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimeter = side_1 + side_2 + side_3 + side_4
print("Периметр фігури:", perimeter)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
apples = 4
peers = apples + 5
plums = apples - 2
trees = apples + peers + plums
print("Посадили", apples, "яблук,", peers, "груш,", plums, "сливи.", "Всього це дорівнює", trees, "дерев")

# task 08
"""
# До обіда температура повітря була на 5 градусів вище нуля.
# Після обіду температура опустилася на 10 градусів.
# Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
zero_temperature = 0
morning_temperature = zero_temperature + 5
day_temperature = morning_temperature - 10
evening_temperature = day_temperature + 4
print("Температура надвечір становила", evening_temperature, "градус")

# task 09
"""
# Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
# 1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
# Скільки сьогодні дітей у театральному гуртку?
"""
boys = 24
girls = boys // 2
kids_today = (boys - 1) + (girls - 2)
print("Сьогодні прийшло", kids_today, "дітей до театрального гуртка")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дорожче,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
price_book_1 = 8
price_book_2 = price_book_1 + 2
price_book_3 = (price_book_1 + price_book_2) // 2
copies = 1
total_price = price_book_1 * copies + price_book_2 * copies + price_book_3 * copies
print(total_price, "грн коштують усі книги")