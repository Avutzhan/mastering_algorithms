import unittest
import search.main
from parameterized import parameterized


# Test Searching Algorithms
class TestSearch(unittest.TestCase):
    @parameterized.expand([
        ["test_1", [1, 2, 3, 4, 5], 4, 3],
        ["test_2", [1, 2, 2, 3], 3, 3]
    ])
    def test_binary_search(self, name, arr, x, expected):
        """
        Test that it can search
        :param name: string
        :param arr: list
        :param x: int
        :param expected: int
        """
        result = search.main.binary_search(arr, x)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
