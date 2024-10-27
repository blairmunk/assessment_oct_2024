import datetime
from animals import *

animals = []

def add_animal():
    animal_type = input("Enter animal type (Dog, Cat, Hamster, Horse, Camel, Donkey): ")
    name = input("Enter animal name: ")
    birth_date = input("Enter animal birth date (yyyy-mm-dd): ")
    birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d")

    if animal_type == "Dog":
        animal = Dog(name, birth_date)
    elif animal_type == "Cat":
        animal = Cat(name, birth_date)
    elif animal_type == "Hamster":
        animal = Hamster(name, birth_date)
    elif animal_type == "Horse":
        animal = Horse(name, birth_date)
    elif animal_type == "Camel":
        animal = Camel(name, birth_date)
    elif animal_type == "Donkey":
        animal = Donkey(name, birth_date)
    else:
        print("Invalid animal type.")
        return

    animals.append(animal)
    print(f"Added {animal.get_type()} named {animal.name}.")

def teach_command():
    name = input("Enter animal name: ")
    command = input("Enter command: ")

    for animal in animals:
        if animal.name == name:
            animal.add_command(command)
            print(f"Taught {animal.name} to {command}.")
            return

    print("Animal not found.")

def list_animals():
    animals.sort(key=lambda animal: animal.birth_date)
    for animal in animals:
        print(f"{animal.name} ({animal.get_type()}), born on {animal.birth_date.strftime('%Y-%m-%d')}, knows commands: {', '.join(animal.get_commands())}")

def count_animals():
    print(f"Total animals: {Animals.get_counter()}")
    print(f"Total pet animals: {PetAnimals.get_counter()}")
    print(f"Total pack animals: {PackAnimals.get_counter()}")
