# Створіть клас Employee, який має атрибути name та salary.
# Далі створіть два класи, Manager та Developer, які успадковуються від Employee.
# Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.
# Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ),
# Developer(ім'я, зарплата, мова програмування), а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.


class Employee:
    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary
        super().__init__(**kwargs)

class Manager(Employee):
    def __init__(self, name, salary, department, **kwargs):
        super().__init__(name=name, salary=salary, **kwargs)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language, **kwargs):
        super().__init__(name=name, salary=salary, **kwargs)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size, **kwargs):
        super().__init__(name=name, salary=salary,
                         department=department,
                         programming_language=programming_language, **kwargs)
        self.team_size = team_size

lead = TeamLead("Оksana", 8000, "AQA", "Python", 5)

print(lead.name)
print(lead.salary)
print(lead.department)
print(lead.programming_language)
print(lead.team_size)

print(TeamLead.mro())
