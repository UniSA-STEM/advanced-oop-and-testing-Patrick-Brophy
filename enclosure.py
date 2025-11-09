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
    def __init__(self, habitat: str, size: int) -> None:
        self.__id = f"Enclosure.{Enclosure.counter}"
        self.__habitat = habitat
        self.__is_clean = True
        self.__has_animal = False
        self.__size = size
        Enclosure.counter += 1
        enclosure_register[self.__id] = self

    def create_enclosure(self) -> None:
