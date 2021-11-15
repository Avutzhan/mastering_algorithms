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


if __name__ == '__main__':
    unittest.main()
