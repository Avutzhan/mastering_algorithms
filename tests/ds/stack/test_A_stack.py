import unittest
import ds.stack.A_stack
from parameterized import parameterized


class TestAStack(unittest.TestCase):
    @parameterized.expand([
        ["five", 4, 1],
        ["seven", 5, 2]
    ])
    def test_push(self, name, item, expected):
        """
        Test that it can push to stack
        :param name: string
        :param item: int
        :param expected: int
        """
        ds.stack.A_stack.push(item)
        result = len(ds.stack.A_stack._stack)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["four", 4, 4],
        ["ninety", 19, 19],
    ])
    def test_pop(self, name, item, expected):
        """
        Test that it can pop item from stack
        :param name: string
        :param item: int
        :param expected: int
        """
        ds.stack.A_stack.clear()
        ds.stack.A_stack.push(item)
        result = ds.stack.A_stack.pop()
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["two", 2, 0],
        ["three", 3, 0]
    ])
    def test_clear(self, name, item, expected):
        """
        Test that it can clear stack
        :param name: string
        :param item: int
        :param expected: int
        """
        ds.stack.A_stack.clear()
        ds.stack.A_stack.push(item)
        ds.stack.A_stack.clear()
        result = len(ds.stack.A_stack._stack)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ["not found", None, True],
        ["found", 1, False],

    ])
    def test_is_empty_true(self, name, item, expected):
        """
        Test that it can check stack is empty
        :param name: string
        :param item: int
        :param expected: bool
        """
        ds.stack.A_stack.clear()
        if item is not None:
            ds.stack.A_stack.push(item)
        result = ds.stack.A_stack.is_empty()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
