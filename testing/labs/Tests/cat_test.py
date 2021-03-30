import unittest

from testing.labs.cat import Cat


class CatTests(unittest.TestCase):
    name = "Machka"

    def setUp(self):
        self.cat_test = Cat(self.name)

    def test_size_increased__when_eat_called(self):
        self.cat_test.eat()
        self.assertEqual(1, self.cat_test.size)

    def test_cat_is_fed__when_eat_called(self):
        self.cat_test.eat()
        self.assertTrue(self.cat_test.fed)

    def test_cat_eat_when_fed__raise_error(self):
        self.cat_test.eat()
        with self.assertRaises(Exception):
            self.cat_test.eat()

    def test_sleep_when_not_fed__raise_error(self):
        with self.assertRaises(Exception):
            self.cat_test.sleep()

    def test_sleepy__when_sleep_called(self):
        self.cat_test.eat()
        self.cat_test.sleep()
        self.assertFalse(self.cat_test.sleepy)


if __name__ == '__main__':
    unittest.main()
