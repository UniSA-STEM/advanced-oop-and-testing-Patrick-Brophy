import pytest
from animal import Mammal, Reptile, animal_register, Bird

def test_animal_register():
    Mammal('Lion', 'Leo', 5, 'Male', 'Savanna', 'Carnivore', 'Mane', 'Gold')
    Reptile('Crocodile', 'Croc', 10, 'Female', 'Swamp', 'Carnivore', 'Scaly', 'Green')
    Bird('Eagle', 'Edna', 2, 'Female', 'Mountain', 'Carnivore', 'Flight', 200)
    return animal_register

class TestAnimal:
    def __init__(self, animal_id, health, status):
        self._animal_id = animal_id
        self._health = health
        self._status = status

        def get_animal_id(self): return self._animal_id
        def get_health(self): return self._health
        def get_status(self): return self._status