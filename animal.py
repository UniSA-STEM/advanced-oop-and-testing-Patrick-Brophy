'''
File: animal.py
Description: Lorem
Author: Patrick Brophy
ID: 110070814
Username: bropy009
This is my own work as defined by the University's Academic Integrity Policy.
'''
from enclosure import enclosure_register

animal_register = {}
from abc import ABC

class Animal(ABC):
    animal_counter = 1
    def __init__(self, family: str, species: str, name: str, age: int, gender: str, biome: str, diet: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__id = f"Animal_{Animal.animal_counter}"
        self.__family = family
        self.__species = species
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__biome = biome
        self.__diet = diet
        self.__health = 'Healthy'
        self.__health_record = {}
        self.__enclosure_ID = None
        self.__on_display = False
        Animal.animal_counter += 1
        animal_register[self.__id] = self

    def get_display_data(self) -> str:
        common_data = f"{self.__family:<10}{self.__species:<13} {self.__name:<14} {self.__age:<5} {self.__gender:<13}{ 'Yes' if self.__on_display else 'No':<8} {self.__biome:<13} {self.__diet:<15}"
        return common_data

    def get_id(self) -> str: return self.__id
    def get_name(self) -> str: return self.__name
    def get_age(self) -> int: return self.__age
    def get_species(self) -> str: return self.__species
    def get_gender(self) -> str: return self.__gender
    def get_biome(self) -> str: return self.__biome
    def get_diet(self) -> str: return self.__diet
    def get_health(self) -> str: return self.__health
    def set_enclosure_ID(self, enclosure_id: str) -> None: self.__enclosure_ID = enclosure_id
    def get_on_display(self) -> bool: return self.__on_display
    def set_on_display(self, on_display: bool) -> None: self.__on_display = on_display
    def get_health_record(self) -> dict: return self.__health_record

    @staticmethod
    def display_animals():
        display_details = []
        print("-" * 45, 'Animal Register', "-" * 45)
        print("ANIMAL ID | CLASS   |   SPECIES   |     NAME    |  AGE | GENDER | ON DISPLAY |   HABITAT   |     DIET     |   FEATURES")
        for id, details in animal_register.items():
            display_details.append(f"{id:<10}: {details.get_display_data()}")
        return "\n".join(display_details)

    @staticmethod
    def get_health_status():
        animal_health_list = []
        for animal in animal_register.values():
            animal_health_list.append(f"{animal.__id}: {animal.__name} the {animal.__species}'s current health status is: {animal.__health}")
        return animal_health_list

    def get_animal_health(self):
        print(f"{self.__id}: {self.__name} the {self.__species}'s current health status is: {self.__health}")

    def set_health(self, health: str) -> None:
        self.__health = health

    def add_new_health_record(self, case_id: str, treatment_record: dict) -> None:
        self.__health_record[case_id] = treatment_record

    @staticmethod
    def animal_search():
        search_results = []
        search_term = input("Enter the ID, name, species, biome, or class of the animal you are searching for: ").strip().lower().capitalize()
        for key, value in animal_register.items():
            if (search_term in value.get_name()
            or search_term in value.get_biome()
            or search_term in value.get_species()
            or search_term in value.get_family()
            or search_term in value.get_id()):
                search_results.append(f"{value.get_id()}: {value.get_name()} the {value.get_species()} of class {value.get_family()}, native to {value.get_biome()}")
        if not search_results:
            return f"No animals matching {search_term} found."
        else:
            results_string = "\n".join(search_results)
            return f"The following animals matching '{search_term}' were found:\n {results_string}"

    def search_health_record(self):
        ...

    def remove_animal_from_enclosure(self) -> str | None:
        if not self.__enclosure_ID:
            return f"{self.get_id()}: {self.get_name()} is not currently assigned to an enclosure."
        else:
            enclosure = enclosure_register[self.__enclosure_ID]
            enclosure.set_occupancy()
            return f"{self.get_id()}: {self.get_name()} removed from {enclosure.get_enclosure_id()}.

    def remove_animal_record(self):
        animal = input(f"Enter the ID of the animal you would like to remove: ")
        while animal not in animal_register.keys():
            print(Animal.display_animals())
            animal = input(f"Invalid input. Enter the ID of the animal you would like to remove: ")
        choice = input(f"Are you sure you want to remove {animal} - y/n: ").strip().lower()
        while choice not in ['y', 'n']:
            choice = input(f"Invalid entry. Please enter 'y' or 'n: ").strip().lower()
            if choice == 'y':
                del animal_register[animal]
                return None
            else:
                return f"Animal removal cancelled."

class Mammal(Animal):
    def __init__(self, species: str, name: str, age: int, gender: str, biome: str, diet: str, coat: str,
                 coat_colour: str,
                 **kwargs: object) -> None:
        super().__init__(family='Mammal', species=species, name=name, age=age, gender=gender, biome=biome, diet=diet, **kwargs)
        self.__coat = coat
        self.__coat_colour = coat_colour

    def get_display_data(self) -> str:
        base_data = super().get_display_data()
        mammal_data = f"{self.__coat:<7} {self.__coat_colour}"
        return base_data + mammal_data

class Reptile(Animal):
    def __init__(self, species: str, name: str, age: int, gender: str, biome: str, diet: str, skin: str, skin_colour: str, **kwargs) -> None:
        super().__init__(family='Reptile', species=species, name=name, age=age, gender=gender, biome=biome, diet=diet, **kwargs)
        self.__skin = skin
        self.__skin_colour = skin_colour

    def get_display_data(self) -> str:
        base_data = super().get_display_data()
        reptile_data = f"{self.__skin:<7} {self.__skin_colour}"
        return base_data + reptile_data

class Bird(Animal):
    def __init__(self, species: str, name: str, age: int, gender: str, biome: str, diet: str, fly: str, wing_span: int, **kwargs) -> None:
        super().__init__(family='Bird', name=name, age=age, gender=gender, species=species, biome=biome, diet=diet, **kwargs)
        self.__fly = fly
        self.__wing_span = wing_span

    def get_display_data(self) -> str:
        base_data = super().get_display_data()
        bird_data = f"{self.__fly:<7} {self.__wing_span}cm"
        return base_data + bird_data


# animal1 = Mammal('koala', 'geoff', '13', 'Male', 'Woods', 'Herbivore', 'Fur', 'Grey')