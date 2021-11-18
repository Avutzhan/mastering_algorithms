import unittest
import dynamic_programming.main
from parameterized import parameterized


# Test Dynamic
class TestDynamic(unittest.TestCase):
    @parameterized.expand([
        ["test_1", 4, 3],
        ["test_2", 5, 5]
    ])
    def test_fib(self, name, n, expected):
        """
        Test that it can find fibonacci
        :param name: string
        :param n: int
        :param expected: int
        """
        result = dynamic_programming.main.fib(n)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", 4, 3],
        ["test_2", 5, 5]
    ])
    def test_dynamic_fib(self, name, n, expected):
        """
        Test that it can find fibonacci
        :param name: string
        :param n: int
        :param expected: int
        """
        result = dynamic_programming.main.dynamic_fib(n)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
