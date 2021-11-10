import unittest
import sort.linear
from parameterized import parameterized


# Test Linear Sorting Algorithms
class TestLinearSort(unittest.TestCase):
    @parameterized.expand([
        ["test_1", [4, 2, 5, 1, 3], [1, 2, 3, 4, 5]],
        ["test_2", [4, 2, 1, 3], [1, 2, 3, 4]]
    ])
    def test_counting_sort(self, name, data, expected):
        """
        Test that it can insert sort array
        :param name: string
        :param data: list
        :param expected: list
        """
        result = sort.linear.counting_sort(data)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
