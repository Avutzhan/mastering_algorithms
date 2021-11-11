import unittest
import recursion.main
from parameterized import parameterized


class TestRecursion(unittest.TestCase):
    @parameterized.expand([
        ["test_1", 5, 120],
        ["test_2", 6, 720]
    ])
    def test_factorial(self, name, data, expected):
        """
        Test that it can insert sort array
        :param name: string
        :param data: list
        :param expected: list
        """
        result = recursion.main.factorial(data)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
