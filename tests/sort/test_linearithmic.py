import unittest
import sort.linearithmic
from parameterized import parameterized


# Test Linearithmic Sorting Algorithms
class TestLinearithmicSort(unittest.TestCase):
    @parameterized.expand([
        ["test_1", [1, 2], [3, 4], [1, 2, 3, 4]],
        ["test_2", [1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]]
    ])
    def test_merge(self, name, a, b, expected):
        """
        Test that it can merge two lists
        :param name: string
        :param a: list
        :param b: list
        :param expected: list
        """
        result = sort.linearithmic.merge(a, b)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", [3, 4, 1, 2], [1, 2, 3, 4]],
        ["test_2", [4, 5, 6, 1, 2, 3], [1, 2, 3, 4, 5, 6]]
    ])
    def test_merge_sort(self, name, a, expected):
        """
        Test that it can sort array
        :param name: string
        :param a: list
        :param expected: list
        """
        sort.linearithmic.merge_sort(a)
        self.assertEqual(a, expected)

    @parameterized.expand([
        ["test_1", [3, 4, 1, 2], [1, 2, 3, 4]],
        ["test_2", [4, 5, 6, 1, 2, 3], [1, 2, 3, 4, 5, 6]]
    ])
    def test_quick_sort(self, name, a, expected):
        """
        Test that it can sort array
        :param name: string
        :param a: list
        :param expected: list
        """
        sort.linearithmic.quick_sort(a)
        self.assertEqual(a, expected)


if __name__ == '__main__':
    unittest.main()
