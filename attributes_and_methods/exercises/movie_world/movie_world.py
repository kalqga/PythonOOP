class MovieWorld:

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    def __repr__(self):
        result = ''
        for customer in self.customers:
            result += f"{customer.__repr__()}\n"
        for dvd in self.dvds:
            result += f"{dvd.__repr__()}\n"
        return result

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        current_dvd = [d for d in self.dvds if dvd_id == d.id][0]
        current_customer = [c for c in self.customers if customer_id == c.id][0]
        if current_customer.age < current_dvd.age_restriction:
            return f"{current_customer.name} should be at least {current_dvd.age_restriction} " \
                   f"to rent this movie"
        elif current_dvd in current_customer.rented_dvds:
            return f"{current_customer.name} has already rented {current_dvd.name}"
        elif current_dvd.is_rented:
            return "DVD is already rented"
        else:
            current_customer.rented_dvds.append(current_dvd)
            current_dvd.is_rented = True
            return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        current_dvd = [d for d in self.dvds if dvd_id == d.id][0]
        current_customer = [c for c in self.customers if customer_id == c.id][0]
        if current_dvd not in current_customer.rented_dvds:
            return f"{current_customer.name} does not have that DVD"
        current_dvd.is_rented = False
        current_customer.rented_dvds.remove(current_dvd)
        return f"{current_customer.name} has successfully returned {current_dvd.name}"
