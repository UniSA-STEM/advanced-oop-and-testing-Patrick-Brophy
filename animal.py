'''
File: animal.py
Description: Lorem
Author: Patrick Brophy
ID: 110070814
Username: bropy009
This is my own work as defined by the University's Academic Integrity Policy.
'''
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
        self.__is_healthy = 'Healthy'
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

    @staticmethod
    def display_animals():
        display_details = []
        print("-" * 45, 'Animal Register', "-" * 45)
        print("ANIMAL ID | CLASS   |   SPECIES   |     NAME    |  AGE | GENDER | ON DISPLAY |   HABITAT   |     DIET     |   FEATURES")
        for id, details in animal_register.items():
            display_details.append(f"{id:<10}: {details.get_display_data()}")
        return "\n".join(display_details)

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
