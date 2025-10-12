class Student:
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

student1 = Student("Alex", "Forbes", 20, 88.5)

print("Student's info:")
student1.display_info()

print("\nUpdating Average grade...")
student1.change_average_grade(92.3)

print("\nUpdated student's info:")
student1.display_info()
