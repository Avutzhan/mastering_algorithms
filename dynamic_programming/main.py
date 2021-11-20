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
    k = [0, 1] + [0] * (n - 1)
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


def linearize_array(A):
    """
    Линеаризует массив произвольной вложенности не по лучшей практике
    То есть инициализирует пустой массив готовый к линеаризации
    :param A:
    :return:
    """
    result = []
    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            result.append(A[i][j])
            # на самом деле A[i][j] элемент многомерного массива хранится в одномерном в позиции A[i*M+j]
            # было в начале не понятно но после пары тестов понял что A[i*M+j] A одномерный массив
            # i строка в многомерном то есть индекс одного из массивов в родительском массиве
            # M количество элементов в одном из массивов в род массиве
            # j индекс каждого элмента внтури одного из массивов в род массиве
            # пока так тупо не разжевал самому себе не понял если честно что такое A[i*M+j]
            # многомерный [[1, 2], [3, 4], [5, 6]] линейный [1, 2, 3, 4, 5, 6]
            # 1) A[0][0] = 0 * 2 + 0 = A[0]
            # 2) A[0][1] = 0 * 2 + 1 = A[1]

            # 3) A[1][0] = 1 * 2 + 0 = A[2]
            # 4) A[1][1] = 1 * 2 + 1 = A[3]

            # 2) A[2][0] = 2 * 2 + 0 = A[4]
            # 2) A[2][1] = 2 * 2 + 1 = A[5]
    return result


def wrong_list_of_lists(M: list, N: list):
    """
    Список списков N строки M элементы нужно сохдать двумерный массив из двух массивов
    :param M: list
    :param N: list
    :return:
    """
    A = [[0] * len(M)] * len(N)
    return A


def best_list_of_lists(M: list, N: list):
    """
    Список списков N строки M элементы нужно сохдать двумерный массив из двух массивов
    :param M: list
    :param N: list
    :return:
    """
    A = [[0]*len(M) for i in range(len(N))]
    return A


def king_steps(N: int, M: int) -> int:
    """
    Количество маршрутов
    Пусть за один ход королю разрешается передвинуться на одну клетку вниз или вправо. Необходимо определить,
    сколько существует различных маршрутов, ведущих из левого верхнего в правый нижний угол.
    W(a, b) = W(a, b - 1) + W(a - 1, b).
    252 шага потребуется для рекурсии и 36 шагод для динамического программирования
    использует треугольник паскаля в решении посмотри на весь массив в конце работы
    :param N:
    :param M:
    :return:
    """
    # create lis of lists
    K = [[0] * (M + 1) for i in range(N + 1)]
    # initialize values, prepare to work
    for i in range(0, M + 1):
        K[0][i] = 1
    for j in range(0, N + 1):
        K[j][0] = 1
    # work
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            K[i][j] = K[i][j - 1] + K[i - 1][j]

    return K[N][M]


def longest_common_subsequence(A, B):
    F = [[0] * (len(B) + 1) for i in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = 1 + F[i - 1][j - 1]
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])
    return F[-1][-1]


def longest_increasing_subsequence(A, B):
    F = [0] * (len(A) + 1)
    for i in range(1, len(A) + 1):
        maximum = 0
        for j in range(1, i):
            if A[i] > A[j] and F[j] > maximum:
                maximum = F[j]
        F[i] = maximum + 1
    return F[len(A)]
