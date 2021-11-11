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
