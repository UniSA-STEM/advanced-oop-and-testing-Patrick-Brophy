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
    def __init__(self, biome: str, size: int) -> None:
        self.__id = f"Enclosure.{Enclosure.counter}"
        self.__biome = biome
        self.__is_clean = True
        self.__has_animal = False
        self.__size = f"{size}m\u00b2"
        Enclosure.counter += 1
        enclosure_register[self.__id] = self

    def get_enclosure_id(self) -> str:
        return self.__id
    def get_enclosure_name(self) -> str:
        return self.__biome

    @staticmethod
    def get_enclosure_data():
        enclosure_data = []
        for key, value in enclosure_register.items():
            enclosure_data.append(f"{key:<13}: {value.__biome:<11} {'Clean 'if value.__is_clean else 'Dirty':<9} {value.__size:<8} {value.__has_animal if value.__has_animal else 'Empty'}")
        return "\n".join(enclosure_data)

    def change_enclosure_cleanliness(self):
        if self.__is_clean:
            self.__is_clean = False
        else:
            self.__is_clean = True

