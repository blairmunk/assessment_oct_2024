import datetime

class Animals:
    _counter = 0

    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
        self.commands = []
        Animals._counter += 1

    def add_command(self, command):
        self.commands.append(command)

    def get_commands(self):
        return self.commands

    @classmethod
    def get_counter(cls):
        return cls._counter

    def get_type(self):
        return self.__class__.__name__

class PetAnimals(Animals):
    _counter = 0

    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
        PetAnimals._counter += 1

    @classmethod
    def get_counter(cls):
        return cls._counter

class Dog(PetAnimals):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

class Cat(PetAnimals):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

class Hamster(PetAnimals):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

class PackAnimals(Animals):
    _counter = 0

    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
        PackAnimals._counter += 1

    @classmethod
    def get_counter(cls):
        return cls._counter

class Horse(PackAnimals):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

class Camel(PackAnimals):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

class Donkey(PackAnimals):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)

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

def menu():
    while True:
        print("\n1. Add animal")
        print("2. Teach command")
        print("3. List animals")
        print("4. Count animals")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_animal()
        elif choice == "2":
            teach_command()
        elif choice == "3":
            list_animals()
        elif choice == "4":
            count_animals()
        elif choice == "5":
            break
        else:
            print("Invalid option.")

menu()
