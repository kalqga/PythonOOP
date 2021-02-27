class Smartphone:

    def __init__(self, memory):
        self.memory = memory
        self.memory_taken = 0
        self.apps = []
        self.is_on = False

    def power(self):
        self.is_on = not self.is_on
        return self.is_on

    def free_memory(self):
        return self.memory - self.memory_taken

    def install(self, app, app_memory):
        if not self.is_on:
            return f"Turn on your phone to install {app}"

        if app_memory > self.free_memory():
            return f"Not enough memory to install {app}"

        self.apps.append(app)
        self.memory_taken += app_memory
        return f"Installing {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.free_memory()}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
