import unittest

from testing.exercises.vehicle.project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):
    fuel = 10.0
    horse_power = 5.0

    def tests_if_fuel_works(self):
        test_vehicle = Vehicle(self.fuel, self.horse_power)
        result = test_vehicle.fuel
        expected = self.fuel
        self.assertEqual(expected, result)

    def tests_if_capacity_works(self):
        test_vehicle = Vehicle(self.fuel, self.horse_power)
        result = test_vehicle.capacity
        expected = self.fuel
        self.assertEqual(expected, result)

    def tests_if_horse_power_works(self):
        test_vehicle = Vehicle(self.fuel, self.horse_power)
        result = test_vehicle.horse_power
        expected = self.horse_power
        self.assertEqual(expected, result)

    def tests_if_fuel_consumption_works(self):
        test_vehicle = Vehicle(self.fuel, self.horse_power)
        result = test_vehicle.fuel_consumption
        expected = Vehicle.DEFAULT_FUEL_CONSUMPTION
        self.assertEqual(expected, result)

    def tests_drive_method__when_fuel_more_than_fuel_needed__should_work(self):
        test_vehicle = Vehicle(self.fuel, self.horse_power)
        test_vehicle.drive(5)
        result = test_vehicle.fuel
        expected = 3.75
        self.assertEqual(expected, result)

    def tests_drive_method__when_fuel_equal_to_fuel_needed__should_work(self):
        test_vehicle = Vehicle(self.fuel, self.horse_power)
        test_vehicle.drive(8)
        result = test_vehicle.fuel
        expected = 0
        self.assertEqual(expected, result)

    def tests_drive_method__when_fuel_less_than_fuel_needed_should_raise_exception(self):
        test_vehicle = Vehicle(self.fuel, self.horse_power)
        with self.assertRaises(Exception) as result:
            test_vehicle.drive(15)
        self.assertEqual(result.exception.args[0], "Not enough fuel")

    def tests_refuel_method__when_fuel_less_than_capacity__should_work(self):
        test_vehicle = Vehicle(self.fuel, self.horse_power)
        test_vehicle.drive(5)
        test_vehicle.refuel(2)
        result = test_vehicle.fuel
        expected = 5.75
        self.assertEqual(expected, result)

    def tests_refuel_method__when_fuel_equal_to_capacity__should_work(self):
        test_vehicle = Vehicle(self.fuel, self.horse_power)
        test_vehicle.drive(8)
        test_vehicle.refuel(10)
        result = test_vehicle.fuel
        expected = 10
        self.assertEqual(expected, result)

    def tests_refuel_method__when_fuel_more_than_capacity__should_raise_exception(self):
        test_vehicle = Vehicle(self.fuel, self.horse_power)
        with self.assertRaises(Exception) as result:
            test_vehicle.refuel(5)
        self.assertEqual(result.exception.args[0], "Too much fuel")

    def tests_str_method__should_work(self):
        test_vehicle = Vehicle(self.fuel, self.horse_power)
        result = test_vehicle.__str__()
        expected = f"The vehicle has 5.0 " \
                   f"horse power with 10.0 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
