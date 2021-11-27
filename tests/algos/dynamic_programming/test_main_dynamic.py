import unittest
import algos.dynamic_programming.main
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
        result = algos.dynamic_programming.main.fib(n)
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
        result = algos.dynamic_programming.main.dynamic_fib(n)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", 4, 3],
        ["test_2", 5, 5]
    ])
    def test_trajectories_num(self, name, n, expected):
        """
        Test that it can find jump nums
        :param name: string
        :param n: int
        :param expected: int
        """
        result = algos.dynamic_programming.main.trajectories_num(n)
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
        result = algos.dynamic_programming.main.count_trajectories(n, allowed)
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
        result = algos.dynamic_programming.main.count_min_cost(n, allowed)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", [[1, 2], [3, 4]], [1, 2, 3, 4]],
        ["test_2", [[1, 2], [3, 4], [5, 6]], [1, 2, 3, 4, 5, 6]]
    ])
    def test_linearize_array(self, name, A, expected):
        """
        Test that it can linearize array
        :param name: string
        :param A: List[List[int]]
        :param expected: List[int]
        """
        result = algos.dynamic_programming.main.linearize_array(A)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", [1, 2], [3, 4], [[0, 0], [0, 0]]],
        ["test_2", [1, 2, 4], [3, 4, 4], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
    ])
    def test_wrong_list_of_lists(self, name, M, N, expected):
        """
        Test that it can create list of lists
        :param name: string
        :param M: list
        :param N: list
        :param expected: list
        """
        result = algos.dynamic_programming.main.wrong_list_of_lists(M, N)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", [1, 2], [3, 4], True],
        ["test_2", [1, 2, 4], [3, 4, 4], True]
    ])
    def test_wrong_list_of_lists_check_items(self, name, M, N, expected):
        """
        Test that A[0] is A[1] must be True because this is wrong way to create list
        :param name: string
        :param M: list
        :param N: list
        :param expected: bool
        """
        A = algos.dynamic_programming.main.wrong_list_of_lists(M, N)
        result = A[0] is A[1]
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", [1, 2], [3, 4], [[0, 0], [0, 0]]],
        ["test_2", [1, 2, 4], [3, 4, 4], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
    ])
    def test_best_list_of_lists(self, name, M, N, expected):
        """
        Test that it can create list of lists
        :param name: string
        :param M: list
        :param N: list
        :param expected: list
        """
        result = algos.dynamic_programming.main.best_list_of_lists(M, N)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", [1, 2], [3, 4], False],
        ["test_2", [1, 2, 4], [3, 4, 4], False]
    ])
    def test_best_list_of_lists_check_items(self, name, M, N, expected):
        """
        Test that A[0] is A[1] must be False because this is best way to create list
        :param name: string
        :param M: list
        :param N: list
        :param expected: bool
        """
        A = algos.dynamic_programming.main.best_list_of_lists(M, N)
        result = A[0] is A[1]
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", 5, 5, 252],
        ["test_2", 8, 8, 12870]
    ])
    def test_king_steps(self, name, N, M, expected):
        """
        Test that it can count king steps
        :param name: string
        :param N: int
        :param M: int
        :param expected: int
        """
        result = algos.dynamic_programming.main.king_steps(N, M)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", [1, 3, 4, 5, 6, 7], [4, 5], 2],
        ["test_2", [1, 3, 4, 5, 6, 7], [4, 5, 6, 7], 4]
    ])
    def test_longest_common_subsequence(self, name, N, M, expected):
        """
        Test that it can count longest common subsequence
        :param name: string
        :param N: list
        :param M: list
        :param expected: int
        """
        result = algos.dynamic_programming.main.longest_common_subsequence(N, M)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 6],
        ["test_2", [1, 3, 4, 4, 4, 4], 3]
    ])
    def test_longest_increasing_subsequence(self, name, A, expected):
        """
        Test that it can count longest increasing subsequence
        :param name: string
        :param A: list
        :param expected: int
        """
        result = algos.dynamic_programming.main.longest_increasing_subsequence(A)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", "колокол", "молоко", 2],
        ["test_2", "hello world", "bye world!", 6]
    ])
    def test_levenshtein(self, name, A, B, expected):
        """
        Test that it can find out levenshtein distance
        :param name: string
        :param A: str
        :param B: str
        :param expected: int
        """
        result = algos.dynamic_programming.main.levenshtein(A, B)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", "колокол", "молоко", False],
        ["test_2", "world", "world", True]
    ])
    def test_check_strings(self, name, A, B, expected):
        """
        Test that it can check strings
        :param name: string
        :param A: str
        :param B: str
        :param expected: bool
        """
        result = algos.dynamic_programming.main.check_strings(A, B)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", "bbbaaaab", "ab", 6],
        ["test_2", "el-world", "world", 3]
    ])
    def test_search_substring(self, name, s, sub, expected):
        """
        Test that it can find substring in string
        :param name: str
        :param s: str
        :param sub: str
        :param expected: int
        """
        result = algos.dynamic_programming.main.search_substring(s, sub)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", "abcabcd", [0, 0, 0, 1, 2, 3, 0]],
        ["test_2", "abacaba", [0, 0, 1, 0, 1, 2, 3]]
    ])
    def test_prefix_function(self, name, s, expected):
        """
        Test that it can find prefix function
        :param name: str
        :param s: str
        :param expected: list
        """
        result = algos.dynamic_programming.main.prefix(s)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["test_1", "bbbaaaab", "ab", 6],
        ["test_2", "el-world", "world", 3]
    ])
    def test_kmp(self, name, s, sub, expected):
        """
        Test that it can find substring in string
        :param name: str
        :param s: str
        :param sub: str
        :param expected: list
        """
        result = algos.dynamic_programming.main.kmp(sub, s)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
