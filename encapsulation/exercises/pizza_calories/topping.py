class Topping:

    def __init__(self, topping_type, weight):
        self.__topping_type = topping_type
        self.__weight = weight

    @property
    def topping(self):
        return self.__topping_type

    @property
    def weight(self):
        return self.__weight

    @topping.setter
    def topping(self, new_topping):
        self.__topping_type = new_topping

    @weight.setter
    def weight(self, new_weight):
        self.__weight = new_weight
