import unittest
from parameterized import parameterized
from one_pass_algorithms.calculate_product import product


class TestCalculateProduct(unittest.TestCase):
    """
    Test that it can calculate product of list of integers with different size
    """
    @parameterized.expand([
        ["five", [1, 2, 3, 4, 5], 120],
        ["six", [1, 2, 3, 4, 5, 6], 720],
        ["seven", [1, 2, 3, 4, 5, 6, 7], 5040],
    ])
    def test_product(self, name, data, expected):
        result = product(data)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
