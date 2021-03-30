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
        pass

    def test_model_called__when_using_valid_parameters__should_work(self):
        pass

    def test_model_called__when_model_is_none__should_raise_exception(self):
        pass

    def test_fuel_consumption__when_more_than_zero__should_work(self):
        pass

    def test_fuel_consumption__when_zero__should_raise_exception(self):
        pass

    def test_fuel_consumption__when_negative__should_raise_exception(self):
        pass

    def test_fuel_capacity__when_more_than_zero__should_work(self):
        pass

    def test_fuel_capacity__when_zero__should_raise_exception(self):
        pass

    def test_fuel_capacity__when_negative__should_raise_exception(self):
        pass

    def test_fuel_amount__when_more_than_zero__should_work(self):
        pass

    def test_fuel_amount__when_zero__should_work(self):
        pass

    def test_fuel_amount__when_negative__should_raise_exception(self):
        pass

    def test_refuel__when_fuel_positive_and_has_capacity__should_work(self):
        pass

    def test_refuel__when_fuel_is_zero_and_has_capacity__should_raise_exception(self):
        pass

    def test_refuel__when_fuel_negative_and_has_capacity__should_raise_exception(self):
        pass

    def test_refuel__when_fuel_less_than_capacity__should_add(self):
        pass

    def test_refuel__when_fuel_equals_capacity__should_add(self):
        pass

    def test_refuel__when_fuel_more_than_capacity__should_be_equal(self):
        pass

    def test_drive__when_fuel_needed_less_than_amount__should_decrease(self):
        pass

    def test_drive__when_fuel_needed_equal_to_amount__should_be_zero(self):
        pass

    def test_drive__when_fuel_needed_more_than_amount__should_raise_exception(self):
        pass
