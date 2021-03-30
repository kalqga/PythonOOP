import unittest

from testing.labs.worker import Worker


class WorkerTests(unittest.TestCase):
    name = "test_name"
    salary = 100
    energy = 5

    def setUp(self):
        self.worker_test = Worker(self.name, self.salary, self.energy)

    def test_when_worker_is_initialized_with_correct_parameters(self):
        self.assertEqual(self.name, self.worker_test.name)
        self.assertEqual(self.salary, self.worker_test.salary)
        self.assertEqual(self.energy, self.worker_test.energy)

    def test_worker_when_rest_is_called__energy_to_be_incremented(self):
        self.worker_test.rest()
        self.assertEqual(self.energy + 1, self.worker_test.energy)

    def test_worker_when_work_is_called_with_no_energy__error_to_be_raised(self):
        self.worker_test.energy = 0
        with self.assertRaises(Exception):
            self.worker_test.work()

    def test_worker_when_work_is_called_with_negative_energy__error_to_be_raised(self):
        self.worker_test.energy = -5
        with self.assertRaises(Exception):
            self.worker_test.work()

    def test_worker_money_increased_by_salary__work_called(self):
        self.worker_test.work()
        self.assertEqual(self.salary, self.worker_test.money)

    def test_worker_energy_decreased__work_called(self):
        self.worker_test.work()
        self.assertEqual(self.energy - 1, self.worker_test.energy)

    def test_worker_get_info__to_return_correct_values(self):
        expected = f'{self.name} has saved 0 money.'
        self.assertEqual(expected, self.worker_test.get_info())


if __name__ == '__main__':
    unittest.main()
