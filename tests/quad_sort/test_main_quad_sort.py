import unittest
import quad_sort.main
from parameterized import parameterized


class TestQuadSort(unittest.TestCase):
    @parameterized.expand([
        ["test_1", [4, 2, 5, 1, 3], [1, 2, 3, 4, 5]],
        ["test_2", [4, 2, 1, 3], [1, 2, 3, 4]]
    ])
    def test_insert_sort(self, name, data, expected):
        """
        Test that it can insert sort array
        :param name: string
        :param data: list
        :param expected: list
        """
        result = quad_sort.main.insert_sort(data)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", [4, 2, 5, 1, 3], [1, 2, 3, 4, 5]],
        ["test_2", [4, 2, 1, 3], [1, 2, 3, 4]]
    ])
    def test_selection_sort(self, name, data, expected):
        """
        Test that it can select sort array
        :param name: string
        :param data: list
        :param expected: list
        """
        result = quad_sort.main.selection_sort(data)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", [4, 2, 5, 1, 3], [1, 2, 3, 4, 5]],
        ["test_2", [4, 2, 1, 3], [1, 2, 3, 4]]
    ])
    def test_bubble_sort(self, name, data, expected):
        """
        Test that it can bubble sort array
        :param name: string
        :param data: list
        :param expected: list
        """
        result = quad_sort.main.bubble_sort(data)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
