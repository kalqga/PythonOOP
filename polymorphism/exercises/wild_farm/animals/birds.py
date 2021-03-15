from abc import ABC

from polymorphism.exercises.wild_farm.animals.animal import Bird
from polymorphism.exercises.wild_farm.food import Food, Meat


class Owl(Bird):
    WEIGHT_INCREASE = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * Owl.WEIGHT_INCREASE


class Hen(Bird, ABC):
    WEIGHT_INCREASE = 0.35

    def make_sound(self):
        return "Cluck"

    def feed(self, food: Food):
        self.food_eaten += food.quantity
        self.weight += food.quantity * Hen.WEIGHT_INCREASE
