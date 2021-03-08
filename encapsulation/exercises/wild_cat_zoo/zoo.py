class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"
        elif self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {type(animal).__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {type(worker).__name__} hired successfully"

    def fire_worker(self, worker_name):
        if self.workers:
            current_worker = [w for w in self.workers if w.name == worker_name][0]
            if current_worker in self.workers:
                self.workers.remove(current_worker)
                return f"{worker_name} fired successfully"
            return f"There is no {worker_name} in the zoo"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salary = 0
        if self.workers:
            for w in self.workers:
                salary += w.salary
            if salary > self.__budget:
                return "You have no budget to pay your workers. They are unhappy"
            self.__budget -= salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        animals_price = 0
        if self.animals:
            for a in self.animals:
                animals_price += a.get_needs()
            if animals_price > self.__budget:
                return "You have no budget to tend the animals. They are unhappy."
            self.__budget -= animals_price
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        if self.animals:
            result = ""
            result += f"You have {len(self.animals)} animals\n"
            lions = [l for l in self.animals if type(l).__name__ == "Lion"]
            tigers = [t for t in self.animals if type(t).__name__ == "Tiger"]
            cheetahs = [c for c in self.animals if type(c).__name__ == "Cheetah"]
            result += f"----- {len(lions)} Lions:\n"
            if lions:
                for el in lions:
                    result += f"{type(el).__repr__(el)}\n"
            result += f"----- {len(tigers)} Tigers:\n"
            if tigers:
                for el in tigers:
                    result += f"{type(el).__repr__(el)}\n"
            result += f"----- {len(cheetahs)} Cheetahs:\n"
            if cheetahs:
                for el in cheetahs:
                    if el == cheetahs[-1]:
                        result += f"{type(el).__repr__(el)}"
                    else:
                        result += f"{type(el).__repr__(el)}\n"
            return result

    def workers_status(self):
        if self.workers:
            result = ""
            result += f"You have {len(self.workers)} workers\n"
            keepers = [k for k in self.workers if type(k).__name__ == "Keeper"]
            caretakers = [c for c in self.workers if type(c).__name__ == "Caretaker"]
            vets = [v for v in self.workers if type(v).__name__ == "Vet"]
            result += f"----- {len(keepers)} Keepers:\n"
            if keepers:
                for el in keepers:
                    result += f"{type(el).__repr__(el)}\n"
            result += f"----- {len(caretakers)} Caretakers:\n"
            if caretakers:
                for el in caretakers:
                    result += f"{type(el).__repr__(el)}\n"
            result += f"----- {len(vets)} Vets:\n"
            if vets:
                for el in vets:
                    if el == vets[-1]:
                        result += f"{type(el).__repr__(el)}"
                    else:
                        result += f"{type(el).__repr__(el)}\n"
            return result
