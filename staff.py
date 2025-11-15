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

    def get_staff_id(self): return self.__staff_id
    def get_name(self) -> str: return self.__name
    def get_schedule(self) -> dict: return self.__schedule
    def get_salary(self) -> int: return self.__salary
    def get_occupation(self) -> str: return self.__occupation

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

    def remove_staff(self, staff_id: str):
        ...

    @staticmethod
    def staff_search():
        search_results = []
        search_term = input("Enter the employee ID, name, or occupation of the staff you are searching for: ").strip().lower().capitalize()
        for key, value in staff_register.items():
            if search_term in value.__name:
                search_results.append(f"{value.__staff_id}: {value.__name} the {value.__occupation}")
            if search_term in value.__staff_id:
                search_results.append(value)
            if search_term in value.__occupation:
                search_results.append(value)
        if not search_results:
            return f"No staff matching {search_term} found."
        else:
            return f"The following staff matching {search_term} were found:\n{search_results}"

class Zookeeper(Staff):
    ...

    def clean_enclosure(self, enclosure):
        print(f"{self.__name} is now cleaning {enclosure.get_enclosure_id()}")
        enclosure.set_is_clean()
        return f"{enclosure.get_enclosure_id()} cleaned."

    def feed_animal(self, animal):
        ...

    @staticmethod
    def display_zookeepers():
        zookeepers = [[value.get_staff_id(), value.get_name()] for key, value in staff_register.items() if value.get_occupation() == 'Zookeeper']
        return zookeepers

class Vet(Staff):
    ...

    def check_animal(self):
        print(Animal.display_animals())
        animal = input("Enter the ID of the animal to checked: ").lower().strip().capitalize()
        while animal not in animal_register:
                animal = input("Invalid entry. Enter the ID of the animal to be treated: ").lower().strip().capitalize()
        animal_object = animal_register[animal]
        animal_object.get_animal_health()
        choice = input("Do you wish to set up a treatment plan for this animal? (Y/N) ").strip().upper()
        while choice not in ['Y', 'N']:
            choice = input("Invalid input. Please enter Y or N.")
        if choice.lower().strip() == 'y':
            print(self.add_health_record(animal_object))
        display_status = input(f'Do you wish to change the display status of this animal? currently {animal_object.get_display_status()} (Y/N) ')
        while display_status not in ['Y', 'N']:
            display_status = input("Invalid input. Please enter Y or N.")
        if display_status.strip().upper() == 'Y':
            animal_object.set_display_status()
        else:
            print(f"Returning to main menu.")

    @staticmethod
    def add_health_record(animal_object):
        case_id = f"Case_{Staff.health_record_counter}"
        Staff.health_record_counter += 1
        report_date = input('Enter the report date (dd/mm/yyyy): ')
        diagnosis = input('Enter the diagnosis or behavioural issue of the animal: ')
        treatment = input("Enter the treatment for the animal: ")
        treatment_record = {
            'Report date': report_date,
            'Diagnosis': diagnosis,
            'Treatment': treatment,
        }
        animal_object.add_new_health_record(case_id, treatment_record)
        return f"{case_id} added to {animal_object.get_name()}'s health record with the following information: {treatment_record}"

patrick = Vet('Patrick', '160000', 'Vet')
patrick2 = Zookeeper('Patrick', '160000', 'Zookeeper')
# patrick.check_animal()
print(Zookeeper.display_zookeepers())
