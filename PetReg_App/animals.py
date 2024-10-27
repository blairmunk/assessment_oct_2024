import datetime

class Pet:
    _counter = 0

    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
        self.commands = []
        Pet._counter += 1

    def add_command(self, command):
        self.commands.append(command)

    def get_commands(self):
        return self.commands

    @classmethod
    def get_counter(cls):
        return cls._counter

class Dog(Pet):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
        self.type = "Dog"

class Cat(Pet):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
        self.type = "Cat"

class Hamster(Pet):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)
        self.type = "Hamster"

pets = []

def add_pet():
    pet_type = input("Enter pet type (Dog, Cat, Hamster): ")
    name = input("Enter pet name: ")
    birth_date = input("Enter pet birth date (yyyy-mm-dd): ")
    birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d")

    if pet_type == "Dog":
        pet = Dog(name, birth_date)
    elif pet_type == "Cat":
        pet = Cat(name, birth_date)
    elif pet_type == "Hamster":
        pet = Hamster(name, birth_date)
    else:
        print("Invalid pet type.")
        return

    pets.append(pet)
    print(f"Added {pet.type} named {pet.name}.")

def teach_command():
    name = input("Enter pet name: ")
    command = input("Enter command: ")

    for pet in pets:
        if pet.name == name:
            pet.add_command(command)
            print(f"Taught {pet.name} to {command}.")
            return

    print("Pet not found.")

def list_pets():
    pets.sort(key=lambda pet: pet.birth_date)
    for pet in pets:
        print(f"{pet.name} ({pet.type}), born on {pet.birth_date.strftime('%Y-%m-%d')}, knows commands: {', '.join(pet.get_commands())}")

def count_pets():
    print(f"Total pets: {Pet.get_counter()}")

def menu():
    while True:
        print("\n1. Add pet")
        print("2. Teach command")
        print("3. List pets")
        print("4. Count pets")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_pet()
        elif choice == "2":
            teach_command()
        elif choice == "3":
            list_pets()
        elif choice == "4":
            count_pets()
        elif choice == "5":
            break
        else:
            print("Invalid option.")

menu()

