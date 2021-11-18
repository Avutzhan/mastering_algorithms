from typing import List


def fib(n):
    """
    Recursive simple and intuitive
    O(F) = O(2^n) or exponential.
    :param n: int
    :return: int
    """
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def dynamic_fib(n):
    """
    Dynamic Programming рекурсия вывернутая наоборот
    В некоторых случаях Динамическое программирование не может быть реализовано
    O(n) linear
    :param n: int
    :return: int
    """
    fb = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fb[i] = fb[i - 1] + fb[i - 2]
    return fb[n]  # last i is result you can return fb[-1]


def trajectories_num(n: int) -> int:
    """
    find trajectories of cricket that can jump with rules
    1) +1
    2) +2
    :param n: int
    :return: int
    """
    k = [0, 1] + [0] * n
    for i in range(2, n + 1):
        k[i] = k[i - 2] + k[i - 1]
    return k[n]


def count_trajectories(n: int, allowed: List[bool]) -> int:
    """
    find trajectories of cricket that can jump with rules
    1) +1
    2) +2
    3) +3
    and there is allowed nums
    :param n: int
    :param allowed: List[bool]
    :return: int
    """
    k = [0, 1, int(allowed[2])] + [0] * (n - 3)
    for i in range(3, n + 1):
        if allowed[i]:
            k[i] = k[i - 1] + k[i - 2] + k[i - 3]
    return k[-1]


def count_min_cost(n, price: list):
    C = [float("-inf"), price[1], price[1] + price[2]] + [0] * (n - 2)
    for i in range(3, n + 1):
        C[i] = price[i] + min(C[i - 1], C[i - 2])
    return C[n]

