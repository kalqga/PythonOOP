class UnsuccessfulInstallException(Exception):
    pass


class Hardware:

    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software):
        if self.capacity < sum(
                [s.capacity_consumption for s in self.software_components]) + software.capacity_consumption \
                or self.memory < sum(
                [s.memory_consumption for s in self.software_components]) + software.memory_consumption:
            raise UnsuccessfulInstallException("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software):
        self.software_components.remove(software)
