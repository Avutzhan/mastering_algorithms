from typing import List

import void as void


def is_simple_num(x: int) -> bool:
    """
    Просто́е число́ — натуральное число, имеющее ровно два различных натуральных делителя — единицу и самого себя.
    Другими словами, число x является простым, если оно больше 1 и при этом делится без остатка только на 1 и на x.
    Пример:
    4 не простое число потому что оно делится на 2 а надо чтобы делилось только на 1 и 4
    Решето Эратосфена, Решето Аткина, Числа Мерсенна и тест Люка-Лемера, Теорема Ферма и тест Миллера-Рабина,
    Тест Люка и Тест Baillie–PSW,
    :param x: int
    :return: bool
    """
    divisor = 2

    # пока делитель меньше х то продолжаем цикл
    while divisor < x:
        # print('divisor = ', divisor)
        # если х делится на делитель без остатка то число не простое
        if x % divisor == 0:
            return False
        # если х делится с остатком то продолжаем цикл и проверяем все возможные делители до самого себя
        # например 19 = 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18. 19 цикл завершается мы проверили все
        # и получили True число простое
        # например 4 с первой итерации получаем False потому что 4 % 2 = 0 делится без остатка
        divisor += 1
    return True


def factorize_num(x: int) -> List[int]:
    """
    Раскладывает число на множители

    Делим число на 2 пока она не станет меньше 1
    :return: List[int]
    """

    result = []
    divisor = 2
    while x > 1:
        if x % divisor == 0:
            result.append(divisor)
            x //= divisor
        else:
            divisor += 1
    return result


def square_numbers(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]
    return nums


def array_search(arr: list, num: int, x: int):
    """
    Осуществляет поиск числа х в массиве arr
    от 0 до N-1 индекса вкюительно
    Возвращает индекс элемента x в массиве A
    или -1 если такого нет
    Если в массиве несколько одинкавых элементов
    равных х то вернуть индекс первого
    :param arr:
    :param num:
    :param x:
    :return:
    """
    for k in range(num):
        if arr[k] == x:
            return k
    return -1
