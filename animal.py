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
    animal_counter = 1
    def __init__(self, family: str, species: str, name: str, age: int, gender: bool, biome: str, diet: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__id = f"Animal.{Animal.animal_counter}"
        self.__family = family
        self.__species = species
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__biome = biome
        self.__diet = diet
        self.__is_healthy = 'Healthy'
        self.__enclosure_ID = None
        self.__on_display = False
        Animal.animal_counter += 1
        animal_register[self.__id] = self

    def __str__(self):
        return f""

    def get_display_data(self) -> str:
        return animal_register.items()

    def get_id(self) -> str: return self.__id
    def get_name(self) -> str: return self.__name
    def get_age(self) -> int: return self.__age

    @staticmethod
    def display_animals():
        display_details = []
        print('------ Animal Register------')
        print("ANIMAL ID | CLASS   |   SPECIES   |     NAME    |  AGE | GENDER |   HABITAT   |   DIET")
        for id, details in animal_register.items():
            display_details.append(f"{id:<10}: {details.get_display_data()}")
        return "\n".join(display_details)

class Mammal(Animal):
    def __init__(self, species: str, name: str, age: int, gender: bool, biome: str, diet: str, coat: str, coat_colour: str, **kwargs) -> None:
        super().__init__(family='Mammal', species=species, name=name, age=age, gender=gender, biome=biome, diet=diet, **kwargs)
        self.__coat = coat
        self.__coat_colour = coat_colour

class Reptile(Animal):
    def __init__(self, species: str, name: str, age: int, gender: bool, biome: str, diet: str, skin: str, skin_colour: str, **kwargs) -> None:
        super().__init__(family='Reptile', species=species, name=name, age=age, gender=gender, biome=biome, diet=diet, **kwargs)
        self.__skin = skin
        self.__skin_colour = skin_colour

class Bird(Animal):
    def __init__(self, species: str, name: str, age: int, gender: bool, biome: str, diet: str, fly: str, wing_span: int, **kwargs) -> None:
        super().__init__(family='Bird', name=name, age=age, gender=gender, species=species, biome=biome, diet=diet, **kwargs)
        if fly:
            self.__fly = True
        else:
            self.__fly = False
        self.__wing_span = wing_span

def create_animal(**kwargs) -> Animal:
    families = {
        'Mammal': Mammal,
        'Reptile': Reptile,
        'Bird' : Bird
    }
    habitats = ['Salt water', 'Fresh water', 'Alpine', 'Savannah', 'Rain forest', 'Woods', 'Mountains']
    diets = ['Herbivore', 'Carnivore', 'Omnivore']
    animal_family = input("Enter the animal family (Mammal, Reptile, or Bird): ").strip().lower().capitalize()
    while animal_family not in families:
        animal_family = input(f"Animal family {animal_family} not found. Must be one of Mammal, Reptile, or Bird: ").strip().lower().capitalize()
    species = input("Species: ").strip().lower().capitalize()
    name = input("Name: ").strip().lower().capitalize()
    while True:
        try:
            age = int(input("Age: "))
            break
        except ValueError:
            print("Age must be an integer.")
    gender = input("Gender (Male/Female): ").strip().lower().capitalize()
    while gender not in ['Male', 'Female']:
        gender = input("Please enter either Male or Female: ").strip().lower().capitalize()
    habitat = input(f"Habitat - choose from {habitats}: ").strip().lower().capitalize()
    while habitat not in habitats:
        habitat = input(f"Habitat must be from {habitats}: ").strip().lower().capitalize()
    diet = input(f"Diet (Herbivore, Carnivore, or Omnivore): ").strip().lower().capitalize()
    while diet not in diets:
        diet = input(f"Diet must be from {diets}: ").strip().lower().capitalize()
    if animal_family == 'Mammal':
        coat = input("Coat or Fur: ").strip().lower().capitalize()
        while coat not in ['Coat', 'Fur']:
            coat = input("Please enter either Coat or Fur: ").strip().lower().capitalize()
        coat_colour = input("What colour is the coat/ fur: ").strip().lower().capitalize()
    if animal_family == 'Reptile':
        skin = input("Does the reptile have Scales or Plates: ").strip().lower().capitalize()
        while skin not in ['Scales', 'Plates']:
            skin = input("Please enter either Scales or Plates: ").strip().lower().capitalize()
        skin_colour = input("What colour are the Scales or Plates: ").strip().lower().capitalize()
    if animal_family == 'Bird':
        fly = input('Is the bird Flying or Flightless: ').strip().lower().capitalize()
        while fly not in ['Flying', 'Flightless']:
            fly = input('Please enter either Flying or Flightless: ').strip().lower().capitalize()
        while True:
            try:
                wing_span = int(input("Please enter the wing span in cm: ").strip().lower())
                break
            except ValueError:
                print("Wing span must be an integer.")
    if animal_family == 'Mammal':
        return families[animal_family](species=species, name=name, age=age, gender=gender, biome=habitat, diet=diet, coat=coat, coat_colour=coat_colour)
    elif animal_family == 'Reptile':
        return families[animal_family](species=species, name=name, age=age, gender=gender, biome=habitat, diet=diet, skin=skin, skin_colour=skin_colour)
    elif animal_family == 'Bird':
        return families[animal_family](species=species, name=name, age=age, gender=gender, biome=habitat, diet=diet, fly=fly, wing_span=wing_span)

animal1 = Mammal('Koala', 'George', 1, True, 'Woods', 'Herbivore', 'Skin', 'Blue')
animal2 = Mammal('Koala', 'Paul', 2, False, 'Rainforest', 'Herbivore', 'Fur', 'Blue')
animal3 = Mammal('Koala', 'Ringo', 3, True, 'Woods', 'Herbivore', 'Skin', 'Blue')
print(Animal.display_animals())
print(Animal.display_animals())