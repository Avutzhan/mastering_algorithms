import unittest
import algos.recursion.main
from parameterized import parameterized


class TestRecursion(unittest.TestCase):
    @parameterized.expand([
        ["test_1", 5, 120],
        ["test_2", 6, 720]
    ])
    def test_factorial(self, name, data, expected):
        """
        Test that it can factorial number
        :param name: string
        :param data: int
        :param expected: int
        """
        result = algos.recursion.main.factorial(data)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", 5, 10, 5],
        ["test_2", 6, 12, 6]
    ])
    def test_gcd(self, name, a, b, expected):
        """
        Test that it can find gcd
        :param name: string
        :param a: int
        :param b: int
        :param expected: int
        """
        result = algos.recursion.main.gcd(a, b)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", 5, 10, 5],
        ["test_2", 6, 12, 6]
    ])
    def test_gcd_better(self, name, a, b, expected):
        """
        Test that it can find gcd
        :param name: string
        :param a: int
        :param b: int
        :param expected: int
        """
        result = algos.recursion.main.gcd_better(a, b)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", 5, 10, 5],
        ["test_2", 6, 12, 6]
    ])
    def test_gcd_one_liner(self, name, a, b, expected):
        """
        Test that it can find gcd
        :param name: string
        :param a: int
        :param b: int
        :param expected: int
        """
        result = algos.recursion.main.gcd_one_liner(a, b)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", 2, 2, 4],
        ["test_2", 3, 3, 27]
    ])
    def test_power(self, name, a, b, expected):
        """
        Test that it can power num
        :param name: string
        :param a: int
        :param b: int
        :param expected: int
        """
        result = algos.recursion.main.power(a, b)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", 2, 2, 4],
        ["test_2", 3, 3, 27]
    ])
    def test_power_better(self, name, a, b, expected):
        """
        Test that it can power num
        :param name: string
        :param a: int
        :param b: int
        :param expected: int
        """
        result = algos.recursion.main.power_better(a, b)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", 3, "A", "B", "C", 7],
        ["test_1", 4, "A", "B", "C", 22]
    ])
    def test_hanoi(self, name, n, a, b, c, expected):
        """
        Test that it can count steps
        :param n: int
        :param a: str
        :param b: str
        :param c: str
        :param expected: int
        """
        result = algos.recursion.main.hanoi(n, a, b, c)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
