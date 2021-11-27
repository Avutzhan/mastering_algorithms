import unittest

from algos.one_pass_algorithms.sum_things import simple_sum, simple_sum_short


class TestSumThings(unittest.TestCase):
    def test_simple_sum(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = simple_sum(data)
        self.assertEqual(result, 6)

    def test_simple_sum_short(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = simple_sum_short(data)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
