import unittest
from parameterized import parameterized
from brute_force.main import is_simple_num, factorize_num, square_numbers


class TestMainBruteForce(unittest.TestCase):
    @parameterized.expand([
        ["five", 4, False],
        ["seven", 19, True]
    ])
    def test_is_simple_num(self, name, data, expected):
        """
        Test that it can find out simple number
        :param name: string
        :param data: int
        :param expected: bool
        """
        result = is_simple_num(data)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["four", 4, [2, 2]],
        ["ninety", 19, [19]],
        ["twenty", 20, [2, 2, 5]]
    ])
    def test_factorize_number(self, name, data, expected):
        """
        Test that it can factorize number
        :param name: string
        :param data: int
        :param expected: List[int]
        """
        result = factorize_num(data)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["two", [2, 2], [4, 4]],
        ["three", [3, 3, 3], [9, 9, 9]]
    ])
    def test_square_numbers(self, name, data, expected):
        """
        Test that it can square list of nums
        :param name: string
        :param data: List[int]
        :param expected: List[int]
        """
        result = square_numbers(data)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
