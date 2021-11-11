def factorial(num: int):
    if num == 0:
        return 1
    return factorial(num - 1) * num


def gcd(a: int, b: int) -> int:
    """
    greatest common divisor
    euclid's algorithm
    НОД наибольший общий делитель двух чисел
    :param a: int
    :param b: int
    :return: int
    """
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:  # a < b
        return gcd(a, b - a)


def gcd_better(a: int, b: int) -> int:
    """
    greatest common divisor
    euclid's algorithm
    НОД наибольший общий делитель двух чисел
    :param a: int
    :param b: int
    :return: int
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def gcd_one_liner(a: int, b: int) -> int:
    """
    greatest common divisor
    euclid's algorithm
    НОД наибольший общий делитель двух чисел
    :param a: int
    :param b: int
    :return: int
    """

    return a if b == 0 else gcd(b, a % b)


def power(a: float, n: int) -> float:
    if n == 0:
        return 1
    else:
        return power(a, n - 1) * a


def power_better(a: float, n: int) -> float:
    if n == 0:
        return 1
    elif n % 2 == 1:  # не четное
        return pow(a, n - 1) * a
    else:  # n четное
        return power_better(a ** 2, n // 2)
