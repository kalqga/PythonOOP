from exam_preparation.sixteen_aug.skeleton.skeleton.project.hardware.hardware import UnsuccessfulInstallException
from exam_preparation.sixteen_aug.skeleton.skeleton.project.hardware.heavy_hardware import HeavyHardware
from exam_preparation.sixteen_aug.skeleton.skeleton.project.hardware.power_hardware import PowerHardware
from exam_preparation.sixteen_aug.skeleton.skeleton.project.software.express_software import ExpressSoftware
from exam_preparation.sixteen_aug.skeleton.skeleton.project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        power_hardware_register = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware_register)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        heavy_hardware_register = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware_register)

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        try:
            hardware = [el for el in System._hardware if el.name == hardware_name][0]
        except IndexError as ex:
            return "Hardware does not exist"

        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)

        try:
            hardware.install(express_software)
            System._software.append(express_software)
        except UnsuccessfulInstallException as ex:
            return "Software cannot be installed"

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        try:
            hardware = [el for el in System._hardware if el.name == hardware_name][0]
        except IndexError as ex:
            return "Hardware does not exist"

        light_software = LightSoftware(name, capacity_consumption, memory_consumption)

        try:
            hardware.install(light_software)
            System._software.append(light_software)
        except UnsuccessfulInstallException as ex:
            return "Software cannot be installed"

    @staticmethod
    def release_software_component(hardware_name, software_name):
        try:
            hardware = [el for el in System._hardware if el.name == hardware_name][0]
            software = [el for el in System._software if el.name == software_name][0]
        except IndexError as ex:
            return "Some of the components do not exist"
        hardware.uninstall(software)

    @staticmethod
    def analyze():
        used_capacity = sum(
            [comp.capacity_consumption for hardware in System._hardware for comp in hardware.software_components]
        )
        total_capacity = sum([hardware.capacity for hardware in System._hardware])
        used_memory = sum(
            [comp.memory_consumption for hardware in System._hardware for comp in hardware.software_components]
        )
        total_memory = sum([hardware.memory for hardware in System._hardware])

        result = "System Analysis\n"
        result += f"Hardware Components: {len(System._hardware)}\n"
        result += f"Software Components: {len(System._software)}\n"
        result += f"Total Operational Memory: {int(used_memory)} / {int(total_memory)}\n"
        result += f"Total Capacity Taken: {int(used_capacity)} / {int(total_capacity)}"

        return result

    @staticmethod
    def system_split():
        result = ''

        for hardware in System._hardware:
            express_software_comps_count = len(
                [comp for comp in hardware.software_components if comp.type == 'Express'])
            light_software_comps_count = len([comp for comp in hardware.software_components if comp.type == 'Light'])
            total_memory_used = sum([comp.memory_consumption for comp in hardware.software_components])
            total_capacity_used = sum([comp.capacity_consumption for comp in hardware.software_components])
            software_components = ', '.join([comp.name for comp in hardware.software_components]) \
                if hardware.software_components else 'None'

            result += f'Hardware Component - {hardware.name}\n' \
                      f'Express Software Components: {express_software_comps_count}\n' \
                      f'Light Software Components: {light_software_comps_count}\n' \
                      f'Memory Usage: {int(total_memory_used)} / {int(hardware.memory)}\n' \
                      f'Capacity Usage: {int(total_capacity_used)} / {int(hardware.capacity)}\n' \
                      f'Type: {hardware.type}\n' \
                      f'Software Components: {software_components}'

        return result