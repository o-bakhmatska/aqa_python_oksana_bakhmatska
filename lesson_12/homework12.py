def divide(numerator, denominator):
    """
    Divides numerator by denominator with type checking and division by zero.
    :param numerator: numerator (number)
    :param denominator: denominator (number)
    :return: division result
    :raises TypeError: if the arguments are not numbers
    :raises ValueError: if denominator == 0
    """
    if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
        raise TypeError("Both arguments must be numbers!")

    if denominator == 0:
        raise ValueError("Division by zero is impossible!")

    return numerator / denominator



class Student:
    """
    The Student class represents a student with basic data and methods for working with it.
    Attributes:
        name (str): Student's first name
        surname (str): Student's last name
        age (int): Student's age
        average_grade (float): Student's average grade
        Methods:
            display_info(): Displays student information
            change_average_grade(new_grade): Changes a student's average grade
     """
    def __init__(self, first_name, last_name, age, average_grade):
        self.name = first_name
        self.surname = last_name
        self.age = age
        self.average_grade = average_grade

    def display_info(self):
        print(f"First name: {self.name}")
        print(f"Last name: {self.surname}")
        print(f"Age: {self.age}")
        print(f"Average_grade: {self.average_grade}")

    def change_average_grade(self, new_grade):
        self.average_grade = new_grade
        print(f"Average grade was changed to: {self.average_grade}")

class ArrayTransformer:
    """
    A class for working with an array of strings containing comma-separated numbers.
    Attributes:
       data (list[str]): A list of strings, where each string contains comma-separated numbers.
    Methods:
       sum_of_numbers(s: str) -> int | str: A static method that sums the numbers in a string.
    Returns the sum of the numbers, or the message "Can't do this!" if there is invalid data.
    transform_all() -> list[int | str]: Applies sum_of_numbers to all elements of data and returns a list of the results.
    """
    def __init__(self, data):
        self.data = data

    @staticmethod
    def sum_of_numbers(s):
        try:
            numbers = [int(x) for x in s.split(',')]
            return sum(numbers)
        except ValueError:
            return "Не можу це зробити!"

    def transform_all(self):
        return [self.sum_of_numbers(item) for item in self.data]