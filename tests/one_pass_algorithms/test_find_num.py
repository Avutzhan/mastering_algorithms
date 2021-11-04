import unittest
from parameterized import parameterized
from one_pass_algorithms.find_num import finder


class TestFindNum(unittest.TestCase):
    @parameterized.expand([
        ["five", [1, 2, 3, 4, 5], 5, True],
        ["seven", [1, 2, 3, 4, 5, 6], 7, False],
        ["two", [1, 2, 3, 4, 5, 6, 7], 2, True],
    ])
    def test_finder(self, name, data, num, expected):
        """
        Test that it can find max value of a list of integers
        :param name: string
        :param data: list[int]
        :param expected: int
        """
        result = finder(data, num)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
