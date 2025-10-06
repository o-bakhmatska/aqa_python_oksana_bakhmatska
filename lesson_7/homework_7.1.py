# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while number * multiplier <= 25:
        result = number * multiplier
        print(f"{number}x{multiplier}={result}")

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two_numbers(a, b):
    return a + b

print(f'Task 2. {sum_two_numbers(3, 4)}')

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

nums = [2, 4.4, 6.6, 5, 8, 10, 12, 14]
print(f'Task 3. {average(nums)}')


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(s):
    return s[::-1]

text = "Написати функцію, яка приймає рядок та повертає його у зворотному порядку."
print(f'Task 4. {reverse_string(text)}')

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longest_word(words):
    if not words:
        return None
    return max(words, key=len)

words_list = ["apple", "banana", "strawberry", "kiwi"]
print(f'Task 5. {longest_word(words_list)}')


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(f'Task 6.1. {find_substring(str1, str2)}') # поверне 7


str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(f'Task 6.2. {find_substring(str1, str2)}') # поверне -1

# task 7
def to_lowercase(original_text):
    """
    Function returns string in lower case
    :param original_text: str
    """
    return original_text.lower()

example_text = "Hello, PYTHON!"
print(f'Task 7.{to_lowercase(example_text)}')

# task 8
def word_second_position(input_string, target_word):
    """Returns the position at which the word occurs for the second time
    """

    first_position = input_string.find(target_word)
    if first_position == -1:
        return -1
    second_position = input_string.find(target_word, first_position + 1)
    return second_position

sentence = "Python is fun, and Python is powerful."
search_word = "Python"
print(f'Task 8. {word_second_position(sentence, search_word)}')


# task 9

def split_and_sort_words(input_text):
    """
    Function returns list of words, sorted in ascending order case-insensitively.

    :param input_text: str
    :return: list
    """
    words = input_text.split()
    words.sort(key=str.lower)  # сортуємо незалежно від регістру
    return words

sentence = "Python is a powerful language"
print(f'Task 9. {split_and_sort_words(sentence)}')

# task 10
def find_h_letter():
    """a loop that will require the user to enter a word that contains the letter "h"
    (both uppercase and lowercase are considered).
    The loop is not terminated if the user enters a word without the letter "h".
    """
    while True:
        word = input("Введіть слово, в якому є літера 'h': ")
        if 'h' in word.lower():
            print("Так! У слові є літера 'h'.")
            break
        else:
            print("У слові немає літери 'h'. Спробуйте ще раз.")

print('Task 10:')
find_h_letter()


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""