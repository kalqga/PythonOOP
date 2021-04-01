import unittest

from testing.exercises.mammal.project.mammal import Mammal


class MammalTests(unittest.TestCase):
    name = "name"
    type = "type"
    sound = "sound"

    def setUp(self):
        self.mammal = Mammal(self.name, self.type, self.sound)

    def tests_name__when_str__should_work(self):
        result = self.mammal.name
        expected = "name"
        self.assertEqual(expected, result)

    def tests_type__when_str__should_work(self):
        result = self.mammal.type
        expected = "type"
        self.assertEqual(expected, result)

    def tests_sound__when_str__should_work(self):
        result = self.mammal.sound
        expected = "sound"
        self.assertEqual(expected, result)

    def tests_make_sound_method__should_work(self):
        result = self.mammal.make_sound()
        expected = f"name makes sound"
        self.assertEqual(expected, result)

    def tests_kingdom_initial__should_return(self):
        result = self.mammal._Mammal__kingdom
        expected = "animals"
        self.assertEqual(expected, result)

    def tests_get_kingdom_method__should_return_kingdom(self):
        result = self.mammal.get_kingdom()
        expected = "animals"
        self.assertEqual(expected, result)

    def tests_get_info_method__should_work(self):
        result = self.mammal.info()
        expected = f"name is of type type"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
