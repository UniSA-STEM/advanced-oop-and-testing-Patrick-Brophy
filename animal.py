'''
File: animal.py
Description: Lorem
Author: Patrick Brophy
ID: 110070814
Username: bropy009
This is my own work as defined by the University's Academic Integrity Policy.
'''
animal_register = {}

class Animal:
    animal_id = 1
    def __init__(self, family: str, species: str, name: str, age: int, gender: bool, biome: str, diet: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__id = f"Animal.{Animal.animal_id}"
        self.__family = family
        self.__species = species
        self.__name = name
        self.__age = age
        if gender:
            self.__gender = 'Male'
        else:
            self.__gender = 'Female'
        self.__biome = biome
        self.__diet = diet
        self.__is_healthy = 'Healthy'
        self.__enclosure_ID = None
        Animal.animal_id += 1
        animal_register[self.__id] = self

    def __str__(self):
        return f""

    def get_display_data(self) -> str:
        return f"{self.__family} {self.__species} {self.__name} {self.__age} {self.__gender} {self.__biome} {self.__diet}"

    def get_id(self) -> str: return self.__id
    def get_name(self) -> str: return self.__name
    def get_age(self) -> int: return self.__age

    @staticmethod
    def display_animals():
        display_details = []
        print('------ Animal Register------')
        print("Animal ID - Class - Species - Name - Age - Gender - Biome - Diet")
        for id, details in animal_register.items():
            display_details.append(f"{id}: {details.get_display_data()}")
        return "\n".join(display_details)

    def create_animal(cls, animal_family: str, **kwargs) -> 'Animal':
        families = {
            'Mammal': Mammal,
            'Reptile': Reptile,
            'Bird' : Bird
        }
        AnimalFamily = families.get(animal_family)
        if not AnimalFamily:
            raise Exception(f"Animal family {animal_family} not found. Must be one of Mammal, Reptile, or Bird")
        return AnimalFamily(**kwargs)


class Mammal(Animal):
    def __init__(self, species: str, name: str, age: int, gender: bool, biome: str, diet: str, coat: bool, coat_colour: str, **kwargs) -> None:
        super().__init__(family='Mammal', species=species, name=name, age=age, gender=gender, biome=biome, diet=diet, **kwargs)
        if coat:
            self.__coat = 'Fur'
        else:
            self.__coat = 'Skin'
        self.__coat_colour = coat_colour

class Reptile(Animal):
    def __init__(self, species: str, name: str, age: int, gender: bool, biome: str, diet: str, skin: bool, skin_colour: str, **kwargs) -> None:
        super().__init__(family='Reptile', species=species, name=name, age=age, gender=gender, biome=biome, diet=diet, **kwargs)
        if skin:
            self.__skin = 'Scales'
        else:
            self.__skin = 'Plates'
        self.__skin_colour = skin_colour

class Bird(Animal):
    def __init__(self, species: str, name: str, age: int, gender: bool, biome: str, diet: str, fly: bool, wing_span: int, **kwargs) -> None:
        super().__init__(family='Bird', name=name, age=age, gender=gender, species=species, biome=biome, diet=diet, **kwargs)
        if fly:
            self.__fly = True
        else:
            self.__fly = False
        self.__wing_span = wing_span

animal1 = Mammal('Koala', 'George', 1, False, 'Woods', 'Herbivore', False, 'Blue')
animal2 = Mammal('Koala', 'Paul', 2, False, 'Woods', 'Herbivore', False, 'Blue')
animal3 = Mammal('Koala', 'Ringo', 3, False, 'Woods', 'Herbivore', False, 'Blue')
print(Animal.display_animals())