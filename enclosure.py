'''
File: enclosure.py
Description: A brief description of this Python module.
Author: Patrick Brophy
ID: 110070814
Username: bropy009
This is my own work as defined by the University's Academic Integrity Policy.
'''
enclosure_register = {}
class Enclosure:
    counter = 1
    def __init__(self, biome: str, size: str) -> None:
        self.__id = f"Enclosure.{Enclosure.counter}"
        self.__biome = biome
        self.__is_clean = True
        self.__has_animal = False
        self.__size = f"{size}m\u00b2"
        Enclosure.counter += 1
        enclosure_register[self.__id] = self

    @staticmethod
    def display_enclosure_data() -> None:
        print("-" * 25, 'Enclosure Register', "-" * 25)
        print(F"Enclosure ID |     BIOME     | STATUS | SIZE | OCCUPANT")
        for key, value in enclosure_register.items():
            print(f"{key:<13}: {value.__biome:<15} {'Clean 'if value.__is_clean else 'Dirty':<8} {value.__size:<6} {value.__has_animal if value.__has_animal else 'Empty'}")

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
    return Enclosure(biome=biome, size=size)


create_enclosure()
Enclosure.display_enclosure_data()