class Dough:

    def __init__(self, flour_type, baking_technique, weight):
        self.__flour_type = flour_type
        self.__baking_technique = baking_technique
        self.__weight = weight

    @property
    def flour(self):
        return self.__flour_type

    @property
    def baking_technique(self):
        return self.__baking_technique

    @property
    def weight(self):
        return self.__weight

    @flour.setter
    def flour(self, new_flour):
        self.__flour_type = new_flour

    @baking_technique.setter
    def baking_technique(self, new_baking_technique):
        self.__baking_technique = new_baking_technique

    @weight.setter
    def weight(self, new_weight):
        self.__weight = new_weight
