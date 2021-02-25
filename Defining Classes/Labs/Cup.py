class Cup:

    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def free_space(self):
        return self.size - self.quantity

    def fill(self, milliliters):
        if self.free_space() - milliliters >= 0:
            self.quantity += milliliters

    def status(self):
        return self.free_space()


cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())
