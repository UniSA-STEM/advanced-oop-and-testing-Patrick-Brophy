'''
File: filename.py
Description: A brief description of this Python module.
Author: Patrick Brophy
ID: 110070814
Username: bropy009
This is my own work as defined by the University's Academic Integrity Policy.
'''
from abc import ABC

from animal import Animal, Mammal, Reptile, Bird, animal_register

staff_register = {}

class Staff(ABC):
    staff_counter = 1
    health_record_counter = 1
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

    def add_health_record(self):
        print(Animal.get_health_status())
        animal = input("Enter the ID of the animal to be treated: ").lower().strip().capitalize()
        while True:
            if animal not in animal_register:
                animal = input("Invalid entry. Enter the ID of the animal to be treated: ").lower().strip().capitalize()
            else:
                break
        case_id = f"Case_{Staff.health_record_counter}"
        Staff.health_record_counter += 1
        diagnoses = input("Enter the diagnoses of the animal: ")
        treatment = input("Enter the treatment for the animal: ")
        treatment_record = {
            'Diagnoses': diagnoses,
            'Treatment': treatment,
        }
        animal_object = animal_register[animal]
        animal_object.add_new_health_record(case_id, treatment_record)
        return f"{case_id} added to {animal_object.get_name()}'s health record with the following information: {treatment_record}"

patrick = Vet('Patrick', '160000', 'Vet')
print(patrick.add_health_record())

