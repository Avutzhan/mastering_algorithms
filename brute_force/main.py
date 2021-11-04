def is_simple_num(x: int) -> bool:
    """
    Просто́е число́ — натуральное число, имеющее ровно два различных натуральных делителя — единицу и самого себя.
    Другими словами, число x является простым, если оно больше 1 и при этом делится без остатка только на 1 и на x.
    :param x: int
    :return: bool
    """
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True
