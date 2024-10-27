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