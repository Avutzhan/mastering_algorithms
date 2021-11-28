import unittest
import ds.stack.main
from parameterized import parameterized


class TestMain(unittest.TestCase):
    @parameterized.expand([
        ["five", "(([()]))[]", True],
        ["seven", "(]", False],
        ["seven", "(", False],
        ["seven", "]", False]
    ])
    def test_check_braces_sequence(self, name, s, expected):
        """
        Test that it can check braces sequence
        :param name: string
        :param s: str
        :param expected: bool
        """
        result = ds.stack.main.check_braces_sequence(s)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
