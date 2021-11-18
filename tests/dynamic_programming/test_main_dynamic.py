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

    @parameterized.expand([
        ["test_1", 4, 3],
        ["test_2", 5, 5]
    ])
    def test_jump_num(self, name, n, expected):
        """
        Test that it can find jump nums
        :param name: string
        :param n: int
        :param expected: int
        """
        result = dynamic_programming.main.trajectories_num(n)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", 4, [False, True, True, False, False], 0],
        ["test_2", 5, [False, True, True, False, True, False], 2]
    ])
    def test_count_trajectories(self, name, n, allowed, expected):
        """
        Test that it can find jump nums
        :param name: string
        :param allowed: List[bool]
        :param n: int
        :param expected: int
        """
        result = dynamic_programming.main.count_trajectories(n, allowed)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", 4, [1, 2, 1, 3, 1], 4],
        ["test_2", 5, [1, 2, 2, 2, 1, 1], 5]
    ])
    def test_count_min_cost(self, name, n, allowed, expected):
        """
        Test that it can find min cost
        :param name: string
        :param allowed: List[bool]
        :param n: int
        :param expected: int
        """
        result = dynamic_programming.main.count_min_cost(n, allowed)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
