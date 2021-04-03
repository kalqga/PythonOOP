from exam_preparation.sixteen_aug.skeleton.skeleton.project.hardware.hardware import Hardware


class HeavyHardware(Hardware):

    TYPE = "Heavy"

    def __init__(self, name, capacity, memory):
        super().__init__(name, HeavyHardware.TYPE, int(capacity * 2), int(memory * 0.75))

