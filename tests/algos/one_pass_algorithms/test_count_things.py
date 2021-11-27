import unittest
from parameterized import parameterized
from algos.one_pass_algorithms.count_things import count_nums


class TestCountNums(unittest.TestCase):
    @parameterized.expand([
        ["five", [1, 2, 3, 4, 5], 5],
        ["six", [1, 2, 3, 4, 5, 6], 6],
        ["seven", [1, 2, 3, 4, 5, 6, 7], 7],
    ])
    def test_count_nums(self, name, data, expected):
        """
        Test that it can count a list of integers with different size
        """
        result = count_nums(data)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
