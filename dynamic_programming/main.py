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
