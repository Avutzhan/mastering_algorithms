import unittest
from parameterized import parameterized
from brute_force.main import is_simple_num


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


if __name__ == '__main__':
    unittest.main()
