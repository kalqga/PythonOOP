class Room:

    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people):
        if self.is_taken or self.capacity < people:
            return f"Room number {self.number} cannot be taken"
        self.guests += people
        self.capacity -= people
        self.is_taken = True
        return True

    def free_room(self):
        if self.is_taken:
            self.is_taken = False
            self.capacity += self.guests
            self.guests = 0
            return True
        return f"Room number {self.number} is not taken"
