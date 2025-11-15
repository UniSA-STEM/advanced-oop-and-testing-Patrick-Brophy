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
        self.__id = f"Enclosure_{Enclosure.counter}"
        self.__biome = biome
        self.__is_clean = True
        self.__occupancy = False
        self.__size = f"{size}m\u00b2"
        Enclosure.counter += 1
        enclosure_register[self.__id] = self

    def get_enclosure_id(self) -> str:
        return self.__id
    def get_enclosure_biome(self) -> str:
        return self.__biome
    def get_occupancy(self) -> bool:
        return self.__occupancy
    def set_occupancy(self, animal_ID = None) -> None:
        if animal_ID is not None:
            self.__occupancy = animal_ID
        else:
            self.__occupancy = False
    def get_is_clean(self) -> bool:
        return self.__is_clean
    def set_is_clean(self) -> None: self.__is_clean = True

    @staticmethod
    def get_dirty_enclosures():
        dirty_enclosures = [enclosure.get_enclosure_id() for enclosure in enclosure_register.values() if enclosure.get_is_clean() is False]
        return dirty_enclosures

    @staticmethod
    def get_enclosure_data():
        enclosure_data = []
        for key, value in enclosure_register.items():
            occupancy = value.get_occupancy() if value.get_occupancy() else 'Empty'
            enclosure_data.append(f"{key:<13}: {value.__biome:<11} {'Clean 'if value.__is_clean else 'Dirty':<9} {value.__size:<8} {occupancy}")
        return "\n".join(enclosure_data)

    @staticmethod
    def enclosure_search():
        search_results = []
        search_term = input("Enter the ID or biome of the enclosure you are searching for: ").strip().lower().capitalize()
        for key, value in enclosure_register.items():
            if search_term in value.get_id() or search_term in value.get_biome():
                search_results.append(f"{value.get_id()}: of the {value.get_biome()} biome is currently {value.get_occupancy()} and {value.get_is_clean()}")
        if not search_results:
            return f"No enclosures matching {search_term} found."
        else:
            results_string = "\n".join(search_results)
            return f"The following enclosures matching '{search_term}' were found:\n {results_string}"


# Enclosure_1 = Enclosure('Woods', 250)
# Enclosure_2 = Enclosure('Woods', 250)
# Enclosure_3 = Enclosure('Woods', 250)
# Enclosure_1.set_is_clean()
# Enclosure_2.set_is_clean()
# Enclosure_3.set_is_clean()
# print(Enclosure.get_dirty_enclosures())

