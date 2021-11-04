import unittest
from parameterized import parameterized
from one_pass_algorithms.find_max import maximum


class TestFindMax(unittest.TestCase):
    @parameterized.expand([
        ["five", [1, 2, 3, 4, 5], 5],
        ["six", [1, 2, 3, 4, 5, 6], 6],
        ["seven", [1, 2, 3, 4, 5, 6, 7], 7],
    ])
    def test_maximum(self, name, data, expected):
        """
        Test that it can find max value of a list of integers
        :param name: string
        :param data: list[int]
        :param expected: int
        """
        result = maximum(data)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
