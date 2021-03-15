from abc import ABC

from polymorphism.exercises.wild_farm.animals.animal import Mammal
from polymorphism.exercises.wild_farm.food import Food, Meat, Vegetable, Fruit


class Mouse(Mammal, ABC):
    WEIGHT_INCREASE = 0.10

    def make_sound(self):
        return "Squeak"

    def feed(self, food: Food):
        if isinstance(food, Vegetable) or isinstance(food, Fruit):
            self.food_eaten += food.quantity
            self.weight += food.quantity * Mouse.WEIGHT_INCREASE
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Dog(Mammal, ABC):
    WEIGHT_INCREASE = 0.40

    def make_sound(self):
        return "Woof!"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * Dog.WEIGHT_INCREASE


class Cat(Mammal, ABC):
    WEIGHT_INCREASE = 0.30

    def make_sound(self):
        return "Meow"

    def feed(self, food: Food):
        if isinstance(food, Vegetable) or isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += food.quantity * Cat.WEIGHT_INCREASE
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Tiger(Mammal, ABC):
    WEIGHT_INCREASE = 1.00

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * Tiger.WEIGHT_INCREASE
