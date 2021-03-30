import unittest

from testing.labs.List.extended_list import IntegerList


class IntegerListTests(unittest.TestCase):

    def test_add_to_list__when_int__expect_to_add_it(self):
        integer_list = IntegerList()
        internal_list = integer_list.add(1)
        self.assertEqual([1], internal_list)

    def test_add_to_list__when_str__raise_value_error(self):
        integer_list = IntegerList()
        with self.assertRaises(ValueError):
            integer_list.add("asd")

    def test_remove_element_on_index__when_index_valid__expect_to_remove_it(self):
        value_to_be_removed = 4
        integer_list = IntegerList(1, 2, 3, value_to_be_removed)
        result = integer_list.remove_index(3)
        self.assertEqual(value_to_be_removed, result)
        self.assertListEqual([1, 2, 3], integer_list.get_data())

    def test_remove_element_on_index__when_index_negative_out_of_range__expect_to_raise_index_error(self):
        integer_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(IndexError):
            integer_list.remove_index(-5)

    def test_remove_element_on_index__when_index_positive_out_of_range__expect_to_raise_index_error(self):
        integer_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(IndexError):
            integer_list.remove_index(5)

    def test_initialize_method__when_integers__expect_to_store_them(self):
        IntegerList(1, 2, 3, 4)

    def test_get_element_on_index__when_index_valid__expect_to_get_it(self):
        value_to_get = 3
        integer_list = IntegerList(1, 2, value_to_get)
        result = integer_list.get(2)
        self.assertEqual(value_to_get, result)

    def test_get_element_on_index__when_index_negative_out_of_range__expect_to_raise_index_error(self):
        integer_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError):
            integer_list.get(-5)

    def test_get_element_on_index__when_index_positive_out_of_range__expect_to_raise_index_error(self):
        integer_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError):
            integer_list.get(5)

    def test_insert_element_on_index__when_index_valid__expect_to_insert_it(self):
        value_to_insert = 3
        index = 2
        integer_list = IntegerList(1, 2, 4, 4)
        integer_list.insert(index, value_to_insert)
        self.assertEqual(index, integer_list.get_index(value_to_insert))
        self.assertEqual(value_to_insert, integer_list.get(index))

    def test_insert_element_on_index__when_index_negative_out_of_range__expect_to_raise_index_error(self):
        integer_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError):
            integer_list.insert(-5, 5)

    def test_insert_element_on_index__when_index_positive_out_of_range__expect_to_raise_index_error(self):
        integer_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError):
            integer_list.insert(5, 5)

    def test_insert_element_on_index__when_value_not_integer__expect_to_raise_value_error(self):
        integer_list = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError):
            integer_list.insert(1, 'asd')

    def test_get_biggest__expect_to_return_biggest_element(self):
        integer_list = IntegerList(1, 2, 15, 3)
        result = integer_list.get_biggest()
        self.assertEqual(15, result)

    def test_get_index__expected_to_return_index_of_element(self):
        integer_list = IntegerList(1, 2, 3)
        result = integer_list.get_index(3)
        self.assertEqual(2, result)


if __name__ == '__main__':
    unittest.main()
