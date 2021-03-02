class PizzaDelivery:
    ordered = False

    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredient, quantity, ingredient_price):
        if self.ordered:
            return self.is_ordered()
        if ingredient not in self.ingredients.keys():
            self.ingredients[ingredient] = quantity
            self.price += ingredient_price * quantity
        else:
            self.ingredients[ingredient] += quantity
            self.price += ingredient_price * quantity

    def is_ordered(self):
        return f"Pizza {self.name} already prepared and we can't make any changes!"

    def remove_ingredient(self, ingredient, quantity, ingredient_price):
        if self.ordered:
            return self.is_ordered()
        elif ingredient not in self.ingredients.keys():
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        else:
            current_quantity = self.ingredients[ingredient]
            if current_quantity < quantity:
                return f"Please check again the desired quantity of {ingredient}!"
            elif current_quantity == quantity:
                self.ingredients[ingredient] = 0
                self.price -= quantity * ingredient_price
            else:
                self.ingredients[ingredient] -= quantity
                self.price -= quantity * ingredient_price

    def make_order(self):
        if self.ordered:
            return self.is_ordered()
        else:
            self.ordered = True
            result = [f'{key}: {value}' for key, value in self.ingredients.items()]
            return f"You've ordered pizza {self.name} prepared with {', '.join(result)} and the price will be {self.price}lv."


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))

