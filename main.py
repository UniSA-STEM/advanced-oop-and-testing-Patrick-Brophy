'''
File: filename.py
Description: A brief description of this Python module.
Author: Patrick Brophy
ID: 110070814
Username: bropy009
This is my own work as defined by the University's Academic Integrity Policy.
'''
from enclosure import Enclosure
from animal import Animal, Mammal, Reptile, Bird

def create_enclosure() -> Enclosure:
    biomes = ['Salt water', 'Fresh water', 'Alpine', 'Savannah', 'Rain forest', 'Woods', 'Mountains']
    biome = input(f"Please enter the biome of the new enclosure. Must be one of {biomes}: ").strip().lower().capitalize()
    while biome not in biomes:
        biome = input(f"Please enter a biome from {biomes}: ").strip().lower().capitalize()
    while True:
        try:
            size = int(input("Please enter the size of the new enclosure in square metres: "))
            break
        except ValueError:
            print("Please enter a number.")
    new_enclosure = Enclosure(biome=biome, size=size)
    print(f"{new_enclosure.get_enclosure_id()} has been created with biome {biome} and size {size}m\u00b2.")
    return new_enclosure

def display_enclosure_data() -> None:
    print("-" * 25, 'Enclosure Register', "-" * 25)
    print(F"Enclosure ID |    BIOME    | STATUS |  SIZE  | OCCUPANT")
    print(Enclosure.get_enclosure_data())

def create_animal(**kwargs) -> Mammal | Reptile | Bird:
    families = dict(Mammal=Mammal, Reptile=Reptile, Bird=Bird)
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
            fly: str = input('Please enter either Flying or Flightless: ').strip().lower().capitalize()
        while True:
            try:
                wing_span: int = int(input("Please enter the wing span in cm: ").strip().lower())
                break
            except ValueError:
                print("Wing span must be an integer.")
    if animal_family == 'Mammal':
        print(f"{name} the {species} of class {animal_family} has been added. They can now be added to an unoccupied enclosure that matches their biome.")
        return families[animal_family](species=species, name=name, age=age, gender=gender, biome=habitat, diet=diet, coat=coat, coat_colour=coat_colour)
    elif animal_family == 'Reptile':
        print(f"{name} the {species} of class {animal_family} has been added. They can now be added to an unoccupied enclosure that matches their biome.")
        return families[animal_family](species=species, name=name, age=age, gender=gender, biome=habitat, diet=diet, skin=skin, skin_colour=skin_colour)
    else:
        print(f"{name} the {species} of class {animal_family} has been added. They can now be added to an unoccupied enclosure that matches their biome.")
        return families[animal_family](species=species, name=name, age=age, gender=gender, biome=habitat, diet=diet, fly=fly, wing_span=wing_span)

