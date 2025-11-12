'''
File: filename.py
Description: A brief description of this Python module.
Author: Patrick Brophy
ID: 110070814
Username: bropy009
This is my own work as defined by the University's Academic Integrity Policy.
'''
from abc import ABC
from tkinter.font import names

staff_register = {}

class Staff(ABC):
    staff_counter = 1
    def __init__(self, name, salary, **kwargs):
        super().__init__(**kwargs)
        self.__staff_id = f"StaffID.{Staff.staff_counter}"
        self.__name = name
        self.__salary = salary
        self.__schedule = {}
        Staff.staff_counter += 1

    def get_staff_details(cls):
        staff_details = []
        for key, value in staff_register.items():
            staff_details.append(value)
        ...

    def increase_salary(self, amount):
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







