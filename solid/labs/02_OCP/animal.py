from abc import ABC, abstractmethod


class Animal:
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species


class SoundMakingAnimals(Animal, ABC):
    def __init__(self, species):
        super(SoundMakingAnimals, self).__init__(species)

    @abstractmethod
    def make_sound(self):
        pass


class NotSoundMakingAnimals(Animal, ABC):
    def __init__(self, species):
        super(NotSoundMakingAnimals, self).__init__(species)

    @abstractmethod
    def make_sound(self):
        pass


class Cat(SoundMakingAnimals, ABC):
    def make_sound(self):
        return f"{self.__class__.__name__} goes Meow"


class Dog(SoundMakingAnimals, ABC):
    def make_sound(self):
        return f"{self.__class__.__name__} goes Bark"


class Iguana(NotSoundMakingAnimals):
    def make_sound(self):
        return f"{self.__class__.__name__} don't make sounds"


animals = [Cat('kitten'), Dog('husky'), Iguana('typical')]
for animal in animals:
    print(animal.make_sound())

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
