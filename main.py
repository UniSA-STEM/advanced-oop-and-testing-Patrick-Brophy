'''
File: filename.py
Description: A brief description of this Python module.
Author: Patrick Brophy
ID: 110070814
Username: bropy009
This is my own work as defined by the University's Academic Integrity Policy.
'''
from enclosure import Enclosure, enclosure_register
from animal import Animal, Mammal, Reptile, Bird, animal_register
from staff import Staff, staff_register, Zookeeper


def create_enclosure() -> Enclosure:
    """Function to create an enclosure. Function is driven by user input and presents a list of the valid responses prior to prompting for input, then validates the user response.
    It asks the user to determine the enclosure biome and size, then adds the object to the enclosure register dictionary with an automatically generated enclosure ID as the dictionary key."""
    biomes = ['Salt water', 'Fresh water', 'Alpine', 'Savannah', 'Rain forest', 'Woods', 'Mountains']
    biome = input(f"Please enter the biome of the new enclosure. Must be one of {biomes}: ").strip().lower().capitalize()
    while biome not in biomes:
        biome = input(f"Please enter a biome from {biomes}: ").strip().lower().capitalize()
    while True:
        try:
            size = int(input("Please enter the size of the new enclosure in square metres: "))
            if size < 1:
                print("Please enter a positive integer")
                continue
            break
        except ValueError:
            print("Please enter a positive number.")
    new_enclosure = Enclosure(biome=biome, size=size)
    print(f"{new_enclosure.get_enclosure_id()} has been created with biome {biome} and size {size}m\u00b2.")
    return new_enclosure

def display_enclosure_data() -> None:
    """Function to display the enclosure data. Function is driven by user input. The function uses an Enclosure class method to compile the data from the Enclosure register dictionary."""
    print("-" * 25, 'Enclosure Register', "-" * 25)
    print(F"Enclosure ID |   BIOME   | STATUS |  SIZE  | OCCUPANT")
    print(Enclosure.get_enclosure_data())

def create_animal(**kwargs) -> Mammal | Reptile | Bird:
    """Function to create a new animal. Function is driven by user input and presents a list of the valid responses prior to prompting for input. Function validate the user response prior
    proceeding. Depending on user input, function prompts user for class specific attributes, then calls the animal parent class __init__ function to create the object and pass the
    class specific attributes to the corresponding child class. The animal object is then stored in the animal register dictionary with an automatically generated animal ID as the dictionary key."""
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
        all_args = {
        'species': species,
        'name': name,
        'age': age,
        'gender': gender,
        'biome': habitat,
        'diet': diet,
        'coat': coat,
        'coat_colour': coat_colour
    }
        new_animal = families[animal_family](**all_args)
        print(f"{new_animal.get_id()}:{name} the {species} of class {animal_family} has been added. They can now be added to an unoccupied enclosure that matches their biome.")
        return new_animal
    elif animal_family == 'Reptile':
        all_args = {
            'species': species,
            'name': name,
            'age': age,
            'gender': gender,
            'biome': habitat,
            'diet': diet,
            'skin': skin,
            'skin_colour': skin_colour
        }
        new_animal = families[animal_family](**all_args)
        print(f"{new_animal.get_id()}:{name} the {species} of class {animal_family} has been added. They can now be added to an unoccupied enclosure that matches their biome.")
        return new_animal
    else:
        all_args = {
            'species': species,
            'name': name,
            'age': age,
            'gender': gender,
            'biome': habitat,
            'diet': diet,
            'fly': fly,
            'wing_span': wing_span
        }
        new_animal = families[animal_family](**all_args)
        print(f"{new_animal.get_id()}:{name} the {species} of class {animal_family} has been added. They can now be added to an unoccupied enclosure that matches their biome.")
        return new_animal

def update_schedule():
    """Function to update the schedule for a selected employee. Function prompts the user to input the employee ID, providing a full list of employees on invalid input.
    On input of a valid employee ID, the user is presented with the current employee schedule for each day, confirms which day of the week they would like to update, update the user schedule,
    and prints a confirmation message with the updated details on completion."""
    employee_id = input("Please enter the full Staff ID of the employee you would like to update (e.g. StaffID.1): ")
    while employee_id not in staff_register:
        employee_id = input("Please enter a valid staff ID: ")
    employee = staff_register[employee_id]
    print(f"{employee_id}: {employee.get_name()} selected.\nCurrent schedule is: ")
    schedule = employee.get_schedule()
    for day, task in (schedule.items()):
        print(f"{day}: {task}")
    day = input('Please enter the day of the week you would like to update: ').strip().lower().capitalize()
    while day not in schedule:
        day = input("Please enter a valid day of the week to update: ").strip().lower().capitalize()
    task = input(f"Please enter the task add to {employee.get_name()}'s schedule: ").strip().lower().capitalize()
    schedule[day] = task
    print(f"Updated schedule for {employee.get_name()} on {day} is {task}")

def assign_animal_to_enclosure():
    """Function to assign and animal to an enclosure. Function first confirms whether animals or enclosures exist, then asks for the ID of the animal, validating the input against the animal
    registry. It then prompts for the enclosure ID to be added and validates whether it is occupied and matches the animal biome. If unoccupied and biome match, it prompts the user if they
    would like to clean the enclosure, calling the clean enclosure function if user confirms. It then updates the enclosure object attributes to reflect it is now occupied and updates
    the animal object with the enclosure ID."""
    if not animal_register:
        print("No animals have been registered. Please create an animal record prior to assigning an enclosure.")
        return
    if not enclosure_register:
        print(f"You must create an enclosure record prior to assigning an animal to an enclosure.")
        return
    while True:
        animal_input = input(f"Please enter the ID of the animal you would like to assign to an enclosure: ").strip().lower().capitalize()
        if animal_input in animal_register:
            animal = animal_register[animal_input]
            break
        else:
            print(f"Please enter a valid animal ID. Current animal list below: \n"
                  f"{Animal.display_animals()}")
    print(f"{animal.get_name()} the {animal.get_species()} can be assigned to an empty enclosure of the {animal.get_biome()} biome.")
    while True:
        enclosure_input = input(f"Please enter the ID of the enclosure you would like to assign {animal.get_name()} to: ").strip().lower().capitalize()
        if enclosure_input not in enclosure_register:
            print(f"Please enter a valid enclosure ID. Current enclosure list below: \n"
                  f"{Enclosure.get_enclosure_data()}")
            continue
        enclosure = enclosure_register[enclosure_input]
        if enclosure.get_occupancy():
            print(f"{enclosure.get_enclosure_id()} is currently occupied. Please select an empty enclosure.")
            continue
        if enclosure.get_enclosure_biome() != animal.get_biome():
            print(f"{enclosure.get_enclosure_id()} is a {enclosure.get_enclosure_biome()} biome, which does not match the animal's required {animal.get_biome()} biome.")
            continue
        break
    if enclosure.get_is_clean() is False:
        choice = input(f"{enclosure.get_enclosure_id()} is currently dirty. Would you like to clean it first? (y/n)")
        if choice.lower() == 'y':
            zookeepers = Zookeeper.display_zookeepers()
            print(f"The below zookeepers are available to clean {enclosure.get_enclosure_id()}.")
            print(zookeepers)
            zookeeper_ids = [_[0] for _ in zookeepers]
            choice = input(f"Enter the ID of the zookeeper you'd like to clean the enclosure: ").strip().lower().capitalize()
            while choice not in zookeeper_ids:
                choice = input(f"Please entera valid zookeeper ID: ").strip().lower().capitalize()
            selected_staff = staff_register[choice]
            selected_staff.clean_enclosure(enclosure)
    animal.set_enclosure_ID(enclosure.get_enclosure_id())
    return f"{animal.get_name()} the {animal.get_species()} has been successfully assigned to {enclosure.get_enclosure_id()}."

def clean_enclosure():
    """Function to clean enclosures. It confirms if there are any dirty enclosures, and if so, prints a list of the dirty enclosures. From there it prompts and validates user input.
    It prompts and validates user to select the employee ID of a zookeeper to conduct the cleaning, updating the enclosure object on completion."""
    dirty_enclosures = Enclosure.get_dirty_enclosures()
    if not dirty_enclosures:
        print("There are currently no dirty enclosures to clean.")
        return
    print(f"The following enclosures are currently dirty:")
    print(dirty_enclosures)
    enclosure_input = input("Please enter the enclosure ID you would like to clean: ")
    while enclosure_input not in enclosure_register or enclosure_register[enclosure_input].is_clean():
        enclosure_input = input(f"Either the enclosure ID is incorrect or the enclosure does not need cleaning.\nPlease enter a valid enclosure ID that requires cleaning.: ")
    print(f"The following zookeepers are currently available to clean:")
    print(Zookeeper.display_zookeepers())
    cleaner_input = input(f"Please enter the staff ID of the zookeeper you'd like to do the cleaning: ").strip().lower().capitalize()
    while cleaner_input not in staff_register or staff_register[cleaner_input].get_occupation() != 'Zookeeper':
        cleaner_input = input(f"Staff ID not found. Please enter a valid zookeeper staff ID: ").strip().lower().capitalize()
    cleaner = staff_register[cleaner_input]
    enclosure = enclosure_register[enclosure_input]
    cleaner.clean_enclosure(enclosure)




# assign_animal_to_enclosure()