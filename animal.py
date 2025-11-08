'''
File: animal.py
Description: Lorem
Author: Patrick Brophy
ID: 110070814
Username: bropy009
This is my own work as defined by the University's Academic Integrity Policy.
'''
animal_dict = {}
class Animal:
    animal_ID = 1
    def __init__(self, name: str, age: int, gender: bool, species: str, biome: str, diet: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__ID = f"Animal{Animal.animal_ID}"
        self.__name = name
        self.__age = age
        if gender:
            self.__gender = 'Male'
        else:
            self.__gender = 'Female'
        self.__species = species
        self.__biome = biome
        self.__diet = diet
        self.__is_healthy = 'Healthy'
        self.animal_ID += 1
        animal_dict[self.__ID] = [self.__name, self.__age, self.__gender, self.__species, self.__biome, self.__diet, self.__is_healthy]

    def get_ID(self) -> str: return self.__ID
    def get_name(self) -> str: return self.__name
    def get_age(self) -> int: return self.__age

class Mammal(Animal):
    def __init__(self, name: str, age: int, gender: bool, species: str, biome: str, diet: str, coat: bool, coat_colour: str, **kwargs) -> None:
        super().__init__(name=name, age=age, gender=gender, species=species, biome=biome, diet=diet, **kwargs)
        if coat:
            self.__coat = 'Fur'
        else:
            self.__coat = 'Skin'
        self.__coat_colour = coat_colour

    def __str__(self) -> str:
        return f"{self.get_name()} {self.get_ID()}"

class Reptile(Animal):
    def __init__(self, name: str, age: int, gender: bool, species: str, biome: str, diet: str, skin: bool, skin_colour: str, **kwargs) -> None:
        super().__init__(name=name, age=age, gender=gender, species=species, biome=biome, diet=diet, **kwargs)
        if skin:
            self.__skin = 'scales'
        else:
            self.__skin = 'plates'
        self.__skin_colour = skin_colour

class Bird(Animal):
    def __init__(self, name: str, age: int, gender: bool, species: str, biome: str, diet: str, fly: bool, wing_span: int, **kwargs) -> None:
        super().__init__(name=name, age=age, gender=gender, species=species, biome=biome, diet=diet, **kwargs)
        if fly:
            self.__fly = True
        else:
            self.__fly = False
        self.__wing_span = wing_span

animal1 = Mammal('George', 12, False, 'Koala', 'Woods', 'Herbivore', False, 'Blue')
animal2 = Mammal('George', 12, False, 'Koala', 'Woods', 'Herbivore', False, 'Blue')
print(animal1)
print(animal2)
print(animal_dict)