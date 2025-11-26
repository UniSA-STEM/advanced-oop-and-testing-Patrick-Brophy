# import pytest
# from animal import animal_register, enclosure_register, Mammal, Reptile, Bird, Animal
#
# class TestEnclosure:
#     def __init__(self, enclosure_id = 'Enclosure_1', __is_occupied = False):
#         self.__enclosure_id = enclosure_id
#         self.__is_occupied = __is_occupied
#
#         def get_enclosure_id(self): return self.__enclosure_id
#         def get_is_occupied(self): return self.__is_occupied
#         def set_is_occupied(self):
#             self.__is_occupied = not self.__is_occupied
#             return self.__is_occupied
#
# @pytest.fixture(autouse=True)
# def clear_registers():
#     animal_register.clear()
#     enclosure_register.clear()