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


summary: int = 0


def hanoi(n: int, a: str, b: str, c: str) -> int:
    global summary
    """
    Hanoi Tower Game
    Узнать сколько шагов нужно для решения головоломки с n дисками
    Rules
    * Мы можем перемещать только один диск в любой момент времени
    * Только диск, который находится наверху, может быть перемещен и помещен сверху на любой другой стержень
    * Диск может быть помещен только поверх большего диска

    # Определить функцию с именем Hanoi Tower, сделать три столбца a, b, c, всего n дисков
    :param n: int
    :param a: str
    :param b: str
    :param c: str
    :return: int
    """

    if n > 0:
        hanoi(n - 1, a, b, c)  # n-1 диски перемещаются от a до b к c
        summary += 1
        hanoi(n - 1, c, a, b)  # n-1 диски перемещаются с c через a на b
    return summary
