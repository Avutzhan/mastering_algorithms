import unittest
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
        result = algos.sort.linear.counting_sort(data)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", [1, 2, 3, 4, 5], True, True],
        ["test_2", [4, 3, 2, 1], False, True]
    ])
    def test_check_sorted(self, name, data, flag, expected):
        """
        Test that it can check sorted
        :param name: string
        :param data: list
        :param flag: bool
        :param expected: bool
        """
        result = algos.sort.linear.check_sorted(data, flag)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
