import unittest

from testing.labs.CarManager.car_manager import Car


class CarManagerTests(unittest.TestCase):
    make = 'make'
    model = 'model'
    fuel_consumption = 1
    fuel_capacity = 10

    def test_make_called__when_using_valid_parameters__should_work(self):
        car_manager = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        self.assertEqual(self.make, car_manager.make)

    def test_make_called__when_make_is_none__should_raise_exception(self):
        self.make = None
        with self.assertRaises(Exception):
            Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)

    def test_model_called__when_using_valid_parameters__should_work(self):
        car_manager = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        self.assertEqual(self.model, car_manager.model)

    def test_model_called__when_model_is_none__should_raise_exception(self):
        self.model = None
        with self.assertRaises(Exception):
            Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)

    def test_fuel_consumption__when_more_than_zero__should_work(self):
        self.fuel_consumption = 15
        car_manager = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        self.assertEqual(15, car_manager.fuel_consumption)

    def test_fuel_consumption__when_zero__should_raise_exception(self):
        self.fuel_consumption = 0
        with self.assertRaises(Exception):
            Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)

    def test_fuel_consumption__when_negative__should_raise_exception(self):
        self.fuel_consumption = -5
        with self.assertRaises(Exception):
            Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)

    def test_fuel_capacity__when_more_than_zero__should_work(self):
        self.fuel_capacity = 15
        car_manager = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        self.assertEqual(15, car_manager.fuel_capacity)

    def test_fuel_capacity__when_zero__should_raise_exception(self):
        self.fuel_capacity = 0
        with self.assertRaises(Exception):
            Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)

    def test_fuel_capacity__when_negative__should_raise_exception(self):
        self.fuel_capacity = -5
        with self.assertRaises(Exception):
            Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)

    def test_fuel_amount__when_more_than_zero__should_work(self):
        car_manager = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car_manager.fuel_amount = 5
        self.assertEqual(5, car_manager.fuel_amount)

    def test_fuel_amount__when_zero__should_work(self):
        car_manager = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        self.assertEqual(0, car_manager.fuel_amount)

    def test_fuel_amount__when_negative__should_raise_exception(self):
        car_manager = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car_manager.fuel_amount = -5

    def test_refuel__when_fuel_positive_and_has_capacity__should_work(self):
        car_manager = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car_manager.refuel(5)
        self.assertEqual(5, car_manager.fuel_amount)

    def test_refuel__when_fuel_is_zero_and_has_capacity__should_raise_exception(self):
        car_manager = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car_manager.refuel(0)

    def test_refuel__when_fuel_negative_and_has_capacity__should_raise_exception(self):
        car_manager = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car_manager.refuel(-5)

    def test_refuel__when_fuel_less_than_capacity__should_add(self):
        car_manager = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car_manager.fuel_amount = 3
        car_manager.refuel(5)
        self.assertEqual(8, car_manager.fuel_amount)

    def test_refuel__when_fuel_equals_capacity__should_add(self):
        car_manager = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car_manager.refuel(10)
        self.assertEqual(self.fuel_capacity, car_manager.fuel_amount)

    def test_refuel__when_fuel_more_than_capacity__should_be_equal(self):
        car_manager = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car_manager.refuel(15)
        self.assertEqual(self.fuel_capacity, car_manager.fuel_amount)

    def test_drive__when_fuel_needed_less_than_amount__should_decrease(self):
        car_manager = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car_manager.fuel_amount = 7
        car_manager.drive(500)
        expected = 2
        self.assertEqual(expected, car_manager.fuel_amount)

    def test_drive__when_fuel_needed_equal_to_amount__should_be_zero(self):
        car_manager = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car_manager.fuel_amount = 5
        car_manager.drive(500)
        expected = 0
        self.assertEqual(expected, car_manager.fuel_amount)

    def test_drive__when_fuel_needed_more_than_amount__should_raise_exception(self):
        car_manager = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car_manager.fuel_amount = 7
        with self.assertRaises(Exception):
            car_manager.drive(5000)


if __name__ == '__main__':
    unittest.main()
