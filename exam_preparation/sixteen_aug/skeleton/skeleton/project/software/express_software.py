from exam_preparation.sixteen_aug.skeleton.skeleton.project.software.software import Software


class ExpressSoftware(Software):
    TYPE = "Express"

    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, ExpressSoftware.TYPE, int(capacity_consumption), int(memory_consumption * 2))
