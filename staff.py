'''
File: filename.py
Description: A brief description of this Python module.
Author: Patrick Brophy
ID: 110070814
Username: bropy009
This is my own work as defined by the University's Academic Integrity Policy.
'''
from abc import ABC
staff_register = {}

class Staff(ABC):
    staff_counter = 1
    def __init__(self, name: str, salary: int, occupation: str, **kwargs):
        super().__init__(**kwargs)
        self.__staff_id = f"Staff_{Staff.staff_counter}"
        self.__name = name.strip().lower().capitalize()
        self.__salary = salary
        self.__schedule = {'Monday': None, 'Tuesday': None, 'Wednesday': None, 'Thursday': None, 'Friday': None, 'Saturday': None, 'Sunday': None}
        self.__occupation = occupation.strip().lower().capitalize()
        staff_register[self.__staff_id] = self
        Staff.staff_counter += 1

    def get_name(self) -> str: return self.__name
    def get_schedule(self) -> dict: return self.__schedule
    def get_salary(self) -> int: return self.__salary

    @classmethod
    def get_staff_details(cls):
        staff_details = []
        print(f"{"-" * 15} Staff Details {"-" * 15}")
        print(f"STAFF ID |    Name    |  Salary  |  Occupation")
        for key, value in staff_register.items():
            staff_details.append(f"{key:<11}{value.__name:<14}{value.__salary:<11}{value.__occupation}")
        return "\n".join(staff_details)

    def increase_salary(self, amount: int):
        self.__salary += amount

    def remove_staff(self):
        ...

class Zookeeper(Staff):
    ...

    def clean_enclosure(self, enclosure):
        ...

    def feed_animal(self, animal):
        ...

class Vet(Staff):
    ...

    def check_animal(self, animal):
        ...

    def treat_animal(self, animal):
        ...

