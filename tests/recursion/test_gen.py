import unittest
import recursion.gen
from parameterized import parameterized


class TestGen(unittest.TestCase):
    @parameterized.expand([
        ["test_1", 3, ['000', '001', '010', '011', '100', '101', '110', '111']],
        ["test_1", 2, ['00', '01', '10', '11']]
    ])
    def test_gen_bin_recursive(self, name, n, expected):
        """
        Test that it can generate numbers
        :param name: str
        :param n: int
        :param expected: list
        """
        gen = recursion.gen.Gen()
        gen.clear_data()
        result = gen.gen_bin_recursive(n)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", 3, ['000', '001', '010', '011', '100', '101', '110', '111']],
        ["test_1", 2, ['00', '01', '10', '11']],
        ["test_1", 5, ['00000', '00001', '00010', '00011', '00100', '00101', '00110', '00111', '01000', '01001',
                       '01010', '01011', '01100', '01101', '01110', '01111', '10000', '10001', '10010', '10011',
                       '10100', '10101', '10110', '10111', '11000', '11001', '11010', '11011', '11100', '11101',
                       '11110', '11111']]  # для двоичной системы счисления
    ])
    def test_gen_bin_iterative(self, name, n, expected):
        """
        Test that it can generate numbers
        :param name: str
        :param n: int
        :param expected: list
        """
        gen = recursion.gen.Gen()
        gen.clear_data()
        result = gen.gen_bin_iterative(n)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
